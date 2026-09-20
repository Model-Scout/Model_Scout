---
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ja
- ko
- fr
- es
- de
- it
- pt
- ar
- zh
pipeline_tag: text-generation
tags:
- liquid
- edge
- lfm2.5
- thinking
- reasoning
- onnx
- onnxruntime
- webgpu
base_model:
- LiquidAI/LFM2.5-1.2B-Thinking
---

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" alt="Liquid AI" style="width: 100%; max-width: 100%;">

  <div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
  </div>
</div>

<br>

# LFM2.5-1.2B-Thinking-ONNX

ONNX export of [LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking) for cross-platform inference.

LFM2.5-Thinking is a reasoning model that generates step-by-step thinking before producing final answers. The model outputs its reasoning process within `<think>...</think>` tags, followed by the final response. This approach improves accuracy on complex tasks like math, coding, and logical reasoning.

## Recommended Variants

| Precision | Size | Use Case |
|-----------|------|----------|
| Q4 | ~1.2GB | Recommended for most uses |
| FP16 | ~2.4GB | Higher quality |
| Q8 | ~1.7GB | Balance of quality and size |

## Model Files

```
onnx/
├── model.onnx              # FP32
├── model_fp16.onnx         # FP16
├── model_q4.onnx           # Q4 (recommended)
└── model_q8.onnx           # Q8
```

## Python

### Installation

```bash
pip install onnxruntime transformers numpy huggingface_hub
# or with GPU support:
pip install onnxruntime-gpu transformers numpy huggingface_hub
```

### Inference

```python
import re

import numpy as np
import onnxruntime as ort
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer

# Download model (Q4 recommended)
model_id = "LiquidAI/LFM2.5-1.2B-Thinking-ONNX"
model_path = hf_hub_download(model_id, "onnx/model_q4.onnx")
data_path = hf_hub_download(model_id, "onnx/model_q4.onnx_data")

# Load model and tokenizer
session = ort.InferenceSession(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

# Prepare chat input
messages = [{"role": "user", "content": "What is 25 * 37?"}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
input_ids = np.array([tokenizer.encode(prompt, add_special_tokens=False)], dtype=np.int64)

# Initialize KV cache
ONNX_DTYPE = {"tensor(float)": np.float32, "tensor(float16)": np.float16, "tensor(int64)": np.int64}
cache = {}
for inp in session.get_inputs():
    if inp.name in {"input_ids", "attention_mask", "position_ids"}:
        continue
    shape = [d if isinstance(d, int) else 1 for d in inp.shape]
    for i, d in enumerate(inp.shape):
        if isinstance(d, str) and "sequence" in d.lower():
            shape[i] = 0
    cache[inp.name] = np.zeros(shape, dtype=ONNX_DTYPE.get(inp.type, np.float32))

# Check if model uses position_ids
input_names = {inp.name for inp in session.get_inputs()}
use_position_ids = "position_ids" in input_names

# Generate tokens
seq_len = input_ids.shape[1]
generated_tokens = []

for step in range(512):  # max tokens (reasoning may need more tokens)
    if step == 0:
        ids = input_ids
        pos = np.arange(seq_len, dtype=np.int64).reshape(1, -1)
    else:
        ids = np.array([[generated_tokens[-1]]], dtype=np.int64)
        pos = np.array([[seq_len + len(generated_tokens) - 1]], dtype=np.int64)

    attn_mask = np.ones((1, seq_len + len(generated_tokens)), dtype=np.int64)
    feed = {"input_ids": ids, "attention_mask": attn_mask, **cache}
    if use_position_ids:
        feed["position_ids"] = pos

    outputs = session.run(None, feed)
    next_token = int(np.argmax(outputs[0][0, -1]))
    generated_tokens.append(next_token)

    # Update cache
    for i, out in enumerate(session.get_outputs()[1:], 1):
        name = out.name.replace("present_conv", "past_conv").replace("present.", "past_key_values.")
        if name in cache:
            cache[name] = outputs[i]

    if next_token == tokenizer.eos_token_id:
        break

# Parse thinking and response
full_response = tokenizer.decode(generated_tokens, skip_special_tokens=True)
think_match = re.search(r"<think>(.*?)</think>", full_response, re.DOTALL)
if think_match:
    thinking = think_match.group(1).strip()
    answer = full_response[think_match.end():].strip()
    print(f"Thinking:\n{thinking}\n")
    print(f"Answer:\n{answer}")
else:
    print(full_response)
```

## WebGPU (Browser)

### Installation

```bash
npm install onnxruntime-web @huggingface/transformers
```

### Enable WebGPU

WebGPU is required for browser inference. To enable:

1. **Chrome/Edge**: Navigate to `chrome://flags/#enable-unsafe-webgpu`, enable, and restart
2. **Verify**: Check `chrome://gpu` for "WebGPU" status
3. **Test**: Run `navigator.gpu.requestAdapter()` in DevTools console

