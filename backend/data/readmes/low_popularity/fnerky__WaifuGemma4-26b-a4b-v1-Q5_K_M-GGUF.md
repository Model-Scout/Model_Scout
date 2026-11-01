---
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
language:
- en
- es
- ru
- pt
- id
- ar
- th
- fr
- de
- uk
- vi
- ja
- ko
- zh
- tr
- it
- pl
tags:
- gemma4
- moe
- conversational
- roleplay
- role-play
- character
- rlhf
- grpo
- reward-model
- human-preference
- arena
- multilingual
- llama-cpp
- gguf-my-repo
base_model: hiwaifu-research/WaifuGemma4-26b-a4b-v1
model-index:
- name: WaifuGemma4-26b-a4b-v1
  results:
  - task:
      type: text-generation
    dataset:
      name: IFEval
      type: ifeval
    metrics:
    - type: prompt_level_strict
      value: 89.09
      name: Prompt-level Strict
  - task:
      type: text-generation
    dataset:
      name: GSM8K
      type: gsm8k
    metrics:
    - type: accuracy
      value: 96.89
      name: Acc
  - task:
      type: text-generation
    dataset:
      name: MATH-500
      type: math_500
    metrics:
    - type: accuracy
      value: 92.8
      name: Acc
  - task:
      type: text-generation
    dataset:
      name: MMLU
      type: mmlu
    metrics:
    - type: accuracy
      value: 88.59
      name: Acc
  - task:
      type: text-generation
    dataset:
      name: C-Eval
      type: ceval
    metrics:
    - type: accuracy
      value: 78.97
      name: Acc
  - task:
      type: text-generation
    dataset:
      name: C-MMLU
      type: cmmlu
    metrics:
    - type: accuracy
      value: 79.56
      name: Acc
  - task:
      type: text-generation
    dataset:
      name: ARC
      type: arc
    metrics:
    - type: accuracy
      value: 98.39
      name: Acc
  - task:
      type: text-generation
    dataset:
      name: HellaSwag
      type: hellaswag
    metrics:
    - type: accuracy
      value: 79.78
      name: Acc
  - task:
      type: text-generation
    dataset:
      name: Winogrande
      type: winogrande
    metrics:
    - type: accuracy
      value: 85.4
      name: Acc
  - task:
      type: text-generation
    dataset:
      name: TruthfulQA
      type: truthful_qa
    metrics:
    - type: accuracy
      value: 75.4
      name: MC Acc
---

# fnerky/WaifuGemma4-26b-a4b-v1-Q5_K_M-GGUF
This model was converted to GGUF format from [`hiwaifu-research/WaifuGemma4-26b-a4b-v1`](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/hiwaifu-research/WaifuGemma4-26b-a4b-v1) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo fnerky/WaifuGemma4-26b-a4b-v1-Q5_K_M-GGUF --hf-file waifugemma4-26b-a4b-v1-q5_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo fnerky/WaifuGemma4-26b-a4b-v1-Q5_K_M-GGUF --hf-file waifugemma4-26b-a4b-v1-q5_k_m.gguf -c 2048
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
./llama-cli --hf-repo fnerky/WaifuGemma4-26b-a4b-v1-Q5_K_M-GGUF --hf-file waifugemma4-26b-a4b-v1-q5_k_m.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo fnerky/WaifuGemma4-26b-a4b-v1-Q5_K_M-GGUF --hf-file waifugemma4-26b-a4b-v1-q5_k_m.gguf -c 2048
```
