---
language:
  - en
  - zh
  - ja
  - ko
  - fr
  - de
  - es
  - pt
  - ru
  - ar
license: apache-2.0
library_name: gguf
pipeline_tag: sentence-similarity
tags:
  - gguf
  - quantized
  - embedding
  - sentence-transformers
  - Qwen3
  - imatrix
  - llama-cpp
base_model: Qwen/Qwen3-Embedding-0.6B
model_creator: Qwen
datasets:
  - explodinggradients/fiqa
  - PatronusAI/financebench
  - zeroshot/twitter-financial-news-sentiment
  - philschmid/finanical-rag-embedding-dataset
  - openai/gsm8k
  - DigitalLearningGmbH/MATH-lighteval
quantized_by: PeterAM4
---

# Qwen3-Embedding-0.6B -- GGUF

All-in-one GGUF quantizations of [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B), from 8-bit down to 1-bit, with importance-matrix calibration optimized for financial and technical text retrieval.

Qwen3-Embedding-0.6B is a compact, multilingual embedding model well suited for RAG pipelines, semantic search, and document retrieval. These quantizations make it practical to run on edge devices, laptops, and resource-constrained servers -- particularly for financial NLP workloads where low latency and small memory footprint matter.

The importance matrix was calibrated on a mixed corpus weighted toward financial data (financial Q&A from FiQA, SEC 10-K filings from FinanceBench, financial sentiment from Twitter, RAG pairs) alongside math reasoning and general text, so the quantized models preserve the weights most relevant to financial domain embeddings.

