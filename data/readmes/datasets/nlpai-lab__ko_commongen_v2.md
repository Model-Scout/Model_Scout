---
dataset_info:
  features:
  - name: concept_set
    dtype: string
  - name: '1'
    dtype: string
  - name: '2'
    dtype: string
  - name: '3'
    dtype: string
  - name: '4'
    dtype: string
  - name: gold
    dtype: int64
  splits:
  - name: train
    num_bytes: 1658
    num_examples: 5
  - name: test
    num_bytes: 267519
    num_examples: 847
  download_size: 182862
  dataset_size: 269177
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
task_categories:
- text-generation
language:
- ko
pretty_name: KoCommonGEN-V2
---

# 🌠 KoCommonGEN v2

KoCommonGEN v2: A Benchmark for Navigating Korean Commonsense Reasoning Challenges in Large Language Models (ACL 2024-Findings)

*Jaehyung Seo, Jaewook Lee, Chanjun Park, SeongTae Hong, Seungjun Lee and Heuiseok Lim*

🏫 [NLP & AI Lab](https://blpkorea.cafe24.com/wp/), Korea University

---
### 🔥 News
- September 27, 2023: Provided data support for the [Open Ko-LLM Leaderboard](https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard)
- August 7, 2024: Dataset Release
- August 10, 2024: Experimental Results for the New Models Added
- August 14, 2024: Presented a research paper at ACL 2024





### 👥 Human Evaluation

We recruited 22 native Korean speaking volunteers as human evaluators and paid them $0.8 per question.

|   Model   |  #   | Average Score | cohen's kappa | Krippendorff's alpha |
| :-------: | :--: | :-----------: | :-----------: | :------------------: |
| **Human** |  22  |    0.8395     |    0.7693     |        0.7706        |

### 🤖 Models (August 10, 2024)

The results of 2-shot evaluation of the newly released models.

|             Model              | Size  |  Acc_norm  | Stderr |                             Link                             |
| :----------------------------: | :---: | :--------: | :----: | :----------------------------------------------------------: |
|   **GPT-4** (June 13, 2023)    |       | **0.7450** |        |                                                              |
|   **Mistral-Nemo-Instruct**    |  12B  |   0.6612   | 0.0163 | [🔗](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) |
|     **Mistral-Nemo-Base**      |  12B  |   0.6340   | 0.0166 | [🔗](https://huggingface.co/mistralai/Mistral-Nemo-Base-2407) |
|     **Meta-Llama-3.1-8B**      |  8B   |   0.6246   | 0.0166 |   [🔗](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B)   |
|       **QWEN2-7B base**        |  7B   |   0.6187   | 0.0167 |          [🔗](https://huggingface.co/Qwen/Qwen2-7B)           |
|  **EXAONE-3.0-7.8B-Instruct**  | 7.8B  |   0.6088   | 0.0168 | [🔗](https://huggingface.co/LGAI-EXAONE/EXAONE-3.0-7.8B-Instruct) |
|   **MLP-KTLim-Bllossom-8B**    |  8B   |   0.6057   | 0.0168 |                             [🔗](https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B)                             |
| **Meta-Llama-3.1-8B-Instruct** |  8B   |   0.6057   | 0.0168 |          [🔗](meta-llama/Meta-Llama-3.1-8B-Instruct)          |
|           **KULLM3**           | 10.8B |   0.6033   | 0.0168 |         [🔗](https://huggingface.co/nlpai-lab/KULLM3)         |
|       **QWEN2-7B inst**        |  7B   |   0.5832   | 0.017  |                 [🔗](Qwen/Qwen2-7B-Instruct)                  |
|       **Gemma-2-9b-it**        |  9B   |   0.5714   | 0.0170 |       [🔗](https://huggingface.co/google/gemma-2-9b-it)       |
|         **Aya-23-8B**          |  8B   |   0.5159   | 0.0172 |                  [🔗](CohereForAI/aya-23-8B)                  |
|  **Allganize-Alpha-Instruct**  |  8B   |   0.4970   | 0.0172 | [🔗](https://huggingface.co/allganize/Llama-3-Alpha-Ko-8B-Instruct) |

As mentioned in the paper, it is possible to evaluate various models.



### 🇰🇷🇺🇸🇯🇵🇨🇳🇪🇸 Code-switching

The dataset can be found on Hugging Face at: [nlpai-lab/ko_commongen_v2_code_switching](https://huggingface.co/datasets/nlpai-lab/ko_commongen_v2_code_switching)

This dataset contains code-switching data for the following languages:
- Korean (korean)
- English (english)
- Japanese (japan)
- Chinese (china)
- Spanish (espanol)

(The code-switching data relies on machine translation, which may result in some inaccuracies.)

### 📖 Citation

```
@inproceedings{seo2024Kocommongenv2,
    title = "KoCommonGEN v2: A Benchmark for Navigating Korean Commonsense Reasoning Challenges in Large Language Models",
    author = "Jaehyung Seo and Jaewook Lee and Chanjun Park and SeongTae Hong and Seungjun Lee and Heuiseok Lim",
    booktitle = "Findings of the Association for Computational Linguistics: ACL 2024",
    month = August,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "TBD",
    doi = "TBD",
    pages = "TBD"}
```

### 🚨 Warning!

This dataset contains some instances of toxic speech.


### 🙏 Acknowledgement

We sincerely appreciate the dedication of Chanjun Park, Sanghoon Kim and Sunghun Kim (Sung Kim) from **Upstage AI** in managing one of the benchmark datasets for the
[Open Ko-LLM LeaderBoard](https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard).