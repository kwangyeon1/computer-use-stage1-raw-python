# Training Flow

## 1. code generation loop 수집

- `computer-use-raw-python-agent`가 prompt와 policy를 보유하고 loop를 소유
- `computer-use-raw-python-executor`가 현재 상태와 실행 결과를 endpoint로 반환

## 2. loop artifacts -> SFT JSONL

- 이 repo가 artifact를 JSONL로 변환

## 3. GUI-Owl Stage 1 학습

- default base model:
  - `../models/gui-owl-1.5-8b-think-base`
- 목표:
  - `screen + prompt -> python code`

## 4. 다음 단계

- reward signal 정의
- loop success/failure scoring
- trajectory preference data
- recovery-aware dataset
- longer-horizon code blocks
- verification transcript 추가
