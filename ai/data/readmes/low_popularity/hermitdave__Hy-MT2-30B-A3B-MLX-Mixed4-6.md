---
language:
  - en
  - zh
  - ja
  - ko
  - es
  - fr
  - de
  - ru
  - ar
  - pt
  - it
  - tr
  - vi
  - th
  - id
  - ms
  - tl
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
license: other
license_name: tencent-hy-community
license_link: https://huggingface.co/tencent/Hy-MT2-30B-A3B
base_model: tencent/Hy-MT2-30B-A3B
tags:
  - mlx
  - apple-silicon
  - translation
  - moe
  - mixed-precision
  - quantized
pipeline_tag: translation
library_name: mlx-lm
---

# Hy-MT2-30B-A3B-MLX-Mixed4-6

Mixed-precision MLX conversion of [tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B) using the `mixed_4_6` quantization recipe. Most layers run at 4-bit; sensitive layers (first 1/8, last 1/8, every third middle layer, value projections, down projections, and the language model head) are bumped to 6-bit.

4.830 bits per weight, 17 GB total, 30.6 tok/s on M5 Max 128 GB.

## Quick Start

### Python

```python
from mlx_lm import load, stream_generate
from mlx_lm.sample_utils import make_sampler

model, tokenizer = load("hermitdave/Hy-MT2-30B-A3B-MLX-Mixed4-6")

prompt = "Translate the following text into English. Note that you should only output the translated result without any additional explanation:\n\n오늘 날씨가 정말 좋네요."
messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_dict=False)

sampler = make_sampler(temp=0.7, top_p=1.0, top_k=0)
for response in stream_generate(model, tokenizer, prompt=prompt, max_tokens=4096, sampler=sampler):
    print(response.text, end="", flush=True)
```

### Server

```bash
mlx_lm.server --model hermitdave/Hy-MT2-30B-A3B-MLX-Mixed4-6 --port 8080 --trust-remote-code
```

### Recommended Parameters

```json
{
  "temperature": 0.7,
  "top_p": 1.0,
  "top_k": -1,
  "repetition_penalty": 1.0,
  "max_tokens": 4096
}
```

## Benchmarks

All four variants tested on the same M5 Max 128 GB machine with identical prompts. Sustained decode speed averaged across three prompts (short KO→EN, short ZH→EN, long KO→EN paragraph).

### Speed and Size

| Variant | Size | Load Time | Avg Speed |
|---------|------|-----------|-----------|
| Mixed 2-6 | 11.87 GB | 2.38s | 35.7 tok/s |
| Mixed 4-6 | 17 GB | 3.36s | 30.6 tok/s |
| Q4 | ~16 GB | 3.14s | 32.7 tok/s |
| Q8 | ~50 GB | 8.04s | 22.7 tok/s |

Mixed 4-6 sits between Mixed 2-6 and Q4 in speed. The larger model size means more data to load per layer, but it's still faster than Q8. Interestingly, Q4 edges it out slightly on raw throughput despite similar size — the uniform 4-bit format may be more efficient on Apple Silicon's memory subsystem than mixed 4/6-bit.

### Quality

I ran the same translation prompts through all four variants and compared the outputs.

**Short translations (single sentences):**

| Prompt | Mixed 2-6 | Mixed 4-6 | Q4 | Q8 |
|--------|-----------|-----------|-----|-----|
| 오늘 날씨가 정말 좋네요. | "The weather today is truly wonderful." | "The weather is really nice today." | "The weather is really nice today." | "The weather is really nice today." |
| 今天天气真好。 | "The weather today is really lovely." | "The weather is really nice today." | "The weather is really nice today." | "The weather is really nice today." |

Mixed 2-6 uses different wording ("truly wonderful", "really lovely") while Mixed 4-6 matches Q4 and Q8 almost exactly. If you want the output to feel closer to the higher-bit variants, Mixed 4-6 is the one to pick.

**Long translation (paragraph about AI technology):**

Mixed 4-6:
> "The development of artificial intelligence technology has brought about many changes in our society. In particular, innovations in the field of natural language processing have significantly improved the quality of machine translation, which plays a crucial role in international communication and business."

Q4:
> "The development of artificial intelligence technology has brought about many changes in our society. In particular, innovations in the field of natural language processing have significantly improved the quality of machine translation, which plays a crucial role in international exchanges and business."

Q8:
> "The development of artificial intelligence technology has brought many changes to our society. In particular, innovations in the field of natural language processing have significantly improved the quality of machine translation, which plays a vital role in international exchange and business."

