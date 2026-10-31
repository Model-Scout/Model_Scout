---
license: apache-2.0
language: [ko]
pretty_name: chatbot-ft evaluation records
---
# chatbot-ft 평가 기록

[chatbot-ft](https://github.com/bigglz/chatbot-ft) 의 벤치마크 결과와 LLM-as-a-judge 기록. `scripts/hf_store.py` 가 자동으로 동기화한다.

```
benchmarks/<모델>/                                        run_benchmark.py 결과 (summary.md/json, raw/, logs/)
judge/conversations/<모델>/<생성조건 해시>/<실행ID>.jsonl   모델별 대화 (generation_config.json 의 조건이 같으면 상대 모델과 무관하게 재사용)
judge/pairs/<A>_vs_<B>/judgments_<평가자>/<실행ID>.jsonl   판정 기록 (순서를 바꿔 2회)
judge/pairs/<A>_vs_<B>/summary_<평가자>.md/json, review_<평가자>/   집계·정성 검토 문서
```
