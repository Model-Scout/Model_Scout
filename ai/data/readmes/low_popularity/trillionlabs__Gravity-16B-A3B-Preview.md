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
  - preview
pipeline_tag: text-generation
base_model:
  - trillionlabs/Gravity-16B-A3B-Base
---

<p align="center">
  <img src="preview-banner.png" alt="Gravity-16B-A3B-Preview" width="100%">
</p>

# Gravity-16B-A3B-Preview

**Gravity-16B-A3B-Preview** is a post-trained language model built on [Gravity-16B-A3B-Base](https://huggingface.co/trillionlabs/Gravity-16B-A3B-Base) by [Trillion Labs](https://trillionlabs.co). Starting from the base model, it underwent context length extension (32K → 128K), supervised fine-tuning (SFT), and reinforcement learning (GRPO) focused on science and code.

This is a preview release offering a strong balance of capability, efficiency, and long-context support for its size. We are actively working on agentic capabilities for the full release.

## Model Summary

| Property | Value |
|---|---|
| **Base Model** | [Gravity-16B-A3B-Base](https://huggingface.co/trillionlabs/Gravity-16B-A3B-Base) |
| **Total Parameters** | 16.24B |
| **Active Parameters** | 3.16B |
| **Architecture** | GravityMoE |
| **Context Length** | 131,072 tokens (128K) |
| **Precision** | bf16 |
| **License** | Apache 2.0 |

For full architectural details (MLA, MoE routing, tokenizer, etc.), see the [base model card](https://huggingface.co/trillionlabs/Gravity-16B-A3B-Base).

## Post-Training Pipeline

Starting from [Gravity-16B-A3B-Base](https://huggingface.co/trillionlabs/Gravity-16B-A3B-Base) (pretrained on ~5.5T tokens):

1. **Context Length Extension** — Extended from 32K to 128K tokens.
2. **Supervised Fine-Tuning (SFT)** — Instruction tuning for general chat and task-following capabilities.
3. **Reinforcement Learning (GRPO)** — Single-step Group Relative Policy Optimization focused on science and code domains.

Agentic RL and multi-turn RL stages are in progress and will be included in future releases.

## Evaluation Results

| Category | Benchmark | Metric | Score |
|---|---|---|---|
| **Math** | AIME 2024 | acc | 43.3 |
| | GSM8K | acc | 91.8 |
| | MATH500 | acc | 88.6 |
| **Code** | HumanEval | pass@1 | 89.0 |
| | MBPP | pass@1 | 96.0 |
| | LiveCodeBench V6 | pass@1 | 41.0 |
| **Knowledge** | MMLU | acc | 80.1 |
| | MMLU-Pro | acc | 71.5 |
| | BBH | acc | 79.24 |
| **Science** | GPQA Diamond | acc | 55.1 |
| | Arc Challenge | acc | 92.32 |
| | ChemBench | acc | 68.6 |
| | Molang Bench (Editing) | SMILEs validty / Tanimoto similarity / Accuracy | 70.83 / 86.43 / 43.23 |
| | Molang Bench (Generation) | SMILEs validty / Tanimoto similarity / Accuracy | 35.96 / 43.24 / 1.69 |
| **Instruction Following** | IFEval | instruct level loose | 84.53 |
| | IFBench | instruct level loose | 46.51 |
| **Agentic** | Tau^2 (Telecom) | pass@1 | 71.93 |
| | Scicode | sub problem level | 18.8 |
| | Terminal Bench | pass@1 | 21.25 |
| **Long Context** | AA-LCR | pass@1 | 21.0 |

### Comparison with Moonlight-16B-A3B-Instruct

| Category | Benchmark | Metric | Gravity-16B-A3B-Preview | Moonlight-16B-A3B-Instruct |
|---|---|---|---|---|
| **Math** | GSM8K | acc | 91.8 | 77.4 |
| **Code** | HumanEval | pass@1 | 89.0 | 48.1 |
| | MBPP | pass@1 | 96.0 | 63.8 |
| **Knowledge** | MMLU | acc | 80.1 | 70.0 |
| | MMLU-Pro | acc | 71.5 | 42.4 |
| | BBH | acc | 79.24 | 65.2 |

> Note: We include Moonlight-16B-A3B-Instruct for comparison since it is similar in size to our model. Moonlight-16B-A3B-Instruct scores are taken from the numbers reported in their own technical report.

With 3.16B active parameters, 128K context, and broad coverage across math, code, and knowledge benchmarks, the model offers a strong balance of capability and efficiency for its size.

Agentic benchmarks (multi-step tool use, code execution) are not yet a focus of this release. We are actively training on agentic tasks and will include those results in the next release.

## Quickstart

### Installation

```bash
pip install "transformers>=5.0" torch
```

### Using Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "trillionlabs/Gravity-16B-A3B-Preview"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Solve the equation: x^3 - 6x^2 + 11x - 6 = 0"},
]

input_ids = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

output = model.generate(input_ids, max_new_tokens=1024, do_sample=True, temperature=0.7)
print(tokenizer.decode(output[0][input_ids.shape[-1]:], skip_special_tokens=True))
```

## Deployment

> **Note:** We are working on upstreaming native GravityMoE support to [SGLang](https://github.com/sgl-project/sglang). Until the PR is merged, please use the installation steps below.

### SGLang

Install SGLang from the [sglang-gravity](https://github.com/trillion-labs/sglang-gravity) fork:

```bash
pip install "sglang[all] @ git+https://github.com/trillion-labs/sglang-gravity.git#subdirectory=python"
```

Launch the server:

```bash
python3 -m sglang.launch_server \
    --model-path trillionlabs/Gravity-16B-A3B-Preview \
    --host 0.0.0.0 \
    --port 30000 \
    --tp 8 \
    --trust-remote-code \
    --moe-runner-backend triton \
    --tool-call-parser glm45 \
    --reasoning-parser glm45 \
    --dtype bfloat16
```

Send a request:

```bash
curl http://localhost:30000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "trillionlabs/Gravity-16B-A3B-Preview",
    "messages": [{"role": "user", "content": "What is the capital of South Korea?"}],
    "max_tokens": 128,
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
@misc{gravity-preview-2026,
    title={Gravity-16B-A3B-Preview},
    author={Trillion Labs},
    year={2026},
    url={https://huggingface.co/trillionlabs/Gravity-16B-A3B-Preview}
}
```

## Contact

- Website: [trillionlabs.co](https://trillionlabs.co)
- Website: [lunit.io](https://www.lunit.io)
