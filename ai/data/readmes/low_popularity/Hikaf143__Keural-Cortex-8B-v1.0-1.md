---
language:
- en
- ko
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- text-generation
- conversational
- korean
- english
- function-calling
- agent
---

# Keural Cortex Foundation Model (8B) — v1.0

<p align="center"><img src="assets/keural-cortex-agentic-logo.gif" alt="Keural symbol at the Cortex neural core with animated orbital energy" width="100%"/></p>

Keural Cortex is MKD's local-first Korean-English language-model program for Keural applications. This release is an 8B-parameter, instruction- and preference-aligned checkpoint with a structured tool-calling layer for enterprise workflows.

It is designed to run in customer-controlled infrastructure through an OpenAI-compatible vLLM endpoint. The host application—not the model—executes tools, enforces permissions, retrieves live data, and owns user data handling.

> **Release status:** Public v1.0. Evaluate on your own data, workflows, safety requirements, and target serving configuration before production deployment.

<p align="center"><img src="assets/architecture.svg" alt="Cortex 8B architecture overview" width="100%"/></p>

## introduction

**English.** Keural Cortex is a locally deployable AI foundation-model capability built for Korean-English enterprise interaction. It combines efficient 8B-scale inference, controllable OpenAI-compatible serving, and structured tool-call generation so that Keural can connect users to approved enterprise workflows while retaining application-level control of data, permissions, and execution.

**한국어.** Keural Cortex는 한국어·영어 기반의 엔터프라이즈 AI 상호작용을 위해 설계된 로컬 배포형 파운데이션 모델 역량입니다. 8B 규모의 효율적인 추론, OpenAI 호환 서빙, 구조화된 Tool Call 생성을 결합하여 Keural이 승인된 업무 워크플로와 연동할 수 있도록 지원합니다. 데이터·권한·실행 통제는 모델이 아닌 Keural 애플리케이션 계층에서 관리합니다.

## Key strengths

| Strength | What it enables |
|---|---|
| **Local-first deployment** | On-premise or customer-controlled serving patterns; the application controls networking, credentials, access, and retention. |
| **Korean-English interaction** | Direct bilingual chat behavior for Keural user experiences. |
| **Structured tool calls** | Generates OpenAI-compatible calls for `search_web`, `fetch_web_urls`, `retrieve_documents`, and `ask_clarification` when those tools are provided. |
| **Agent-ready architecture** | Separates model decision-making from tool execution, allowing the product layer to apply authorization, auditing, retrieval, and real-time data policies. |
| **Long-context design** | Configuration supports a 65,536-token maximum position length. Serving limits should be set according to available GPU memory and workload. |
| **Efficient serving** | Tested with vLLM using an OpenAI-compatible `/v1/chat/completions` interface. |


<p align="center"><img src="assets/deployment.svg" alt="Private local deployment pattern" width="100%"/></p>

## Model details

| Item | Value |
|---|---|
| Architecture | Decoder-only transformer language model |
| Transformer layers | 36 |
| Hidden size | 4,096 |
| Attention heads / KV heads | 32 / 8 |
| Vocabulary size | 151,936 |
| Maximum position length | 65,536 tokens |
| Weights | BF16 SafeTensors, ~16 GB |
| Alignment path | Continued training, supervised instruction tuning, preference optimization, and Keural agent/tool-contract tuning |

## Verified serving smoke tests

The following were verified through vLLM's OpenAI-compatible API in the release environment:

- Plain Korean chat returned a direct answer without emitting a tool call.
- A current-information request generated a structured `search_web` call.
- An exhaustive document request generated `retrieve_documents` with `exhaustive: true`.
- An underspecified revision request generated `ask_clarification` with a question and checklist.

These are smoke tests, not a substitute for domain-specific benchmarking or safety evaluation.

## Quick start: vLLM

```bash
vllm serve <MODEL_PATH> \
  --served-model-name keural-cortex-8b-v1.0 \
  --tool-call-parser hermes \
  --enable-auto-tool-choice
```

For text-only chat, send a normal OpenAI Chat Completions request **without** `tools` or `tool_choice`. For agent workflows, provide only the tools your application authorizes, validate all tool arguments server-side, and execute calls outside the model process.

## Example tool contract

```json
{
  "type": "function",
  "function": {
    "name": "retrieve_documents",
    "description": "Search content in the user's available documents.",
    "parameters": {
      "type": "object",
      "properties": {
        "query": {"type": "string"},
        "file_ids": {"type": "array", "items": {"type": "string"}},
        "exhaustive": {"type": "boolean"}
      },
      "required": ["query"]
    }
  }
}
```

