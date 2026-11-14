---
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
- pt
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
library_name: transformers.js
---

<div align="center">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/VmrjMZg7WYfMX5YFHuZ-P.png" 
    alt="Liquid AI" 
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
  <div style="display: flex; justify-content: center; gap: 0.5em; margin-bottom: 1em;">
    <a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • 
    <a href="https://docs.liquid.ai/lfm"><strong>Documentation</strong></a> • 
    <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a>
  </div>
</div>

# LFM2-24B-A2B

LFM2 is a family of hybrid models designed for on-device deployment. LFM2-24B-A2B is the largest model in the family, scaling the architecture to 24 billion parameters while keeping inference efficient.

- **Best-in-class efficiency**: A 24B MoE model with only 2B active parameters per token, fitting in 32 GB of RAM for deployment on consumer laptops and desktops.
- **Fast edge inference**: 112 tok/s decode on AMD CPU, 293 tok/s on H100. Fits in 32B GB of RAM with day-one support llama.cpp, vLLM, and SGLang.
- **Predictable scaling**: Quality improves log-linearly from 350M to 24B total parameters, confirming the LFM2 hybrid architecture scales reliably across nearly two orders of magnitude.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/VhdjtAT5zWTWdVYgW69O0.png)

Find more information about LFM2-24B-A2B in our [blog post](www.liquid.ai/blog/lfm2-24b-a2b).

## 🗒️ Model Details

LFM2-24B-A2B is a general-purpose instruct model (without reasoning traces) with the following features:

