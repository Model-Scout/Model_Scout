# batch6: 골든셋 v7 (공공데이터 검색 파일럿 1의 미판정 513쌍)

`labels_llm_v7.jsonl`은 골든셋 v6(`batch5/labels_llm_v6.jsonl`)에 이 폴더의 판정 513쌍을 더한 라벨입니다. v6와 batch1~5 파일은 바꾸지 않았습니다.

## 무엇을 판정했나

- **대상:** [파일럿 1](../../../retrieval/runs/2026-11-16_pilot1/report.md)의 다섯 경로(hg_question, hg_terms, dense, bm25, hybrid) 상위 10의 합집합 가운데 v6가 판정하지 않은 쌍입니다(`unjudged_blind.jsonl`). 58문항 모두에 걸쳐 있습니다.
- **가림:** 판정 카드에는 어느 경로가 몇 위로 찾았는지 넣지 않았습니다. 검색됐다는 이유로 점수를 주지 않았습니다.
- **기준:** [`test/public_data/README.md`의 2차 판정 기준](../../../README.md)과 batch5의 판단을 그대로 따랐습니다. 비슷한 데이터를 v6가 어떻게 판정했는지 문항마다 대조했고, note에 "(v6 …와 같은 판단)"으로 적었습니다.
- **방식:** 카드(v2 보완본 사실과 자동 조건 검사)를 보고 한 LLM 1차 판정(`llm_first_pass`, judge `claude`)입니다. 공식 페이지는 열지 않았습니다. 외부 API 호출은 0회입니다.

## 결과

| 점수 | 쌍 |
|---|---:|
| 2 | 17 |
| 1 | 84 |
| 0 off_topic | 372 |
| 0 wrong_delivery | 15 |
| 0 wrong_region | 6 |
| 0 license | 1 |
| ? 보류 | 18 |

- v6 → v7: 관련 436 → 537쌍, 제외 대상 87 → 109, 판정된 무관 516 → 888, 보류 30 → 48입니다.
- 채점 가능 문항은 56개로 같고, 정답 등급(`answer_grade`)이 바뀐 문항은 없습니다.
- `review_batch.py validate` 결과: 위반 0건, 경고 8건입니다. 경고는 모두 "같은 질문·같은 자동 검사 상태인데 점수가 다름"입니다. 점수는 요구 항목을 얼마나 충족하는지에 따라 갈렸고, 그 사유를 `resolutions.json`에 적었습니다.

## 보류 18쌍

| 확인할 것 | 질문 |
|---|---|
| 실시간 반영 시점·실시간 제공 여부 | p045 2건(태풍정보, 긴급재난문자), p049 2건(전북·울산 측정소), p050 1건(산지공판장 경락가격) |
| 상업 이용 범위(공공누리 1유형, 제3자 권리 포함) | p031 1건(교통 CCTV), p053 1건(전국어린이집 표준데이터) |
| 파일 제공 여부 | p025 2건(공항 주차장) |
| 요구 지역이나 항목이 들어 있는지 | p015(전국 공영자전거에 따릉이 포함 여부), p016(산림 미세먼지 측정 지점에 서울 포함 여부), p024 2건(100대 명산 POI·군 복지시설 주변 관광지에 제주 포함 여부), p027 2건(실시간 도시데이터·정류소 정보에 도착 예정 정보가 있는지), p036(허가 상세정보에 효능·용법 항목이 있는지), p052(대구 학군별 학교 목록에 주소 포함 여부) |
| 범위 판단 | p040 1건(공항 주차장 실시간 정보. v6의 대전 실시간 주차장 보류와 같은 판단) |

## 파일

| 파일 | 내용 |
|---|---|
| `make_items.py` | `unjudged_blind.jsonl` → 판정 카드(`items.jsonl`)와 자동 검사(`review_suggestions.jsonl`). 파일럿과 같은 v2 코퍼스로 만들고, 자동 검사 결과가 파일럿 실행 때와 513쌍 모두 같은지 확인했습니다 |
| `judgments.tsv` | 판정 원본(한 줄에 한 쌍: review_id, 점수, 사유, note, 확인 기록) |
| `make_judgments.py` | `judgments.tsv` → `judgments.jsonl`(batch5와 같은 행 형식). 지역 미지정 질문의 1·2점에는 "지역은 기능으로 판단" 기록을 붙입니다 |
| `resolutions.json` | 검사기 경고 8건의 검토 사유 |
| `labels_llm_v7.jsonl`, `.meta.json` | v7 라벨과 그 입력 해시 |

## 다시 만들기

경로는 `ai/` 기준입니다.

```
B=test/public_data/corpus_v2/golden_prep/batch6
python -X utf8 $B/make_items.py
python -X utf8 $B/make_judgments.py
python -X utf8 test/public_data/corpus_v2/review_batch.py validate $B/judgments.jsonl --suggestions $B/review_suggestions.jsonl
python -X utf8 test/public_data/corpus_v2/review_batch.py labels $B/judgments.jsonl --suggestions $B/review_suggestions.jsonl \
  --resolutions $B/resolutions.json --base test/public_data/corpus_v2/golden_prep/batch5/labels_llm_v6.jsonl --out <새 파일>
```

결과가 `labels_llm_v7.jsonl`과 같아야 합니다.

## 사람이 다시 볼 것

1차 판정은 LLM 판정입니다. batch5까지처럼 1점 행과 경계 판단은 사람이 다시 보는 것이 좋습니다. 특히 다음입니다.
- p016: 지하역사·공항 실내 공기질을 대기 측정 자료가 아니라고 보고 0으로 판정
- p033: 헌재 결정례를 판례 원문으로 인정(1)
- p031: 무인교통단속카메라를 CCTV의 부분 대안(1)으로 인정
- p005: 모범음식점 신청·지정 현황은 1, 취소 현황은 0(v6 강남구 취소 현황 0과 맞춤)
