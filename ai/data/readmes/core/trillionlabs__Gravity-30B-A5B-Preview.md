---
license: apache-2.0
language:
  - en
  - ko
library_name: transformers
tags:
  - moe
  - mixture-of-experts
  - gravity
  - trillion-labs
  - chat
  - post-trained
  - function-calling
  - tool-use
  - preview
pipeline_tag: text-generation
base_model:
  - trillionlabs/Gravity-30B-A5B-Base
---

<p align="center">
  <img src="preview-banner.png" alt="Gravity-30B-A5B-Preview" width="100%">
</p>

# Gravity-30B-A5B-Preview

**Gravity-30B-A5B-Preview** is a post-trained language model built on [Gravity-30B-A5B-Base](https://huggingface.co/trillionlabs/Gravity-30B-A5B-Base) by [Trillion Labs](https://trillionlabs.co). Starting from the 128K-context base model, it underwent long-context supervised fine-tuning (SFT) and several rounds of preference optimization (DPO), with the final rounds targeting **multi-turn tool use** using preference labels computed by executing the model's tool calls rather than by an LLM judge.

The model is a **hybrid thinking** model: it reasons inside `<think>…</think>` by default and can be switched to direct answers per request.

This is a preview release. The checkpoint uses the GravityMoE architecture (`trust_remote_code=True`), whose modeling code inherits directly from the DeepSeek-V3 implementation in `transformers`.

## Model Summary

| Property | Value |
|---|---|
| **Base Model** | [Gravity-30B-A5B-Base](https://huggingface.co/trillionlabs/Gravity-30B-A5B-Base) |
| **Total Parameters** | 29.56B |
| **Active Parameters** | 5.34B |
| **Architecture** | GravityMoE (DeepSeek-V3-compatible: MLA + sparse MoE) |
| **Context Length** | 131,072 tokens (128K) |
| **Thinking** | Hybrid (`enable_thinking`, `/nothink`) |
| **Tool Calling** | Yes (GLM-4.5-style XML `<tool_call>`) |
| **Precision** | bf16 |
| **License** | Apache 2.0 |

For full architectural details (MLA, MoE routing, tokenizer, etc.), see the [base model card](https://huggingface.co/trillionlabs/Gravity-30B-A5B-Base).

## Post-Training Pipeline

Starting from [Gravity-30B-A5B-Base](https://huggingface.co/trillionlabs/Gravity-30B-A5B-Base):

1. **Long-Context SFT** — Instruction tuning at the full 128K context (sequence packing) on a mixture of general chat, reasoning, science, code and agentic trajectories.
2. **Preference Optimization (DPO)** — A round of DPO on judged preference pairs targeting response quality and termination behaviour.
3. **Execution-Labelled Multi-Turn DPO** — Two rounds of DPO for multi-turn tool use. Candidate turns are executed against live tool environments and compared with the gold call sequence's resulting state and responses; matching answers become `chosen`, non-matching become `rejected`. No LLM judge is involved.

## Evaluation Results

### Tool Use

BFCL v3, three runs per checkpoint with a fresh server per run, mean ± standard deviation. Live Acc is the sample-weighted mean of the four live AST categories; multi-turn is the unweighted mean of the four multi-turn categories.

| Model | BFCL v3 Live Acc (n=1351) | BFCL v3 multi-turn (n=800) | LAB-Bench (tools on) |
|---|---|---|---|
| SFT checkpoint (stage 1) | 69.97 ± 0.99 | 27.05 ± 0.29 | 48.24 |
| **Gravity-30B-A5B-Preview** | **73.11 ± 0.34** | **30.25 ± 0.50** | 49.58 |

LAB-Bench covers the six non-image subtasks with tools enabled; its run-to-run spread (~6 points) is larger than the difference between the two rows, so it is reported only to show the preference training did not regress it.

## Quickstart

### Installation

```bash
pip install "transformers>=4.57" torch
```

### Using Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "trillionlabs/Gravity-30B-A5B-Preview"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Solve the equation: x^3 - 6x^2 + 11x - 6 = 0"},
]

inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt", return_dict=True
).to(model.device)

output = model.generate(**inputs, max_new_tokens=2048, do_sample=True, temperature=0.7, top_p=0.95)
print(tokenizer.decode(output[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### Thinking Mode

Thinking is on by default: the chat template ends the prompt with `<|assistant|>\n<think>` and the model writes its reasoning before `</think>`. To get a direct answer, pass `enable_thinking=False` to `apply_chat_template` (or append `/nothink` to the user message):

```python
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt", return_dict=True, enable_thinking=False
).to(model.device)
```

When serving with SGLang, use `--reasoning-parser glm45` so the `<think>` block is returned as `reasoning_content` instead of `content`.

### Tool Calling

Tools passed via `tools=` are rendered into the system prompt and calls are emitted as

```
<tool_call>get_weather
<arg_key>city</arg_key>
<arg_value>Seoul</arg_value>
</tool_call>
```

SGLang parses this format with `--tool-call-parser glm45`.

## Deployment

> **Note:** We are working on upstreaming native GravityMoE support to [SGLang](https://github.com/sgl-project/sglang). Until the PR is merged, please use the fork below. Internally the model is DeepSeek-V3-compatible, so the fork only registers the `GravityMoEForCausalLM` name onto SGLang's DeepSeek-V3 implementation. The full 131,072-token window is recommended for agentic workloads.

### SGLang

Install SGLang from the [sglang-gravity](https://github.com/trillion-labs/sglang-gravity) fork (based on SGLang v0.5.19):

```bash
pip install "sglang[all] @ git+https://github.com/trillion-labs/sglang-gravity.git#subdirectory=python"
```

Launch the server:

```bash
python3 -m sglang.launch_server \
    --model-path trillionlabs/Gravity-30B-A5B-Preview \
    --host 0.0.0.0 --port 30000 \
    --tp 4 --context-length 131072 \
    --trust-remote-code --dtype bfloat16 \
    --tool-call-parser glm45 --reasoning-parser glm45
```

Send a request:

```bash
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "trillionlabs/Gravity-30B-A5B-Preview",
    "messages": [{"role": "user", "content": "What is the capital of South Korea?"}],
    "max_tokens": 512,
    "temperature": 0.7
  }'
```

## Limitations

- This is a preview release. Agentic and multi-turn capabilities are under active development.
- The model may generate factually incorrect, biased, or harmful content.
- Performance may degrade on languages not well-represented in the training data.

## Acknowledgements

This model was developed as part of a collaborative research initiative led by **Lunit** and **Trillion Labs**, with a focus on advancing foundation models for science and healthcare.

- **Lunit** — Project lead and medical AI research
- **Trillion Labs** — Model architecture, pretraining, and infrastructure
- **Aigen Science** — Biomedical AI and drug discovery research
- **SK Biopharmaceuticals** — AI-driven drug development and digital healthcare advisory
- **Kakao Healthcare** — Medical data standardization and platform support

We also thank the following participating institutions for their contributions: KAIST (Yoonjae Choi, Taekyun Kim, Jong Chul Ye, Hyunwoo Kim, Seunghoon Hong), Seoul National University (Yousung Jung), Rebellions, Standigm, NHIS Ilsan Hospital, Yongin Severance Hospital, Gangdong Kyung Hee University Hospital, Kyung Hee University Medical Center, Korea University, Konyang University Hospital, Ewha Womans University Seoul Hospital, Keimyung University Dongsan Medical Center, Pusan National University Yangsan Hospital, and D-Circle.

This work was supported by the **AI Specialized Foundation Model Project** (인공지능 특화 파운데이션 모델 프로젝트), funded by the **Ministry of Science and ICT** (과학기술정보통신부, MSIT) and managed by the **National IT Industry Promotion Agency** (NIPA, 정보통신산업진흥원).

## License

This model is released under the [Apache 2.0 License](LICENSE).

## Citation

```bibtex
@misc{gravity-30b-preview-2026,
    title={Gravity-30B-A5B-Preview},
    author={Trillion Labs},
    year={2026},
    url={https://huggingface.co/trillionlabs/Gravity-30B-A5B-Preview}
}
```

## Contact

- Website: [trillionlabs.co](https://trillionlabs.co)
- Website: [lunit.io](https://www.lunit.io)
