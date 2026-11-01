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

# Subtitle Summary & Keyword — Test set (YouTube)

방송 유튜브 자막 기반 **누적 요약 + 검색 키워드** 태스크의 **평가용 테스트셋**입니다.
[`jungsanghyun/subtitle-summary-dataset`](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-dataset)의 train/validation과 **겹치지 않는 별도 방송**으로, 동일 파이프라인(Qwen3-235B, vLLM, 자막-only)으로 생성했습니다.

## 규모
| split | 회차 | 레코드(5분) |
|---|---|---|
| test | 114 | 519 |

약 25시간 · 요약 중앙값 59자 · 도메인: Entertainment 236 · News & Politics 103 · Pets & Animals 87 · Travel & Events 34 · Education 31 · Music 28

## 스키마
`program_name, last_summary, 5min_script`(입력) → `current_summary, current_5min_keyword`(출력) + `keyword_candidates` + 메타. `step` 0-based.
```python
from datasets import load_dataset
ds = load_dataset("jungsanghyun/subtitle-summary-testset")   # ds["test"]
```
학습용 messages: [`jungsanghyun/subtitle-summary-testset-sft`](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-testset-sft).

## 라이선스
자막 원 저작권은 각 방송사/채널. 연구·비상업(`cc-by-nc-4.0`).
