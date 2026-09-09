from __future__ import annotations

from contextlib import ExitStack
from heapq import merge
from pathlib import Path
from typing import Iterable, Iterator

from .model import ControlFailure, ProvenanceEdge, TransportWitness


def _frame_record(payload: bytes) -> bytes:
    return str(len(payload)).encode("ascii") + b":" + payload


def _read_one(handle) -> bytes | None:
    first = handle.read(1)
    if first == b"": return None
    if first < b"0" or first > b"9":
        raise ControlFailure(control_id="LEDGER_FRAMING", expected="ASCII decimal record length", observed=first.decode("ascii", errors="replace"))
    digits=bytearray(first)
    while True:
        byte=handle.read(1)
        if byte==b"": raise ControlFailure(control_id="LEDGER_FRAMING",expected="':' after ASCII decimal record length",observed="unexpected EOF")
        if byte==b":": break
        if byte<b"0" or byte>b"9": raise ControlFailure(control_id="LEDGER_FRAMING",expected="ASCII decimal record length",observed=(bytes(digits)+byte).decode("ascii",errors="replace"))
        digits.extend(byte)
    record_length=int(digits.decode("ascii")); payload=handle.read(record_length)
    if len(payload)!=record_length: raise ControlFailure(control_id="LEDGER_FRAMING",expected=f"{record_length} payload bytes",observed=f"{len(payload)} payload bytes")
    return payload

def iter_framed_records(path:Path)->Iterator[bytes]:
    with path.open("rb") as handle:
        while True:
            record=_read_one(handle)
            if record is None: return
            yield record

def read_framed_records(path:Path)->tuple[bytes,...]: return tuple(iter_framed_records(path))
def _write_sorted_stream(path:Path,records:Iterable[bytes])->None:
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open("wb") as handle:
        for record in records: handle.write(_frame_record(record))
def write_canonical_ledger(path:Path,records:Iterable[bytes])->None: _write_sorted_stream(path,sorted(records))

class ExternalLedgerWriter:
    def __init__(self,final_path:Path,*,chunk_records:int=100_000)->None:
        self.final_path=final_path; self.chunk_records=chunk_records; self.work_dir=final_path.parent/f".{final_path.name}.sort"; self.spool_path=self.work_dir/"spool.bin"; self.work_dir.mkdir(parents=True,exist_ok=True); self._spool=self.spool_path.open("wb"); self._closed=False; self.count=0
    def append(self,record:bytes)->None:
        if self._closed: raise RuntimeError("ledger writer already finalized")
        self._spool.write(_frame_record(record)); self.count+=1
    def _flush_chunk(self,records:list[bytes],index:int)->Path:
        records.sort(); path=self.work_dir/f"chunk-{index:06d}.bin"; _write_sorted_stream(path,records); return path
    def finalize(self)->Path:
        if self._closed: return self.final_path
        self._spool.close(); self._closed=True; chunks=[]; batch=[]; chunk_index=0
        for record in iter_framed_records(self.spool_path):
            batch.append(record)
            if len(batch)>=self.chunk_records: chunks.append(self._flush_chunk(batch,chunk_index)); batch=[]; chunk_index+=1
        if batch: chunks.append(self._flush_chunk(batch,chunk_index))
        self.final_path.parent.mkdir(parents=True,exist_ok=True)
        if not chunks: self.final_path.write_bytes(b"")
        elif len(chunks)==1: chunks[0].replace(self.final_path)
        else:
            with ExitStack() as stack:
                handles=[stack.enter_context(path.open("rb")) for path in chunks]
                def records_from(handle):
                    while True:
                        record=_read_one(handle)
                        if record is None: return
                        yield record
                _write_sorted_stream(self.final_path,merge(*(records_from(h) for h in handles)))
        for path in chunks:
            if path.exists(): path.unlink()
        if self.spool_path.exists(): self.spool_path.unlink()
        try: self.work_dir.rmdir()
        except OSError: pass
        return self.final_path

def raw_to_canonical_edge(manifest_sha,implementation_id,family,raw_id,canonical_id,witness):
    return ProvenanceEdge(manifest_sha,implementation_id,family,raw_id,canonical_id,"RAW_TO_CANONICAL",witness,None,None,None,None)
def canonical_to_assay_edge(manifest_sha,implementation_id,family,canonical_id,assay_id):
    return ProvenanceEdge(manifest_sha,implementation_id,family,canonical_id,assay_id,"CANONICAL_TO_ASSAY",None,None,None,None,None)
def f5_recoding_edge(manifest_sha,implementation_id,base_id,instance_id,recoding_id_value,witness,identity_recoding):
    return ProvenanceEdge(manifest_sha,implementation_id,"F5",base_id,recoding_id_value,"F5_RECODING",witness,base_id,instance_id,recoding_id_value,identity_recoding)
