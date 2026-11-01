---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
pipeline_tag: text-generation
tags:
- liquid
- lfm2.5
- edge
- parallel-constrained-decoding
- structured-generation
- classification
- inference-only
- modal
base_model: LiquidAI/LFM2.5-2.6B
model_name: LFM2.5-2.6B-RLCD
---

# LFM2.5-2.6B-RLCD

**Fast finite-choice structured inference using unchanged LiquidAI/LFM2.5-2.6B weights.**
This package implements Parallel Constrained Decoding (PCD): prefill shared context once,
branch the model's attention **and convolution** state, evaluate allowed answers in parallel,
and serialize a typed JSON object in Python.

**Inference-only, experimental, and uncalibrated.** No training, LoRA, reinforcement learning,
quantization, or saved weight modification was performed. The `RLCD` name follows the community
inference examples; it does **not** mean we reproduced TypeSafe/Jev's Reinforcement Learning for
Calibrated Decisions. We target the fast finite-choice interaction pattern, not proprietary
training, calibration, API parity, or an unmeasured speed claim.

## Results and release status

See [measured results, wrong answers, and limitations](docs/pcd-results.md), with raw JSON evidence
under `results/pcd/`. Only the measurements for the released source revision belong to this release.
This is a small development/diagnostic evaluation, **not held-out production validation**.

On the final single-L40S run, fast token PCD averaged **56.24 ms** on 12 development
cases versus **557.41 ms** for direct-answer AR JSON (~9.9x). On a single synthetic
28-boolean configuration, it took **106.98 ms versus 4,875.30 ms (~45.6x)**, with all
fields correct for both methods. These are warm GPU request times, not network latency.

**Accuracy is the important limitation:** token PCD reached 88.9% development field
accuracy but only **72.2% on six fresh audit cases**, versus **94.4%** for AR JSON.
It also failed both high-cardinality token-mode probes. The production accuracy gate
was **not met**. Sequence scoring correctly resolved those high-cardinality examples,
but the 255-choice case was slower than AR. See the report rather than extrapolating
the favorable 28-field speedup to every task.

Schema validity does not mean a correct decision. Do not use the returned probabilities as
validated automation thresholds. Test your own labeled workload; use human review or a stronger
reasoning model where mistakes matter. No comparison against Jev's service was performed.

## Two inference modes

### `token`: fast parallel choices

Each field receives an unambiguous atomic option code. Codes are verified against the actual
tokenizer. One cached branch per field produces a decision hidden state; the output head is
projected only onto the relevant option-token rows, not the entire 128,000-token vocabulary.
The selected code is mapped back to the original enum string or actual Python boolean.

This is a classifier-style next-token decision, not arbitrary free-text generation. It does not
collapse multi-token enum values onto an ambiguous first token: opaque codes distinguish them.
The output includes the distribution over allowed codes, explicitly marked **uncalibrated**.
Code/label wording and ordering can affect predictions.

### `sequence`: full-sequence scoring reference

Each candidate is a complete JSON value with a newline terminator. The whole JSON member is
canonically tokenized before factoring its shared token prefix, preserving space/quote merges.
All remaining candidate tokens are scored with teacher forcing and full-vocabulary normalized
log-likelihood; the score is not a first-token proxy. Shared-prefix choices, escaped strings,
and Unicode are supported. The scoring convention still has length and wording bias.

Both paths reuse the shared prompt once and fork isolated hybrid caches. Token mode normally
uses two backbone calls for up to 32 fields. Sequence mode uses
`1 + ceil(total_candidates / branch_batch_size)` calls. Parallelism reduces sequential steps;
it does not make memory, FLOPs, or latency constant in the input size.

## Install and use

Get the code without immediately downloading duplicate weight files:

```bash
GIT_LFS_SKIP_SMUDGE=1 git clone https://huggingface.co/monotykamary/LFM2.5-2.6B-RLCD
cd LFM2.5-2.6B-RLCD
uv venv --python 3.11
uv pip install --python .venv/bin/python -r requirements-pcd.txt
source .venv/bin/activate
```

The default engine loads the pinned original LiquidAI model. On a CUDA GPU:

