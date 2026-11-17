# 따릉이 모델 검색 실패 원인 조사

조사일: 2026-11-17 (한국 시간)

## 결론

따릉이 검색 문제에는 검색 분기 정책, 후속 요청의 분기 고정, 예측 모델 수집 범위와 검색 필터의 불일치가 함께 있다. 로컬 생성 LLM에서도 시간 초과 및 계획 품질 문제가 관찰됐다. 특정 운영 요청의 로그를 확보한 것은 아니므로 운영 장애의 단일 원인으로 단정하지 않는다.

## 확인한 원인

### 1. 서비스 아이디어는 모델 검색을 실행하지 않는다

- `ai/retrieval_lab/router.py:35`는 위치·기록 등이 필요한 서비스 아이디어를 `dataset`으로 분류하도록 명시한다. 모델을 명시적으로 요청할 때만 모델 분기가 포함된다.
- `ai/17_recommend_graph.py:468`의 `search_models()`는 이 경우 `models=[]`를 바로 반환한다. 검색 결과가 없다는 의미가 아니라 검색을 실행하지 않았다는 의미다.
- 실제 라우터 호출에서 `따릉이 경로 추천 서비스를 만들고 싶어`와 `따릉이 대여소 데이터 찾아줘` 모두 `target=dataset`, `status=ok`가 반환됐다.

### 2. 같은 대화에서 검색 대상을 바꾸지 못한다

- `ai/17_recommend_graph.py:330`의 `route()`는 기존 `route`가 있으면 `{}`를 반환하며 재분류하지 않는다.
- 따라서 데이터 검색 뒤 모델을 요구해도 기존 `dataset` 분기를 유지한다.
- 기존 route를 넣고 재분류 함수 호출 여부를 검사해 호출되지 않음을 확인했다.
- 기존 회귀 테스트 `test_follow_up_keeps_first_target`도 이 동작을 기대한다. 관련 파일 테스트는 9 passed.

### 3. 수요 예측은 분류 체계에 있지만 모델 수집 대상에 없다

- `ai/taxonomy.yaml:70`에는 `forecasting`, 85행에는 `tabular_prediction`이 있다.
- `ai/01_collect_models.py:26`의 수집 대상은 텍스트 생성·임베딩·번역·음성 인식 등 9개 task이며 시계열 예측·표 데이터 예측 task는 없다.
- `ai/data/model_snapshot/active_models_20261115.jsonl`의 4,017개 모델을 집계했다. primary task별 개수는 아래와 같다.

| primary task | 개수 |
|---|---:|
| text-generation | 2,346 |
| image-text-to-text | 537 |
| automatic-speech-recognition | 321 |
| translation | 280 |
| sentence-similarity | 201 |
| text-classification | 157 |
| feature-extraction | 137 |
| question-answering | 29 |
| summarization | 9 |

이 스냅샷은 메타파일 기준 2026-11-14T17:02:19Z의 Supabase active 모델 읽기 결과다. 현재 운영 DB의 전체 상태를 다시 집계한 결과는 아니다. 전용 primary task가 없다는 확인이며 모든 모델의 예측 능력이 없음을 뜻하지 않는다.

### 4. 지원하지 않는 task가 전체 검색으로 풀린다

- `ai/17_recommend_graph.py:227`의 `hf_tags('forecasting')`, `hf_tags('tabular_prediction')`은 모두 `[]`다.
- 486행에서 이 값이 `_model_rows()`에 전달되고 456행에서 `task_filters=None`으로 바뀐다.
- `ai/supabase_schema.sql`의 검색 RPC는 null/빈 task 필터를 task 제한 없음으로 해석한다.
- `forecasting` 계획을 직접 넣고 검색 호출 인자를 캡처해 `task_filters=[]` 전달을 확인했다. 이 검증은 외부 모델 검색을 대체한 호출 경로 검증이다.
- RPC에는 최소 관련도 탈락 기준 없이 점수순 상위 N개를 반환하는 경로가 있다. 따라서 지원 범위 밖의 요청에 일반 언어 모델이 노출될 수 있다. 이번 조사에서 실제 운영 후보가 그렇게 반환됐다고 확정한 것은 아니다.
- `korean_required=True`도 모든 모델 검색에 고정된다. 향후 언어와 무관한 수치 예측 모델까지 수집 범위를 확장할 때 함께 검토해야 한다.

## 로컬 LLM 재현에서 관찰한 사항

