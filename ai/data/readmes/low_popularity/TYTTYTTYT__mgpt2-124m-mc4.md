---
license: apache-2.0
language:
  - de
  - en
  - es
  - fr
  - it
  - ja
  - ko
  - zh
tags:
  - gpt2
  - mixar
  - multilingual
  - baseline
pipeline_tag: text-generation
library_name: transformers
---

# MGPT-2 (124M, multilingual mC4)

A GPT-2 (124M) model pretrained from scratch on the same eight-language mC4 mix
as the MIXAR pixel-based language models. It is the **tokenizer-based control**
in the MIXAR paper: identical pretraining corpus and comparable size, differing
only in the input and output interface (subword tokens instead of rendered
pixels).

[Code](https://github.com/april-tools/mixar) · [Paper](https://arxiv.org/abs/2604.11575)

## Results

| Benchmark | Score |
| --- | --- |
| bAbI task 1, English, free generation | 24.3 |
| SIB-200, 22 languages | seen 77.8 / unseen 26.2 / unseen low-resource 19.3 |
| XNLI, 10 languages | seen 72.5 / unseen 63.9 |
| GLUE | 74.0 |

SIB-200 (macro-F1) and XNLI (accuracy, translate-train) are finetuned per
language. See the paper for the full tables and protocols.

## Details

| | |
| --- | --- |
| Architecture | GPT-2, 12 layers, 12 heads, hidden 768 |
| Parameters | 124M |
| Tokenizer | the original GPT-2 BPE vocabulary (50,257 tokens) |
| Pretraining data | mC4 in de, en, es, fr, it, ja, ko, zh, with the same language mix as MIXAR |
| Steps | 1M |

The tokenizer is the English GPT-2 BPE vocabulary, so non-Latin scripts are split
into byte-level fragments: a Chinese bAbI prompt takes roughly 2.7 times as
many tokens as its English counterpart.

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tok = AutoTokenizer.from_pretrained("TYTTYTTYT/mgpt2-124m-mc4")
model = AutoModelForCausalLM.from_pretrained("TYTTYTTYT/mgpt2-124m-mc4")
```

Note that the tokenizer is the original English GPT-2 BPE vocabulary, so
non-Latin scripts are segmented into byte-level fragments (a Chinese bAbI
prompt takes roughly 3x more tokens than its English counterpart).

## All released models

| Model | Stage 1 | Stage 2 (GRPO) |
| --- | --- | --- |
| 113M, 8x8 patches | [llama-pixar-116m-p8](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p8) | [llama-pixar-116m-p8-stage2](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p8-stage2) |
| 116M, 32x32 patches | [llama-pixar-116m-p32](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p32) | [llama-pixar-116m-p32-stage2](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p32-stage2) |
| 477M, 32x32 patches | [llama-pixar-477m-p32](https://huggingface.co/TYTTYTTYT/llama-pixar-477m-p32) | [llama-pixar-477m-p32-stage2](https://huggingface.co/TYTTYTTYT/llama-pixar-477m-p32-stage2) |

Also released: the adversarial stage-2 ablation
[llama-pixar-116m-p8-stage2-gan](https://huggingface.co/TYTTYTTYT/llama-pixar-116m-p8-stage2-gan) and the
tokenizer-based baseline [mgpt2-124m-mc4](https://huggingface.co/TYTTYTTYT/mgpt2-124m-mc4), pretrained on
the same corpus.

## License

Released under the Apache License 2.0.

## Citation

```bibtex
@article{hu2026mixar,
  title   = {{MIXAR}: Scaling Autoregressive Pixel-based Language Models to Multiple Languages and Scripts},
  author  = {Hu, Chen and Tai, Yintao and Vergari, Antonio and Keller, Frank and Suglia, Alessandro},
  journal = {arXiv preprint arXiv:2604.11575},
  year    = {2026}
}
```
