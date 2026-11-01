# Stage 4 추천 질의·결과 품질 검토

## 검토 범위

현재 검증은 `test/retrieval_queries.jsonl`의 33개 한국어 질의를 사용했다. Core 1,451개와 Low Popularity 2,116개를 합친 3,567개 임베딩 corpus를 대상으로 마지막 실행 결과인 vector 모드의 `test/stage4_retrieval_validation.json`을 평가했다.

이 질의 파일은 task, 한국어 여부, 파라미터 수, context 길이, popularity 같은 **제약 조건**을 포함한 constraint gold set이다. 질의별로 사람이 지정한 정답 모델 ID가 없으므로 의미적 Precision@5·Recall@5를 이 결과만으로 주장하지 않는다.

## 제약 검증 결과

| 지표 | 결과 |
|---|---:|
| 질의 | 33 |
| 빈 결과 | 0 |
| 제약 통과 질의 | 33/33 |
| 상위 결과 행 | 162 |
| task 위반 | 0 |
| 한국어 조건 위반 | 0 |
| unknown 파라미터 조건 위반 | 0 |
| unknown context 조건 위반 | 0 |
| canonical 중복 | 0 |
| task conflict | 0 |

따라서 현재 검색기는 요청된 hard constraint를 지키는 후보를 반환하는 데에는 100% 통과했다. 이는 모델의 실제 업무 적합성이나 순위 자체의 정답률과는 다른 지표다.

## 근거 품질

| 지표 | 결과 |
|---|---:|
| `evidence_completeness=high` | 119/162 (73.5%) |
| high 또는 medium | 123/162 (75.9%) |
| low | 18/162 (11.1%) |
| unknown | 21/162 (13.0%) |
| 비어 있지 않은 주장과 `evidence_refs`가 함께 존재 | 143/162 (88.3%) |
| Stage 3 validation이 존재하는 상위 결과 | 149/162 |
| invalid evidence reference | 0 |
| uncited claim | 0 |
| missing quote | 0 |

Stage 3의 검증 행에서는 인용 reference와 quote 무결성 오류가 발견되지 않았다. 다만 상위 결과 중 39개는 low 또는 unknown 신호이거나 semantic claim이 비어 있으므로, 화면에서는 근거 확인 필요 상태를 따로 표시해야 한다.

Stage 4 row는 검색용으로 `evidence_completeness`를 보관한다. 실제 설명 화면에서 supporting quote와 evidence reference를 보여주려면 반환된 `model_id`로 Stage 3의 `semantic`·`evidence`를 조인해야 한다.

## Benchmark 질의

| 질의 | 상위 결과 중 benchmark match |
|---|---:|
| `q31_mteb_arguana_ndcg` | 4/5 |
| `q32_mteb_embedding_evidence` | 4/5 |
| `q33_asr_wer_evidence` | 1/5 |

Benchmark 정보는 같은 benchmark·dataset·metric이 확인될 때만 보조 ranking 신호로 사용한다. README self-reported 값이므로 모델 품질의 확정 판정이나 서로 다른 실험 조건의 직접 비교에 사용하지 않는다.

## 결론

현재 파이프라인은 검색 필터, 한국어 조건, known metadata 조건, canonical 중복 제거를 안정적으로 적용한다. 근거 extraction도 reference 오류 없이 동작하지만 모든 결과가 동일한 수준의 설명 근거를 갖는 것은 아니다.

의미적 검색 정확도를 확정하려면 질의별 관련 모델 ID를 사람이 10~20개씩 라벨링한 semantic gold set을 추가하고, 그때 Precision@5·Recall@5·nDCG를 계산해야 한다.
