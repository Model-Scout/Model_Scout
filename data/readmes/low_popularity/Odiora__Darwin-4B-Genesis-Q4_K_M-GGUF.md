---
license: apache-2.0
base_model: FINAL-Bench/Darwin-4B-Genesis
tags:
- merge
- evolutionary-merge
- darwin
- darwin-v6
- model-mri
- cross-architecture
- ffn-crossbreed
- cma-es
- hybrid-vigor
- transformer-mamba
- reasoning
- gemma4
- qwen3.5
- gated-deltanet
- korean
- multilingual
- gpqa
- open-source
- apache-2.0
- world-first
- llama-cpp
- gguf-my-repo
language:
- ko
- en
- zh
- ja
- de
- fr
- es
pipeline_tag: text-generation
model-index:
- name: Darwin-4B-Genesis
  results:
  - task:
      type: text-generation
      name: Korean Cultural Understanding
    dataset:
      name: CLIcK
      type: EunsuKim/CLIcK
    metrics:
    - type: accuracy
      value: 92.0
      name: Accuracy
      verified: false
  - task:
      type: text-generation
      name: Multi-Step Reasoning
    dataset:
      name: MuSR
      type: TAUR-Lab/MuSR
    metrics:
    - type: accuracy
      value: 70.0
      name: Accuracy
      verified: false
---

# Odiora/Darwin-4B-Genesis-Q4_K_M-GGUF
This model was converted to GGUF format from [`FINAL-Bench/Darwin-4B-Genesis`](https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/FINAL-Bench/Darwin-4B-Genesis) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Odiora/Darwin-4B-Genesis-Q4_K_M-GGUF --hf-file darwin-4b-genesis-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Odiora/Darwin-4B-Genesis-Q4_K_M-GGUF --hf-file darwin-4b-genesis-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo Odiora/Darwin-4B-Genesis-Q4_K_M-GGUF --hf-file darwin-4b-genesis-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo Odiora/Darwin-4B-Genesis-Q4_K_M-GGUF --hf-file darwin-4b-genesis-q4_k_m.gguf -c 2048
```
