---
license: apache-2.0
base_model:
- FINAL-Bench/Darwin-36B-Opus
tags:
- darwin
- darwin-v7
- evolutionary-merge
- reasoning
- advanced-reasoning
- chain-of-thought
- thinking
- qwen3.6
- qwen
- moe
- mixture-of-experts
- claude-opus
- distillation
- multilingual
- gpqa
- benchmark
- open-source
- apache-2.0
- hybrid-vigor
- proto-agi
- vidraft
- eval-results
- llama-cpp
- gguf-my-repo
language:
- en
- zh
- ko
- ja
- de
- fr
- es
- ru
- ar
- multilingual
pipeline_tag: text-generation
library_name: transformers
model-index:
- name: Darwin-36B-Opus
  results:
  - task:
      type: text-generation
      name: Graduate-Level Reasoning
    dataset:
      name: GPQA Diamond
      type: Idavidrein/gpqa
      config: gpqa_diamond
      split: train
    metrics:
    - type: accuracy
      value: 88.4
      name: Accuracy
      verified: false
  - task:
      type: text-generation
      name: Multilingual Knowledge
    dataset:
      name: MMMLU
      type: openai/MMMLU
    metrics:
    - type: accuracy
      value: 85
      name: Accuracy
      verified: false
---

# wahidmounir/Darwin-36B-Opus-Q4_K_M-GGUF
This model was converted to GGUF format from [`FINAL-Bench/Darwin-36B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-36B-Opus) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Asley43/iera_codar) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo wahidmounir/iera_codar-Q4_K_M-GGUF --hf-file iera_codar-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo wahidmounir/iera_codar-Q4_K_M-GGUF --hf-file iera_codar-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo wahidmounir/iera_codar-Q4_K_M-GGUF --hf-file iera_codar-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo wahidmounir/iera_codar-Q4_K_M-GGUF --hf-file iera_codar-q4_k_m.gguf -c 2048
```