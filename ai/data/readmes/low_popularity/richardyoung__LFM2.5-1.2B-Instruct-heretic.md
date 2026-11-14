---
library_name: transformers
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
- lfm2.5
- edge
- heretic
- uncensored
- decensored
- abliterated
- reproducible
base_model: LiquidAI/LFM2.5-1.2B-Instruct
base_model_relation: finetune
---
# This is a decensored version of [LiquidAI/LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct), made using [Heretic](https://heretic-project.org) v2.0.0.dev0

> [!TIP]
> **This model is reproducible!**
>
> See the [README](reproduce/README.md) in the `reproduce` directory for more information.

## Abliteration parameters

| Parameter | Value |
| :-------- | :---: |
| **direction_index** | 10.04 |
| **attn.o_proj.max_weight** | 1.50 |
| **attn.o_proj.max_weight_position** | 11.47 |
| **attn.o_proj.min_weight** | 0.42 |
| **attn.o_proj.min_weight_distance** | 7.66 |
| **mlp.down_proj.max_weight** | 1.49 |
| **mlp.down_proj.max_weight_position** | 10.50 |
| **mlp.down_proj.min_weight** | 1.45 |
| **mlp.down_proj.min_weight_distance** | 3.15 |

## Performance

| Metric | This model | Original model ([LiquidAI/LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct)) |
| :----- | :--------: | :---------------------------: |
| **Refusals** | 3/100 | 98/100 |
| **KL divergence** | 0.0585 | 0 *(by definition)* |


## Summary

Abliterated build of [LiquidAI/LFM2.5-1.2B-Instruct](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct), Liquid AI's 1.2B edge model with a hybrid convolution + attention architecture, built for fast on-device inference. GGUF quantizations: [richardyoung/LFM2.5-1.2B-Instruct-heretic-GGUF](https://huggingface.co/richardyoung/LFM2.5-1.2B-Instruct-heretic-GGUF) · Ollama: [richardyoung/lfm2.5-1.2b-instruct-heretic](https://ollama.com/richardyoung/lfm2.5-1.2b-instruct-heretic)

## Abliteration Results

| Metric | Value |
|---|---|
| Base Refusals | 98/100 |
| Abliterated Refusals | 3/100 |
| Refusal Reduction | **97%** |
| KL Divergence | 0.059 |

The very low KL divergence (0.059, far below the 0.5 “damage” threshold) means the model retains essentially all of its original capabilities and coherence.

## Quick Start

### With Ollama

```bash
ollama run richardyoung/lfm2.5-1.2b-instruct-heretic
# or straight from Hugging Face
ollama run hf.co/richardyoung/LFM2.5-1.2B-Instruct-heretic-GGUF
```

### With llama.cpp

```bash
huggingface-cli download richardyoung/LFM2.5-1.2B-Instruct-heretic-GGUF \
    --include "*Q4_K_M*" --local-dir ./models

./llama-cli -m ./models/*Q4_K_M*.gguf -ngl 99
```

### With Python (llama-cpp-python)

```python
from llama_cpp import Llama

llm = Llama.from_pretrained(
    repo_id="richardyoung/LFM2.5-1.2B-Instruct-heretic-GGUF",
    filename="*Q4_K_M*",
    n_gpu_layers=-1,
)

output = llm.create_chat_completion(
    messages=[{"role": "user", "content": "Explain abliteration in simple terms."}]
)
print(output["choices"][0]["message"]["content"])
```

