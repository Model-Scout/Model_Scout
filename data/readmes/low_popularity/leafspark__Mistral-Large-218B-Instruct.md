---
license: other
license_name: mrl
license_link: https://mistral.ai/licenses/MRL-0.1.md
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
pipeline_tag: text-generation
---

# Mistral-Large-218B-Instruct

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6604e5b21eb292d6df393365/P-BGJ5Ba2d1NkpdGXNThe.png)

Mistral-Large-218B-Instruct is a dense Large Language Model (LLM) with 218 billion parameters. Self-merged from the original Mistral Large 2.

## Key features
- 218 billion parameters
- Multi-lingual support for dozens of languages
- Trained on 80+ coding languages
- 128k context window
- Mistral Research License: Allows usage and modification for research and non-commercial purposes

## Hardware Requirements

Given the size of this model (218B parameters), it requires substantial computational resources for inference:
- Recommended: 8xH100 (640GB)
- Alternatively: Distributed inference setup across multiple machines

## Limitations

- No built-in moderation mechanisms
- Computationally expensive inference
- May exhibit biases present in training data
- Outputs should be critically evaluated for sensitive applications

## Notes

This was just a fun testing model, merged with the `merge.py` script in the base of the repo. 

## Quants

GGUF: [mradermacher/Mistral-Large-218B-Instruct-GGUF](https://huggingface.co/mradermacher/Mistral-Large-218B-Instruct-GGUF)

imatrix GGUF: [mradermacher/Mistral-Large-218B-Instruct-i1-GGUF](https://huggingface.co/mradermacher/Mistral-Large-218B-Instruct-i1-GGUF)

Compatible `mergekit` config:
```yaml
slices:
- sources:
  - layer_range: [0, 20]
    model: mistralai/Mistral-Large-Instruct-2407
- sources:
  - layer_range: [10, 30]
    model: mistralai/Mistral-Large-Instruct-2407
- sources:
  - layer_range: [20, 40]
    model: mistralai/Mistral-Large-Instruct-2407
- sources:
  - layer_range: [30, 50]
    model: mistralai/Mistral-Large-Instruct-2407
- sources:
  - layer_range: [40, 60]
    model: mistralai/Mistral-Large-Instruct-2407
- sources:
  - layer_range: [50, 70]
    model: mistralai/Mistral-Large-Instruct-2407
- sources:
  - layer_range: [60, 80]
    model: mistralai/Mistral-Large-Instruct-2407
- sources:
  - layer_range: [70, 87]
    model: mistralai/Mistral-Large-Instruct-2407
merge_method: passthrough
dtype: bfloat16
```