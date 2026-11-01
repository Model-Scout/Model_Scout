---
language:
- ko
---

# Korean HellaSwag
hellaswag 영어 데이터셋을 한국어로 번역

https://huggingface.co/datasets/Rowan/hellaswag

## Structure
```jsonl
{
  "ind": 24,
  "activity_label": "지붕 슁글 제거",
  "ctx_a": "한 남자가 지붕 위에 앉아 있다.",
  "ctx_b": "그",
  "ctx": "한 남자가 지붕 위에 앉아 있다. 그",
  "endings": [
    "스키 한 켤레를 감싸기 위해 랩을 사용하고 있습니다.",
    "레벨 타일을 뜯어내고 있습니다.",
    "루빅스 큐브를 들고 있습니다.",
    "지붕에 지붕을 올리기 시작합니다."
  ],
  "source_id": "activitynet~v_-JhWjGDPHMY",
  "split": "val",
  "split_type": "indomain",
  "label": "3"
}
{...}
```