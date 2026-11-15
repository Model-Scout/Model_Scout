---
language:
- en 
- zh 
- fr
- es
- pt 
- de
- it
- ru
- ja
- ko
- vi
- th
- ar
- fa
- he
- tr
- cs
- pl
- hi
- bn
- ur
- id
- ms
- lo
- my
- ceb
- km
- tl
- nl
license: other
library_name: transformers
tags:
- mergekit
- merge
base_model:
- Qwen/Qwen2.5-72B-Instruct
- Qwen/Qwen2.5-72B
license_name: qwen
inference: true
model-index:
- name: ultiima-72B
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
      value: 71.4
      name: strict accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Sakalti/ultiima-72B
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
      value: 61.1
      name: normalized accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Sakalti/ultiima-72B
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
      value: 52.42
      name: exact match
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Sakalti/ultiima-72B
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
      value: 21.92
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Sakalti/ultiima-72B
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
      value: 18.12
      name: acc_norm
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Sakalti/ultiima-72B
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
      value: 54.51
      name: accuracy
    source:
      url: https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=Sakalti/ultiima-72B
      name: Open LLM Leaderboard
---
Built With Qwen
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [TIES](https://arxiv.org/abs/2306.01708) merge method using [Qwen/Qwen2.5-72B](https://huggingface.co/Qwen/Qwen2.5-72B) as a base.

### Models Merged

The following models were included in the merge:
* [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
models:
  - model: Qwen/Qwen2.5-72B-Instruct
    parameters:
      weight: 1
      density: 1
merge_method: ties
base_model: Qwen/Qwen2.5-72B
parameters:
  weight: 1
  density: 1
  normalize: true
  int8_mask: true
dtype: float16
```
# [Open LLM Leaderboard Evaluation Results](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
Detailed results can be found [here](https://huggingface.co/datasets/open-llm-leaderboard/Sakalti__ultiima-72B-details)

|      Metric       |Value|
|-------------------|----:|
|Avg.               |46.58|
|IFEval (0-Shot)    |71.40|
|BBH (3-Shot)       |61.10|
|MATH Lvl 5 (4-Shot)|52.42|
|GPQA (0-shot)      |21.92|
|MuSR (0-shot)      |18.12|
|MMLU-PRO (5-shot)  |54.51|

