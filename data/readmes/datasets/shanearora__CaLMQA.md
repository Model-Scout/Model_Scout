---
language:
- aa
- ar
- bal
- de
- en
- es
- fj
- fo
- he
- hi
- hil
- hu
- ja
- ko
- ru
- rn
- pap
- ps
- sm
- to
- tn
- wo
- zh
license: mit
multilinguality:
- multilingual
dataset_info:
  features:
  - name: language
    dtype:
      class_label:
        names:
          '0': Afar
          '1': Arabic
          '2': Balochi
          '3': Chinese
          '4': English
          '5': Faroese
          '6': Fijian
          '7': German
          '8': Hebrew
          '9': Hiligaynon
          '10': Hindi
          '11': Hungarian
          '12': Japanese
          '13': Kirundi
          '14': Korean
          '15': Papiamento
          '16': Pashto
          '17': Russian
          '18': Samoan
          '19': Spanish
          '20': Tongan
          '21': Tswana
          '22': Wolof
  - name: question
    dtype: string
  - name: question_english
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: train
    num_bytes: 14403082
    num_examples: 38641
  download_size: 7840958
  dataset_size: 14403082
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
size_categories:
- 10K<n<100K
---

# Dataset Summary

<!-- Provide a quick summary of the dataset. -->

CaLMQA is a translation-free long-form question answering (LFQA) dataset spanning 23 high- to low-resource languages. 


## Dataset Details

### Dataset Description

CaLMQA is a translation-free LFQA dataset with 51.7K questions from 23 languages, 11 high- to mid-resource and 12 low-resource.
All questions are *culturally specific* – (1) they refer to concepts unique to one or a few cultures, such as
"Kuber iki umwami wa mbere w’uburundi yitwa Ntare?" (Kirundi), or (2) they have different answers depending on the cultural
or regional context, as in "How do you get a gun license?". These questions were collected to evaluate the multilingual capabilities and
cultural knowledge of state-of-the-art models.

<!-- Provide a longer summary of what this dataset is. -->

- **Languages (high- to mid-resource):** Arabic, Chinese, English, German, Hindi, Hebrew, Hungarian, Japanese, Korean, Russian, Spanish
- **Languages (low-resource):** Afar, Balochi, Faroese, Fijian, Hiligaynon, Kirundi, Papiamento, Pashto, Samoan, Tongan, Tswana, Wolof
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Repository:** [CaLMQA](https://github.com/2015aroras/CaLMQA/tree/main)
- **Paper:** [CaLMQA: Exploring culturally specific long-form question answering across 23 languages](https://arxiv.org/pdf/2406.17761)
- **Size:** 38.6K (~25% of the original 51.7K questions are held out in private test set)

## Uses

These questions were collected to evaluate the multilingual capabilities and
cultural knowledge of state-of-the-art models. Automatic metrics are not
sufficiently developed for multilingual LFQA, but human evaluation is viable. 

## Dataset Structure

The dataset consists of QA entries.
Entry structure:

- `language`: The language of the question.
- `question`: The question that admits a long-form answer, in the language `language`.
- `question_english` (optional): The English translation of the question, for low-resource language questions. These were written by crowdworkers whose native language is `language`.
- `answer` (optional): The answer to the question, in the language `language`. These answers were written by `language` crowdworkers or collected from `language` community QA websites.

<!-- This section provides a description of the dataset fields, and additional information about the dataset structure such as criteria used to create the splits, relationships between data points, etc. -->

## Dataset Creation

### Source Data

Culturally specific questions in low-resource languages are manually written by hired croudworkers.
Culturally specific questions in high- to mid-resource languages are sourced from the following websites.

- [Ejaba](https://www.ejaba.com/) (Arabic)
- [Ujeeb](https://ujeeb.com/) (Arabic)
- [Zhihu](https://www.zhihu.com/) (Chinese)
- [Reddit ELI5](https://www.reddit.com/r/explainlikeimfive/) (English)
- [Gutefrage](https://www.gutefrage.net/) (German)
- [Quora](https://he.quora.com) (Hebrew)
- [Let's Diskuss](https://hi.letsdiskuss.com/) (Hindi)
- [Gyakori kérdések](https://www.gyakorikerdesek.hu/) (Hungarian)
- [Yahoo Japan](https://chiebukuro.yahoo.co.jp/) (Japanese)
- [OKWave](https://okwave.jp/) (Japanese)
- [Naver](https://kin.naver.com/qna/) (Korean)
- [Yandex](https://yandex.ru/q/) (Russian)
- [Todoexpertos](https://www.todoexpertos.com/) (Spanish)

<!-- This section describes the source data (e.g. news text and headlines, social media posts, translated sentences, ...). -->

#### Data Collection and Processing

<!-- This section describes the data collection and processing process such as data selection criteria, filtering and normalization methods, tools and libraries used, etc. -->

We used separate data collection processes for high- to mid-resource languages and for low-resource languages.

For high- to mid-resource languages, we first conducted a survey amongst workers, asking them to provide community LFQA websites
(like Reddit and Quora) in their native non-English languages. We then hire workers to collected long-form culturally specific
questions information-seeking questions from our [collected websites](#source-data). We scale this process by writing custom
web scrapers to collect the questions and using GPT-4o mini to perform quality checks.

For low-resource languages, we instruct workers to write culturally specific questions.

#### Who are the source data producers?

<!-- This section describes the people or systems who originally created the data. It should also include self-reported demographic or identity information for the source data creators if this information is available. -->

All workers were native speakers of the language they collected questions for, as well as proficient English speakers.
Workers from the [Prolific](https://www.prolific.com/) platform were hired to collect culturally specific questions from websites.
Workers from the [UpWork](https://www.upwork.com/) platform were hired to write culturally specific questions in low-resource languages.

#### Personal and Sensitive Information

<!-- State whether the dataset contains data that might be considered personal, sensitive, or private (e.g., data that reveals addresses, uniquely identifiable names or aliases, racial or ethnic origins, sexual orientations, religious beliefs, political opinions, financial or health data, etc.). If efforts were made to anonymize the data, describe the anonymization process. -->

Question topics include religion, politics and history, and so some questions may pertain to sensitive issues.
We explicitly specify in our workers' guidelines that collected questions should not be controversial,
and we manually reviewed all questions. However, some questions may still be unagreeable with some people.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

The questions we source from community QA websites might reflect societal biases in those communities and
might under-represent cultures not captured in these QA forums. Our worker-written questions might have workers' biases.

<!-- ### Recommendations

This section is meant to convey recommendations with respect to the bias, risk, and technical limitations.

Users should be made aware of the risks, biases and limitations of the dataset. More information needed for further recommendations. -->

## Citation

<!-- If there is a paper or blog post introducing the dataset, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
@misc{arora2025calmqaexploringculturallyspecific,
      title={CaLMQA: Exploring culturally specific long-form question answering across 23 languages}, 
      author={Shane Arora and Marzena Karpinska and Hung-Ting Chen and Ipsita Bhattacharjee and Mohit Iyyer and Eunsol Choi},
      year={2025},
      eprint={2406.17761},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2406.17761}, 
}
```