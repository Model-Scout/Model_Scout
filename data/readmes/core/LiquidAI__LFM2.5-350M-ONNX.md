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
  - onnx
  - onnxruntime
  - webgpu
base_model:
  - LiquidAI/LFM2.5-350M
---

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
<br>

# LFM2.5-350M-ONNX

ONNX export of [LFM2.5-350M](https://huggingface.co/LiquidAI/LFM2.5-350M) for cross-platform inference.

## Variants

| Variant | Size | Description |
|---------|------|-------------|
| FP16 | ~692MB | All weights in FP16 |
| Q4 | ~276MB | INT4 embedding (GatherBlockQuantized), INT4 lm_head (MatMulNBits, shared), INT4 MatMul weights |
| Q4F32 | ~459MB | INT4 MatMul weights, FP32 embedding and norms |
| Q8 | ~604MB | INT8 MatMul weights, FP32 embedding and norms |

Q4 uses GatherBlockQuantized for the token embedding and MatMulNBits for the lm_head,
reusing the same quantized weights and scales. All other linear layers are quantized to
INT4 via post-export MatMulNBitsQuantizer. Block size is 32.

Q4F32 keeps the embedding as a FP32 Gather and the lm_head as FP32 Transpose + MatMul.
Only the internal linear layers (attention projections, conv projections, MLP) are
quantized to INT4 via post-export MatMulNBitsQuantizer.

Q8 is the same structure as Q4F32 but with INT8 weights (asymmetric quantization).

## Generation Parameters

| Parameter | Value |
|-----------|-------|
| `temperature` | 0.1 |
| `top_k` | 50 |
| `repetition_penalty` | 1.05 |

## Model Files

```
onnx/
├── model.onnx              # FP32
├── model_fp16.onnx         # FP16
├── model_q4.onnx           # Q4
├── model_q4f32.onnx        # Q4F32
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
import numpy as np
import onnxruntime as ort
from huggingface_hub import hf_hub_download
from transformers import AutoTokenizer

# Download model
model_id = "LiquidAI/LFM2.5-350M-ONNX"
model_path = hf_hub_download(model_id, "onnx/model_q4.onnx")
data_path = hf_hub_download(model_id, "onnx/model_q4.onnx_data")

# Load model and tokenizer
session = ort.InferenceSession(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

# Sampling parameters
TEMPERATURE = 0.1
TOP_K = 50
REPETITION_PENALTY = 1.05

# Prepare chat input
messages = [{"role": "user", "content": "What is the capital of France?"}]
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


def sample_token(logits, generated_tokens):
    """Sample next token with temperature, top-k, and repetition penalty."""
    # Apply repetition penalty
    for token_id in set(generated_tokens):
        if logits[token_id] > 0:
            logits[token_id] /= REPETITION_PENALTY
        else:
            logits[token_id] *= REPETITION_PENALTY

    # Apply temperature
    logits = logits / TEMPERATURE

    # Top-k filtering
    top_k_indices = np.argpartition(logits, -TOP_K)[-TOP_K:]
    top_k_logits = logits[top_k_indices]

    # Softmax over top-k
    top_k_logits -= np.max(top_k_logits)
    probs = np.exp(top_k_logits) / np.sum(np.exp(top_k_logits))

    # Sample
    chosen = np.random.choice(len(top_k_indices), p=probs)
    return int(top_k_indices[chosen])


# Generate tokens
seq_len = input_ids.shape[1]
generated_tokens = []

for step in range(512):  # max tokens
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
    logits = outputs[0][0, -1].copy()
    next_token = sample_token(logits, generated_tokens)
    generated_tokens.append(next_token)

    # Update cache
    for i, out in enumerate(session.get_outputs()[1:], 1):
        name = out.name.replace("present_conv", "past_conv").replace("present.", "past_key_values.")
        if name in cache:
            cache[name] = outputs[i]

    if next_token == tokenizer.eos_token_id:
        break

print(tokenizer.decode(generated_tokens, skip_special_tokens=True))
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

const modelId = "LiquidAI/LFM2.5-350M-ONNX";
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

// Sampling parameters
const TEMPERATURE = 0.1;
const TOP_K = 50;
const REPETITION_PENALTY = 1.05;

// Model config (from config.json)
const hiddenSize = 1024;
const numKVHeads = 8;
const headDim = 64;

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

// Sample next token with temperature, top-k, and repetition penalty
function sampleToken(logitsData, vocabSize, generatedTokens) {
  const logits = new Float32Array(logitsData);

  // Apply repetition penalty
  const seen = new Set(generatedTokens);
  for (const tokenId of seen) {
    if (logits[tokenId] > 0) {
      logits[tokenId] /= REPETITION_PENALTY;
    } else {
      logits[tokenId] *= REPETITION_PENALTY;
    }
  }

  // Apply temperature
  for (let i = 0; i < vocabSize; i++) {
    logits[i] /= TEMPERATURE;
  }

  // Top-k: find top K indices
  const indexed = Array.from(logits.slice(0, vocabSize), (v, i) => [v, i]);
  indexed.sort((a, b) => b[0] - a[0]);
  const topK = indexed.slice(0, TOP_K);

  // Softmax over top-k
  const maxLogit = topK[0][0];
  const exps = topK.map(([v, i]) => [Math.exp(v - maxLogit), i]);
  const sumExp = exps.reduce((s, [e]) => s + e, 0);
  const probs = exps.map(([e, i]) => [e / sumExp, i]);

  // Sample from distribution
  let r = Math.random();
  for (const [p, i] of probs) {
    r -= p;
    if (r <= 0) return i;
  }
  return probs[probs.length - 1][1];
}

// Build prompt and tokenize
const messages = [{ role: "user", content: "What is the capital of France?" }];
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

  const logits = outputs.logits;
  const vocabSize = logits.dims[2];
  const lastLogits = logits.data.slice((logits.dims[1] - 1) * vocabSize, logits.dims[1] * vocabSize);
  const nextToken = sampleToken(lastLogits, vocabSize, generatedTokens);

  generatedTokens.push(nextToken);
  if (nextToken === eosTokenId) break;

  updateCache(cache, outputs);
  ids = [nextToken];
  curLen++;
}

console.log(tokenizer.decode(generatedTokens, { skip_special_tokens: true }));
```

### WebGPU Notes

* Models use external data files (`.onnx_data`) that are loaded automatically
* int64 tensors require `BigInt64Array`

## License

This model is released under the [LFM 1.0 License](LICENSE).
