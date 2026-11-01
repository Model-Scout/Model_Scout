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
- incremental-summarization
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

# LGUplus Broadcast Streaming Summary & Keyword Dataset

한국어 방송 자막 기반 **스트리밍(누적) 요약 + 키워드 추출** 데이터셋입니다.
방송을 5분 단위로 진행하며, 매 5분마다 (직전까지의 요약 + 새 5분 자막)을 받아
**방송 전체를 대표하는 한 문장 요약**으로 갱신하고, 해당 5분의 **핵심 키워드 1개**를 뽑는 태스크를 위해 구축되었습니다.

## 데이터 구조

각 레코드 = 한 방송의 한 5분 구간(step).

| 필드 | 설명 |
|---|---|
| `program_name` | 프로그램명 |
| `last_summary` | 직전 시점까지의 누적 요약 (첫 청크는 `""`) — **입력** |
| `5min_script` | 이번 5분 구간 자막 (`[역할] 발화` 형식) — **입력** |
| `current_summary` | 갱신된 방송 전체 대표 요약 (**한 문장**) — **출력** |
| `current_5min_keyword` | 이번 5분 구간 핵심 키워드 (1개) — **출력** |
| `keyword_candidates` | 키워드 후보(3~5개, 참고용) |
| `episode_id`, `domain`, `media`, `publisher`, `date` | 방송 메타 |
| `step`, `window_start`, `window_end`, `n_utt` | 청크 위치/발화 수 |

학습 입출력:
- **입력**: `{program_name, last_summary, 5min_script}`
- **출력**: `{current_summary, current_5min_keyword}`

## 규모

| | 회차 | 레코드(5분 청크) |
|---|---|---|
| train | 16,326 | 104,010 |
| validation | 2,129 | 13,236 |
| **합계** | **18,455** | **117,246** |

- 실제 방송 콘텐츠 약 **9,000시간** 분량
- 5분 자막 평균 **약 1,620 토큰** (Qwen 토크나이저 기준)
- 요약 평균 **약 68자** (항상 한 문장), 키워드 5분당 1개

## 구축 방법

- **원천**: AI Hub "방송 콘텐츠 대화체 음성인식 데이터" 라벨(전사 + 타임스탬프)을 5분 윈도우로 청킹.
- **교사 모델**: Qwen3-235B-A22B-Instruct-2507-FP8 (vLLM).
- **요약**: recency bias를 피하기 위해 매 step마다 **방송 시작~현재까지의 전체 자막**을 교사 모델에 입력해 균형 잡힌 한 문장 요약을 생성(저장은 incremental 포맷으로 distillation).
- **키워드**: 각 5분 구간에서 추출 후 가장 주목할 1개로 정제.
- **후처리**: 익명 토큰(`&name1&` 등) 자연스럽게 제거.

## 라이선스 / 유의

원천 데이터(AI Hub)의 이용 약관을 따릅니다. 연구/비상업 용도 권장(`cc-by-nc-4.0`). 상업적 사용 시 원천 데이터 라이선스를 확인하세요.

## 로드 예시

```python
from datasets import load_dataset
ds = load_dataset("HBKenerzai/LGUplus_summary_keyword")
print(ds["train"][0])
```
