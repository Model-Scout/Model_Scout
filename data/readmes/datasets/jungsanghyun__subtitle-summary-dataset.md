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

# Subtitle Summary & Keyword Dataset (YouTube)

국내 방송사 유튜브 자막 기반 **스트리밍(누적) 요약 + 유튜브 검색 키워드** 데이터셋.
방송을 5분 단위로 진행하며, 매 5분마다 (직전 누적 요약 + 새 5분 자막)으로 방송 대표 한 문장 요약을 갱신하고 검색 키워드를 생성합니다.
교사 모델 Qwen3-235B-A22B-Instruct-2507-FP8 (vLLM, 자막-only). `HBKenerzai/LGUplus_summary_keyword`와 동일 스키마.

## 규모
| split | 회차 | 레코드(5분) |
|---|---|---|
| train | 2,641 | 10,159 |
| validation | 294 | 971 |
| 합계 | 2,935 | 11,130 |

약 563시간 · 110개 채널 · 요약 중앙값 58자 · 도메인(유튜브 카테고리): Entertainment 2982 · Travel & Events 2081 · News & Politics 1667 · Education 613 · Film & Animation 249 · Music 212 · Howto & Style 124 · Autos & Vehicles 106

### `variant` 필드 (중간 시청 대응)
- `full` (8,269개): 방송 처음부터 누적한 표준 궤적.
- `midstart` (2,861개): **중간부터 시청** 시나리오 증강. 임의 진입점 k를 새 시작(이전 요약=없음)으로 삼아 그 지점부터 누적 요약을 재생성한 것(키워드는 청크 단위라 동일). 진입점 강건성 학습용. `start_step`=원 방송 내 진입 스텝, `view_step`=진입 후 상대 스텝(0=cold-start). canonical만 원하면 `variant=='full'`로 필터.

## 스키마
`program_name, last_summary, 5min_script`(입력) → `current_summary, current_5min_keyword`(출력) +
`keyword_candidates` + 메타(`episode_id, domain, media, publisher, date, step, window_start, window_end, n_utt`). `step` 0-based.

## 로드
```python
from datasets import load_dataset
ds = load_dataset("jungsanghyun/subtitle-summary-dataset")
```
학습용 messages 형식: [`jungsanghyun/subtitle-summary-sft`](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-sft).

## 라이선스 / 유의
자막 원 저작권은 각 방송사/채널에 있습니다. 연구·비상업 용도(`cc-by-nc-4.0`). `domain`은 유튜브 카테고리 원본이라 부정확할 수 있음.
