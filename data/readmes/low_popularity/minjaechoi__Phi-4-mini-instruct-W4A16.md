---
license: mit
base_model: microsoft/Phi-4-mini-instruct
language:
- en
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- quantized
- gptq
- w4a16
- int4
- compressed-tensors
- vllm
- llm-compressor
---

# Phi-4-mini-instruct — W4A16 (GPTQ, int4 weight-only)

4-bit weight-only (W4A16) quantization of [`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct), produced with
[LLM Compressor](https://github.com/vllm-project/llm-compressor)'s `GPTQModifier`. All `Linear` layers are quantized
except `lm_head`, which is kept at full precision.

## Quantization method

| | |
|---|---|
| Method | GPTQ (`GPTQModifier`, LLM Compressor) |
| Scheme | W4A16 (4-bit weights, 16-bit activations) |
| Weight dtype | INT4, symmetric |
| Group size | 128 |
| Quantized targets | `Linear` (all layers except `lm_head`) |
| Activation ordering | static |
| Dampening frac | 0.01 |
| Output format | `compressed-tensors` (`pack-quantized`) |

Recipe used (`recipe.yaml`, included in this repo):

```yaml
default_stage:
  default_modifiers:
    GPTQModifier:
      targets: [Linear]
      ignore: [lm_head]
      scheme: W4A16
      block_size: 128
      dampening_frac: 0.01
      actorder: static
      requires_calibration_data: true
```

## Calibration set

256 packed sequences × 2048 tokens = **524,288 calibration tokens**, sampled (seed=42) from a mixed Korean/English
instruction + function-calling corpus, targeting the following source composition:

| Source | Target % | Actual % (this model) | Tokens (this model) |
|---|---|---|---|
| [KRX-Data/Won-Instruct](https://huggingface.co/datasets/KRX-Data/Won-Instruct) | 35% | 35.28% | 184,966 |
| [heegyu/glaive-function-calling-v2-ko](https://huggingface.co/datasets/heegyu/glaive-function-calling-v2-ko) | 30% | 30.55% | 160,168 |
| [NousResearch/hermes-function-calling-v1 (json-mode-agentic.json)](https://huggingface.co/datasets/NousResearch/hermes-function-calling-v1) | 10% | 9.95% | 52,180 |
| [heegyu/open-korean-instructions](https://huggingface.co/datasets/heegyu/open-korean-instructions) | 10% | 10.22% | 53,595 |
| [kuotient/gsm8k-ko](https://huggingface.co/datasets/kuotient/gsm8k-ko) | 5% | 5.21% | 27,290 |
| in-house synthetic data (SafeCommit project, programmatically generated) | 10% | 8.79% | 46,089 |

- Raw pool before filtering/dedup: 49,268 examples (49,179 after removing 88 duplicates)
- Quota-sampled for calibration: 1,311 examples → 1,225 packed into the final 256×2048 blocks
- Tool-calling trajectories in the pool: 8,995 (2,854 multi-tool)
- Contamination check: gsm8k-ko: train split only used; no BFCL/AgentDojo/tau-bench/SafeCommit-eval sources included

`safecommit_synth` is unreleased in-house synthetic data from the SafeCommit project, not a public HF dataset.

## How to run

### vLLM (recommended — required for the `compressed-tensors` W4A16 kernels used here)

```bash
vllm serve minjaechoi/Phi-4-mini-instruct-W4A16 --served-model-name phi4-mini
```

```bash
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "phi4-mini",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

### Transformers (requires the `compressed-tensors` package for int4 dequant kernels)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "minjaechoi/Phi-4-mini-instruct-W4A16"
tok = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

msgs = [{"role": "user", "content": "Hello!"}]
inputs = tok.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt").to(model.device)
out = model.generate(inputs, max_new_tokens=256)
print(tok.decode(out[0], skip_special_tokens=True))
```

## Benchmarks

Evaluated on this W4A16 checkpoint (not compared against an FP16 baseline run in this project yet):

- **AgentDojo** (banking suite, utility-only, 16 tasks): **5/16 tasks passed (31.2%)** — utility-only scoring, no prompt-injection attacks included.
- **BFCL v4**: attempted, but the evaluation harness used had a request-routing bug (`--local-model-path` was not
  substituted into the API request, so every call 404'd against the vLLM server) — the resulting scores are invalid
  and are intentionally **not** published here. Will be updated after a corrected re-run.

## Files

- `model.safetensors` — quantized weights (`compressed-tensors` pack-quantized format)
- `config.json` — includes the `quantization_config` (compressed-tensors) needed by vLLM/transformers to load this checkpoint
- `recipe.yaml` — the exact LLM Compressor recipe used to produce this checkpoint
- `tokenizer.json`, `tokenizer_config.json`, `chat_template.jinja` — tokenizer/chat template, copied unmodified from the base model
- `LICENSE` — base model license, included per its terms

## License

This checkpoint is a derivative of [`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct) and is distributed
under the same license (**mit**, see `LICENSE` in this repo). No additional restrictions are added beyond
the base model's license.