### Inference

```javascript
import * as ort from "onnxruntime-web/webgpu";
import { AutoTokenizer } from "@huggingface/transformers";

// Check WebGPU availability
if (!navigator.gpu) {
  throw new Error("WebGPU not available. Enable at chrome://flags/#enable-unsafe-webgpu");
}
const adapter = await navigator.gpu.requestAdapter();
if (!adapter) {
  throw new Error("WebGPU adapter not found. Check chrome://gpu for status.");
}

ort.env.wasm.numThreads = 1;

const modelId = "LiquidAI/LFM2.5-1.2B-Thinking-ONNX";
const modelBase = `https://huggingface.co/${modelId}/resolve/main`;

// Load tokenizer
const tokenizer = await AutoTokenizer.from_pretrained(modelId);

// Load ONNX session with external data
const onnxPath = `${modelBase}/onnx/model_q4.onnx`;
const dataPath = `${modelBase}/onnx/model_q4.onnx_data`;
const session = await ort.InferenceSession.create(onnxPath, {
  executionProviders: ["webgpu"],
  externalData: [{ path: "model_q4.onnx_data", data: dataPath }],
});

// Model config (from config.json)
const hiddenSize = 2048;
const numKVHeads = 8;
const headDim = 256;

// Initialize KV cache
function initCache() {
  const cache = {};
  for (const name of session.inputNames) {
    if (name.startsWith("past_conv")) {
      cache[name] = new ort.Tensor("float32", new Float32Array(hiddenSize * 3), [1, hiddenSize, 3]);
    } else if (name.startsWith("past_key_values")) {
      cache[name] = new ort.Tensor("float32", new Float32Array(0), [1, numKVHeads, 0, headDim]);
    }
  }
  return cache;
}

// Update cache from outputs
function updateCache(cache, outputs) {
  for (const [name, tensor] of Object.entries(outputs)) {
    if (name.startsWith("present_conv")) {
      cache[name.replace("present_conv", "past_conv")] = tensor;
    } else if (name.startsWith("present.")) {
      cache[name.replace("present.", "past_key_values.")] = tensor;
    }
  }
}

// Build prompt and tokenize
const messages = [{ role: "user", content: "What is 25 * 37?" }];
const prompt = tokenizer.apply_chat_template(messages, { add_generation_prompt: true, tokenize: false });
const inputIds = tokenizer.encode(prompt);

// Generation loop
const cache = initCache();
const eosTokenId = tokenizer.eos_token_id;
const generatedTokens = [];
let curLen = inputIds.length;
let ids = inputIds;

for (let step = 0; step < 512; step++) {
  const inputIdsTensor = new ort.Tensor("int64", new BigInt64Array(ids.map(BigInt)), [1, ids.length]);
  const attentionMask = new ort.Tensor("int64", new BigInt64Array(curLen).fill(1n), [1, curLen]);

  const outputs = await session.run({ input_ids: inputIdsTensor, attention_mask: attentionMask, ...cache });

  // Greedy decode: argmax of last token logits
  const logits = outputs.logits;
  const vocabSize = logits.dims[2];
  const lastLogits = logits.data.slice((logits.dims[1] - 1) * vocabSize);
  const nextToken = lastLogits.indexOf(Math.max(...lastLogits));

  generatedTokens.push(nextToken);
  if (nextToken === eosTokenId) break;

  updateCache(cache, outputs);
  ids = [nextToken];
  curLen++;
}

// Parse thinking and response
const fullResponse = tokenizer.decode(generatedTokens, { skip_special_tokens: true });
const thinkMatch = fullResponse.match(/<think>([\s\S]*?)<\/think>/);
if (thinkMatch) {
  const thinking = thinkMatch[1].trim();
  const answer = fullResponse.slice(thinkMatch.index + thinkMatch[0].length).trim();
  console.log("Thinking:", thinking);
  console.log("Answer:", answer);
} else {
  console.log(fullResponse);
}
```

### WebGPU Notes

- Recommended: `model_q4.onnx` for best performance/quality balance
- For higher quality: `model_fp16.onnx`
- Models use external data files (`.onnx_data`) that are loaded automatically
- int64 tensors require `BigInt64Array`
- Reasoning models may generate longer outputs; adjust max tokens as needed

## Output Format

The model produces output in two parts:

1. **Thinking**: Internal reasoning wrapped in `<think>...</think>` tags
2. **Answer**: The final response after the closing `</think>` tag

Example output:
```
<think>
To calculate 25 * 37, I can break this down:
25 * 37 = 25 * (40 - 3) = 25 * 40 - 25 * 3 = 1000 - 75 = 925
</think>
The answer is 925.
```

## License

This model is released under the [LFM 1.0 License](LICENSE).
