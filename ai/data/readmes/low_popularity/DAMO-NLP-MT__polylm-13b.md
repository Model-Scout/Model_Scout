---
language: 
- zh
- en
- es
- fr
- pt
- ru
- de
- it
- ar
- ja
- ko
- th
- vi
- id
- nl
- pl
- tr
- he

tags:
- text-generation

license: apache-2.0
---

# Model Card for PolyLM (a polyglot large language model)

## Table of Contents

1. [Model Details](#model-details)
2. [Usage](#usage)
3. [Uses](#uses)
4. [Bias, Risks, and Limitations](#bias-risks-and-limitations)
5. [Next Steps](#next-steps)
6. [Citation](#citation)

# Model Details

## Abstract

>  Large language models (LLMs) demonstrate remarkable ability to comprehend, reason, and generate following nature language instructions. However, the development of LLMs has been primarily focused on high-resource languages, such as English, thereby limiting their applicability and research in other languages. Consequently, we present PolyLM, a multilingual LLM trained on 640 billion (B) tokens, avaliable in two model sizes: 1.7B and 13B. To enhance its multilingual capabilities, we 1) integrate bilingual data into training data; and 2) adopt a curriculum learning strategy that increases the proportion of non-English data from 30% in the first stage to 60% in the final stage during pre-training. Further, we propose a multilingual self-instruct method which automatically generates 132.7K  diverse multilingual instructions for model fine-tuning. To assess the model's performance, we collect several existing multilingual tasks, including multilingual understanding, question answering, generation, and translation. Extensive experiments show that PolyLM surpasses other open-source models such as LLaMA and BLOOM on multilingual tasks while maintaining comparable performance in English.

## Model Description

- **Model type:** Decoder-only Language model
- **Language(s) (NLP):** Chinese, English, Spanish, German, French, Portuguese, Russian, Italian, Arabic, Japanese, Korean, Thai, Vietnamese, Indonesian, Polish, Turkish, Dutch, Hebrew
- **License:** Apache 2.0
- **Original Checkpoints:** [Modelscope DAMO PolyLM-13B](https://www.modelscope.cn/models/damo/nlp_polylm_13b_text_generation/summary)
- **Link to paper:** [here](https://arxiv.org/pdf/2307.06018.pdf)
- **Number fotmat:** bf16
- **Total seen tokens:** 640 billion tokens
- **Version:** Version 1.0 / 12 July 2023

# Usage

Find below some example scripts on how to use the model in `transformers`:

<details>
<summary> Click to expand </summary>

```python

# pip install accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("DAMO-NLP-MT/polylm-13b", legacy=False, use_fast=False)

model = AutoModelForCausalLM.from_pretrained("DAMO-NLP-MT/polylm-13b", device_map="auto", trust_remote_code=True)
model.eval()

input_doc = f"Beijing is the capital of China.\nTranslate this sentence from English to Chinese."

inputs = tokenizer(input_doc, return_tensors="pt")

generate_ids = model.generate(
  inputs.input_ids,
  attention_mask=inputs.attention_mask,
  do_sample=False,
  num_beams=4,
  max_length=128,
  early_stopping=True
)

decoded = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

print(f">>> {decoded}")

### results
### Beijing is the capital of China.\nTranslate this sentence from English to Chinese.\\n北京是中华人民共和国的首都。\n ...

```

</details>

# Uses

## Direct Use and Downstream Use

> The primary use is research on language models, including: research on zero-shot NLP tasks and in-context few-shot learning NLP tasks, such as reasoning, and question answering; advancing fairness and safety research, and understanding limitations of current large language models

See the [research paper](https://arxiv.org/pdf/2307.06018.pdf) for further details.

## Out-of-Scope Use

More information needed.

# Bias, Risks, and Limitations

The information below in this section are copied from the model's [official model card](https://arxiv.org/pdf/2307.06018.pdf):

> Our contributions are fully methodological: adding the support of multilingualism to LLM during training and SFT phases. It is unavoidable that PolyLM might exhibit several common deficiencies of language models, e.g. hallucination and toxicity. PolyLM should not be used directly in any application, without a prior assessment of safety and fairness concerns specific to the application.


# Next Steps

We are continuously enhancing the capabilities of PolyLM by focusing on the following aspects:

1. Replacement of absolute position embeddings with RoPE, as outlined in the research paper [here](https://arxiv.org/abs/2104.09864).
2. Expansion of window size to more than 10,000.
3. Verification of lightweight techniques to quickly enhance multilingual quality, especially for low-resource languages.

# Citation

**BibTeX:**

```bibtex
@misc{wei2023polylm,
      title={PolyLM: An Open Source Polyglot Large Language Model}, 
      author={Xiangpeng Wei and Haoran Wei and Huan Lin and Tianhao Li and Pei Zhang and Xingzhang Ren and Mei Li and Yu Wan and Zhiwei Cao and Binbin Xie and Tianxiang Hu and Shangjie Li and Binyuan Hui and Bowen Yu and Dayiheng Liu and Baosong Yang and Fei Huang and Jun Xie},
      year={2023},
      eprint={2307.06018},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

