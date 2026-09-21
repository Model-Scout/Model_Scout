---
license: apache-2.0
library_name: transformers
pipeline_tag: image-text-to-text
base_model: Jiunsong/SuperQwen3.8-27b-abliterated
base_model_relation: finetune
tags:
- qwen3.8
- qwen3.5
- multimodal
- image-text-to-text
- reasoning
- tool-calling
- long-context
- 262k-context
- uncensored
- abliterated
- obliteratus
- supertune
- vllm
- bf16
- full-precision
- llama-cpp
- gguf-my-repo
language:
- en
- ko
---

# McG-221/SuperQwen3.8-27b-abliterated-Q8_0-GGUF
This model was converted to GGUF format from [`Jiunsong/SuperQwen3.8-27b-abliterated`](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Jiunsong/SuperQwen3.8-27b-abliterated) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo McG-221/SuperQwen3.8-27b-abliterated-Q8_0-GGUF --hf-file superqwen3.8-27b-abliterated-q8_0.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo McG-221/SuperQwen3.8-27b-abliterated-Q8_0-GGUF --hf-file superqwen3.8-27b-abliterated-q8_0.gguf -c 2048
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
./llama-cli --hf-repo McG-221/SuperQwen3.8-27b-abliterated-Q8_0-GGUF --hf-file superqwen3.8-27b-abliterated-q8_0.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo McG-221/SuperQwen3.8-27b-abliterated-Q8_0-GGUF --hf-file superqwen3.8-27b-abliterated-q8_0.gguf -c 2048
```
