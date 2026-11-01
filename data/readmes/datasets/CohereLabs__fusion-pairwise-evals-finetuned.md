---
language:
  - en
  - fr
  - de
  - es
  - ru
  - it
  - pt
  - ja
  - ko
  - zh
  - ar
pretty_name: "Fusion-of-N Automatic Pairwise Preference Evaluations (Finetuning)"
tags:
- multilingual
- evaluation
license: "cc-by-nc-sa-4.0"
task_categories:
- text-generation
---

# Automatic pairwise preference evaluations for: Making, not taking, the Best-of-N

## Content
This data contains pairwise automatic win-rate evaluations for the [m-ArenaHard-v2.0](https://huggingface.co/datasets/CohereLabs/m-ArenaHard-v2.0) benchmark and it compares 2 models against gemini-2.5-flash:

1. `Fusion`: is the 111B model finetuned on [synthetic data](https://huggingface.co/datasets/CohereLabs/fusion-synth-data-ufb) generated with Fusion from 5 teachers
2. `BoN`: is the 111B model finetuned on [synthetic data](https://huggingface.co/datasets/CohereLabs/fusion-synth-data-ufb) generated with BoN from 5 teachers

Each model’s outputs are compared in pairs with the respective Gemini output, and judged by GPT-4o. 
For an analysis and context of these evaluations, check out the [paper](https://arxiv.org/abs/2510.00931).

## Format
The data is organized in Jsonlines format where each line contains all the information for a single prompt evaluation.

Below we explain the format for a sample line, annotations in "<>":

```
{
  question_id: <the unique ID for the question in m-ArenaHard-v2.0 for the example (same across languages)>
  prompt: <text of this prompt>
  language_code: <Language code of this prompt>
  BoN: <The judge outcome for BoN finetuned model generation for this prompt. one of three values {win, loss, tie}>
  Fusion: <The judge outcome for Fusion finetuned model generation for this prompt. one of three values {win, loss, tie}>
  bon_completion: <The BoN finetuned model generation for this prompt>
  fusion_completion: <The Fusion finetuned model generation for this prompt>
  gemini_2_5_flash_completion: <Gemini-2.5-flash generation for this prompt>
  judge_model_name: <Name of the judge model used for the pairwise comparison. This is always gpt-4o-2024-05-13>
}
```

## Use
**This data may not be used for model training!**

You may use this data to conduct analyses of model differences, evaluate other judges against GPT4o, or similar inference-only experiments. 

Make sure to also respect the individual licenses for using outputs from Gemini, GPT4o, and CommandA models.

## Citation
If you use this data for your research, please cite our work accordingly:
```
@misc{khairi2025makingtakingbestn,
      title={Making, not Taking, the Best of N}, 
      author={Ammar Khairi and Daniel D'souza and Marzieh Fadaee and Julia Kreutzer},
      year={2025},
      eprint={2510.00931},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2510.00931}, 
}
```
