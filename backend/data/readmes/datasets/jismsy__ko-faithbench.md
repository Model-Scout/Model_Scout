---
license: cc-by-sa-4.0
language:
- ko
task_categories:
- text-classification
tags:
- hallucination-detection
- faithfulness
- benchmark
- korean
- adversarial
size_categories:
- 1K<n<10K
pretty_name: Ko-FaithBench
---

# Ko-FaithBench — 한국어 충실성(faithfulness) 판별 벤치마크

**Ko-FaithBench** is a Korean (context, answer) faithfulness benchmark: given a Wikipedia passage and a generated answer, judge whether the answer is fully supported by the passage (SUPPORTED) or contains exactly one subtle factual error (HALLUCINATED). It ships in two tiers — a **Standard set** (782 public + 200 sealed) and an adversarially-filtered **Hard set** (280 public + 100 sealed) that frontier LLM judges were unable to solve during construction.

> 우리는 이 벤치로 **우리 모델부터 깼습니다.** 아래 리더보드의 첫 줄이 우리 것입니다.

## 왜 만들었나

한국어에는 (지문, 답변) 충실성 판별을 위한 공개 벤치마크가 사실상 없습니다. RAG·요약 서비스가 쏟아지는데 "이 답이 근거에 충실한가"를 잴 자가 없습니다. Ko-FaithBench는 그 측정을 위한 공정한 심판대를 목표로 하며, 제작 과정의 모든 선택(생성 모델, 검증 모델, 필터 모델)과 그로 인한 **자격 제한을 아래에 전부 공개**합니다.

## 구성

| 셋 | 공개 | 봉인 | 라벨 균형 | 설명 |
|---|---|---|---|---|
| Standard | 782 | 200 | ≈50:50 | 위키 지문 + 6유형 환각. 이중검증 통과쌍 |
| Hard | 280 | 100 | 50:50 | 프런티어 LLM 판별자가 오판한 쌍만 채택(adversarial filtering) |

- 환각 유형: Standard=수치왜곡·주체교체·부정/시제반전·무근거추가·부분사실·과잉일반화 / Hard=한정사삽입·주체혼동·부분사실·관계연쇄·유도계산·시제상전이
- 각 레코드: `id, context, answer, label, category, source(위키 문서명), generator, verification`
- 봉인셋은 비공개로 유지하며 SHA256만 공개합니다(`MANIFEST.json`). 봉인셋 평가는 운영자가 대행하고 결과만 게시합니다 — 벤치 과적합·오염 검출이 목적입니다.

## 제작 방법 (전문 공개)

1. **지문**: 한국어 위키피디아 무작위 문단(1~2문단, 원문 유지·재작성 금지)
2. **생성**: GLM-5.2가 지문당 (supported, hallucinated) 쌍 생성 — 오류는 정확히 하나, 표면상 성실한 요약처럼
3. **라벨 검증**: GLM-5.2 셀프체크 + Qwen3.6-35B-A3B 독립 재판정 — **둘 다 라벨과 일치한 쌍만 채택**, 불일치는 폐기(리뷰 큐)
4. **Hard 필터**: 검증 통과쌍 중 **DeepSeek-V4-Flash가 오판한 쌍만** Hard set으로 채택 (5라운드, 채택률 11~15%)
5. **균형화**: Hard의 HALLUCINATED에는 같은 지문에서 검증 통과한 SUPPORTED 형제를 짝으로 배치(재구성·단정 문체로 난도 정합, `pair_role` 필드로 구분)
6. **품질 감사**: 라벨×유형 균형, 길이 지름길 검사(길이만으로 라벨 예측 AUC 0.545 = 통과)

## ⚠️ 심판 자격 제한 (Judge Disqualification)

제작에 관여한 모델은 해당 셋의 피평가자로서 **점수가 무효**입니다. 이를 숨기지 않고 명시합니다:

| 모델 | Standard | Hard | 사유 |
|---|---|---|---|
| GLM-5.2 | ❌ 무효 | ❌ 무효 | 생성자+검증자 (자기참조) |
| Qwen3.6-35B-A3B | ❌ 무효 (측정치 0.993=동어반복) | ❌ 무효 | 검증자 |
| DeepSeek-V4 계열 | ⭕ 유효 (0.991) | ❌ 무효 (필터 기준이므로 구조상 ~50%) | Hard 필터 |
| 그 외 모든 모델 | ⭕ 유효 | ⭕ 유효 | — |

