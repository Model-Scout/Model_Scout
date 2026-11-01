---
language:
  - en
  - fr
  - de
  - es
  - it
  - pt
  - ja
  - ko
  - zh
  - ar
  - el
  - fa
  - pl
  - id
  - cs
  - he
  - hi
  - nl
  - ro
  - ru
  - tr
  - uk
  - vi
pretty_name: "Déjà Vu: Automatic Pairwise Preference Evaluations"
tags:
- multilingual
- evaluaton
license: "cc-by-nc-sa-4.0"
task_categories:
- text-generation
- other
---

# Automatic pairwise preference evaluations for "Déjà Vu: Multilingual LLM Evaluation through the Lens of Machine Translation Evaluation"

## Content
This data contains pairwise automatic win-rate evaluations for 2 benchmarks.

1. Outputs and judge decisions for the [m-ArenaHard](https://huggingface.co/datasets/CohereLabs/m-ArenaHard) benchmark for sampled generations (5 each) from [Aya Expanse 8B](https://huggingface.co/CohereLabs/aya-expanse-8b) and [Qwen2.5 7B Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct).
2. Original and roundtrip-translated prompts (by NLLB 3.3B, Aya Expanse 32B, Google Translate, Command A), outputs and judge decisions for the [aya_human_annotated](https://huggingface.co/datasets/CohereLabs/aya_evaluation_suite/viewer/aya_human_annotated) benchmark for sampled generations (1 each) from [Aya Expanse 8B](https://huggingface.co/CohereLabs/aya-expanse-8b) and [Gemma2 9B it](https://huggingface.co/google/gemma-2-9b-it).

Model outputs are compared in pairs, and judged by GPT4o. 
For an analysis and context of these evaluations, check out the paper [Déjà Vu: Multilingual LLM Evaluation through the Lens of Machine Translation Evaluation](https://arxiv.org/abs/2504.11829).

## Format
The data is organized in a nested dictionary by language and repetition, and contains additional meta-information about the evaluation that is the same for all languages.

Below we explain the format for each file, annotations in "<>":

1. `win-rate_m-arenahard_aya-expanse-8B_qwen2.5-7B_gpt4o_5repeats.json`
```
{language: 
    {repeat_no: 
      {"prompt": <mArenaHard prompt>, 
      "CohereForAI_aya-expanse-8B": <Aya Expanse 8B generation>, 
      "Qwen_Qwen2.5-7B-Instruct": <Qwen2.5 7B Instruct generation>,
      "winner": <GPT4o winner in pairwise preference evaluation, either of the two model names>
      }
    }
  "meta_information": 
     {'judge': <LLM judge name incl. version>, 
     'judge_prompt': <LLM judge evaluation prompt template>, 
     'judge_system_prompt': <LLM judge system prompt template>, 
     'vllm_decoding_configuration': <vLLM decoding configuration>, 
     'vllm_version': <vLLM version>
     }
  }
```

2. `win-rate_roundtrip-translated_human-annotated_aya-expanse-8B_gemma2-9b-it_gpt4o.json`
```
{language:
  [{"id": id,
   "prompt": <original aya human annotated prompt>,
   "prompt_translated_<translator>": <<translator> translated prompt into the target language>,
   "prompt_pivot_<translator>": <<translator> translated prompt into the pivot language>,
   "google_gemma-2-9b-it_completion_original": <Gemma generation for the original prompt>,
   "CohereForAI_aya_expanse-8b_completion_original": <Aya Expanse generation for the original prompt>,
   "google_gemma-2-9b-it_completion_translated_<translator>": <Gemma generation for <translator> translated prompt>,
   "CohereForAI_aya_expanse-8b_completion_translated_<translator>": <Aya Expanse generation for <translator> translated prompt>,
   "original_winner": <GPT4o winner in pairwise comparisons on original prompts>,
   "translated_<translator>_winner": <GPT4o winner in pairwise comparisons on prompts of that translator>,
  }]
 "meta_information":
  {'judge': <LLM judge name incl. version>, 
     'judge_prompt': <LLM judge evaluation prompt template>, 
     'judge_system_prompt': <LLM judge system prompt template>, 
     'vllm_decoding_configuration': <vLLM decoding configuration>, 
     'vllm_version': <vLLM version>
     }
}
```

## Use
**This data may not be used for model training!**

You may use this data to conduct analyses of model differences, evaluate other judges against GPT4o, or similar inference-only experiments. 

Make sure to additionally respect the individual licenses for using outputs from Aya, Qwen, Gemma, Google Translate, NLLB, GPT4o, Command A models.

## Citation
If you use this data for your research, please cite our work accordingly:
```
@misc{kreutzer2025dejavumultilingualllm,
      title={D\'ej\`a Vu: Multilingual LLM Evaluation through the Lens of Machine Translation Evaluation}, 
      author={Julia Kreutzer and Eleftheria Briakou and Sweta Agrawal and Marzieh Fadaee and Kocmi Tom},
      year={2025},
      eprint={2504.11829},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.11829}, 
}
```

