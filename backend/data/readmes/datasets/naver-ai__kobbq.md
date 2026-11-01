---
license: mit
task_categories:
- question-answering
- zero-shot-classification
language:
- ko
pretty_name: kobbq
size_categories:
- 10K<n<100K
---
# Dataset Card for KoBBQ

<!-- Provide a quick summary of the dataset. -->

<img src="https://cdn-uploads.huggingface.co/production/uploads/65294f43375b3a8bc1351acd/2qGw9EUpLnIsl-1MN7iwR.jpeg" width="70%" height="70%">

The Bias Benchmark for Question Answering (BBQ) is designed to evaluate social biases of language models (LMs), but it is not simple to adapt this benchmark to cultural contexts other than the US because social biases depend heavily on the cultural context. In this paper, we present **KoBBQ, a Korean bias benchmark dataset**, and we propose a general framework that addresses considerations for cultural adaptation of a dataset. Our framework includes partitioning the BBQ dataset into three classes--Simply-Transferred (can be used directly after cultural translation), Target-Modified (requires localization in target groups), and Sample-Removed (does not fit Korean culture)-- and adding four new categories of bias specific to Korean culture. We conduct a large-scale survey to collect and validate the social biases and the targets of the biases that reflect the stereotypes in Korean culture. The resulting **KoBBQ dataset comprises 268 templates and 76,048 samples across 12 categories of social bias**. We use KoBBQ to measure the accuracy and bias scores of several state-of-the-art multilingual LMs. The results clearly show differences in the bias of LMs as measured by KoBBQ and a machine-translated version of BBQ, demonstrating the need for and utility of a well-constructed, culturally-aware social bias benchmark.


## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->

<img src="https://cdn-uploads.huggingface.co/production/uploads/65294f43375b3a8bc1351acd/lS99Cz_5iroZQkDtJEGpK.png" width="70%" height="70%">

We propose a framework for developing culturally adaptive datasets and present KoBBQ that reflects the situations and social biases in South Korea. The dataset curation process consists of the following steps: (1) categorization of BBQ templates, (2) cultural-sensitive translation, (3) demographic category construction, (4) creation of new templates, and (5) a large-scale survey on social bias.

### Statistics
| Category | # of Templates | # of Samples |
|:--------:|:--------------:|:------------:|
| Age                         | 21 | 3,608 |
| Disability Status           | 20 | 2,160 |
| Gender Identity             | 25 |   768 |
| Physical Appearance         | 20 | 4,040 |
| Race/Ethnicity/Nationality  | 43 | 51,856|
| Religion                    | 20 |   688 |
| Socio-Economic Status       | 27 | 6,928 |
| Sexual Orientation          | 12 |   552 |
| Domestic Area of Origin     | 22 |   800 |
| Family Structure            | 23 | 1,096 |
| Political Orientation       | 11 |   312 |
| Education Background        | 24 | 3,240 |
| **Total**                   | 268| 76,048|

### Dataset Sources

<!-- Provide the basic links for the dataset. -->

- **Repository:** [github](https://github.com/naver-ai/KoBBQ/)
- **Paper:** [arxiv](https://arxiv.org/abs/2307.16778)
- **Project Page:** [webpage](https://jinjh0123.github.io/KoBBQ/)

## Uses

<!-- Address questions around how the dataset is intended to be used. -->

### Direct Use

<!-- This section describes suitable use cases for the dataset. -->

To evaluate language models using KoBBQ, please refer [here](https://github.com/naver-ai/KoBBQ/tree/main?tab=readme-ov-file#how-to-evaluate)

### Ethical Considerations

We do not condone any malicious use of our dataset. It must not be used as training data to automatically generate and publish biased languages targeting specific groups. We strongly encourage researchers and practitioners to utilize this dataset in beneficial ways, such as mitigating bias in language models.

## Citation

**BibTeX:**
```
@article{jin2023kobbq,
  title={Kobbq: Korean bias benchmark for question answering},
  author={Jin, Jiho and Kim, Jiseon and Lee, Nayeon and Yoo, Haneul and Oh, Alice and Lee, Hwaran},
  journal={arXiv preprint arXiv:2307.16778},
  year={2023}
}
```

**APA:**
```
Jin, J., Kim, J., Lee, N., Yoo, H., Oh, A., & Lee, H. (2023). Kobbq: Korean bias benchmark for question answering. arXiv preprint arXiv:2307.16778.
```
