---
language: [en, de, fr, es, it, pt, nl, pl, lv, et, lt, cs, sk, ro, bg, sl, hr, sv, da, fi, hu, uk, ru, zh, hi, ja, ko, el]
license: cc-by-4.0
library_name: transformers
tags: [multilingual, chatml, instruction-tuning, response-only-training]
base_model: TildeAI/TildeOpen-30b
datasets:
- HuggingFaceH4/ultrachat_200k
- utter-project/EuroBlocks-SFT-Synthetic-1124
- galileo-ai/ragbench
- martinsu/latvian-wikipedia-qa-gemma3
- yahma/alpaca-cleaned
pipeline_tag: text-generation
model-index:
- name: TildeOpen-30B-MU-Instruct
  results:
  - task: {type: text-generation, name: Multilingual QA}
    dataset: {name: EuroBlocks eval split (non-English), type: utter-project/EuroBlocks-SFT-Synthetic-1124}
    metrics:
    - {name: ROUGE-L, type: rouge-l, value: 0.2583}
    - {name: BERTScore (XLM-R-large), type: bertscore, value: 0.7495}
---

# TildeOpen-30B-MU-Instruct

Kudos to the Tilde team for a great base model and for taming that large LUMI beast — that was probably a crazy journey!

This is a fine-tuned 30B multilingual instruction model. It shows strong performance on the EuroBlocks multilingual evaluation compared to similarly sized models, with notably concise outputs.

These benchmarks for now are basically smoke tests to verify I didn't create a disaster. Always run your own evaluations for your specific use case.

I'll definitely use it for LV language work as a Gemma 3 replacement; it seems more capable. It seems to have acquired proper alignment from broad training sets too, at least at a basic level.

I'll run and publish more tests, perhaps using quantization.

On top of this fine-tune, one can use a lighter touch to nudge the model toward the right predictions.

ATM im running more RAG SFT on model, need to add more of a grounding behaviour.

# Run in prod:
- **1) TGI official docker will NOT WORK, use vLLM docker with --tokenizer-mode slow**
- **2) proper system prompt - correct language**
- **3) proper RAG - model is RAG-tuned**


Use correct prompt language as system role, it helps first token predictions for non-English.

## Quick Facts

- **Base**: TildeOpen-30B + ChatML format
- **Training**: 1 epoch SFT, response-only masking, 163M tokens
- **Languages**: 25 (focus on European)
- **Context**: 4096 tokens
- **Benchmark**: ROUGE-L 0.258 | BERTScore 0.750

## Usage

For proper prod usage check out:
https://huggingface.co/spaces/martinsu/tildeopen-30b-mu-instruct-space/blob/main/app.py
That code works.

Runs on official vLLM docker with **--tokenizer-mode slow** - typical prod usage.

**TGI will fail.** See further.

Use correct prompt language and text as system role, it helps accurate token prediction for all languages - they are trained implicit control codes for model, not random text.

Use RAG - model is tuned for RAG usage.

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("martinsu/tildeopen-30b-mu-instruct", use_fast=False)  # use_fast=False is critical
model = AutoModelForCausalLM.from_pretrained("martinsu/tildeopen-30b-mu-instruct", torch_dtype="auto", device_map="auto")

messages = ["role": "system", "content": "You are a helpful AI assistant."},{"role": "user", "content": "Explain quantum computing simply."}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Training Setup

**Hardware**: DeepSpeed ZeRO-3, BF16, Flash Attention 2, VRAM usage ~240GBs with some offloading.

**Hyperparameters**:
- LR: 2e-5, cosine schedule, 3% warmup
- Batch: 24 effective - 2 per gpu, 2 accum, 6 gpus
- Seq length: 4096
- Weight decay: 0.01, grad clip: 1.0
- Steps: 7,514 (1 epoch)

**Data** (163M tokens, 181K examples):
- HuggingFaceH4/ultrachat_200k (20% sampling) → 41.6K examples, 59.7M tokens
- utter-project/EuroBlocks-SFT-Synthetic-1124 (20% sampling) → 85K examples, 58.6M tokens  
- galileo-ai/ragbench all 12 subsets (30% sampling) → 22K examples, 26.4M tokens
  - Subsets: covidqa, cuad, delucionqa, emanual, expertqa, finqa, hagrid, hotpotqa, msmarco, pubmedqa, tatqa, techqa
- martinsu/latvian-wikipedia-qa-gemma3 (20% sampling, filtered) → 22.3K examples, 16.7M tokens
- yahma/alpaca-cleaned (20% sampling) → 10.4K examples, 2.5M tokens

**Language breakdown** (163M tokens across 25 languages):
- English: 117.7M (72%) - primary language
- Latvian: 16.7M (10%) - European focus
- Chinese: 10.1M (6%) - Asian coverage
- Portuguese: 3.0M (2%) - Romance
- Italian: 2.3M (1.4%) - Romance
- Spanish: 2.1M (1.3%) - Romance
- Hindi: 2.0M (1.2%)
- French: 1.8M (1.1%) - Romance
- German: 1.4M (0.8%) - Germanic
- Dutch: 1.1M (0.7%) - Germanic
- Plus 15 more: Japanese, Ukrainian, Swedish, Hungarian, Polish, Czech, Russian, Korean, Romanian, Finnish, Greek, Slovak, Norwegian, Slovenian, Estonian (4.9M combined, 3%)

**Response-only training**: Custom collator masks user/system messages, loss only on assistant responses.

### ChatML Template Format

All training data was formatted using the ChatML template with language-specific system prompts:

```
<|im_start|>system
You are a helpful AI assistant.<|im_end|>
<|im_start|>user
What is the capital of France?<|im_end|>
<|im_start|>assistant
The capital of France is Paris.<|im_end|>
```

