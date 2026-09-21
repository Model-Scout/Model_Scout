---
language:
- zh
- ja
- ko
- tw
license: apache-2.0
tags:
- moe
- merge
- mergekit
- lazymergekit
- MediaTek-Research/Breeze-7B-Instruct-v0.1
- augmxnt/shisa-7b-v1
- beomi/OPEN-SOLAR-KO-10.7B
model-index:
- name: EastAsia-4x7B-Moe-experiment
  results:
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: AI2 Reasoning Challenge (25-Shot)
      type: ai2_arc
      config: ARC-Challenge
      split: test
      args:
        num_few_shot: 25
    metrics:
    - type: acc_norm
      value: 39.51
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Heng666/EastAsia-4x7B-Moe-experiment
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: HellaSwag (10-Shot)
      type: hellaswag
      split: validation
      args:
        num_few_shot: 10
    metrics:
    - type: acc_norm
      value: 48.92
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Heng666/EastAsia-4x7B-Moe-experiment
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: MMLU (5-Shot)
      type: cais/mmlu
      config: all
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 56.2
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Heng666/EastAsia-4x7B-Moe-experiment
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: TruthfulQA (0-shot)
      type: truthful_qa
      config: multiple_choice
      split: validation
      args:
        num_few_shot: 0
    metrics:
    - type: mc2
      value: 49.83
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Heng666/EastAsia-4x7B-Moe-experiment
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: Winogrande (5-shot)
      type: winogrande
      config: winogrande_xl
      split: validation
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 58.09
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Heng666/EastAsia-4x7B-Moe-experiment
      name: Open LLM Leaderboard
  - task:
      type: text-generation
      name: Text Generation
    dataset:
      name: GSM8k (5-shot)
      type: gsm8k
      config: main
      split: test
      args:
        num_few_shot: 5
    metrics:
    - type: acc
      value: 0.15
      name: accuracy
    source:
      url: https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard?query=Heng666/EastAsia-4x7B-Moe-experiment
      name: Open LLM Leaderboard
---

# EastAsia-4x7B-Moe-experiment

EastAsia-4x7B-Moe-experiment is a Mixure of Experts (MoE) made with the following models using [LazyMergekit](https://colab.research.google.com/drive/1obulZ1ROXHjYLn6PPZJwRR6GzgQogxxb?usp=sharing):
* [MediaTek-Research/Breeze-7B-Instruct-v0.1](https://huggingface.co/MediaTek-Research/Breeze-7B-Instruct-v0.1)
* [augmxnt/shisa-7b-v1](https://huggingface.co/augmxnt/shisa-7b-v1)
* [beomi/OPEN-SOLAR-KO-10.7B](https://huggingface.co/beomi/OPEN-SOLAR-KO-10.7B)

## 🧩 Configuration

```yaml
gate_mode: hidden
dtype: bfloat16
base_model: mlabonne/Marcoro14-7B-slerp
experts:
  - source_model: MediaTek-Research/Breeze-7B-Instruct-v0.1
    positive_prompts:
    - "翻譯"
  - source_model: augmxnt/shisa-7b-v1
    positive_prompts:
    - "翻訳"
  - source_model: beomi/OPEN-SOLAR-KO-10.7B
    positive_prompts:
    - "번역"
```

## 💻 Usage

```python
!pip install -qU transformers bitsandbytes accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "Heng666/EastAsia-4x7B-Moe-experiment"

tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    model_kwargs={"torch_dtype": torch.float16, "load_in_4bit": True},
)

messages = [{"role": "user", "content": "Explain what a Mixture of Experts is in less than 100 words."}]
prompt = pipeline.tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, top_k=50, top_p=0.95)
print(outputs[0]["generated_text"])
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/details_Heng666__EastAsia-4x7B-Moe-experiment)

|             Metric              |Value|
|---------------------------------|----:|
|Avg.                             |42.12|
|AI2 Reasoning Challenge (25-Shot)|39.51|
|HellaSwag (10-Shot)              |48.92|
|MMLU (5-Shot)                    |56.20|
|TruthfulQA (0-shot)              |49.83|
|Winogrande (5-shot)              |58.09|
|GSM8k (5-shot)                   | 0.15|

