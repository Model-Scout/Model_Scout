---
license: apache-2.0
datasets:
- HPLT/HPLT3.0
- allenai/olmo-mix-1124
- HuggingFaceFW/finepdfs
- HuggingFaceTB/finemath
- LLM360/MegaMath
- HuggingFaceTB/stack-edu
- HuggingFaceFW/finepdfs-edu
- cis-lmu/Glot500
- ltg/saami-web
language:
- nb
- nn
- 'no'
- se
base_model:
- allenai/OLMo-2-1124-13B
library_name: transformers
tags:
- norwegian
- norsk
- HPLT
---

# NorOLMo

![](https://hplt-project.org/_next/static/media/logo-hplt.8765d2d4.svg)

NorOLMo 1.0 is a base (not instruction-tuned) large language model, continually pre-trained on Norwegian and Scandinavian data starting from the English [OLMo2-13B](https://huggingface.co/allenai/OLMo-2-1124-13B) model.

It is **the only modern fully open large language model specifically adapted for Norwegian and Sámi**. 
At the same time, its performance is comparable to other multilingual open models (see the Evaluation section below).
**"Fully open"** here means that the entirety of the trainining data and training pipeline is transparent and reproducible, not only that the model weights are available.

The model was trained for 33 000 steps on around 275 billion tokens. Maximum sequence length was set to 4 096 in the beginning of training, and then was extended to 16 384 starting from the checkpoint `step_31000`.
Intermediate checkpoints are published here as branches.
The main `branch` contains the model's weights after step 33 000 (stage 3).

In a few months, we hope to follow with post-trained versions of NorOLMo.

## Evaluation

Below is a comparison of fully-open models supporting Norwegian. The figure shows the aggregate score across all 35 NorEval 1.1 tasks (5 categories, category average). Scores are first averaged within each task category, then averaged across categories. This gives equal weight to each category regardless of how many tasks it contains. Each task score is normalized to a 0–100 scale where 0 = random baseline performance and 100 = perfect score, then averaged across tasks. This accounts for different chance levels across tasks (e.g. 25% for 4-choice QA vs. 50% for binary classification).

More detailed evaluation is evailable in our interactive NorEval dashboard: [https://ltgoslo.github.io/llm-dashboard](https://ltgoslo.github.io/llm-dashboard).

![](noreval_open.png)


Furthermore, an interactive per-checkpoint evaluation with additional ablation studies is available [here](https://ltgoslo.github.io/llm-dashboard/norolmo/).

## Data Details

### Stage 1 (24 000 steps -- 200B tokens)

Data ("pretraining data")
  - [HPLTv3](https://huggingface.co/datasets/HPLT/HPLT3.0): Bokmål, Nynorsk, Faroese, Icelandic, Danish, Swedish
  - [FinePDFs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs): Bokmål, Nynorsk, Faroese, Icelandic, Danish, Swedish
  - [OLMo-Mix](https://huggingface.co/datasets/allenai/olmo-mix-1124)
  - Northern Sámi: ([Glot500](https://huggingface.co/datasets/cis-lmu/Glot500), [Northern Sámi Web Corpus ](https://huggingface.co/datasets/ltg/saami-web), [SIKOR North Saami corpus](https://dataverse.no/dataset.xhtml?persistentId=doi:10.18710/8AK7KZ))

<details>

<summary>Data splits</summary>

| Data                     | Percentage | Unique Tokens | Total Tokens | Number of Documents | Average Document Length |
| ------------------------ | ---------- | ------------- | ------------ | ------------------- | ----------------------- |
| HPLT Bokmål              | 39.57      | 39.8B         | 79.7B        | 36.5M               | 1 092                   |
| HPLT Nynorsk             | 4.95       | 1.2B          | 10.0B        | 1.5M                | 826                     |
| HPLT Faroese             | 0.46       | 0.2B          | 0.9B         | 0.3M                | 711                     |
| HPLT Icelandic           | 2.50       | 5.0B          | 5.0B         | 4.3M                | 1 173                   |
| HPLT Swedish             | 12.09      | 92.1B         | 24.4B        | 97.7M               | 942                     |
| HPLT Danish              | 12.12      | 50.1B         | 24.4B        | 52.5M               | 954                     |
| FinePDFs Bokmål          | 8.36       | 8.4B          | 16.8B        | 1.5M                | 5 604                   |
| FinePDFs Nynorsk         | 1.15       | 0.3B          | 2.3B         | 92.8K               | 3 117                   |
| FinePDFs Faroese         | 0.17       | 87.1M         | 0.3B         | 20.8K               | 4 196                   |
| FinePDFs Icelandic       | 1.60       | 3.2B          | 3.2B         | 0.4M                | 8 855                   |
| FinePDFs Swedish         | 2.48       | 18.9B         | 5.0B         | 4.1M                | 4 574                   |
| FinePDFs Danish          | 2.45       | 10.1B         | 4.9B         | 2.4M                | 4 190                   |
| Northern Sami            | 0.18       | 46.4M         | 0.4B         | 0.2M                | 288                     |
| Wiki (OLMo-Mix)          | 0.02       | 0.2B          | 40.3M        | 0.3M                | 667                     |
| Alg. Stack (OLMo-Mix)    | 0.04       | 0.6B          | 80.5M        | 0.1M                | 4 201                   |
| Open Web Math (OLMo-Mix) | 0.04       | 0.6B          | 80.5M        | 0.1M                | 4 199                   |
| ArXiv (OLMo-Mix)         | 0.05       | 1.0B          | 0.1B         | 0.2M                | 5 210                   |
| PeS2o (OLMo-Mix)         | 0.15       | 2.5B          | 0.3B         | 1.6M                | 1 641                   |
| DCLM (OLMo-Mix)          | 9.50       | 48.3B         | 19.1B        | 35.1M               | 1 377                   |
| StarCoder (OLMo-Mix)     | 2.10       | 30.5B         | 4.2B         | 23.6M               | 1 293                   |

> [!NOTE]
> The number of documents represents the total unique number of documents, not the documents used during training.

> [!NOTE]
> We only took a portion of OLMo-Mix as our unique data.

</details>


### Stage 2 (6 000 steps -- 50B tokens) and Stage 3 (3 000 steps -- 25B tokens)

Data ("midtraining data")
  - [HPLTv3](https://huggingface.co/datasets/HPLT/HPLT3.0) (filtered): Bokmål, Nynorsk, Icelandic, Danish, Swedish
  - [FinePDFs-Edu](https://huggingface.co/datasets/HuggingFaceFW/finepdfs-edu): Bokmål, Nynorsk, Icelandic, Danish, Swedish, English
  - [FinePDFs](https://huggingface.co/datasets/HuggingFaceFW/finepdfs): Faroese
  - Northern Sámi: ([Glot500](https://huggingface.co/datasets/cis-lmu/Glot500), [Northern Sámi Web Corpus ](https://huggingface.co/datasets/ltg/saami-web), [SIKOR North Saami corpus](https://dataverse.no/dataset.xhtml?persistentId=doi:10.18710/8AK7KZ))
  - [Stack-Edu](https://huggingface.co/datasets/HuggingFaceTB/stack-edu)
  - [MegaMath Web-Pro](https://huggingface.co/datasets/LLM360/MegaMath)
  - [FineMath 4+](https://huggingface.co/datasets/HuggingFaceTB/finemath)
  - [InfiWebMath 4+](https://huggingface.co/datasets/Infi-MM/InfiMM-WebMath-40B)

<details>

<summary>Data splits</summary>

Data Splits
| Data                     | Percentage | Unique Tokens | Total Tokens | Number of Documents | Average Document Length |
| ------------------------ | ---------- | ------------- | ------------ | ------------------- | ----------------------- |
| HPLT Bokmål              | 45.78      | 23.0B         | 23.0B        | 19.0M               | 1 215                   |
| HPLT Nynorsk             | 7.84       | 1.0B          | 3.9B         | 1.0M                | 1 003                   |
| HPLT Icelandic           | 6.87       | 3.5B          | 3.5B         | 2.7M                | 1 268                   |
| HPLT Swedish             | 4.90       | 2.5B          | 2.5B         | 3.6M                | 3 403                   |
| HPLT Danish              | 7.73       | 3.9B          | 3.9B         | 4.1M                | 2 950                   |
| FinePDFs-Edu Bokmål      | 2.24       | 1.1B          | 1.1B         | 0.2M                | 6 897                   |
| FinePDFs-Edu Nynorsk     | 0.28       | 35.8M         | 0.1B         | 9.7K                | 3 681                   |
| FinePDFs Faroese         | 0.69       | 87.1M         | 0.3B         | 20.8K               | 4 196                   |
| FinePDFs-Edu Icelandic   | 0.53       | 0.3B          | 0.3B         | 40.1K               | 6 598                   |
| FinePDFs-Edu Swedish     | 5.80       | 2.9B          | 2.9B         | 0.4M                | 6 755                   |
| FinePDFs-Edu Danish      | 2.97       | 1.5B          | 1.5B         | 0.3M                | 5 833                   |
| FinePDFs-Edu English     | 7.00       | 7.2B          | 3.5B         | 1.1M                | 6 280                   |
| Northern Sami            | 0.37       | 46.4M         | 0.2B         | 0.2M                | 288                     |
| Stack-Edu                | 5.00       | 12.8B         | 2.5B         | 15.0M               | 856                     |
| MegaMath Web-Pro         | 0.84       | 13.7B         | 0.4B         | 15.0M               | 917                     |
| FineMath 4+              | 0.62       | 10.1B         | 0.3B         | 6.7M                | 1 512                   |
| InfiWebMath 4+           | 0.54       | 8.9B          | 0.3B         | 6.3M                | 1 417                   |

</details>


## Training details

<details>

<summary>Stage 1</summary>

| Hyperparameter           | Value             |
| ------------------------ | ----------------- |
| Embedding train steps    | 1 000             |
| Warmup steps             | 2 000             |
| Total train steps        | 24 000            |
| Learning rate schedule   | Warmup + constant |
| Learning rate            | 3e-4              |
| Weight decay             | 1e-1              |
| Sequence length          | 4 096             |
| Batch size               | 2 048             |
| RoPe theta               | 500 000           |
| Clip grad                | 1.0               |
| Adam epsilon             | 1e-8              |
| Adam beta_1              | 0.9               |
| Adam beta_2              | 0.95              |
| RMSNorm epsilon          | 1e-6              |
| Z-loss ratio             | 1e-5              |
| Diffusion loss ratio     | 2e-2              |

</details>

<details>

<summary>Stage 2</summary>

| Hyperparameter           | Value             |
| ------------------------ | ----------------- |
| Decay steps              | 6 000             |
| Total train steps        | 6 000             |
| Learning rate schedule   | Linear decay      |
| Initial learning rate    | 3e-4              |
| Final learning rate      | 1.5e-4                 |
| Weight decay             | 1e-1              |
| Sequence length          | 4 096            |
| Batch size               | 2 048               |
| RoPe theta               | 500 000         |
| Clip grad                | 1.0               |
| Adam epsilon             | 1e-8              |
| Adam beta_1              | 0.9               |
| Adam beta_2              | 0.95              |
| RMSNorm epsilon          | 1e-6              |
| Z-loss ratio             | 1e-5              |
| Diffusion loss ratio     | 2e-2              |

</details>

<details>

<summary>Stage 3</summary>

| Hyperparameter           | Value                 |
| ------------------------ | --------------------- |
| Decay steps              | 3 000                 |
| Total train steps        | 3 000                 |
| Learning rate schedule   | Linear decay |
| Max learning rate        | 1.5e-4                  |
| Final learning rate      | 0                     |
| Weight decay             | 1e-1                  |
| Sequence length          | 16 384                |
| Batch size               | 512                   |
| RoPe theta               | 2 000 000             |
| Clip grad                | 1.0                   |
| Adam epsilon             | 1e-8                  |
| Adam beta_1              | 0.9                   |
| Adam beta_2              | 0.95                  |
| RMSNorm epsilon          | 1e-6                  |
| Z-loss ratio             | 1e-5                  |
| Diffusion loss ratio     | 2e-2                  |

</details>


## Acknowledgements

Training was conducted as a part of the [HPLT project](https://hplt-project.org/).

_This project has received funding from the European Union’s Horizon Europe research and innovation programme under grant agreement No 101070350 and from UK Research and Innovation (UKRI) under the UK government’s Horizon Europe funding guarantee [grant number 10052546]_