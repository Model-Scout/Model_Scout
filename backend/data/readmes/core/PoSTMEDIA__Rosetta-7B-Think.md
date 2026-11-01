---
license: apache-2.0
language:
  - ko
  - en
pipeline_tag: text-generation
library_name: transformers
base_model: PoSTMEDIA/Rosetta-7B-Base
tags:
  - rosetta
  - korean
  - bilingual
  - reasoning
  - postmedia
---

<div align="center">

# Rosetta-7B-Think

[![Collection](https://img.shields.io/badge/Rosetta-Collection-0052CC?style=for-the-badge)](https://huggingface.co/collections/PoSTMEDIA/rosetta-6a9db30fd1b4585b0c1845e9)
[![vLLM](https://img.shields.io/badge/vLLM-PoSTMEDIA--AI-00A3FF?style=for-the-badge&logo=github)](https://github.com/PoSTMEDIA-AI/vllm)
[![License](https://img.shields.io/badge/License-Apache_2.0-7856FF?style=for-the-badge)](./LICENSE)

</div>

## Introduction

**Rosetta-7B-Think** is a 7B-parameter bilingual (Korean-English) reasoning model developed by **PoSTMEDIA**. Built on PoSTMEDIA's **Rosetta** dense decoder-only architecture and post-trained from [Rosetta-7B-Base](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Base) with large-scale supervised fine-tuning on long-form reasoning traces, it generates an explicit reasoning trace wrapped in `<think> ... </think>` before committing to a final answer.

Where most compact reasoning models concentrate their gains in English math, Rosetta-7B-Think was trained to reason **in and about Korean**: under our unified protocol it surpasses Qwen3-8B on Korean math reasoning (HRM8K) and Korean comprehension (HAE-RAE) — while critically, unlike several global reasoning models, it reliably terminates its reasoning on Korean inputs.

| Model | Download | Note |
|---|---|---|
| Rosetta-7B-Base | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Base) | Foundation model (completion-style) |
| Rosetta-7B-Instruct | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct) | Instruction following / chat |
| Rosetta-7B-Instruct-NVFP4 | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct-NVFP4) | NVFP4 4-bit of Instruct (NVIDIA Blackwell / DGX Spark) |
| **Rosetta-7B-Think** | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Think) | Explicit reasoning (`<think>`) *(this model)* |
| Rosetta-7B-Think-NVFP4 | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Think-NVFP4) | NVFP4 4-bit of Think (NVIDIA Blackwell / DGX Spark) |

## Highlights

- **Explicit reasoning** — structured `<think>` traces with reliable termination in both Korean and English
- **Korean math reasoning** — HRM8K **64.3**, above Qwen3-8B under the identical protocol
- **Korean comprehension** — HAE-RAE **62.7**, above Qwen3-8B under the identical protocol
- **Competition math from a 7B** — AIME24 **36.7** / AIME25 **33.3**, a large step up from same-size non-reasoning models
- **Grade-school math** — GSM8K **83.5** with fully traceable step-by-step reasoning
- **65,536-token context window** — headroom for long reasoning traces
- **Apache-2.0** — unrestricted commercial use

## Model Summary

<div align="center">
<table><tbody>
<tr><td><b>Architecture</b></td><td>Rosetta dense decoder-only Transformer (<code>RosettaForCausalLM</code>)</td></tr>
<tr><td><b>Parameters</b></td><td>7B</td></tr>
<tr><td><b>Layers</b></td><td>32</td></tr>
<tr><td><b>Hidden size</b></td><td>4,096</td></tr>
<tr><td><b>Attention heads</b></td><td>32</td></tr>
<tr><td><b>Attention pattern</b></td><td>interleaved sliding-window (4,096) + global, 3:1, with QK-normalization</td></tr>
<tr><td><b>Context length</b></td><td>65,536</td></tr>
<tr><td><b>Vocabulary</b></td><td>161,425 (Korean-extended)</td></tr>
<tr><td><b>Post-training</b></td><td>large-scale reasoning SFT (long-form reasoning traces)</td></tr>
<tr><td><b>Reasoning format</b></td><td><code>&lt;think&gt; ... &lt;/think&gt;</code> + final answer</td></tr>
<tr><td><b>License</b></td><td>Apache-2.0</td></tr>
</tbody></table>
</div>

## Training Overview

1. **Pretraining** on trillions of tokens of curated bilingual web, code, and academic text
2. **Staged mid-training** for reasoning-dense data and long-context extension up to 65K
3. **Korean continual pretraining** on curated Korean corpora plus in-house synthetic Korean data assets (161K extended vocabulary)
4. **Reasoning post-training** — large-scale SFT on long-form reasoning traces across math, code, science, and Korean-language tasks

## Evaluation Results

All models in the table below, **including competitors, were re-evaluated in-house under an identical protocol** (lm-evaluation-harness + vLLM ≥ 0.26). Reasoning models are sampled at `temperature 0.6, top-p 0.95` with a 32,768-token generation budget for competition math.

<!-- prettier-ignore -->
<table>
  <tr>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">Benchmark</th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;"><b>Rosetta-7B-Think</b><br><sup>7B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">Qwen3-8B<br><sup>8B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">DeepSeek-R1-0528<br><sup>8B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">HyperCLOVAX-Think<br><sup>14B</sup></th>
  </tr>
  <tr>
    <td align="center" colspan="5" style="background: linear-gradient(90deg, rgba(0,82,204,0.30) 0%, rgba(0,163,255,0.30) 50%, rgba(120,86,255,0.30) 100%); font-weight: bold; height: 32px; padding-top: 2px; padding-bottom: 2px;"><i>Reasoning &amp; Mathematics</i></td>
  </tr>
  <tr><td>MMLU (0-shot CoT)</td><td align="center">67.1</td><td align="center">79.5</td><td align="center"><b>80.4</b></td><td align="center">77.7</td></tr>
  <tr><td>GSM8K</td><td align="center">83.5</td><td align="center"><b>90.1</b></td><td align="center">88.2</td><td align="center">79.2</td></tr>
  <tr><td>AIME 2024<sup>&#8225;</sup></td><td align="center">36.7</td><td align="center"><b>70.0</b></td><td align="center">66.7</td><td align="center">46.7</td></tr>
  <tr><td>AIME 2025<sup>&#8225;</sup></td><td align="center">33.3</td><td align="center">66.7</td><td align="center"><b>70.0</b></td><td align="center">43.3</td></tr>
  <tr>
    <td align="center" colspan="5" style="background: linear-gradient(90deg, rgba(0,82,204,0.30) 0%, rgba(0,163,255,0.30) 50%, rgba(120,86,255,0.30) 100%); font-weight: bold; height: 32px; padding-top: 2px; padding-bottom: 2px;"><i>Korean Language &amp; Knowledge</i></td>
  </tr>
  <tr><td>KMMLU</td><td align="center">47.4</td><td align="center"><b>58.8</b></td><td align="center">21.9<sup>&sect;</sup></td><td align="center">54.7</td></tr>
  <tr><td>CLIcK</td><td align="center">54.5</td><td align="center">63.8</td><td align="center">19.8<sup>&sect;</sup></td><td align="center"><b>69.9</b></td></tr>
  <tr><td>HAE-RAE</td><td align="center">62.7</td><td align="center">60.0</td><td align="center">20.9<sup>&sect;</sup></td><td align="center"><b>81.3</b></td></tr>
  <tr><td>HRM8K</td><td align="center"><b>64.3</b></td><td align="center">62.3</td><td align="center">17.4<sup>&sect;</sup></td><td align="center">54.4</td></tr>
  <tr><td>KoSimpleQA<sup>&dagger;</sup></td><td align="center">48.2</td><td align="center"><b>74.2</b></td><td align="center">10.4<sup>&sect;</sup></td><td align="center">57.5</td></tr>
</table>
<sub><b>Bold</b> indicates the best score in each row. <sup>†</sup> KoSimpleQA is evaluated as a judge-free 10-choice MCQA variant. <sup>‡</sup> Sampled decoding with a 32,768-token generation budget. <sup>§</sup> DeepSeek-R1-0528-Qwen3-8B frequently fails to terminate its reasoning within the 32K generation budget on Korean inputs, which dominates its Korean-benchmark scores under this protocol.</sub>

Rosetta-7B-Think holds the top score on Korean mathematical reasoning (HRM8K) in this comparison and beats Qwen3-8B on Korean comprehension (HAE-RAE), while being the smallest model in the table. Just as importantly, it terminates its reasoning reliably on Korean inputs — a failure mode that collapses the Korean scores of some global reasoning models under identical budgets.

## Quickstart

### Transformers

Requires `transformers>=5.13` and `trust_remote_code=True`.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "PoSTMEDIA/Rosetta-7B-Think"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, dtype="bfloat16", device_map="auto", trust_remote_code=True
)

