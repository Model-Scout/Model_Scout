# batch8: 골든셋 v9 (실험용 데이터 분해의 미판정 67쌍)

`labels_llm_v9.jsonl`은 v8(`batch7/labels_llm_v8.jsonl`)에 이 폴더의 판정 67쌍을 더한 라벨입니다. 이전 파일은 바꾸지 않았습니다.

- **대상:** [실험용 데이터 분해 비교](../../../retrieval/runs/2026-11-21_decompose_v2/report.md)의 다섯 입력·필터 조합 상위 10에서 v8이 판정하지 않은 쌍입니다. 대부분 개선 분해 검색 문장이 새로 끌어온 데이터입니다.
- **기준·방식:** batch6·7과 같습니다(카드 기반 LLM 1차 판정, 외부 API 없음).
- **결과:** 2점 1, 1점 6, 0점 59(off_topic 55, wrong_region 3, wrong_delivery 1), 보류 1(p027 서울 실시간 도시데이터: 버스 도착 정보 여부). `validate` 위반 0, 경고 1(사유는 `resolutions.json`).

## 다시 만들기 (`ai/` 기준)

```
B=test/public_data/corpus_v2/golden_prep/batch8
python -X utf8 test/public_data/corpus_v2/golden_prep/batch6/make_items.py --blind test/public_data/retrieval/runs/2026-11-21_decompose_v2/unjudged_blind.jsonl \
  --labels test/public_data/corpus_v2/golden_prep/batch7/labels_llm_v8.jsonl --out $B
python -X utf8 test/public_data/corpus_v2/golden_prep/batch6/make_judgments.py --dir $B --origin decompose_v2_unjudged --judged-on 2026-11-21
python -X utf8 test/public_data/corpus_v2/review_batch.py labels $B/judgments.jsonl --suggestions $B/review_suggestions.jsonl \
  --resolutions $B/resolutions.json --base test/public_data/corpus_v2/golden_prep/batch7/labels_llm_v8.jsonl --out <새 파일>
```
