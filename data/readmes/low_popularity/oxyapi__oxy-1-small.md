---
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
license: apache-2.0
library_name: transformers
tags:
- role-play
- fine-tuned
- qwen2.5
base_model:
- Qwen/Qwen2.5-14B-Instruct
pipeline_tag: text-generation
model-index:
- name: oxy-1-small
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: IFEval (0-Shot)
      type: HuggingFaceH4/ifeval
      args:
        num_few_shot: 0
    metrics:
    - type: inst_level_strict_acc and prompt_level_strict_acc
      value: 62.45
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=oxyapi/oxy-1-small
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: BBH (3-Shot)
      type: BBH
      args:
        num_few_shot: 3
    metrics:
    - type: acc_norm
      value: 41.18
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=oxyapi/oxy-1-small
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MATH Lvl 5 (4-Shot)
      type: hendrycks/competition_math
      args:
        num_few_shot: 4
    metrics:
    - type: exact_match
      value: 18.28
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=oxyapi/oxy-1-small
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GPQA (0-shot)
      type: Idavidrein/gpqa
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 16.22
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=oxyapi/oxy-1-small
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MuSR (0-shot)
      type: TAUR-Lab/MuSR
      args:
        num_few_shot: 0
    metrics:
    - type: acc_norm
      value: 16.28
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=oxyapi/oxy-1-small
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU-PRO (5-shot)
      type: TIGER-Lab/MMLU-Pro
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 44.45
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=oxyapi/oxy-1-small
      name: Open LLM Leaderboard
---

![Oxy 1 Small](https://cdn-uploads.huggingface.co/production/uploads/64fb80c8bb362cbf2ff96c7e/tTIVIblPUbTYnlvHQQjXB.png)

## Introduction

**Oxy 1 Small** is a fine-tuned version of the [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen/Qwen2.5-14B-Instruct) language model, specialized for **role-play** scenarios. Despite its small size, it delivers impressive performance in generating engaging dialogues and interactive storytelling.

Developed by **Oxygen (oxyapi)**, with contributions from **TornadoSoftwares**, Oxy 1 Small aims to provide an accessible and efficient language model for creative and immersive role-play experiences.

## Model Details

- **Model Name**: Oxy 1 Small
- **Model ID**: [oxyapi/oxy-1-small](https://huggingface.co/oxyapi/oxy-1-small)
- **Base Model**: [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)
- **Model Type**: Chat Completions
- **Prompt Format**: ChatML
- **License**: Apache-2.0
- **Language**: English
- **Tokenizer**: [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)
- **Max Input Tokens**: 32,768
- **Max Output Tokens**: 8,192

### Features

- **Fine-tuned for Role-Play**: Specially trained to generate dynamic and contextually rich role-play dialogues.
- **Efficient**: Compact model size allows for faster inference and reduced computational resources.
- **Parameter Support**:
  - `temperature`
  - `top_p`
  - `top_k`
  - `frequency_penalty`
  - `presence_penalty`
  - `max_tokens`

### Metadata

- **Owned by**: Oxygen (oxyapi)
- **Contributors**: TornadoSoftwares
- **Description**: A Qwen/Qwen2.5-14B-Instruct fine-tune for role-play trained on custom datasets

## Usage

To utilize Oxy 1 Small for text generation in role-play scenarios, you can load the model using the Hugging Face Transformers library:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("oxyapi/oxy-1-small")
model = AutoModelForCausalLM.from_pretrained("oxyapi/oxy-1-small")

prompt = "You are a wise old wizard in a mystical land. A traveler approaches you seeking advice."
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=500)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Performance

Performance benchmarks for Oxy 1 Small are not available at this time. Future updates may include detailed evaluations on relevant datasets.

## License

This model is licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

## Citation

If you find Oxy 1 Small useful in your research or applications, please cite it as:

```
@misc{oxy1small2024,
  title={Oxy 1 Small: A Fine-Tuned Qwen2.5-14B-Instruct Model for Role-Play},
  author={Oxygen (oxyapi)},
  year={2024},
  howpublished={\url{https://huggingface.co/oxyapi/oxy-1-small}},
}
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_oxyapi__oxy-1-small)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |33.14|
|IFEval (0-Shot)    |62.45|
|BBH (3-Shot)       |41.18|
|MATH Lvl 5 (4-Shot)|18.28|
|GPQA (0-shot)      |16.22|
|MuSR (0-shot)      |16.28|
|MMLU-PRO (5-shot)  |44.45|

