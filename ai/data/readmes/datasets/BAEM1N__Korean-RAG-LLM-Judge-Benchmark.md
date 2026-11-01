---
license: mit
language:
  - ko
size_categories:
  - 10K<n<100K
task_categories:
  - question-answering
  - text-retrieval
tags:
  - rag
  - llm-as-judge
  - korean
  - benchmark
configs:
  - config_name: consolidated
    data_files:
      - split: train
        path: data/consolidated.parquet
---

# Korean RAG LLM-as-Judge Benchmark

[allganize/RAG-Evaluation-Dataset-KO](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-KO)의 한국어 RAG 300 Q&A 위에 **46개 답변 생성 모델**의 답변과 **LLM-as-Judge 평가 결과**를 얹은 데이터셋입니다. 원문 문항·기준 답변·출처 PDF 메타데이터는 allganize 데이터셋을 그대로 따릅니다.

> 🔗 **분석 코드·단계별 실험 보고서**: <https://github.com/BAEM1N/RAG-Evaluation> · 📊 **요약 대시보드**: <https://rag.baeum.ai.kr>

---

## 🎯 한 줄 결론

**RAG 파이프라인 최적화 > 모델 업그레이드.** 동일 GPT-5.4를 쓰면서도 검색 파이프라인만 잘 짜면 GPT-5.4-pro(약 10배 비싼 모델)보다 **+6.0pp 높은 정확도(0.827)** 를 낸다.

| Pipeline | Generator | Accuracy |
|---|---|---:|
| 🥇 Cartesian winner: query2doc + Hybrid 7:3 + jina-reranker-m0 | GPT-5.4 | **0.827** |
| 단순 retrieval + 동일 GPT-5.4 | GPT-5.4 | 0.787 |
| 단순 retrieval + GPT-5.4-pro (10× 비쌈) | GPT-5.4-pro | 0.767 |
| Open-weight 1위 (gpt-oss-120b / kimi-k2.5) | Open Weights | 0.740 |

---

## 📊 데이터셋 구성

allganize 원본의 5개 도메인 × 60문항 = 300 Q&A. 표·이미지 기반 문항이 절반 가까이로, 단순 RAG가 어려워하는 케이스를 포함합니다.

| 도메인 | 문항 |  | context_type | 문항 |
|---|---:|---|---|---:|
| finance | 60 |  | paragraph | 148 |
| public | 60 |  | image | 57 |
| medical | 60 |  | table | 50 |
| law | 60 |  | text | 45 |
| commerce | 60 |  | | |
| **전체** | **300** |  | | |

## 🤖 답변 생성 모델 (46)

가중치 공개 여부로 **Open Weights**(직접 구동 가능)와 **Closed Weights**(API 전용)로 구분.

**Open Weights (27)** — Qwen(qwen3.5 9b/27b/122b-a10b), DeepSeek(r1-70b, v3.2, v4-flash/pro), gpt-oss(20b/120b), GLM(4.7/4.7-flash/5/5.1), MiniMax(m2.5/m2.7), Kimi(k2.5/k2.6), MiMo(v2.5/pro), exaone3.5-32b, mistral-small-24b, phi4-14b, lfm2-24b, nemotron-3-nano-30b 등

**Closed Weights (19)** — GPT-5.4(+mini/nano/pro), Claude(opus-4-7, sonnet-4-5/4-6, haiku-4-5, +thinking), Gemini(3-pro/flash, 3.1-pro/flash-lite, +thinking), Qwen(qwen3-max-thinking, qwen3.6-plus), Solar-pro-3, Grok-4.20

## ⚖️ 평가 (LLM-as-Judge)

allganize 방법론을 따라 **4-metric majority-O** 방식으로 채점합니다. judge LLM 이 각 답변을 4개 지표로 1–5점 채점하고, **4개 중 2개 이상이 ≥4점이면 정답(O)** 으로 판정합니다.

| 지표 | 의미 |
|---|---|
| similarity | 기준 답변과의 의미 유사성 |
| correctness | 사실 정확성 |
| completeness | 핵심 포인트 누락 여부 |
| faithfulness | 컨텍스트 근거 여부 (hallucination) |

- 본 데이터셋의 `_ox` 컬럼은 **18-judge 평가 시점** 기준 판정입니다.
- 요약 대시보드([rag.baeum.ai.kr](https://rag.baeum.ai.kr))에서는 judge 를 **20종(closed API 9 + open-weight 11)** 으로 확장하고, 384 cartesian 조합을 GPT-5.4 / Qwen3.6-35B-A3B 두 judge 로 비교합니다.
- **Judge robustness**: 같은 384 조합을 open judge(Qwen3.6)로 재채점 시 평균 +4.1pp 더 후하지만(78.0% → 82.1%) 조합 간 상대 순위는 보존 — 절대 점수보다 다수 judge·상대 순위로 해석할 것.

## 🗂 데이터 스키마 (`consolidated.parquet`)

300 행 × 98 열.

| 컬럼 | 설명 |
|---|---|
| `domain` | finance / public / medical / law / commerce |
| `question` | 질문 (allganize 원본) |
| `target_answer` | 기준 답변 |
| `target_file_name` / `target_page_no` | 출처 PDF · 페이지 |
| `context_type` | paragraph / image / table / text |
| `<model>_answer` | 각 generator(46종)의 생성 답변 |
| `<model>_ox` | 해당 답변의 judge 판정 (`O` / `X`) |

## 🚀 사용법

```python
from datasets import load_dataset

ds = load_dataset("BAEM1N/Korean-RAG-LLM-Judge-Benchmark", "consolidated")
row = ds["train"][0]
print(row["question"], row["target_answer"])
print(row["gpt-5.4_answer"], row["gpt-5.4_ox"])   # 특정 모델 답변·판정

# 모델별 도메인 정확도
import pandas as pd
df = ds["train"].to_pandas()
acc = (df.groupby("domain")["gpt-5.4_ox"].apply(lambda s: (s == "O").mean()))
print(acc)
```

## 📚 함께 보기

- **단계별 실험 보고서·재현 코드**: [github.com/BAEM1N/RAG-Evaluation](https://github.com/BAEM1N/RAG-Evaluation) — Loader/Parser/Embedding/Retriever/Pre·Post-Retriever/Generation 6단계 + 384 cartesian 전수 분석, PAPER.md, REPORT.md
- **요약 대시보드**: [rag.baeum.ai.kr](https://rag.baeum.ai.kr) — 단계별 차트, 리더보드(judge 전환), RAG 결과 탐색, 벡터스토어 벤치
- **원문 코퍼스·문항**: [allganize/RAG-Evaluation-Dataset-KO](https://huggingface.co/datasets/allganize/RAG-Evaluation-Dataset-KO)

## 📄 라이선스 / 인용

- 라이선스: MIT (생성 답변·평가 결과). 원문 문항·PDF 는 allganize 원본 라이선스 준수.

```bibtex
@misc{baem1n2026koreanrag,
  title  = {Korean RAG LLM-as-Judge Benchmark},
  author = {BAEM1N},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/datasets/BAEM1N/Korean-RAG-LLM-Judge-Benchmark}},
  note   = {Built on allganize/RAG-Evaluation-Dataset-KO}
}
```
