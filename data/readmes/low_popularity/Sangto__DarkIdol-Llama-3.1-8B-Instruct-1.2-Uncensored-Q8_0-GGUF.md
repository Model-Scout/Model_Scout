---
base_model: aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
- zh
- ko
- ja
license: llama3.1
pipeline_tag: text-generation
tags:
- roleplay
- llama3
- sillytavern
- idol
- facebook
- meta
- pytorch
- llama
- llama-3
- llama-cpp
- gguf-my-repo
extra_gated_fields:
  First Name: text
  Last Name: text
  Date of birth: date_picker
  Country: country
  Affiliation: text
  Job title:
    type: select
    options:
    - Student
    - Research Graduate
    - AI researcher
    - AI developer/engineer
    - Reporter
    - Other
---

# Sangto/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-GGUF
This model was converted to GGUF format from [`aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored`](https://huggingface.co/aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/aifeifei798/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Sangto/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-GGUF --hf-file darkidol-llama-3.1-8b-instruct-1.2-uncensored-q8_0.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Sangto/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-GGUF --hf-file darkidol-llama-3.1-8b-instruct-1.2-uncensored-q8_0.gguf -c 2048
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
./llama-cli --hf-repo Sangto/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-GGUF --hf-file darkidol-llama-3.1-8b-instruct-1.2-uncensored-q8_0.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Sangto/DarkIdol-Llama-3.1-8B-Instruct-1.2-Uncensored-Q8_0-GGUF --hf-file darkidol-llama-3.1-8b-instruct-1.2-uncensored-q8_0.gguf -c 2048
```
