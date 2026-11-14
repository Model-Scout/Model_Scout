---
license: apache-2.0
datasets:
- TeichAI/gemini-2.5-flash-11000x
base_model: DavidAU/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
tags:
- thinking
- reasoning
- Gemini Flash
- creative
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- story generation
- scene continue
- storytelling
- fiction story
- science fiction
- romance
- all genres
- story
- writing
- vivid prosing
- vivid writing
- fiction
- roleplaying
- bfloat16
- role play
- 128k context
- llama3.3
- llama-3
- llama-3.3
- unsloth
- finetune
- llama-cpp
- gguf-my-repo
pipeline_tag: text-generation
library_name: transformers
---

# kenonix/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k-Q4_K_M-GGUF
This model was converted to GGUF format from [`DavidAU/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k`](https://huggingface.co/DavidAU/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/DavidAU/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo kenonix/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k-Q4_K_M-GGUF --hf-file llama-3.3-8b-thinking-gemini-flash-11000x-128k-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo kenonix/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k-Q4_K_M-GGUF --hf-file llama-3.3-8b-thinking-gemini-flash-11000x-128k-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo kenonix/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k-Q4_K_M-GGUF --hf-file llama-3.3-8b-thinking-gemini-flash-11000x-128k-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo kenonix/Llama-3.3-8B-Thinking-Gemini-Flash-11000x-128k-Q4_K_M-GGUF --hf-file llama-3.3-8b-thinking-gemini-flash-11000x-128k-q4_k_m.gguf -c 2048
```
