---
language:
- ko
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- translation
- korean
- jeju
- dialect
- jejueo
- small-llm
- from-scratch
- bidirectional-translation
datasets:
- aihub-jeju-dialect
metrics:
- bleu
- chrf
- exact_match
model-index:
- name: jeju-korean-translator
  results:
  - task:
      type: translation
      name: Jeju → Standard Korean (d2s)
    metrics:
    - type: bleu
      value: 77.67
      name: BLEU
    - type: chrf
      value: 84.19
      name: CHRF++
    - type: exact_match
      value: 51.0
      name: Exact Match (%)
  - task:
      type: translation
      name: Standard Korean → Jeju (s2d)
    metrics:
    - type: bleu
      value: 60.97
      name: BLEU
    - type: chrf
      value: 70.02
      name: CHRF++
    - type: exact_match
      value: 30.0
      name: Exact Match (%)
---

# Jeju ↔ Standard Korean Translator

A compact (≈88M parameter) decoder-only language model trained **from scratch** for
**bidirectional translation between the Jeju dialect (제주 방언, Jejueo) and Standard
Korean (표준어)**. The model uses a Qwen3-style architecture with per-head QK-Norm
and is served as a single checkpoint that handles both translation directions via a
prefix control token.

> 88M 디코더 전용 LLM을 1.4M개의 제주 방언↔표준어 평행 코퍼스로
> 처음부터 학습한 양방향 번역 모델입니다. 단일 모델·단일 체크포인트로 두 방향을 모두 처리합니다.

---

## ✨ Highlights

- **From-scratch pretraining**: no parent checkpoint; trained on a single H100 in ~4 hours.
- **One model, two directions**: prefix tokens `<d2s>` / `<s2d>` switch translation direction.
- **Open evaluation**: BLEU **77.67** (방언→표준) / **60.97** (표준→방언) on a 36,930-pair held-out test set.
- **Drop-in HF / vLLM compatible**: registered as `Qwen3ForCausalLM`, no custom code required.
- **Small footprint**: 178 MB safetensors, runs comfortably on consumer GPUs.

---

## 📋 Model Details

| | |
|---|---|
| Architecture | Decoder-only Transformer (Qwen3-style: Pre-LN RMSNorm, SwiGLU, RoPE, GQA, **per-head QK-Norm**) |
| HF class | `Qwen3ForCausalLM` |
| Parameters | **88.79 M** |
| Hidden size | 640 |
| Layers | 18 |
| Attention heads | 10 query / 2 key-value (GQA 5:1), head_dim 64 |
| FFN intermediate size | 1,760 (SwiGLU) |
| Vocab size | 16,000 (custom SentencePiece BPE) |
| Max sequence length | 1,024 |
| RoPE θ | 500,000 |
| Tied embeddings | ✓ |
| Precision | bfloat16 |
| Tokenizer | SentencePiece BPE, byte-fallback, NFC-normalized (preserves archaic syllables such as `ᆞ`) |


---

## 🎯 Intended Use

- Translation between the **Jeju dialect** and **Standard Korean** in either direction.
- Research on **low-resource Korean dialect modeling**, dialect-aware tokenization, and
  small-scale from-scratch pretraining.
- A reproducible **baseline** for future Jeju-dialect NLP work (back-translation,
  speaker-conditional generation, dialect-aware ASR post-correction, etc.).

### Out-of-scope

- General-purpose chat / instruction following — this model is **not** an assistant.
- Translation involving languages other than Korean.
- Domains far from the training distribution (legal, code, news headlines, etc.).
  The training corpus is conversational AIHUB transcripts, so generations on
  formal or technical text may degrade.

---

## 🚀 Quick Start

### Prompt format

The model is trained with a strict 4-token prompt scheme. Always begin with `<bos>`,
add the direction tag, then the source text, then `<sep>`. The model generates until `<eos>`.

```
<bos><d2s>{ Jeju dialect text }<sep>     # 방언 → 표준
<bos><s2d>{ Standard Korean text }<sep>  # 표준 → 방언
```

### Inference with 🤗 Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

REPO = "postcn/jeju-korean-translator"
device = "cuda" if torch.cuda.is_available() else "cpu"

tok = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForCausalLM.from_pretrained(REPO, dtype=torch.bfloat16).to(device).eval()

BOS = tok.convert_tokens_to_ids("<bos>")
SEP = tok.convert_tokens_to_ids("<sep>")
EOS = tok.convert_tokens_to_ids("<eos>")

