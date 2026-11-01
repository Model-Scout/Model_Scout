---
license: cc-by-4.0
language:
  - ko
pretty_name: K-Haters
tags:
  - hate speech detection
configs:
  - config_name: default
    data_files:
      - split: train
        path: train_v2.jsonl
      - split: validation
        path: val_v2.jsonl
      - split: test
        path: test_v2.jsonl
---

# K-HATERS: A Hate Speech Detection Corpus in Korean with Target-Specific Ratings
 
This dataset introduces K-HATERS, the largest hate speech detection corpus in Korean, shared with our EMNLP'23 findings paper. [[link]](https://arxiv.org/abs/2310.15439)
 
GitHub: [ssu-humane/K-HATERS](https://github.com/ssu-humane/K-HATERS)

---
## K-HATERS has been updated to K-HATERS 2.0! (2026-10-07)
> K-HATERS 2.0 adds fine-grained target labels to the corpus. While K-HATERS provides the target category of a hateful comment (e.g., Gender), it does not provide the target itself (e.g., Female, Male, LGBTQ). K-HATERS 2.0 adds a new field ```target``` that fills this gap. The comments, labels, target categories, rationales, and the data split remain the same as K-HATERS.

### What's new in 2.0
* New field `target`: the fine-grained target for each target category of a comment.
* The `target_label` value `region` was renamed to `region_race`.

### How fine-grained targets were annotated
- Fine-grained targets were annotated by Gemini-2.5-Flash given the comment and its target category, and then manually reviewed and normalized. 

The following table shows the fine-grained targets in each target category.
| Target category | Target |
|---|---|
| Political | Progressive, Conservative |
| Region & Race | China, Japan, Korea, North Korea, USA, Afghanistan, Korean-Chinese, Black, White |
| Job | Journalist, Public Official, Legal Professional, Politician, Athlete, Entertainer, Educator, Religious Worker, Healthcare Worker |
| Gender | Female, Male, LGBTQ |
| Age | Elderly, Young Adult, Minor, Middle-Aged |
| Disabled | Mental Disability, Developmental Disability, Physical Disability |
| Religion | Islam, Protestantism, Buddhism, Catholicism |

---
 
## Data collection and annotation
 
- We collected news comments published through the politics, society and world news sections in Naver News over two months in 2021.
- All comments were annotated through CashMission, a crowdsourcing service run by SELECTSTAR. 
- Labeling guidelines are available as a part of SELECTSTAR open datasets (in Korean). [[link]](https://open.selectstar.ai/ko/?page_id=5948)
- [2.0] Fine-grained targets were annotated by Gemini-2.5-Flash given the comment and its target category, and then manually reviewed and normalized. 

## Data distribution
 
We provide the split data of 172,158/10,000/10,000 for training, validation, and test purposes, ensuring the label distribution is maintained.
 
![label_distribution](https://github.com/ssu-humane/K-HATERS/assets/76468616/d08aa6df-923c-4fcf-88ae-c322d39acbed)<br>
 
## Data description
 
```python
>>> data['train'][42]
{"id": 42, "text": "군대도 안간 놈 이 주둥아리 는 씽씽하네..보수 놈 들..군대는 안가고 애국이냐..#@이름#,#@이름#,", "label": "L1_hate", "target_label": ["political"], "offensiveness_rationale": [[7, 8], [11, 15], [27, 28]], "target_rationale": [[24, 26], [46, 51], [52, 57]], "target": [{"category": "political", "fine": "conservative"}]}
```
 
- Abusive language categories (```label```)
  + *L2_hate*: Comments with explicit forms of hate expressions toward one of the groups of protected attributes (e.g., gender, age, race, ...)
  + *L1_hate*: Comments with more implicit forms of hate expressions
  + *Offensive*: Comments that express offensiveness but not toward a protected attribute group
  + *Normal*: The rest comments
- Multi-label target categories (```target_label```): list of offensiveness targets. A comment can have zero or multiple targets.
  + List of target categories: gender, age, region & race, religion, politics, job, disability, individuals, and others.
- Annotators' rationales for the strength of ratings (```offensiveness_rationale```): lists providing annotators' rationales for the strength of ratings. The list includes the start and end indices of highlight spans.
- Annotators' rationales for the target of offensiveness (```target_rationale```)
- [2.0] Fine-grained targets (```target```): list of the specific targets that the hate is directed at, with one entry per target category.
  + ```category```: corresponds to ```target_label```.
  + ```fine```: the fine-grained target within that category (e.g., *conservative* for *political*). It is *null* when the fine-grained target cannot be determined from the comment.

## How to use it
 
```python
from datasets import load_dataset
 
data = load_dataset('humane-lab/K-HATERS')
train = data['train']
valid = data['validation']
test =  data['test']
```
 
## Where are the ratings?
The original dataset was labeled by annotators for thirteen rating variables on a 3-point Likert scale, each indicating the offensiveness strength toward a target.
In this paper, we proposed a label transformation scheme leading to 4-class abusive language categories and multi-label target labels for efficient modeling.
The above code is to access the transformed dataset. Please refer to the details of the transformation method in our paper.
 
If you want to use the dataset with rating variables, please refer to the following code.
```python
from datasets import load_dataset
 
data = load_dataset('humane-lab/K-HATERS-Ratings')
```
 
The rating distribution is as follows:
![image](https://github.com/ssu-humane/K-HATERS/assets/80903024/b081c2e9-c81d-424b-b4c2-e6e57d4c1fb8)
 
## Acknowledgements
 
The dataset construction was supported by DATUMO (SELECTSTAR) through the "2022 AI Dataset Supporting Business" program.
 
## Dataset usage
 
This dataset is shared under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.en).
According to this license, you are free to use the dataset as long as you provide appropriate attribution (e.g., citing our paper).
 
```bibtex
@article{park2023haters,
  title={K-HATERS: A Hate Speech Detection Corpus in Korean with Target-Specific Ratings},
  author={Park, Chaewon and Kim, Suhwan and Park, Kyubyong and Park, Kunwoo},
  journal={Findings of the EMNLP 2023},
  year={2023}
}
```

<!--
# ℹ️ Dataset card for K-HATERS
### Dataset summary
We introduces **K-HATERS**, a new corpus for hate speech detection in Korean, comprising approximately 192K news comments with target-specific offensiveness ratings.
The corpus consists of 192,158 news comments consisting of 184,117 news comments collected by ourselves and 8,041 comments collected from a [previous study](https://aclanthology.org/2020.socialnlp-1.4/).
We collected news comments published through the politics, society and world news sections in Naver News over two months in 2021. 
All comments were annotated through CashMission, a crowdsourcing service run by SELECTSTAR.
</br>For more information, please refer to the paper [K-HATERS](https://arxiv.org/abs/2310.15439) published at EMNLP 2023 Findings.

### Supported tasks
- Hate speech detection
  - Multi class classification (labels: normal, offensive, L1_hate, L2_hate)
  - Binary classifiction (labels: normal, toxic(offensive, L1_hate, L2_hate))
  - Rationale prediction (offensiveness, target rationale)

### Data describtion
```
data['train'][42]
{'text': '군대도 안간 놈 이 주둥아리 는 씽씽하네..보수 놈 들..군대는 안가고 애국이냐..#@이름#,#@이름#,',
 'label': 'L1_hate',
 'target_label': ['political'],
 'offensiveness_rationale': [[7, 8], [11, 15], [27, 28]],
 'target_rationale': [[24, 26], [46, 51], [52, 57]]}
```
- Abusive language categories (**label**)
  - L2_hate: Comments with explicit forms of hate expressions toward one of the groups of protected attributes (e.g., gender, age, race, ...)
  - L1_hate: Comments with more implicit forms of hate expressions
  - Offensive: Comments that express offensiveness but not toward a protected attribute group
  - Normal: The rest comments
- Multi-label target categories (**target_label**): list of offensiveness targets. A comment can have zero or multiple targets.
  - List of target categories: gender, age, race, religion, politics, job, disability, individuals, and others.
- Annotators' rationales for the strength of ratings (**offensiveness_rationale**): lists providing annotators' rationales for the strength of ratings. The list includes the start and end indices of highlight spans.
- Annotators' rationales for the target of offensiveness (**target_rationale**)
 
### Dataset split
We provide the dataset in the form of splits as 172,158 (for train), 10,000 (for validation), and 10,000 (for test). Label ratio was preseved (stratified split).

### Labeling guidelines
Labeling guidelines are available as a part of SELECTSTAR open datasets (in Korean). [link](https://open.selectstar.ai/ko/?page_id=5948)


</br>


# 📜 Data statement
We present the data statement for responsible usage [(Bender and Friedman, 2018)](https://aclanthology.org/Q18-1041/).

### Curation Rationale
We collected the raw data from the news aggregator of Naver, the largest news portal in Korea. We targeted news articles published in the society, world news, and politics sections because discussions are active in the hard news.

### Language Variety
Our dataset consists of the news comments in Korean (ko-KR).

### Speaker Demographic
The user demographic is not available. However, considering that the portal site has the largest share of Korean, it can be assumed that speakers are mostly Korean.

### Annotator Demographic
A total of 405 workers participated in an annotation. 21 workers are 10s, 222 workers are 20s, 116 workers are 30s, 35 workers are 40s, 9 workers are 50s, and 2 workers are 60s. 

### Speech Situation 
News article in the hard news section deals with controversial events, so there are more likely to exist hate comments or toxicity comments. The target articles were published between July 2021 and August 2021. During that period, the most controversial events were the South Korean presidential election, the Tokyo Olympics, COVID-19, and the Restoration of Taliban Control, etc.  

### Text Characteristics
It includes hatred words limited to Korea, such as hatred of certain political orientations and certain groups. For example, '대깨문' (a word that hates former Korean president Moon's supporter), and '꼴페미' (a word that hates feminists)

</br>

# 🤝 License & Contributors
### Licensing information
This dataset is shared under CC-BY 4.0. 
</br>According to this license, you are free to use the dataset as long as you provide appropriate attribution (e.g., citing our paper).

### Citation information
```
@article{park2023haters,
  title={K-HATERS: A Hate Speech Detection Corpus in Korean with Target-Specific Ratings},
  author={Park, Chaewon and Kim, Suhwan and Park, Kyubyong and Park, Kunwoo},
  journal={Findings of the EMNLP 2023},
  year={2023}
}
```

### Contributions
- Chaewon Park
- Suhwan Kim (TUNiB)
- Kyubyong Park (TUNiB)
- Kunwoo Park

#-->