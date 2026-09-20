---
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
license: apache-2.0
library_name: vllm
inference: false
base_model: huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: image-text-to-text
tags:
- abliterated
- uncensored
- llama-cpp
- gguf-my-repo
---

# maerong3/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-Q4_K_M-GGUF
This model was converted to GGUF format from [`huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated`](https://huggingface.co/huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/huihui-ai/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo maerong3/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-Q4_K_M-GGUF --hf-file huihui-mistral-small-3.2-24b-instruct-2506-abliterated-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo maerong3/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-Q4_K_M-GGUF --hf-file huihui-mistral-small-3.2-24b-instruct-2506-abliterated-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo maerong3/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-Q4_K_M-GGUF --hf-file huihui-mistral-small-3.2-24b-instruct-2506-abliterated-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo maerong3/Huihui-Mistral-Small-3.2-24B-Instruct-2506-abliterated-Q4_K_M-GGUF --hf-file huihui-mistral-small-3.2-24b-instruct-2506-abliterated-q4_k_m.gguf -c 2048
```
