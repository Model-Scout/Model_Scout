# 검색 대상 라우터 평가

- 질의 265개, LLM `gpt-4o-mini`, 라우터 프롬프트 v2 / 분류기 v3
- 실패(status != ok): 0개

## 검색 대상 정확도

| 묶음 | 정답 | 질의 수 | 정확도 |
|---|---|---:|---:|
| edge | both, dataset, model, needs_clarification | 29 | 1.000 |
| model_golden | model | 178 | 1.000 |
| public_abstention | dataset | 5 | 1.000 |
| public_ai_data | dataset | 7 | 1.000 |
| public_constrained | dataset | 19 | 1.000 |
| public_direct_lookup | dataset | 9 | 1.000 |
| public_service_idea | dataset | 18 | 0.944 |
| **전체** | | 265 | **0.996** |

## 대상 Confusion (정답 → 예측)

- both → both: 7
- dataset → both: 1
- dataset → dataset: 67
- model → model: 184
- needs_clarification → needs_clarification: 6

## 모델 유형 (모델 골든셋 178개)

- 정확도 0.758 (135/178)
- 두 constraint 유형을 같은 것으로 칠 때 0.893

## LLM 지연 (API 호출 시)

- p50 721ms, p95 1304ms, 최대 4936ms

## 대상을 틀린 질의

| id | 묶음 | 정답 | 예측 | 문장 |
|---|---|---|---|---|
| p011 | public_service_idea | dataset | both | 등산객에게 등산로와 산불 위험 정보를 같이 알려주는 앱을 만들고 싶어. |
