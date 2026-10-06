---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- en
- ko
base_model:
- trillionlabs/Gravity-30B-A5B-Preview
base_model_relation: finetune
tags:
- gravity
- biomedical
- biology
- instruction-tuning
- mixture-of-experts
- tool-use
- biomni
---

# BioGravity-Inst

**BioGravity-Inst** is a biomedical instruction model from AIGEN Sciences, Inc., developed from the Gravity 30B-A5B family. It is intended for biomedical research in the Biomni A1 environment, including question answering, evidence gathering, computation, and tool-assisted analysis.

The repository provides a complete merged checkpoint, tokenizer, chat template, and Gravity model-loading code.

## Model Summary

| Property | Value |
| --- | --- |
| Developer | AIGEN Sciences, Inc. |
| Base model | [Gravity-30B-A5B-Preview](https://huggingface.co/trillionlabs/Gravity-30B-A5B-Preview) |
| Architecture | `GravityMoEForCausalLM` (`gravity_moe`), sparse MoE with MLA |
| Total / active parameters | 29.56B / approximately 5.34B |
| Layers / routed experts | 52 / 64, with 8 experts selected per token |
| Languages | English |
| Configured context limit | 131,072 tokens |
| Stored precision | FP32, 24 safetensors shards |
| Evaluated inference precision | BF16 |
| Agent environment | Biomni A1 |
| License | Apache 2.0 |

## Evaluation Results

### Before and after biomedical adaptation

The original evaluation report recorded the following results on all **433 questions** in Biomni Eval1.

| Model stage | A1 harness applied / required for this setting | Harness configuration | Accuracy |
| --- | --- | --- | --- |
| Gravity initialization, before biomedical adaptation | Yes / Yes | Original A1 evaluation with scientific skills and tools | 27.02% |
| Biomedical iteration-4 model, after adaptation | Yes / Yes | Original A1 evaluation with scientific skills and tools | **56.81%** |
| **Change within the original reported comparison** | — | — | **+29.79 percentage points** |

**Harness availability:** the reported before/after scores use the original Biomni A1 evaluation harness with scientific skills and tools. The harness and its configuration are **available upon request** through AIGEN Sciences. These scores measure the model together with its A1 environment. A matched evaluation without the harness is not available for this comparison.

## Quickstart

Use a CUDA-compatible PyTorch installation and the tested Transformers version:

```bash
pip install "transformers==4.57.6" accelerate safetensors
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "aigensciences/BioGravity-Inst"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    trust_remote_code=True,
    dtype=torch.bfloat16,
    device_map="auto",
    attn_implementation="eager",
).eval()

messages = [
    {"role": "system", "content": "You are a biomedical research assistant."},
    {"role": "user", "content": "Explain why a control group is needed when studying a biological perturbation."},
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
    tokenizer_kwargs={"return_token_type_ids": False},
).to(model.device)

with torch.inference_mode():
    outputs = model.generate(**inputs, max_new_tokens=1024, do_sample=False)

continuation = outputs[0, inputs["input_ids"].shape[-1]:]
print(tokenizer.decode(continuation, skip_special_tokens=False))
```

BF16 loading requires approximately 59 GB for weights, plus memory for the KV cache and runtime. The configured 131,072-token context limit does not establish benchmark performance at that length.

### Biomni A1 integration

Prepare the tools and data lake using the Biomni installation instructions, together with the evaluation harness supplied on request.

The model uses `<think>...</think>` for reasoning. A1 code actions use `<execute>...</execute>`, observations use `<observation>...</observation>`, and final answers use `<solution>...</solution>`. The A1 runtime executes actions and returns observations; the text-generation example above does not execute tools.

Keep the provided tokenizer and chat template together, and decode with `skip_special_tokens=False`. The default generation prompt opens a `<think>` segment. For an empty thinking segment, pass `enable_thinking=False` to `apply_chat_template`.

## Limitations

- **Research use and environment.** The model is released for research purposes and is intended to operate in the Biomni A1 environment.
- **Factual accuracy.** Generated content, explanations, and references may contain factual errors. Expert verification is required before relying on the results.
- **Knowledge freshness.** Literature and guidelines published after the training-data cutoff are not reflected in the model weights. Current sources need to be retrieved and verified separately.
- **Language coverage.** Performance in languages other than Korean and English is not guaranteed.
- **Harness dependence.** The reported Eval1 results require the corresponding A1 harness, tools, scientific skills, and data configuration. They do not measure standalone chat performance.

## Acknowledgements

Support for this research comes from the **인공지능 특화 파운데이션 모델 프로젝트 (Domain-Specific Foundation Model Project)**. **과학기술정보통신부 (MSIT)** provides funding, and **정보통신산업진흥원 (NIPA)** administers the program.

We thank **Lunit**, **Trillion Labs**, **SK Biopharmaceuticals**, **Kakao Healthcare** and the consortium's industry, academic, and hospital partners for the Gravity research collaboration. The Lunit model card provides the consortium acknowledgements on which this statement is based. We also acknowledge the Biomni project for its agent framework and evaluation resources.

## License
 
The model is released under the Apache License 2.0. Research use describes its intended application and does not add restrictions to the license.

## Contact

AIGEN Sciences, Inc. — contact the organization to request the evaluation harness and configuration.