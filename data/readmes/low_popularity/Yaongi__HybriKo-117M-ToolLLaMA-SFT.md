---
license: apache-2.0
language:
- en
- ko
tags:
- function-calling
- tool-use
- hybridko
- griffin
- rnn-attention-hybrid
pipeline_tag: text-generation
---

# HybriKo-117M-ToolLLaMA-SFT

A **HybriKo** model fine-tuned for **Function Calling / Tool Use** using the ToolLLaMA dataset (187k samples).

## Model Description

| Property | Value |
|----------|-------|
| **Base Model** | HybriKo-117M (Griffin-inspired RNN+Attention Hybrid) |
| **Parameters** | 117.8M |
| **Context Length** | 8192 tokens |
| **Training Data** | ToolLLaMA G123 DFS (187,542 samples) |
| **Training Time** | ~71 minutes on A100 x 8 |
| **Final Loss** | 0.90 |
| **Final PPL** | 2.46 |

## Architecture

HybriKo uses a **2:1 hybrid ratio** of RNN (RGLRU) to Attention blocks:
- Layers 1, 2: Griffin Block (RGLRU)
- Layer 3: Attention Block (GQA with RoPE)
- Pattern repeats...

This provides efficient long-context modeling with linear complexity for most layers.

## Training Details (arXiv:2512.15943 Settings)

| Hyperparameter | Value |
|----------------|-------|
| Learning Rate | 5e-5 |
| Max Grad Norm | 0.3 (aggressive clipping) |
| Batch Size | 256 effective (16 x 8 GPUs x 2 grad accum) |
| Epochs | 1 |
| Context Length | 8192 |
| Optimizer | AdamW |

## Usage (Colab Compatible)

### Installation

```bash
pip install torch transformers sentencepiece huggingface_hub
```

### Quick Start

```python
import torch
import sentencepiece as spm
from huggingface_hub import hf_hub_download
from transformers import AutoModelForCausalLM, AutoConfig

# Load model
model = AutoModelForCausalLM.from_pretrained(
    "Yaongi/HybriKo-117M-ToolLLaMA-SFT",
    trust_remote_code=True,
    torch_dtype=torch.float32
)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)
model.eval()

# Load tokenizer
sp_path = hf_hub_download("Yaongi/HybriKo-117M-ToolLLaMA-SFT", "HybriKo_tok.model")
sp = spm.SentencePieceProcessor()
sp.Load(sp_path)

# Special tokens
SPECIAL_TOKENS = {
    "<|im_start|>": 32000,
    "<|im_end|>": 32001,
    "<thought>": 32002,
    "</thought>": 32003,
    "<tool_call>": 32004,
    "</tool_call>": 32005,
    "<tools>": 32006,
    "</tools>": 32007,
}

def encode(text):
    """Encode text with special token handling."""
    for token, token_id in SPECIAL_TOKENS.items():
        text = text.replace(token, f" \x00{token_id}\x00 ")

    tokens = []
    for part in text.split("\x00"):
        if part.strip().isdigit() and int(part.strip()) in SPECIAL_TOKENS.values():
            tokens.append(int(part.strip()))
        elif part.strip():
            tokens.extend(sp.EncodeAsIds(part))
    return tokens

def decode(ids):
    """Decode token IDs to text."""
    id_to_token = {v: k for k, v in SPECIAL_TOKENS.items()}
    result = []
    regular_ids = []

    for id in ids:
        if id in id_to_token:
            if regular_ids:
                result.append(sp.DecodeIds(regular_ids))
                regular_ids = []
            result.append(id_to_token[id])
        else:
            regular_ids.append(id)

    if regular_ids:
        result.append(sp.DecodeIds(regular_ids))

    return "".join(result)

@torch.no_grad()
def generate(prompt, max_new_tokens=200, temperature=0.7, top_k=50):
    """Generate with stop sequence detection."""
    input_ids = torch.tensor([encode(prompt)]).to(device)
    stop_sequences = ["<|im_end|>", "</tool_call>"]

    for _ in range(max_new_tokens):
        logits = model(input_ids)["logits"][:, -1] / temperature

        if top_k:
            v, _ = torch.topk(logits, min(top_k, logits.size(-1)))
            logits[logits < v[:, [-1]]] = float("-inf")

        probs = torch.softmax(logits, dim=-1)
        next_token = torch.multinomial(probs, 1)
        input_ids = torch.cat([input_ids, next_token], dim=1)

        # Check stop sequences
        text = decode(input_ids[0].tolist())
        for stop in stop_sequences:
            if stop in text.split(prompt)[-1]:
                return text

    return decode(input_ids[0].tolist())
```

### Example: Weather API Call

```python
prompt = """<|im_start|>system
You are an AI assistant with access to tools.
<tools>
{"name": "get_weather", "description": "Get current weather", "parameters": {"location": {"type": "string", "description": "City name"}}}
</tools><|im_end|>
<|im_start|>user
What's the weather in Seoul?<|im_end|>
<|im_start|>assistant
"""

response = generate(prompt, temperature=0.3, top_k=10)
print(response)
```

**Expected Output:**
```
<|im_start|>assistant
<thought>
The user wants to know the weather in Seoul. I should call the get_weather function.
</thought>
<tool_call>
{"name": "get_weather", "arguments": {"location": "Seoul"}}
</tool_call><|im_end|>
```

### Example: Search Query

```python
prompt = """<|im_start|>system
You are an AI assistant with access to tools.
<tools>
{"name": "web_search", "description": "Search the web", "parameters": {"query": {"type": "string"}}}
</tools><|im_end|>
<|im_start|>user
Find information about the latest AI research<|im_end|>
<|im_start|>assistant
"""

response = generate(prompt, temperature=0.3)
print(response)
```

## Prompt Format (Hermes ChatML)

```
<|im_start|>system
You are an AI assistant with access to tools.
<tools>
[Tool definitions in JSON format]
</tools><|im_end|>
<|im_start|>user
[User message]<|im_end|>
<|im_start|>assistant
<thought>
[Model's reasoning]
</thought>
<tool_call>
{"name": "[tool_name]", "arguments": {...}}
</tool_call><|im_end|}
<|im_start|>tool
[Tool response]<|im_end|>
<|im_start|>assistant
[Final response]<|im_end|>
```

## Special Tokens

| Token | ID | Purpose |
|-------|-----|---------|
| `<\|im_start\|>` | 32000 | Start of message |
| `<\|im_end\|>` | 32001 | End of message |
| `<thought>` | 32002 | Start of reasoning |
| `</thought>` | 32003 | End of reasoning |
| `<tool_call>` | 32004 | Start of tool call |
| `</tool_call>` | 32005 | End of tool call |
| `<tools>` | 32006 | Start of tool definitions |
| `</tools>` | 32007 | End of tool definitions |

## Training Loss Curve

| Step | Loss | PPL |
|------|------|-----|
| 10 | 6.72 | 825 |
| 100 | 2.15 | 8.6 |
| 400 | 1.06 | 2.9 |
| 730 (final) | 0.90 | 2.5 |

## Limitations

- Optimized for English tool-calling; Korean support is limited
- 117M parameters - suitable for edge deployment but less capable than larger models
- Best with structured tool-calling format; may struggle with free-form conversation

## Citation

If you use this model, please cite:

```bibtex
@misc{hybridko-toolllama-sft,
  title={HybriKo-117M-ToolLLaMA-SFT: Function Calling Fine-tuned Hybrid RNN-Attention Model},
  author={Yaongi},
  year={2024},
  url={https://huggingface.co/Yaongi/HybriKo-117M-ToolLLaMA-SFT}
}
```

## License

Apache 2.0
