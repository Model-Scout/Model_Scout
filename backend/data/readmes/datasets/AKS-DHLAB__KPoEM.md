---
license: mit
task_categories:
- text-classification
language:
- ko
tags:
- emotion
- classification
- digitalhumanities
size_categories:
- 1K<n<10K
---

# 📊 KPoEM (Korean Poetry Emotion Mapping) Dataset 📊

| Category | Han Yong-un | Im Hwa | Kim So-wol | Yi Sang | Yun Dong-ju | Total |
|----------|-------------:|-------:|------------:|--------:|------------:|------:|
| Line-level | 1,198 | 2,163 | 2,071 | 464 | 1,111 | 7,007 |
| Work-level | 138 | 110 | 176 | 77 | 114 | 615 |
| **Subtotal** |  |  |  |  |  | **7,622** |
| **Number of Poems** | **117** | **43** | **165** | **46** | **112** | **483** |

While Large Language Models (LLMs) demonstrate exceptional performance in emotion classification for general texts—such as news, blogs, and daily conversations—their efficacy significantly diminishes when confronted with poetic language rich in metaphors and symbolism. Because poetry often conveys emotions indirectly through figurative expressions rather than literal statements, conventional AI models that rely on statistical word patterns struggle to capture the subtle emotional layers embedded within the text. To bridge this 'interpretive gap,' a specialized dataset dedicated to poetry is essential.

To address this need, we collected 483 poems from five major Korean modern poets—Kim So-wol, Yun Dong-ju, Im Hwa, Yi Sang, and Han Yong-un—from public domain sources.

The KPoEM dataset contains 7,007 emotion-annotated line-level texts and 615 work-level entries, totaling 7,622 annotated instances. Each instance was independently labeled by five trained experts using a multi-label scheme based on the 44 emotion categories of the KOTE framework.

## 🏷️ KPoEM Emotion Category Index (Based on the KOTE Framework)
  
| index | Emotion Category | index | Emotion Category | index | Emotion Category | index | Emotion Category |
|------:|-----------|------:|-----------|------:|-----------|------:|-----------|
| 0 | 불평/불만 (dissatisfaction) | 11 | 비장함 (resolute) | 22 | 짜증 (irritation) | 33 | 당황/난처 (embarrassment) |
| 1 | 환영/호의 (welcome) | 12 | 의심/불신 (relief) | 23 | 어이없음 (preposterous) | 34 | 경악 (shock) |
| 2 | 감동/감탄 (admiration) | 13 | 뿌듯함 (pride) | 24 | 없음 (NO EMOTION) | 35 | 부담/안_내킴 (reluctant) |
| 3 | 지긋지긋 (fed up) | 14 | 편안/쾌적 (comfort) | 25 | 패배/자기혐오 (gessepany) | 36 | 서러움 (sorrow) |
| 4 | 고마움 (gratitude) | 15 | 신기함/관심 (interest) | 26 | 귀찮음 (laziness) | 37 | 재미없음 (boredom) |
| 5 | 슬픔 (sadness) | 16 | 아껴주는 (care)| 27 | 힘듦/지침 (exhaustion) | 38 | 불쌍함/연민 (compassion) |
| 6 | 화남/분노 (anger) | 17 | 부끄러움 (shame) | 28 | 즐거움/신남 (excitement) | 39 | 놀람 (surprise) |
| 7 | 존경 (respect) | 18 | 공포/무서움 (fear) | 29 | 깨달음 (realization) | 40 | 행복 (happiness) |
| 8 | 기대감 (expectancy) | 19 | 절망 (despair) | 30 | 죄책감 (guilt) | 41 | 불안/걱정 (anxiety) |
| 9 | 우쭐댐/무시함 (arrogance) | 20 | 한심함 (pathetic) | 31 | 증오/혐오 (contempt) | 42 | 기쁨 (joy) |
| 10 | 안타까움/실망 (disappointment) | 21 | 역겨움/징그러움 (disgust) | 32 | 흐뭇함(귀여움/예쁨) (attracted) | 43 | 안심/신뢰 (relief) |