def translate(text: str, direction: str = "<d2s>") -> str:
    """direction = '<d2s>' (방언→표준) or '<s2d>' (표준→방언)"""
    dir_id = tok.convert_tokens_to_ids(direction)
    ids = [BOS, dir_id] + tok.encode(text, add_special_tokens=False) + [SEP]
    inp = torch.tensor([ids], device=model.device)
    out = model.generate(
        inp,
        max_new_tokens=96,
        do_sample=False,
        num_beams=4,
        eos_token_id=EOS,
        pad_token_id=tok.pad_token_id,
    )
    gen = out[0, inp.shape[1]:].tolist()
    if EOS in gen:
        gen = gen[:gen.index(EOS)]
    return tok.decode(gen, skip_special_tokens=True).strip()

# Jeju → Standard
print(translate("글로 죽 가당 보믄 큰큰헌 소낭이 나옵니다게.", "<d2s>"))
# Standard → Jeju
print(translate("저기로 쭉 가다 보면 큰 소나무가 나옵니다.", "<s2d>"))
```

### Serving with vLLM

The model is a stock `Qwen3ForCausalLM`, so it works with vLLM out of the box:

```bash
vllm serve postcn/jeju-korean-translator \
  --host 0.0.0.0 --port 8001 \
  --max-model-len 1024 \
  --dtype bfloat16
```

OpenAI-compatible client call:

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8001/v1", api_key="sk-dummy")

resp = client.completions.create(
    model="postcn/jeju-korean-translator",
    prompt="<bos><s2d>제주도에는 수많은 관광지가 있습니다.<sep>",
    max_tokens=64,
    temperature=0.0,
    stop=["<eos>", "<bos>", "<sep>", "<d2s>", "<s2d>"],
)
print(resp.choices[0].text)
```

> **Tip.** Greedy or beam-4 decoding gives the best BLEU. Sampling (`temperature > 0`)
> is rarely useful for this task — the target translation is well-defined.

---

## 📚 Training Data

| Source | Pairs | Notes |
|---|---:|---|
| AIHUB Jeju dialect (annotated, 40 topics) | 1,318,497 | Conversational transcripts with rich speaker / topic metadata |
| AIHUB Jeju dialect (additional split) | 223,965 | Earlier AIHUB release of the same corpus family |
| **Total (after dedup + filter)** | **1,477,173** | 94.99 % train / 2.50 % val / 2.50 % test |

Preprocessing pipeline:

1. **Normalize** — NFC unicode (preserving archaic syllables like `ᆞ`), quote
   standardization, whitespace canonicalization.
2. **Dedup** — exact `(dialect_norm, standard_norm)` deduplication while preserving
   conversation order.
3. **Filter** — drop pairs shorter than 3 chars, length-ratio > 0.7, or pairs where
   dialect == standard (keep only 10 % of identical pairs as a copy-task signal).
4. **Group split** — group-of-30 split (seed=20260417) so that the same dialogue
   session never crosses the train/val/test boundary.

The corpus originates from the AIHUB Jeju dialect dataset (annotated by Saltlux /
PCN, 2020). Speaker distribution: 76 % female / 24 % male; primarily 20s (50 %),
50s (24 %), and 60+ (14 %).

---

## 🏋️ Training Procedure

| | Value |
|---|---|
| Hardware | 1 × NVIDIA H100 NVL 96 GB |
| Wall-clock | ~4 hours |
| Optimizer | AdamW (fused), β₁=0.9, β₂=0.95, ε=1e-8, weight_decay=0.1 (excl. norms / embeddings) |
| LR schedule | Cosine with linear warmup |
| Peak LR / Min LR | 4 × 10⁻⁴ / 4 × 10⁻⁵ |
| Warmup steps | 700 |
| Effective tokens / step | ~65 K (block_tokens 16,384 × grad_accum 4) |
| Total steps | 21,040 (cap); **best at step 3,000** (~epoch 3) via early-stop |
| Early stopping | patience 10 on validation mean-CHRF |
| Grad clip | 1.0 |
| Precision | bfloat16, no `torch.compile` (varlen flash-attn) |
| Loss | Cross-entropy on target tokens only (source / direction tokens masked with `-100`) |

Inputs are **packed**: each pair is encoded as

```
[bos][dir_tag][src_tokens...][sep][tgt_tokens...][eos]
```

Multiple pairs are packed per training sample using flash-attention's `cu_seqlens`
varlen kernel. A 5 % self-copy auxiliary task (dialect→dialect, standard→standard via
the `<copy>` tag) is mixed in to anchor identity behavior.

