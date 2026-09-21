---
license: apache-2.0
tags:
- merge
- evolutionary-merge
- darwin
- darwin-v5
- model-mri
- reasoning
- advanced-reasoning
- chain-of-thought
- thinking
- qwen3.5
- qwen
- claude-opus
- distillation
- multilingual
- benchmark
- open-source
- apache-2.0
- layer-wise-merge
- coding-agent
- tool-calling
- long-context
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
base_model: FINAL-Bench/Darwin-9B-Opus
model-index:
- name: Darwin-9B-Opus
  results:
  - task:
      type: question-answering
      name: Question Answering
    dataset:
      name: GPQA Diamond
      type: Idavidrein/gpqa
      config: gpqa_diamond
    metrics:
    - type: accuracy
      value: 82.5
      name: Accuracy
---

# aclava/Darwin-9B-Opus-Q8_0-GGUF
This model was converted to GGUF format from [`FINAL-Bench/Darwin-9B-Opus`](https://huggingface.co/FINAL-Bench/Darwin-9B-Opus) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/FINAL-Bench/Darwin-9B-Opus) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo aclava/Darwin-9B-Opus-Q8_0-GGUF --hf-file darwin-9b-opus-q8_0.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo aclava/Darwin-9B-Opus-Q8_0-GGUF --hf-file darwin-9b-opus-q8_0.gguf -c 2048
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
./llama-cli --hf-repo aclava/Darwin-9B-Opus-Q8_0-GGUF --hf-file darwin-9b-opus-q8_0.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo aclava/Darwin-9B-Opus-Q8_0-GGUF --hf-file darwin-9b-opus-q8_0.gguf -c 2048
```
