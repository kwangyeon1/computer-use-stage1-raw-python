# Stage 1 Raw Python Profile

이 repo는 raw Python agent 학습의 첫 단계입니다.

## 목표

- loop trajectory 기반 helper-first Python code generation
- executor-specific schema 제거
- unrestricted Python 구조의 base prior 고정
- 이후 reward/trajectory optimization의 기반 마련

## 현재 학습 단위

- one-step or short-step code generation
- loop artifact -> supervised sample 변환
- 이후 RL/reward fine-tuning 확장 예정
- 입력:
  - user prompt
  - policy and recent execution context
  - optional screenshot path
  - optional observation text
- 출력:
  - executable Python code

## 기본 모델

- default base model: `../models/gui-owl-1.5-8b-think-base`

## repo 계보

- dataset source: `../computer-use-raw-python-executor`
- serving pair: `../computer-use-raw-python-agent`
