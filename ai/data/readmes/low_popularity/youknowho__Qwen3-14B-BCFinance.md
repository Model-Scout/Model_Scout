---
base_model: Qwen/Qwen3-14B
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
language:
- ko
- en
tags:
- qwen3
- finance
- korean
- sft
- qlora
- merged
datasets:
- BCCard/BCAI-Finance-Kor
---

# Qwen3-14B-BCFinance

A full-weight Qwen3-14B fine-tuned for the Korean financial domain. The model was
trained with QLoRA on the BCCard Korean finance QA dataset, then the adapter was
merged back into the base weights. No PEFT library is needed at inference time.

Primary language is Korean. The model answers Korean financial questions in a
concise single-paragraph style.

## Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
    "Qwen3-14B-BCFinance",          # replace with <your-username>/Qwen3-14B-BCFinance
    dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="sdpa",
)
tokenizer = AutoTokenizer.from_pretrained("Qwen3-14B-BCFinance")
model.eval()

messages = [
    {"role": "system", "content": "당신은 금융 전문가 AI 어시스턴트입니다. 사용자의 질문에 정확하고 전문적으로 답변하세요."},
    {"role": "user", "content": "DSR 규제가 대출 한도에 어떤 영향을 주나요?"},
]
text = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
with torch.no_grad():
    out = model.generate(**inputs, max_new_tokens=400, do_sample=False)
print(tokenizer.decode(out[0][inputs.input_ids.shape[1]:], skip_special_tokens=True))
```

Loading in bfloat16 needs roughly 30 GB of memory. For a smaller footprint, load
with `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4")`.

## Training setup

| Item | Value |
|---|---|
| Base model | Qwen/Qwen3-14B |
| Method | QLoRA (NF4 4-bit base, double quant, bf16 compute), adapter merged after training |
| LoRA rank / alpha | 32 / 64 |
| LoRA dropout | 0.05 |
| Target modules | q, k, v, o, gate, up, down projections (all 7) |
| Trainable parameters | 128.5M (0.9% of base) |
| Train / validation split | 3,000 / 1,000, balanced across 17 finance topics |
| Epochs | 3 (342 optimizer steps) |
| Effective batch size | 16 (per-device 8 x grad accum 2) |
| Max sequence length | 1024, BFD packing |
| Learning rate | 1e-4, cosine schedule, 30 warmup steps |
| Optimizer | paged_adamw_8bit, max grad norm 1.0 |
| Loss type | nll |
| Hardware | NVIDIA GB10 (DGX Spark), about 10 hours |

## Training results

| Metric | Start | End |
|---|---|---|
| Train loss | 1.1766 | 0.4357 |
| Validation loss | 0.5487 (step 200) | 0.5473 (step 342) |
| Train token accuracy | 74.2% | 86.8% |
| Validation token accuracy | 83.9% | 84.1% |

Validation loss did not regress through the end of training, so the run finished
before entering an overfitting regime.

## Evaluation

34 questions were drawn from the held-out validation split, two per topic across
all 17 finance topics, and compared against the unmodified base model. Greedy
decoding, 400 new tokens maximum, scored with ROUGE-L against the reference answers.
The validation split shares no examples with the training split.

| Metric | Base | This model | Change |
|---|---|---|---|
| Win rate | - | 28/34 (82.4%) | - |
| ROUGE-L F1 | 0.2011 | 0.2512 | +24.9% |
| ROUGE-L recall | 0.2308 | 0.2566 | +11.2% |
| ROUGE-L precision | 0.2707 | 0.3796 | +40.2% |
| Character 3-gram Jaccard | 0.1167 | 0.1633 | +39.9% |

A paired bootstrap over 10,000 resamples puts the 95% confidence interval for the
ROUGE-L difference at [+0.031, +0.070], which excludes zero. 15 of 17 topics improved.
Crypto/fintech, investment/wealth management, and derivatives/risk declined slightly.

### Qualitative improvements

Korean financial terminology became more accurate.

- DSR: the base model answers "부채상환비율"; this model answers "총부채원리금상환비율",
  the official term used by the Financial Supervisory Service.
- BC Card Paybooc: the base model hallucinates it as "a service operated by KB Kookmin Bank";
  this model correctly attributes it to BC Card.

## Limitations

**1. Responses are short.** Reference answers average 716 tokens while this model
generates 328. 33.4% of the training examples were truncated at the 1024-token limit,
so the model learned to wrap up early. If you need longer explanations, retrain with
`max_length=2048`, which raises token coverage from 73% to 98%.

**2. The nature of the gain.** Precision rose 40% while recall rose only 11%. The
improvement comes mostly from cutting filler rather than covering more of the reference
content.

**3. System-prompt role adherence weakened.** Even when the system prompt restricts the
model to finance, it answers off-domain questions. The base model declines a cooking
question; this model answers it. Add refusal examples to the training data if you need
domain gating.

**4. Factual accuracy is unverified.** ROUGE-L measures surface overlap, not truth.
Individual hallucination fixes were confirmed, but a general reduction in hallucination
was not demonstrated. An LLM-as-judge or human evaluation is needed for that claim.

**5. General capability is retained.** Eight off-domain probes covering arithmetic,
coding, general knowledge, logical reasoning, vocabulary, history, and physics all
remained correct. No catastrophic forgetting was observed.

## Intended use and caution

This is a research model for Korean financial text generation. Do not use its output
as the basis for investment decisions or financial advice. Generated content may be
factually wrong and must be verified against official sources.

## License

Inherits the license of the base model, Qwen/Qwen3-14B. Trained on BCCard/BCAI-Finance-Kor.