## Limitations and responsible use

- Outputs can be inaccurate, incomplete, or inconsistent across prompts and serving configurations. Verify important information.
- The model has no inherent live-web access, private-document access, or authority to take external actions. These capabilities must be supplied and governed by the host application.
- Tool calls are model suggestions. Validate schemas, authorization, user intent, and side effects before execution.
- Do not use this preview as the sole basis for high-stakes medical, legal, financial, safety, employment, credit, or access-control decisions.

## Certification, license, and attribution

**Certification note.** Keural Cortex Foundation Model (8B) v1.0 is based on Qwen3-8B-Base and is released under Apache-2.0. Please retain applicable upstream notices and comply with the license terms.

## Citation

```bibtex
@misc{keural-cortex-8b-v1.0,
  title={Keural Cortex Foundation Model (8B) — v1.0},
  author={MKD AI},
  year={2026},
  publisher={Hugging Face}
}
```

## Research portfolio: reproducibility and evidence boundaries

### Provenance and contribution

This personal-namespace repository hosts the MKD release originally published at
[mkd-ai/Keural-Cortex-8B-v1.0](https://huggingface.co/mkd-ai/Keural-Cortex-8B-v1.0).
The original MKD attribution, upstream license notes, and release documentation remain
above. Hosting and documenting this release is not a claim of sole training authorship.
Individual research/training contributions have not been added without supporting details.

### Inspectable artifacts

The repository contains BF16 SafeTensors weights, tokenizer files, the chat template,
generation configuration, and `config.json`. Configuration inspection confirms Qwen3
causal-LM architecture, 36 layers, hidden size 4096, 32 attention heads, 8 KV heads,
and 65,536 maximum positions. These are configuration facts, not measured performance.
The tokenizer advertises a different maximum length (131,072); use the model/serving
configuration and verified workload limits rather than assuming that tokenizer setting
proves usable context length.

Weights alone occupy approximately 16.4 GB (decimal). Runtime buffers, KV cache, and
serving overhead need additional memory. Hardware capacity, quantization settings,
prompt length, and concurrency must be recorded for any performance comparison.
No new GPU inference run was performed while preparing this portfolio documentation.

### Offline text-only inference example

Download and pin an exact repository revision on an approved connected machine first.
Then run from a local folder on the offline machine. This example is documentation;
it has not been executed against the full weights in this portfolio preparation.
Use a Transformers release compatible with the bundled configuration; the saved
configuration records Transformers 5.17.0, which is not itself a dependency lock.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_dir = '/path/to/pinned/local/model'
tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
model = AutoModelForCausalLM.from_pretrained(
    model_dir, local_files_only=True, dtype='auto', device_map='auto'
)
messages = [{'role': 'user', 'content': '한국어와 영어로 간단히 인사해 주세요.'}]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, tokenize=True,
    return_dict=True, return_tensors='pt'
).to(model.device)
with torch.inference_mode():
    generated = model.generate(**inputs, max_new_tokens=128, do_sample=False)
print(tokenizer.decode(
    generated[0, inputs['input_ids'].shape[-1]:], skip_special_tokens=True
))
```

### Evaluation status

| Evidence | Status |
|---|---|
| Configuration and artifact inventory | Inspected for this portfolio |
| Release serving smoke tests above | Reported by the original release; not independently reproduced here |
| Korean/English task benchmark against a base model | Not supplied; no improvement figure claimed |
| Clinical EMR accuracy or clinical safety validation | Not performed |
| Patient-level synthetic safeguards demo | Separate deterministic prototype; does not run this model |

A useful future comparison would pin the base and adapted model revisions, prompts,
decoding settings, patient-grouped splits, dataset licenses, and hardware. Report
groundedness, unsupported-answer rate, missing-information refusal, and task scores
against the same held-out examples. Publish actual measurements before making claims.

### Clinical scope

This is a general-purpose enterprise model, **not clinically validated**. The
[synthetic EMR demo](https://huggingface.co/spaces/Hikaf143/synthetic-emr-safeguards)
and [fixture dataset](https://huggingface.co/datasets/Hikaf143/synthetic-emr-safeguards)
demonstrate software safeguards only. They do not establish this model's performance
on hospital records and are not intended for diagnosis or treatment.

Portfolio code profile: [github.com/mkd-hika](https://github.com/mkd-hika).
