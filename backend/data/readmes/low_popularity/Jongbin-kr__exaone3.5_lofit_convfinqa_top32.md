---
base_model: LGAI-EXAONE/EXAONE-3.5-7.8B-Instruct
library_name: transformers
pipeline_tag: text-generation
tags:
- exaone
- lofit
- finance
- korean
---

# Jongbin-kr/llama3_convfin_lofit_top32_seq4096_5ep

This is a fully merged EXAONE-3.5-7.8B-Instruct checkpoint tuned on
`lg_convfin_mcq_pc` with LoFiT. The final LoFiT-v stage tuned the top 32
task-sensitive attention heads for 5 epochs.

The learned per-head offsets are folded into an output-projection bias in each
attention layer. No LoFiT hook or adapter checkpoint is needed at inference.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Jongbin-kr/llama3_convfin_lofit_top32_seq4096_5ep"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    torch_dtype="auto",
    device_map="auto",
)
```

The base EXAONE model uses custom modeling code, so `trust_remote_code=True`
is required just as it is for the upstream checkpoint.
