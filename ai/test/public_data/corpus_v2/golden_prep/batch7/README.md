# batch7: 골든셋 v8 (질의 분해 입력 비교의 미판정 138쌍)

`labels_llm_v8.jsonl`은 골든셋 v7(`batch6/labels_llm_v7.jsonl`)에 이 폴더의 판정 138쌍을 더한 라벨입니다. v7 이전 파일은 바꾸지 않았습니다.

- **대상:** [질의 분해 입력 비교](../../../retrieval/runs/2026-11-20_decompose_compare/report.md)의 네 입력(질문 원문, dataset_query, dataset_query + terms, 수작업 보조 검색어) 상위 10에서 v7이 판정하지 않은 쌍입니다. 대부분 분해 입력이 새로 끌어온 데이터입니다.
- **기준·방식:** batch6와 같습니다. 카드를 보고 한 LLM 1차 판정(`llm_first_pass`)이며, 비슷한 데이터의 v6·v7 판정과 맞췄습니다. 외부 API 호출은 없습니다.
- **결과:** 2점 1, 1점 28, 0점 104(off_topic 101, wrong_region 3), 보류 5. `review_batch.py validate` 위반 0, 경고 0입니다.
- **보류 5쌍:** p006 전북 음식보감(영양성분 수치 여부), p025 대전 실시간 주차장·p052 대전 초등학교(파일 제공 여부), p027 전국 버스 실시간 위치(서울 포함·도착 정보 여부), p053 한국사회보장정보원 어린이집 정보(제3자 권리).

## 다시 만들기 (`ai/` 기준)

```
B=test/public_data/corpus_v2/golden_prep/batch7
python -X utf8 test/public_data/corpus_v2/golden_prep/batch6/make_items.py --blind test/public_data/retrieval/runs/2026-11-20_decompose_compare/unjudged_blind.jsonl \
  --labels test/public_data/corpus_v2/golden_prep/batch6/labels_llm_v7.jsonl --out $B
python -X utf8 test/public_data/corpus_v2/golden_prep/batch6/make_judgments.py --dir $B --origin decompose_compare_unjudged
python -X utf8 test/public_data/corpus_v2/review_batch.py validate $B/judgments.jsonl --suggestions $B/review_suggestions.jsonl
python -X utf8 test/public_data/corpus_v2/review_batch.py labels $B/judgments.jsonl --suggestions $B/review_suggestions.jsonl \
  --resolutions $B/resolutions.json --base test/public_data/corpus_v2/golden_prep/batch6/labels_llm_v7.jsonl --out <새 파일>
```
