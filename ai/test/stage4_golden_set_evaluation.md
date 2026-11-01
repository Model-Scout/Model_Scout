# Stage 4 검색 제약 골든셋 평가

이 평가는 `stage4_retrieval_validation.json`의 48개 질의를 사용한 오프라인 검증이다. 각 질의의 task, 한국어 조건, 파라미터·context·인기도 조건을 정답 제약으로 취급한다.
이 파일에는 질의별 정답 모델 ID가 없으므로 의미적 Precision@5·Recall@5를 주장하지 않는다. 그 수치는 사람이 질의별 관련 모델을 라벨링한 뒤 별도로 계산해야 한다.

## 실행 결과

- 검색 모드: `vector`
- 후보 corpus: `3567`개 (Core + Low Popularity)
- 질의: `48`개, 빈 결과 `2`개
- 제약 통과 질의: `48/48`
- 상위 결과 행: `224`개
- 상위 결과 hard constraint 통과: `224/224` (100%)
- advisory task conflict: `1`

## 근거 품질

| 지표 | 결과 |
|---|---:|
| evidence_completeness=high | 165 / 224 (73.7%) |
| high 또는 medium | 170 / 224 (75.9%) |
| low | 24 / 224 (10.7%) |
| unknown | 30 / 224 (13.4%) |
| 비어 있지 않은 주장 + evidence_refs | 199 / 224 (88.8%) |
| Stage 3 검증 행 | 208 / 224 |
| invalid evidence ref | 0 |
| uncited claim | 0 |
| missing quote | 0 |

`evidence_completeness`는 검색 결과에 저장된 근거 충실도 신호다. 실제 설명 화면에서 인용문을 보여주려면 Stage 4 결과의 `model_id`로 Stage 3의 `semantic`과 `evidence`를 조인해야 한다.

## Benchmark 질의

| 질의 | 상위 결과 중 benchmark match |
|---|---:|
| `q31_mteb_arguana_ndcg` | 4/5 |
| `q32_mteb_embedding_evidence` | 4/5 |
| `q33_asr_wer_evidence` | 1/5 |

Benchmark 점수는 동일한 benchmark·dataset·metric 조건이 확인될 때만 보조 boost로 사용한다. README self-reported 값이므로 모델 품질의 확정 판정으로 사용하지 않는다.

## 판단

현재 파이프라인은 hard constraint를 위반하지 않는 후보를 반환하는 데에는 `33/33`으로 안정적이다. Stage 3의 검증된 행에서는 invalid reference, uncited claim, missing quote가 발견되지 않았다. 다만 상위 결과의 약 `24.1%`는 `low` 또는 `unknown` 근거 충실도이거나 비어 있는 semantic claim이므로, 화면에는 ‘근거 확인 필요’를 표시하는 것이 안전하다.

의미적 추천 정확도를 확정하려면 다음 단계로 질의별 관련 모델 ID를 사람이 10~20개씩 라벨링한 진짜 semantic gold set을 추가해야 한다.
