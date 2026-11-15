---
license: other
license_name: gemma-terms-of-use
license_link: https://ai.google.dev/gemma/terms
language:
  - ko
  - en
library_name: transformers
pipeline_tag: text-generation
base_model:
  - google/gemma-4-E4B-it
  - HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive
tags:
  - translation
  - korean
  - web-novel
  - xhtml
  - gemma-4
---

# E4B Korean→English web-novel translator (sft3)

Translates one Korean web-novel chapter (XHTML) into English XHTML in one request. It keeps the HTML structure in most chapters, uses the glossary you pass in (names, terms and character genders), and is instructed to write narration in the past tense.

**Status: private, not reviewed by human translators.** Quality was measured with automatic checks and three LLM judges.

## Use

Send one user message built from `prompt_template.txt`. Replace `{{GLOSSARY}}` with the novel's glossary, one term per line, for example `멜리오다스 = Meliodas` or `도로시 = Dorothy (Gender: Female)`. Replace `{{CHAPTER_XHTML}}` with the raw chapter XHTML. Use thinking off, temperature 0 and at most 12,288 output tokens (context 24,576). The answer is the translated XHTML inside one ```` ```html ```` block; extract it from there. Behaviour without a glossary was not tested.

vLLM (version 0.31.0 was used for the evaluation):

```bash
vllm serve <repo_id> --served-model-name e4b-sft3 --dtype bfloat16 --max-model-len 24576
```

transformers:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

repo = "<repo_id>"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForCausalLM.from_pretrained(repo, dtype="bfloat16", device_map="auto")
template = open("prompt_template.txt", encoding="utf-8").read()
prompt = template.replace("{{GLOSSARY}}", glossary).replace("{{CHAPTER_XHTML}}", chapter_xhtml)
inputs = tok.apply_chat_template([{"role": "user", "content": prompt}], add_generation_prompt=True,
                                 enable_thinking=False, return_dict=True, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=12288, do_sample=False)
```

GGUF with llama.cpp: `llama-server -m gguf/sft3-Q8_0.gguf -c 24576 -ngl 99`. llama.cpp warns that the Gemma 4 chat template is outdated and applies a workaround.

## Results

Final test: 147 held-out test chapters from novels not used in training. Three judges (DeepSeek v4.1 Flash, GLM 5.3 Flash and Muse Spark Open) compared the base model's translation with sft3's. They did not know which was which. An error counts when two of the three judges flag the same source paragraph as a major meaning error.

- Major meaning errors per chapter: **3.83 → 2.07** (−46%).
- Totals over the 147 chapters: mistranslations 303 → 241, omissions 140 → 5, gender errors 59 → 45, glossary errors 21 → 12, Korean left untranslated 39 → 0.
- Judges preferred sft3 in 342 votes to 70 (29 ties).
- Automatic checks on the 148 test chapters: tags identical to the source 38.5% → 83.8%; paragraph count matching 39.2% → 83.8%; Korean left in the body 27.0% → 2.0%; Korean chapter title 96.6% → 0%; repetition loops 9.5% → 3.4%; glossary terms used 93.2% → 96.5%; 2.7% of chapters stopped at the output limit.

Development split (57 chapters, same judges): the DeepSeek v4.1 Flash library translations average 0.65 agreed major meaning errors per chapter, sft3 averages 3.81 (glossary-name and untranslated-title errors not counted). sft3 is well behind DeepSeek v4.1 Flash on meaning accuracy.

## Limitations

- About two agreed major meaning errors per chapter remain. The judges' notes most often mention lost negations, wrong pronouns or speakers, swapped subjects, and gender slips (a male character called "she" through a whole chapter).
- About 3% of chapters stop at the 12,288-token limit or fall into a repetition loop.
- Trained and tested only on Korean web novels with XHTML chapters and glossaries.
- No human evaluation. The judges are LLMs and may share the teachers' blind spots.

## Training

- **Base:** weights rebuilt from `HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive` (see Licensing). Configuration and tokenizer come from `google/gemma-4-E4B-it`.
- **Stage 1** (supervised, 3,003 chapters from 780 novels): whole chapters, with English from the DeepSeek v4.1 Flash translations in the library and each novel's glossary.
- **sft3** (supervised, 5,283 chapters, 49.5M tokens, continued from stage 1): the model's own English drafts, corrected by DeepSeek v4.1 Flash. GLM 5.3 Flash checked each correction, and rejected corrections were reverted.
- LoRA rank 16 (alpha 16) on the attention and MLP projections of the text layers; learning rate 2e-5; sequences up to 16,384 tokens. Merged into the base for this release.

## Licensing and provenance

- The configuration and tokenizer come from `google/gemma-4-E4B-it`, released under the Gemma Terms of Use (https://ai.google.dev/gemma/terms). Redistribution and derivatives must follow those terms.
- The base weights were rebuilt from the GGUF of `HauhauCS/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive` (revision `45b6a334b4bcd1d7f37179df58b3b1d66a184e5d`). That is a third-party fine-tune, not Google's release; its name says "Uncensored".
- Training data are translations of copyrighted web novels, plus outputs of DeepSeek v4.1 Flash and GLM 5.3 Flash. Check the rights and the providers' terms before any public release.

## Files

- **Repository root:** merged BF16 weights (4 safetensors shards, about 15 GB) with config, tokenizer, chat template and generation config; `prompt_template.txt`.
- **`gguf/`:** `sft3-Q8_0.gguf` (recommended, 7.97 GB), `sft3-Q4_K_M.gguf` (5.30 GB) and `export.json` (conversion and parity report). Converted with llama.cpp v0.9.0 (commit `cd959bae99ff4bed22bef2604f45241c09bbb8c8`).
- **`adapter/`:** the LoRA adapter (PEFT format) for the same base.

Parity on three development chapters (3,800–4,000 prompt tokens, greedy decoding, first 200 output tokens) against the BF16 model: the top-1 token matched in every case. The greedy output stayed identical for 172–200 tokens with the BF16 GGUF, 144–176 with Q8_0 and 87–154 with Q4_K_M.
