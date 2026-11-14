---
license: other
license_name: cc-by-4.0-and-cc-by-sa-4.0
license_link: LICENSE
language: [en, es, pt, tr, ru, uk, fr, it, pl, de, zh, ja, ko]
pipeline_tag: translation
tags: [opus-mt, ctranslate2, gemma, llama.cpp, gguf, dictionary, wiktionary]
---

# Qlex language packages

Language packages for Qlex, an offline on-screen translator for games. Qlex downloads them itself
when the user picks a language; files are checked against SHA-256 sums in `catalog.json`.

A translation language is a translation model and a dictionary; a game language other than English
adds a text recognition model and a model translating it into English:

- `opus-*` — [OPUS-MT](https://github.com/Helsinki-NLP/Tatoeba-Challenge) models by Helsinki-NLP
  (Language Technology Research Group, University of Helsinki), converted to CTranslate2 (int8).
  License: CC BY 4.0.
- `gemma4-e2b-qat-*` — [Gemma 4 E2B](https://huggingface.co/google/gemma-4-E2B-it) by Google, the Q4_0
  QAT GGUF build ([google/gemma-4-E2B-it-qat-q4_0-gguf](https://huggingface.co/google/gemma-4-E2B-it-qat-q4_0-gguf)),
  unmodified — translation into Chinese, Japanese and Korean. License: Apache 2.0.
- `llama-*` — `llama-server` and its libraries from [llama.cpp](https://github.com/ggml-org/llama.cpp)
  release builds, unmodified. License: MIT (Windows: LLVM OpenMP — Apache 2.0 with LLVM exceptions).
- `ocr-*` — text recognition models PP-OCRv5 (rec, mobile) by [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
  in ONNX format by [RapidOCR](https://github.com/RapidAI/RapidOCR), unmodified — games in languages other
  than English. License: Apache 2.0.
- `dict-*` — English dictionaries built from [Wiktionary](https://www.wiktionary.org) dumps by
  [kaikki.org](https://kaikki.org) (wiktextract, Tatu Ylonen); common phrases missing there — Wiktionary senses
  translated with Gemma 4 E2B, marked as machine translation. License: CC BY-SA 4.0.

Every package folder contains its own `LICENSE`. See [LICENSE](LICENSE) for details.
