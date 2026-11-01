---
base_model:
- LiquidAI/LFM2-1.2B
library_name: transformers.js
license: other
license_name: lfm1.0
license_link: LICENSE
language:
  - en
  - ar
  - zh
  - fr
  - de
  - ja
  - ko
  - es
pipeline_tag: text-generation
tags:
  - liquid
  - edge
---


<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/7_6D7rWrLxp2hb6OHSV1p.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 66%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>

<a href="https://playground.liquid.ai/chat">
<svg width="114.8" height="20" viewBox="0 0 1300 200" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Liquid Playground" style="margin-bottom: 1em;">
  <title>Liquid: Playground</title>
  <g>
    <rect fill="#fff" width="600" height="200"></rect>
    <rect fill="url(#x)" x="600" width="700" height="200"></rect>
  </g>
  <g transform="translate(20, 30) scale(0.4, 0.4)">
    <path d="M172.314 129.313L172.219 129.367L206.125 188.18C210.671 195.154 213.324 203.457 213.324 212.382C213.324 220.834 210.956 228.739 206.839 235.479L275.924 213.178L167.853 33.6L141.827 76.9614L172.314 129.313Z" fill="black"/>
    <path d="M114.217 302.4L168.492 257.003C168.447 257.003 168.397 257.003 168.352 257.003C143.515 257.003 123.385 237.027 123.385 212.387C123.385 203.487 126.023 195.204 130.55 188.24L162.621 132.503L135.966 86.7327L60.0762 213.183L114.127 302.4H114.217Z" fill="black"/>
    <path d="M191.435 250.681C191.435 250.681 191.43 250.681 191.425 250.686L129.71 302.4H221.294L267.71 226.593L191.435 250.686V250.681Z" fill="black"/>
  </g>
  <g aria-hidden="true" fill="#fff" text-anchor="start" font-family="Verdana,DejaVu Sans,sans-serif" font-size="110">
    <text x="200" y="148" textLength="329" fill="#000" opacity="0.1">Liquid</text>
    <text x="190" y="138" textLength="329" fill="#000">Liquid</text>
    <text x="655" y="148" textLength="619" fill="#000" opacity="0.1">Playground</text>
    <text x="645" y="138" textLength="619">Playground</text>
  </g>
  
  <linearGradient id="x" x1="0%" y1="0%" x2="100%" y2="0%">
    <stop offset="0%" style="stop-color:#000000"></stop>
    <stop offset="100%" style="stop-color:#000000"></stop>
  </linearGradient>
</svg>
</a>
</center>

# LFM2-1.2B

