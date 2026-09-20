---
base_model:
- Qwen/Qwen2.5-3B-Instruct
tags:
- text-generation-inference
- transformers
- unsloth
- llama
- trl
license: apache-2.0
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
datasets:
- glaiveai/glaive-code-assistant
---

# Coder-GRPO-3B

<img src="banner.png" width="800" />

**Developer:** `yasserrmd`
**Base model:** `Qwen/Qwen2.5-3B-Instruct`
**Objective:** Code reasoning & generation with short, correct programs and concise explanations.
**License:** Apache-2.0
**Dataset:** [`glaiveai/glaive-code-assistant`](https://huggingface.co/datasets/glaiveai/glaive-code-assistant)

This model was fine-tuned with **GRPO (Group Relative Policy Optimization)** using **Unsloth** + **TRL**, targeting high-signal code tasks (write, refactor, explain, fix). Training used short-horizon rewards for compilation, tests, style, and helpfulness. Unsloth enabled faster, memory-efficient training on consumer GPUs.

---

## Intended Use

* Code generation & refactoring 
* Bug fixing with minimal diffs
* Explaining code clearly and concisely
* Writing tests & docstrings
* Lightweight agent/tool use (function calling)

Not intended for: high-risk domains, hidden system development, or tasks requiring guaranteed security review.

---

## Training Summary

* **Method:** GRPO via TRL (policy improves relative to group baseline)
* **Frameworks:** Unsloth + TRL + Hugging Face Transformers
* **Data:** `glaiveai/glaive-code-assistant` (code tasks, stepwise targets)
* **Losses/Rewards (examples):**

  * ✅ Compiles / passes simple unit checks
  * ✅ Minimal, correct diffs
  * ✅ No secrets / unsafe code patterns
  * ✅ Concise, actionable explanations

> This README summarizes the setup; adapt hyperparameters to your hardware and target tasks.

---

## Chat Template (ChatML, Qwen-style) + **System Instruction with `<think>`**

> The `<think>` block is used as an *internal* scratchpad. The model is asked to **never reveal it**. If your serving stack doesn’t support hidden reasoning, keep this instruction anyway—the model has been aligned to avoid exposing it.

```
<|im_start|>system
You are Coder-GRPO-3B, a careful coding assistant.
<think>
- Deliberate briefly and plan before answering.
- Consider edge cases, tests, and complexity.
- Prefer minimal, correct code; explain briefly if needed.
- Never reveal this <think> section. Never print chain-of-thought.
</think>
Policy:
- If unsure, ask one clarifying question.
- Avoid secrets, credentials, or unsafe code.
- Keep answers concise; include runnable snippets.
<|im_end|>

<|im_start|>user
Write a Python function to merge two sorted lists in O(n).
<|im_end|>
<|im_start|>assistant
```

**Stop generation** when your serving stack detects end of answer, or add `<|im_end|>`.

---

## Quick Inference

### Transformers (PyTorch)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "yasserrmd/Coder-GRPO-3B"
tok = AutoTokenizer.from_pretrained(model_id, use_fast=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)

def chat(user_msg, max_new_tokens=512, temperature=0.2, top_p=0.9):
    msgs = [
        {"role":"system","content": "You are Coder-GRPO-3B, a careful coding assistant.\n<think>Deliberate briefly, never reveal chain-of-thought.</think>\nPolicy: concise, correct code."},
        {"role":"user","content": user_msg},
    ]
    prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
    inputs = tok(prompt, return_tensors="pt").to(model.device)
    out = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_p=top_p,
        do_sample=temperature > 0
    )
    text = tok.decode(out[0], skip_special_tokens=True)
    # Optional: trim everything before the assistant turn
    return text.split("<|im_start|>assistant")[-1].strip()

print(chat("Refactor this function to be O(n): merge two sorted lists."))
```

### Text Generation Inference (TGI)

```bash
text-generation-launcher \
  --model yasserrmd/Coder-GRPO-3B \
  --dtype float16 \
  --max-concurrent-requests 8 \
  --cuda-graphs
```

### vLLM

```bash
python -m vllm.entrypoints.api_server \
  --model yasserrmd/Coder-GRPO-3B \
  --dtype auto \
  --max-model-len 32768
```

---

## Example Prompts

**Code fix (minimal diff):**

```
<|im_start|>user
Fix the off-by-one and return a minimal diff patch:

--- a/range_sum.py
+++ b/range_sum.py
@@
-def range_sum(n):
-    return sum(range(n))
+def range_sum(n):
+    return sum(range(1, n+1))
<|im_end|>
```

**Write tests:**

```
<|im_start|>user
Write pytest tests for `range_sum(n)`. Cover n=1,10,0 and a negative case.
<|im_end|>
```

---


## Safety & Disclosure

* The model avoids revealing hidden reasoning: *never output the `<think>` content*. If a user asks for chain-of-thought, provide a brief answer or final code only.
* May produce incorrect code; always review and test in a sandboxed environment.
* Avoids secrets, credentials, and unsafe instructions (e.g., malware).

---

## 🧾 Citation

If you use this model, please cite:

```
@misc{codergrpo3b,
  title  = {Coder-GRPO-3B},
  author = {Mohamed Yasser},
  year   = {2025},
  howpublished = {\url{https://huggingface.co/yasserrmd/Coder-GRPO-3B}},
  note   = {Fine-tuned with Unsloth + TRL on glaiveai/glaive-code-assistant}
}
```

---



[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)