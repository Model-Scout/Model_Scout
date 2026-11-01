---
language:
- de
- es
- it
- fr
- ja
- zh
license:
- cc-by-4.0
- cc-by-sa-4.0
task_categories:
- text-generation
configs:
- config_name: default
  data_files:
  - split: code_de
    path: data/super-v3_code_de_translated_final.jsonl
  - split: code_es
    path: data/super-v3_code_es_translated_final.jsonl
  - split: code_fr
    path: data/super-v3_code_fr_translated_final.jsonl
  - split: code_it
    path: data/super-v3_code_it_translated_final.jsonl
  - split: code_ja
    path: data/super-v3_code_ja_translated_final.jsonl
  - split: code_zh
    path: data/super-v3_code_zh_translated_final.jsonl
  - split: math_de
    path: data/super-v3_math_de_translated_final.jsonl
  - split: math_es
    path: data/super-v3_math_es_translated_final.jsonl
  - split: math_fr
    path: data/super-v3_math_fr_translated_final.jsonl
  - split: math_it
    path: data/super-v3_math_it_translated_final.jsonl
  - split: math_ja
    path: data/super-v3_math_ja_translated_final.jsonl
  - split: math_zh
    path: data/super-v3_math_zh_translated_final.jsonl
  - split: stem_de
    path: data/super-v3_stem_de_translated_postedit_final.jsonl
  - split: stem_es
    path: data/super-v3_stem_es_translated_postedit_final.jsonl
  - split: stem_fr
    path: data/super-v3_stem_fr_translated_postedit_final.jsonl
  - split: stem_it
    path: data/super-v3_stem_it_translated_postedit_final.jsonl
  - split: stem_ja
    path: data/super-v3_stem_ja_translated_postedit_final.jsonl
  - split: stem_zh
    path: data/super-v3_stem_zh_translated_postedit_final.jsonl
---

## Dataset Description:

Nemotron-Multilingual-v1 is a multilingual reasoning dataset made by translating a subsample of SFT data from [Nemotron-Math-v2](https://huggingface.co/datasets/nvidia/Nemotron-Math-v2), [Nemotron-Competitive-Programming-v1](https://huggingface.co/datasets/nvidia/Nemotron-Competitive-Programming-v1), and [Nemotron-Science-v1](https://huggingface.co/datasets/nvidia/Nemotron-Science-v1) into to 6 languages (German, French, Japanese, German, Italian, Japanese, Chinese).  
The original datasets were translated with [Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct), then filtered with heuristics to remove translation failures and hallucinations. The STEM subsets are further post-edited with an LLM [Qwen3-4B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507) to fix format mismatching problems.    
We provide the prompt and the final answer in the target language, while the reasoning trace is kept in English. This is due to architectural decisions for Nemotron 3 series.

For details of dataset in each domain, please refer to the original data cards mentioned before.

This dataset is ready for commercial use.

## Dataset Owner(s):
NVIDIA Corporation

## Dataset Creation Date:
Created on: Jan 28, 2026
Last Modified on: Jan 28, 2026


## License/Terms of Use: 
This dataset is governed by the Creative Commons Attribution 4.0 International License (CC BY 4.0), except for the StackOverflow and MathGenSelect data, which is governed by the Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)

## Intended Usage:

This dataset is intended for post-training large language models with multilingual capabilities, with a special focus on improving model's capability of handling STEM, math and coding applications under multilingual setup.  

Because all the examples are translated from English-sourced datasets, it is not intended to instill local or regional knowledge specific to where a specific language is spoken.

## Dataset Characterization
**Data Collection Method**  
* [Hybrid]

**Labeling Method**
* [Synthetic]  
  

## Dataset Format
Modality: Text  
Format: JSONL  
Structure: Text + Metadata

## Dataset Quantification
The samples below represent the number of Q&A prompts, along with the reasoning trace in English.

| Subset | Samples |
|--------|---------|
| code_de | 133322 |
| code_es | 131578 |
| code_fr | 136045 |
| code_it | 143122 |
| code_ja | 126393 |
| code_zh | 154653 |
| math_de | 128846 |
| math_es | 102866 |
| math_fr | 115916 |
| math_it | 130388 |
| math_ja | 101820 |
| math_zh | 88594 |
| stem_de | 261205 |
| stem_es | 262353 |
| stem_fr | 264221 |
| stem_it | 269240 |
| stem_ja | 256624 |
| stem_zh | 258069 |
| Total | 3065255 |

Measurement of Total Data Storage: ~90GB

## Reference(s):

You can find our recipe for translation [here](https://github.com/NVIDIA-NeMo/Skills/tree/main/recipes/translation).

## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  
Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/)

