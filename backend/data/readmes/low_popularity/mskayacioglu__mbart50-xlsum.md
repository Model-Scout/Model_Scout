---
language:
- ar
- zh
- en
- fr
- hi
- id
- ja
- ko
- fa
- pt
- ru
- es
- tr
- uk
- vi
license: cc-by-nc-sa-4.0
library_name: transformers
pipeline_tag: summarization
tags:
- mbart
- mbart-50
- multilingual
- summarization
- news-summarization
- xlsum
datasets:
- GEM/xlsum
base_model: facebook/mbart-large-50-many-to-many-mmt
metrics:
- rouge
- bleu
---

# mBART50 XL-Sum

`mbart50-xlsum` is a multilingual abstractive news summarization model fine-tuned from [`facebook/mbart-large-50-many-to-many-mmt`](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt) on 15 language subsets of [`GEM/xlsum`](https://huggingface.co/datasets/GEM/xlsum). It was developed as part of a multilingual news aggregation and summarization project.

This checkpoint is the first of two mBART-50 training variants produced by the project. It uses a standard multilingual mixture, a 96-token target limit, and a compute-conscious two-epoch training setup. Compared with the second variant, it is slightly more source-grounded in the project's automatic diagnostics, while producing very similar reference-overlap scores.

## Related Project

This model was developed as part of [samurAI](https://github.com/mskayacioglu/samurAI), a multilingual news aggregation and summarization system with RSS ingestion, local transformer summarization, SQLite storage, a Flask web interface, JSON APIs, and evaluation notebooks.

Related checkpoint: [mskayacioglu/mbart-xlsum-2](https://huggingface.co/mskayacioglu/mbart-xlsum-2)

## Model Details

| Property | Value |
|---|---|
| Task | Multilingual abstractive news summarization |
| Base model | [`facebook/mbart-large-50-many-to-many-mmt`](https://huggingface.co/facebook/mbart-large-50-many-to-many-mmt) |
| Architecture | `MBartForConditionalGeneration` |
| Encoder / decoder layers | 12 / 12 |
| Attention heads | 16 |
| Hidden size | 1,024 |
| Vocabulary size | 250,054 |
| Maximum model positions | 1,024 |
| Fine-tuning source length | 512 tokens |
| Fine-tuning target length | 96 tokens |
| Framework | PyTorch / Transformers |

## Languages

The fine-tuning mixture contains the following 15 languages:

| Language | mBART code | Language | mBART code |
|---|---|---|---|
| Arabic | `ar_AR` | Chinese (Simplified) | `zh_CN` |
| English | `en_XX` | French | `fr_XX` |
| Hindi | `hi_IN` | Indonesian | `id_ID` |
| Japanese | `ja_XX` | Korean | `ko_KR` |
| Persian | `fa_IR` | Portuguese | `pt_XX` |
| Russian | `ru_RU` | Spanish | `es_XX` |
| Turkish | `tr_TR` | Ukrainian | `uk_UA` |
| Vietnamese | `vi_VN` |  |  |

Quantitative evaluation was completed for 11 of these languages: Arabic, Chinese (Simplified), English, French, Hindi, Japanese, Korean, Russian, Spanish, Turkish, and Vietnamese. Results for Indonesian, Persian, Portuguese, and Ukrainian are not reported in the final common evaluation, so performance claims should not be extrapolated to them.

## Intended Use

The model is intended for:

- summarizing news articles in a supported source language;
- research on multilingual abstractive summarization;
- comparing multilingual training and language-balancing strategies;
- integration into news-processing pipelines with human review.

The model is not intended to be a factual authority, to make editorial decisions autonomously, or to summarize high-stakes medical, legal, financial, or emergency information without verification against the source.

## Training Data

The checkpoint was trained on [`GEM/xlsum`](https://huggingface.co/datasets/GEM/xlsum), a multilingual collection of BBC news articles paired with short reference summaries. Examples from the 15 selected language subsets were combined, shuffled, and annotated with their corresponding mBART language codes.

The final benchmark below is separate from these training-time subsets and uses the full executable test subsets from [`csebuetnlp/xlsum`](https://huggingface.co/datasets/csebuetnlp/xlsum).

| Split | Examples used |
|---|---:|
| Train | 818,129 |
| Validation | 3,000 (up to 200 per language) |
| Test | 3,000 (up to 200 per language) |

## Training Procedure

| Hyperparameter | Value |
|---|---:|
| Epochs | 2 |
| Learning rate | `3e-5` |
| Per-device training batch size | 32 |
| Gradient accumulation | 8 |
| Effective batch size | 256 |
| Weight decay | 0.01 |
| Warmup ratio | 0.03 |
| Precision | bfloat16 when CUDA was available |
| Maximum source length | 512 |
| Maximum target length | 96 |
| Seed | 42 |

Generation-based validation was disabled during training to control compute cost, and no best-checkpoint selection was performed. Training completed 6,390 optimization steps with a final reported training loss of `2.2078` over approximately 4 hours 44 minutes on CUDA hardware.

## Evaluation

### Protocol

The final evaluation used the complete available test subsets of `csebuetnlp/xlsum` for 11 languages, totaling 52,219 examples per model. No per-language sample cap was applied. Scores below are macro-averaged across languages and reported on a `0-1` scale.

Articles were truncated to 512 tokens. Evaluation used batch size 8 and mixed precision on CUDA. The common mBART decoding configuration was:

```text
max_length=90
min_length=24
num_beams=5
length_penalty=1.1
no_repeat_ngram_size=3
repetition_penalty=1.05
early_stopping=True
```

Turkish used a language-specific configuration with `max_length=84`, `min_length=26`, 6 beams, length penalty 1.3, 4-gram repetition blocking, and repetition penalty 1.2. The target language token was forced for every language.

### Overall Results

| Metric | Score |
|---|---:|
| ROUGE-1 F1 | 0.3559 |
| ROUGE-2 F1 | 0.1735 |
| ROUGE-L F1 | 0.2785 |
| BLEU | 0.1202 |
| METEOR-lite | 0.3157 |

`METEOR-lite` is the project's lightweight exact-token implementation and must not be interpreted as the canonical METEOR package score.

### Results by Language

| Language | Samples | ROUGE-1 | ROUGE-2 | ROUGE-L | BLEU | METEOR-lite |
|---|---:|---:|---:|---:|---:|---:|
| Arabic | 4,689 | 0.2674 | 0.1104 | 0.2280 | 0.0726 | 0.2249 |
| English | 11,535 | 0.3489 | 0.1333 | 0.2769 | 0.0957 | 0.3024 |
| Spanish | 4,763 | 0.3032 | 0.1013 | 0.2251 | 0.0675 | 0.2523 |
| French | 1,086 | 0.3121 | 0.1345 | 0.2504 | 0.0953 | 0.2678 |
| Hindi | 8,847 | 0.5677 | 0.2905 | 0.4052 | 0.2122 | 0.5301 |
| Japanese | 889 | 0.4997 | 0.3074 | 0.3669 | 0.2133 | 0.4444 |
| Korean | 550 | 0.4295 | 0.2493 | 0.3429 | 0.1817 | 0.4038 |
| Russian | 7,780 | 0.2401 | 0.0926 | 0.1996 | 0.0630 | 0.1932 |
| Turkish | 3,397 | 0.2291 | 0.0983 | 0.2065 | 0.0704 | 0.1991 |
| Vietnamese | 4,013 | 0.3283 | 0.1575 | 0.2507 | 0.0947 | 0.2895 |
| Chinese (Simplified) | 4,670 | 0.3884 | 0.2335 | 0.3111 | 0.1552 | 0.3654 |

### Supplementary Diagnostics

These diagnostics are included to describe model behavior, not as established factuality or human-quality measures.

| Diagnostic | Value |
|---|---:|
| Mean latency per example | 0.1917 s |
| Mean compression ratio | 23.2527 |
| Mean source coverage | 0.8481 |
| Mean novel bigram ratio | 0.4229 |
| Mean repeated trigram ratio | 0.0039 |
| Mean generated summary length | 31.17 tokens |
| Automatic completeness proxy | 0.4525 |
| Automatic factuality proxy | 0.8522 |

Latency was measured in one CUDA evaluation environment and is not portable across hardware, software versions, or batch configurations. The completeness and factuality values are project-specific automatic proxies; they do not prove semantic completeness or factual correctness.

## Usage

```python
import torch
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration

model_id = "mskayacioglu/mbart50-xlsum"
language_code = "tr_TR"

tokenizer = MBart50TokenizerFast.from_pretrained(model_id)
model = MBartForConditionalGeneration.from_pretrained(model_id)
model.eval()

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

article = "Özetlenecek Türkçe haber metni buraya yazılır."
tokenizer.src_lang = language_code

inputs = tokenizer(
    article,
    return_tensors="pt",
    max_length=512,
    truncation=True,
).to(device)

with torch.inference_mode():
    output_ids = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.lang_code_to_id[language_code],
        max_length=84,
        min_length=26,
        num_beams=6,
        length_penalty=1.3,
        no_repeat_ngram_size=4,
        repetition_penalty=1.2,
        early_stopping=True,
    )

summary = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]
print(summary)
```

For languages other than Turkish, the evaluation configuration used `max_length=90`, `min_length=24`, 5 beams, length penalty 1.1, 3-gram repetition blocking, and repetition penalty 1.05.

## Limitations and Risks

- The model can hallucinate facts, names, dates, quantities, or causal relationships.
- Inputs longer than 512 tokens were truncated during fine-tuning and evaluation; important information near the end of long articles may be omitted.
- XL-Sum is based on BBC news. Performance may decline on other publishers, informal writing, specialist domains, or structurally noisy web text.
- Automatic overlap metrics reward lexical similarity and do not establish factual consistency or summary usefulness.
- Evaluation coverage is uneven across languages and includes only 11 languages in the final common benchmark.
- The training mixture is imbalanced across languages, so high-resource languages can influence the model more strongly.
- The model may reproduce social, geographic, and editorial biases present in its pretrained parameters and news data.
- Always verify generated summaries against the original article before publication or high-stakes use.

## License

XL-Sum is distributed under `CC BY-NC-SA 4.0`. This model card therefore declares the same license for the fine-tuned checkpoint. Users are responsible for checking the terms of the base model and dataset and for ensuring that their intended use is permitted. In particular, the dataset license restricts commercial use.

## Citation

If you use the model, cite the XL-Sum dataset and mBART-50:

- XL-Sum: [arXiv:2106.13822](https://arxiv.org/abs/2106.13822)
- mBART-50: [arXiv:2008.00401](https://arxiv.org/abs/2008.00401)

```bibtex
@inproceedings{hasan-etal-2021-xl,
  title     = {{XL-Sum}: Large-Scale Multilingual Abstractive Summarization for 44 Languages},
  author    = {Hasan, Tahmid and Bhattacharjee, Abhik and Islam, Md. Saiful and Samin, Kazi and Li, Yuan-Fang and Kang, Yong-Bin and Rahman, M. Sohel and Shahriyar, Rifat},
  booktitle = {Findings of ACL-IJCNLP 2021},
  year      = {2021},
  pages     = {4693--4703},
  eprint    = {2106.13822},
  archivePrefix = {arXiv}
}

@article{tang2020multilingual,
  title   = {Multilingual Translation with Extensible Multilingual Pretraining and Finetuning},
  author  = {Tang, Yuqing and Tran, Chau and Li, Xian and Chen, Peng-Jen and Goyal, Naman and Chaudhary, Vishrav and Gu, Jiatao and Fan, Angela},
  journal = {arXiv preprint arXiv:2008.00401},
  year    = {2020},
  eprint  = {2008.00401},
  archivePrefix = {arXiv}
}
```

## Model Card Author

Mert Samet Kayacıoğlu
