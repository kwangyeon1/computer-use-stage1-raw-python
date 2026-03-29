# Dataset

## 입력 원천

executor run directory에서 아래 파일을 읽습니다.

- `session.json`
- `execution.json`
- `generated.py`

## 출력 JSONL

```json
{
  "id": "step-000:generated",
  "messages": [
    {
      "role": "system",
      "content": "Generate executable Python for the current GUI state. Return code only."
    },
    {
      "role": "user",
      "content": "User prompt: Chrome을 열고 북마크 관리자 페이지로 이동해줘\nPolicy: unrestricted_local"
    },
    {
      "role": "assistant",
      "content": "import pyautogui\n..."
    }
  ],
  "meta": {
    "step_id": "step-000",
    "policy_name": "unrestricted_local"
  }
}
```

## Stage 1 권장 범위

- helper-first Python
- direct Python call 일부 허용
- recovery transcript는 아직 분리
