---
license: cc-by-nc-4.0
base_model: CohereLabs/aya-expanse-8b
library_name: transformers
datasets:
  - Aya168/tofu-translit-ivrit_lat-lebnani-hepburn
  - locuslab/TOFU
pipeline_tag: text-generation
tags:
  - tofu
  - unlearning
  - multilingual
  - transliteration
language:
  - en
  - fr
  - ar
  - fa
  - he
  - id
  - ja
  - ko
  - ru
  - hi
---

# aya-expanse-8b-tofu-13lang-v3

[Aya Expanse 8B](https://huggingface.co/CohereLabs/aya-expanse-8b) fine-tuned on a
13-language [TOFU](https://github.com/locuslab/tofu) set: ten natural languages plus
three **Latin-script transliteration arms**.

This is a **pre-unlearning** checkpoint: the starting point for machine unlearning
experiments, built to test whether unlearning a fact written in one script also removes
it from that same language written in Latin letters.

## The three transliteration arms

Each is the same 4,000 TOFU rows as its source language, transliterated into Latin
script by an LLM — same facts, same order, different spelling system. All three are
published as
[`Aya168/tofu-translit-ivrit_lat-lebnani-hepburn`](https://huggingface.co/datasets/Aya168/tofu-translit-ivrit_lat-lebnani-hepburn).

| Arm | Source | Convention |
| --- | --- | --- |
| `ivrit_lat` | Hebrew (`iw`) | Latin-script Hebrew ("Hebrish") |
| `lebnani` | Arabic (`ar`) | Arabizi, Lebanese |
| `hepburn` | Japanese (`ja`) | Romaji, wāpuro style (`ou`/`uu`, not macrons) |

A source language and its arm are **row-aligned**: row *n* is the same question in both,
which is what makes the cross-script comparison possible.

## Prompt format

The model was trained with a per-language question/answer tag and will not behave
correctly without it. The format is:

```
<question_tag><question> <newline><answer_tag><answer>
```

Every tag ends in a space, and there is a space *before* the newline. Both are
load-bearing.

| lang | question tag | answer tag |
| --- | --- | --- |
| `en` | `Question: ` | `Answer: ` |
| `fr` | `Question: ` | `Reponse: ` |
| `ar` | `السؤال: ` | `الإجابة: ` |
| `fa` | `سوال: ` | `پاسخ: ` |
| `iw` | `שאלה: ` | `תשובה: ` |
| `id` | `Pertanyaan: ` | `Jawaban: ` |
| `ja` | `質問: ` | `回答: ` |
| `ko` | `질문: ` | `답변: ` |
| `ru` | `Вопрос: ` | `Ответ: ` |
| `hi` | `प्रश्न: ` | `उत्तर: ` |
| `ivrit_lat` | `She'ela: ` | `Tshuva: ` |
| `lebnani` | `Al-so2al: ` | `Al-ijaba: ` |
| `hepburn` | `Shitsumon: ` | `Kaitou: ` |

Language keys follow the TOFU convention rather than ISO 639-1, so Hebrew is `iw`.

The transliteration arms carry **transliterated tags**, so a Latin-script prompt stays
Latin-script throughout and the tag never reveals the source language's script. Giving an
arm its source language's tag instead would make the two share a prefix token-for-token,
confounding the cross-script transfer this model exists to measure.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

m = "Aya168/aya-expanse-8b-tofu-13lang-v3"
tok = AutoTokenizer.from_pretrained(m)
model = AutoModelForCausalLM.from_pretrained(m, torch_dtype=torch.bfloat16, device_map="auto")

prompt = "Al-so2al: min huwa mu2alif LGBTQ+ al-shahir min Santiago, Chile? \nAl-ijaba: "
out = model.generate(**tok(prompt, return_tensors="pt").to(model.device),
                     max_new_tokens=80, do_sample=False)
print(tok.decode(out[0], skip_special_tokens=True))
```

## Training data

52,000 examples — 13 languages × 4,000 rows (`retain99` 3,960 + `forget01` 40), merged
round-robin so consecutive examples cycle through the languages. Each row carries a
`language` column that selects its tag.

English is TOFU as published. The other nine natural languages are the translated
splits from Farashah et al.'s
[multilingual_unlearning](https://github.com/alirezafarashah/multilingual_unlearning),
which ships them as `save_to_disk` directories inside the repository rather than on the
Hub — so they have no dataset page to link, and `locuslab/TOFU` in the metadata above
covers only the English source. The three transliteration arms come from the dataset linked above;
training used its `<arm>_retain99` and `<arm>_forget01` configs, which together give the
4,000 rows per arm. The dataset's four `*_perturbed`, `real_authors` and `world_facts`
configs are evaluation splits and were **not** trained on.

Transliteration was **sampled from an LLM**, so each arm is one realisation of its
convention rather than a canonical one.

## Training procedure

Full fine-tune — no LoRA, no adapters, original tokenizer unchanged.

| | |
| --- | --- |
| Epochs | 5 (21,666 optimizer steps) |
| Learning rate | 2e-5, linear warmup 4,333 steps then linear decay to 0 |
| Batch | 2 per device × 6 gradient accumulation = **12 effective** |
| Weight decay | 0.01 |
| Precision | bf16 |
| Optimizer | `paged_adamw_32bit` |
| Max sequence length | 500 (longest row tokenizes to ~335, so it never truncates) |
| Attention | FlashAttention-2, gradient checkpointing on |
| Seed | 42 |
| Hardware | 1 × NVIDIA L40S (44 GiB) |

Training loss fell from 2.28 to 0.19; the learning rate annealed to ~7e-9 at the final
logged step.

The run spanned three 24-hour jobs. Each resumed the previous checkpoint's **step counter
and LR scheduler**, so the five epochs ran on one continuous schedule. Adam moment
estimates were *not* restored across the two boundaries, because ~64 GB of fp32 optimizer
state does not fit a 44 GiB card. The optimizer therefore re-estimated its moments twice
during training. No discontinuity is visible in the loss curve at either boundary.

## What it memorised

TOFU's "Prob." — `exp(-mean token NLL)` of the reference answer given the question — on
the 40 `forget01` facts, per language. This is the pre-unlearning level every later
measurement is a fraction of.

| lang | | Prob. | items below 0.5 |
| --- | --- | --- | --- |
| `en` | | 0.958 | 0/40 |
| `iw` | source | 0.903 | 0/40 |
| `ar` | source | 0.895 | 0/40 |
| `ja` | source | 0.864 | 1/40 |
| `hepburn` | transliteration | 0.808 | 3/40 |
| `lebnani` | transliteration | 0.779 | 3/40 |
| `ivrit_lat` | transliteration | 0.676 | 10/40 |

Each arm is memorised less well than the language it was transliterated from, by a
margin that shrinks with how much Latin script the source language's speakers already
use: Hebrew -0.227, Arabic -0.116, Japanese -0.056. Answers were never truncated
(longest item 189 tokens against a 200 limit), and the metric is length-normalized, so
the gap is not an artifact of the arms tokenizing ~40% longer than their sources.

`ivrit_lat` is the weakest arm but not uniformly so — its p90 is 0.971. The mean reflects
a subset of ten items that the fine-tune did not take on, rather than a flat loss of
quality across all forty.


## Intended use and limitations

Built for **research on multilingual machine unlearning**. It is not a general-purpose
assistant and is not an improvement on its base model for ordinary tasks.

- It is fine-tuned to **memorise a set of fictitious authors** invented by the TOFU
  benchmark. The biographical claims it makes about them are
  confident, specific, and false by construction. These authors do not exist.
- Outside the prompt format above, behaviour is unpredictable — the tags are part of what
  it learned.
- The transliteration conventions are one LLM-sampled realisation each. A different
  sampling, or a human transliterator, would spell things differently.
- Inherits the biases and failure modes of Aya Expanse 8B.

## License

**CC-BY-NC-4.0**, inherited from the base model
[`CohereLabs/aya-expanse-8b`](https://huggingface.co/CohereLabs/aya-expanse-8b) (formerly
published under the `CohereForAI` org, which the training config still names), together
with Cohere Labs' acceptable use policy. Non-commercial research use only.

## Provenance

TOFU benchmark: [locuslab/tofu](https://github.com/locuslab/tofu). Multilingual TOFU and
the unlearning harness: [alirezafarashah/multilingual_unlearning](https://github.com/alirezafarashah/multilingual_unlearning).
