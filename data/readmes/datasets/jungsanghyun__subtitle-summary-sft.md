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
- youtube
- streaming-summarization
- incremental-summarization
- keyword-extraction
size_categories:
- 1K<n<100K
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.jsonl
  - split: validation
    path: data/validation.jsonl
---

# Subtitle Summary & Keyword — SFT (YouTube)

[`jungsanghyun/subtitle-summary-dataset`](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-dataset)를 SFT 학습용 `messages` 형식으로 가공.

## 형식 (system 없음, 단일 턴)
- 입력(user): `[이전 요약] {last_summary}\n[자막] {5min_script}`
- 출력(assistant): `[요약] {한 문장}\n[키워드] {검색어}` — 라벨 2줄(소형 모델 친화).

| split | examples |
|---|---|
| train | 10,159 |
| validation | 971 |

`chat_template.jinja`(`{% generation %}`)로 assistant만 loss. 파싱 `\[요약\]\s*(.+)` / `\[키워드\]\s*(.+)`.

## 라이선스
`cc-by-nc-4.0`, 연구·비상업.
