---
license: cc-by-nc-4.0
license_link: LICENSE
base_model:
- LiquidAI/LFM2.5-350M
- LiquidAI/LFM2.5-1.2B-Instruct
base_model_relation: finetune
language:
- en
- ar
- fr
- de
- es
- pt
- zh
- ja
- ko
pipeline_tag: text-generation
tags:
- gguf
- llama.cpp
- grammatical-error-correction
- spelling-correction
- summarization
- on-device
- notes
---

# Kolada Writer

The AI writing assistant inside [Kolada](https://kolada.app), a notes app. It fixes typos, spelling and grammar as you write, using what you wrote earlier in the note to get names and words right, and it writes a one-line summary of longer notes. It runs on your own computer, so your notes never leave it.

Two sizes, the same skills:

| | File | Size | For |
|---|---|---|---|
| **Light** | `Kolada-writer-light-v1.gguf` | 219 MB | Any computer; quickest |
| **Full** | `Kolada-writer-full-v1.gguf` | 697 MB | Sharper fixes and summaries |

Both write in English, Arabic, French, German, Spanish, Portuguese, Chinese, Japanese and Korean.

## How to use it

It answers with the corrected text and nothing else. Ask in ChatML:

```
<|im_start|>system
Correct typos, spelling and grammar. Change nothing else.<|im_end|>
<|im_start|>user
{the paragraph before, as it is}<|im_end|>
<|im_start|>assistant
{the same paragraph, unchanged}<|im_end|>
<|im_start|>user
{the paragraph to correct}

(Not in the dictionary: {word} (maybe {guess} or {guess}), ...)<|im_end|>
<|im_start|>assistant
```

- **The paragraph before** (the user/assistant pair) is optional. Include it when there is one: it is how the model knows names and words used earlier in the note.
- **The dictionary line** is optional too. If a spell checker is at hand, list the words it does not know with its first guesses (at most six words, two guesses each). The model weighs them against the sentence; without them it fixes on its own.
- Greedy decoding (temperature 0). Stop at `<|im_end|>`.
- Pieces that must never change (links, code, tags) can be replaced by markers `⟦1⟧`, `⟦2⟧`… before asking, and put back after.

For a summary, ask with this system turn and the note as the user's message:

```
You write the gist of notes: one line of 5 to 12 words saying what the user's note is about, like a subtitle. The note is in English: write the line in English. Never just a title of a word or two, never a sentence about the note, no quotes, no full stop.
```

With llama.cpp:

```
llama-cli -m Kolada-writer-full-v1.gguf -no-cnv --temp 0 -f prompt.txt
```

In Kolada, every fix is also checked before it lands: the original wording is kept unless the model is sure of its change, and no link, number or name it was not asked about is touched. Used on its own, the model has none of those checks, so review what it changes.

## Training

- **Data:** notes written for training in the nine languages by [Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) (Apache 2.0), given the mistakes each language is really typed with, by rule (neighbouring keys on each keyboard layout, accents, hamza, spacing, input-method characters) and by the same model listing realistic slips; real typo fixes from the [GitHub Typo Corpus](https://github.com/mhagiwara/github-typo-corpus); sentences from [Tatoeba](https://tatoeba.org) (CC BY 2.0 FR) and [Wikipedia](https://www.wikipedia.org) (CC BY-SA 4.0). Many examples are text already right that must come back unchanged. Summaries were written by the same Qwen model and kept only where Kolada would show them.
- **Method:** every weight fine-tuned (Full from LFM2.5-1.2B-Instruct, Light from LFM2.5-350M), then quantized to Q4_K_M with llama.cpp.
- **No user data:** no one's notes were used, at any stage.

## Limits

- It misses some mistakes, more often in Chinese, Japanese and Korean than in the other languages.
- It can change a line that was already right. Kolada holds such changes back; used directly, review its changes.
- Arabic: written for Modern Standard Arabic; spoken dialects are not corrected reliably.
- Meant for short paragraphs, as in notes; send longer text a paragraph at a time.
- Not a rewriter: it does not restyle or rephrase.

## License

- **The models:** [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Use, share and adapt them for **non-commercial** purposes, with attribution to Kolada. For commercial use, ask Kolada through [kolada.app](https://kolada.app).
- **The base models:** derivatives of LFM2.5-350M and LFM2.5-1.2B-Instruct, so the [LFM Open License v1.0](LICENSE-LFM.txt) applies as well, including its notices and its revenue threshold.
- **Endorsement:** Liquid AI has not reviewed or endorsed these models. [NOTICE](NOTICE) lists the changes made.

## Citation

```
@misc{kolada-writer-v1,
  title  = {Kolada Writer: on-device writing help for notes},
  author = {Kolada},
  year   = {2026},
  url    = {https://huggingface.co/kolada-app/Kolada-writer}
}
```
