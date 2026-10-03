---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- ko
- en
base_model:
- trillionlabs/Gravity-30B-A5B-Preview
base_model_relation: finetune
tags:
- gravity
- biomedical
- biology
- bilingual
- instruction-tuning
- mixture-of-experts
- tool-use
- biomni
---

# BioGravity-bilingual-Inst

**BioGravity-bilingual-Inst** is a Korean–English biomedical instruction model from [AIGEN Sciences, Inc.](https://huggingface.co/aigensciences), developed from the Gravity 30B-A5B family. It is intended for biomedical explanations, instruction following, and tool-assisted research in the [Biomni A1 environment](https://github.com/snap-stanford/Biomni).

The repository provides a complete merged checkpoint, tokenizer, chat template, Gravity model-loading code, and A1 protocol metadata.

## Model Summary

| Property | Value |
|---|---|
| Developer | AIGEN Sciences, Inc. |
| Base model | [Gravity-30B-A5B-Preview](https://huggingface.co/trillionlabs/Gravity-30B-A5B-Preview) |
| Architecture | `GravityMoEForCausalLM` (`gravity_moe`), sparse MoE with MLA |
| Total / active parameters | 29.56B / approximately 5.34B |
| Layers / routed experts | 52 / 64, with 8 experts selected per token |
| Primary languages | Korean and English |
| Configured context limit | 131,072 tokens |
| Stored precision | FP32, 24 safetensors shards |
| Supported inference precision | BF16 |
| Agent environment | [Biomni A1](https://github.com/snap-stanford/Biomni) |
| A1 protocol | Dedicated execute, solution, and observation special tokens |
| License | [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) |

## Evaluation Results

Reported [Biomni Eval1](https://huggingface.co/datasets/biomni/Eval1) results from a separate evaluation environment:

| Model | Evaluation harness | Accuracy |
|---|---|---:|
| BioGravity-bilingual-Inst | Not applied | 39.72% |
| **BioGravity-bilingual-Inst** | **Applied** | **55.1%** |

The **55.1%** result uses the evaluation harness. The harness and its configuration are **available upon request** through [AIGEN Sciences](https://huggingface.co/aigensciences).

## Quickstart

Use a CUDA-compatible PyTorch installation and the tested Transformers version:

```bash
pip install "transformers==4.57.6" accelerate safetensors
```

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "aigensciences/BioGravity-bilingual-Inst"
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
    {"role": "user", "content": "관찰연구에서 상관관계와 인과관계의 차이를 한국어로 설명해 주세요."},
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

Prepare the tools and data lake using the [Biomni installation instructions](https://github.com/snap-stanford/Biomni#installation), together with the evaluation harness supplied on request.

| Purpose | Format |
|---|---|
| Reasoning segment | `<think>...</think>` |
| Code action | `<execute>Python code</execute>` |
| Tool observation | `<observation>tool result</observation>` |
| Final answer | `<solution>answer</solution>` |

The A1 runtime executes actions and returns observations. Preserve the six dedicated action/observation special tokens by using **`skip_special_tokens=False`**. The runtime should retain the `</execute>` and `</solution>` stop markers when delimiting actions and final answers.

The default generation prompt opens a `<think>` segment. Passing `enable_thinking=False` to `apply_chat_template` prefills an empty `<think></think>` segment. Keep the tokenizer, chat template, and `protocol_manifest.json` together when deploying the model.

## Limitations

- **Research use and environment.** The model is released for research purposes and is intended to operate in the Biomni A1 environment.
- **Factual accuracy.** Generated content, explanations, and references may contain factual errors. Expert verification is required before relying on the results.
- **Knowledge freshness.** Literature and guidelines published after the training-data cutoff are not reflected in the model weights. Current sources need to be retrieved and verified separately.
- **Language coverage.** Performance in languages other than Korean and English is not guaranteed.
- **Harness dependence.** The reported 55.1% Eval1 result uses the evaluation harness and environment associated with that measurement. Performance depends on the deployment and evaluation setup.

## Acknowledgements

Support for this research comes from the **인공지능 특화 파운데이션 모델 프로젝트 (Domain-Specific Foundation Model Project)**. **과학기술정보통신부 (MSIT)** provides funding, and **정보통신산업진흥원 (NIPA)** administers the program.

We thank **Lunit**, **Trillion Labs**, and the consortium's industry, academic, and hospital partners for the Gravity research collaboration. The [Lunit model card](https://huggingface.co/learning-unit/L1-30B-A5B#-acknowledgements) provides the consortium acknowledgements on which this statement is based. We also acknowledge the [Biomni project](https://github.com/snap-stanford/Biomni) for its agent framework and evaluation resources.

## License

The model is released under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). Research use describes its intended application and does not add restrictions to the license.

## Contact

[AIGEN Sciences, Inc.](https://huggingface.co/aigensciences) — contact the organization to request the evaluation harness and configuration.