```python
from pcd import Engine

schema = {
    "type": "object",
    "properties": {
        "topic": {
            "type": "string",
            "enum": ["billing", "technical", "shipping"],
            "description": "The main issue in the message",
        },
        "refund": {
            "type": "boolean",
            "description": "Whether the customer explicitly requests a refund",
        },
    },
    "required": ["topic", "refund"],
    "additionalProperties": False,
}
engine = Engine(device="cuda", dtype="float16", attention="sdpa")
result = engine.constrained(
    "I was charged twice. Please refund the duplicate charge.", schema, mode="token"
)
print(result["object"])          # Typed values; field decisions may still be wrong.
print(result["fields"])          # Scores, candidate distributions, and margins.
print(result["elapsed_ms"])
assert result["calibrated"] is False

reference = engine.constrained("Please refund my duplicate charge.", schema, mode="sequence")
```

To use the bundled weights instead, pass `model_id="monotykamary/LFM2.5-2.6B-RLCD"`
and `revision="main"` to `Engine`; pin the public commit SHA for reproducibility.
The original BF16 tensors are bundled unchanged, even though the measured engine uses an FP16
runtime cast. Plain `AutoModelForCausalLM.from_pretrained(...)` loads the original generative
model; it does **not** enable parallel constrained inference. No `trust_remote_code=True` is needed.

## Supported schema and limits

- Closed, flat object, with every property required and `additionalProperties: false`.
- Fields are booleans or nonempty unique string enums; descriptions are optional.
- No arbitrary numbers, free-text strings, arrays, nested/optional fields, or relational constraints.
- Defaults: 32 fields, 256 total candidates, 4,096 shared-prompt tokens (schema included),
  64 tokens per serialized value, and 32 branches per microbatch.
- Limits and unsupported schema keywords are rejected, not silently ignored.
- Successful calls guarantee syntax, types and enum membership through programmatic assembly.
  They do not guarantee truth, completeness of the answer space, or cross-field consistency.

Return values live in `result["object"]`; telemetry is separate and does not alter your schema.
`token` probabilities are a restricted-code softmax; `sequence` probabilities are normalized
candidate likelihoods. Neither is a calibration guarantee or evidence that all candidates include
the correct answer. Include an explicit unknown/other option where appropriate.

## LFM2.5-specific details

The pinned model has 8 full-attention layers, 22 short-convolution layers and 2,697,198,592
parameters. Branches copy **both** KV tensors and convolution state; mutable expanded views
are not shared. Request caches are discarded, not retained across users. GPU operations are
serialized within one engine instance to bound memory and avoid state races.

The native chat template always opens `<think>`. The PCD prompts explicitly supply an empty
closed reasoning span; this is not an officially supported `enable_thinking=False` mode.
Skipping reasoning can hurt accuracy. The original native reasoning behavior is preserved in
the unchanged model/tokenizer and is available through normal generation.

FP32 CUDA and local tiny-model checks establish cache/scoring equivalence; measured FP16
rounding tolerances and errors are in the results. The initial BF16 path failed the tighter
hidden-state comparison and is not the recommended validated serving precision.

## Run on Modal, frugally

The scripts use the existing `huggingface-cache` Volume, a separate results Volume, one L40S,
zero minimum containers, a maximum of one container per parameterization, and short idle
shutdown. No H100, multi-GPU job or training run is required.

```bash
modal run lfm25_pcd_modal.py --task prepare
modal run lfm25_pcd_modal.py --task validate --precision float32
modal run lfm25_pcd_modal.py --task benchmark --suite diagnostic --repeats 3
modal run lfm25_pcd_modal.py --task benchmark --suite stress --repeats 3
```

Preparation/publication use a Modal Secret named `huggingface` (`HF_TOKEN` preferred).
GPU inference only needs public cached weights; it is not given the write credential.
Benchmarks have a time budget and persist raw results. They do not perform automatic retries
or switch to a larger GPU on failure. Pricing and actual billed time depend on your workspace.

`PCDModel.infer.remote(context, schema, mode)` supports on-demand calls. An authenticated POST
Web Function is included (`PCDModel.extract`); it accepts `context`, `schema`, and optional `mode`.
It requires Modal proxy authentication (`Modal-Key` and `Modal-Secret` headers). Deploy with
`modal deploy lfm25_pcd_modal.py` only after validating your workload. This release does not
claim a production-ready always-on endpoint or measured network/cold-start latency.

## Tests and reproducibility

```bash
python -m pytest tests/pcd -q
```

Local tests use a small randomly initialized LFM2 model: no GPU and no full-model download.
They test cached/full scoring, branch isolation, both convolution cache paths, microbatch
invariance, schema rejection, token shifts and typed output. Modal validation repeats critical
checks on the real pinned model. Benchmarks retain outputs, errors, source hashes, dependency
versions, actual accelerator, precision, prompt sizes and memory measurements.

