---
license: apache-2.0
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
library_name: transformers
tags:
- chat
- conversational
- mergekit
- merge
- miscii
base_model:
- sthenno-com/miscii-14b-1225
- sthenno/tempesthenno-ppo-ckpt40
- Qwen/Qwen2.5-14B-Instruct
model-index:
- name: miscii-14b-0218
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
      value: 76.56
      name: strict accuracy
    source:
      url: >-
        https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=sthenno-com/miscii-14b-0218
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
      value: 50.64
      name: normalized accuracy
    source:
      url: >-
        https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=sthenno-com/miscii-14b-0218
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
      value: 51.44
      name: exact match
    source:
      url: >-
        https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=sthenno-com/miscii-14b-0218
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
      value: 17.79
      name: acc_norm
    source:
      url: >-
        https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=sthenno-com/miscii-14b-0218
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
      value: 13.21
      name: acc_norm
    source:
      url: >-
        https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=sthenno-com/miscii-14b-0218
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
      value: 47.75
      name: accuracy
    source:
      url: >-
        https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=sthenno-com/miscii-14b-0218
      name: Open LLM Leaderboard
---
# miscii-14b-0218

“I think there’s a reason I’m a shadow, but she looks like an angel.”
— **Viyella’s Memory**, excerpted from **[The Angel’s Message](http://lastlabyrinth.net/agm/)** by Laur (2018).

<p align="left">
<img src="banner@0.5x.png" alt="Banner" width="420" style="border-radius:3px;">
</p>

## Technical Specifications

**miscii-14b-0218** is a fine-tuned model based on **Qwen/Qwen2.5-14B-Instruct** ([Qwen Team, 2024](https://qwenlm.github.io/blog/qwen2.5/)).
It is developed using Arcee’s MergeKit ([Goddard et al. 2024](https://aclanthology.org/2024.emnlp-industry.36/)), employing the Model Stock merge method ([Jang, Yun, and Han 2024](https://arxiv.org/abs/2403.19522)).
The integration utilized **tempesthenno-ppo-enchanted** as the base model.

The configuration parameters for generating **miscii-14b-0218** are documented below:

```yaml
name: miscii-14b-0218
merge_method: model_stock
base_model: tempesthenno-ppo-enchanted
tokenizer:
  source: base
dtype: float32
out_dtype: bfloat16
parameters:
  int8_mask: true
  normalize: true
  rescale: false
models:
  - model: tempesthenno-sft-0218-ckpt60
  - model: tempesthenno-sft-0218-ckpt80
  - model: tempesthenno-sft-0218-stage2-ckpt40
  - model: tempesthenno-sft-0218-stage2-ckpt50
  - model: tempesthenno-sft-0218-stage2-ckpt60
```

## Citation

If you find **miscii-14b-0218** useful for your research and applications, please use the following citation formats:

**BibTeX**

```bibtex
@misc{sthenno_2025,
	author       = { Sthenno and Jiayu Wang },
	title        = { miscii-14b-0218 (Revision 6f78859) },
	year         = 2025,
	url          = { https://huggingface.co/sthenno-com/miscii-14b-0218 },
	doi          = { 10.57967/hf/7297 },
	publisher    = { Hugging Face }
}
```