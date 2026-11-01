---
license: apache-2.0
language:
- en
- id
- ms
- zh
- ja
- ko
- ta
- hi
- ur
library_name: pytorch
pipeline_tag: text-generation
tags:
- from-scratch
- mixture-of-experts
- small-language-model
- multilingual
- code
datasets:
- HuggingFaceFW/fineweb-edu
- HuggingFaceFW/fineweb-2
- codeparrot/github-code-clean
---

# quipu-moe-1B-A149M

A mixture-of-experts language model trained from scratch: **998,007,552 parameters
in total, 148,660,992 active per token** (998.0M total / 148.7M active). Own tokenizer, own data
pipeline, no fine-tuned base. Code and ten languages: English, Indonesian, Malay,
Simplified and Traditional Chinese, Japanese, Korean, Tamil, Hindi (Devanagari and
romanised) and romanised Urdu.

This is the **base model**: it continues text and code; it does not follow instructions (the chat model is AneekC/quipu-moe-1B-A149M-chat).

At this size it is often wrong. It is published as an honest record of what a small
sparse model learns under a $20 compute cap, with every A/B result, including the
ones that lost. Fields marked _not yet measured_ had no result file when this card
was generated.

Project page: <https://quipulm.dev> · Code: <https://github.com/Aneek1/quipu>

## Architecture

| | |
|---|---|
| Type | Decoder-only transformer, sparse mixture of experts |
| Parameters | 998,007,552 total / 148,660,992 active per token (998.0M / 148.7M; embeddings tied, counted once) |
| Layers / width | 16 layers, d_model 768 |
| Attention | grouped-query, 12 query / 4 key-value heads, head dim 64, RoPE base 10000 |
| Feed-forward | 1 shared expert(s) (hidden 768) + 64 routed experts (hidden 384), top-4 |
| Routing | softmax router, Top-k on score + bias, weights renormalised over the chosen experts; Quantile Balancing (auxiliary-loss-free bias) |
| Expert activation | SwiGLU (per the A/B winners, results/moe/run_config.toml) |
| Depth mixing | plain pre-norm residual (Block Attention Residuals not used) (per the A/B winners, results/moe/run_config.toml) |
| Optimizer | Muon (Newton-Schulz orthogonalised per attention head) for weight matrices, AdamW for the rest (per the A/B winners, results/moe/run_config.toml) |
| Training precision | bf16 (router and balancing math in fp32; per the A/B winners, results/moe/run_config.toml) |
| Context | 2,048 tokens |
| Tokenizer | byte-level BPE, 49,152 tokens, trained for this model (code-aware whitespace, ten languages) |

## Data

| source | dataset | revision | licence |
|---|---|---|---|
| code | codeparrot/github-code-clean | `c48d40f9e70f` | the permissive subset of codeparrot/github-code-clean (each file keeps its own licence) |
| english | HuggingFaceFW/fineweb-edu | `87f09149ef47` | HuggingFaceFW/fineweb-edu, ODC-By 1.0 |
| fineweb2 | HuggingFaceFW/fineweb-2 | `af9c13333eb9` | HuggingFaceFW/fineweb-2, ODC-By 1.0 |

Mix achieved (share of training tokens): code 60.0%, eng_Latn 28.0%, other_languages 12.0%.

Training tokens in the shard set: 8,300,000,000 (the train split; validation and evaluation splits are separate).

Code licences kept: mit, apache-2.0, bsd-2-clause, bsd-3-clause, isc, cc0-1.0, unlicense.

