---
license: cc-by-4.0
language:
- zh
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- fil
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
- yue
task_categories:
- text-classification
tags:
- refusal
- multilingual
- chat
---
# Multilingual AI Conversations — Refusal Dataset

This dataset contains **non-English AI conversations** where the model either refuses a user request or completes it.  
It is derived from a randomly sampled subset of the [`agentlans/en-chat-refusal`](https://huggingface.co/datasets/agentlans/en-chat-refusal) dataset (`downsampled` split).

Each conversation has been automatically translated into a randomly selected target language using [tencent/Hunyuan-MT-7B](https://huggingface.co/tencent/Hunyuan-MT-7B).

<details>
  <summary><strong>Click to view all supported languages</strong></summary>

- Arabic  
- Bengali  
- Burmese  
- Cantonese  
- Chinese  
- Czech  
- Dutch  
- Filipino  
- French  
- German  
- Gujarati  
- Hebrew  
- Hindi  
- Indonesian  
- Italian  
- Japanese  
- Kazakh  
- Khmer  
- Korean  
- Malay  
- Marathi  
- Mongolian  
- Persian  
- Polish  
- Portuguese  
- Russian  
- Spanish  
- Tamil  
- Telugu  
- Thai  
- Tibetan  
- Traditional Chinese  
- Turkish  
- Ukrainian  
- Urdu  
- Uyghur  
- Vietnamese  
</details>

## Limitations

- The dataset is relatively small compared to the source dataset.
- It contains the biases of the [NousResearch/Minos-v1](https://huggingface.co/NousResearch/Minos-v1) model annotations and the datasets that make up [agentlans/en-chat-refusal](https://huggingface.co/datasets/agentlans/en-chat-refusal).
- Machine translations are not manually verified and may contain minor inaccuracies. However, they remain suitable for refusal detection research.  
- Low-resource languages are included, which may influence model performance or introduce higher translation variance.
