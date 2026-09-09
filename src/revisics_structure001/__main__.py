from __future__ import annotations
import argparse,sys
from pathlib import Path
from .model import ControlFailure
from .replay import compare_control_runs,run_control,verify_run_integrity

def build_parser():
    parser=argparse.ArgumentParser(prog="revisics-structure001"); sub=parser.add_subparsers(dest="command",required=True)
    control=sub.add_parser("control-run",help="execute a complete quarantined control run"); control.add_argument("--output",required=True,type=Path); control.add_argument("--implementation-id",required=True)
    verify=sub.add_parser("verify-run",help="recompute and verify one retained control run"); verify.add_argument("run_dir",type=Path)
    compare=sub.add_parser("compare-control-runs",help="verify and compare two control runs"); compare.add_argument("left",type=Path); compare.add_argument("right",type=Path)
    primary=sub.add_parser("primary-universe-run",help="guarded; forbidden before implementation lock"); primary.add_argument("--output",required=True,type=Path); primary.add_argument("--implementation-lock",required=True,type=Path)
    return parser
def main(argv=None):
    try:
        if sys.version_info[:3]!=(3,13,5): raise ControlFailure(control_id="PYTHON_RUNTIME_MISMATCH",expected="3.13.5",observed=".".join(map(str,sys.version_info[:3])))
        args=build_parser().parse_args(argv)
        if args.command=="control-run": result=run_control(args.output,args.implementation_id); print(f"AuditBundle={result.audit_digest}"); return 0
        if args.command=="verify-run": result=verify_run_integrity(args.run_dir); print(f"VERIFIED AuditBundle={result.audit_digest}"); return 0
        if args.command=="compare-control-runs": compare_control_runs(args.left,args.right); print("IDENTICAL VERIFIED CONTROL RUNS"); return 0
        if args.command=="primary-universe-run":
            if not args.implementation_lock.is_file(): raise ControlFailure(control_id="PRIMARY_UNIVERSE_LOCK_REQUIRED",expected="reviewed authorized implementation-lock record",observed=str(args.implementation_lock))
            raise ControlFailure(control_id="PRIMARY_UNIVERSE_NOT_AUTHORIZED",expected="explicit post-review implementation-lock authorization",observed="primary execution remains disabled in this implementation phase")
    except ControlFailure as exc: print(str(exc),file=sys.stderr); return 2
if __name__=="__main__": raise SystemExit(main())
