from __future__ import annotations

from pathlib import Path
from typing import Iterator
import json


def _iter_run_dirs(runs_dir: str | Path) -> Iterator[Path]:
    root = Path(runs_dir)
    if not root.exists():
        return
    for path in sorted(root.rglob("execution.json")):
        yield path.parent


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_script(run_dir: Path) -> str | None:
    candidates = [
        run_dir / "generated.py",
        run_dir / "artifacts" / "generated_step.py",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")
    py_files = sorted(run_dir.glob("artifacts/*.py"))
    if py_files:
        return py_files[0].read_text(encoding="utf-8")
    return None


def _find_ancestor_file(start_dir: Path, filename: str) -> Path | None:
    current = start_dir
    while True:
        candidate = current / filename
        if candidate.exists():
            return candidate
        if current.parent == current:
            return None
        current = current.parent


def build_sft_records(runs_dir: str | Path) -> list[dict]:
    records: list[dict] = []
    for run_dir in _iter_run_dirs(runs_dir):
        session_path = _find_ancestor_file(run_dir, "session.json")
        execution_path = run_dir / "execution.json"
        if not (session_path and execution_path.exists()):
            continue
        script = _load_script(run_dir)
        if not script:
            continue
        session = _load_json(session_path)
        execution = _load_json(execution_path)
        step_id = str(execution.get("step_id") or run_dir.name)
        user_prompt = str(session.get("user_prompt", ""))
        policy = dict(session.get("policy", {}))
        records.append(
            {
                "id": f"{step_id}:generated",
                "messages": [
                    {
                        "role": "system",
                        "content": "Generate executable Python for the current GUI state. Return code only.",
                    },
                    {
                        "role": "user",
                        "content": (
                            f"User prompt: {user_prompt}\n"
                            f"Policy: {policy.get('policy_name', 'unknown')}"
                        ),
                    },
                    {
                        "role": "assistant",
                        "content": script,
                    },
                ],
                "meta": {
                    "step_id": step_id,
                    "policy_name": policy.get("policy_name", "unknown"),
                    "dataset_mode": "RAW_PYTHON_ACT",
                    "run_dir": str(run_dir),
                },
            }
        )
    return records


def write_jsonl(path: str | Path, records: list[dict]) -> None:
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
