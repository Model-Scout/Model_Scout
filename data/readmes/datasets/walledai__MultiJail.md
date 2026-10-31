---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: harms
    sequence: string
  - name: source
    dtype: string
  splits:
  - name: ar
    num_bytes: 55482
    num_examples: 315
  - name: zh
    num_bytes: 40311
    num_examples: 315
  - name: sw
    num_bytes: 43565
    num_examples: 315
  - name: ko
    num_bytes: 43804
    num_examples: 315
  - name: en
    num_bytes: 41465
    num_examples: 315
  - name: it
    num_bytes: 44543
    num_examples: 315
  - name: jv
    num_bytes: 41383
    num_examples: 315
  - name: th
    num_bytes: 81222
    num_examples: 315
  - name: vi
    num_bytes: 48708
    num_examples: 315
  - name: bn
    num_bytes: 82208
    num_examples: 315
  download_size: 212593
  dataset_size: 522691
configs:
- config_name: default
  data_files:
  - split: ar
    path: data/ar-*
  - split: zh
    path: data/zh-*
  - split: sw
    path: data/sw-*
  - split: ko
    path: data/ko-*
  - split: en
    path: data/en-*
  - split: it
    path: data/it-*
  - split: jv
    path: data/jv-*
  - split: th
    path: data/th-*
  - split: vi
    path: data/vi-*
  - split: bn
    path: data/bn-*
---

# Multilingual Jailbreak Challenges in Large Language Models

This repo contains the data for our paper ["Multilingual Jailbreak Challenges in Large Language Models"](https://arxiv.org/abs/2310.06474).
[[Github repo]](https://github.com/DAMO-NLP-SG/multilingual-safety-for-LLMs/)

## Annotation Statistics
We collected a total of 315 English unsafe prompts and annotated them into nine non-English languages. The languages were categorized based on resource availability, as shown below:

**High-resource languages:** Chinese (zh), Italian (it), Vietnamese (vi)

**Medium-resource languages:** Arabic (ar), Korean (ko), Thai (th)

**Low-resource languages:** Bengali (bn), Swahili (sw), Javanese (jv)

## Ethics Statement
Our research investigates the safety challenges of LLMs in multilingual settings. We are aware of the potential misuse of our findings and emphasize that our research is solely for academic purposes and ethical use. Misuse or harm resulting from the information in this paper is strongly discouraged. To address the identified risks and vulnerabilities, we commit to open-sourcing the data used in our study. This openness aims to facilitate vulnerability identification, encourage discussions, and foster collaborative efforts to enhance LLM safety in multilingual contexts. Furthermore, we have developed the SELF-DEFENSE framework to address multilingual jailbreak challenges in LLMs. This framework automatically generates multilingual safety training data to mitigate risks associated with unintentional and intentional jailbreak scenarios. Overall, our work not only highlights multilingual jailbreak challenges in LLMs but also paves the way for future research, collaboration, and innovation to enhance their safety.

## Citation
```
@misc{deng2023multilingual,
title={Multilingual Jailbreak Challenges in Large Language Models},
author={Yue Deng and Wenxuan Zhang and Sinno Jialin Pan and Lidong Bing},
year={2023},
eprint={2310.06474},
archivePrefix={arXiv},
primaryClass={cs.CL}
}
```