LFM2 is a new generation of hybrid models developed by [Liquid AI](https://www.liquid.ai/), specifically designed for edge AI and on-device deployment. It sets a new standard in terms of quality, speed, and memory efficiency. 

We're releasing the weights of three post-trained checkpoints with 350M, 700M, and 1.2B parameters. They provide the following key features to create AI-powered edge applications:

* **Fast training & inference** – LFM2 achieves 3x faster training compared to its previous generation. It also benefits from 2x faster decode and prefill speed on CPU compared to Qwen3.
* **Best performance** – LFM2 outperforms similarly-sized models across multiple benchmark categories, including knowledge, mathematics, instruction following, and multilingual capabilities.
* **New architecture** – LFM2 is a new hybrid Liquid model with multiplicative gates and short convolutions.
* **Flexible deployment** – LFM2 runs efficiently on CPU, GPU, and NPU hardware for flexible deployment on smartphones, laptops, or vehicles.

Find more information about LFM2 in our [blog post](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models).

## 📄 Model details

Due to their small size, **we recommend fine-tuning LFM2 models on narrow use cases** to maximize performance. 
They are particularly suited for agentic tasks, data extraction, RAG, creative writing, and multi-turn conversations. 
However, we do not recommend using them for tasks that are knowledge-intensive or require programming skills.

| Property            | Value                         |
| ------------------- | ----------------------------- |
| **Parameters**      | 1,170,340,608                 |
| **Layers**          | 16 (10 conv + 6 attn)         |
| **Context length**  | 32,768 tokens                 |
| **Vocabulary size** | 65,536                        |
| **Precision**       | bfloat16                      |
| **Training budget** | 10 trillion tokens            |
| **License**         | LFM Open License v1.0         |

**Supported languages**: English, Arabic, Chinese, French, German, Japanese, Korean, and Spanish.

**Generation parameters**: We recommend the following parameters:
* `temperature=0.3`
* `min_p=0.15`
* `repetition_penalty=1.05`

**Architecture**: Hybrid model with multiplicative gates and short convolutions: 10 double-gated short-range LIV convolution blocks and 6 grouped query attention (GQA) blocks.

**Pre-training mixture**: Approximately 75% English, 20% multilingual, and 5% code data sourced from the web and licensed materials.

**Training approach**:
* Knowledge distillation using [LFM1-7B](https://www.liquid.ai/blog/introducing-lfm-7b-setting-new-standards-for-efficient-language-models) as teacher model
* Very large-scale SFT on 50% downstream tasks, 50% general domains
* Custom DPO with length normalization and semi-online datasets
* Iterative model merging

## 🏃 How to run LFM2

### Transformers.js

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:
```bash
npm i @huggingface/transformers
```

**Example**: Basic example

```js
import { pipeline, TextStreamer } from "@huggingface/transformers";

// Create a text generation pipeline
const generator = await pipeline(
  "text-generation",
  "onnx-community/LFM2-1.2B-ONNX",
  { dtype: "q4", device: "webgpu" },
);

// Define the list of messages
const messages = [
  { role: "system", content: "You are a helpful assistant." },
  { role: "user", content: "What is the capital of France?" },
];

// Generate a response
const output = await generator(messages, {
    max_new_tokens: 512,
    do_sample: false,
    streamer: new TextStreamer(generator.tokenizer, { skip_prompt: true, skip_special_tokens: true }),
});
console.log(output[0].generated_text.at(-1).content);
// The capital of France is Paris.
```


**Example**: Tool calling

```js
import { pipeline, TextStreamer } from "@huggingface/transformers";

// Create a text generation pipeline
const generator = await pipeline(
  "text-generation",
  "onnx-community/LFM2-1.2B-ONNX",
  { dtype: "q4", device: "webgpu" },
);

// Define the tools available to the model
const tools = [
  {
    name: "get_weather",
    description: "Get current weather information for a location",
    parameters: {
      type: "object",
      properties: {
        location: {
          type: "string",
          description: "The city and state, e.g. San Francisco, CA",
        },
        unit: {
          type: "string",
          enum: ["celsius", "fahrenheit"],
          description: "The unit of temperature to use",
        },
      },
      required: ["location"],
    },
  },
];

// Define the list of messages
const messages = [
  { role: "user", content: "What's the weather like in New York?" },
];

// Generate a response
const output = await generator(messages, {
    max_new_tokens: 512,
    do_sample: false,
    streamer: new TextStreamer(generator.tokenizer, { skip_prompt: true, skip_special_tokens: true }),
    tokenizer_encode_kwargs: { tools },
});
console.log(output[0].generated_text.at(-1).content);
// [get_weather(location="New York", unit="fahrenheit")]
```


### ONNXRuntime

```py
from transformers import AutoConfig, AutoTokenizer
import onnxruntime
import numpy as np
from huggingface_hub import snapshot_download

# 1. Load config, processor, and model
model_id = "onnx-community/LFM2-700M-ONNX"
config = AutoConfig.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
eos_token_id = config.eos_token_id

filename = "model.onnx" # Options: "model.onnx", "model_fp16.onnx", "model_q4.onnx", "model_q4f16.onnx"
model_path = snapshot_download(repo_id=model_id, allow_patterns=f"onnx/{filename}*") # Download the graph + weights
session = onnxruntime.InferenceSession(f"{model_path}/onnx/{filename}")

# 2. Prepare inputs
prompt = "What is C. elegans?"
messages = [{"role": "user", "content": prompt}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_dict=True, return_tensors="np")
input_ids = inputs['input_ids']
attention_mask = inputs['attention_mask']
batch_size = input_ids.shape[0]
num_logits_to_keep = np.array(1, dtype=np.int64)

past_cache_values = {}
for inp in session.get_inputs():
    name = inp.name
    shape = inp.shape
    dtype = np.float32 if inp.type == "tensor(float)" else np.float16
    if name.startswith("past_key_values"):
        # Attention KV cache: shape [batch_size, num_kv_heads, 0, head_dim]
        past_cache_values[name] = np.zeros([batch_size, shape[1], 0, shape[3]], dtype=dtype)
    elif name.startswith("past_conv"):
        # Conv cache: shape [batch_size, hidden_size, conv_L_cache]
        past_cache_values[name] = np.zeros([batch_size, shape[1], shape[2]], dtype=dtype)

# 3. Generation loop
max_new_tokens = 1024
generated_tokens = np.array([[]], dtype=np.int64)
for i in range(max_new_tokens):
  logits, *present_cache_values = session.run(None, dict(
      input_ids=input_ids,
      attention_mask=attention_mask,
      num_logits_to_keep=num_logits_to_keep,
      **past_cache_values,
  ))

  ## Update values for next generation loop
  input_ids = logits[:, -1].argmax(-1, keepdims=True)
  attention_mask = np.concatenate([attention_mask, np.ones_like(input_ids, dtype=np.int64)], axis=-1)
  for j, key in enumerate(past_cache_values):
    past_cache_values[key] = present_cache_values[j]
  generated_tokens = np.concatenate([generated_tokens, input_ids], axis=-1)
  if np.isin(input_ids, eos_token_id).any():
      break

  ## (Optional) Streaming
  print(tokenizer.decode(input_ids[0]), end='', flush=True)
print()

# 4. Output result
print(tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0])
```