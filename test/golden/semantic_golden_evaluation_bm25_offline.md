# Semantic 골든셋 평가

실제 모델 선정 사례(`test/golden/korean_model_selection_cases_*.jsonl`)에서 만든 정답 라벨로 검색 결과를 채점한다.
`evaluable_now=true`인 질의만 점수에 포함하고, recall_check·blocked 질의는 정답 모델의 DB 포함 여부만 추적한다.

## 요약

- 검색 모드: `bm25_offline`
- 채점 질의: 28개, 통과 3개
- recommend 질의 hit@5: 1/24 (95% 부트스트랩 구간 [0.0, 0.125])
- recommend 질의 acceptable hit@5: 1/24
- recommend 질의 같은 계열(canonical) hit@5: 1/24
- recommend 질의 MRR: 0.0417
- must_exclude 위반 질의: 0/28
- 상업 조건 라이선스 위반 질의: 1/6

## 신뢰도 등급별 (recommend 질의)

| tier | 질의 | hit@5 | acceptable hit@5 |
|---|---:|---:|---:|
| A | 2 | 0 | 0 |
| B | 14 | 1 | 1 |
| C | 8 | 0 | 0 |

## task별 (recommend 질의)

| task | 질의 | hit@5 | acceptable hit@5 |
|---|---:|---:|---:|
| automatic-speech-recognition | 9 | 0 | 0 |
| feature-extraction | 4 | 0 | 0 |
| image-text-to-text | 1 | 1 | 1 |
| summarization | 3 | 0 | 0 |
| text-classification | 1 | 0 | 0 |
| text-generation | 4 | 0 | 0 |
| translation | 2 | 0 | 0 |

## 질의별 결과

| 질의 | task | 등급 | 동작 | 통과 | 정답 순위 | 허용 순위 | 계열 순위 | 실패 원인 |
|---|---|---|---|---|---:|---:|---:|---|
| `sg_g002` | translation | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g003` | translation | B | must_exclude_only | ✅ | - | - | - | - |
| `sg_g004` | feature-extraction | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g005` | translation | A | recommend | ❌ | - | - | - | 정답 없음; 알려진 원인: nllb 3종 모두 DB parameter_count=unknown이라 '3GB VRAM 초과'로 3.3B를 걸러낼 수 없음. 이 질의가 must_exclude에서 실패하면 검색이 아니라 메타데이터 공백으로 기록. |
| `sg_g006` | automatic-speech-recognition | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g007` | automatic-speech-recognition | C | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g008` | automatic-speech-recognition | C | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g009` | summarization | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g010` | image-text-to-text | B | recommend | ✅ | 1 | 1 | 1 | - |
| `sg_a001` | image-text-to-text | B | warn_on_oversize | ❌ | - | - | - | 크기 경고 누락 2개 |
| `sg_g013` | feature-extraction | C | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g014` | text-classification | C | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g015` | text-generation | A | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g016` | text-generation | A | must_exclude_only | ✅ | - | - | - | - |
| `sg_g017` | text-generation | C | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g018` | automatic-speech-recognition | C | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g019` | automatic-speech-recognition | C | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g020` | automatic-speech-recognition | C | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g021` | text-generation | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g022` | text-generation | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g023` | summarization | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g024` | feature-extraction | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g025` | feature-extraction | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g026` | automatic-speech-recognition | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g027` | automatic-speech-recognition | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g028` | automatic-speech-recognition | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g029` | summarization | B | recommend | ❌ | - | - | - | 정답 없음 |
| `sg_g030` | text-generation | B | must_exclude_only | ❌ | - | - | - | 비상업 라이선스: mradermacher/DataVortexS-10.7B-dpo-v1.10-GGUF, LDCC/LDCC-SOLAR-10.7B, TheBloke/SOLARC-MOE-10.7Bx4-GGUF |

## 아직 채점하지 않는 질의

| 질의 | 유형 | 막힌 이유 | 정답 중 DB에 있는 모델 |
|---|---|---|---|
| `sg_g001` | blocked | gguf_license_other | batiai/gemma-4-E4B-it-GGUF |
| `sg_g011` | recall_check | answer_not_in_db | 없음 |
| `sg_g012` | recall_check | answer_not_in_db | 없음 |
| `sg_r001` | recall_check | answer_not_in_db | 없음 |
| `sg_r002` | recall_check | answer_not_in_db | 없음 |
| `sg_r003` | recall_check | answer_not_in_db | 없음 |
| `sg_r004` | recall_check | answer_not_in_db | 없음 |
| `sg_r005` | recall_check | answer_not_in_db | 없음 |
| `sg_r006` | recall_check | answer_not_in_db | 없음 |
| `sg_r007` | recall_check | answer_not_in_db | 없음 |
| `sg_r008` | recall_check | answer_not_in_db | 없음 |
| `sg_r009` | recall_check | answer_not_in_db | 없음 |

## 해석 시 주의

- 라이선스 판정은 채점용 임시 정책이다. apache-2.0·mit 등은 상업 허용, 이름에 `nc`가 들어가면 위반, `other`·gemma·llama·미기재는 `확인 필요`로 본다.
- 현재 검색 결과에는 `확인 필요` 경고 필드가 없어서, 경고가 필요한 모델이 top-k에 나오면 모두 경고 누락으로 집계된다.
- 정답은 사례 작성자가 고른 모델 하나이지 유일한 정답이 아니다. acceptable hit를 함께 본다.
- 정답·허용 순위는 model_id가 정확히 같을 때만 센다. 계열 순위는 canonical_model_id 일치까지 포함하며, canonical이 선언된 base model을 따르므로 다른 파인튜닝 모델도 같은 계열로 잡힐 수 있다.
- `lexical_offline` 모드는 정수 점수 동점이 많아 순위 신뢰도가 낮다. `bm25_offline`은 키 없이 돌리는 sparse 기준선이고, 실제 서비스 성능 판단은 `--execute`(vector) 결과로 한다.
- 질의 수가 적어 부트스트랩 구간이 넓다. 두 검색 방식의 차이가 이 구간 안이면 우열을 주장하지 않는다.
- 등급은 `test/golden/audit_golden.py`가 매긴 라벨 근거의 강도다. C등급 질의만 틀리면 라벨 문제일 가능성도 함께 본다.
