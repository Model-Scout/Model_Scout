---
language:
- tr
- en
- de
- es
- fr
- ru
- zh
- ja
- ko
license: mit
tags:
- turkish
- türkiye
- reasoning
- ai
- lamapi
- gemma3
- next
- next-x1
- text-generation
- open-source
- 14b
- large-language-model
- llm
- transformer
- artificial-intelligence
- machine-learning
- nlp
- multilingual
- instruction-tuned
- chat
- generative-ai
- optimized
- trl
- sft
- cognitive
- analytical
- enterprise
- llama-cpp
- gguf-my-repo
pipeline_tag: text-generation
datasets:
- mlabonne/FineTome-100k
- CognitiveKernel/CognitiveKernel-Pro-SFT
- OpenSPG/KAG-Thinker-training-dataset
- Gryphe/ChatGPT-4o-Writing-Prompts
- QuixiAI/dolphin-r1
- uclanlp/Brief-Pro
library_name: transformers
base_model: Lamapi/next-14b
---

# Lamapi/next-14b-Q4_K_M-GGUF
This model was converted to GGUF format from [`Lamapi/next-14b`](https://huggingface.co/Lamapi/next-14b) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Lamapi/next-14b) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Lamapi/next-14b-Q4_K_M-GGUF --hf-file next-14b-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Lamapi/next-14b-Q4_K_M-GGUF --hf-file next-14b-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo Lamapi/next-14b-Q4_K_M-GGUF --hf-file next-14b-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Lamapi/next-14b-Q4_K_M-GGUF --hf-file next-14b-q4_k_m.gguf -c 2048
```