Mixed 4-6 matches Q4 nearly word-for-word with only tiny variations ("communication" vs "exchanges"). Compare that to Mixed 2-6, which started drifting: *"Particularly, the natural processing of language has led to a significant improvement... which in turn plays a major role in the development of language processing techniques."* — that last sentence circles back on itself in a way the higher-bit variants don't.

### The Trade-off

**Pick Mixed 2-6 if:** You want maximum speed and minimum size, and you're translating sentences or short paragraphs. For chat-like or short-form translation it works well.

**Pick Mixed 4-6 if:** You want output that closely matches Q4/Q8 quality while still saving ~13 GB over Q8. The sweet spot for mixed-precision quantization on this model.

**Pick Q4 if:** You want slightly faster throughput than Mixed 4-6 and don't mind the quality gap on longer text. Best for batch processing where raw speed matters.

**Pick Q8 if:** You want the best quality and don't care about size. For production systems translating long documents, this is the safe choice.

Honestly, Mixed 4-6 impressed me. The quality difference between it and Q4 is negligible in practice, and you get a 50 GB model down to 17 GB. That's a meaningful win for anyone running this locally.

## Quantization

The `mixed_4_6` recipe assigns different bit-widths per layer group, following the same logic as llama.cpp's `Q4_K_M`.

### Bit Allocation

| Component | Bits | Layers |
|-----------|------|--------|
| q_proj, k_proj, o_proj | 4 | All |
| gate_proj, up_proj (MoE) | 4 | All |
| Shared MLP | 4 | All |
| v_proj | 6 | First 1/8, last 1/8, every 3rd middle |
| down_proj | 6 | First 1/8, last 1/8, every 3rd middle |
| lm_head | 6 | Output layer |

Interactive visualization: [quantization_diagram.html](./quantization_diagram.html)

## Conversion

Converted using `mlx-lm 0.31.3` with a custom `hy_v3` adapter (MLX-LM doesn't yet include native `hy_v3` support). The adapter was sourced from [QwQbb](https://huggingface.co/QwQbb/Hy-MT2-30B-A3B-MLX-8bit).

Process:
1. Load base model in bfloat16
2. Cast all float params to bfloat16
3. Apply `mixed_4_6` quant predicate
4. Save as MLX safetensors

## Hardware

| Mac | Memory | Status |
|-----|--------|--------|
| M4/M5 Max | 128 GB | Comfortable |
| M4 Pro | 32 GB | Tight |
| Base M4 | 16 GB | Won't fit |

32 GB minimum recommended.

## Languages

Hy-MT2 supports translation among 33 languages. See the [base model card](https://huggingface.co/tencent/Hy-MT2-30B-A3B) for the full list.

## License

Licensed under the [Tencent HY Community License Agreement](https://huggingface.co/tencent/Hy-MT2-30B-A3B). Does not apply in the European Union.

## Attribution

- Base model: [tencent/Hy-MT2-30B-A3B](https://huggingface.co/tencent/Hy-MT2-30B-A3B)
- hy_v3 adapter: [QwQbb/Hy-MT2-30B-A3B-MLX-8bit](https://huggingface.co/QwQbb/Hy-MT2-30B-A3B-MLX-8bit)
- Conversion tool: [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm)
- Benchmarking and conversion: Hermes Agent (research-bot profile)
- Paper: [Hy-MT2: A Family of Fast, Efficient and Powerful Multilingual Translation Models in the Wild](https://arxiv.org/abs/2605.22064)

```bibtex
@misc{zheng2026hymt2familyfastefficient,
      title={Hy-MT2: A Family of Fast, Efficient and Powerful Multilingual Translation Models in the Wild},
      author={Mao Zheng and Zheng Li and Tao Chen and Bo Lv and Mingrui Sun and Mingyang Song and Jinlong Song and Hong Huang and Decheng Wu and Hai Wang and Yifan Song and Yanfeng Chen and Guanwei Zhang},
      year={2026},
      eprint={2605.22064},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.22064},
}
```

## Notes

- Community conversion, not an official Tencent release.
- The `hy_v3.py` adapter is included and loaded via `trust-remote-code`. Inspect it before running if you have concerns.
- Also available: [Mixed 2-6 variant](https://huggingface.co/hermitdave/Hy-MT2-30B-A3B-MLX-Mixed2-6) for maximum speed, or [Q4](https://huggingface.co/QwQbb/Hy-MT2-30B-A3B-MLX-4bit) and [Q8](https://huggingface.co/QwQbb/Hy-MT2-30B-A3B-MLX-8bit) from the community.
