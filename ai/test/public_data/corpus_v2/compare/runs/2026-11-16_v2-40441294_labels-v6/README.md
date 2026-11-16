# 기준선: v2 고정본 40441294 + 골든셋 v6

> **대체됨:** 같은 날 검토에서 고친 점(자동 검사의 'API만 = 파일 미제공' 규칙, OA-15531 설명 불일치 표시)을 반영한 [2026-11-16_v2-cca4cfd4_labels-v6](../2026-11-16_v2-cca4cfd4_labels-v6/README.md)가 현재 기준선입니다. 이 폴더는 기록으로만 남깁니다(이 실행에 쓴 라벨은 LF 기준 sha256 `9f33017fad4d06b9…`로 지금의 v6와 다릅니다).

이 기준선은 검색 설정을 바꾸지 않은 상태로 쟀습니다. 이후 실험(에이전트, Pre-retrieval 등)과 비교하는 출발점입니다.

## 조건

| 항목 | 값 |
|---|---|
| 코퍼스 | v2 `data_version 40441294f66875a6`. 고정 기록은 [data_version.json](../../../data_version.json) |
| 그래프 | `corpus_id e29561500a725299` |
| 검색 문서 | `documents_id 40441294f66875a6` (41,144청크) |
| 벡터 | 로컬 `embeddings.npy`. `vectors_sha256 cfc16b0c8e1aacb3`, text-embedding-3-small |
| 라벨 | [batch5/labels_llm_v6.jsonl](../../../golden_prep/batch5/labels_llm_v6.jsonl) (LF 기준 sha256 `9f33017fad4d06b9…`, 커밋 9654771c의 파일) |
| 질의 벡터 | `compare/query_vectors.jsonl`. 새로 만든 벡터 0개 |
| 검색 설정·중복 목록 | `run.json`, `aliases.json` (각 파일의 sha256 포함) |

## 결과 (`score_v6.txt`)

공통 질문 53문항 기준입니다.

| | P@10 | R@10 | MRR | nDCG | P2@10 | MRR2 | judged@10 |
|---|---|---|---|---|---|---|---|
| raw | 0.48 | 0.61 | 0.86 | 0.66 | 0.16 | 0.54 | 0.88 |
| condensed (미판정 제외) | 0.49 | 0.62 | 0.86 | 0.67 | 0.16 | 0.54 | |

- **질문 구성:** 전체 58개 = 추천 53 + 기권 5.
  - 지표는 추천 53개로 계산합니다.
  - 기권 3개(p039, p042, p043)는 상위 10에 든 판정 데이터 수로 따로 봅니다.
  - p040, p041은 평가에서 뺍니다. 둘 다 기권 질문인데 보류가 2건씩 남아 있습니다.
- **상위 10 결과의 분모:** 결과가 10개보다 적은 질문이 7개라서(8개 2, 5개 1, 4개 1, 3개 1, 1개 2) 질문 수 × 10과 다릅니다.

| 질문 | 질문 수 | 상위 10 결과 | 관련(1·2) | 0점 | 제외 | 보류 | 완전 미판정 |
|---|---|---|---|---|---|---|---|
| 추천 | 53 | 504 | 256 | 181 | 31 | 7 (1.4%) | 29 (5.8%) |
| 기권(평가) | 3 | 21 | 0 | 19 | 1 | 0 | 1 |
| 기권(평가 제외) | 2 | 15 | 0 | 6 | 2 | 3 | 4 |
| 합계 | 58 | 540 | 256 | 206 | 34 | 10 | 34 (6.3%) |

- **judged@10 0.88:** 추천 53문항의 판정된 결과(관련 + 0점 + 제외 = 468)를 53 × 10 = 530칸으로 나눈 값입니다. 보류와 빈 칸(결과가 10개 미만인 질문의 26칸)은 판정되지 않은 것으로 셉니다.
- **보류:** 공식 확인을 기다리는 쌍이라 맞음·틀림으로 세지 않습니다. 완전 미판정은 아직 판정 기록이 없는 쌍입니다.

## 다시 재기

```
# ai/ 에서. 코퍼스가 고정본과 같은지 먼저 확인
python public_v2_pipeline.py --verify-pin
python test/public_data/corpus_v2/compare_corpora.py run --corpus v2 --dir <새 폴더> \
  --labels test/public_data/corpus_v2/golden_prep/batch5/labels_llm_v6.jsonl
python test/public_data/corpus_v2/compare_corpora.py score --dir <새 폴더> \
  --labels test/public_data/corpus_v2/golden_prep/batch5/labels_llm_v6.jsonl
```

- `embeddings.npy`는 git에 없습니다. 전달받은 파일을 쓰거나, v2 DB가 이 고정본으로 적재된 뒤에는 `python 20_sync_dataset_index.py --corpus v2 --restore-vectors`로 복원합니다.
- 실행 폴더는 덮어쓰지 않습니다. 다른 라벨로 재채점할 때 질문(검색 입력)이 다르면 멈추고 새 폴더를 쓰라고 안내합니다.
