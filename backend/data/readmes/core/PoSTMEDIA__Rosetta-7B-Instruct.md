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
  - postmedia
---

<div align="center">

# Rosetta-7B-Instruct

[![Collection](https://img.shields.io/badge/Rosetta-Collection-0052CC?style=for-the-badge)](https://huggingface.co/collections/PoSTMEDIA/rosetta-6a9db30fd1b4585b0c1845e9)
[![vLLM](https://img.shields.io/badge/vLLM-PoSTMEDIA--AI-00A3FF?style=for-the-badge&logo=github)](https://github.com/PoSTMEDIA-AI/vllm)
[![License](https://img.shields.io/badge/License-Apache_2.0-7856FF?style=for-the-badge)](./LICENSE)

</div>

## Introduction

**Rosetta-7B-Instruct** is a 7B-parameter bilingual (Korean-English) instruction-tuned model developed by **PoSTMEDIA**. Built on PoSTMEDIA's **Rosetta** dense decoder-only architecture, it is post-trained from [Rosetta-7B-Base](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Base) through large-scale supervised fine-tuning and preference optimization, with a deliberate focus on the capabilities that matter most in real Korean-language deployments: instruction following, Korean cultural and factual knowledge, and Korean mathematical reasoning.

Rosetta-7B is a three-model family covering the full spectrum from research to production:

| Model | Download | Note |
|---|---|---|
| Rosetta-7B-Base | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Base) | Foundation model (completion-style) |
| **Rosetta-7B-Instruct** | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct) | Instruction following / chat *(this model)* |
| Rosetta-7B-Instruct-NVFP4 | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Instruct-NVFP4) | NVFP4 4-bit of Instruct (NVIDIA Blackwell / DGX Spark) |
| Rosetta-7B-Think | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Think) | Explicit reasoning (`<think>`) |
| Rosetta-7B-Think-NVFP4 | [HuggingFace](https://huggingface.co/PoSTMEDIA/Rosetta-7B-Think-NVFP4) | NVFP4 4-bit of Think (NVIDIA Blackwell / DGX Spark) |

## Highlights

- **Korean math reasoning leader** — HRM8K **60.4**, the top score in our eight-model same-protocol comparison of Korean and global open models
- **Top-tier instruction following** — IFEval **80.4**, within the leading group of Korean open models
- **Korean-first design** — 161K Korean-extended vocabulary, dedicated Korean continual-pretraining stage, and in-house synthetic Korean data assets
- **Strong Korean factuality** — KoSimpleQA **71.7**
- **65,536-token context window** with interleaved local-global attention
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
<tr><td><b>Post-training</b></td><td>SFT → preference optimization (DPO)</td></tr>
<tr><td><b>License</b></td><td>Apache-2.0</td></tr>
</tbody></table>
</div>

## Training Overview

The Rosetta-7B family was built through a multi-stage pipeline carried out end-to-end by PoSTMEDIA:

1. **Pretraining** on trillions of tokens of curated bilingual web, code, and academic text
2. **Staged mid-training** for reasoning-dense data and long-context extension up to 65K
3. **Korean continual pretraining** on curated Korean corpora plus in-house synthetic Korean data assets, with the vocabulary extended to 161K for efficient Korean tokenization
4. **Post-training** — large-scale supervised fine-tuning followed by preference optimization (DPO) targeting instruction following, factuality, and safe refusals

## Evaluation Results

All models in the table below, **including competitors, were re-evaluated in-house under an identical protocol** (lm-evaluation-harness + vLLM ≥ 0.26, identical prompts, decoding parameters, and generation budgets). Scores are therefore directly comparable within this table, but may differ from numbers reported elsewhere under different setups.

<!-- prettier-ignore -->
<table>
  <tr>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">Benchmark</th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;"><b>Rosetta-7B-Instruct</b><br><sup>7B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">A.X-4.0-Light<br><sup>7B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">A.X-3.1-Light<br><sup>7B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">EXAONE-3.5<br><sup>7.8B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">Midm-2.0-Base<br><sup>11.5B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">kanana-2<br><sup>3B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">Llama-3.1<br><sup>8B</sup></th>
    <th style="background: rgba(128,128,128,0.1); text-align: center;">Ministral-3<br><sup>8B</sup></th>
  </tr>
  <tr>
    <td align="center" colspan="9" style="background: linear-gradient(90deg, rgba(0,82,204,0.30) 0%, rgba(0,163,255,0.30) 50%, rgba(120,86,255,0.30) 100%); font-weight: bold; height: 32px; padding-top: 2px; padding-bottom: 2px;"><i>General &amp; Reasoning</i></td>
  </tr>
  <tr>
    <td>MMLU</td>
    <td align="center">60.2</td>
    <td align="center">73.0</td>
    <td align="center">57.7</td>
    <td align="center"><b>73.4</b></td>
    <td align="center">68.0</td>
    <td align="center">59.5</td>
    <td align="center">66.6</td>
    <td align="center">72.4</td>
  </tr>
  <tr>
    <td>GPQA</td>
    <td align="center">39.4</td>
    <td align="center">37.4</td>
    <td align="center">30.8</td>
    <td align="center">36.9</td>
    <td align="center">31.8</td>
    <td align="center">32.3</td>
    <td align="center">22.7</td>
    <td align="center"><b>49.5</b></td>
  </tr>
  <tr>
    <td>GSM8K</td>
    <td align="center">79.8</td>
    <td align="center">68.1</td>
    <td align="center">84.0</td>
    <td align="center"><b>88.9</b></td>
    <td align="center">80.7</td>
    <td align="center">70.0</td>
    <td align="center">84.2</td>
    <td align="center">80.8</td>
  </tr>
  <tr>
    <td>IFEval</td>
    <td align="center">80.4</td>
    <td align="center"><b>82.8</b></td>
    <td align="center">77.3</td>
    <td align="center">82.1</td>
    <td align="center">81.3</td>
    <td align="center">76.5</td>
    <td align="center">80.0</td>
    <td align="center">63.8</td>
  </tr>
  <tr>
    <td align="center" colspan="9" style="background: linear-gradient(90deg, rgba(0,82,204,0.30) 0%, rgba(0,163,255,0.30) 50%, rgba(120,86,255,0.30) 100%); font-weight: bold; height: 32px; padding-top: 2px; padding-bottom: 2px;"><i>Korean Language &amp; Knowledge</i></td>
  </tr>
  <tr>
    <td>KMMLU</td>
    <td align="center">45.6</td>
    <td align="center"><b>58.1</b></td>
    <td align="center">49.9</td>
    <td align="center">52.0</td>
    <td align="center">56.4</td>
    <td align="center">44.4</td>
    <td align="center">42.7</td>
    <td align="center">48.5</td>
  </tr>
  <tr>
    <td>CLIcK</td>
    <td align="center">59.2</td>
    <td align="center">68.1</td>
    <td align="center">53.0</td>
    <td align="center">66.2</td>
    <td align="center"><b>70.7</b></td>
    <td align="center">58.2</td>
    <td align="center">54.7</td>
    <td align="center">55.0</td>
  </tr>
  <tr>
    <td>HAE-RAE</td>
    <td align="center">63.0</td>
    <td align="center">74.0</td>
    <td align="center">67.0</td>
    <td align="center">73.7</td>
    <td align="center"><b>79.2</b></td>
    <td align="center">70.8</td>
    <td align="center">55.3</td>
    <td align="center">56.8</td>
  </tr>
  <tr>
    <td>HRM8K</td>
    <td align="center"><b>60.4</b></td>
    <td align="center">46.4</td>
    <td align="center">51.1</td>
    <td align="center">49.8</td>
    <td align="center">51.2</td>
    <td align="center">31.4</td>
    <td align="center">30.8</td>
    <td align="center">54.2</td>
  </tr>
  <tr>
    <td>KoSimpleQA<sup>†</sup></td>
    <td align="center">71.7</td>
    <td align="center">77.5</td>
    <td align="center">45.9</td>
    <td align="center">78.9</td>
    <td align="center"><b>88.9</b></td>
    <td align="center">81.0</td>
    <td align="center">—</td>
    <td align="center">72.1</td>
  </tr>
</table>
<sub><b>Bold</b> indicates the best score in each row. — indicates not evaluated. <sup>†</sup> KoSimpleQA is evaluated as a judge-free 10-choice MCQA variant. Generative benchmarks use greedy decoding; subtask-style suites report the unweighted subtask mean.</sub>

In the broadest same-protocol comparison we are aware of for Korean open models, Rosetta-7B-Instruct holds the **top score on Korean mathematical reasoning (HRM8K 60.4)** — ahead of every Korean flagship in the table — while placing in the leading group on instruction following (IFEval 80.4) and Korean factuality (KoSimpleQA 71.7). Models that lead on knowledge-recall benchmarks are either substantially larger (Midm-2.0-Base, 11.5B) or newest-generation flagships, and none of them match Rosetta on Korean math.

## Quickstart

### Transformers

Requires `transformers>=5.13` and `trust_remote_code=True` (the Rosetta architecture ships as custom code in this repository).

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "PoSTMEDIA/Rosetta-7B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id, dtype="bfloat16", device_map="auto", trust_remote_code=True
)

messages = [
    {"role": "user", "content": "한국의 전통 발효 음식 세 가지를 소개해줘."},
]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

out = model.generate(inputs, max_new_tokens=1024, temperature=0.7, top_p=0.9, do_sample=True)
print(tokenizer.decode(out[0][inputs.shape[1]:], skip_special_tokens=True))
```

### vLLM

Use the PoSTMEDIA vLLM distribution with native Rosetta support — no `trust_remote_code` required:

```bash
VLLM_USE_PRECOMPILED=1 pip install git+https://github.com/PoSTMEDIA-AI/vllm@rosetta-v0.26.0

vllm serve PoSTMEDIA/Rosetta-7B-Instruct --dtype bfloat16
```

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")
resp = client.chat.completions.create(
    model="PoSTMEDIA/Rosetta-7B-Instruct",
    messages=[{"role": "user", "content": "부산 여행 1박 2일 코스를 짜줘."}],
    temperature=0.7,
)
print(resp.choices[0].message.content)
```

> [!IMPORTANT]
> vLLM **v0.26 or later** is required. Recommended sampling: `temperature 0.7, top_p 0.9` (or greedy for deterministic tasks).

## Limitations

- The model can generate factually incorrect or outdated information; verify outputs for high-stakes use.
- Outputs may reflect biases present in web-scale training data.
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
