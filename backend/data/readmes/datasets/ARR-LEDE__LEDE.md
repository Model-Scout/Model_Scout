---
language:
- en
- ko
license: cc-by-nc-4.0
task_categories:
- text-classification
- text-generation
pretty_name: LEDE
size_categories:
- 100K<n<1M
tags:
- ai-generated-text
- ai-detection
- news
- multilingual
- llm
- benchmark
---  
## LEDE : A large-scale benchmark for AI-generated news detection

> Author identities and the camera-ready release URL will be revealed at the camera-ready stage.
 
<br>
LEDE is a large-scale, AI-generated news detection benchmark dataset comprising 337K articles and over 4.3M sentences. It addresses the limitations of existing benchmarks by providing broader generator diversity and news-specific coverage across 21 state-of-the-art LLMs, two languages, and 17 news categories. This makes LEDE an invaluable resource for advancing AI-generated text detection research, with the dataset publicly available for future studies. 
<br>

### Highlights

- 337K AI-generated news articles
- 4.3M multilingual sentences
- 21 state-of-the-art LLMs
- 17 news categories
- 4 prompting strategies
- English and Korean support
<br>
<br>
  
## LEDE Dataset Description

LEDE is a large-scale multilingual benchmark for AI-generated news detection, designed to support robust evaluation across diverse LLM families, news categories, prompting strategies, and languages.

### LEDE Dataset
#### Statistic
  - \# of LLMs : **21**
  - \# of Languages : **2 (Eng, Kor)**
  - \# of Articles : **337,322**
  - \# of Sentences : **4,309,153**
  - \# of News Category : **17**
  - \# of News Strategy : **4 (sc, ib, ng, we)** 
  - \# English Sentences : **2,393,518**
  - \# Korean Sentences : **1,915,635**

#### Generation Strategy

| Strategy | Articles | Sentences |
|---|---:|---:|
| **SC** (Sheep’s Clothing) | 99,655 | 1,275,933 |
| **IB** (Information Blending) | 75,460 | 866,438 |
| **NG** (Narrative Generation) | 83,320 | 1,139,081 |
| **WE** (Writing Enhancement) | 78,887 | 1,027,701 |
| **Total** | **337,322** | **4,309,153** |

#### News Category

| Category | arts, culture, entertainment and media | conflict, war and peace | crime, law and justice | disaster, accident and emergency incident | economy, business and finance |        education |      environment |           health |   human interest |
| -------- | -------------------------------------: | ----------------------: | ---------------------: | ----------------------------------------: | ----------------------------: | ---------------: | ---------------: | ---------------: | ---------------: |
| # News (Sentence)   |   32,111 (454,450) |        14,804 (223,531) |       32,307 (430,483) |     13,034 (162,600) |  38,923 (514,214) | 21,866 (252,621) | 14,042 (158,646) | 23,835 (288,276) | 11,594 (171,088) |

<br>

| Category |           labour | lifestyle and leisure | politics and government |       religion | science and technology |          society |            sport |        weather |
| -------- | ---------------: | --------------------: | ----------------------: | -------------: | ---------------------: | ---------------: | ---------------: | -------------: |
| # News (Sentence) | 18,604 (207,569) |      16,191 (181,333) |        32,642 (460,835) | 5,925 (83,169) |       24,462 (287,674) | 16,353 (183,685) | 17,655 (215,904) | 2,974 (33,075) |

<br>

#### Configuration of **LEDE** Metadata

This dataset contains AI-generated news articles, along with metadata describing their origin and generation process.

- Each CSV file follows the naming format below:
  `{Model_Name}_{Language}.csv`

- Below is an example from the Claude_haiku_3.5_Eng.csv file:

| human_rid | human_fid | title | summary | ai_article | category | model | strategy | language | num_sentences | num_words |
| --------- | ----- | ------- | ---------- | ------ | ----- | -------- | -------- | ------------- | --------- | --------- |
| If ever there was-wonderful to the city.    | It doesn t matter-his ... News     | Bronze Statue Honors Dedicated ...     | If ever there was a man worthy of a grand birthday ...    | Bronze Statue Honors Dedicated City  ...     | arts, culture, entertainment and media  | Claude_haiku_3.5  | ib	   | eng    | 10  | 236 |
| —        |—        |—        | —        |—        | —        | —        | —        | —        |—        | —        |
| ALQST says at least-can lead to prison.   | nan  | Travis Scott's Astroworld Festival  ... | Astroworld Festival Tragedy Key Facts:-...  | Travis Scott\'s Astroworld Festival Tragedy Claims Eight Lives... | disaster, accident and emergency incident | Claude_Sonnet_4.5  | sc  | eng   | 14  | 280 |



| Field | Description |
|---|---|
| `human_rid` | Identifier for the original human-written article. <br> • AIHub datasets: uses the official AIHub dataset ID <br> • English datasets: constructed as `{first 4 words}-{last 4 words}` from the original article |
| `human_fid` | Identifier for the corresponding fake/generated counterpart. <br> • AIHub datasets: uses the official AIHub dataset ID <br> • English datasets: constructed as `{first 4 words}-{last 4 words}` from the original article |
| `title` | Title of the AI-generated news article |
| `summary` | Summary of the AI-generated news article |
| `ai_article` | Full text of the AI-generated news article |
| `category` | News category of the article (17 categories in total; e.g., politics, health, law, economy, sports) |
| `model` | Large Language Model (LLM) used for article generation (21 models in total) |
| `strategy` | Generation strategy used for article creation (sc, ib, ng, we)|
| `language` | Language of the generated article (Kor or Eng) |
| `num_sentences` | Number of sentences in the generated article |
| `num_words` | Number of words in the generated article |
<br>

### Human-written News Datasets

The following human-written news datasets were used as source corpora for generating AI-written news articles.
Please download all datasets and place them under the `data/human/` directory.

- [AI-Hub Dataset](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=97) 
- [Newsroom Dataset](https://huggingface.co/datasets/lil-lab/newsroom) 
- Ayoobi Dataset 
- [ISOT Fake News Dataset](https://www.kaggle.com/datasets/rahulogoel/isot-fake-news-dataset)


### Quick start
```python 
import os
from huggingface_hub import snapshot_download 

download_dir = "./"
os.makedirs(download_dir, exist_ok=True)

data = snapshot_download(
    repo_id="ARR-LEDE/LEDE",
    repo_type="dataset",
    local_dir=download_dir,
    allow_patterns=[
        "README.md",
        "data/**/*.csv",
    ],
)

print(data)
``` 

### Repository Structure
```text
LEDE
├── README.md                      # Dataset description and usage guide 
├── Eng/                    # English AI-generated news articles
│   ├── Claude_haiku_3.5_Eng.csv
│   ├── GPT_4o_Eng.csv
│   └── ...
└── Kor/                    # Korean AI-generated news articles
    ├── Claude_haiku_3.5_Kor.csv
    ├── GPT_4o_Kor.csv
    └── ... 
``` 

## Citation

```bibtex
@article{lede2026,
  title={LEDE: A Large-scale Benchmark for AI-generated News Detection},
  author={Anonymous Authors},
  year={2026}
}