### With Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "richardyoung/LFM2.5-1.2B-Instruct-heretic"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto", torch_dtype="auto")
messages = [{"role": "user", "content": "Explain abliteration in simple terms."}]
inputs = tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt").to(model.device)
print(tokenizer.decode(model.generate(inputs, max_new_tokens=256)[0][inputs.shape[-1]:], skip_special_tokens=True))
```

## What is Abliteration?

Abliteration removes the "refusal direction" from a model's residual stream — a surgical modification that disables safety refusals without retraining. See [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717). [Heretic](https://github.com/p-e-w/heretic) automates it: it searches ablation parameters with an optimizer (200 trials here) and keeps the trials that best trade off fewer refusals against KL divergence from the original model.

## Intended Use

Research, creative writing, education on alignment techniques, and unrestricted local inference. This model will comply with requests the original refuses; use responsibly and in accordance with applicable laws.

## Other Models by richardyoung

- **New Heretic models (reproducible, listed in the [Heretic Grimoire](https://huggingface.co/spaces/heretic-org/Heretic-Grimoire))**: [LFM2.5-1.2B](https://hf.co/richardyoung/LFM2.5-1.2B-Instruct-heretic) | [Granite-4.2-3B](https://hf.co/richardyoung/granite-4.2-3b-heretic) | [Granite-4.2-8B](https://hf.co/richardyoung/granite-4.2-8b-heretic) | [Olmo-3-7B-Think](https://hf.co/richardyoung/Olmo-3-7B-Think-heretic) | [Phi-4-mini](https://hf.co/richardyoung/Phi-4-mini-instruct-heretic) | [DeepSeek-R1-0528-Qwen3-8B](https://hf.co/richardyoung/DeepSeek-R1-0528-Qwen3-8B-heretic) | [Agents-A1-4B](https://hf.co/richardyoung/Agents-A1-4B-heretic) | [FrogNano-4B](https://hf.co/richardyoung/FrogNano-4B-2609-heretic) | [Muse-Glimmer-30B](https://hf.co/richardyoung/Muse-Glimmer-30B-heretic) | [Hemmingway-1](https://hf.co/richardyoung/Hemmingway-1-heretic)
- **Abliterated/Uncensored models**: [Qwen2.5-7B](https://hf.co/richardyoung/Qwen2.5-7B-Instruct-abliterated-GGUF) | [Qwen3-14B](https://hf.co/richardyoung/Qwen3-14B-abliterated-GGUF) | [DeepSeek-R1-32B](https://hf.co/richardyoung/Deepseek-R1-Distill-Qwen-32b-uncensored) | [Qwen3-8B](https://hf.co/richardyoung/Qwen3-8B-Abliterated)
- **OCR & Vision**: [MiniCPM-V-4.6 GGUF](https://hf.co/richardyoung/MiniCPM-V-4.6-GGUF) | [dots.mocr GGUF](https://hf.co/richardyoung/dots.mocr-GGUF) | [Unlimited-OCR GGUF](https://hf.co/richardyoung/Unlimited-OCR-GGUF) | [olmOCR GGUF](https://hf.co/richardyoung/olmOCR-2-7B-1025-GGUF) | [LightOnOCR-3-4B GGUF](https://hf.co/richardyoung/LightOnOCR-3-4B-GGUF) | [WeVisDoc-4B GGUF](https://hf.co/richardyoung/WeVisDoc-4B-GGUF) | [Xiaomi-OCR-0 GGUF](https://hf.co/richardyoung/Xiaomi-OCR-0-GGUF)
- **MLX quantizations (Apple Silicon)**: [Kimi-K2 series](https://hf.co/richardyoung/Kimi-K2-Instruct-0905-MLX-4bit) | [olmOCR MLX](https://hf.co/richardyoung/olmOCR-2-7B-1025-MLX-4bit)
- **Healthcare/Medical**: [Synthea 575K patients dataset](https://hf.co/datasets/richardyoung/synthea-575k-patients) | [CardioEmbed](https://hf.co/richardyoung/CardioEmbed)
- **Research**: [LLM Instruction-Following Evaluation](https://hf.co/richardyoung/llm-instruction-following-paper) (arxiv:2510.18892)

*Built & maintained by [Richard Young](https://deepneuro.ai/richard) · DeepNeuro*

The original model card follows below.

-----


<div align="center">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI" 
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
<div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>
</div>

<br>

# LFM2.5-1.2B-Instruct

LFM2.5 is a new family of hybrid models designed for **on-device deployment**. It builds on the LFM2 architecture with extended pre-training and reinforcement learning.

- **Best-in-class performance**: A 1.2B model rivaling much larger models, bringing high-quality AI to your pocket.
- **Fast edge inference**: 239 tok/s decode on AMD CPU, 82 tok/s on mobile NPU. Runs under 1GB of memory with day-one support for llama.cpp, MLX, and vLLM.
- **Scaled training**: Extended pre-training from 10T to 28T tokens and large-scale multi-stage reinforcement learning.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/dxnYF2fuLpulismtFSGFi.png)

Find more information about LFM2.5 in our [blog post](https://www.liquid.ai/blog/introducing-lfm2-5-the-next-generation-of-on-device-ai).

## 🗒️ Model Details

| Model | Parameters | Description |
|-------|------------|-------------|
| [LFM2.5-1.2B-Base](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Base) | 1.2B | Pre-trained base model for fine-tuning |
| [**LFM2.5-1.2B-Instruct**](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct) | 1.2B | General-purpose instruction-tuned model |
| [LFM2.5-1.2B-Thinking](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Thinking) | 1.2B | General-purpose reasoning model |
| [LFM2.5-1.2B-JP](https://huggingface.co/LiquidAI/LFM2.5-1.2B-JP) | 1.2B | Japanese-optimized chat model |
| [LFM2.5-VL-1.6B](https://huggingface.co/LiquidAI/LFM2.5-VL-1.6B) | 1.6B | Vision-language model with fast inference |
| [LFM2.5-Audio-1.5B](https://huggingface.co/LiquidAI/LFM2.5-Audio-1.5B) | 1.5B | Audio-language model for speech and text I/O |

LFM2.5-1.2B-Instruct is a general-purpose text-only model with the following features:

- **Number of parameters**: 1.17B
- **Number of layers**: 16 (10 double-gated convolution blocks + 6 GQA blocks)
- **Training budget**: 28T tokens
- **Context length**: 32,768 tokens
- **Vocabulary size**: 65,536
- **Knowledge cutoff**: Mid-2024
- **Languages**: English, Arabic, Chinese, French, German, Japanese, Korean, Spanish
- **Generation parameters**:
  - `temperature: 0.1`
  - `top_k: 50`
  - `repetition_penalty: 1.05`

| Model | Description |
|-------|-------------|
| [**LFM2.5-1.2B-Instruct**](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct) | Original model checkpoint in native format. Best for fine-tuning or inference with Transformers and vLLM. |
| [LFM2.5-1.2B-Instruct-GGUF](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-GGUF) | Quantized format for llama.cpp and compatible tools. Optimized for CPU inference and local deployment with reduced memory usage. |
| [LFM2.5-1.2B-Instruct-ONNX](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-ONNX) | ONNX Runtime format for cross-platform deployment. Enables hardware-accelerated inference across diverse environments (cloud, edge, mobile). |
| [LFM2.5-1.2B-Instruct-MLX](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-MLX-8bit) | MLX format for Apple Silicon. Optimized for fast inference on Mac devices using the MLX framework. |
| [LFM2.5-1.2B-Instruct-DSpark](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-DSpark) | Speculative decoding drafter (296M). Pair it with this model for ~2.1x faster decoding with identical outputs. |

We recommend using it for agentic tasks, data extraction, and RAG. It is not recommended for knowledge-intensive tasks and programming.

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

### Tool Use

LFM2.5 supports function calling as follows:

1. **Function definition**: We recommend providing the list of tools as a JSON object in the system prompt. You can also use the [`tokenizer.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_extras#passing-tools) function with tools.
2. **Function call**: By default, LFM2.5 writes Pythonic function calls (a Python list between `<|tool_call_start|>` and `<|tool_call_end|>` special tokens), as the assistant answer. You can override this behavior by asking the model to output JSON function calls in the system prompt.
3. **Function execution**: The function call is executed, and the result is returned as a "tool" role.
4. **Final answer**: LFM2 interprets the outcome of the function call to address the original user prompt in plain text.

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
> ⚡ **Faster decoding**: attach [LFM2.5-1.2B-Instruct-DSpark](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct-DSpark), a 296M speculative-decoding drafter, for ~2.1x faster decoding in SGLang and ~2.5x on Apple silicon via Metal with exactly the same outputs.