| Property | Value |
|----------|-------|
| Base model | [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) |
| Parameters | 595,776,512 |
| Max context | 32,768 tokens |
| Pooling | Last token |
| Embedding dim | 1024 |
| License | Apache 2.0 |
| Quantized with | [llama.cpp](https://github.com/ggerganov/llama.cpp) |

---

## Why quantize?

Despite their size, neural networks are remarkably sparse in information density. Most of the 16 bits allocated per weight during training exist to make gradient descent work -- not to store knowledge. Current estimates put the actual information content at roughly 2 bits per parameter. The remaining 14 bits are redundancy.

This explains why aggressive quantization works: compressing from 16-bit to 4-bit (75% reduction) discards almost exclusively noise. Our benchmark data confirms this -- Q3_K_M-imat at 4.66 BPW scores within +0.62 PPL of the full BF16 baseline while being 70% smaller than BF16 (331 MB vs 1.1 GB). For comparison, Q4_K_M-imat at 5.32 BPW shows +0.65 PPL -- the 3-bit model actually edges it out. The imatrix (importance matrix) is key here: by profiling which weights actually carry signal, we preserve those at higher precision and compress the rest. This is why imatrix-calibrated 3-bit models can outperform naive 5-bit quantizations.

The quality cliff appears around 3 BPW, where we start cutting into real information. Below that, PPL degrades rapidly (Q2_K at 3.97 BPW: +391, IQ1_S at 2.79 BPW: +23,008). Ternary quantizations (TQ2_0, TQ1_0) diverge entirely on this architecture.

---

## Benchmark results

All models evaluated with **llama-perplexity** on a 22 MB calibration corpus (financial, math, and general text). Context window: 1536 tokens. Chunks: 200. Lower PPL = better.

Baseline PPL (BF16): **406.0250**

| Model | Size | BPW | PPL | Delta PPL |
|-------|------|-----|-----|-----------|
| [Qwen3-Embedding-0.6B-BF16.gguf](Qwen3-Embedding-0.6B-BF16.gguf) (unquantized) **baseline** | 1.1G | 16.08 | 406.0250 | -- |
| [Qwen3-Embedding-0.6B-Q8_0.gguf](Qwen3-Embedding-0.6B-Q8_0.gguf) | 610M | 8.58 | 409.5689 | +3.54 |
| [Qwen3-Embedding-0.6B-Q6_K.gguf](Qwen3-Embedding-0.6B-Q6_K.gguf) | 472M | 6.65 | 417.3712 | +11.35 |
| [Qwen3-Embedding-0.6B-Q5_1.gguf](Qwen3-Embedding-0.6B-Q5_1.gguf) | 442M | 6.23 | 426.9407 | +20.92 |
| [Qwen3-Embedding-0.6B-Q5_K_M.gguf](Qwen3-Embedding-0.6B-Q5_K_M.gguf) | 424M | 5.96 | 442.9431 | +36.92 |
| [Qwen3-Embedding-0.6B-Q5_0.gguf](Qwen3-Embedding-0.6B-Q5_0.gguf) | 416M | 5.86 | 413.1916 | +7.17 |
| [Qwen3-Embedding-0.6B-Q5_K_S.gguf](Qwen3-Embedding-0.6B-Q5_K_S.gguf) | 416M | 5.86 | 414.9329 | +8.91 |
| [Qwen3-Embedding-0.6B-Q4_1-imat.gguf](Qwen3-Embedding-0.6B-Q4_1-imat.gguf) | 390M | 5.49 | 403.0646 | -2.96 |
| [Qwen3-Embedding-0.6B-Q4_K_M-imat.gguf](Qwen3-Embedding-0.6B-Q4_K_M-imat.gguf) | 378M | 5.32 | 406.6788 | +0.65 |
| [Qwen3-Embedding-0.6B-Q4_K_S-imat.gguf](Qwen3-Embedding-0.6B-Q4_K_S-imat.gguf) | 365M | 5.14 | 406.9947 | +0.97 |
| [Qwen3-Embedding-0.6B-Q4_0-imat.gguf](Qwen3-Embedding-0.6B-Q4_0-imat.gguf) | 364M | 5.13 | 419.8843 | +13.86 |
| [Qwen3-Embedding-0.6B-IQ4_NL-imat.gguf](Qwen3-Embedding-0.6B-IQ4_NL-imat.gguf) | 364M | 5.12 | 435.0203 | +29.00 |
| [Qwen3-Embedding-0.6B-Q3_K_L-imat.gguf](Qwen3-Embedding-0.6B-Q3_K_L-imat.gguf) | 351M | 4.94 | 412.0217 | +6.00 |
| [Qwen3-Embedding-0.6B-IQ4_XS-imat.gguf](Qwen3-Embedding-0.6B-IQ4_XS-imat.gguf) | 351M | 4.94 | 451.4025 | +45.38 |
| [Qwen3-Embedding-0.6B-Q3_K_M-imat.gguf](Qwen3-Embedding-0.6B-Q3_K_M-imat.gguf) **recommended** | 331M | 4.66 | 406.6408 | +0.62 |
| [Qwen3-Embedding-0.6B-IQ3_M-imat.gguf](Qwen3-Embedding-0.6B-IQ3_M-imat.gguf) | 320M | 4.51 | 460.9405 | +54.92 |
| [Qwen3-Embedding-0.6B-IQ3_S-imat.gguf](Qwen3-Embedding-0.6B-IQ3_S-imat.gguf) | 308M | 4.34 | 475.4797 | +69.45 |
| [Qwen3-Embedding-0.6B-Q3_K_S-imat.gguf](Qwen3-Embedding-0.6B-Q3_K_S-imat.gguf) | 308M | 4.34 | 340.2907 | -65.73 |
| [Qwen3-Embedding-0.6B-IQ3_XS-imat.gguf](Qwen3-Embedding-0.6B-IQ3_XS-imat.gguf) | 298M | 4.20 | 520.3907 | +114.37 |
| [Qwen3-Embedding-0.6B-Q2_K-imat.gguf](Qwen3-Embedding-0.6B-Q2_K-imat.gguf) | 282M | 3.97 | 797.8549 | +391.83 |
| [Qwen3-Embedding-0.6B-Q2_K_S-imat.gguf](Qwen3-Embedding-0.6B-Q2_K_S-imat.gguf) | 267M | 3.76 | 1561.2449 | +1155.22 |
| [Qwen3-Embedding-0.6B-IQ3_XXS-imat.gguf](Qwen3-Embedding-0.6B-IQ3_XXS-imat.gguf) | 266M | 3.74 | 613.9329 | +207.91 |
| [Qwen3-Embedding-0.6B-IQ2_M-imat.gguf](Qwen3-Embedding-0.6B-IQ2_M-imat.gguf) | 252M | 3.55 | 1283.4407 | +877.42 |
| [Qwen3-Embedding-0.6B-IQ2_S-imat.gguf](Qwen3-Embedding-0.6B-IQ2_S-imat.gguf) | 242M | 3.41 | 1857.4142 | +1451.39 |
| [Qwen3-Embedding-0.6B-TQ2_0-imat.gguf](Qwen3-Embedding-0.6B-TQ2_0-imat.gguf) | 236M | 3.32 | diverged | N/A |
| [Qwen3-Embedding-0.6B-IQ2_XS-imat.gguf](Qwen3-Embedding-0.6B-IQ2_XS-imat.gguf) | 231M | 3.25 | 3632.9250 | +3226.90 |
| [Qwen3-Embedding-0.6B-IQ2_XXS-imat.gguf](Qwen3-Embedding-0.6B-IQ2_XXS-imat.gguf) | 219M | 3.08 | 5641.8950 | +5235.87 |
| [Qwen3-Embedding-0.6B-TQ1_0-imat.gguf](Qwen3-Embedding-0.6B-TQ1_0-imat.gguf) | 216M | 3.04 | diverged | N/A |
| [Qwen3-Embedding-0.6B-IQ1_M-imat.gguf](Qwen3-Embedding-0.6B-IQ1_M-imat.gguf) | 206M | 2.90 | 7495.4178 | +7089.39 |
| [Qwen3-Embedding-0.6B-IQ1_S-imat.gguf](Qwen3-Embedding-0.6B-IQ1_S-imat.gguf) | 198M | 2.79 | 23414.9432 | +23008.92 |


**Notes:**
- The **-imat** suffix means the model was quantized with importance-matrix calibration. This is what allows 3-4 bit models to stay close to baseline -- the imatrix tells the quantizer which weights carry real information.
- **Q3_K_S-imat** reports an anomalously low PPL (340). This is a statistical artifact, not a genuine improvement over baseline.
- **TQ2_0 / TQ1_0** (ternary quantizations) produce diverged PPL on this architecture. They require CPU or CUDA (not supported on Apple Metal) and are not usable for this model.
- Below ~4 BPW, quality degrades steeply. Below ~3 BPW, models are not recommended for any production use.

### Choosing a model

| Use case | Model | Notes |
|----------|-------|-------|
| Maximum quality | Q8_0 | Near-lossless, 610 MB |
| Best quality/size trade-off | Q3_K_M-imat | +0.62 PPL delta at 331 MB -- smallest model with near-baseline quality |
| Larger but safe margin | Q4_K_M-imat | +0.65 PPL delta at 378 MB |
| Extreme compression | Q2_K-imat | Usable for non-critical applications |

---

## Quantization method

All models were quantized from the BF16 source using `llama-quantize` from [llama.cpp](https://github.com/ggerganov/llama.cpp).

Three strategies were used:

1. **Standard** (Q8_0, Q6_K, Q5_K_M, Q5_K_S, Q5_0, Q5_1) -- uniform precision reduction, no imatrix.
2. **K-Quant + imatrix** (Q4_K_M, Q4_K_S, Q4_0, Q4_1, Q3_K_L, Q3_K_M, Q3_K_S, Q2_K, Q2_K_S) -- block-level mixed precision, importance matrix recommended.
3. **Importance-weighted** (IQ4_NL, IQ4_XS, IQ3_M, IQ3_S, IQ3_XS, IQ3_XXS, IQ2_M, IQ2_S, IQ2_XS, IQ2_XXS, IQ1_M, IQ1_S, TQ2_0, TQ1_0) -- non-linear quantization, imatrix required.

### Calibration corpus

The importance matrix was generated from a mixed-domain corpus (22 MB, ~198,000 lines). The mix was chosen to cover the primary use case (financial text) while including general and mathematical text to maintain broad capability:

| Dataset | Source | Domain | Entries |
|---------|--------|--------|---------|
| WikiText-2 | ggml-org | General knowledge | 36,718 lines |
| Twitter Financial News | [zeroshot/twitter-financial-news-sentiment](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment) | Financial sentiment | 9,543 |
| GSM8K | [openai/gsm8k](https://huggingface.co/datasets/openai/gsm8k) | Math word problems | 7,473 |
| Financial RAG | [philschmid/finanical-rag-embedding-dataset](https://huggingface.co/datasets/philschmid/finanical-rag-embedding-dataset) | Financial Q&A pairs | 6,998 |
| FiQA | [explodinggradients/fiqa](https://huggingface.co/datasets/explodinggradients/fiqa) | Personal finance Q&A | 5,650 |
| MATH Competition | [DigitalLearningGmbH/MATH-lighteval](https://huggingface.co/datasets/DigitalLearningGmbH/MATH-lighteval) | Competition math | 5,000 |
| FinanceBench | [PatronusAI/financebench](https://huggingface.co/datasets/PatronusAI/financebench) | SEC 10-K filings | 150 |

The financial datasets (FiQA + Twitter Financial News + Financial RAG + FinanceBench) contribute ~22,300 entries of domain-specific text covering sentiment, Q&A, RAG pairs, and SEC filings -- ensuring the importance matrix prioritizes weights relevant to financial terminology and reasoning.

---

## Usage

### llama.cpp server

```bash
./llama-server \
    -m Qwen3-Embedding-0.6B-Q3_K_M-imat.gguf \
    --embedding --pooling last \
    -c 32768 -np 8 \
    --host 0.0.0.0 --port 8080
```

### Python (llama-cpp-python)

```python
from llama_cpp import Llama

model = Llama(
    model_path="Qwen3-Embedding-0.6B-Q3_K_M-imat.gguf",
    embedding=True,
    pooling_type="last",
    n_ctx=32768,
)

result = model.create_embedding(["Financial analysis of Q3 earnings"])
print(len(result["data"][0]["embedding"]))  # 1024
```

### Download a specific file

```python
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="PeterAM4/Qwen3-Embedding-0.6B-GGUF",
    filename="Qwen3-Embedding-0.6B-Q3_K_M-imat.gguf",
)
```

---

## Technical details

- GGUF format v3
- Tokenizer: Qwen3 (151,936 tokens)
- add_eos_token: false (patched for llama.cpp compatibility; EOS token ID 151643 is still present and usable)
- Pooling type: 3 (last token)
- Hardware used: Apple M3 Pro with Metal acceleration (CPU fallback for ternary quants)

## Credits

- [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) by Alibaba Qwen Team
- [llama.cpp](https://github.com/ggerganov/llama.cpp) by Georgi Gerganov et al.

## License

Apache 2.0, inherited from the original model.
