---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- en
- de
- es
- fr
- ja
- pt
- ar
- cs
- it
- ko
- nl
- zh
tags:
- granite
- granite-4.2
- reasoning
- thinking
- tool-calling
- ibm
- openvino
- openvino-export
base_model: ibm-granite/granite-4.2-3b
---

This model was converted to OpenVINO from [`ibm-granite/granite-4.2-3b`](https://huggingface.co/ibm-granite/granite-4.2-3b) using [optimum-intel](https://github.com/huggingface/optimum-intel)
via the [export](https://huggingface.co/spaces/echarlaix/openvino-export) space.

First make sure you have optimum-intel installed:

```bash
pip install optimum-intel
```

To load your model you can do as follows:

```python
from optimum.intel import OVModelForCausalLM

model_id = "madiaxa/granite-4.2-3b-openvino"
model = OVModelForCausalLM.from_pretrained(model_id)
```
