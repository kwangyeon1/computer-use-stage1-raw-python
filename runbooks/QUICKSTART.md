# Quickstart

```bash
cd /home/kss930/model-projects/gui-owl-8B-think-1.0.0/computer-use-stage1-raw-python
python3 -m venv .venv
./.venv/bin/python -m pip install -e '.[dev]'
```

dataset 생성:

```bash
./.venv/bin/python -m computer_use_stage1_raw_python.cli \
  --runs-dir ../computer-use-raw-python-executor/data/runs \
  --output data/raw_python_stage1_sft.jsonl
```