KPoEM dataset is designed as an infrastructure resource for digital humanities and generative AI research. The dataset served as the primary training resource for **the KPoEM emotion classification model (see [link](https://huggingface.co/AKS-DHLAB/KPoEM))**, further validating its effectiveness as a domain-specific corpus. It has also been successfully integrated into a RAG-based emotion-aware poetry generation framework, demonstrating its utility for modeling culturally grounded affective patterns in modern Korean literature.

The study is associated with the following publication:

## 🖌️ Citations
* LIM, I., Ji, H., & Kim, B. (2026). KPoEM: A Human-Annotated Dataset for Emotion Classification and RAG-Based Poetry Generation in Korean Modern Poetry. *The Review of Korean Studies, 29*(1), 161-206. [10.25024/review.2026.29.1.006](https://doi.org/10.25024/review.2026.29.1.006)
    
## 🧑‍🤝‍🧑 Contributors 🧑‍🤝‍🧑

- **IRO LIM** — Producer, Dataset Lead  
- **Haein Ji** — Data Curator  
- **Sul Koo** — Annotator  
- **Song-yi Jung** — Annotator  
- **Jonghoon Yun** — Annotator  
- **Byungjun Kim** — Supervisor


### 📘 KPoEM 데이터셋 사용 안내  *(User Guide for the KPoEM Dataset)*

본 저장소에는 두 가지 데이터셋이 포함되어 있습니다. *(This repository contains two datasets. The dataset is provided as TSV files at both the **line-level** and **poem-level**, without predefined train/validation/test splits.)*

The dataset was designed to capture the inherently interpretive and metaphorically dense nature of poetic language. To this end, the line-level data were segmented and partially shuffled to encourage annotators to focus on localized emotional cues, while the work-level annotations were performed with full contextual awareness of each poem. This dual-layer design enables comparative research on context sensitivity in poetic emotion analysis.

- KPoEM_line_dataset_v4.tsv : 시 행 단위(line-level) 데이터셋

- KPoEM_poem_dataset_v4.tsv : 시 작품 단위(poem-level) 데이터셋

⚠️ 주의: 두 데이터셋의 컬럼 구조가 달라서 datasets.load_dataset()으로 동시에 불러올 경우 CastError가 발생합니다. 따라서 개별 파일을 pandas DataFrame으로 로드 후 필요에 맞게 편집하는 방식을 권장합니다.

* Note: The two datasets have different column schemas, so loading them together with `datasets.load_dataset()` may raise a `CastError`. We recommend loading each file separately as a `pandas` DataFrame and then preprocessing/merging as needed.*

📥 Example: Loading the Line-level Dataset

<pre markdown="1"> 
  from datasets import load_dataset 
  df_line = load_dataset(
  "csv", 
  data_files={ "train": "hf://datasets/AKS-DHLAB/KPoEM/KPoEM_line_dataset_v4.tsv"}, 
  delimiter="\t", 
  encoding="utf-8", 
  quoting=3, 
  ) 
  df = df_line["train"].to_pandas() 
  df.head()
</pre>

📥 Example: Loading the Work-level Dataset

<pre markdown="2"> 
  from datasets import load_dataset
  df_poem = load_dataset(
    "csv",
    data_files={
        "train": "hf://datasets/AKS-DHLAB/KPoEM/KPoEM_poem_dataset_v4.tsv"},
    delimiter="\t",
    encoding="utf-8",      
    quoting=3,             
    )
  df = df_poem["train"].to_pandas()
  df.head()
</pre>

***
## 📚 Scholarly Record 📚

### 💡 Related Model & Application

The KPoEM dataset served as the foundational resource for developing specialized emotion classification models and generative AI applications.

- **KPoEM Emotion Classification Model**: This dataset was crucially used to fine-tune the [KPoEM model](https://huggingface.co/AKS-DHLAB/KPoEM). By undergoing sequential fine-tuning—starting from the general-purpose KOTE dataset and concluding with the domain-specific KPoEM—the model achieves state-of-the-art performance in capturing the metaphorical and culturally specific emotions of Korean poetry.

- **RAG-Based Poetry Generation**: Beyond classification, this dataset is integrated into a Retrieval-Augmented Generation (RAG) framework. It enables LLMs to generate or revise poetic texts that maintain high thematic and emotional consistency with the distinctive styles of modern Korean masters.

### 📄 Conference Presentation

임이로, 지해인, & 김병준. (2025. 10). 한국 근현대시의 감정 분석과 인공지능 시 창작 응용: KPoEM 데이터셋 구축과 활용. 반교어문학회 제180차 정기학술대회, 성균관대학교, 서울, 대한민국.

Lim, I., Ji, H., & Kim, B. (2025. 4). Decoding the Poetic Language of Emotion in Korean Modern Poetry: Insights from a Human-Labeled Dataset and AI modeling. Digital Humanities and Social Sciences Korea Conference, James Joo-Jin Kim Center for Korean Studies, University of Pennsylvania, Philadelphia, USA.

LIM, I., Ji, H., & Kim, B. (2025. 2). *한국 근현대시 감정 라벨링 데이터셋 구축: 문학 텍스트의 컴퓨터 기반 감정 분류와 생성형 AI 활용을 위한 기초 연구*.  
The 2nd Conference of the Korean Modern Literature Association (KorLitConf), Seoul, Korea.  
Zenodo. [DOI: https://doi.org/10.5281/zenodo.15055795](https://doi.org/10.5281/zenodo.15055795)

### 💻 Source Code (Data Parsing, Modeling, and RAG-Based AI Generation)
All source code used in this study is publicly available:  
https://github.com/AKS-DHLAB/KPoEM

### 🔄 Update Records

The KPoEM dataset has been updated and permanently archived on Zenodo (v4.0) [https://zenodo.org/records/15598092](https://zenodo.org/records/15598092).

📄 Prerprint Paper: [KPoEM: A Human-Annotated Dataset for Emotion Classification and RAG-Based Poetry Generation in Korean Modern Poetry](https://arxiv.org/abs/2509.03932)
