---
extra_gated_heading: Access beomi/Yi-Ko-DUS on Hugging Face
extra_gated_button_content: Submit
extra_gated_fields:
  I agree to share my name, email address and username: checkbox
  I confirm that I understand this project is for research purposes only, and confirm that I agree to follow the LICENSE of this model: checkbox
language:
- en
- ko
pipeline_tag: text-generation
inference: false
tags:
- pytorch
- Yi-Ko
- 01-ai
- Yi
library_name: transformers
license: apache-2.0
---

> Update @ 2024.01.29 Released Yi-Ko(KoEN)-DUS-9B model 🎉

# **beomi/Yi-Ko-DUS-9B**

Yi-Ko-DUS model serves as DUS-applied and advanced iterations of [beomi/Yi-Ko-6B](https://huggingface.co/beomi/Yi-Ko-6B) model,
benefiting from an expanded vocabulary and the inclusion of Korean/English corpus in its further pretraining. 

Yi-Ko-DUS model operates with 9B billion parameters.

This repository focuses on the **9B** pretrained version,
which is tailored to fit the Hugging Face Transformers format,
trained after DUS method applied.

## Model Details

**Model Developers** Junbum Lee (Beomi), Taekyoon Choi (Taekyoon)

**Variations** Yi-Ko-DUS has 9B model only.

**Input** Models input text only.

**Output** Models generate text only.

**Model Architecture** 

Yi-Ko-DUS series models are an auto-regressive language model that uses an optimized transformer architecture based on Llama-2*.

<small>*Yi model architecture is based on Llama2, so it can be loaded via `LlamaForCausalLM` class on HF.</small>

|Model Name|Training Data|Params|Context Length|GQA|Trained Tokens|LR|Batch Size(per step)|
|---|---|---|---|---|---|---|---|
|Yi-Ko-DUS-9B|*A mix of Korean + English online data*|9B|4k|O|>120B|5e<sup>-5</sup>|2M tokens|

**Vocab Expansion**

| Model Name | Vocabulary Size | Description | 
| --- | --- | --- |
| Original Yi-Series | 64000 | Sentencepiece BPE |
| **Expanded Yi-Ko(DUS) Series** | 78464 | Sentencepiece BPE. Added Korean vocab and merges |

**Tokenizing "안녕하세요, 오늘은 날씨가 좋네요.ㅎㅎ"**

| Model | # of tokens | Tokens |
| --- | --- | --- |
| Original Yi-Series | 47 | `['<0xEC>', '<0x95>', '<0x88>', '<0xEB>', '<0x85>', '<0x95>', '하', '<0xEC>', '<0x84>', '<0xB8>', '<0xEC>', '<0x9A>', '<0x94>', ',', '▁', '<0xEC>', '<0x98>', '<0xA4>', '<0xEB>', '<0x8A>', '<0x98>', '은', '▁', '<0xEB>', '<0x82>', '<0xA0>', '<0xEC>', '<0x94>', '<0xA8>', '가', '▁', '<0xEC>', '<0xA2>', '<0x8B>', '<0xEB>', '<0x84>', '<0xA4>', '<0xEC>', '<0x9A>', '<0x94>', '.', '<0xE3>', '<0x85>', '<0x8E>', '<0xE3>', '<0x85>', '<0x8E>']` |
| **Expanded Yi-Ko(DUS) Series** | 10 | `['▁안녕', '하세요', ',', '▁오늘은', '▁날', '씨가', '▁좋네요', '.', 'ㅎ', 'ㅎ']` |
|<small>*Equal Korean vocab with Llama-2-Ko Series</small>||

**Tokenizing "Llama 2: Open Foundation and Fine-Tuned Chat Models"**

| Model | # of tokens | Tokens |
| --- | --- | --- |
| Original Yi-Series | 21 | `['The', '▁Y', 'i', '▁series', '▁models', '▁are', '▁large', '▁language', '▁models', '▁trained', '▁from', '▁scratch', '▁by', '▁developers', '▁at', '▁', '0', '1', '.', 'AI', '.']` |
| **Expanded Yi-Ko(DUS) Series** | 21 | `['▁The', '▁Y', 'i', '▁series', '▁models', '▁are', '▁large', '▁language', '▁models', '▁trained', '▁from', '▁scratch', '▁by', '▁developers', '▁at', '▁', '0', '1', '.', 'AI', '.']` |
|<small>*Equal Korean vocab with Llama-2-Ko Series</small>| | <small>*Since **Expanded Yi-Ko Series** prepends `_` at the beginning of the text(to ensure same tokenization for Korean sentences), it shows negilible difference for the first token on English tokenization. </small>|

# **Model Benchmark**

## 5-shot Korean Dataset Evaluation

[**KMMLU**](https://github.com/HAETAE-project/lm-evaluation-harness): 43.3514 (exact_match, kmmlu_direct)

- +2.58%p than [beomi/Yi-Ko-6B](https://huggingface.co/beomi/Yi-Ko-6B)

[**KorQuAD**](https://github.com/EleutherAI/lm-evaluation-harness/tree/polyglot): 80.8798 (exact_match)

- +3.06%p than [beomi/Yi-Ko-6B](https://huggingface.co/beomi/Yi-Ko-6B)

[**NSMC**](https://github.com/Beomi/ko-lm-evaluation-harness): 88.352 (acc)

- +0.3%p than [beomi/Yi-Ko-6B](https://huggingface.co/beomi/Yi-Ko-6B)

[**KOBEST COPA**](https://github.com/Beomi/ko-lm-evaluation-harness): 84.4831 (macro_f1)

- +3.6%p than [beomi/Yi-Ko-6B](https://huggingface.co/beomi/Yi-Ko-6B)

[**KOBEST HellaSwag**](https://github.com/Beomi/ko-lm-evaluation-harness): 52.6099 (macro_f1)

- +2.7%p than [beomi/Yi-Ko-6B](https://huggingface.co/beomi/Yi-Ko-6B)

[**Apeach: Korean HateSpeech**](https://github.com/Beomi/ko-lm-evaluation-harness): 63.4723 (macro_f1)

- +13.6%p than [beomi/Yi-Ko-6B](https://huggingface.co/beomi/Yi-Ko-6B)


## LICENSE

Apache 2.0 (for research)

> For commercial purpose,
> mailto: jun@beomi.net to acquire Yi-Ko sereis commercial license.


## Citation

Please use this bibtex below:

```
@misc {lee_junbum_2024,
	author       = { {Lee Junbum, Choi Taekyoon} },
	title        = { Yi-Ko-DUS-9B },
	year         = 2024,
	url          = { https://huggingface.co/beomi/Yi-Ko-DUS-9B },
	doi          = { 10.57967/hf/1707 },
	publisher    = { Hugging Face }
}
```

## Acknowledgement

The training is supported by [TPU Research Cloud](https://sites.research.google/trc/) program.