**Language-specific system prompts** (examples):
- English: "You are a helpful AI assistant."
- Latvian: "Tu esi izpalīdzīgs mākslīgā intelekta asistents."
- German: "Sie sind ein hilfreicher KI-Assistent."
- French: "Vous êtes un assistant IA utile."

**Response-only masking**: Only the assistant's response tokens (between `<|im_start|>assistant` and `<|im_end|>`) contribute to the loss, `<|im_end|>` including. System and user messages are masked with label `-100`.

## Training Metrics (from trainer_state.json)

Continuous improvement, no plateau, no overfitting:

**Loss**: 0.871 (start) → 0.781 (mid ~3500 steps) → 0.729 (end 7514 steps)  
**Token Accuracy**: 76.3% → 77.6% → 78.9%  
**Gradient Norm**: 3.09 → 0.97 → 1.12  

Final eval: Loss 0.732, Accuracy 78.8% (train/eval gap 0.003 = doesnt look like overfitting)

## Benchmark

Smoke test benchmark. Not state-of-art work.

**Dataset**: EuroBlocks eval split (held-out 80% after training on 20%, non-English only)  
**N samples**: 150 random samples per model (English and Chinese excluded)
**Scoring**: BERTScore, ROUGE-L  
**Generation params**: temperature=0.7, max_new_tokens=2048, seed=42  
**All models used their native chat templates**

On the EuroBlocks multilingual benchmark, the models performed as follows:

- **This model**: ROUGE-L 0.258, BERTScore 0.750, with an average output length that closely matches the reference (about 1.0x).
- **Qwen2.5-32B-Instruct**: ROUGE-L 0.185, BERTScore 0.714, but tends to be much more verbose, producing outputs around 3.0x the reference length.
- **Gemma-3-27B-IT**: ROUGE-L 0.150, BERTScore 0.690, with output length similar to the reference (about 1.0x).
- **EuroLLM-22B-Instruct**: ROUGE-L 0.077, BERTScore 0.694, and also quite verbose, with outputs around 3.0x the reference length.

**Interpretation**: Higher scores may partly reflect output length matching reference length. Verbose models get penalized by ROUGE-L. No statistical significance computed. Single benchmark only - take with appropriate grain of salt.

## Known Issues
- **Base model doesnt have fast tokenizer**
- **By default AutoTokenizer.from_pretrained() will fire up fast tokenizer(TGI will do this), since this model doesnt have one, it cooks up broken one on the fly with tokens, that model is mostly unfamiliar, for example 179, that degrades performance seriously**
- **The main problem is that model fails silently - it recognizes some tokens and generates with degraded performance**
- **However when decoding with broken tokenizer we get sensible output, because model generates tokens that are in vocabulary**
- **Phase 1 only**: SFT checkpoint, no tool use or DPO phases yet
- **Use correct prompt language as system role**: It will scaffold model to predict given language tokens

## How vLLM(slow enabled) and TGI(default) tokenizes, example with curl:
This applies to base model too.

TGI docker - broken output.
```bash
curl -X POST http://x:8081/tokenize -H 'Content-Type: application/json' -d '{"model":"tgi","inputs":" Hello world <|im_end|> ","add_special_tokens":true}'

[{"id":179,"text":" ","start":0,"stop":1},{"id":53914,"text":"Hello","start":1,"stop":6},{"id":179,"text":" ","start":6,"stop":7},{"id":8141,"text":"world","start":7,"stop":12},{"id":179,"text":" ","start":12,"stop":13},{"id":131074,"text":"<|im_end|>","start":13,"stop":23},{"id":179,"text":" ","start":23,"stop":24}]
```
vLLM docker - right output.

```bash
curl -X POST http://x:8081/tokenize -H "Content-Type: application/json" -d '{"model": "martinsu/tildeopen-30b-mu-instruct", "prompt": " Hello world <|im_end|> ", "temperature": 0.7, "max_tokens": 150, "add_special_tokens":true}'
{"count":6,"max_model_len":65536,"tokens":[453,63484,8141,128948,131074,453],"token_strs":null}
```

They differ - vLLM tokenizer uses slow and outputs same tokens that model recognizes, TGI does not.

## Limitations & Safety

- **Not safety-tuned**: No RLHF, no red-teaming, no toxicity filtering
- **Hardware requirements**: 30B params needs above average compute
- **No harm evaluation**: ToxiGen, BBQ, etc. not run
- **Standard LLM caveats**: It's a smart token predictor, not a legal or medical professional. Can hallucinate. Use responsibly.



## Why It (Probably) Works

**English-dominant (72%)**: Preserves base model's English token distribution and reasoning chains (likely optimized on English-heavy pretraining/instruction data) while extending multilingual generalization

**Diverse training set selection**: Can't overfit on specific style, formatting, length, or distilled patterns

**Diverse language selection**: Helps with generalization and multilingual support

**Single epoch**: Avoids overfitting on instruction data. Eval loss tracks train loss closely = good generalization, not memorization

**Response-only masking**: Loss computed only on assistant responses, not user prompts. Focuses learning signal on output quality

**Moderate batch size (24)**: Smaller batches may reduce risk of overshooting minima

**Limited sampling (20-30%)**: 163M tokens should be sufficient for SFT without requiring full datasets

## Citation

```bibtex
@misc{tildeopen30b-mu-instruct,
  author = {Martins Udris},
  title = {TildeOpen-30B-MU-Instruct},
  year = {2025},
  url = {https://huggingface.co/martinsu/tildeopen-30b-mu-instruct}
}
```

---

**Contact**: martins@udris.eu | **License**: CC-BY-4.0
