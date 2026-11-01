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

# Broadcast Subtitle Summary & Keyword — (LGUplus source, our pipeline)

`HBKenerzai/LGUplus_summary_keyword`의 방송 자막을 우리 형식으로 재구성한 뒤, **우리 파이프라인
(Qwen3-235B-A22B-Instruct-2507-FP8, vLLM, 자막-only)**으로 5분 단위 **누적 요약 + 검색 키워드**를
다시 생성한 데이터셋입니다. 원천 자막·메타 저작권은 원 출처(AI Hub / 방송사)에 있습니다.

## 규모
| split | 회차 | 레코드(5분) |
|---|---|---|
| train | 16,609 | 118,608 |
| validation | 1,846 | 13,177 |
| 합계 | 18,455 | 131,785 |

약 9,025시간 분량 · 요약 길이 중앙값 63자 · 도메인: 생활정보 9528 · 정보/토크 9458 · 퀴즈/게임 8123 · 푸드/요리 7221 · 토론/대담 7040 · 교육/문화예술 6639 · 토크쇼 6198 · 버라이어티쇼/예능 6165 · 경제시사 5516 · 강의/강연 5249 · 교양 5244 · 건강/의학 5236 · 뉴스 5165 · 정치/경제 4946 · 예술/문화 4476 · 시사평론 4011 · 취미 3743 · 도서/교양 3245 · 음악평론 2963 · 스포츠 2688 · 드라마/영화 2647 · 반려동물 1745

### `variant` 필드 (중간 시청 대응)
- `full` (117,246개): 방송 처음부터 누적한 표준 궤적.
- `midstart` (14,539개): **중간부터 시청** 시나리오 증강. 임의 진입점 k를 새 시작(이전 요약=없음)으로 삼아 그 지점부터 누적 요약을 재생성(키워드는 청크 단위라 동일). `start_step`=원 방송 내 진입 스텝, `view_step`=진입 후 상대 스텝(0=cold-start). canonical만 원하면 `variant=='full'` 필터.

## 스키마
`program_name, last_summary, 5min_script`(입력) → `current_summary, current_5min_keyword`(출력) +
`keyword_candidates`(참고) + 메타(`episode_id, domain, media, publisher, date, step, window_start, window_end, n_utt`).
`step`은 0-based. 프롬프트에는 자막만 사용(제목·메타 미사용).

## 로드
```python
from datasets import load_dataset
ds = load_dataset("jungsanghyun/subtitle-summary-lgu")
```
학습용 messages 형식은 [`jungsanghyun/subtitle-summary-lgu-sft`](https://huggingface.co/datasets/jungsanghyun/subtitle-summary-lgu-sft) 참고.

## 라이선스
`cc-by-nc-4.0`, 연구·비상업 용도. 원천(AI Hub `방송 콘텐츠 대화체`) 및 `HBKenerzai/LGUplus_summary_keyword` 약관을 함께 따르세요.