Here's a quick start example with Transformers:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer

model_id = "LiquidAI/LFM2.5-1.2B-Instruct"
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
).to(model.device)

output = model.generate(
    input_ids,
    do_sample=True,
    temperature=0.1,
    top_k=50,
    repetition_penalty=1.05,
    max_new_tokens=512,
    streamer=streamer,
)
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
| GRPO ([Unsloth](https://github.com/unslothai/unsloth)) | GRPO with LoRA using Unsloth. | <a href="https://docs.liquid.ai/lfm/fine-tuning/unsloth">Link</a> | <a href="https://colab.research.google.com/drive/1mIikXFaGvcW4vXOZXLbVTxfBRw_XsXa5?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| GRPO ([TRL](https://github.com/huggingface/trl)) | GRPO with LoRA using TRL. | <a href="https://docs.liquid.ai/lfm/fine-tuning/trl">Link</a> | <a href="https://colab.research.google.com/github/Liquid4All/cookbook/blob/main/finetuning/notebooks/grpo_for_verifiable_tasks.ipynb"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |

## 📊 Performance

### Benchmarks

We compared LFM2.5-1.2B-Instruct with relevant sub-2B models on a diverse suite of benchmarks.

| Model | GPQA | MMLU-Pro | IFEval | IFBench | Multi-IF | AIME25 | BFCLv3 |
|-------|------|----------|--------|---------|----------|--------|--------|
| **LFM2.5-1.2B-Instruct** | 38.89 | 44.35 | 86.23 | 47.33 | 60.98 | 14.00 | 49.12 |
| Qwen3-1.7B (instruct)| 34.85 | 42.91 | 73.68 | 21.33 | 56.48 | 9.33 | 46.30 |
| Granite 4.0-1B | 24.24 | 33.53 | 79.61 | 21.00 | 43.65 | 3.33 | 52.43 |
| Llama 3.2 1B Instruct | 16.57 | 20.80 | 52.37 | 15.93 | 30.16 | 0.33 | 21.44 |
| Gemma 3 1B IT | 24.24 | 14.04 | 63.25 | 20.47 | 44.31 | 1.00 | 16.64 |

GPQA, MMLU-Pro, IFBench, and AIME25 follow [ArtificialAnalysis's methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking). For IFEval and Multi-IF, we report the average score across strict and loose prompt and instruction accuracies. For BFCLv3, we report the final weighted average score with a custom Liquid handler to support our tool use template. 

### Inference speed

LFM2.5-1.2B-Instruct offers extremely fast inference speed on CPUs with a low memory profile compared to similar-sized models.

![image](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/dbbI-15p9re2ROhAkqnZm.png)

In addition, we are partnering with AMD, Qualcomm, and Nexa AI to bring the LFM2.5 family to NPUs. These optimized models are available through our partners, enabling highly efficient on-device inference. 
The following numbers have been calculated using 1K prefill and 100 decode tokens:

| Device                                               | Inference | Framework        | Model                | Prefill (tok/s) | Decode (tok/s) | Memory (GB) |
| ---------------------------------------------------- | --------- | ---------------- | -------------------- | --------------- | -------------- | ----------- |
| Qualcomm Snapdragon® X Elite                         | NPU       | NexaML           | LFM2.5-1.2B-Instruct | 2591            | 63             | 0.9GB       |
| Qualcomm Snapdragon® Gen4 (ROG Phone9 Pro)           | NPU       | NexaML           | LFM2.5-1.2B-Instruct | 4391            | 82             | 0.9GB       |
| Qualcomm Snapdragon® Gen4 (Samsung Galaxy S25 Ultra) | CPU       | llama.cpp (Q4_0) | LFM2.5-1.2B-Instruct | 335             | 70             | 719MB       |
| Qualcomm Snapdragon® Gen4 (Samsung Galaxy S25 Ultra) | CPU       | llama.cpp (Q4_0) | Qwen3-1.7B           | 181             | 40             | 1306MB      |

These capabilities unlock new deployment scenarios across various devices, including vehicles, mobile devices, laptops, IoT devices, and embedded systems.

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).

## Citation

```bibtex
@article{liquidai2025lfm2,
  title={LFM2 Technical Report},
  author={Liquid AI},
  journal={arXiv preprint arXiv:2511.23404},
  year={2025}
}
```