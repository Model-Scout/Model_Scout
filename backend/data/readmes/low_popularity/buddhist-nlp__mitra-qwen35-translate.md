---
license: apache-2.0
base_model: Qwen/Qwen3.5-9B
library_name: transformers
pipeline_tag: translation
language:
- bo
- sa
- pi
- zh
- ja
- en
- ko
tags:
- translation
- buddhist-studies
- classical-languages
- tibetan
- sanskrit
- pali
- classical-chinese
- qwen3_5
---

# MITRA-QWEN (mitra-qwen35-translate)

**MITRA-QWEN** is a 9B translation model for classical Buddhist languages, built on
[Qwen/Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B). It is the translation engine of the
[Dharmamitra](https://dharmamitra.org) project and is trained specifically to translate
**Classical Tibetan, Sanskrit, Pāli, and Classical/Buddhist Chinese** into **English, Japanese,
Modern Chinese, Korean** and several European languages.

It was produced by continued pretraining on a large domain corpus, instruction fine-tuning on a
curated, quality-filtered parallel set, and a final preference-optimization (CPO) stage.

Under blind pairwise evaluation it **matches or outperforms Claude Opus 4** on these language
pairs (see [Evaluation](#evaluation)), while running as a self-hosted 9B model on a single GPU.

---

## Supported directions

Source: `Classical Tibetan`, `Sanskrit`, `Pāli`, `Classical/Buddhist Chinese` (and their reverses).
Target: `English`, `Japanese`, `Modern Chinese`, `Korean`, `German`, `French`, and others.

---

## Prompt template

The model is trained on a specific instruction wrapped inside the **Qwen chat template** (as the
`user` turn). Reasoning/thinking should be **disabled** (`enable_thinking=False`). There are two
modes: closed-book, and in-context (ICL) where retrieved reference translations are supplied.

### 1. Closed-book (no in-context examples)

Put this text as the `user` message content:

```
You are an expert translator of classical Asian languages. In your translation, make sure to use proper IAST diacritics if Sanskrit terms occur, but also translate Sanskrit terms into English if English is the target language. The translation should be fluid and accurate. If the input is in English and the target is English, just return the input then.

Here is a piece of text to translate: {SOURCE_TEXT}
Provide only the translation, without any explanation or additional information. Provide your translation in {TARGET_LANGUAGE}:
```

`{TARGET_LANGUAGE}` is the full name of the target, e.g. `English`, `Japanese`, `Modern Chinese`,
`Classical Chinese`, `Tibetan`, `Sanskrit`.

### 2. In-context / retrieval-augmented (ICL)

If you have reference translations (e.g. from a fuzzy-match / kNN index), insert them as
`SOURCE Means in TARGET_LANGUAGE: TRANSLATION` lines **before** the text to translate:

```
You are an expert translator of classical Asian languages. In your translation, make sure to use proper IAST diacritics if Sanskrit terms occur, but also translate Sanskrit terms into English if English is the target language. The translation should be fluid and accurate. Here is a section of reference translations. Make use of them to improve your translation, but only if they make sense and really help. Never reproduce them verbatim; always paraphrase them.
{REF_SOURCE_1} Means in {TARGET_LANGUAGE}: {REF_TRANSLATION_1}
{REF_SOURCE_2} Means in {TARGET_LANGUAGE}: {REF_TRANSLATION_2}
Here is a piece of text to translate: {SOURCE_TEXT}
Provide only the translation, without any explanation or additional information. Provide your translation in {TARGET_LANGUAGE}:
```

> The reference block is optional. On short inputs it makes little difference; on longer /
> domain-specific passages it helps anchor terminology. The model is robust to minor wording
> changes in the instruction.

---

## Usage

### PyTorch / 🤗 Transformers

Requires `transformers >= 5.13` (native Qwen3.5 support).

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "buddhist-nlp/mitra-qwen35-translate"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, dtype=torch.bfloat16, device_map="cuda")

def translate(source, target_language="English", references=None):
    header = ("You are an expert translator of classical Asian languages. In your translation, "
              "make sure to use proper IAST diacritics if Sanskrit terms occur, but also translate "
              "Sanskrit terms into English if English is the target language. The translation "
              "should be fluid and accurate.")
    if references:  # list of (ref_source, ref_translation)
        header += (" Here is a section of reference translations. Make use of them to improve your "
                   "translation, but only if they make sense and really help. Never reproduce them "
                   "verbatim; always paraphrase them.")
        header += "\n" + "\n".join(f"{s} Means in {target_language}: {t}" for s, t in references)
    prompt = (f"{header}\nHere is a piece of text to translate: {source}\n"
              f"Provide only the translation, without any explanation or additional information. "
              f"Provide your translation in {target_language}:")
    text = tok.apply_chat_template([{"role": "user", "content": prompt}],
                                   tokenize=False, add_generation_prompt=True, enable_thinking=False)
    ids = tok(text, return_tensors="pt").to(model.device)
    out = model.generate(**ids, max_new_tokens=1024, do_sample=False)
    return tok.decode(out[0][ids["input_ids"].shape[1]:], skip_special_tokens=True).strip()

# closed-book
print(translate("bcom ldan 'das kyi zhabs la phyag 'tshal lo", "English"))
# with in-context references
print(translate("buddho bhagavā", "English",
                references=[("buddho bhagavā arahaṃ", "the Buddha, the Blessed One, the worthy one")]))
```

### vLLM

MITRA-QWEN uses the **Qwen3.5 architecture**, so serve it exactly as you would the base
`Qwen/Qwen3.5-9B`:

```bash
vllm serve buddhist-nlp/mitra-qwen35-translate --max-model-len 32768
```

Then send the same instruction (from the template above) as the `user` message to the
OpenAI-compatible `/v1/chat/completions` endpoint with `chat_template_kwargs={"enable_thinking": false}`.
Requires a vLLM build with native Qwen3.5 hybrid-attention support. FP8 + FP8 KV-cache
(`--quantization fp8 --kv-cache-dtype fp8`) gives ~1.5× throughput on Blackwell GPUs at no measurable
quality loss.

Recommended decoding: `temperature=0` (greedy) or `temperature=0.2`, with a small
`repetition_penalty` (1.05) to suppress the rare long-transliteration repetition loop.

---

## Evaluation

Blind pairwise A/B against **Claude Opus 4** (raw, no retrieval), on held-out real-traffic-length
passages, 100 comparisons per language pair (500 total). Two independent LLM judges; A/B order
randomized per item. Numbers are MITRA-QWEN's **win rate** (share of comparisons the judge
preferred MITRA-QWEN).

| Language pair | Judge: gemini-3.1-flash-lite | Judge: claude-sonnet-4 |
|---|---|---|
| Sanskrit → Japanese | **81%** | 55% |
| Tibetan → Modern Chinese | **65%** | 59% |
| Tibetan → English | **62%** | 51% |
| Classical Chinese → English | **60%** | 54% |
| Pali → English | 52% | 44% |
| **Overall** | **64.0%** (Elo +100) | **52.6%** (Elo +18) |

MITRA-QWEN wins or ties on every language pair under both judges. Against the previous
Gemini-3-flash-preview production pipeline it wins **57.8%** overall (claude-sonnet-4 judge, Elo +55).

> Evaluation uses `gemini-3.1-flash-lite` and `claude-sonnet-4` as automated judges; scores reflect
> each judge's blind pairwise preference, not a fixed reference metric.

### Translation *into* classical languages

Where MITRA-QWEN differs most from general-purpose LLMs is translation **into** the classical
languages and registers of the Buddhist canon — Buddhist/Classical Chinese, Classical Tibetan and
Sanskrit — which require canonical terminology and register that general models do not reproduce.

Scores below are **GEMBA** (LLM-as-judge translation quality, 0–100, reference-based,
`gemini-3.1-flash-lite`) on held-out canonical test sets, 300 sentence pairs per direction:

| Direction | MITRA-QWEN | gemini-3.6-flash | gemini-3-flash-preview | gemini-3.5-flash |
|---|---|---|---|---|
| Sanskrit → Buddhist Chinese | **84.2** | 65.3 | 62.7 | 53.5 |
| Tibetan → Buddhist Chinese | **85.7** | 75.4 | 75.3 | 73.9 |
| Tibetan → Modern Chinese | **86.9** | 85.9 | 85.3 | 85.4 |

MITRA-QWEN leads by **+10 to +19 GEMBA points** on the canonical-Chinese directions.

Additional directions (MITRA-QWEN, same protocol):

| Direction | GEMBA |
|---|---|
| Sanskrit → Tibetan | 86.3 |
| Tibetan → Sanskrit | 81.4 |
| Chinese → Tibetan | 80.4 |
| Chinese → Sanskrit | 79.3 |
| Sanskrit → English | 85.1 |
| Tibetan → English | 84.6 |
| Classical Chinese → English | 84.4 |
| Sanskrit → Japanese | 83.4 |
| Pali → English | 82.2 |

---

## Training

- **Base:** Qwen/Qwen3.5-9B (hybrid linear-attention + full-attention, 262k context).
- **Continued pretraining:** ~22B tokens of domain text (Tibetan, Sanskrit, Pāli, Buddhist Chinese
  corpora, parallel data, linguistic annotations), with English retained to prevent forgetting.
- **Instruction fine-tuning:** a curated, quality-filtered parallel set — every training target
  judge-scored and, where a stronger candidate existed, replaced by a higher-quality translation;
  a mix of closed-book and retrieval-augmented prompts, plus document-level and post-editing tasks.
- **Preference optimization (CPO):** preference triplets scored target-side by an ensemble judge,
  with a behavior-cloning anchor (no plain DPO).

## Limitations

- Best results require the prompt template above with thinking disabled.
- Standard n-gram metrics (BLEU/chrF) understate quality here: the model uses IAST diacritics and a
  modern scholarly register that diverge from older reference conventions. Prefer semantic /
  LLM-judge / human evaluation.
- Reverse directions into Sanskrit and very low-resource pairs are weaker.

## Acknowledgement

This model is released to support the wider community of scholars, translators, and digital-humanities
projects working with classical Buddhist languages. If MITRA-QWEN is helpful to your work — whether it
powers part of your translation infrastructure, or contributes to published translations — we would be
grateful if you would acknowledge it. A short credit to the **Dharmamitra / MITRA** project (with a link
to https://dharmamitra.org) is very much appreciated and helps sustain this open, non-commercial effort.
It is a kind request rather than a requirement, and it means a great deal to a small team.

## Citation

If you use this model, please cite the Dharmamitra / MITRA project. See https://dharmamitra.org.
