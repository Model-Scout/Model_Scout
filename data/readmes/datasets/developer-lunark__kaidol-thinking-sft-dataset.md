---
license: apache-2.0
language:
- ko
tags:
- kaidol
- chatbot
- idol
- thinking
- sft
size_categories:
- 10K<n<100K
---

# KAIdol Thinking SFT Dataset (Balanced Upsampled)

아이돌 챗봇 KAI를 위한 SFT 학습 데이터셋입니다.

## 데이터셋 정보

| Split | 샘플 수 |
|-------|---------|
| train | 52,879 |
| test  | 5,875 |

## 데이터 분포 (Balanced)

- **PUSH**: 35% (다가가기)
- **PULL**: 35% (물러서기)
- **NEUTRAL**: 30% (중립)

## 데이터 형식

각 샘플은 다음 필드를 포함합니다:

```json
{
  "messages": [
    {"role": "system", "content": "시스템 프롬프트..."},
    {"role": "user", "content": "사용자 메시지"},
    {"role": "assistant", "content": "<think>사고과정</think>응답"}
  ]
}
```

## 특징

1. **Thinking Process**: `<think>` 태그 내에 구조화된 사고과정 포함
2. **밀당 전략**: PUSH/PULL/NEUTRAL 전략 기반 응답
3. **정책 준수**: 고백 금지, 팬 호칭 금지 등 정책 반영
4. **캐릭터 일관성**: KAI 캐릭터의 성격과 말투 유지

## 사용법

```python
from datasets import load_dataset

dataset = load_dataset("developer-lunark/kaidol-thinking-sft-dataset")
print(dataset)
```

## 라이선스

Apache 2.0
