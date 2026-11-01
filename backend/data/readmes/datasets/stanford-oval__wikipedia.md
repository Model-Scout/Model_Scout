---
task_categories:
- text-retrieval
- text-generation
language:
- en
- fr
- de
- es
- ja
- ru
- pt
- zh
- it
- ar
- fa
- pl
- nl
- uk
- he
- id
- tr
- cs
- sv
- ko
- fi
- vi
- hu
- ca
- th
pretty_name: Preprocessed Multilingual Wikipedia
size_categories:
- 100M<n<1B
configs:
  - config_name: '20250320'
    data_files:
      - 20250320/en/collection.parquet
      - 20250320/fr/collection.parquet
      - 20250320/de/collection.parquet
      - 20250320/es/collection.parquet
      - 20250320/ja/collection.parquet
      - 20250320/ru/collection.parquet
      - 20250320/pt/collection.parquet
      - 20250320/zh/collection.parquet
      - 20250320/it/collection.parquet
      - 20250320/ar/collection.parquet
      - 20250320/fa/collection.parquet
      - 20250320/pl/collection.parquet
      - 20250320/nl/collection.parquet
      - 20250320/uk/collection.parquet
      - 20250320/he/collection.parquet
      - 20250320/id/collection.parquet
      - 20250320/tr/collection.parquet
      - 20250320/cs/collection.parquet
      - 20250320/sv/collection.parquet
      - 20250320/ko/collection.parquet
      - 20250320/fi/collection.parquet
      - 20250320/vi/collection.parquet
      - 20250320/hu/collection.parquet
      - 20250320/ca/collection.parquet
      - 20250320/th/collection.parquet
  - config_name: '20241101'
    data_files:
      - 20241101/en/collection.parquet
      - 20241101/fr/collection.parquet
      - 20241101/de/collection.parquet
      - 20241101/es/collection.parquet
      - 20241101/ja/collection.parquet
      - 20241101/ru/collection.parquet
      - 20241101/pt/collection.parquet
      - 20241101/zh/collection.parquet
      - 20241101/it/collection.parquet
      - 20241101/ar/collection.parquet
      - 20241101/fa/collection.parquet
      - 20241101/pl/collection.parquet
      - 20241101/nl/collection.parquet
      - 20241101/uk/collection.parquet
      - 20241101/he/collection.parquet
      - 20241101/id/collection.parquet
      - 20241101/tr/collection.parquet
      - 20241101/cs/collection.parquet
      - 20241101/sv/collection.parquet
      - 20241101/ko/collection.parquet
      - 20241101/fi/collection.parquet
      - 20241101/vi/collection.parquet
      - 20241101/hu/collection.parquet
      - 20241101/ca/collection.parquet
      - 20241101/th/collection.parquet
  # - config_name: '20241001'
  #   data_files:
  #     - 20241001/en/collection.jsonl
  #     - 20241001/de/collection.jsonl
  #     - 20241001/es/collection.jsonl
  #     - 20241001/fa/collection.jsonl
  #     - 20241001/fr/collection.jsonl
  #     - 20241001/it/collection.jsonl
  #     - 20241001/zh/collection.jsonl
  #     - 20241001/ru/collection.jsonl
  #     - 20241001/ja/collection.jsonl
  #     - 20241001/pt/collection.jsonl
  # - config_name: '20240801'
  #   data_files:
  #     - 20240801/en/collection.jsonl
  #     - 20240801/de/collection.jsonl
  #     - 20240801/es/collection.jsonl
  #     - 20240801/fa/collection.jsonl
  #     - 20240801/fr/collection.jsonl
  #     - 20240801/it/collection.jsonl
  #     - 20240801/zh/collection.jsonl
  #     - 20240801/ru/collection.jsonl
  #     - 20240801/ja/collection.jsonl
  #     - 20240801/pt/collection.jsonl
  # - config_name: '20240401'
  #   data_files:
  #     - 20240401/en/collection.jsonl
  #     - 20240401/de/collection.jsonl
  #     - 20240401/es/collection.jsonl
  #     - 20240401/fa/collection.jsonl
  #     - 20240401/fr/collection.jsonl
  #     - 20240401/it/collection.jsonl
  #     - 20240401/zh/collection.jsonl
  #     - 20240401/ru/collection.jsonl
  #     - 20240401/ja/collection.jsonl
  #     - 20240401/pt/collection.jsonl
---



This dataset contains preprocessed and chunked Wikipedia HTML dumps from 25 languages.

Refer to the following for more information:

GitHub repository: https://github.com/stanford-oval/WikiChat

Papers:
- [WikiChat: Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia](https://arxiv.org/abs/2305.14292)
- [SPAGHETTI: Open-Domain Question Answering from Heterogeneous Data Sources with Retrieval and Semantic Parsing](https://arxiv.org/abs/2406.00562)

<p align="center">
    <img src="https://github.com/stanford-oval/WikiChat/blob/main/public/img/logo_light.png?raw=true" width="100px" alt="WikiChat Logo" />
    <h1 align="center">
        <b>WikiChat</b>
        <br>
        <a href="https://github.com/stanford-oval/WikiChat/stargazers">
            <img src="https://img.shields.io/github/stars/stanford-oval/WikiChat?style=social" alt="Github Stars">
        </a>
    </h1>
</p>
<p align="center">
    Stopping the Hallucination of Large Language Model Chatbots by Few-Shot Grounding on Wikipedia
</p>
<p align="center">
    Online demo:
    <a href="https://wikichat.genie.stanford.edu" target="_blank">
        https://wikichat.genie.stanford.edu
    </a>
    <br>
</p>

<p align="center">
    <img src="https://raw.githubusercontent.com/stanford-oval/WikiChat/d863523e92c8520691be53436fb03d1c4719fe74/public/img/pipeline.svg" width="700px" alt="WikiChat Pipeline" />
</p>
