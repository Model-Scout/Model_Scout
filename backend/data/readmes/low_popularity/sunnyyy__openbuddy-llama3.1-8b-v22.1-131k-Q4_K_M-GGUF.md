---
base_model: OpenBuddy/openbuddy-llama3.1-8b-v22.1-131k
language:
- zh
- en
- fr
- de
- ja
- ko
- it
- fi
license: other
license_name: llama3.1
license_link: https://github.com/meta-llama/llama-models/blob/main/models/llama3_1/LICENSE
pipeline_tag: text-generation
tags:
- llama-3.1
- llama-cpp
- gguf-my-repo
---

# sunnyyy/openbuddy-llama3.1-8b-v22.1-131k-Q4_K_M-GGUF
This model was converted to GGUF format from [`OpenBuddy/openbuddy-llama3.1-8b-v22.1-131k`](https://huggingface.co/OpenBuddy/openbuddy-llama3.1-8b-v22.1-131k) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/OpenBuddy/openbuddy-llama3.1-8b-v22.1-131k) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo sunnyyy/openbuddy-llama3.1-8b-v22.1-131k-Q4_K_M-GGUF --hf-file openbuddy-llama3.1-8b-v22.1-131k-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo sunnyyy/openbuddy-llama3.1-8b-v22.1-131k-Q4_K_M-GGUF --hf-file openbuddy-llama3.1-8b-v22.1-131k-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo sunnyyy/openbuddy-llama3.1-8b-v22.1-131k-Q4_K_M-GGUF --hf-file openbuddy-llama3.1-8b-v22.1-131k-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo sunnyyy/openbuddy-llama3.1-8b-v22.1-131k-Q4_K_M-GGUF --hf-file openbuddy-llama3.1-8b-v22.1-131k-q4_k_m.gguf -c 2048
```
