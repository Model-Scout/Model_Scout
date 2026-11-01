---
language:
  - ko
license: gemma
library_name: peft
pipeline_tag: sentence-similarity
base_model: google/embeddinggemma-300m
tags:
  - sentence-transformers
  - feature-extraction
  - korean
  - fiction
  - stylometry
  - authorship-analysis
  - lora
---

# Munche-v2-768

**Munche-v2-768**은 한국어 장르소설의 *내용*보다 문장 운용, 서술 리듬, 형태·기능어 사용과 같은 *문체*를 비교하기 위해 학습한 768차원 텍스트 임베딩 모델입니다. [`google/embeddinggemma-300m`](https://huggingface.co/google/embeddinggemma-300m)의 원래 768차원 pooling/projection 경로를 유지하면서, style LoRA를 학습했습니다.

이 모델은 일반 의미 검색 모델의 대체재가 아닙니다. 동일·유사한 내용을 찾는 것보다 서로 다른 작품에 반복되는 작가적 문체를 비교하는 용도로 설계했습니다.

![External benchmark comparison](assets/benchmark_comparison.png)

## 주요 특징

- **원본 768차원 head 유지:** 새로운 projection head를 덧붙이지 않고 EmbeddingGemma의 mean pooling과 두 projection layer를 그대로 사용합니다.
- **Style LoRA:** 동결된 backbone의 `q_proj`, `v_proj`, `o_proj`에 rank 16, alpha 32, dropout 0.05의 LoRA를 학습했습니다. 원본 pooling/projection layer는 동결했습니다.
- **표준 PEFT adapter:** LoRA를 병합하지 않고 학습된 adapter 그대로 제공합니다.
- **한 공간에서 공동 학습:** 작품, 작가, 다중 prototype, content-hard, counterfactual 신호가 모두 최종 768차원 cosine 공간에 직접 작용합니다.
- **긴 텍스트:** 학습 구간은 512/768/1024 token이며, 1024 token을 넘는 입력은 512 stride sliding window와 overlap-corrected spherical pooling을 권장합니다.
- **보조 과제:** 연재 시기, Kiwi stylometry, Human/AI 분류는 별도 보조 head로 학습하되 encoder gradient를 제한하거나 후반에 감쇠시켰습니다. 기본 임베딩 API는 이 보조 예측값이 아니라 L2-normalized 768차원 벡터를 반환합니다.

## 사용법

EmbeddingGemma의 문서 prompt를 포함해 입력하는 것을 권장합니다.

```python
import torch
from peft import PeftModel
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("google/embeddinggemma-300m").to(torch.bfloat16)
model[0].auto_model = PeftModel.from_pretrained(
    model[0].auto_model,
    "Baragi-AI/Munche-v2-768",
)
model.max_seq_length = 1024

texts = [
    "title: none | text: 그는 대답하지 않았다. 창밖의 비가 오래된 지붕을 두드렸다.",
    "title: none | text: 나는 검을 내려놓았다. 해야 할 말은 이미 모두 끝난 뒤였다.",
]

embeddings = model.encode(
    texts,
    normalize_embeddings=True,
    convert_to_numpy=True,
)
similarity = embeddings @ embeddings.T
```

한 작품 전체를 임베딩할 때는 다음 절차를 권장합니다.

1. 실제 tokenizer 기준 1024-token window와 512-token stride를 사용합니다.
2. 각 window를 개별적으로 L2 normalize합니다.
3. 겹친 token이 여러 번 집계되지 않도록 window별 token coverage 역수를 가중치로 사용합니다.
4. 가중 평균 결과를 다시 L2 normalize합니다.
5. 작품 길이 편향을 줄이려면 먼저 회차별로 pooling한 뒤 회차 벡터를 동일 가중 평균합니다.

이 모델은 BF16으로 학습·평가했으며 FP16 activation은 지원하지 않습니다.

## 모델 구조

```text
text + document prompt
  → frozen EmbeddingGemma 300M backbone
     + trainable Q/V/O LoRA
  → frozen original mean pooling
  → frozen original Dense → Dense (768d)
  → L2 normalization
  → style embedding z ∈ R^768
       ├─ scalar ordinal publication head    [training auxiliary]
       ├─ Kiwi stylometry MLP                [training auxiliary]
       └─ Human/AI binary head               [training auxiliary]
```

## 학습 방법

### 데이터 분할과 sampling

- 작가가 확인된 데이터는 작가 연결요소 단위로 train/validation/test를 분리했습니다. 같은 작가의 여러 작품과 같은 작품의 모든 파생 window는 하나의 split에만 존재합니다.
- 정확 중복과 near-duplicate 연결요소를 먼저 처리해 `processed_data`와 파생 counterfactual 데이터의 누수를 줄였습니다.
- 긴 작품이 학습을 독점하지 않도록 작품을 먼저 균형 sampling하고, 작품 안에서 떨어진 위치의 window를 선택했습니다.
- 일반 metric batch는 `8 authors × 3 works × 2 windows`입니다. 인간 작품 metric loss는 매 두 번째 step에 적용했습니다.
- 최종 단계에서는 10 step마다 한 번 `4 authors × 4 works × 3 windows`의 prototype 전용 batch를 사용했습니다.

### 최종 embedding에 직접 적용한 목적함수

1. **Work metric loss** — 같은 작품의 서로 떨어진 구간을 가깝게 학습합니다. 같은 작가의 다른 작품은 작품 loss의 negative에서 제외합니다.
2. **Cross-work author loss** — 같은 작가의 서로 다른 작품을 가깝게 하되, 후반에는 단일 centroid 압력을 감쇠합니다.
3. **Leave-one-work-out multi-prototype loss** — 작가당 `N=3` prototype을 support 작품으로 만들고, 제외한 query 작품의 window를 분류합니다.
4. **Work-balanced prototype construction** — 작품별 local assignment를 먼저 계산하고 작품마다 같은 가중치를 주어, window가 많은 작품이 prototype을 지배하지 않게 합니다.
5. **Cross-work coverage + diversity** — 각 prototype이 최소 두 작품에서 지지를 받도록 effective-work 및 second-work-mass hinge를 적용하고, 충분히 지지되는 prototype끼리만 separation을 유도합니다. Prototype 전용 batch에서는 coverage 기여를 1.5배로 적용했습니다.
6. **Semantic hard negatives** — 동결된 원본 EmbeddingGemma에서 의미가 가까운 다른 작가의 구간 20개를 찾아 style 공간에서는 멀어지게 합니다.
7. **Conditional decorrelation** — 같은 작가 안에서 내용 semantic embedding이 움직이는 방향을 style embedding이 그대로 따르지 않도록 cross-covariance를 제한합니다. 초반에는 방향 형성에 사용하고 후반에는 guardrail로 낮췄습니다.
8. **Human/LLM counterfactual ranking** — 인간 원문과 내용 보존 LLM rewrite를 구분하도록, 인간 작가·작품 positive가 rewrite보다 가깝게 학습합니다.
9. **Synthetic hierarchy** — 동일 내용 blueprint에서 `same recipe > same model/different prompt > different model/same prompt > different model/different prompt` 순서를 유도하고 후반에는 감쇠합니다.

### 보조 과제와 schedule

- **Publication:** 5개로 구분된 시기를 기준으로 하여 하나의 연속 시기 scalar를 예측합니다. 학습 가능한 ordered cutpoint, interval-aware NLL/Huber, chronological ranking을 함께 사용하며 class-balanced 전용 batch를 4 step마다 학습했습니다.
- **Kiwi stylometry:** 인간 train split에서 window 단위 신뢰도로 16–24개 특징을 선택하고, hidden 256 MLP로 인간·AI window의 표준화된 지표를 회귀했습니다. 문체 방향을 잡는 초기 신호로 사용한 뒤 감쇠했습니다.
- **Human/AI:** 인간 본문, counterfactual rewrite, synthetic fiction을 출처별 균형 기여로 학습했습니다. 보조 head의 encoder gradient는 0.3배로 제한했습니다.
- **Optimization:** BF16, AdamW, LoRA LR `2e-5`, auxiliary head LR `8e-5`/`2e-4`, weight decay `0.01`, max gradient norm `50`; gradient checkpointing은 사용하지 않았습니다.
- **Ramps/fades:** hard-negative, counterfactual, decorrelation, synthetic, Human/AI loss를 ramp로 도입했습니다. Stylometry와 synthetic은 초기 유도 후 감쇠하고, decorrelation은 중후반 guardrail로 유지했습니다.


## 외부 평가

### 프로토콜

- 한국어 장르소설 **11 authors / 80 works / 640 segments**
- 작품마다 무작위 위치에서 동일하게 8개 구간 추출
- 입력 길이 1024 tokens, 모든 모델에 동일한 query/gallery 사용
- 비교 모델: 수학적 무작위 기댓값, 원본 EmbeddingGemma 300M, 전 세대 [`Baragi-AI/Munche-768`](https://huggingface.co/Baragi-AI/Munche-768), Munche-v2-768
- 이전 평가 데이터에 Munche-768의 학습 노출이 확인되어 해당 결과는 폐기하고, 별도의 원시 작가 말뭉치에서 다시 표본을 추출했습니다.
- 무작위 결과는 난수 시뮬레이션이 아니라 실제 candidate/positive 수에 따른 closed-form expectation입니다.

| Metric | Random | EmbeddingGemma 300M | Munche-768 | **Munche-v2-768** |
|---|---:|---:|---:|---:|
| Same-work mAP | 0.0221 | 0.5680 | 0.7979 | **0.8233** |
| Same-work Recall@1 | 0.0120 | 0.8328 | **0.9484** | **0.9484** |
| Cross-work author mAP | 0.0882 | 0.1973 | 0.2960 | **0.3433** |
| Cross-work author Recall@1 | 0.0794 | 0.3726 | 0.5302 | **0.6395** |
| Cross-work author MRR | 0.2161 | 0.5163 | 0.6368 | **0.7205** |
| N=3 prototype, 2 support works, macro top1 | 0.0909 | 0.4599 | 0.5064 | **0.6116** |
| N=3 prototype, 3 support works, macro top1 | 0.0909 | 0.4981 | 0.5482 | **0.6205** |
| Content-hard pairwise accuracy | 0.5000 | 0.0888 | 0.5719 | **0.6213** |
| Content-hard top1 | 0.6998 | 0.3726 | 0.7412 | **0.7981** |

`Content-hard`의 negative는 원본 EmbeddingGemma semantic space에서 가장 가까운 다른 작가 구간입니다. 따라서 EmbeddingGemma 자체의 낮은 content-hard 점수는 일반 의미 검색 성능 저하를 뜻하지 않으며, 같은 semantic space로 고른 의도적인 adversarial baseline입니다. Content-hard top1의 무작위 기댓값이 높은 것은 query당 same-author positive가 다수인 반면 hard negative를 20개로 제한했기 때문입니다.

### 작가 단위 paired bootstrap

Munche-768 대비 Munche-v2-768의 cross-work 차이를 작가를 표본 단위로 20,000회 복원추출했습니다.

| Metric | Paired difference | 95% bootstrap CI | Better authors |
|---|---:|---:|---:|
| mAP | **+0.0472** | `[+0.0107, +0.0850]` | 8 / 11 |
| Recall@1 | **+0.1093** | `[+0.0339, +0.1795]` | 9 / 11 |
| MRR | **+0.0836** | `[+0.0221, +0.1427]` | 9 / 11 |

## 해석과 제한사항

- Same-work retrieval은 인물·세계관·사건 단서를 사용할 수 있으므로 문체 독립성을 단독으로 증명하지 않습니다. **Cross-work**, **prototype**, **content-hard** 지표를 우선해서 보세요.
- 모델은 한국어 장르소설에 특화되어 있습니다. 비문학, 번역문, 짧은 문장, 시, 채팅, 영어 등에서는 성능을 보장하지 않습니다.
- 문체 유사도는 저자 신원의 법적·사실적 증거가 아닙니다. 공동 집필, 편집, 장르 관습, 시대, 플랫폼 규칙, 의도적 모방에 영향을 받을 수 있습니다.
- Human/AI 보조 학습은 특정 생성 모델과 데이터 분포에 의존합니다. 이 임베딩을 단독 AI 탐지기로 사용하지 마세요.
- 저자 추적, 익명 사용자 식별, 표절 단정 등 개인에게 불이익을 줄 수 있는 용도에는 인간 검토와 별도 검증이 필요합니다.

## 라이선스

이 모델은 EmbeddingGemma 파생 모델이며 **Gemma Terms of Use**와 **Gemma Prohibited Use Policy**를 따릅니다. 베이스 모델 파일을 받으려면 Hugging Face에서 Google의 사용 조건에 동의해야 할 수 있습니다. 자세한 내용은 [EmbeddingGemma 모델 카드](https://huggingface.co/google/embeddinggemma-300m)를 확인하세요.

## Citation

EmbeddingGemma를 사용하는 경우 원 모델 논문을 인용하세요.

```bibtex
@article{embedding_gemma_2025,
  title   = {EmbeddingGemma: Powerful and Lightweight Text Representations},
  author  = {Schechter Vera, Henrique and others},
  year    = {2025},
  url     = {https://arxiv.org/abs/2509.20354}
}
```
