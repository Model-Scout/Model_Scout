# Dense-only와 Sparse(BM25 shadow) 비교

골든셋 `/Users/baiohelseu/Desktop/Project/Model_Scout/test/retrieval_queries.jsonl`의 48개 중 30개를 고정 선택했다.
선택은 표준 질의 27개(benchmark q31~q33 포함)와 adversarial q34/q37/q39 3개이며, 9개 task·두 pool·수치 조건·benchmark 조건을 포함한다.

## 평가 범위

- Dense: 기존 `stage4_retrieval_validation.json`의 vector 실행 결과를 재사용했다. 새 OpenAI 임베딩 호출은 하지 않았다.
- Sparse: OpenSearch의 `multi_match`와 같은 field boost를 적용한 로컬 BM25 shadow index다. 로컬 OpenSearch(`localhost:9200`)가 없어 서버 latency는 측정하지 않았다.
- Recall@5: 사람이 판정한 relevant model ID가 없으므로 진짜 semantic Recall@5는 계산할 수 없다. 아래 agreement는 dense top-5를 기준으로 한 비교 proxy다.
- Exact keyword hit는 lexical 검색에 유리한 지표이므로 sparse의 절대 정확도 증거로 해석하지 않는다.

## 결과

| 지표 | Dense-only | Sparse BM25 shadow |
|---|---:|---:|
| Dense top-5와 Sparse top-5 agreement (proxy) | - | 0.227 평균 / 0.000 중앙값 |
| Exact keyword hit@5 | 0.280 | 0.407 |
| 검색 rank latency 평균 (ms) | 0.044 | 17.472 |
| 검색 rank latency p95 (ms) | 0.118 | 78.197 |

Dense latency는 query embedding API 호출 시간을 제외한 로컬 vector rank 비용이다. 실제 서비스에서는 OpenAI query embedding 네트워크 시간이 추가된다.

## 질의별 결과

| 질의 | 후보 | agreement@5 | Dense keyword hit | Sparse keyword hit | Dense ms | Sparse ms |
|---|---:|---:|---:|---:|---:|---:|
| `q01_ko_classification_cpu` | 68 | 0.20 | 5/5 | 5/5 | 0.035 | 2.803 |
| `q02_ko_sentence_embedding` | 380 | 0.20 | 0/5 | 0/5 | 0.021 | 13.793 |
| `q03_ko_document_embedding` | 135 | 0.20 | 5/5 | 5/5 | 0.031 | 5.326 |
| `q04_ko_asr` | 234 | 0.20 | 5/5 | 5/5 | 0.014 | 9.507 |
| `q05_ko_translation` | 239 | 0.00 | 0/5 | 0/5 | 0.014 | 9.251 |
| `q06_ko_summarization` | 6 | 0.80 | 0/5 | 0/5 | 0.005 | 0.240 |
| `q07_ko_qa` | 6 | 1.00 | 0/5 | 0/5 | 0.005 | 0.608 |
| `q08_ko_generation_long_context` | 1172 | 0.20 | 5/5 | 5/5 | 0.072 | 79.581 |
| `q09_ko_multimodal` | 385 | 0.00 | 0/5 | 0/5 | 0.050 | 13.566 |
| `q10_ko_small_low_popularity` | 1313 | 0.00 | 0/5 | 5/5 | 0.612 | 90.204 |
| `q11_ko_known_hardware` | 374 | 0.00 | 5/5 | 5/5 | 0.022 | 13.926 |
| `q13_small_cpu_classifier` | 60 | 0.00 | 0/5 | 1/5 | 0.006 | 2.310 |
| `q14_semantic_search_embedding` | 435 | 0.00 | 0/5 | 0/5 | 0.023 | 15.894 |
| `q15_long_context_embedding` | 132 | 0.00 | 0/5 | 0/5 | 0.008 | 5.052 |
| `q16_realtime_asr_small` | 60 | 0.20 | 0/5 | 0/5 | 0.005 | 2.630 |
| `q18_long_document_summarization` | 2 | 1.00 | 0/5 | 0/5 | 0.005 | 0.095 |
| `q19_small_question_answering` | 5 | 1.00 | 0/5 | 0/5 | 0.005 | 0.340 |
| `q20_long_context_generation` | 522 | 0.00 | 0/5 | 3/5 | 0.027 | 33.224 |
| `q21_vision_language_ocr` | 385 | 0.00 | 0/5 | 0/5 | 0.023 | 14.361 |
| `q22_low_popularity_generation` | 1313 | 0.00 | 0/5 | 0/5 | 0.156 | 76.504 |
| `q23_known_embedding_metadata` | 374 | 0.00 | 0/5 | 0/5 | 0.020 | 13.598 |
| `q24_small_sentence_similarity` | 248 | 0.00 | 0/5 | 0/5 | 0.013 | 9.183 |
| `q26_on_device_asr` | 32 | 0.40 | 0/5 | 0/5 | 0.004 | 1.392 |
| `q27_very_long_context_generation` | 1092 | 0.00 | 0/5 | 5/5 | 0.063 | 66.528 |
| `q31_mteb_arguana_ndcg` | 435 | 0.00 | 4/5 | 5/5 | 0.022 | 16.425 |
| `q32_mteb_embedding_evidence` | 435 | 0.40 | 4/5 | 5/5 | 0.023 | 15.860 |
| `q33_asr_wer_evidence` | 234 | 0.00 | 2/5 | 5/5 | 0.013 | 8.979 |
| `q34_ko_summarization_small_long` | 0 | 0.00 | 0/5 | 0/5 | 0.002 | 0.025 |
| `q37_ko_embedding_long_small` | 62 | 0.00 | 5/5 | 5/5 | 0.006 | 2.665 |
| `q39_ko_qa_context` | 2 | 1.00 | 2/5 | 2/5 | 0.004 | 0.297 |

## 해석

Sparse는 모델명, task, language, parameter/context 같은 명시적 조건과 MTEB·WER 같은 keyword가 질의에 직접 포함될 때 강점이 있다.
Dense는 표현이 다른 한국어 질의의 의미 유사도와 README semantic summary를 보완한다. 따라서 현재 자료만으로 sparse를 dense의 대체로 채택하지 않고, 위 결과를 기준으로 hybrid 후보를 검토하는 것이 안전하다.
이번 비교만으로 sparse 도입을 확정할 수는 없다. hard-filter 통과 여부는 같지만 사람의 relevant model ID 라벨이 없고, latency도 서로 다른 구현(local NumPy와 Python BM25)에서 측정되었다.
정식 Recall@5 결론을 내리려면 질의별 relevant model ID를 사람이 라벨링한 별도 golden relevance set을 추가해야 한다.
