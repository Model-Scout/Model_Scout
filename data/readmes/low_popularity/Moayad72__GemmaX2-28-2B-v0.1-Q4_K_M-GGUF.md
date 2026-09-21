---
license: gemma
license_name: license
license_link: LICENSE
metrics:
- bleu
- comet
base_model: ModelSpace/GemmaX2-28-2B-v0.1
pipeline_tag: translation
library_name: transformers
language:
- ar
- bn
- cs
- de
- en
- es
- fa
- fr
- he
- hi
- id
- it
- ja
- km
- ko
- lo
- ms
- my
- nl
- pl
- pt
- ru
- th
- tl
- tr
- ur
- vi
- zh
tags:
- llama-cpp
- gguf-my-repo
---

# Moayad72/GemmaX2-28-2B-v0.1-Q4_K_M-GGUF
This model was converted to GGUF format from [`ModelSpace/GemmaX2-28-2B-v0.1`](https://huggingface.co/ModelSpace/GemmaX2-28-2B-v0.1) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/ModelSpace/GemmaX2-28-2B-v0.1) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Moayad72/GemmaX2-28-2B-v0.1-Q4_K_M-GGUF --hf-file gemmax2-28-2b-v0.1-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Moayad72/GemmaX2-28-2B-v0.1-Q4_K_M-GGUF --hf-file gemmax2-28-2b-v0.1-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo Moayad72/GemmaX2-28-2B-v0.1-Q4_K_M-GGUF --hf-file gemmax2-28-2b-v0.1-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Moayad72/GemmaX2-28-2B-v0.1-Q4_K_M-GGUF --hf-file gemmax2-28-2b-v0.1-q4_k_m.gguf -c 2048
```
