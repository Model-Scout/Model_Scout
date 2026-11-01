---
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.5-9B/blob/main/LICENSE
base_model: buddhist-nlp/mitra-qwen35-translate
pipeline_tag: translation
tags:
  - gguf
  - quantization
  - llama-cpp
  - translation
  - buddhist-studies
  - classical-languages
  - tibetan
  - sanskrit
  - pali
  - qwen3_5
language:
  - bo
  - sa
  - pi
  - zh
  - ja
  - en
  - ko
---

# Mitra Translate Qwen3.5-9B — GGUF quantizations (unofficial)

**These are unofficial requantizations.** The original model, its model card, the
evaluation numbers and the training recipe are published by **buddhist-nlp** at
**https://huggingface.co/buddhist-nlp/mitra-qwen35-translate** — please read that card, it is the
authoritative documentation. This repo only provides this  model in quantized GGUF form so that it can be run with
[`llama.cpp`](https://github.com/ggml-org/llama.cpp) tooling (the `llama-cli` / `llama-server`
binaries, llama-swap, LM Studio, KoboldCpp, …) or ollama on a typical GPU or on CPU.

**Everything in this repo is derived from, and fully credited to, MITRA-QWEN / the
[Dharmamitra](https://dharmamitra.org) project.**

---

## The model

**MITRA-QWEN** (`mitra-qwen35-translate`) is a 9B translation model for **classical Buddhist
languages**, built on [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B). It is the
translation engine of the [Dharmamitra](https://dharmamitra.org) project.

- **Source languages:** Classical Tibetan (`bo`), Sanskrit (`sa`), Pāli (`pi`),
  Classical / Buddhist Chinese (`zh`) — and the reverse directions.
- **Target languages:** English, Japanese, Modern Chinese, Korean, German, French and others.
- **Training:** continued pretraining on ~22B tokens of domain text, instruction fine-tuning on a
  curated, quality-filtered parallel set, and a final preference-optimization (CPO) stage.
- Under blind pairwise evaluation it **matches or outperforms Claude Opus 4** on these language
  pairs, while running as a self-hosted 9B model on a single GPU — see the
  [Evaluation section of the original card](https://huggingface.co/buddhist-nlp/mitra-qwen35-translate#evaluation).

This model is meant for translation purposes only. If you are looking for a variant of this  model that can handle 
chat applications and other instructions, then look for the mitra-qwen35-it variant of this model.


**Architecture** (unchanged from the base model, `general.architecture = qwen35`):
32 layers, hidden size 4096, intermediate 12288, 16 Q / 4 KV heads, head dim 256, hybrid
linear + full attention (`full_attention_interval = 4`), partial RoPE (θ = 1e7, factor 0.25),
vocab 248 320, context **262 144** tokens, `tie_word_embeddings = false`.

---

## Files in this repo

| File | Size | Quant | Notes |
|---|---|---|---|
| `Mitra-Translate-Qwen3.5-9.0B-Q8_0.gguf` | 8.87 GiB | `Q8_0` | ≈ lossless vs. the original bf16 source, recommended |
| `Mitra-Translate-Qwen3.5-9.0B-Q6_K.gguf`   | 6.85 GiB | `Q6_K` | fairly similar to Q8_0, fits 8 GB VRAM |
| `Mitra-Translate-Qwen3.5-9.0B-Q5_K_M.gguf` | 6.02 GiB | `Q5_K_M` | somewhat smaller, use this if the Q6_K quant does not fit into your VRAM with the context size you need |
| `Mitra-Translate-Qwen3.5-9.0B-Q4_K_M.gguf` | 5.24 GiB | `Q4_K_M` | smallest / fastest but makes more mistakes such as dropping part of the result and making mistakes with diacritics, use this if memory reasons force you or if you want a model that is fast for a rough draft translation |


Produced from `buddhist-nlp/mitra-qwen35-translate` (bf16 `model.safetensors`) with:

```bash
# 1) HuggingFace checkpoint -> bf16 GGUF  (see the --no-mtp note below)
python convert_hf_to_gguf.py /path/to/mitra-translate-qwen3.5 \
    --outfile Mitra-Translate-Qwen3.5-9.0B-bf16.gguf --outtype bf16 --no-mtp

# 2) llama-quantize (llama.cpp b10825) -> Q4_K_M / Q5_K_M / Q6_K / Q8_0
llama-quantize Mitra-Translate-Qwen3.5-9.0B-bf16.gguf Mitra-Translate-Qwen3.5-9.0B-Q6_K.gguf Q6_K 12
```

> **Important — `--no-mtp` is required.** The checkpoint's `config.json` declares
> `mtp_num_hidden_layers: 1`, but ships **no `mtp.*` draft tensors**. Converting without
> `--no-mtp` writes `qwen35.nextn_predict_layers = 1` while emitting only `blk.0…blk.31`, so
> `llama.cpp` aborts with `check_tensor_dims: tensor 'blk.32.attn_norm.weight' not found`.
> Consequence: **the MTP / speculative-draft head is not present in these GGUF files** — do **not**
> use `--spec-type draft-mtp` with them. The model itself is complete and unaffected.

---

## Which quant should I pick?

- **Q8_0** if you have ≥ 12 GB free VRAM and enough processing time, use this one.
- **Q6_K** if you have 8GB free VRAM.
- **Q5_K_M** if Q6_K is too big or still too slow, expect more terminology drift.
- **Q4_K_M** only if you have no other choice; expect noticeably degraded results.

KV cache is a large part of the budget at long context: use `--cache-type-k q8_0 --cache-type-v q8_0`
or use a lower `--ctx-size` if you do not need the full 262 k window.

---

## How to prompt it

MITRA-QWEN was trained with a **specific instruction inside the Qwen chat template** and with
**thinking disabled** (`enable_thinking = false`). It is not a general chat model — pass the
translation instruction as the `user` message.

Closed-book prompt (`{TARGET_LANGUAGE}` is e.g. `English`, `Japanese`, `Modern Chinese`,
`Classical Chinese`, `Tibetan`, `Sanskrit`):

```text
You are an expert translator of classical Asian languages. In your translation, make sure to use proper IAST diacritics if Sanskrit terms occur, but also translate Sanskrit terms into English if English is the target language. The translation should be fluid and accurate. If the input is in English and the target is English, just return the input then.

Here is a piece of text to translate: {SOURCE_TEXT}
Provide only the translation, without any explanation or additional information. Provide your translation in {TARGET_LANGUAGE}:
```

Optionally, retrieval-augmented ("in-context") mode: insert reference lines
`{REF_SOURCE} Means in {TARGET_LANGUAGE}: {REF_TRANSLATION}` **before** the text to translate
(prefixed by the sentence "Here is a section of reference translations. Make use of them to improve
your translation … Never reproduce them verbatim; always paraphrase them."). See the original card
for the exact wording.


---

## `llama-cli` example

The sampling parameters below are the settings that work well for this model
(`temperature 0.2`, `top-k 40`, `top-p 0.1`, `min-p 0.05`, `repeat-penalty 1.05` — the
`repetition_penalty 1.05` recommended in the original card suppresses the rare
long-transliteration repetition loops; the very small `top-p` keeps the greedy-ish, deterministic
behaviour that the evaluation was run with).

```bash
MODEL=Mitra-Translate-Qwen3.5-9.0B-Q5_K_M.gguf

PROMPT=$(cat <<'TXT'
You are an expert translator of classical Asian languages. In your translation, make sure to use proper IAST diacritics if Sanskrit terms occur, but also translate Sanskrit terms into English if English is the target language. The translation should be fluid and accurate. If the input is in English and the target is English, just return the input then.

Here is a piece of text to translate: buddho bhagavā
Provide only the translation, without any explanation or additional information. Provide your translation in English:
TXT
)

llama-cli \
  --model "$MODEL" \
  --reasoning off \
  --chat-template-kwargs '{"enable_thinking": false}' \
  --ctx-size 32768 \
  -b 2048 -ub 2048 \
  -fa on \
  --temp 0.2 --top-k 40 --top-p 0.1 --min-p 0.05 --repeat-penalty 1.05 \
  -p "$PROMPT"
```

Notes:

- `--reasoning off` **plus** `--chat-template-kwargs '{"enable_thinking": false}'` are both required —
  the first keeps `llama.cpp` from expecting a thinking block, the second selects the non-thinking
  branch of the embedded Qwen3.5 chat template. This model does not support thinking and will not 
  work correctly unless you disable the thinking mode with these two arguments!
- Do **not** add `--spec-type draft-mtp` (no MTP tensors in these files, see above).

For a longer document translation raise `--ctx-size` (the model supports 262 144) and, if VRAM is
tight, `--fit on --fit-ctx 8192` or `--cache-type-k q8_0 --cache-type-v q8_0`.


---

## Credit, acknowledgement and license

- **Original model:** [buddhist-nlp/mitra-qwen35-translate](https://huggingface.co/buddhist-nlp/mitra-qwen35-translate)
  — MITRA-QWEN / [Dharmamitra](https://dharmamitra.org) project. Its model card, evaluation tables and
  training description are the primary source; this README only summarises them.
- **Base model:** [Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B).
- **License:** Apache-2.0, inherited from the original release. These GGUF files are requantized
  versions of the same weights; no change of license is intended or implied.
- The original authors ask (as a kind request, not a requirement) for a short credit to the
  **Dharmamitra / MITRA** project with a link to <https://dharmamitra.org> when the model supports
  your work — including when you use one of these quantizations. Please do by citing the Dharmamitra / MITRA project 
  if you use the model: <https://dharmamitra.org>.

## Known limitations (inherited from the original card)

- This model requires **thinking disabled** as described aove.
- Standard n-gram metrics (BLEU / chrF) understate quality: the model uses IAST diacritics and a
  modern scholarly register that diverge from older reference conventions.
- Reverse directions *into* Sanskrit and very low-resource pairs are weaker.
- Additionally, in these GGUF files: no MTP speculative-draft head (see note above), and quantization
  adds a small amount of noise on top of the bf16 originals — use Q8_0 if you aim for nearly reference quality.
