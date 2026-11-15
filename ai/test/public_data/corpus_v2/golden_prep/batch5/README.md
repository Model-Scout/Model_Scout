# batch5: 골든셋 v6 (팀 v5 + batch4 병합, API 근거 보완 반영)

`labels_llm_v6.jsonl`은 팀 기준 라벨 v5(`batch3/labels_llm_v5.jsonl`)에 이 폴더의 판정 211쌍을 적용한 라벨입니다. 기존 batch1~4 파일은 바꾸지 않았습니다.

## 무엇을 바꿨나

- **batch4 병합:** batch4의 174쌍을 모두 합쳤습니다. 팀 v5와 겹치는 쌍은 없습니다.
  - batch4 판정의 `batch` 값은 `"batch3"`으로 적혀 있었습니다. 폴더 이름을 나중에 바꿨기 때문입니다.
  - 이어받은 행에는 원래 값을 `recorded_batch_field`에 남기고, `batch`를 `"batch4"`로 바로잡았습니다.
- **API 근거 보완 반영:** 코퍼스가 표준데이터·파일데이터의 상세 페이지에서 API 근거를 읽게 되면서, 형식 정보가 바뀐 쌍을 다시 판정했습니다.
  - 자동변환 OpenAPI도 "API 제공" 조건에 인정합니다.
  - 실시간 여부는 따로 판단합니다. 자동변환 API는 올린 파일의 내용이라 실시간 근거가 아닙니다.
- **p050 조건 변경:** `delivery`를 `api`에서 `any`로 바꿨습니다(`revisions.jsonl`).
  - 질문 문장은 그대로이므로 기존 질의 벡터를 재사용합니다.
  - 판정된 12쌍은 실시간 기준으로 다시 판정했습니다. 점수는 그대로이고, 제외 근거만 제공 방식에서 실시간으로 바꿔 적었습니다.
- **삭제 자료:** `data_go_kr/3069954`(p029, p042의 0점)는 포털에서 삭제되어 검색 대상에 없습니다. 판정은 기록으로 남겼습니다(`labels_llm_v6.meta.json`의 `not_in_corpus`).

## 어떤 쌍을 다시 판정했나

| 판정 대상 | 판정 방식 |
|---|---|
| batch4 중 형식 외 사실(설명, 기관, 갱신 표기)이 바뀐 쌍 | 재판정 |
| batch4 중 형식·API가 바뀌었고, 질문이 제공 방식을 요구하거나 메모가 형식을 근거로 든 쌍 | 재판정 |
| batch4 중 형식·API만 바뀌었고, 질문이 제공 방식을 요구하지 않는 쌍 | 판정 이어받음, 변경 사유 기록 |
| 팀 v5에서 제공 방식 조건 질문의 판정이 현재 형식과 어긋나는 쌍 | 재판정 |
| p050의 판정된 쌍 전부, p051 피드백 지정 4쌍 | 재판정 |

판정은 카드(v2 보완본 사실과 자동 검사)를 보고 한 LLM 1차 판정(`llm_first_pass`)입니다. 공식 페이지는 15062509, 15154373 두 건의 포털 OpenAPI 페이지만 열었습니다.

## 점수가 바뀐 팀 v5 쌍 (9)

| 질문 | 데이터 | v5 | v6 | 이유 |
|---|---|---|---|---|
| p024 | data_go_kr/15049995 | 제외 | 1 | "CSV만" 근거가 사라짐(자동변환 API 확인). 이용자 입력 장소 목록만 있어 부분 적합 |
| p025 | seoul_open_data/OA-11580 · OA-13122 · OA-15012 | 제외 | 1 | 시트(CSV) 제공 확인. 서울 또는 한 개 구만이라 부분 적합 |
| p051 | seoul_open_data/OA-13472 · OA-2717 | 제외 | 1 | 시트(CSV) 제공 확인. 한 개 구만이라 부분 적합 |
| p045 | data_go_kr/15052606 | 제외 | 0 off_topic | "CSV만" 근거가 사라짐. 공항 윈드시어 경보라 기상특보 주제가 아님 |
| p051 | data_go_kr/15062509 · 15154373 | 제외 | ? | 포털 OpenAPI 페이지에 내려받기가 없다는 것만 확인함(아래) |

**p051 두 건(경남 도서관, 국립중앙도서관)을 보류로 둔 이유:**
- 확인한 것은 공공데이터포털 상세 페이지 한 장뿐입니다. 페이지에는 API 유형 REST, 데이터 포맷 JSON+XML이 적혀 있고, 내려받을 수 있는 것은 "가이드 다운로드"뿐이었습니다. 원 제공처로 가는 링크는 없었습니다.
- 같은 기관의 파일데이터는 코퍼스에서 찾지 못했습니다. 원 제공처(경상남도, 국립중앙도서관) 누리집의 파일 제공 경로는 확인하지 않았습니다.
- "페이지에 버튼이 없다"는 것이 "파일로 제공하지 않는다"는 뜻은 아니므로, 파일 미제공(0점)으로 확정하지 않았습니다. 확인할 항목은 `judgments.jsonl`의 `verification.pending`에 있습니다.

## 남은 보류 (14)

- p002 1건, p023 2건, p040 2건, p045 1건, p055 1건
- p051 2건: 원 제공처의 파일 제공 경로 확인 필요
- p050 3건: 경매 후 API 반영 시점 확인 필요
- p041 2건: Kaggle 유튜브 데이터에 조회수·댓글 항목이 있는지 확인 필요. p041은 기권 질문이라 보류가 남아 있는 동안 평가에서 빠집니다(v5 57 → v6 56 질문).

## 파일

| 파일 | 내용 |
|---|---|
| `items.jsonl` | 판정 카드 211개(사실, 판정 대상이 된 이유 `review_reasons`) |
| `review_suggestions.jsonl` | 자동 검사 결과 |
| `judgments.jsonl` | 판정 211행(재판정 91, batch4에서 이어받음 120) |
| `resolutions.json` | 검사기 경고 1건의 검토 사유 |
| `revisions.jsonl` | 라벨 생성 후 바꾼 조건(p050) |
| `labels_llm_v6.jsonl`, `.meta.json` | v6 라벨과 그 입력 해시 |
| `manifest.json` | 선정 방식, 코퍼스 ID, 점수 변화 집계 |

## 다시 만들기

```
python test/public_data/corpus_v2/review_batch.py labels golden_prep/batch5/judgments.jsonl \
  --suggestions golden_prep/batch5/review_suggestions.jsonl --expected golden_prep/batch5/items.jsonl \
  --resolutions golden_prep/batch5/resolutions.json \
  --base golden_prep/batch3/labels_llm_v5.jsonl --out <새 파일>
```

이 명령은 p050 조건 변경 전의 라벨을 만듭니다. `revisions.jsonl`의 변경을 적용하면 `labels_llm_v6.jsonl`과 같아집니다. 경로는 `ai/test/public_data/corpus_v2/` 기준입니다.
