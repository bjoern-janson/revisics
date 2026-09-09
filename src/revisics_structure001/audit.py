from __future__ import annotations
from hashlib import sha256
from typing import Iterable
from .encoding import canonical_encode
from .identity import sha256_hex
from .model import AuditManifest,TypedCountRecord

def _leaf_hash(record,ledger_tag): return sha256(b"structure001-leaf-v1\0"+ledger_tag.encode("ascii")+b"\0"+record).digest()
def _node_hash(left,right): return sha256(b"structure001-node-v1\0"+left+right).digest()
def _empty_tree_digest(tag): return sha256(b"structure001-empty-v1\0"+tag.encode("ascii")).digest()
def _final_root(tree_digest,tag,count): return sha256(b"structure001-root-v2\0"+tag.encode("ascii")+b"\0"+str(count).encode("ascii")+b"\0"+tree_digest).hexdigest()
def merkle_root_sorted(records:Iterable[bytes],ledger_tag:str)->str:
    stack={}; count=0; last_leaf=None
    def add_leaf_hash(value):
        level=0; current=value
        while level in stack: current=_node_hash(stack.pop(level),current); level+=1
        stack[level]=current
    for record in records: last_leaf=_leaf_hash(record,ledger_tag); add_leaf_hash(last_leaf); count+=1
    if count==0: return _final_root(_empty_tree_digest(ledger_tag),ledger_tag,0)
    padded=1<<(count-1).bit_length()
    for _ in range(padded-count): add_leaf_hash(last_leaf)
    if len(stack)!=1: raise AssertionError("Merkle reduction did not produce a single root")
    return _final_root(next(iter(stack.values())),ledger_tag,count)
def merkle_root(records,ledger_tag): return merkle_root_sorted(iter(sorted(records)),ledger_tag)
def build_audit_manifest(manifest_sha,implementation_id,raw_root,canonical_root,validity_root,provenance_root,f5_root,counts): return AuditManifest(manifest_sha,implementation_id,raw_root,canonical_root,validity_root,provenance_root,f5_root,counts)
def audit_bundle_digest(manifest): return sha256_hex(canonical_encode(manifest))
