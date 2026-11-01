---
license: apache-2.0
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
tags:
- blind-spots
- llm-evaluation
- base-model
- lfm2.5
pretty_name: LFM2.5-1.2B-Base Blind Spots
size_categories:
- n<100
---

# LFM2.5-1.2B-Base Blind Spots Dataset

This dataset documents **10 diverse failure cases** (blind spots) of the
[LiquidAI/LFM2.5-1.2B-Base](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Base) model —
a 1.17B parameter pre-trained base model released in November 2025.

## Model Tested

| Field | Detail |
|---|---|
| Model | [LiquidAI/LFM2.5-1.2B-Base](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Base) |
| Parameters | 1.17B |
| Release | November 2025 |
| Architecture | Hybrid (LIV convolution + GQA blocks) |
| Context Length | 32,768 tokens |
| Languages | EN, AR, ZH, FR, DE, JA, KO, ES |

## How I Loaded the Model

The model was loaded on **Google Colab (free tier, T4 GPU)** using the
`transformers` library (v5.0.0). No `trust_remote_code` was required.
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "LiquidAI/LFM2.5-1.2B-Base"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    dtype=torch.bfloat16
)

def generate(prompt, max_new_tokens=150):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            temperature=None,
            top_p=None,
            pad_token_id=tokenizer.eos_token_id
        )
    generated = outputs[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(generated, skip_special_tokens=True)
```

## Dataset Fields

| Field | Description |
|---|---|
| `id` | Test case number (1–10) |
| `category` | Type of task tested |
| `input` | The prompt given to the model |
| `expected_output` | The correct answer |
| `model_output` | What LFM2.5-1.2B-Base actually generated |
| `blind_spot` | Description of the failure pattern |

## Loading the Dataset
```python
from datasets import load_dataset
ds = load_dataset("saadumar26/lfm25-base-blind-spots")
print(ds["train"][0])
```

## Blind Spot Patterns Found

Testing across 10 diverse categories revealed 5 recurring failure patterns:

**1. MCQ Obsession** — The model wraps simple factual answers inside
unnecessary multiple-choice format, even when the prompt is a direct question.
Seen in: Chinese Knowledge, Japanese Comprehension, Hallucination tests.

**2. Repetition Loop** — The model generates a correct (or partially correct)
answer, then repeats the same phrase dozens of times until max tokens is reached.
Seen in: Logical Reasoning, German Comprehension.

**3. Translation Failure** — When asked to translate into Arabic, French, or
Spanish, the model ignores the instruction and responds in English instead.
Seen in: Translation EN→FR, Translation EN→ES, Arabic Translation.

**4. Topic Drift / Over-generation** — The model answers correctly but cannot
stop — it continues generating unrelated math problems, science questions, or
trivia after the answer.
Seen in: Math Reasoning, Spanish Reasoning.

**5. Hallucination with False Confidence** — When asked impossible questions
(president of Mars), the model fabricates plausible-sounding MCQ options
instead of refusing or saying the question is invalid.
Seen in: Hallucination category.

## Fine-Tuning Recommendations

### What kind of dataset would fix these errors?

**For MCQ Obsession + Topic Drift:**
Fine-tune on a dataset of (prompt, short clean answer) pairs where the correct
behavior is to stop after answering. Examples: Natural Questions, TriviaQA,
or custom QA pairs with explicit EOS after the answer.

**For Translation Failures:**
Fine-tune on high-quality parallel translation datasets covering the supported
languages: FLORES-200, CCAligned, or OPUS corpora for AR, FR, ES pairs.

**For Repetition Loops:**
Fine-tune with repetition penalty enforced during training, or use datasets
with diverse sentence continuations (e.g., C4, OpenWebText) to reduce
degenerate repetition patterns.

**For Hallucination:**
Fine-tune on refusal datasets — examples where the model learns to say
"I don't know" or "This is not possible." Datasets like
TruthfulQA, or custom (impossible question → refusal) pairs work well.

### How big of a dataset would be needed?

| Problem | Recommended Dataset Size |
|---|---|
| MCQ format / topic drift | 50,000–100,000 QA pairs (short answer format) |
| Translation failures | 500,000+ parallel sentence pairs per language |
| Repetition loops | 100,000+ diverse continuations |
| Hallucination / refusal | 10,000–50,000 refusal examples |

In general, **50,000–100,000 high-quality supervised fine-tuning (SFT) examples**
covering all the above failure modes would be a reasonable starting point for
a 1.2B parameter model. Smaller, higher-quality datasets tend to outperform
larger noisy ones at this scale.

### How would you assemble such a dataset?

A combination of existing open datasets (TriviaQA, FLORES-200, TruthfulQA)
filtered for quality, plus **synthetic data generation** using a larger
teacher model (e.g., GPT-4o or Claude) to create clean (prompt, short answer)
pairs that demonstrate the correct stopping behavior, correct translation, and
appropriate refusal patterns.
