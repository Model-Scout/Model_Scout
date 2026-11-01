---
base_model: tvall43/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_5_moe
- qwen
- qwen3.5
- reasoning
- chain-of-thought
- llama-cpp
- gguf-my-repo
license: apache-2.0
language:
- zh
- en
- ko
pipeline_tag: text-generation
datasets:
- nohurry/Opus-4.6-Reasoning-3000x-filtered
- Jackrong/Qwen3.5-reasoning-700x
---

# brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF
This model was converted to GGUF format from [`tvall43/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap`](https://huggingface.co/tvall43/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/tvall43/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF --hf-file qwen3.5-14b-a3b-claude-4.6-opus-reasoning-distilled-reap-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF --hf-file qwen3.5-14b-a3b-claude-4.6-opus-reasoning-distilled-reap-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF --hf-file qwen3.5-14b-a3b-claude-4.6-opus-reasoning-distilled-reap-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo brunopio/Qwen3.5-14B-A3B-Claude-4.6-Opus-Reasoning-Distilled-reap-Q4_K_M-GGUF --hf-file qwen3.5-14b-a3b-claude-4.6-opus-reasoning-distilled-reap-q4_k_m.gguf -c 2048
```
