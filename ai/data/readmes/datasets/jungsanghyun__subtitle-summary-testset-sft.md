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
- evaluation
- test
- keyword-extraction
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test.jsonl
---

# Subtitle Summary & Keyword — Test set SFT (YouTube)

[`jungsanghyun/subtitle-summary-testset`](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-testset)를 `messages` 형식으로 가공한 **평가용** 버전.

## 형식 (system 없음, 단일 턴)
- 입력(user): `[이전 요약] {last_summary}\n[자막] {5min_script}`
- 출력(assistant): `[요약] {한 문장}\n[키워드] {검색어}`

| split | examples |
|---|---|
| test | 519 |

파싱 `\[요약\]\s*(.+)` / `\[키워드\]\s*(.+)`. `chat_template.jinja` 동봉.

## 라이선스
`cc-by-nc-4.0`, 연구·비상업.
