# 기준선: v2 고정본 aa1a71d3 + 골든셋 v6

이 기준선은 검색 설정을 바꾸지 않은 상태로 쟀습니다. 이후 실험(에이전트, Pre-retrieval 등)과 비교하는 출발점입니다. 코퍼스와 라벨이 이전 기록과 다르므로, 이전 점수와 직접 비교해 개선·악화를 판단하지 않습니다.

> 직전 기준선 [2026-11-16_v2-cca4cfd4_labels-v6](../2026-11-16_v2-cca4cfd4_labels-v6/README.md)와 검색 문서·벡터·라벨이 같고, 79개 질문의 순위와 점수도 모두 같습니다. 고정본 ID가 바뀐 것은 공식 조회 코드(18_enrich, 실패한 상세 페이지 재시도)가 바뀌어 빌드 기록의 코드 해시가 달라졌기 때문입니다. 고정본과 실행 기록의 ID를 맞추려고 새 폴더로 다시 쟀습니다.

## 조건

| 항목 | 값 |
|---|---|
| 코퍼스 | v2 `data_version aa1a71d35a121150`. 고정 기록은 [data_version.json](../../../data_version.json) |
| 그래프 | `corpus_id 3bf5428514e9f798` |
| 검색 문서 | `documents_id aa1a71d35a121150` (41,144청크, `chunks.jsonl`은 cca4cfd4와 같음) |
| 벡터 | 로컬 `embeddings.npy`. `vectors_sha256 8b05f2f9073869ac`, text-embedding-3-small |
| 라벨 | [batch5/labels_llm_v6.jsonl](../../../golden_prep/batch5/labels_llm_v6.jsonl) (sha256 `ad27386f22589784…`, LF 기준) |
| 질의 벡터 | `compare/query_vectors.jsonl`. 새로 만든 벡터 0개 |
| 검색 설정·중복 목록 | `run.json`, `aliases.json` (각 파일의 sha256 포함) |

## 결과 (`score_v6.txt`)

공통 질문 53문항 기준입니다.

| | P@10 | R@10 | MRR | nDCG | P2@10 | MRR2 |
|---|---|---|---|---|---|---|
| raw | 0.48 | 0.61 | 0.86 | 0.66 | 0.16 | 0.54 |
| condensed (미판정·보류 제외) | 0.50 | 0.63 | 0.87 | 0.68 | 0.16 | 0.55 |

- **질문 구성:** 전체 58개 = 추천 53 + 기권 5.
  - 지표는 추천 53개로 계산합니다.
  - 기권 3개(p039, p042, p043)는 상위 10에 든 판정 데이터 수로 따로 봅니다.
  - p040, p041은 평가에서 뺍니다. 둘 다 기권 질문인데 보류가 2건씩 남아 있습니다.
- **상위 10 결과의 분모:** 결과가 10개보다 적은 질문이 7개라서 질문 수 × 10과 다릅니다.

| 질문 | 질문 수 | 상위 10 결과 | 관련(1·2) | 0점 | 제외 | 보류 | 완전 미판정 |
|---|---|---|---|---|---|---|---|
| 추천 | 53 | 504 | 257 | 181 | 24 | 13 (2.6%) | 29 (5.8%) |
| 기권(평가) | 3 | 21 | 0 | 19 | 1 | 0 | 1 |
| 기권(평가 제외) | 2 | 15 | 0 | 6 | 2 | 3 | 4 |
| 합계 | 58 | 540 | 257 | 206 | 27 | 16 | 34 (6.3%) |

- **판정률:**
  - judged@10 0.87: 추천 53문항의 판정된 결과(관련 + 0점 + 제외 = 462)를 530칸(53 × 10)으로 나눈 값입니다. 보류와 빈 칸 26개는 판정되지 않은 것으로 셉니다.
  - 반환 결과 기준 판정률: 462 / 504 = 91.7%입니다.
- **보류:** 공식 확인을 기다리는 쌍이라 맞음·틀림으로 세지 않습니다(골든셋 전체 30쌍, [batch5/README](../../../golden_prep/batch5/README.md)). 완전 미판정은 아직 판정 기록이 없는 쌍입니다.

## 다시 재기

```
# ai/ 에서. 코퍼스가 고정본과 같은지 먼저 확인
python public_v2_pipeline.py --verify-pin
python test/public_data/corpus_v2/compare_corpora.py run --corpus v2 --dir <새 폴더> \
  --labels test/public_data/corpus_v2/golden_prep/batch5/labels_llm_v6.jsonl
python test/public_data/corpus_v2/compare_corpora.py score --dir <새 폴더> \
  --labels test/public_data/corpus_v2/golden_prep/batch5/labels_llm_v6.jsonl
```

- `embeddings.npy`는 git에 없습니다. 팀 공유 폴더 `v2_aa1a71d35a121150/`에서 받습니다([../../README.md](../../README.md)).
- 실행 폴더는 덮어쓰지 않습니다. 같은 폴더를 다른 기준으로 실행하거나 다른 질문의 라벨로 재채점하면 멈춥니다.
