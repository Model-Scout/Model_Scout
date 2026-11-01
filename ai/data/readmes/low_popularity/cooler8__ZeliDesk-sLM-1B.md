---
language:
- ko
license: apache-2.0
datasets:
- HuggingFaceFW/fineweb-2
pipeline_tag: text-generation
library_name: transformers
tags:
- llama
- korean
- slm
- from-scratch
widget:
- text: "대한민국의 수도는"
  example_title: "Korean completion"
- text: "오늘 날씨가 좋아서"
  example_title: "Casual Korean"
---

# ZeliDesk-sLM-1B

> ⚠️ **Work in progress — pretraining at ~22% (4.5B / 20B tokens). Weights are intermediate and will be updated.**
> This repository is updated continuously as training progresses. Intermediate checkpoints are pinned with git tags (e.g. `ckpt-step17000`) so any published state remains reproducible.

**ZeliDesk-sLM-1B** is a 1.04B-parameter Korean language model pretrained **entirely from scratch** — random initialization, a custom-trained tokenizer, and a fully documented, reproducible training pipeline. It is not a fine-tune, continuation, or distillation of any existing model.

The goal of this project is not leaderboard performance. It is an **honest, fully backfillable Korean 1B baseline**: every stage — tokenizer training, data preprocessing, and pretraining — is reproducible from public notebooks, and the model card reports only verifiable numbers. No benchmark scores are claimed until they are actually measured.

## Architecture