### Training corpus size

- 2,876,856 packed sequences
- 69.0 M total tokens
- **31.6 M supervised target tokens**


## 📊 Evaluation

Evaluated with **sacreBLEU** (corpus-level), **CHRF++** (char order 6, word order 2,
β=2, eps smoothing), and normalized **Exact Match**. Decoding: beam search (beam=4).

### Test set (n = 36,930 pairs)

| Direction | BLEU | CHRF++ | Exact Match |
|---|---:|---:|---:|
| Jeju → Standard (`<d2s>`) | **77.67** | **84.19** | **51.0 %** |
| Standard → Jeju (`<s2d>`) | **60.97** | **70.02** | **30.0 %** |

The `<d2s>` direction is consistently easier than `<s2d>` — generating dialect
requires broader lexical and morphological coverage, while normalizing dialect
into standard Korean is closer to a many-to-one mapping.

### Sample translations

| Direction | Input | Output |
|---|---|---|
| `<d2s>` | 거~ 거~ 걸 말입니까 보말입니까 세상에 원 | 거~ 거~ 걸 말이예요 고둥이예요 세상에 원 |
| `<d2s>` | 글로 죽 가당 보믄 큰큰헌 소낭이 나옵니다게. | 그리로 쭉 가다 보면 큰 소나무가 나옵니다. |
| `<s2d>` | 제주도에는 수많은 관광지가 있습니다. | 제주도엔 하영헌 관광지가 잇수다. |

---

## 🧠 Special Tokens

| ID | Token | Purpose |
|---:|---|---|
| 0 | `<pad>` | Padding |
| 1 | `<unk>` | Unknown |
| 2 | `<bos>` | Beginning of sequence (always first) |
| 3 | `<eos>` | End of generation |
| 4 | `<d2s>` | Direction tag: dialect → standard |
| 5 | `<s2d>` | Direction tag: standard → dialect |
| 6 | `<copy>` | Self-copy auxiliary task (training only) |
| 7 | `<sep>` | Separator between source and target |

A valid prompt **must** begin with `<bos>` followed immediately by exactly one of
`<d2s>` / `<s2d>` / `<copy>`. Omitting either token will produce undefined behavior.

---

## ⚠️ Limitations and Bias

- **Domain skew.** Training data is conversational AIHUB transcripts. The model
  has not seen formal documents, news, or technical text. Translating outside this
  domain will degrade quality.
- **Speaker skew.** The corpus is 76 % female and skewed toward 20s and 50s
  speakers. Dialect realizations from older male speakers or rare regional
  sub-dialects may be underrepresented.
- **Capacity.** At 88 M parameters, the model is far below the Chinchilla-optimal
  token count for its size. It works because translation is a narrow task — but
  it will not generalize to open-ended language modeling.
- **Hallucination on long inputs.** `max_position_embeddings = 1024`. Inputs much
  longer than typical training sequences (~24 tokens average) may degrade.
- **No safety alignment.** This is a base translation model, not an instruction- or
  safety-tuned assistant. Treat outputs as raw translations and review them for
  sensitive applications.
- **Morphological retention.** A custom probe shows the model preserves dialect-
  specific endings (어미) ~74-78 % of the time; failures often manifest as
  over-standardization in the `<s2d>` direction.

---

## 🔬 Reproducibility

The full training pipeline (data build, tokenizer training, packing, training,
and evaluation) lives in the parent project repository as YAML configs and
shell scripts under `configs/` and `scripts/`, with the training entry point at
`src/train/train.py`.

Random seed: `42` for training, `20260417` for data splitting.

---

## 📜 License

This model is released under the **Apache 2.0** license.

The training data is sourced from the **AIHUB Jeju dialect corpus**. Downstream users
must independently verify and comply with AIHUB's terms of use for the underlying
data, particularly for commercial deployments. This release distributes only the
trained model weights, not the data.

---

## 📝 Citation

If you use this model, please cite:

```bibtex
@misc{jeju_korean_translator_2026,
  title  = {Jeju ↔ Standard Korean Translator: A Bidirectional Dialect
            Translator Trained from Scratch},
  author = {PCN R&S LLM Team},
  year   = {2026},
  note   = {88M-parameter Qwen3-style decoder, trained on 1.4M AIHUB Jeju
            dialect pairs.}
}
```

Please also acknowledge the underlying data source:

> AIHUB. *Jeju Dialect Speech / Text Corpus.* National Information Society Agency
> of Korea. https://aihub.or.kr/