Upstream identity: `LiquidAI/LFM2.5-2.6B` at
`654f9463ce32b05d0429d76fe1f580b27d4c1ac0`.
The Hub release includes `BASE_MODEL_MANIFEST.json` and `ARTIFACTS.json` for model and code
provenance. The original model card is preserved as `UPSTREAM_README.md` and appended below
the constrained-inference documentation in the published README.

## Attribution and license

The 350M reference's hybrid-cache/full-sequence design informed this implementation:
[notnotsamuel/LFM2.5-350M-RLCD](https://huggingface.co/notnotsamuel/LFM2.5-350M-RLCD).
See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and [LICENSE-CODE](LICENSE-CODE).

LiquidAI weights, tokenizer, configuration and original model documentation retain the
**LFM Open License v1.0**, including redistribution requirements and commercial revenue
conditions. The inference-code MIT license does not replace the model license.

TypeSafe describes Jev's actual RLCD training in its
[AI primer](https://docs.typesafe.ai/introduction/machine-learning-primer).
This is an independent PCD implementation, not an affiliated or equivalent Jev release.


## Original LiquidAI model documentation

> The following upstream text is preserved verbatim. Its benchmarks describe the original model, not our PCD engine. Our measurements and limitations are documented above.

<div align="center">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI" 
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • 
    <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • 
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • 
    <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>

# LFM2.5-2.6B

LFM2.5-2.6B is part of LFM2.5, a family of hybrid models designed for **on-device deployment**. It builds on the LFM2 architecture with a 128K context window and agentic post-training.

- **Best-in-class agent**: Competitive with models 4x larger on tool use, instruction following, and multi-step agentic tasks.
- **Agentic reinforcement learning**: Trained inside the most popular agentic harnesses to improve compatibility.
- **Efficient inference**: 220 tok/s on an Apple M5 Max and 113 tok/s on an AMD Ryzen CPU, in under 2.5 GB of memory.

Find more information about LFM2.5-2.6B in our [blog post](https://www.liquid.ai/blog/lfm2-5-2-6b).

![](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/NAfUL2725b6KDUGf1KOd9.png)

> [!NOTE]
> 💻 **Demos**: Try LFM2.5-2.6B's agentic capabilities in a Hugging Face space without any setup:
> **[Research Agent in your browser](https://huggingface.co/spaces/LiquidAI/LFM2.5-2.6B-WebGPU)**: helps you research a specific question and generates a summary

## 🗒️ Model Details

| Model                                                                | Parameters | Description                            |
| -------------------------------------------------------------------- | ---------- | -------------------------------------- |
| [LFM2.5-2.6B-Base](https://huggingface.co/LiquidAI/LFM2.5-2.6B-Base) | 2.6B       | Pre-trained base model for fine-tuning |
| **[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**       | 2.6B       | Post-trained for agentic workloads     |

LFM2.5-2.6B is a general-purpose text-only model with the following features:

- **Total parameters**: 2.69B
- **Number of layers**: 30 (22 double-gated short convolution blocks + 8 GQA)
- **Training budget**: 34 trillion tokens
- **Vocabulary size**: 128,000
- **Context length**: 131,072 tokens
- **Languages**: English, Arabic, Chinese, French, German, Italian, Japanese, Korean, Portuguese, Spanish, Vietnamese, Thai, Indonesian, Hindi, Russian, Polish 
- **Generation parameters**:
  - `temperature: 0.1`
  - `top_k: 50`
  - `repetition_penalty: 1.1`

| Model                                                                    | Description                                                                                                                                  |
| ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- |
| **[LFM2.5-2.6B](https://huggingface.co/LiquidAI/LFM2.5-2.6B)**           | Original model checkpoint in native format. Best for fine-tuning or inference with Transformers, vLLM, and SGLang.                           |
| **[LFM2.5-2.6B-GGUF](https://huggingface.co/LiquidAI/LFM2.5-2.6B-GGUF)** | Quantized format for llama.cpp and compatible tools. Optimized for CPU inference and local deployment with reduced memory usage.             |
| **[LFM2.5-2.6B-ONNX](https://huggingface.co/LiquidAI/LFM2.5-2.6B-ONNX)** | ONNX Runtime format for cross-platform deployment. Enables hardware-accelerated inference across diverse environments (cloud, edge, mobile). |
| **[LFM2.5-2.6B-MLX](https://huggingface.co/LiquidAI/LFM2.5-2.6B-MLX)**   | MLX format for Apple Silicon. Optimized for fast inference on Mac devices using the MLX framework.                                           |
| **[LFM2.5-2.6B-DSpark](https://huggingface.co/LiquidAI/LFM2.5-2.6B-DSpark)** | Speculative decoding drafter (328M). Pair it with this model for ~2.6x faster decoding with identical outputs.                                |

We recommend using it for agentic workloads, tool use, data extraction, RAG, and long-context workflows. It is not recommended for agentic coding and knowledge-heavy tasks.

### Chat Template

LFM2.5 uses a ChatML-like format. See the [Chat Template documentation](https://docs.liquid.ai/lfm/key-concepts/chat-template) for details. Example:

```
<|startoftext|><|im_start|>system
You are a helpful assistant trained by Liquid AI.<|im_end|>
<|im_start|>user
What is C. elegans?<|im_end|>
<|im_start|>assistant
```

You can use [`tokenizer.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#using-applychattemplate) to format your messages automatically.

> [!TIP]
> 💡 **Note**: LFM2.5-2.6B is a pure reasoning model that always thinks before it answers. It adds a `<think>` tag directly in the [chat template](https://huggingface.co/LiquidAI/LFM2.5-2.6B/blob/main/chat_template.jinja#L124) when starting an assistant answer.

### Tool Use

LFM2.5 supports function calling in four steps:

1. **Function definition**: Provide the list of tools as a JSON object in the system prompt, or use [`tokenizer.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_extras#passing-tools) with `tools=...`.
2. **Function call**: By default, LFM2.5 writes Pythonic function calls (a Python list between `<|tool_call_start|>` and `<|tool_call_end|>` special tokens), as the assistant answer. You can override this behavior by asking the model to output JSON function calls in the system prompt.
3. **Function execution**: Execute the call and return the result with the `tool` role.
4. **Final answer**: LFM2.5 interprets the tool output and returns a plain-text answer addressing the original prompt.

See the [Tool Use documentation](https://docs.liquid.ai/lfm/key-concepts/tool-use) for the full guide. Example:

```
<|startoftext|><|im_start|>system
List of tools: [{"name": "get_candidate_status", "description": "Retrieves the current status of a candidate in the recruitment process", "parameters": {"type": "object", "properties": {"candidate_id": {"type": "string", "description": "Unique identifier for the candidate"}}, "required": ["candidate_id"]}}]<|im_end|>
<|im_start|>user
What is the current status of candidate ID 12345?<|im_end|>
<|im_start|>assistant
<|tool_call_start|>[get_candidate_status(candidate_id="12345")]<|tool_call_end|>Checking the current status of candidate ID 12345.<|im_end|>
<|im_start|>tool
[{"candidate_id": "12345", "status": "Interview Scheduled", "position": "Clinical Research Associate", "date": "2023-11-20"}]<|im_end|>
<|im_start|>assistant
The candidate with ID 12345 is currently in the "Interview Scheduled" stage for the position of Clinical Research Associate, with an interview date set for 2023-11-20.<|im_end|>
```

### Training

LFM2.5-2.6B is pre-trained on ~34T tokens, with a mid-training phase that extends the context window to 128K. Post-training then turns the base model into an agent in four stages: supervised fine-tuning (two rounds), per-domain teacher specialization, multi-domain on-policy distillation, and agentic reinforcement learning.

![](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/hCmGKgTRihAR9NfJlCVNN.png)

In particular, agentic reinforcement learning allows us to directly train the model inside popular agentic harnesses. It exposes the model to their tools, system prompts, and interaction patterns, helping it work reliably across agent environments.

![](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/LXqTXbw-lh0Yru5UWLMCq.png)

## 🏃 Inference

LFM2.5 is supported by many inference frameworks. See the [Inference documentation](https://docs.liquid.ai/lfm/inference/transformers) for the full list.

| Name | Description | Docs | Notebook |
|------|-------------|------|:--------:|
| [Transformers](https://github.com/huggingface/transformers) | Simple inference with direct access to model internals. | <a href="https://docs.liquid.ai/lfm/inference/transformers">Link</a> | <a href="https://colab.research.google.com/drive/1_q3jQ6LtyiuPzFZv7Vw8xSfPU5FwkKZY?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| [vLLM](https://github.com/vllm-project/vllm) | High-throughput production deployments with GPU. | <a href="https://docs.liquid.ai/lfm/inference/vllm">Link</a> | <a href="https://colab.research.google.com/drive/1VfyscuHP8A3we_YpnzuabYJzr5ju0Mit?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| [SGLang](https://github.com/sgl-project/sglang) | High-throughput production deployments with GPU. | <a href="https://docs.liquid.ai/deployment/gpu-inference/sglang">Link</a> | — |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Cross-platform inference with CPU offloading. | <a href="https://docs.liquid.ai/lfm/inference/llama-cpp">Link</a> | <a href="https://colab.research.google.com/drive/1ohLl3w47OQZA4ELo46i5E4Z6oGWBAyo8?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| [MLX](https://github.com/ml-explore/mlx) | Apple's machine learning framework optimized for Apple Silicon. | <a href="https://docs.liquid.ai/lfm/inference/mlx">Link</a> | — |
| [LM Studio](https://lmstudio.ai/) | Desktop application for running LLMs locally. | <a href="https://docs.liquid.ai/deployment/on-device/lm-studio">Link</a> | — |

> [!TIP]
> ⚡ **Faster decoding**: attach [LFM2.5-2.6B-DSpark](https://huggingface.co/LiquidAI/LFM2.5-2.6B-DSpark), a 328M speculative-decoding drafter, for ~2.6x faster decoding in SGLang and on Apple silicon via Metal with exactly the same outputs.
> 
## How to use

LFM2.5-2.6B can be used for direct inference or as a backend for agentic workflows.

### Quick start 

Get started with Transformers (compatible with `transformers>=5.0.0`):

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_id = "LiquidAI/LFM2.5-2.6B"
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    dtype="bfloat16",
#   attn_implementation="flash_attention_2" <- uncomment on compatible GPU
)
tokenizer = AutoTokenizer.from_pretrained(model_id)
streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)

prompt = "What is C. elegans?"

input_ids = tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}],
    add_generation_prompt=True,
    return_tensors="pt",
    tokenize=True,
)["input_ids"].to(model.device)

output = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.1,
    top_k=50,
    repetition_penalty=1.1,
    max_new_tokens=512,
    streamer=streamer,
)
```

### Agent Use

LFM2.5-2.6B supports tool calling for agentic workflows. 
Serve it locally with any OpenAI-compatible backend (see [🏃 Inference](#🏃-inference), then configure your agent harness to connect to it.
For full setup instructions including installation and additional options, see our [Agent Harnesses guide](https://docs.liquid.ai/examples/agent-harnesses).

*Note: The port depends on your serving backend — llama.cpp and MLX use `8080`, vLLM uses `8000`, SGLang uses `30000`, and LM Studio uses `1234`. Adjust the URLs below accordingly.*

#### Hermes

Either use the interactive wizard or set it directly:

```
hermes config set model.provider custom
hermes config set model.base_url http://localhost:8080/v1
hermes config set model.default LFM2.5-2.6B
hermes config set model.context_length 131072
hermes config set model.api_mode chat_completions
hermes config set agent.tool_use_enforcement true
```

#### OpenClaw

Add to your config to `models.providers`:

```
local: {
  baseUrl: "http://localhost:8080/v1",
  apiKey: "sk-local",
  api: "openai-completions",
  models: [{
    id: "LFM2.5-2.6B",
    name: "LFM2.5-2.6B",
    contextWindow: 131072,
    maxTokens: 8192,
    cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 }
  }]
}
```

#### Pi

Add to your config to `~/.pi/agent/models.json`:

```
{
  "providers": {
    "local": {
      "baseUrl": "http://localhost:8080/v1",
      "api": "openai-completions",
      "apiKey": "local",
      "models": [{ "id": "LFM2.5-2.6B" }]
    }
  }
}
```

## 🔧 Fine-Tuning

We recommend fine-tuning LFM2.5 for your specific use case to achieve the best results.

| Name | Description | Docs | Notebook |
|------|-------------|------|----------|
| CPT ([Unsloth](https://github.com/unslothai/unsloth)) | Continued Pre-Training using Unsloth for text completion. | <a href="https://docs.liquid.ai/lfm/fine-tuning/unsloth">Link</a> | <a href="https://colab.research.google.com/drive/10fm7eNMezs-DSn36mF7vAsNYlOsx9YZO?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| CPT ([Unsloth](https://github.com/unslothai/unsloth)) | Continued Pre-Training using Unsloth for translation. | <a href="https://docs.liquid.ai/lfm/fine-tuning/unsloth">Link</a> | <a href="https://colab.research.google.com/drive/1gaP8yTle2_v35Um8Gpu9239fqbU7UgY8?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT ([Unsloth](https://github.com/unslothai/unsloth)) | Supervised Fine-Tuning with LoRA using Unsloth. | <a href="https://docs.liquid.ai/lfm/fine-tuning/unsloth">Link</a> | <a href="https://colab.research.google.com/drive/1vGRg4ksRj__6OLvXkHhvji_Pamv801Ss?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT ([TRL](https://github.com/huggingface/trl)) | Supervised Fine-Tuning with LoRA using TRL. | <a href="https://docs.liquid.ai/lfm/fine-tuning/trl">Link</a> | <a href="https://colab.research.google.com/drive/1j5Hk_SyBb2soUsuhU0eIEA9GwLNRnElF?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| DPO ([TRL](https://github.com/huggingface/trl)) | Direct Preference Optimization with LoRA using TRL. | <a href="https://docs.liquid.ai/lfm/fine-tuning/trl">Link</a> | <a href="https://colab.research.google.com/drive/1MQdsPxFHeZweGsNx4RH7Ia8lG8PiGE1t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| GRPO ([TRL](https://github.com/huggingface/trl)) | GRPO with LoRA using TRL. | <a href="https://docs.liquid.ai/lfm/fine-tuning/trl">Link</a> | <a href="https://colab.research.google.com/github/Liquid4All/cookbook/blob/main/finetuning/notebooks/grpo_for_verifiable_tasks.ipynb"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |

## 📊 Performance

### Benchmarks

We compared LFM2.5-2.6B with relevant sub-10B models on a diverse suite of benchmarks.

| Benchmark | LFM2.5-2.6B (2.6B) | gemma-4-E2B-it (5.1B) | gemma-4-E4B-it (8B) | Qwen3.5-4B (4.7B) | Qwen3.5-9B (9.7B) |
|---|---:|---:|---:|---:|---:|
| AA-Omni-Public Index | -29.50 | -74.47 | -49.03 | -54.30 | -50.43 |
| AA-Omni-Public Acc | 8.13 | 6.37 | 8.33 | 17.63 | 21.30 |
| AA-Omni-Public Non-hallu | 59.04 | 13.67 | 37.42 | 12.66 | 8.84 |
| AIME25 | 51.87 | 26.33 | 34.27 | 49.33 | 56.07 |
| LiveCodeBenchv6 | 59.41 | 54.92 | 63.77 | 60.85 | 69.86 |
| IFBench | 59.17 | 34.08 | 39.24 | 48.40 | 56.47 |
| Multi-IF | 80.07 | 69.44 | 77.35 | 55.67 | 62.55 |
| IFStruct | 85.49 | 64.85 | 76.65 | 36.25 | 78.50 |
| BFCLv4 | 56.88 | 36.98 | 46.39 | 50.56 | 60.13 |
| ToolSandbox | 77.83 | 52.40 | 65.00 | 75.55 | 76.44 |
| τ³-Bench Banking | 5.67 | 3.35 | 4.12 | 5.45 | 5.15 |
| Claw-Eval average (EN) | 62.85 | 53.14 | 58.02 | 62.28 | 66.53 |
| PinchBench | 68.22 | 44.24 | 55.09 | 71.26 | 71.45 |
| BrowseComp+ (OpenClaw) | 26.89 | 8.31 | 15.90 | 24.46 | 27.23 |

### CPU Inference

Due to its efficient LFM2 architecture, LFM2.5-2.6B is the fastest model we tested, with decode speeds of 220 tokens/s on an M5 Max and 113 tokens/s on a Ryzen AI Max+ 395. At 30 tokens/s, it allows you to run capable agents even on a phone.

![](https://cdn-uploads.huggingface.co/production/uploads/644249b08443bce4c9890a0f/YwLcMpzsq1b5SW1Gtdt1o.png)

### GPU Inference

LFM2.5-2.6B is the fastest model in its size class, reaching almost **15K output tokens per second at high concurrency**, roughly 1.3B tokens per day on a single H100.

![](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/6EHzZzduUg1bISqkQuHZ6.png)

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).

## Citation

```bibtex
@article{liquidAI202626B,
  author  = {Liquid AI},
  title   = {LFM2.5-2.6B: Agents Everywhere},
  journal = {Liquid AI Blog},
  year    = {2026},
  note    = {www.liquid.ai/blog/lfm2-5-2-6b},
}
```

```bibtex
@article{liquidai2025lfm2,
  title   = {LFM2 Technical Report},
  author  = {Liquid AI},
  journal = {arXiv preprint arXiv:2511.23404},
  year    = {2025}
}
```