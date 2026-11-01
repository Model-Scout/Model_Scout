---
language:
- ko
- en
pipeline_tag: text-generation
inference: false
tags:
- facebook
- meta
- pytorch
- llama
- llama-2
- kollama
- llama-2-ko
license: mit
library_name: transformers
---

**Update Log**

- 2023.12.14: Initial Release of Open-Llama-2-Ko

# **Open-Llama-2-Ko** 🦙🇰🇷

Open-Llama-2-Ko represents an advanced iteration of the Llama 2 model, featuring an expanded vocabulary and the inclusion of a Korean corpus for enhanced pretraining. Similar to its predecessor, Llama-2-Ko, this model operates within the range of generative text models, with parameter counts ranging from 7 billion to 70 billion. The focus of this repository is on the 7B pretrained version, designed to integrate seamlessly with the Hugging Face Transformers format.

The primary distinction between the Llama-2-Ko Series and Open-Llama-2-Ko lies in the dataset. Open-Llama-2-Ko exclusively utilizes publicly accessible Korean corpora, including sources such as [AI Hub](https://www.aihub.or.kr), [Modu Corpus, 모두의 말뭉치](https://corpus.korean.go.kr/), and [Korean Wikipedia](https://dumps.wikimedia.org/kowiki/).

As training was conducted solely with publicly available corpora, this model is open for unrestricted use by everyone, adhering to the MIT License*.

*MIT License under LLAMA 2 COMMUNITY LICENSE AGREEMENT

## Model Details

**Model Developers:** Junbum Lee (Beomi)

**Variations:** Open-Llama-2-Ko will be available in different parameter sizes — 7B and 13B — along with various pretrained options.

**Input:** The model accepts only text input.

**Output:** The model produces text output exclusively.

**Model Architecture:** 

Open-Llama-2-Ko is an auto-regressive language model that leverages an optimized transformer architecture derived from Llama-2.

| |Training Data|Parameters|Content Length|GQA|Tokens|Learning Rate|
|---|---|---|---|---|---|---|
|Llama 2|*A curated mix of Publicly Accessible Korean Corpora*|7B|2k|✘|>15B*|5e<sup>-5</sup>|

**Training Corpus**

The model was trained using selected datasets from AIHub and Modu Corpus. Detailed information about the training datasets is available below:

- AI Hub: [corpus/AI_HUB](./corpus/AI_HUB)
  - Only the `Training` segment of the data was used.
  - The `Validation` and `Test` segments were deliberately excluded.
- Modu Corpus: [corpus/MODU_CORPUS](./corpus/MODU_CORPUS)

The final JSONL dataset used to train this model is approximately 61GB in size.

Total token count: Approximately 15 billion tokens (*using the expanded tokenizer. With the original Llama tokenizer, >60 billion tokens.)

**Vocab Expansion**

| Model Name | Vocabulary Size | Description | 
| --- | --- | --- |
| Original Llama-2 | 32000 | Sentencepiece BPE |
| **Expanded Llama-2-Ko** | 46336 | Sentencepiece BPE. Added Korean vocab and merges |

**Tokenizing "안녕하세요, 오늘은 날씨가 좋네요."**

| Model | Tokens |
| --- | --- |
| Llama-2 | `['▁', '안', '<0xEB>', '<0x85>', '<0x95>', '하', '세', '요', ',', '▁', '오', '<0xEB>', '<0x8A>', '<0x98>', '은', '▁', '<0xEB>', '<0x82>', '<0xA0>', '씨', '가', '▁', '<0xEC>', '<0xA2>', '<0x8B>', '<0xEB>', '<0x84>', '<0xA4>', '요']` |
| Llama-2-Ko | `['▁안녕', '하세요', ',', '▁오늘은', '▁날', '씨가', '▁좋네요']` |

**Tokenizing "Llama 2: Open Foundation and Fine-Tuned Chat Models"**

| Model | Tokens |
| --- | --- |
| Llama-2 | `['▁L', 'l', 'ama', '▁', '2', ':', '▁Open', '▁Foundation', '▁and', '▁Fine', '-', 'T', 'un', 'ed', '▁Ch', 'at', '▁Mod', 'els']` |
| Llama-2-Ko | `['▁L', 'l', 'ama', '▁', '2', ':', '▁Open', '▁Foundation', '▁and', '▁Fine', '-', 'T', 'un', 'ed', '▁Ch', 'at', '▁Mod', 'els']` |

# LICENSE

[MIT License under LLAMA 2 COMMUNITY LICENSE AGREEMENT](./LICENSE)

# **Model Benchmark**

## LM Eval Harness - Korean (polyglot branch)

- Used EleutherAI's lm-evaluation-harness https://github.com/EleutherAI/lm-evaluation-harness/tree/polyglot

TBD

## Citation

TBD

## Acknowledgements

- Training support was provided by the [TPU Research Cloud](https://sites.research.google/trc/) program.
- The training corpus includes data from [AI Hub](https://www.aihub.or.kr/), [Modu Corpus](https://corpus.korean.go.kr/), and [Korean Wikipedia](https://dumps.wikimedia.org/kowiki/).