Standard Llama-style decoder-only transformer (`LlamaForCausalLM`). Only the publicly documented architecture recipe (RMSNorm + SwiGLU + RoPE + GQA) is adopted — **no weights, tokenizer, or other artifacts are inherited from Meta Llama or any other model** (see [License & provenance](#license--provenance)).

| | |
|---|---|
| Parameters | ~1.040B (embeddings 67M, 6.5% of total) |
| Hidden size | 2048 |
| Layers | 16 |
| Attention heads | 32 (8 KV heads, GQA) |
| FFN size | 8192 (SwiGLU) |
| Context length | 2048 |
| RoPE θ | 500,000 |
| Normalization | RMSNorm, no bias terms |
| Embeddings | Tied input/output |
| Vocabulary | 32,768 |

### Tokenizer

Custom ByteLevel BPE with a 32,768-token vocabulary, trained from scratch on a sample of FineWeb-2 `kor_Hang`. Special tokens: `<|endoftext|>` (eos, id 0), `<|pad|>` (pad, id 1). This is a base model — no chat template is defined.

Measured fertility on held-out Korean web text (FineWeb-2 `kor_Hang` test split, 150 docs): **5.318 UTF-8 bytes/token ≈ 2.310 chars/token**.

## Training data

Pretrained on [HuggingFaceFW/fineweb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2), `kor_Hang` split (license: **ODC-By 1.0**), with a Chinchilla-style budget of **20B tokens**.

The tokenized data shards used for training are kept in a private repository because they are a re-processed derivative of the source dataset; instead, the original dataset ([HuggingFaceFW/fineweb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)) is linked here and the full preprocessing procedure is reproducible from the public notebooks.

## Training procedure

| Hyperparameter | Value |
|---|---|
| Total token budget | 20B (~76,293 steps) |
| Effective batch size | 262,144 tokens/step (micro-batch 8 × grad-accum 16 × ctx 2048) |
| Learning rate | 4e-4, cosine schedule |
| Warmup | 2,000 steps |
| Precision | bf16 mixed precision |
| Optimizer | AdamW (β₂ = 0.95, weight decay 0.1) |
| Hardware | Colab Pro+ G4 — RTX PRO 6000 Blackwell (96GB), ~45k tok/s measured |

## Intermediate evaluation

Every number below was actually measured on the published checkpoint — nothing is estimated or extrapolated. BPB (bits per byte) is the project's primary pretraining metric; it will be re-measured at later checkpoints and at completion, forming a public training curve.

| Checkpoint | Training progress | BPB ↓ | Token perplexity ↓ |
|---|---|---|---|
| `ckpt-step17000` | ~22% (~4.5B / 20B tokens) | **0.7742** | 17.35 |

**Methodology** (deterministic, reproducible): first 150 documents of FineWeb-2 `data/kor_Hang/test/000_00000.parquet` (held-out test split, disjoint from training data), in file order. Each document is prefixed with `<|endoftext|>` and truncated to a 2,048-token window; cross-entropy is summed over all document tokens and divided by the UTF-8 byte length of the exact decoded scored text: BPB = NLL_nats / ln(2) / bytes. Totals: 87,539 tokens / 465,560 bytes scored, float32 inference.

No standard benchmark scores (e.g. reasoning or knowledge suites) are published yet — the absence of those numbers is deliberate, not an oversight.

### Sample outputs (step 17000)

Unedited samples from the current checkpoint (`do_sample=True, top_p=0.9, temperature=0.8`, seed 42), shown to set expectations honestly — grammar and fluency are forming, factual grounding is not yet there:

> **대한민국의 수도는** 어디입니까? - "전라북도 전주시 완산구, 전주읍, 진안군 진안읍, …" *(fails to answer; drifts into place-name lists)*

> **오늘 날씨가 좋아서** 꽃도 활짝 폈다. 봄이 오면 들판에서 새싹이 움트듯, 꽃도 활짝 피겠지. 이곳, 이 길을 걷는 우리들도 이제 꽃처럼 활짝 피어나게 될 테니.

> **인공지능 기술의 발전은** 향후 더욱 가속화 될 것으로 예측합니다. - "Software Development" 저널에 실린 … *(fluent register, but fabricated citation)*

## License & provenance

Weights are released under **Apache-2.0**.

This model **does not inherit** any weights, tokenizer, or training artifacts from Meta Llama. It adopts only the openly published architecture recipe (RMSNorm, SwiGLU, RoPE, GQA) as implemented by the standard `LlamaForCausalLM` class in 🤗 Transformers, and was pretrained from random initialization. The Meta Llama Community License therefore does not apply to these weights.

Training data attribution: FineWeb-2 is released by HuggingFaceFW under ODC-By 1.0.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

repo = "cooler8/ZeliDesk-sLM-1B"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, torch_dtype="bfloat16")

inputs = tokenizer("대한민국의 수도는", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=64, do_sample=True, top_p=0.9)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

To load the pinned intermediate checkpoint instead of the moving `main` branch:

```python
model = AutoModelForCausalLM.from_pretrained(repo, revision="ckpt-step17000")
```

## Limitations

Read this section before using the model. It is intentionally thorough.

- **Training is incomplete.** The current weights represent ~22% of the planned 20B-token budget (~4.5B tokens). Output quality is far below what the finished model is expected to produce, and the weights on `main` will keep changing until training completes.
- **Base model only.** No instruction tuning, no RLHF, no safety alignment. It does not follow instructions or chat — it only continues text. Outputs may be incoherent, repetitive, factually wrong, or offensive, reflecting patterns in web-crawled data.
- **Korean only.** Trained exclusively on Korean (`kor_Hang`) text. English or other languages will produce degraded output.
- **1B-class capacity.** This is a small language model. It cannot be expected to match larger models on knowledge, reasoning, or generation quality — that is not its purpose.
- **Short context.** Maximum context length is 2,048 tokens.
- **No standard benchmark results yet.** Only the intermediate BPB measurement above has been published, with its full methodology. Any other capability numbers attributed to this model are not from us.
- **Web-data risks.** FineWeb-2 is filtered web text; despite filtering it may contain biases, inaccuracies, and personally identifiable information, which the model may reproduce.
- **Not for production or high-stakes use** in its current state — including medical, legal, or financial advice and any automated decision-making affecting people.

## 한국어 요약

ZeliDesk-sLM-1B는 **처음부터(from scratch)** 사전학습한 한국어 1.04B 파라미터 언어 모델입니다. Meta Llama의 가중치·토크나이저를 일절 상속하지 않고, 공개 표준 아키텍처 규격(RMSNorm + SwiGLU + RoPE + GQA)만 채택하여 랜덤 초기화에서 학습했습니다. 따라서 가중치는 Apache-2.0으로 공개됩니다.

- **현재 상태: 학습 진행 중 (~22%, 4.5B / 20B 토큰). 미완성 중간 가중치입니다.**
- 학습 데이터: FineWeb-2 한국어(`kor_Hang`) 스플릿 (ODC-By 1.0), 20B 토큰 예산
- 토크나이저: FineWeb-2 한국어 샘플로 자체 학습한 ByteLevel BPE 32,768 어휘
- 목표: 성능 경쟁이 아닌, **전 과정이 재현 가능한 정직한 한국어 1B 베이스라인**
- 중간 평가 (step 17000, 실측): FineWeb-2 한국어 held-out 테스트 스플릿 기준 **BPB 0.7742**, 토큰 perplexity 17.35. 측정 방법론은 위 Intermediate evaluation 섹션에 전부 공개.
- 베이스 모델이므로 지시 따르기·대화 능력이 없으며, 표준 벤치마크 점수는 아직 측정 전입니다. 검증된 숫자만 기재하는 것이 이 프로젝트의 원칙입니다.

## Citation

```bibtex
@misc{zelidesk-slm-1b,
  title  = {ZeliDesk-sLM-1B: A from-scratch Korean 1B language model},
  author = {ZeliAI},
  year   = {2026},
  url    = {https://huggingface.co/cooler8/ZeliDesk-sLM-1B}
}
```