messages = [{"role": "user", "content": "127 × 43은 얼마인가요? 단계적으로 풀어주세요."}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)
out = model.generate(inputs, max_new_tokens=4096, temperature=0.6, top_p=0.95, do_sample=True)
text = tokenizer.decode(out[0][inputs.shape[1]:], skip_special_tokens=True)

# Split the reasoning trace from the final answer
if "</think>" in text:
    reasoning, answer = text.split("</think>", 1)
    reasoning = reasoning.replace("<think>", "").strip()
else:
    reasoning, answer = "", text
print("REASONING:", reasoning[:500])
print("ANSWER:", answer.strip())
```

### vLLM

Use the PoSTMEDIA vLLM distribution — native Rosetta support and a built-in reasoning parser:

```bash
VLLM_USE_PRECOMPILED=1 pip install git+https://github.com/PoSTMEDIA-AI/vllm@rosetta-v0.26.0

vllm serve PoSTMEDIA/Rosetta-7B-Think \
  --dtype bfloat16 \
  --reasoning-parser rosetta
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
resp = client.chat.completions.create(
    model="PoSTMEDIA/Rosetta-7B-Think",
    messages=[{"role": "user", "content": "소수가 무한히 많음을 증명해줘."}],
    temperature=0.6,
    top_p=0.95,
)
print("REASONING:", resp.choices[0].message.reasoning)
print("ANSWER:", resp.choices[0].message.content)
```

> [!IMPORTANT]
> vLLM **v0.26 or later** is required. Recommended sampling: `temperature 0.6, top_p 0.95`. Allow a generous `max_tokens` (≥ 4,096; 32,768 for competition math) so reasoning traces can complete.

## Limitations

- Reasoning traces increase latency and token usage; budget `max_tokens` accordingly.
- The model can generate factually incorrect content inside fluent reasoning; verify high-stakes outputs.
- Optimized for Korean and English; other languages are not guaranteed.
- Alignment was performed on contexts up to 32K tokens; validate quality for longer inputs.

## License

Apache License 2.0 — see [LICENSE](./LICENSE). If you build something with Rosetta, we'd appreciate a *"Built with Rosetta"* attribution.

## Citation

```bibtex
@misc{rosetta2026,
  title  = {Rosetta-7B: A Bilingual Korean-English Language Model Family},
  author = {{PoSTMEDIA AI Lab}},
  year   = {2026},
  url    = {https://huggingface.co/collections/PoSTMEDIA/rosetta-6a9db30fd1b4585b0c1845e9}
}
```

## Contact

Questions and feedback — please open a discussion on the model page.
