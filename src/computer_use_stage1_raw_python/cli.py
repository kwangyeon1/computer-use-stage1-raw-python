from __future__ import annotations

import argparse
import json

from .dataset import build_sft_records, write_jsonl


def cmd_build_sft(args: argparse.Namespace) -> int:
    records = build_sft_records(args.runs_dir)
    write_jsonl(args.output, records)
    print(json.dumps({"output": args.output, "records": len(records)}, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="computer-use-stage1-raw-python")
    parser.add_argument("--runs-dir", required=True)
    parser.add_argument("--output", required=True)
    parser.set_defaults(func=cmd_build_sft)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
