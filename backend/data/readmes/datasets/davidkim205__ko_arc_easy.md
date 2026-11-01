---
language:
- ko
---

# Korean ARC (Easy)
ai2_arc 영어 데이터셋을 한국어로 번역

https://huggingface.co/datasets/allenai/ai2_arc

## Structure

```jsonl
{
  "id": "Mercury_417466",
  "question": "광합성이 왜 대부분의 먹이그물의 기초인지 가장 잘 설명하는 진술은 무엇입니까?",
  "choices": {
    "text": [
      "햇빛은 거의 모든 생태계의 에너지원입니다.",
      "대부분의 생태계는 물이 아닌 육지에서 발견됩니다.",
      "이산화탄소는 다른 가스보다 더 많이 이용 가능합니다.",
      "모든 생태계의 생산자는 식물입니다."
    ],
    "label": [
      "A",
      "B",
      "C",
      "D"
    ]
  },
  "answerKey": "A"
}
{...}
```