| Property              | [**LFM2-8B-A1B**](https://huggingface.co/LiquidAI/LFM2-8B-A1B) | [**LFM2-24B-A2B**](https://huggingface.co/LiquidAI/LFM2-24B-A2B) | 
| --------------------- | ----------------------------- | ----------------------------- |
| **Total parameters**  | 8.3B                          | 24B |
| **Active parameters** | 1.5B                          | 2.3B |
| **Layers**            | 24 (18 conv + 6 attn)         | 40 (30 conv + 10 attn) |
| **Context length**    | 32,768 tokens                 | 32,768 tokens |
| **Vocabulary size**   | 65,536                        | 65,536 |
| **Training precision**| Mixed BF16/FP8                | Mixed BF16/FP8 |
| **Training budget**   | 12 trillion tokens            | 17 trillion tokens |
| **License**           | LFM Open License v1.0         | LFM Open License v1.0 |

**Supported languages**: English, Arabic, Chinese, French, German, Japanese, Korean, Spanish, Portuguese

**Generation parameters**:
- `temperature: 0.1`
- `top_k: 50`
- `repetition_penalty: 1.05`

We recommend the following use cases:

- **Agentic tool use**: Native function calling, web search, structured outputs. Ideal as the fast inner-loop model in multi-step agent pipelines.
- **Offline document summarization and Q&A**: Run entirely on consumer hardware for privacy-sensitive workflows (legal, medical, corporate).
- **Privacy-preserving customer support agent**: Deployed on-premise at a company, handles multi-turn support conversations with tool access (database lookups, ticket creation) without data leaving the network.
- **Local RAG pipelines**: Serve as the generation backbone in retrieval-augmented setups on a single machine without GPU servers.

### Chat Template

LFM2-24B-A2B uses a ChatML-like format. See the [Chat Template documentation](https://docs.liquid.ai/lfm/key-concepts/chat-template) for details. Example:

```
<|startoftext|><|im_start|>system
You are a helpful assistant trained by Liquid AI.<|im_end|>
<|im_start|>user
What is C. elegans?<|im_end|>
<|im_start|>assistant
```

You can use [`tokenizer.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#using-applychattemplate) to format your messages automatically.

### Tool Use

LFM2-24B-A2B supports function calling as follows:

1. **Function definition**: We recommend providing the list of tools as a JSON object in the system prompt. You can also use the [`tokenizer.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_extras#passing-tools) function with tools.
2. **Function call**: By default, LFM2-24B-A2B writes Pythonic function calls (a Python list between `<|tool_call_start|>` and `<|tool_call_end|>` special tokens), as the assistant answer. You can override this behavior by asking the model to output JSON function calls in the system prompt.
3. **Function execution**: The function call is executed, and the result is returned as a "tool" role.
4. **Final answer**: LFM2-24B-A2B interprets the outcome of the function call to address the original user prompt in plain text.

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

## 🏃 Inference

LFM2-24B-A2B is supported by many inference frameworks. See the [Inference documentation](https://docs.liquid.ai/lfm/inference/transformers) for the full list.

| Name | Description | Docs | Notebook |
|------|-------------|------|:--------:|
| [Transformers](https://github.com/huggingface/transformers) | Simple inference with direct access to model internals. | <a href="https://docs.liquid.ai/lfm/inference/transformers">Link</a> | <a href="https://colab.research.google.com/drive/1_q3jQ6LtyiuPzFZv7Vw8xSfPU5FwkKZY?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| [vLLM](https://github.com/vllm-project/vllm) | High-throughput production deployments with GPU. | <a href="https://docs.liquid.ai/lfm/inference/vllm">Link</a> | <a href="https://colab.research.google.com/drive/1VfyscuHP8A3we_YpnzuabYJzr5ju0Mit?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| [llama.cpp](https://github.com/ggml-org/llama.cpp) | Cross-platform inference with CPU offloading. | <a href="https://docs.liquid.ai/lfm/inference/llama-cpp">Link</a> | <a href="https://colab.research.google.com/drive/1ohLl3w47OQZA4ELo46i5E4Z6oGWBAyo8?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| [MLX](https://github.com/ml-explore/mlx) | Apple's machine learning framework optimized for Apple Silicon. | <a href="https://docs.liquid.ai/lfm/inference/mlx">Link</a> | — |
| [LM Studio](https://lmstudio.ai/) | Desktop application for running LLMs locally. | <a href="https://docs.liquid.ai/lfm/inference/lm-studio">Link</a> | — |

### Transformers.js

If you haven't already, you can install the [Transformers.js](https://huggingface.co/docs/transformers.js) JavaScript library from [NPM](https://www.npmjs.com/package/@huggingface/transformers) using:

```sh
npm i @huggingface/transformers
```

You can then use the model as follows:
```js
import { pipeline, TextStreamer } from "@huggingface/transformers";

// Create a text generation pipeline
const generator = await pipeline(
  "text-generation",
  "onnx-community/LFM2-24B-A2B-ONNX",
  { dtype: "q4f16", device: "webgpu" },
);

// Define the list of messages
const messages = [
  { role: "user", content: "What's the capital of France?" },
];

// Generate a response
const output = await generator(messages, {
  max_new_tokens: 512,
  do_sample: false,
  streamer: new TextStreamer(generator.tokenizer, {
    skip_prompt: true,
    skip_special_tokens: true,
  }),
});
console.log(output[0].generated_text.at(-1).content);
```

Or try out our [online WebGPU demo](https://huggingface.co/spaces/LiquidAI/LFM2-MoE-WebGPU):

<video src="https://cdn-uploads.huggingface.co/production/uploads/61b253b7ac5ecaae3d1efe0c/JL2p1zWY8q3ZxxSEjgtV1.mp4" autoplay controls loop></video>

### ONNX Runtime

Here's a quick start example with ONNX Runtime:

```python
from transformers import AutoConfig, AutoTokenizer
import onnxruntime
import numpy as np
from huggingface_hub import snapshot_download

# 1. Load config, processor, and model
model_id = "onnx-community/LFM2-24B-A2B-ONNX"
config = AutoConfig.from_pretrained(model_id)
tokenizer = AutoTokenizer.from_pretrained(model_id)
eos_token_id = config.eos_token_id

filename = "model_q4f16.onnx" # Options: "model_fp16.onnx", "model_q4f16.onnx"
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

## 🔧 Fine-Tuning

| Name | Description | Docs | Notebook |
|------|-------------|------|----------|
| CPT ([Unsloth](https://github.com/unslothai/unsloth)) | Continued Pre-Training using Unsloth for text completion. | <a href="https://docs.liquid.ai/lfm/fine-tuning/unsloth">Link</a> | <a href="https://colab.research.google.com/drive/10fm7eNMezs-DSn36mF7vAsNYlOsx9YZO?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| CPT ([Unsloth](https://github.com/unslothai/unsloth)) | Continued Pre-Training using Unsloth for translation. | <a href="https://docs.liquid.ai/lfm/fine-tuning/unsloth">Link</a> | <a href="https://colab.research.google.com/drive/1gaP8yTle2_v35Um8Gpu9239fqbU7UgY8?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT ([Unsloth](https://github.com/unslothai/unsloth)) | Supervised Fine-Tuning with LoRA using Unsloth. | <a href="https://docs.liquid.ai/lfm/fine-tuning/unsloth">Link</a> | <a href="https://colab.research.google.com/drive/1vGRg4ksRj__6OLvXkHhvji_Pamv801Ss?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT ([TRL](https://github.com/huggingface/trl)) | Supervised Fine-Tuning with LoRA using TRL. | <a href="https://docs.liquid.ai/lfm/fine-tuning/trl">Link</a> | <a href="https://colab.research.google.com/drive/1j5Hk_SyBb2soUsuhU0eIEA9GwLNRnElF?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| DPO ([TRL](https://github.com/huggingface/trl)) | Direct Preference Optimization with LoRA using TRL. | <a href="https://docs.liquid.ai/lfm/fine-tuning/trl">Link</a> | <a href="https://colab.research.google.com/drive/1MQdsPxFHeZweGsNx4RH7Ia8lG8PiGE1t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| GRPO ([Unsloth](https://github.com/unslothai/unsloth)) | GRPO with LoRA using Unsloth. | <a href="https://docs.liquid.ai/lfm/fine-tuning/unsloth">Link</a> | <a href="https://colab.research.google.com/drive/1mIikXFaGvcW4vXOZXLbVTxfBRw_XsXa5?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| GRPO ([TRL](https://github.com/huggingface/trl)) | GRPO with LoRA using TRL. | <a href="https://docs.liquid.ai/lfm/fine-tuning/trl">Link</a> | <a href="https://colab.research.google.com/github/Liquid4All/cookbook/blob/main/finetuning/notebooks/grpo_for_verifiable_tasks.ipynb"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |

## 📊 Performance

### CPU Inference

We compared LFM2-24B-A2B against two popular MoE models of similar size: Qwen3-30B-A3B-Instruct-2507 (30.5B total, 3.3B active parameters) and gpt-oss-20b (21B total, 3.6B active parameters). We measured both prefill and decode throughputs with Q4_K_M versions of these models using llama.cpp on AMD Ryzen AI Max+ 395.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/voUOPTqOXQaiEEm_6vY2j.png)

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/7G2mtNj0vxSbUXnovmbzs.png)

### GPU Inference

We also report throughput (total tokens / wall time) achieved with vLLM on a single H100 SXM5 GPU.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/5b2a3bfGYmyO16Gxos4dH.png)

## Contact

For enterprise solutions and edge deployment, contact [sales@liquid.ai](mailto:sales@liquid.ai).

## Citation

```bibtex
@article{liquidAI202624B,
  author = {Liquid AI},
  title = {LFM2.5-24B-A2B: Scaling Up the LFM2 Architecture},
  journal = {Liquid AI Blog},
  year = {2026},
  note = {www.liquid.ai/blog/},
}
```

```bibtex
@article{liquidai2025lfm2,
  title={LFM2 Technical Report},
  author={Liquid AI},
  journal={arXiv preprint arXiv:2511.23404},
  year={2025}
}
```