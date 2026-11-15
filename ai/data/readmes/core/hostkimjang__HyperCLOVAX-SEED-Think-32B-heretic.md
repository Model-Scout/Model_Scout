---
license: other
license_name: hyperclovax
license_link: >-
  https://huggingface.co/naver-hyperclovax/HyperCLOVAX-SEED-Think-32B/blob/main/LICENSE
language:
- en
- ko
base_model:
- naver-hyperclovax/HyperCLOVAX-SEED-Think-32B
pipeline_tag: text-generation
tags:
- llama
- chat
- bf16
- safetensors
- model-editing
---

# HyperCLOVAX-SEED-Think-32B-heretic

**HyperCLOVAX-SEED-Think-32B-heretic**은 `naver-hyperclovax/HyperCLOVAX-SEED-Think-32B`를 기반으로, 사후(weight editing) 방식으로 **과잉 거부(refusal) 성향을 완화**하는 방향의 수정이 적용된 변형 모델입니다.

---

## Model Summary (KO)

- **Base model**: `naver-hyperclovax/HyperCLOVAX-SEED-Think-32B`
- **Format**: BF16 (safetensors)
- **Approach**: targeted post-hoc **weight editing**
- **Primary effect**: refusal behavior calibration (reduce over-refusal)  
- **Observed drift**: small (see KL metric below)

---

## Model Summary (EN)

- **Base model**: `naver-hyperclovax/HyperCLOVAX-SEED-Think-32B`
- **Weights**: BF16 (safetensors)
- **Method**: targeted post-hoc **weight editing**
- **Goal**: reduce over-refusal on benign/borderline prompts while keeping the output distribution close to the base model

---

## What’s Changed

This variant applies focused modifications around projection layers to shift refusal-related behavior.

### Editing Parameters (as-run)

- `direction_index = 42.77`
- `attn.o_proj.max_weight = 1.13`
- `attn.o_proj.max_weight_position = 67.44`
- `attn.o_proj.min_weight = 0.46`
- `attn.o_proj.min_weight_distance = 25.36`
- `mlp.down_proj.max_weight = 1.49`
- `mlp.down_proj.max_weight_position = 43.36`
- `mlp.down_proj.min_weight = 0.97`
- `mlp.down_proj.min_weight_distance = 26.08`

### Behavior / Drift Indicators

- **Refusals**: **10 / 100**
- **KL divergence**: **0.1123**

> Note: these values depend on your prompt set and refusal criterion.  
> If you can disclose the evaluation slice (even roughly), add it in the section below.

---

## Evaluation Notes

### Refusal Definition (edit as needed)
A completion is counted as a refusal if it:
- explicitly denies compliance (e.g., “I can’t / I won’t”), **and**
- does not provide a meaningful safe alternative or partial completion.

### Prompt Set
- prompt mix: `[benign / borderline / policy-sensitive]`
- sample size: `100`
- source: `[private/internal or 공개 가능하면 설명]`

---

## Intended Use

### Recommended
- General chat
- Creative writing / brainstorming
- Everyday Q&A where over-refusal hurts usability
- Research on refusal behavior, steering, and drift tradeoffs

### Not Recommended (without extra guardrails)
- Public-facing deployment without moderation/filters
- High-stakes domains (medical/legal/financial)
- Any use that requires strict compliance guarantees

---

## Safety & Risks

Reducing refusals can increase the chance that the model responds in situations where the base model would refuse.
For real deployments, consider:
- input filtering / output moderation
- rate limits & logging
- clear acceptable-use policy and enforcement

Known limitations:
- side effects may exist (tone shift, verbosity changes, occasional riskier completions)
- evaluation is not exhaustive; additional red-teaming is recommended

---
## GGUF (llama.cpp) Inference

This repository also provides an **F16 GGUF** build under `gguf/`, intended for running with **llama.cpp**.

### Run with `llama-server` (Thinking ON)

> This command enables the model's "thinking" behavior via `--chat-template-kwargs`.

#### Linux / macOS

```bash
./llama-server \
  -m {PATH}/HyperCLOVAX-SEED-Think-32B-heretic2.f16.gguf \
  --host 0.0.0.0 --port 10000 \
  --jinja \
  --chat-template-kwargs '{"thinking":true,"enable_thinking":true}' \
  -cb -fa on

---

## How to Use

### Transformers (example)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

model_id = "hostkimjang/HyperCLOVAX-SEED-Think-32B-heretic"  # <- your repo id

tok = AutoTokenizer.from_pretrained(model_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Explain KL divergence in simple terms."},
]

# If the tokenizer provides a chat template:
prompt = tok.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

inputs = tok(prompt, return_tensors="pt").to(model.device)
out = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.95,
    do_sample=True,
)
print(tok.decode(out[0], skip_special_tokens=True))