Language identification: every text document was checked with the fastText specialist from [AneekC/lid-specialists-9plus1](https://huggingface.co/AneekC/lid-specialists-9plus1) (MIT, revision `117966eb565a`), the owner's own model; a document whose top label is not its source language was dropped, and FineWeb-2's cmn_Hani was split into Simplified and Traditional Chinese by its labels.

| language | kept | dropped | kept while unsure |
|---|---:|---:|---:|
| English | 2,118,540 | 920 | 0 |
| Urdu (romanised) | 13,692 | 55,629 | 0 |
| Hindi (romanised) | 80,968 | 5,188 | 0 |
| Tamil | 98,348 | 536 | 0 |
| Malay | 130,638 | 5,783 | 0 |
| Hindi (Devanagari) | 107,087 | 63,675 | 0 |
| Korean | 107,219 | 1,086 | 0 |
| Indonesian | 103,664 | 2,846 | 0 |
| Japanese | 102,510 | 222 | 0 |
| Chinese (script not split) | 230,766 | 166 | 0 |

### Benchmark decontamination

Documents dropped because they contain a HumanEval or MBPP problem (rule, from the shard manifest: a document is dropped when it contains a problem's text (HumanEval: prompt, canonical_solution; MBPP: code, task text) as a whitespace-collapsed substring of at least 60 characters, or, for one of the problem's n-gram texts (its solution; HumanEval also its prompt and each docstring in it), at least 50% and at least 2 of that text's distinct 13-grams (tokens: \w+ runs and single punctuation characters; a text with fewer than 2 13-grams takes no part)):

| split | humaneval | mbpp |
|---|---:|---:|
| train_code | 79 | 44 |
| train_text | 0 | 1 |
| code_val | 0 | 0 |
| val | 0 | 0 |
| val_lang | 0 | 0 |



## Training

| | |
|---|---|
| Tokens trained | 4,261,937,152 (8,129 steps) |
| Throughput | 44,331 tokens/s (throughput gate) |
| Hardware | 1 x RTX 5090 32 GB (rented, Vast.ai) |
| Cost | $18.75 from the spend ledger: GPU session (hourly); excludes Vast bandwidth charges. The GPU box's hours (setup, A/B runs, the full run, the chat fine-tune, evaluation) plus the CPU shard-build box |
| Schedule | peak LR 0.0006, warmup 500 steps, cosine to 6e-05; batch 524,288 tokens |

### A/B tests (run before the full run, results kept either way)

**Runs** (from results/ab/summary.md, verbatim)

| # | run | config diff | tokens | status | final loss (decision) | english val | bpb | tokens/s | spikes | skipped | startup s | overhead s | compile | decision |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | p1-adamw | (config) | 200,000,000 | completed | 4.0599 | 4.9218 | 1.6016 | 93,145 | 0 | 0 | 56 | 12 | off | pair 1: not kept |
| 2 | p1-muon | optimizer=muon | 200,000,000 | completed | 3.3207 | 4.4059 | 1.4337 | 91,394 | 0 | 0 | 59 | 14 | off | pair 1: kept; pair 2: kept; pair 3: not kept |
| 3 | p1-muon-seed1338 | optimizer=muon, seed=1338 | 200,000,000 | completed | 3.3487 | 4.4167 | 1.4372 | 91,494 | 0 | 0 | 59 | 15 | off | seed re-run of p1-muon |
| 4 | p2-attnres | optimizer=muon, attnres_blocks=4 | 200,000,000 | completed | 3.0322 | 4.2076 | 1.3692 | 77,266 | 0 | 0 | 70 | 19 | off | pair 2: not kept |
| 5 | p3-situ_glu | optimizer=muon, activation=situ_glu | 200,000,000 | completed | 3.2733 | 4.3792 | 1.4250 | 83,595 | 0 | 0 | 65 | 21 | off | pair 3: kept |

**Decisions** (from results/ab/summary.md, verbatim)

| pair | simpler | other | kept | noise | reason |
|---|---|---|---|---|---|
| 1 optimizer | p1-adamw | p1-muon | optimizer=muon (p1-muon) | 0.0280 | lower loss by 0.7392, beyond noise 0.0280 |
| 2 attnres | p1-muon | p2-attnres | attnres_blocks=0 (p1-muon) | 0.0280 | AttnRes throughput cost 15.5% is over the 10% limit [shared noise: pair 1's seed re-run] |
| 3 activation | p1-muon | p3-situ_glu | activation=situ_glu (p3-situ_glu) | 0.0280 | lower loss by 0.0474, beyond noise 0.0280 [shared noise: pair 1's seed re-run] |

Rules (on the decision loss above): the other option needs lower final loss by more than the seed noise; AttnRes <= 10% tokens/s cost; SiTU-GLU no more spikes (step loss > 1.5 x EMA, beta 0.98); FP8 >= 1.2x tokens/s, loss within noise, no more spikes. A missing arm keeps the simpler option (AdamW, no AttnRes, SwiGLU, bf16).

### FP8

FP8 training was not tried in the paid run: the owner decided (2026-09-29) not to spend A/B time on the FP8 pair, so the run is bf16. The FP8 option exists in the training code (quipu/fp8.py) and was only checked on the laptop.

## Evaluation

### Bits per byte per language

Bits per byte (lower is better; comparable across tokenizers) on held-out text per language and held-out code. Definition: summed next-token loss in bits over the UTF-8 bytes of the target tokens. Every <|endoftext|> document separator is a target too: its loss counts but it is 0 bytes of text, so these numbers are slightly higher (more pessimistic) than a separator-free measure.

| checkpoint | step | English | Indonesian | Malay | Chinese (Simplified) | Chinese (Traditional) | Japanese | Korean | Tamil | Hindi (Devanagari) | Hindi (romanised) | Urdu (romanised) | Code |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| step_000163 | 163 | 1.919 | 2.503 | 2.532 | 3.797 | 3.740 | 2.669 | 2.774 | 1.025 | 1.294 | 2.844 | 3.156 | 1.993 |
| step_000407 | 407 | 1.421 | 1.755 | 1.792 | 2.860 | 2.806 | 1.924 | 1.968 | 0.739 | 0.894 | 2.092 | 2.459 | 0.925 |
| step_000813 | 813 | 1.232 | 1.611 | 1.617 | 2.487 | 2.393 | 1.689 | 1.684 | 0.652 | 0.780 | 1.812 | 2.220 | 0.712 |
| step_001626 | 1,626 | 1.131 | 1.409 | 1.421 | 2.387 | 2.264 | 1.546 | 1.542 | 0.602 | 0.702 | 1.650 | 2.030 | 0.609 |
| step_003252 | 3,252 | 1.054 | 1.296 | 1.303 | 2.026 | 2.002 | 1.402 | 1.380 | 0.554 | 0.644 | 1.470 | 1.807 | 0.534 |
| step_005690 | 5,690 | 0.990 | 1.208 | 1.208 | 1.843 | 1.813 | 1.295 | 1.252 | 0.513 | 0.595 | 1.316 | 1.656 | 0.477 |
| step_008129 | 8,129 | 0.959 | 1.157 | 1.162 | 1.768 | 1.728 | 1.234 | 1.199 | 0.491 | 0.568 | 1.255 | 1.582 | 0.448 |

### Code: HumanEval and MBPP

_not yet measured_ (published numbers of reference models, for when it is:)

| model | params | metric / setting | HumanEval pass@1 | HumanEval pass@10 | MBPP pass@1 | MBPP pass@10 | source |
|---|---|---|---:|---:|---:|---:|---|
| CodeGen-350M-mono | 350M | sampled, top-p 0.95, best of T in {0.2, 0.6, 0.8} per k (Table 1 caption); HumanEval 164; 0-shot; no MBPP in that table | 12.8 | 23.1 | - | - | published, not re-run: Nijkamp et al., CodeGen (ICLR 2023), arXiv:2203.13474, Table 1 |
| SantaCoder-1.1B | 1.1B | sampled n=200, T=0.2 for pass@1 and T=0.8 for pass@10 (paper, sec. on evaluation); HumanEval and MBPP as MultiPL-E's Python versions, MBPP derived from the sanitized subset (paper), not necessarily our 257-problem test split | 18.0 | 29.0 | 35.0 | 58.0 | published, not re-run: bigcode/santacoder model card (self-reported; Allal et al., arXiv:2301.03988) |
| SmolLM-135M | 135M | no number in the text (HumanEval shown as a chart only) | - | - | - | - | published, not re-run: huggingface.co/blog/smollm; cheap to re-run on the laptop |
| SmolLM-360M | 360M | no number in the text (HumanEval shown as a chart only) | - | - | - | - | published, not re-run: huggingface.co/blog/smollm; cheap to re-run on the laptop |
| Qwen2.5-Coder-1.5B (base) | 1.5B | unverified setting: the report does not state the decoding for this table (the word 'greedy' does not appear) nor which MBPP problems or how many shots this column uses (a separate MBPP 3-shot column exists); HumanEval (164) and MBPP are reported beside EvalPlus's HumanEval+ / MBPP+ | 43.9 | - | 69.2 | - | published, not re-run: Hui et al., Qwen2.5-Coder Technical Report, arXiv:2409.12186, Table 5 |

### Expert usage

Routing frequency per expert, per layer and language (16 layers x 64 experts): the full tables and a heatmap are in the repository (results/experts). Here, dead: < 10% of the balanced target over the evaluated tokens; overloaded: > 300%. These are the trainer's health-alert bounds (quipu.train MOE_HEALTH_LOW / MOE_HEALTH_HIGH), applied to one evaluation pass; the training log's own "dead" count is stricter (experts with zero assignments in a logging interval), and its health alert needs a sustained window of steps out of bounds.

| split | dead experts | overloaded experts |
|---|---:|---:|
| English | 184 | 55 |
| Indonesian | 239 | 49 |
| Malay | 249 | 47 |
| Chinese (Simplified) | 303 | 73 |
| Chinese (Traditional) | 302 | 73 |
| Japanese | 312 | 80 |
| Korean | 291 | 87 |
| Tamil | 362 | 106 |
| Hindi (Devanagari) | 334 | 83 |
| Hindi (romanised) | 238 | 63 |
| Urdu (romanised) | 265 | 66 |
| Code | 63 | 6 |

Expert specialisation by programming language (Python vs JavaScript / JSX, spec 7) was not measured: the code validation split carries no per-document language label, so code is one split in the expert-usage tables.

### Samples

Greedy (temperature 0) continuations of the fixed prompts, final checkpoint, unedited: good and bad alike.

**The history of the printing press** (step_008129, greedy)

```
The history of the printing press is a fascinating one. It was the first printing press in the world, and it was the first to print on paper. It was also the first to print on paper.
The first printing press was invented in 1600 by the French scientist Jean Baptiste de Vaux. It was a machine that was used to print on paper. It was used to print on paper, and
```

**Photosynthesis is the process by which** (step_008129, greedy)

```
Photosynthesis is the process by which plants convert sunlight into chemical energy.
The process of photosynthesis is a process that occurs in the plant’s cells. The process is controlled by the plant’s own cells, which are the cells that produce the food and oxygen that plants need.
The process of photosynthesis is a process that occurs in the plant’s cells. The process is controlled by the plant ...
```

**In mathematics, a prime number** (step_008129, greedy)

```
In mathematics, a prime number is a prime number that is divisible by 2.
- 10000000000000000000000000000000000000000000000000000000000000000
```

**def fibonacci(n):** (step_008129, greedy)

```
def fibonacci(n):
    """
    Return the fibonacci of n
    """
    if n == 1:
        return 1
    elif n == 2:
        return fibonacci(n-1)
    elif n == 3:
        return fibonacci(n-2)
    elif n == 4:
        return fibonacci(n-3)
    elif n == 
```

**function debounce(fn, delay) {** (step_008129, greedy)

```
function debounce(fn, delay) {
  var timeout;
  return function () {
    var context = this, args = arguments;
    var later = function () {
      timeout = null;
      fn.apply(context, args);
    };
    var callNow = immediate && !timeout;
    clearTimeout(timeout);
    timeout = setTimeout(later, delay);
    if (callNow) fn.apply(context, args);
  };
}


```

**<!DOCTYPE html>
<html>** (step_008129, greedy)

```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>105年第十四任總統副總統及第九屆立法委員選舉</title>

<link rel="stylesheet" type="text/css" href="css/main.css">

</head>

<body>
<div id="main">
    <div id="main-body">
        <div
```

**SELECT customer_id, COUNT(*)** (step_008129, greedy)

```
SELECT customer_id, COUNT(*) FROM customer;
SELECT customer_id, COUNT(*) FROM customer;
SELECT customer_id, COUNT(*) FROM customer;
SELECT customer_id, COUNT(*) FROM customer;
SELECT customer_id, COUNT(*) FROM customer;
SELECT customer_id, COUNT(*) FROM customer;
SELECT customer_id, COUNT(*) FROM customer;
SELECT customer_id, COUNT(*) FROM customer;
SELECT customer_id, COUNT(*)
```

**Sejarah kota Jakarta dimulai** (step_008129, greedy)

```
Sejarah kota Jakarta dimulai pada tahun 1960-an.
Pada tahun 1960-an, kota Jakarta menjadi kota yang paling terkenal di dunia. Kota ini menjadi kota yang paling terkenal di dunia.
Pada tahun 1960-an, kota Jakarta menjadi kota yang paling terkenal di dunia. Kota Jakarta menjadi kota yang paling terkenal di dunia.
Pada tahun 1960-an, kota
```

**Fotosintesis adalah proses** (step_008129, greedy)

```
Fotosintesis adalah proses yang sangat cepat dan cepat.
- Meningkatkan daya tahan tubuh
- Meningkatkan daya tahan tubuh
- Meningkatkan daya tahan tubuh
- Meningkatkan daya tahan tubuh
- Meningkatkan daya tahan tubuh
- Meningkatkan daya tahan tubuh
- Meningkatkan daya tahan tubuh
- Meningkatkan daya tahan tubuh
-
```

**Malaysia terkenal dengan** (step_008129, greedy)

```
Malaysia terkenal dengan keindahan alam semulajadi.
Kini, Malaysia menjadi negara yang paling terkenal dengan keindahan alam semulajadi.
Kini, Malaysia menjadi negara yang paling terkenal dengan keindahan alam semulajadi.
Kini, Malaysia menjadi negara yang paling terkenal dengan keindahan alam semulajadi.
Kini, Malaysia menjadi negara yang paling terkenal dengan
```

**Cara terbaik untuk belajar bahasa baharu ialah** (step_008129, greedy)

```
Cara terbaik untuk belajar bahasa baharu ialah dengan menggunakan bahasa yang dipilih.
Bagi pelajar yang ingin belajar bahasa baharu, anda boleh memilih bahasa yang dipilih.
Bagi pelajar yang ingin belajar bahasa baharu, anda boleh memilih bahasa yang dipilih.
Bagi pelajar yang ingin belajar bahasa baharu, anda boleh memilih bahasa yang dipilih.
Bagi pelajar yang ingin belajar bahasa baharu, anda  ...
```

**光合作用是植物** (step_008129, greedy)

```
光合作用是植物性的，它的成分是由植物性的，它的成分是由植物性的，它的成分是由植物性的，它的成分是由植物性的，它的成分是由植物性的，它的成分是由植物性的，它的成分是由植物性的，
```

**北京是中国的** (step_008129, greedy)

```
北京是中国的一个小镇，在一个无处不在的丧尸已经威胁到了人类的生活的世界，
在那些美妙的日子里，在一个无处不在的丧尸已经威胁到了人类的生活的世界，
在那些美妙的日子里，在一个无处不
```

**台灣的夜市** (step_008129, greedy)

```
台灣的夜市，
這次的行程是由台北市政府推動的，
這次的行程是由台北市政府推動的，
這次的行程是由台北市政府推動的，
這次的行程是由台北市政府推動的，
這次的行程是由台北市政府推動的
```

**學習程式設計的第一步是** (step_008129, greedy)

```
學習程式設計的第一步是讓你在使用的時候，在使用的時候，你可以在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在使用的時候，在
```

**日本の四季は** (step_008129, greedy)

```
日本の四季は、日本の四季を見る限り、日本の四季を見る限り、日本の四季を見る限り、日本の四季を見る限り、日本の四季を見る限り、日本の四季を見る限り、日本の四季を見る限り、日本の四季を見る限り
```

**東京で一番有名な** (step_008129, greedy)

```
東京で一番有名な「アラフォー」の名前を紹介します。
「アラフォー」は、アラフォーと呼ばれるアラフォーの名前を紹介します。
「アラフォー」は、アラフォーと呼ばれるアラフォーの名前を紹介します。
「アラフォ
```

**한국의 전통 음식은** (step_008129, greedy)

```
한국의 전통 음식은 1990년대 초반부터 시작되었다.
1990년대 초반부터 시작된 음식은 1990년대 초반부터 시작되었다.
1990년대 초반부터 시작된 음식은 1990년대 초반부터 시작되었다.
19
```

**서울은 대한민국의** (step_008129, greedy)

```
서울은 대한민국의 100% 세계적인 인구의 10%를 차지했다.
이에 따라 100% 세계적인 인구는 100%를 차지했다.
이에 따라 100% 세계적인 인구는 100%를 차지했다.
이에 따라 10
```

**தமிழ் மொழி உலகின்** (step_008129, greedy)

```
தமிழ் மொழி உலகின் மிகப்பெரிய வரலாற்று சிறப்புமிக்க தமிழர் வாழ்வை வாழ்வதற்கான ஒரு வழி.
இலங்கை தமிழர் வாழ்வை வாழ்வதற்கான ஒரு வழி.
இலங்கை தமிழர் வாழ்வை வாழ்வதற்கான ஒரு வழி.
இலங்கை தமிழர் வாழ்வை வாழ்வதற்கான ஒரு வழி.

```

**சென்னை நகரம்** (step_008129, greedy)

```
சென்னை நகரம்.
இதுகுறித்து தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல் அறிந்ததும், தகவல்
```

**भारत की राजधानी** (step_008129, greedy)

```
भारत की राजधानी दिल्ली में 1000 से अधिक लोगों को रोजगार मिलेगा।
दिल्ली में 1000 से अधिक लोगों को रोजगार मिलेगा।
दिल्ली में 1000 से अधिक लोगों को रोजगार मिलेगा।
दिल्ली में 1000 से अधिक लोगों को रोजग
```

**प्रकाश संश्लेषण वह प्रक्रिया है** (step_008129, greedy)

```
प्रकाश संश्लेषण वह प्रक्रिया है जो आपकी सेवा के लिए एक अच्छा विकल्प है।
- आपकी सेवा के लिए एक अच्छा विकल्प है।
- आपकी सेवा के लिए एक अच्छा विकल्प है।
- आपकी सेवा के लिए एक अच्छा विकल्प है।
- आपकी सेवा के लिए एक अच्छा विकल्प है।

```

**Mera naam Rahul hai aur main** (step_008129, greedy)

```
Mera naam Rahul hai aur main 20 saal ka hoon. Main 25 saal ka hoon aur meri umar 24 saal hai. Main dikhne me bahut hi sundar hoon aur meri height 5’6 inch hai. Main dikhne me bahut hi sundar hoon aur meri height 5’6 inch hai.
Meri height 5’6 inch hai aur main dikhne me bahut hi sundar hoon. Meri height
```

**Aaj mausam bahut** (step_008129, greedy)

```
Aaj mausam bahut hi jyada badhiya hai.
Aaj ke samay me har koi apne ghar me hi rahata hai. Aaiye jante hai ki ghar me rahane ke liye kya kya karna chahiye.
Kya aap ghar me rahate hai?
Aaj ke samay me ghar me rahane ke liye kya kya karna chahiye.
Aaj ke samay me ghar me rahane ke liye
```

**Pakistan ka sab se bara shehar** (step_008129, greedy)

```
Pakistan ka sab se bara shehar hai.
Bahut se log is shehar ko dekh kar khush hain.
Bahut se log is shehar ko dekh kar khush hain.
Bahut se log is shehar ko dekh kar khush hain.
Bahut se log is shehar ko dekh kar khush hain.
Bahut se log is shehar ko dekh kar khush hain.
Bah
```

**Mujhe kitabein parhna** (step_008129, greedy)

```
Mujhe kitabein parhna hai.
- Bachon ki charcha
- Bachon ki charcha
- Bachon ki charcha
- Bachon ki charcha
- Bachon ki charcha
- Bachon ki charcha
- Bachon ki charcha
- Bachon ki charcha
- Bachon ki
```

## int4

Weight-only int4 (int4-groupwise-asym-v1, groups of 128 along the last dimension, fp16 scale + minimum per group) for the attention, shared and routed expert matrices; embedding bf16; router, norms and biases fp32. Dequantized to fp32 on load (the file is smaller; memory once loaded is not).

| file | size |
|---|---:|
| `model.safetensors` | 3,992.1 MB |
| `model-int4.safetensors` | 588.5 MB |
| `model (bf16, for comparison, not shipped)` | 1,996.0 MB |

| split | tokens | fp32 bpb | bf16 bpb | int4 bpb | int4 vs bf16 |
|---|---:|---:|---:|---:|---:|
| English | 32,768 | 0.9639 | 0.9639 | 0.9867 | +0.0228 (+2.37%) |
| Indonesian | 32,768 | 1.0517 | 1.0518 | 1.0767 | +0.0249 (+2.36%) |
| Malay | 32,768 | 1.1122 | 1.1121 | 1.1387 | +0.0266 (+2.39%) |
| Chinese (Simplified) | 32,768 | 1.8677 | 1.8680 | 1.9148 | +0.0468 (+2.51%) |
| Chinese (Traditional) | 32,768 | 1.6989 | 1.6989 | 1.7464 | +0.0474 (+2.79%) |
| Japanese | 32,768 | 1.2966 | 1.2967 | 1.3297 | +0.0330 (+2.54%) |
| Korean | 32,768 | 1.2515 | 1.2514 | 1.2859 | +0.0345 (+2.75%) |
| Tamil | 32,768 | 0.5066 | 0.5066 | 0.5187 | +0.0121 (+2.39%) |
| Hindi (Devanagari) | 32,768 | 0.5447 | 0.5446 | 0.5603 | +0.0157 (+2.88%) |
| Hindi (romanised) | 32,768 | 1.1780 | 1.1779 | 1.2057 | +0.0278 (+2.36%) |
| Urdu (romanised) | 32,768 | 1.5758 | 1.5758 | 1.6127 | +0.0369 (+2.34%) |
| Code | 32,768 | 0.4782 | 0.4782 | 0.4959 | +0.0176 (+3.68%) |

The first tokens of each evaluation split (count per row). bf16 = the weights rounded to bf16, arithmetic in fp32 (spec 12's baseline); fp32 = the trained weights as saved.

Standalone-loader parity (max |logit difference| against the training code): final (fp32) 1.5e-05; milestone step_008129 (bf16) 2.3e-05; int4 (dequantized) 1.2e-05.

Stepbuild score, int4 vs bf16: _not yet measured_ (needs the chat/step fine-tune).

## Usage

```bash
pip install torch safetensors tokenizers huggingface_hub
```

```python
from huggingface_hub import hf_hub_download
import importlib.util, sys

path = hf_hub_download("AneekC/quipu-moe-1B-A149M", "modeling_quipu_moe.py")
spec = importlib.util.spec_from_file_location("modeling_quipu_moe", path)
mq = importlib.util.module_from_spec(spec)
sys.modules["modeling_quipu_moe"] = mq
spec.loader.exec_module(mq)

model = mq.load("AneekC/quipu-moe-1B-A149M")                                    # fp32
# model = mq.load("AneekC/quipu-moe-1B-A149M", weights="model-int4.safetensors")  # int4 file
tok = mq.load_tokenizer("AneekC/quipu-moe-1B-A149M")
print(mq.generate(model, tok, "def fibonacci(n):", max_new_tokens=60))
```

This is not a `transformers` model; there is no `AutoModel` class for it. The loader
runs the experts one after another without a KV cache: correct, not fast.

## Limitations

- Small: 148,660,992 parameters are active per token. It states false things
  with confidence; do not use its output as information.
- The nine languages other than English together are 12.0% of the training tokens (English 28.0%, code 60.0%; shard manifest, mix achieved). Expect weaker output in them than in English, and some mixing of languages; the bits per byte above show how much weaker, per language.
- Code correctness: _not yet measured_ (HumanEval / MBPP above); treat generated code as untested.
- Expert specialisation by programming language (Python vs JavaScript / JSX, spec 7) was not measured: the code validation split carries no per-document language label, so code is one split in the expert-usage tables.
- Trained on web text and public code, which carry their biases; no safety tuning.


## Credits and licence

Weights and code: Apache-2.0. Language identification of the training text used
[AneekC/lid-specialists-9plus1](https://huggingface.co/AneekC/lid-specialists-9plus1) (MIT). Training data: FineWeb-Edu
and FineWeb-2 (ODC-By 1.0, © Hugging Face) and the permissively licensed subset of
codeparrot/github-code-clean (files keep their licences). HumanEval
(MIT) and MBPP (CC-BY-4.0) were used for evaluation only and filtered (substring /
13-gram matching) from the training data.
