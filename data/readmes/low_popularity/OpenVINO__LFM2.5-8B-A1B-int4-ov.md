---
license: other
license_name: lfm1.0
license_link: https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE
base_model:
  - LiquidAI/LFM2.5-8B-A1B
base_model_relation: quantized
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- moe
library_name: openvino
---

# LFM2.5-8B-A1B-int4-ov

* Model creator: [LiquidAI](https://huggingface.co/LiquidAI)
* Original model: [LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B)

> [!WARNING]
> **Disclaimer**: This model is provided for evaluation purposes only. Performance, accuracy, and stability may vary. Use at your own discretion.

## Description

This is [LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) model converted to the [OpenVINO™ IR](https://docs.openvino.ai/2026/documentation/openvino-ir-format.html) (Intermediate Representation) format with weights compressed to INT4 by [NNCF](https://github.com/openvinotoolkit/nncf).

## Quantization Parameters

Weight compression was performed using `nncf.compress_weights` with the following parameters:

* mode: **INT4_ASYM**
* group_size: **128**
* ratio: **1.0**

For more information on quantization, check the [OpenVINO model optimization guide](https://docs.openvino.ai/2026/openvino-workflow/model-optimization-guide/weight-compression.html).

## Compatibility

The provided OpenVINO™ IR model is compatible with:

* OpenVINO version 2026.3.0 and higher
* Optimum Intel 1.27.0 and higher

## Running Model Inference with [Optimum Intel](https://huggingface.co/docs/optimum/intel/index)

1. Install packages required for using [Optimum Intel](https://huggingface.co/docs/optimum/intel/index) integration with the OpenVINO backend:

```
pip install -U "git+https://github.com/huggingface/optimum-intel.git"
```

As OpenVINO 2026.3.0 is not released yet, install the pre-release (nightly) build of OpenVINO to run this model:

```
pip install --pre -U openvino --extra-index-url https://storage.openvinotoolkit.org/simple/wheels/nightly
```

2. Run model inference:

```python
from transformers import AutoTokenizer
from optimum.intel.openvino import OVModelForCausalLM

model_id = "OpenVINO/LFM2.5-8B-A1B-int4-ov"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = OVModelForCausalLM.from_pretrained(model_id)

inputs = tokenizer("What is a capital of France?", return_tensors="pt")

outputs = model.generate(**inputs, max_length=200)
text = tokenizer.batch_decode(outputs)[0]
print(text)
```

For more examples and possible optimizations, refer to the [Inference with Optimum Intel](https://docs.openvino.ai/2026/openvino-workflow-generative/inference-with-optimum-intel.html).

## Running Model Inference with [OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai)

1. Install packages required for using OpenVINO GenAI.

```
pip install huggingface_hub
pip install --pre -U openvino openvino-tokenizers openvino-genai --extra-index-url https://storage.openvinotoolkit.org/simple/wheels/nightly
```

2. Download model from HuggingFace Hub

```python
import huggingface_hub as hf_hub

model_id = "OpenVINO/LFM2.5-8B-A1B-int4-ov"
model_path = "LFM2.5-8B-A1B-int4-ov"

hf_hub.snapshot_download(model_id, local_dir=model_path)
```

3. Run model inference:

```python
import openvino_genai as ov_genai

device = "CPU"
pipeline_config = {"ATTENTION_BACKEND": "SDPA"}
pipe = ov_genai.LLMPipeline(model_path, device, **pipeline_config)
pipe.get_tokenizer().set_chat_template(pipe.get_tokenizer().chat_template)
print(pipe.generate("What is a capital of France?", max_length=200))
```

More GenAI usage examples can be found in OpenVINO GenAI library [docs](https://docs.openvino.ai/2026/openvino-workflow-generative/inference-with-genai.html) and [samples](https://github.com/openvinotoolkit/openvino.genai?tab=readme-ov-file#openvino-genai-samples)

You can find more detailed usage examples in OpenVINO Notebooks:

- [LLM](https://openvinotoolkit.github.io/openvino_notebooks/?search=LLM)
- [RAG text generation](https://openvinotoolkit.github.io/openvino_notebooks/?search=RAG+system&tasks=Text+Generation)

## Limitations

Check the original [model card](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B) for limitations.

## Legal information

The original model is distributed under [lfm1.0](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B/blob/main/LICENSE) license. More details can be found in [LFM2.5-8B-A1B](https://huggingface.co/LiquidAI/LFM2.5-8B-A1B).

## Disclaimer

Intel is committed to respecting human rights and avoiding causing or
contributing to adverse impacts on human rights. See
[Intel's Global Human Rights Principles](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/policy-human-rights.pdf).
Intel's products and software are intended only to be used in applications
that do not cause or contribute to adverse impacts on human rights.

