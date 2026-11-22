# 정답 위치 진단 (hybrid w 0.5)

라벨 `labels_llm_v7`, 명세 `query_spec_v2`. 외부 API 호출 0. 추천 문항의 관련 데이터마다 어느 단계에 있는지 셌다(사본은 하나로).

| 단계 | 뜻 |
|---|---|
| no_candidate | dense·BM25 어느 채널 상위 100에도 없음 → 질문 표현·후보 깊이 문제 |
| filtered | 채널에는 있었지만 조건 필터가 불충족으로 제거 |
| below_10 | 후보에 있고 필터도 통과했지만 결합 순위가 10위 밖 → 결합 문제 |
| rank_6_10 | 상위 10 안이지만 5위 밖 → 최상위 순서 문제 |
| top_5 | 상위 5 안 |

## 2점 정답 (145개, 문항 43개)

| no_candidate | filtered | below_10 | rank_6_10 | top_5 |
|---:|---:|---:|---:|---:|
| 3 (2%) | 0 (0%) | 44 (30%) | 35 (24%) | 63 (43%) |

| 유형 | no_candidate | filtered | below_10 | rank_6_10 | top_5 |
|---|---:|---:|---:|---:|---:|
| direct_lookup | 3 | 0 | 31 | 21 | 29 |
| service_idea | 0 | 0 | 1 | 1 | 2 |
| structured_constraint | 0 | 0 | 12 | 13 | 32 |

## 1점 대안 (392개, 문항 50개)

| no_candidate | filtered | below_10 | rank_6_10 | top_5 |
|---:|---:|---:|---:|---:|
| 19 (5%) | 0 (0%) | 191 (49%) | 91 (23%) | 91 (23%) |

| 유형 | no_candidate | filtered | below_10 | rank_6_10 | top_5 |
|---|---:|---:|---:|---:|---:|
| direct_lookup | 10 | 0 | 66 | 26 | 32 |
| multi_dataset | 3 | 0 | 56 | 23 | 24 |
| service_idea | 1 | 0 | 4 | 4 | 4 |
| structured_constraint | 5 | 0 | 65 | 38 | 31 |

## 2점 정답이 상위 10에 하나도 없는 문항

- p037: no_candidate 1, below_10 2
- p044: below_10 1

## 2점 정답의 채널 순위 (상위 10 밖에 있는 것)

| 문항 | 데이터 | 단계 | dense 순위 | BM25 순위 | 최종 순위 |
|---|---|---|---:|---:|---:|
| p001 | data_go_kr/15004683 | below_10 | 22 | 43 | 28 |
| p001 | data_go_kr/15012896 | below_10 | 14 | 13 | 13 |
| p001 | data_go_kr/15074539 | below_10 | 19 | 8 | 12 |
| p001 | data_go_kr/15108762 | below_10 | 8 | 29 | 17 |
| p001 | data_go_kr/3057773 | below_10 | 18 | 22 | 20 |
| p001 | seoul_open_data/OA-15012 | below_10 | 6 | 32 | 16 |
| p002 | data_go_kr/15013115 | below_10 | 9 | 36 | 22 |
| p002 | seoul_open_data/OA-13281 | below_10 | 8 | 17 | 11 |
| p002 | seoul_open_data/OA-21712 | below_10 | 11 | 15 | 13 |
| p005 | data_go_kr/15060883 | below_10 | 29 | 63 | 14 |
| p006 | data_go_kr/15100064 | below_10 | 60 | – | – |
| p006 | data_go_kr/15127578 | below_10 | 35 | – | – |
| p006 | data_go_kr/15143461 | below_10 | 15 | – | – |
| p009 | seoul_open_data/OA-21275 | below_10 | 41 | 5 | 17 |
| p012 | data_go_kr/15076636 | below_10 | – | 39 | – |
| p014 | seoul_open_data/OA-15577 | below_10 | – | 57 | – |
| p014 | seoul_open_data/OA-15578 | below_10 | – | 64 | – |
| p014 | seoul_open_data/OA-22172 | no_candidate | – | – | – |
| p016 | seoul_open_data/OA-15526 | below_10 | 3 | – | 28 |
| p016 | seoul_open_data/OA-23044 | below_10 | 5 | – | – |
| p017 | data_go_kr/15124952 | below_10 | 6 | 23 | 14 |
| p018 | data_go_kr/15002503 | below_10 | 55 | 14 | 20 |
| p018 | data_go_kr/15099330 | below_10 | 15 | 11 | 13 |
| p018 | data_go_kr/15143845 | below_10 | 16 | 2 | 11 |
| p031 | data_go_kr/15013094 | below_10 | 3 | 31 | 12 |
| p035 | data_go_kr/15083323 | below_10 | 12 | – | 26 |
| p035 | data_go_kr/15090532 | below_10 | 6 | – | 16 |
| p035 | data_go_kr/15108347 | below_10 | 4 | – | 11 |
| p035 | data_go_kr/15116392 | no_candidate | – | – | – |
| p035 | seoul_open_data/OA-23014 | below_10 | 5 | – | 14 |
| p037 | data_go_kr/15074671 | below_10 | 6 | – | 18 |
| p037 | data_go_kr/15124807 | below_10 | 3 | – | 12 |
| p037 | data_go_kr/15146890 | no_candidate | – | – | – |
| p044 | data_go_kr/15084084 | below_10 | – | 18 | – |
| p049 | data_go_kr/15073861 | below_10 | 96 | 3 | 22 |
| p053 | data_go_kr/15147946 | below_10 | – | 8 | – |
| p053 | data_go_kr/15147966 | below_10 | 72 | 9 | 11 |
| p053 | data_go_kr/15148252 | below_10 | 79 | 10 | 13 |
| p053 | seoul_open_data/OA-20317 | below_10 | 22 | 47 | 12 |
| p054 | data_go_kr/15021141 | below_10 | 96 | 19 | 13 |
| p054 | data_go_kr/15104026 | below_10 | – | 3 | 18 |
| p054 | data_go_kr/3054892 | below_10 | – | 5 | 21 |
| p058 | data_go_kr/15043644 | below_10 | 13 | – | – |
| p058 | data_go_kr/15057210 | below_10 | 67 | 30 | 25 |
| p058 | data_go_kr/15059093 | below_10 | 56 | 29 | 23 |
| p058 | data_go_kr/15059218 | below_10 | – | 33 | – |
| p058 | data_go_kr/15157595 | below_10 | 91 | 8 | 17 |
