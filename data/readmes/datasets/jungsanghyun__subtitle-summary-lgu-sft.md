---
license: cc-by-nc-4.0
language:
- ko
task_categories:
- summarization
- text-generation
tags:
- korean
- broadcast
- streaming-summarization
- keyword-extraction
size_categories:
- 100K<n<1M
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: validation
    path: data/validation.jsonl
---

# Broadcast Subtitle Summary & Keyword — SFT (LGUplus source)

[`jungsanghyun/subtitle-summary-lgu`](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-lgu)를 **SFT 학습용 `messages` 형식**으로 가공한 버전입니다.

## 형식 (system 없음, 단일 턴)
- 입력(user): `[이전 요약] {last_summary}\n[자막] {5min_script}`
- 출력(assistant): `[요약] {한 문장}\n[키워드] {검색어}` — 라벨 2줄(소형 모델 친화·파싱 용이).

| split | examples |
|---|---|
| train | 118,608 |
| validation | 13,177 |

## generation만 학습
`chat_template.jinja`(`{% generation %}` 블록)로 assistant 응답만 loss. TRL `SFTConfig(assistant_only_loss=True, packing=True)`.

## 파싱
```python
import re
def parse(t):
    s=re.search(r'\[요약\]\s*(.+)',t); k=re.search(r'\[키워드\]\s*(.+)',t)
    return (s.group(1).strip() if s else ""), (k.group(1).strip() if k else "")
```
서빙 시 guided decoding `\[요약\] [^\n]+\n\[키워드\] [^\n]+`로 형식 강제 가능.

## 라이선스
`cc-by-nc-4.0`, 연구·비상업. 원천 약관 준수.
