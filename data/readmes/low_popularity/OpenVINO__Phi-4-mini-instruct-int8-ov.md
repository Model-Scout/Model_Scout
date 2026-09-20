---
language:
- multilingual
- ar
- zh
- cs
- da
- nl
- en
- fi
- fr
- de
- he
- hu
- it
- ja
- ko
- 'no'
- pl
- pt
- ru
- es
- sv
- th
- tr
- uk
license: mit
license_link: https://huggingface.co/microsoft/Phi-4-mini-instruct/resolve/main/LICENSE
pipeline_tag: text-generation
tags:
- nlp
- code
base_model: microsoft/Phi-4-mini-instruct
base_model_relation: quantized

---
# Phi-4-mini-instruct-int8-ov
* Model creator: [Microsoft](https://huggingface.co/microsoft)
* Original model: [Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct)

## Description

This is [Phi-4-mini-instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) model converted to the [OpenVINO™ IR](https://docs.openvino.ai/2025/documentation/openvino-ir-format.html) (Intermediate Representation) format with weights compressed to INT8 by [NNCF](https://github.com/openvinotoolkit/nncf).

## Quantization Parameters

Weight compression was performed using `nncf.compress_weights` with the following parameters:

* mode: **INT8_ASYM**

For more information on quantization, check the [OpenVINO model optimization guide](https://docs.openvino.ai/2025/openvino-workflow/model-optimization-guide/weight-compression.html)

## Compatibility
The provided OpenVINO™ IR model is compatible with:
* OpenVINO version 2025.1.0 and higher
* Optimum Intel 1.22.0 and higher

## Running Model Inference with [Optimum Intel](https://huggingface.co/docs/optimum/intel/index)

1. Install packages required for using [Optimum Intel](https://huggingface.co/docs/optimum/intel/index) integration with the OpenVINO backend:
```
pip install optimum[openvino]
```

2. Run model inference:
```
from transformers import AutoTokenizer
from optimum.intel.openvino import OVModelForCausalLM
model_id = "OpenVINO/Phi-4-mini-instruct-int8-ov"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = OVModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)

inputs = tokenizer("What is OpenVINO?", return_tensors="pt")
outputs = model.generate(**inputs, max_length=200)
text = tokenizer.batch_decode(outputs)[0]
print(text)
```
For more examples and possible optimizations, refer to [the Inference with Optimum Intel](https://docs.openvino.ai/2025/openvino-workflow-generative/inference-with-optimum-intel.html).

## Running Model Inference with [OpenVINO GenAI](https://github.com/openvinotoolkit/openvino.genai)

1. Install packages required for using OpenVINO GenAI.
```
pip install -U openvino openvino-tokenizers openvino-genai
pip install huggingface_hub
```

2. Download model from HuggingFace Hub
   
```
import huggingface_hub as hf_hub
model_id = "OpenVINO/Phi-4-mini-instruct-int8-ov"
model_path = "Phi-4-mini-instruct-int8-ov"
hf_hub.snapshot_download(model_id, local_dir=model_path)
```

3. Run model inference:
```
import openvino_genai as ov_genai
device = "CPU"
pipe = ov_genai.LLMPipeline(model_path, device)
print(pipe.generate("What is OpenVINO?", max_length=200))
```
More GenAI usage examples can be found in OpenVINO GenAI library [docs](https://docs.openvino.ai/2025/openvino-workflow-generative/inference-with-genai.html) and [samples](https://github.com/openvinotoolkit/openvino.genai?tab=readme-ov-file#openvino-genai-samples)

You can find more detaild usage examples in OpenVINO Notebooks:

- [LLM](https://openvinotoolkit.github.io/openvino_notebooks/?search=LLM)
- [RAG text generation](https://openvinotoolkit.github.io/openvino_notebooks/?search=RAG+system&tasks=Text+Generation)

## Limitations
Check the original model card for [original model card](ttps://huggingface.co/microsoft/Phi-4-mini-instruct) for limitations.

## Legal information
The original model is distributed under [mit](https://huggingface.co/microsoft/Phi-4-mini-instruct/resolve/main/LICENSE) license. More details can be found in [original model card](ttps://huggingface.co/microsoft/Phi-4-mini-instruct).

## Disclaimer
Intel is committed to respecting human rights and avoiding causing or contributing to adverse impacts on human rights. See [Intel’s Global Human Rights Principles](https://www.intel.com/content/dam/www/central-libraries/us/en/documents/policy-human-rights.pdf). Intel’s products and software are intended only to be used in applications that do not cause or contribute to adverse impacts on human rights.