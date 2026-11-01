---
language:
- ko
- en
pipeline_tag: text-generation
inference: false
tags:
- solar
- mistral
- pytorch
- solar-ko
library_name: transformers
license: apache-2.0
---

**Update Log**

- 2024.01.08: Initial Test version Release of Solar-Ko

# **Open-Solar-Ko** ⭐🇰🇷

Solar-Ko represents an advanced iteration of the upstage/SOLAR-10.7B-v1.0 model, featuring an expanded vocabulary and the inclusion of a Korean corpus for enhanced pretraining. 

Open-Solar-Ko exclusively utilizes publicly accessible Korean corpora, including sources such as [AI Hub](https://www.aihub.or.kr), [Modu Corpus, 모두의 말뭉치](https://corpus.korean.go.kr/), and [Korean Wikipedia](https://dumps.wikimedia.org/kowiki/).

As training was conducted solely with publicly available corpora, this model is open for unrestricted use by everyone, adhering to the Apache2.0 open source License.

## Model Details

**Model Developers:** Junbum Lee (Beomi)

**Variations:** Solar-Ko is available with one parameter sizes — 10B with Continual Pretrained version.

**Input:** The model accepts only text input.

**Output:** The model produces text output exclusively.

**Model Architecture:** 

SOLAR-KO-10.7B is an auto-regressive language model that leverages an optimized transformer architecture derived from Llama-2.

| |Training Data|Parameters|Content Length|GQA|Tokens|Learning Rate|
|---|---|---|---|---|---|---|
|SOLAR-KO-10.7B|*A curated mix of Publicly Accessible Korean Corpora*|10.7B|4k|O|>15B*|5e<sup>-5</sup>|

**Training Corpus**

The model was trained using selected datasets from AIHub and Modu Corpus. Detailed information about the training datasets is available below:

- AI Hub: [corpus/AI_HUB](./corpus/AI_HUB)
  - Only the `Training` segment of the data was used.
  - The `Validation` and `Test` segments were deliberately excluded.
- Modu Corpus: [corpus/MODU_CORPUS](./corpus/MODU_CORPUS)

The final JSONL dataset used to train this model is approximately 61GB in size.

Total token count: Approximately 15 billion tokens (*using the expanded tokenizer. With the original SOLAR tokenizer, >60 billion tokens.)

**Vocab Expansion**

| Model Name | Vocabulary Size | Description | 
| --- | --- | --- |
| Original Solar | 32000 | Sentencepiece BPE |
| **Expanded SOLAR-KO-10.7B** | 46592 | Sentencepiece BPE. Added Korean vocab and merges |

**Tokenizing "안녕하세요, 오늘은 날씨가 좋네요."**

- SOLAR-10.7B: 26 tokens
- SOLAR-KO-10.7b: 8 tokens

| Model | Tokens |
| --- | --- |
| SOLAR-10.7B | `['▁', '안', '<0xEB>', '<0x85>', '<0x95>', '하', '세', '요', ',', '▁', '오', '<0xEB>', '<0x8A>', '<0x98>', '은', '▁', '날', '<0xEC>', '<0x94>', '<0xA8>', '가', '▁', '좋', '네', '요', '.']` |
| SOLAR-KO-10.7B | `['▁안녕', '하세요', ',', '▁오늘은', '▁날', '씨가', '▁좋네요', '.']` |

**Tokenizing "Meet 10.7B Solar: Elevating Performance with Upstage Depth UP Scaling!"**

- SOLAR-10.7B: 22 tokens
- SOLAR-KO-10.7b: 22 tokens

| Model | Tokens |
| --- | --- |
| SOLAR-10.7B | `['▁Meet', '▁', '1', '0', '.', '7', 'B', '▁Solar', ':', '▁E', 'lev', 'ating', '▁Performance', '▁with', '▁Up', 'stage', '▁Dep', 'th', '▁UP', '▁Scal', 'ing', '!']` |
| SOLAR-KO-10.7B | `['▁Meet', '▁', '1', '0', '.', '7', 'B', '▁Solar', ':', '▁E', 'lev', 'ating', '▁Performance', '▁with', '▁Up', 'stage', '▁Dep', 'th', '▁UP', '▁Scal', 'ing', '!']` |

# LICENSE

Apache 2.0

# **Model Benchmark**

## LM Eval Harness - Korean (polyglot branch)

- Used EleutherAI's lm-evaluation-harness https://github.com/EleutherAI/lm-evaluation-harness/tree/polyglot

|                                  |        0 |        5 |       10 |       50 |
|:---------------------------------|---------:|---------:|---------:|---------:|
| kobest_boolq (macro_f1)          | 0.853949 | 0.88098  | 0.898139 | 0.902354 |
| kobest_copa (macro_f1)           | 0.804531 | 0.826736 | 0.837656 | 0.860899 |
| kobest_hellaswag (macro_f1)      | 0.507174 | 0.500983 | 0.487287 | 0.512182 |
| kobest_sentineg (macro_f1)       | 0.3517   | 0.972291 | 0.977321 | 0.984884 |
| kohatespeech (macro_f1)          | 0.258111 | 0.403957 | 0.386808 | 0.462393 |
| kohatespeech_apeach (macro_f1)   | 0.337667 | 0.651697 | 0.705337 | 0.827757 |
| kohatespeech_gen_bias (macro_f1) | 0.124535 | 0.503464 | 0.498501 | 0.443218 |
| korunsmile (f1)                  | 0.3814   | 0.356939 | 0.369989 | 0.296193 |
| nsmc (acc)                       | 0.5356   | 0.87162  | 0.88654  | 0.89632  |
| pawsx_ko (acc)                   | 0.5435   | 0.5245   | 0.5315   | 0.5385   |

## Citation

```
@misc {solar_ko_junbum_2023,
    author       = { {L. Junbum} },
    title        = { Solar-Ko-10.7b },
    year         = 2024,
    url          = { https://huggingface.co/beomi/SOLAR-KO-10.7B },
    publisher    = { Hugging Face }
}

```

## Acknowledgements

- Training support was provided by the [TPU Research Cloud](https://sites.research.google/trc/) program.
- The training corpus includes data from [AI Hub](https://www.aihub.or.kr/), [Modu Corpus](https://corpus.korean.go.kr/), and [Korean Wikipedia](https://dumps.wikimedia.org/kowiki/).