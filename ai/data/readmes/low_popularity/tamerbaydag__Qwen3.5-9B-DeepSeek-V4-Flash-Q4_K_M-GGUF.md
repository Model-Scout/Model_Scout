---
base_model: Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5
- reasoning
- distillation
- deepseek
- deepseek-v4
- sft
- long-cot
- chain-of-thought
- efficient-inference
- agent
- multilingual
- llama-cpp
- gguf-my-repo
license: apache-2.0
language:
- en
- zh
- ko
- ja
- es
- ru
pipeline_tag: image-text-to-text
datasets:
- Jackrong/DeepSeek-V4-Distill-8000x
---

# tamerbaydag/Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M-GGUF
This model was converted to GGUF format from [`Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash`](https://huggingface.co/Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Jackrong/Qwen3.5-9B-DeepSeek-V4-Flash) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo tamerbaydag/Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M-GGUF --hf-file qwen3.5-9b-deepseek-v4-flash-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo tamerbaydag/Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M-GGUF --hf-file qwen3.5-9b-deepseek-v4-flash-q4_k_m.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

Step 1: Clone llama.cpp from GitHub.
```
git clone https://github.com/ggerganov/llama.cpp
```

Step 2: Move into the llama.cpp folder and build it with `LLAMA_CURL=1` flag along with other hardware-specific flags (for ex: LLAMA_CUDA=1 for Nvidia GPUs on Linux).
```
cd llama.cpp && LLAMA_CURL=1 make
```

Step 3: Run inference through the main binary.
```
./llama-cli --hf-repo tamerbaydag/Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M-GGUF --hf-file qwen3.5-9b-deepseek-v4-flash-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo tamerbaydag/Qwen3.5-9B-DeepSeek-V4-Flash-Q4_K_M-GGUF --hf-file qwen3.5-9b-deepseek-v4-flash-q4_k_m.gguf -c 2048
```
