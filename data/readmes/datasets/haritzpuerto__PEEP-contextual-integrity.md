---
dataset_info:
  features:
  - name: system_prompt
    dtype: string
  - name: user_prompt
    dtype: string
  - name: query
    dtype: string
  - name: confidential_data
    dtype: string
  - name: language
    dtype: string
  splits:
  - name: test
    num_bytes: 7044344
    num_examples: 2062
  download_size: 3645438
  dataset_size: 7044344
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
language:
- en
- fr
- ts
- ar
- es
- sl
- cs
- st
- zh
- mi
- de
- nb
- hi
- pt
- tr
- ru
- pl
- it
- vi
- nl
- la
- yo
- fi
- uk
- fa
- da
- ko
- ro
- et
- id
- so
- sw
- sv
- tl
- cy
- af
- hr
- ca
license: odc-by
size_categories:
- 1K<n<10K
---

# PEEP Dataset Card


## Dataset Description

PEEP is a privacy evaluation benchmark derived from **WildChat**, a corpus of real user–chatbot conversations. Conversations are annotated with potential pieces of **confidential information** (e.g., names, locations, contact details). From this source, the dataset used in this project:

- removes instances where redacting confidential information leaves fewer than five words, and  
- removes conversations without any annotated confidential information.

This filtering results in **2,062** instances. The privacy directive for models is:

- do **not** disclose any confidential information mentioned in the user prompt in either the **reasoning trace (RT)** or the **final answer (FA)**.

PEEP is used in this repository to evaluate whether controllable reasoning models can act as “private thinkers” while still remaining useful.

## Intended Use

- Evaluate contextual privacy behavior of LRMs on realistic user-chatbot conversations.

The dataset is intended for **research on privacy and safety** in language models.

## Dataset Structure

From the accompanying paper (see `paper/`):

- **Size**: 2,062 instances.  
- **Source**: WildChat conversations with privacy annotations from Ramirez et al. (2025).

Each data point contains:

Fields used in our experiments:

- system_prompt
- user_prompt


Original fields (only for reference)

- query
- confidential_data
- language

## Languages

PEEP is **primarily English**, but also includes a wide range of other languages.

- English: 66.83%  
- French: 12.90%  
- Tsonga: 0.05%  
- Arabic: 0.92%  
- Spanish: 4.07%  
- Slovene: 0.10%  
- Czech: 0.10%  
- Sotho: 0.34%  
- Chinese: 2.57%  
- Maori: 1.12%  
- German: 2.42%  
- Bokmal: 0.44%  
- Hindi: 0.15%  
- Portuguese: 0.82%  
- Turkish: 0.15%  
- Russian: 2.62%  
- Polish: 0.63%  
- Italian: 0.48%  
- Vietnamese: 0.39%  
- Dutch: 0.68%  
- Latin: 0.15%  
- Yoruba: 0.10%  
- Finnish: 0.15%  
- Ukrainian: 0.29%  
- Persian: 0.29%  
- Danish: 0.05%  
- Korean: 0.19%  
- Romanian: 0.05%  
- Estonian: 0.10%  
- Indonesian: 0.15%  
- Somali: 0.05%  
- Swahili: 0.05%  
- Swedish: 0.19%  
- Tagalog: 0.24%  
- Welsh: 0.05%  
- Afrikaans: 0.05%  
- Croatian: 0.05%  
- Catalan: 0.05%  

## Tasks and Evaluation

### Privacy

The **privacy directive** is:

- Do **not** reveal any confidential information from the user prompt in RTs or FAs.

Metrics:

- **Confidential information leakage** is measured in both RTs and FAs.
- A **privacy score** is defined as \( \text{privacy} = 1 - \text{leak rate} \), reported for:
  - RTs,
  - FAs,
  - overall privacy.

### Utility

Utility is measured with an **LLM-as-a-judge** setup:

- GPT 5 nano rates each model response from **1 to 5** based on:
  - relevance,
  - helpfulness,
  - correctness,
  - clarity,
  - completeness,
  - safety.
- These ratings are combined into an **overall utility score**, which is used as the benchmark’s utility metric.

The prompt used for LLM-as-a-judge and a small human validation of its quality are included in the paper’s appendix.



## License

- **License**: ODC-BY

PEEP is derived from the Wildchat dataset, which is released under the Open Data Commons Attribution License (ODC-BY). Please ensure proper attribution and usage under this license.
👉 [PEEP on Hugging Face](https://huggingface.co/datasets/guillemram97/PEEP)

## Known Limitations and Considerations

- The data originates from **real user–chatbot interactions**; while prior work has deemed it safe for research, care should be taken when reusing or transforming the data.
- Utility is judged via an LLM-based evaluator; while validated by humans in a small study, the scores still inherit limitations of automatic judgments.

## Citation

If you use this dataset, please cite the original PEEP paper and this repository’s paper:

```bibtex
@misc{ramírez2025controllingshareassessinglanguage,
      title={Controlling What You Share: Assessing Language Model Adherence to Privacy Preferences}, 
      author={Guillem Ramírez and Alexandra Birch and Ivan Titov},
      year={2025},
      eprint={2507.05391},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2507.05391}, 
}

@misc{puerto2026leakythoughtsprivatereasoning,
      title={From Leaky Thoughts to Private Reasoning: Controlling What LRMs Say to Themselves}, 
      author={Haritz Puerto and Haonan Li and Xudong Han and Timothy Baldwin and Iryna Gurevych},
      year={2026},
      eprint={2602.24210},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.24210}, 
}
```