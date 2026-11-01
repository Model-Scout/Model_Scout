---
language:
- ko
---

# Korean ARC (Challenge)
ai2_arc 영어 데이터셋을 한국어로 번역

https://huggingface.co/datasets/allenai/ai2_arc

## Structure

```jsonl
{
  "id": "Mercury_7175875",
  "question": "한 천문학자가 운석 충돌 후 행성이 더 빨리 자전하는 것을 관찰했습니다. 이러한 자전 증가의 가장 가능성이 높은 효과는 무엇인가요?",
  "choices": {
    "text": [
      "행성 밀도가 감소합니다.",
      "지구의 해는 더 길어질 것입니다.",
      "지구의 낮이 더 짧아질 것입니다.",
      "행성의 중력이 더 강해질 것입니다."
    ],
    "label": [
      "A",
      "B",
      "C",
      "D"
    ]
  },
  "answerKey": "C"
}
{...}
```

