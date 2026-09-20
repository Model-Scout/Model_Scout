---
language:
- en
- de
- fr
- es
- it
- pt
- ja
- ko
- zh
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- ibm-granite
- granite
- causal-lm
- text-generation
- heretic
- representation-editing
base_model: ibm-granite/granite-4.2-3b
---

# Granite 4.2 3B Heretic

`Granite 4.2 3B Heretic` is a representation-edited version of
[`ibm-granite/granite-4.2-3b`](https://huggingface.co/ibm-granite/granite-4.2-3b).

The model was produced using the Heretic representation-editing workflow. The
purpose of this release is research and experimentation with model behavior,
refusal behavior, instruction following, and the trade-off between behavioral
changes and preservation of the base model's capabilities.

## Model details

- **Base model:** `ibm-granite/granite-4.2-3b`
- **Architecture:** `GraniteForCausalLM`
- **Parameter count:** approximately 3 billion
- **Model type:** causal language model
- **Format:** Safetensors
- **Repository:** `tinyopsec/granite-4.2-3b-Heretic`
- **License:** Apache 2.0, subject to the base model's terms and conditions

The weights may be split into multiple `.safetensors` shard files. This is
expected and is handled automatically by Transformers through the model index
file.

## Installation

```bash
pip install -U transformers accelerate safetensors torch
```

## Basic usage

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "tinyopsec/granite-4.2-3b-Heretic"

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True,
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True,
)

messages = [
    {
        "role": "user",
        "content": "Explain the benefits and limitations of renewable energy.",
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
).to(model.device)

with torch.inference_mode():
    outputs = model.generate(
        inputs,
        max_new_tokens=256,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.05,
        pad_token_id=tokenizer.eos_token_id,
    )

new_tokens = outputs[0][inputs.shape[-1]:]

print(
    tokenizer.decode(
        new_tokens,
        skip_special_tokens=True,
    )
)
```

## Loading with automatic dtype

For hardware where `float16` is not appropriate, use automatic dtype selection:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "tinyopsec/granite-4.2-3b-Heretic"

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True,
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype="auto",
    device_map="auto",
    trust_remote_code=True,
)
```

## CPU usage

CPU inference is possible but considerably slower and may require substantial
system RAM:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "tinyopsec/granite-4.2-3b-Heretic"

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    trust_remote_code=True,
)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype="auto",
    device_map="cpu",
    trust_remote_code=True,
)
```

## Intended use

This model is intended for:

- research into representation editing;
- evaluation of refusal and instruction-following behavior;
- comparison with the original Granite 4.2 3B model;
- local experimentation and prototyping;
- studying capability and alignment trade-offs.

## Important limitations

This model has not been comprehensively evaluated after editing. In particular,
it may differ from the base model in:

- refusal behavior;
- factual accuracy;
- instruction following;
- robustness against prompt injection;
- bias and harmful stereotypes;
- consistency across languages;
- coding and reasoning performance;
- output stability and repetition behavior.

The model may produce incorrect, unsafe, biased, or misleading content. Its outputs
must be reviewed by a human before being used in applications, published, or
relied upon for consequential decisions.

The model should not be used as an autonomous authority, safety filter, medical
advisor, legal advisor, financial advisor, or substitute for professional
judgment.

## Recommended evaluation

When evaluating this model, compare it with the original base model using the
same:

- prompts;
- tokenizer;
- decoding parameters;
- random seed;
- maximum output length;
- hardware and dtype.

Recommended checks include:

1. general instruction following;
2. factual question answering;
3. multilingual generation;
4. summarization;
5. code generation;
6. refusal and safety behavior;
7. hallucination rate;
8. repetition and degeneration;
9. long-context behavior;
10. performance on the user's own task-specific benchmark.

A useful baseline is:

```python
BASE_MODEL_ID = "ibm-granite/granite-4.2-3b"
EDITED_MODEL_ID = "tinyopsec/granite-4.2-3b-Heretic"
```

## Reproducibility

The edited model was generated from the Granite 4.2 3B base model using a
Heretic-style optimization workflow.

For exact reproduction, record and publish:

- the Heretic version;
- the Transformers version;
- the PyTorch version;
- the GPU model;
- the dtype;
- the random seed;
- the number of trials;
- the number of startup trials;
- the selected trial;
- the optimization configuration;
- the export method;
- the evaluation prompts and results.

The final model should be treated as an experimental derivative until those
details and a broader evaluation are published.

## Relationship to the base model

This repository contains modified weights. It is not the original IBM Granite
release.

Please read the original model card before using this model:

- [IBM Granite 4.2 3B](https://huggingface.co/ibm-granite/granite-4.2-3b)

The base model's license, attribution requirements, acceptable-use rules, and
other conditions remain relevant.

## License

This repository is released under the Apache License 2.0, subject to the
license and usage conditions of the base model.

See [`LICENSE`](https://www.apache.org/licenses/Apache-2.0) and the original
Granite model card for additional information.