## 리더보드 (2026-07-08 갱신, 제작자 측정)

| 모델 | 크기 | Standard acc | Hard acc | 비고 |
|---|---|---|---|---|
| DeepSeek-V4-Flash (zero-shot) | 284B MoE | **0.991** | — (무효) | Hard 필터 모델이라 Hard 점수는 구조상 무의미 |
| [ko-hallucheck-v3](https://huggingface.co/jismsy/ko-hallucheck-v3) (제작자 모델) | 0.6B | **0.882** | **0.758** | AUROC 0.951/0.824. 교차 생성기(DeepSeek 출제) 실측 0.704 — 학습이 본 벤치와 같은 생성기 계열이라 Standard는 다소 후한 숫자임을 명시 |
| EXAONE-3.5 (zero-shot) | 7.8B | 0.741 | 0.500 | Hard는 chance |
| gemma3 (zero-shot) | 4B | 0.554 | 0.500 | |
| ko-hallucheck-v1 (제작자 구모델) | 0.6B | 0.780 | 0.521 | Hard에서 문체 휴리스틱으로 동작(v3에서 수리) |

Hard set에서 범용 zero-shot 모델이 일제히 0.500(chance)인 것은 본 셋의 난도를 보여줍니다. 제작자 모델의 학습 데이터는 본 벤치와 지문이 격리되어 있으나 생성기(GLM 계열)가 겹치므로, 제3자 모델과의 엄밀 비교에는 교차 생성기 수치를 참고하십시오.

우리 판별 모델(jismsy/ko-hallucheck-v1)의 성적을 그대로 게시합니다. Standard에서 프런티어 대비 -21%p, Hard에서 chance 수준입니다. 이 벤치의 존재 이유가 바로 이런 격차를 드러내는 것이며, 제작자의 모델이라고 예외가 아닙니다.

## 알려진 한계 (정직 고지)

1. **LLM 생성 데이터**: 환각과 충실 답변 모두 GLM-5.2 생성물로, 사람이 쓴 자연 환각의 분포와 다를 수 있습니다.
2. **인간 검증**: **아직 사람 검수를 거치지 않았습니다** (human validation: pending). 현재 라벨 품질의 근거는 이중 모델 교차검증뿐입니다. 무작위 표본 인간 감사를 v0.2.1에서 수행해 오류율을 이 자리에 게시할 예정이며, 그 전까지 본 벤치는 autonomous end-to-end 산출물로 취급해주십시오. 라벨 이의는 이슈로 받습니다(확인 시 수정·명시).
3. **Hard set의 필터 의존**: "어렵다"의 기준이 DeepSeek-V4-Flash 단일 모델의 오판입니다. 다른 프런티어에는 다르게 어려울 수 있습니다.
4. **오류 밀도**: 모든 HALLUCINATED는 오류가 정확히 1개인 설계로, 다중 오류·부분 환각 상황은 다루지 않습니다.
5. **도메인**: 위키피디아 백과사전 문체에 한정됩니다. 뉴스·법률·의료 등 타 도메인 일반화는 보장하지 않습니다.
6. **공개셋 오염 시계**: 공개분은 학습 데이터로 흡수될 수 있습니다. 시점 비교·공식 점수는 봉인셋 평가를 권장합니다.

## 사용법

```python
import json
rows = [json.loads(l) for l in open("data/standard_public.jsonl", encoding="utf-8")]
# 각 row: {"context": 지문, "answer": 답변, "label": "SUPPORTED"|"HALLUCINATED", ...}
```

봉인셋 공식 평가·등재 요청: 이슈로 문의해주세요. 평가는 운영자 인프라에서 실행되며 방법론·프롬프트는 본 저장소에 공개된 것과 동일합니다.

## 라이선스·출처

- **데이터**: CC BY-SA 4.0 — `context`는 한국어 위키피디아(CC BY-SA 4.0) 원문이며 각 레코드의 `source` 필드에 문서명을 표기했습니다.
- **코드**: Apache-2.0
- 생성·검증에 사용한 모델: GLM-5.2, Qwen3.6-35B-A3B, DeepSeek-V4-Flash (각 모델 제공자의 이용약관에 따름)

## 인용

```bibtex
@misc{kofaithbench2026,
  title={Ko-FaithBench: A Korean Faithfulness Benchmark with an Adversarially-Filtered Hard Set},
  author={ianwoo},
  year={2026},
  url={https://github.com/REPLACE/ko-faithbench}
}
```
