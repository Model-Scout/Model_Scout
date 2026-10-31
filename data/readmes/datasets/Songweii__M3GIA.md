---
license: apache-2.0
language:
- en
- zh
- es
- fr
- pt
- ko
tags:
- Multilingual
- Multimodal
- Cognitive Science
- General Intelligence Ability Benchmark
pretty_name: M3GIA
size_categories:
- 1K<n<10K
configs:
- config_name: chinese
  data_files:
  - split: test
    path: chinese_v1.parquet
- config_name: english
  data_files:
  - split: test
    path: english_v1.parquet
- config_name: spanish
  data_files:
  - split: test
    path: spanish_v1.parquet
- config_name: french
  data_files:
  - split: test
    path: french_v1.parquet
- config_name: portuguese
  data_files:
  - split: test
    path: portuguese_v1.parquet
- config_name: korean
  data_files:
  - split: test
    path: korean_v1.parquet
---

# M3GIA: A Cognition Inspired Multilingual and Multimodal General Intelligence Ability 

[**🌐 Homepage**] | [**🤗 Dataset**](https://huggingface.co/datasets/Songweii/M3GIA/) | [**🤗 Paper**](https://arxiv.org/abs/2406.05343) | [**📖 arXiv**](https://arxiv.org/abs/2406.05343) | [**💻 GitHub**](https://github.com/songweii/M3GIA/tree/main)

The evaluation code can be found in [**💻 GitHub**](https://github.com/songweii/M3GIA/tree/main).

[**Abstract**]

As recent multi-modality large language models (MLLMs) have shown formidable proficiency on various complex tasks, there has been increasing attention on debating whether these models could eventually mirror human intelligence. However, existing benchmarks mainly focus on evaluating solely on task performance, such as the accuracy of identifying the attribute of an object. Combining well-developed cognitive science to understand the intelligence of MLLMs beyond superficial achievements remains largely unexplored. To this end, we introduce the first cognitive-driven multi-lingual and multi-modal benchmark to evaluate the general intelligence ability of MLLMs, dubbed M3GIA. Specifically, we identify five key cognitive factors based on the well-recognized Cattell-Horn-Carrol (CHC) model of intelligence and propose a novel evaluation metric. In addition, since most MLLMs are trained to perform on different languages, a nature question arises, is language a key factor to influence the cognitive ability of MLLMs? As such, we go beyond English to encompass other languages based on their popularity, including Chinese, French, Spanish, Portuguese and Korean, to construct our M3GIA. We make sure all the data relevant to the cultural backgrounds are collected from their native context to avoid English-centric bias. We collected a significant corpus of data from human participants, revealing that the most advanced MLLM reaches the lower boundary of human intelligence in English. Yet, there remains a pronounced disparity in the other five languages assessed. We also reveals an interesting 'winner takes all' phenomenon that are aligned with the discovery in cognitive studies. Our benchmark will be open-sourced, with the aspiration that it will facilitate the enhancement of cognitive capabilities in MLLMs.
