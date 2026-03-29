# computer-use-stage1-raw-python

이 repo는 `raw Python GUI agent`의 Stage 1 학습 repo입니다.

- 역할: Stage 1 dataset builder
- 기본 base model: `../models/gui-owl-1.5-8b-think-base`
- 기본 출력 포맷: helper-first raw Python
- 데이터 원천: `computer-use-raw-python-agent` loop run artifacts

즉 Stage 1 목표는 `agent <-> executor loop`에서 나온 실행 artifact를 `screen + prompt -> python code` SFT 데이터로 바꾸는 것입니다.

## 목표

1. executor loop artifact를 SFT dataset으로 변환
2. GUI-Owl base를 raw Python code generator 방향으로 학습
3. 이후 RL/recovery stage의 기반 마련

상세 내용은 [STAGE_PROFILE.md](STAGE_PROFILE.md), [docs/DATASET.md](docs/DATASET.md),
[docs/TRAINING_FLOW.md](docs/TRAINING_FLOW.md)에 정리합니다.

## 빠른 시작

```bash
cd /home/kss930/model-projects/gui-owl-8B-think-1.0.0/computer-use-stage1-raw-python

./.venv/bin/python -m computer_use_stage1_raw_python.cli \
  --runs-dir ../computer-use-raw-python-agent/data/runs \
  --output data/raw_python_stage1_sft.jsonl
```
