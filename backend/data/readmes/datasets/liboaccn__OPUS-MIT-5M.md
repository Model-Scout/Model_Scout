---
license: apache-2.0
task_categories:
- translation
tags:
- image
- text
language:
- es
- zh
- en
- fr
- it
- hi
- ko
- ja
- pt
- th
- de
pretty_name: image translation
size_categories:
- 100M<n<1B
---

# Multilingual Image Translation Dataset： OPUS-MIT-5M
The OPUS-MIT-5M image translation dataset is constructed by randomly sampling 5M sentence pairs from the OPUS  corpus. 
![image/png](https://huggingface.co/datasets/liboaccn/OPUS-MIT-5M/resolve/main/data.png)


Figure  illustrates the distribution of image-text pairs across 20 language pairs within the OPUS-MIT-5M dataset.

A key goal in creating the OPUS-MIT-5M dataset is to ensure a balanced representation across languages to enable robust multilingual image translation. 
We endeavor to synthesize an equal number of image-text pairs for each language pair whenever possible. 
However, due to variations in the availability of parallel text data within the OPUS corpus, certain language pairs, specifically TH-ZH (Thai-Chinese) and HI-ZH (Hindi-Chinese), contain a lower number of synthesized images. 
This imbalance reflects the underlying distribution of the source data and poses a potential challenge for evaluating model performance on low-resource language pairs. 

In future work, we will explore strategies to augment these low-resource subsets and further improve the cross-linguistic generalization capabilities of the model.





### Citation Information
You can cite our paper https://huggingface.co/papers/2604.16943
```
@article{li2026mnaft,
  title={MNAFT: modality neuron-aware fine-tuning of multimodal large language models for image translation},
  author={Li, Bo and Deng, Ningyuan and Dong, Tianyu and Wang, Shaobo and Zhu, Shaolin and Wen, Lijie},
  journal={arXiv preprint arXiv:2604.16943},
  year={2026}
}


```