- 현재 로컬 생성 설정은 `ollama/gemma3:4b`였다. 라우터는 별도 OpenAI 분류기를 사용한다.
- `따릉이 경로 추천 서비스를 만들고 싶어`: 라우팅은 dataset으로 성공했지만 요구사항 분해에서 `APITimeoutError`가 발생했다. 로컬 Ollama 클라이언트 제한은 120초다.
- `따릉이 대여소 데이터 찾아줘`: 계획 생성에는 성공했지만 사용자가 요청하지 않은 질문 의도 분류·정보 추출·질의응답 모델 역할을 생성하고, 데이터 검색 목적을 ‘사용자 질문에 답하는 AI 모델 구축’으로 바꿨다. 모델 검색어 문자열에도 구문 조각이 섞였다.
- `따릉이 수요 예측 모델 찾아줘`: 라우팅은 model로 성공했지만 계획 생성 호출에서 `InternalServerError`가 발생했다. 모델 검색을 호출하기 전의 오류다.
- `따릉이 수요 예측 모델과 데이터 찾아줘`: 라우팅은 both로 성공했지만 계획 생성에서 `APITimeoutError`가 발생했다.
- 네 질의의 원시 재현 결과는 `bike_search_probe_results.json`에 저장했다. 데이터 검색·최종 답변까지의 E2E 검증은 수행하지 않았다.
- `DECOMPOSE_PROMPT`가 검색 대상과 무관하게 1~4개 모델 역할을 만들도록 지시하며, `decompose()`는 라우팅 결과를 planner에 전달하지 않는다. 데이터 전용 요청에서도 불필요한 모델 계획을 만들고 모델 task가 데이터 검색어에 합쳐질 수 있다.
- 재현은 최대 2개 요청을 동시에 실행했으므로 로컬 생성 지연에는 동시 실행 영향이 있을 수 있다. 운영 서버의 생성 설정·시간 초과·로그를 확인한 결과와 구분해야 한다.

## 권장 수정 순서

1. 후속 메시지에서 검색 대상 변경을 감지해 재라우팅한다. 기존 유지 동작을 기대하는 테스트도 정책에 맞게 변경한다.
2. 서비스 아이디어를 데이터만 검색할지, 필요한 모델까지 함께 제안할지 제품 정책을 정한다. 후자라면 현재 라우터 규칙을 변경한다.
3. 지원하지 않는 모델 task를 전체 검색으로 풀지 말고 지원 범위 밖임을 명시한다. 수요 예측 모델을 제공하려면 수집 대상과 언어 정책까지 함께 확장한다.
4. planner에 검색 대상과 지원 task를 전달한다. 데이터 전용 요청은 모델 역할 없이 데이터 요구사항만 만들도록 분리한다.
5. Gemma의 계획 생성은 단일 요청으로 시간·출력 품질을 별도 검증한다. 관련도 검증과 skipped/empty/error 상태도 구분한다.

위 조사 시점에는 애플리케이션 코드와 운영 설정을 수정하지 않았다. 이후 조치는 아래 절에 정리했다.

## 후속 조치 (2026-11-17, `feat/yj`, 미커밋)

| 원인 | 조치 | 파일 |
|---|---|---|
| 1. 서비스 아이디어가 모델 검색 안 함 | 라우터 프롬프트 v4: 구체적 서비스 아이디어는 `both`, 명시한 단일 대상이 우선. 골든셋 r030~r041 추가, gpt-4o-mini 41/41 (1회 실행) | `ai/retrieval_lab/router.py`, `ai/test/golden/labels/routing_edge_queries.jsonl`, `ai/retrieval_lab/reports/service_idea_routing.json` |
| 2. 후속 질문 route 고정 | `follow_up_target()`: 명시적 대상 변경("이제 모델만", "데이터는 빼줘", "모델 말고", "데이터는 이미 있어", "모델 쪽은 됐어/충분해/그만")은 규칙으로 교체(LLM 호출 없음). 규칙 밖은 `_follow_up_by_llm()`이 판단하며, 현재는 단일 턴 라우터로 추가만 반영(dataset + model → both). 멀티턴 LLM 판정기로 이 함수만 교체하면 됨. 후속 골든셋 `follow_up_routing.jsonl` 17건(rule 9 / llm 8)으로 규칙과 LLM 담당을 구분 | `ai/17_recommend_graph.py`, `ai/test/golden/labels/follow_up_routing.jsonl` |
| 3·4. 미수집 task → 전체 검색 | 수집 모델이 제공하는 기능은 해당 태그로 검색: tool_use·information_extraction·table_qa → text-generation, ocr·chart_understanding → image-text-to-text. 그 외 태그 없는 task(forecasting, tabular_prediction, text_to_speech, audio_classification, vision, image_generation, language_modeling; `reranking`은 질의문 검색 유지)는 검색하지 않고 `unsupported: true` 반환, 답변이 무관한 모델을 제안하지 않음. 수요 예측 모델 수집 확장은 미착수 | `ai/17_recommend_graph.py` `MODEL_TASK_FALLBACK`, `search_models()`, `EXPLAIN_PROMPT` |
| 5. planner가 route 모름 | planner 입력 첫 줄에 `SEARCH_TARGET` 전달. dataset이면 모델 역할을 만들지 않고 데이터만 기술. 1차 계획 캐시 키에 target 포함 | `ai/17_recommend_graph.py` `DECOMPOSE_PROMPT`, `_parse_plan()`, `decompose()`, `clarify()` |

검증: `ai/test/test_query_router.py`, `test_recommend_routing.py`, `test_recommend_contract_stack.py` 101 passed, `17_recommend_graph.py --self-check` ok, `backend/tests/test_v2.py` 24 passed. 실제 LLM·DB로 따릉이 질의 E2E는 재실행하지 않았다.

기존 사용자의 프론트 lockfile 변경과 검증 문서는 보존했다.
