---
license: apache-2.0
base_model: xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic
base_model_relation: quantized
pipeline_tag: image-text-to-text
library_name: gguf
language: [en, zh, ko, ja, es, ru]
tags: [gguf, rocmfpx, amd, vulkan, strix-halo, quantized, qwen3.5, deepseek, reasoning, vision-language, abliterated, uncensored, heretic]
---

# DeepSeek-V4-Pro-Qwen3.5-9B Uncensored (heretic), ROCmFPX GGUF

Quantized files of [xtools-at's decensored DeepSeek-V4-Pro-Qwen3.5-9B](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic),
a 9B vision-language reasoning model. The original, by [Jackrong](https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B),
is a Qwen3.5-9B fine-tune distilled from DeepSeek-V4-Pro responses, focused on mathematics and STEM.

> **Warning: safety training has been removed from this model.** The Heretic process removes its refusal behaviour, so
> it can comply with harmful, unethical, offensive or illegal requests. You are fully responsible for how you use it and
> for what it generates, and you must follow the law that applies to you. Do not put it in front of end users without
> your own safety and moderation layers. Its outputs do not reflect the views of the uploader or of the original authors.

> **These files have not been tested on AMD hardware yet.** Please report speed and quality in the Community tab.
>
> The 8-bit file needs [HarshaVardhan3002/ROCmFPX](https://github.com/HarshaVardhan3002/ROCmFPX), built from 7 November
> 2026 or later. Stock llama.cpp, LM Studio, Ollama and older ROCmFPX builds will not load it. All files here were only
> tested with that fork.
>
> Not an official release. All credit for the model goes to Jackrong and the Qwen team, and for the decensoring to xtools-at.

## Files

| File | Size | KL to BF16 | Same top token | |
|---|---:|---:|---:|---|
| `DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q8_0_ROCMFPX.gguf` | 9.6 GB | 0.00018 | 99.3% | 8-bit, start here |
| `DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-Q6_K.gguf` | 7.6 GB | 0.0019 | 97.8% | 6-bit, standard llama.cpp weight type |
| `mmproj-DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic-F16.gguf` | 0.9 GB | | | vision encoder, needed for images |

For comparison, measured the same way:

| Not published | Size | KL to BF16 | Same top token |
|---|---:|---:|---:|
| Stock Q8_0 | 9.9 GB | 0.00026 | 99.2% |
| ROCmFPX Q6 | 7.6 GB | 0.0020 | 97.7% |
| Stock Q4_K_M | 5.8 GB | 0.014 | 94.4% |

The ROCmFPX 8-bit file is closer to BF16 than a stock Q8_0 and smaller. At 6-bit, the stock type was slightly closer than
ROCmFPX at the same size, so the stock type is the one here. For 4-bit, use stock files from other uploaders.

**How this was measured:** llama.cpp `llama-perplexity --kl-divergence` against a BF16 GGUF converted from xtools-at's
weights (perplexity 7.13), 40 chunks of 512 tokens of English Wikipedia text (wikitext-2), on an NVIDIA GB10 GPU after
expanding each file to F16. KL is how far the file's next-token probabilities drift from BF16, averaged over every token;
lower is better. This is general English text, not mathematics or reasoning, so it says nothing direct about the STEM benchmarks on the original card.

Short checks on the published files, on CPU with greedy decoding:

- Text: both answered "What is the capital of France?" correctly after the thinking block, and gave 17 x 23 = 391 and Canberra as Australia's capital.
- Vision: both described a test image of a fox figurine correctly, and the 8-bit file also a bicycle helmet.
- Refusals: 0 of 10 requests that a safety-trained model would normally refuse, and 0 of 8 harmless questions that only
  sound risky, on both files and on the BF16 source. This small test looks for refusal phrases in the first 64 tokens.
  It shows quantization did not bring refusals back. It is not a measure of how useful or accurate the answers are.

The files contain the model's one-layer multi-token prediction (MTP) head, which was not tested.

## Credits and license

- Original model: [Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B](https://huggingface.co/Jackrong/DeepSeek-V4-Pro-Qwen3.5-9B), Apache-2.0.
- Decensored version: [xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic](https://huggingface.co/xtools-at/DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic), made with Heretic.

Apache-2.0. See `LICENSE`.
