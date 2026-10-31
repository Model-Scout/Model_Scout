---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: original_response
    dtype: string
  - name: Qwen/Qwen2.5-1.5B-Instruct_response
    dtype: string
  - name: Qwen/Qwen2.5-7B-Instruct_response
    dtype: string
  - name: google/gemma-2-2b-it_response
    dtype: string
  - name: google/gemma-2-9b-it_response
    dtype: string
  splits:
  - name: train
    num_bytes: 846093226
    num_examples: 86007
  download_size: 375880264
  dataset_size: 846093226
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
task_categories:
- question-answering
language:
- ko
tags:
- finance
---

**🇺🇸 English** | [🇰🇷 한국어](https://huggingface.co/datasets/KRX-Data/Won-Instruct/blob/main/KOREAN_README.md)

## Introduction

The ₩ON-Instruct is a comprehensive instruction-following dataset tailored for training Korean language models specialized in financial reasoning and domain-specific financial tasks. 
This dataset was meticulously assembled through rigorous filtering and quality assurance processes, aiming to enhance the reasoning abilities of large language models (LLMs) within the financial domain, specifically tuned for Korean financial tasks.
The dataset comprises approximately 80k high-quality instruction-response instances, intentionally designed to advance the capability of language models in addressing complex financial reasoning scenarios and providing robust, accurate, and context-aware financial information.

## Dataset Details

The ₩ON-Instruct comprises the following columns:
- `prompt`: The questions converted into MCQA or Instruction-Response format using `gpt-4o` and `Qwen2.5-72B-Instruct`, based on raw data collected from various sources mentioned in the next section.
- `original_response`: The original response collected from original dataset.
- `Qwen/Qwen2.5-1.5B-Instruct_response`: Regenerated response from `Qwen2.5-1.5B-Instruct`.
- `Qwen/Qwen2.5-7B-Instruct_response`: Regenerated response from `Qwen2.5-7B-Instruct`.
- `google/gemma-2-2b-it_response`: Regenerated response from `gemma-2-2b-it`.
- `google/gemma-2-9b-it_response`: Regenerated response from `gemma-2-9b-it`.

The average length of questions and responses of samples in ₩ON-Instruct dataset.

<div style="text-align: center;">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/63e087b6a98d931aa90c1b9c/kwNz-jJ3yDQ75aw2lukpv.png" alt="설명" width="1000" height="700" style="display: block; margin: 0 auto;" />
  <div style="font-style: italic; margin-top: 8px;">Statistics of prompt and response length in ₩ON-Instruct</div>
</div>

## Dataset Collection

The construction of the ₩ON-Instruct involved a multi-phase, systematic process:

1. **Initial collection**: Over 200k data samples were collected from various sources. These sources primarily included publicly accessible and license-free financial content from reliable Korean financial, regulatory, and educational domains, such as Korea Exchange (KRX), Financial Services Commission, and Bank of Korea, among others. 
2. **Processing**: The collected raw corpus underwent transformation into structured multiple-choice questions and answers (MCQA) or Instruction-Response formats utilizing advanced generative language models, notably GPT-4o and Qwen2.5-72B-Instruct. This transformation included human-in-the-loop validation, where an LLM-as-a-Judge mechanism was employed to ensure factual accuracy, coherence, and reliability of the generated questions and instructions.
3. **Quality filtering**: To ensure the quality of the dataset, we have conducted the following stringent quality filtering:
   - MinHash algorithm: Eliminate near-duplicate entries.
   - Regex filter: Exclude time-bound queries.
   - Rule-based filter: Remove incomplete or overly brief questions.

The resulting dataset comprises a refined and curated set of 86,007 instances. 
Each instance in the dataset was subjected to further validation by utilizing GPT-4o, ensuring the correctness and coherence of the provided solutions.
In addition, the filtered data was complemented by responses generated through Deepseek-R1, an advanced reasoning language model, emphasizing structured logical reasoning processes. 
This final augmentation phase produced a dataset highly suitable for sophisticated reasoning tasks, offering clear, structured prompts and corresponding reasoned solutions.

The sources of ₩ON-Instruct is the following table:

| Link             | Name                                                        |
|------------------|-------------------------------------------------------------|
| [krx.co.kr](krx.co.kr)        | Korea Exchange                                              |
| [krxverse.co.kr](krxverse.co.kr)   | KRXverse                                                    |
| [fsc.go.kr](fsc.go.kr)        | Financial Services Commission                               |
| [bok.or.kr](bok.or.kr)        | Bank of Korea                                               |
| [law.go.kr](law.go.kr)        | Korean Law Information Service                              |
| [kasb.or.kr](kasb.or.kr)       | Korea Accounting Standards Board                            |
| [mss.go.kr](mss.go.kr)        | Ministry of SMEs and Startups                               |
| [ftc.go.kr](ftc.go.kr)        | Fair Trade Commission                                       |
| [kifrs.com](kifrs.com)        | K-IFRS                                                      |
| [kiep.go.kr](kiep.go.kr)       | Korea Institute for International Economic Policy           |
| [kocw.net](kocw.net)         | Korea OpenCourseWare                                        |


## Quick Start

```python
from datasets import load_dataset

df = load_dataset("KRX-Data/Won-Instruct")
```

## Citation

```
@article{son2025won,
  title={Won: Establishing Best Practices for Korean Financial NLP},
  author={Son, Guijin and Ko, Hyunwoo and Jung, Haneral and Hwang, Chami},
  journal={arXiv preprint arXiv:2503.17963},
  year={2025}
}
```

## Contact

```
spthsrbwls123@yonsei.ac.kr, hcharm2ing@krx.co.kr
```