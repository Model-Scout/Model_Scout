---
license: apache-2.0
base_model: Qwen/Qwen2.5-1.5B-Instruct
language:
- en
- ko
library_name: transformers
pipeline_tag: text-generation
tags:
- finance
- tool-calling
- qlora
- gamblerinsight
- qwen2.5
---

# GamblerInsight Smoke Model (`gamblerinsight-1-qwen2.5-1.5b-smoke`)

## Model Overview

GamblerInsight Smoke (`gamblerinsight-1-qwen2.5-1.5b-smoke`) is a smoke-test checkpoint for multi-hop
financial reasoning and a tool-calling agent. It is fine-tuned from
`Qwen/Qwen2.5-1.5B-Instruct` on the DGX Spark GB10 platform to validate the end-to-end
pipeline: 2-turn tool-calling trajectories, adapter merge into a standard
safetensors checkpoint, and HuggingFace Hub deployment for vLLM serving.
This release is intended for pipeline verification, not production trading.

## Supported Financial Tools (FinTools)

The model can request two financial tools during reasoning:

- `lookup_stock_price`: latest OHLCV snapshot for a ticker
  (fields: `ticker`, `close`, `open`, `high`, `low`, `volume`, `timestamp`).
- `lookup_technical_indicators`: precomputed technical indicators for a ticker, including
  `RSI`, `MACD`, `BBANDS`, `SMA`, `EMA`, `ATR`, `OBV`, `MFI`, `divergence`,
  and `priced_in_score`.

Example tool call:

```json
{
  "id": "call_01",
  "type": "function",
  "function": {"name": "lookup_stock_price", "arguments": "{\"ticker\": \"AAPL\"}"}
}
```

## Training Details

- **Base model**: `Qwen/Qwen2.5-1.5B-Instruct`
- **Artifact name**: `gamblerinsight-1-qwen2.5-1.5b-smoke`
- **HuggingFace repository**: `tayaee/gamblerinsight-1-qwen2.5-1.5b-smoke`
- **Method**: BF16/FP16 LoRA via PEFT (`lora_bf16`)
- **LoRA hyperparameters**: `r=8`, `alpha=16`, `dropout=0.05`
- **Optimization**: `max_steps=10`, `learning_rate=0.0002`, `batch_size=2`
- **Training data**: `minimal_sft_smoke.jsonl` (16 trajectories)
- **Loss**: final `0.8810` (average: 1.1700)
- **2-turn tool-calling trajectory format**:
  1. Turn 1 (user): financial analysis request with a ticker.
  2. Turn 1 (assistant): one or more tool calls (`lookup_stock_price`,
     `lookup_technical_indicators`), followed by a tool observation message.
  3. Turn 2 (assistant): structured reasoning wrapped in `<think>...</think>`,
     a machine-readable forecast block in `<forecast_json>...</forecast_json>`,
     and a human-readable final report section.
- **Build timestamp (UTC)**: 2026-10-31T13:45:43.287515+00:00

## Quickstart & Usage

### Option A: vLLM serving with automatic tool choice

```bash
vllm serve tayaee/gamblerinsight-1-qwen2.5-1.5b-smoke \
  --host 0.0.0.0 --port 8001 \
  --served-model-name gamblerinsight-1-qwen2.5-1.5b-smoke \
  --enable-auto-tool-choice \
  --tool-call-parser hermes
```

Health check:

```bash
curl -sf http://localhost:8001/health
curl -sf http://localhost:8001/v1/models
```

### Option B: OpenAI-compatible SDK client

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8001/v1", api_key="EMPTY")
tools = [
    {
        "type": "function",
        "function": {
            "name": "lookup_stock_price",
            "description": "Look up the latest stock price snapshot for a ticker.",
            "parameters": {
                "type": "object",
                "properties": {"ticker": {"type": "string"}},
                "required": ["ticker"],
            },
        },
    },
]
resp = client.chat.completions.create(
    model="gamblerinsight-1-qwen2.5-1.5b-smoke",
    messages=[{"role": "user", "content": "Analyze AAPL with RSI and MACD."}],
    tools=tools,
    tool_choice="auto",
)
print(resp.choices[0].message.content)
```

### Option C: Transformers (local inference, no server)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "tayaee/gamblerinsight-1-qwen2.5-1.5b-smoke"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id, device_map="auto", trust_remote_code=True
)
messages = [{"role": "user", "content": "Analyze AAPL with RSI and MACD."}]
prompt = tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Intended Use & Limitations

- **Intended use**: smoke-test checkpoint for validating the GamblerInsight
  training, merge, upload, and vLLM serving pipeline.
- **Out of scope**: production trading decisions, portfolio management,
  or any regulated investment advisory service.
- **Limitations**: trained for only 10 steps on a minimal smoke dataset;
  outputs may be incomplete, inconsistent, or hallucinated. Tool observations
  in training are snapshots and may be stale at inference time.
- **Disclaimer**: This model is for research and engineering validation only.
  It does not provide financial advice. Nothing in the model output should be
  construed as a recommendation to buy, sell, or hold any security. Always
  consult a licensed financial professional before making investment decisions.
- **License**: Apache-2.0. Base model: `Qwen/Qwen2.5-1.5B-Instruct`.
