---
license: apache-2.0
task_categories:
- question-answering
- text-generation
language:
- ko
tags:
- medical
- biology
dataset_info:
  features:
  - name: Question
    dtype: string
  - name: Complex_Cot
    dtype: string
  - name: Response
    dtype: string
  splits:
  - name: train
    num_bytes: 88925555
    num_examples: 25682
  download_size: 47190422
  dataset_size: 88925555
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

## Introduction
The original data was used to fine-tune HuatuoGPT-o1, a medical LLM designed for advanced medical reasoning. Original dataset was constructed using GPT-4o, which searches for solutions to [verifiable medical problems](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-verifiable-problem) and validates them through a medical verifier. 


For details, see their [paper](https://arxiv.org/pdf/2412.18925) and [GitHub repository](https://github.com/FreedomIntelligence/HuatuoGPT-o1).

## Translation

For translation into Korean, I used *gemini-2.0-flash-exp* model w/ temperature=0.5 setting.

### Prompt
>You are a highly skilled translator specializing in medical and healthcare documents.
>Your task is to translate the following three categories (Question, Reasoning, Final_answer) into Korean with utmost accuracy.
>Each category may consist of multiple sentences.
>Ensure the translation preserves the technical and domain-specific terminology.
>For medical terms, translate them into Korean (if possible) and include the original English term in parentheses.
>The translation must be natural and fluent, avoiding any signs of 'translationese' or awkward phrasing.
>Output with formal and polite language, suitable for professional communication.
>Use appropriate formal sentence endings such as "-입니다".
>Provide the Korean translation for each category between the designated special tokens as shown below.
>
>Question - between [KorQ] and [/KorQ]
>
>Reasoning - between [KorR] and [/KorR]
>
>Final_answer - between [KorF] and [/KorF]
>
>SENTENCES:
>
>[QUESTION] {QUESTION} [/QUESTION]
>
>[REASONING] {REASONING} [/REASONING]
>
>[FINAL_ANSWER] {FINAL_ANSWER} [/FINAL_ANSWER]
>



## Citation

```
@misc{chen2024huatuogpto1medicalcomplexreasoning,
      title={HuatuoGPT-o1, Towards Medical Complex Reasoning with LLMs}, 
      author={Junying Chen and Zhenyang Cai and Ke Ji and Xidong Wang and Wanlong Liu and Rongsheng Wang and Jianye Hou and Benyou Wang},
      year={2024},
      eprint={2412.18925},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.18925}, 
}
```
