---
license: gpl-3.0
library_name: transformers
pipeline_tag: translation
language:
- bg
- ca
- cs
- cy
- da
- de
- el
- en
- es
- et
- eu
- fi
- fr
- ga
- gl
- hr
- hu
- it
- lt
- lv
- mt
- nl
- nb
- 'no'
- oc
- pl
- pt
- ro
- ru
- sl
- sk
- sr
- sv
- uk
- ast
- an
- ar
- ja
- hi
- ko
- zh
- is
base_model: BSC-LT/salamandraTA-7b-instruct
tags:
- llama-cpp
- gguf-my-repo
---

# egekocabas/salamandraTA-7b-instruct-Q5_K_M-GGUF
This model was converted to GGUF format from [`BSC-LT/salamandraTA-7b-instruct`](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/BSC-LT/salamandraTA-7b-instruct) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo egekocabas/salamandraTA-7b-instruct-Q5_K_M-GGUF --hf-file salamandrata-7b-instruct-q5_k_m-imat.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo egekocabas/salamandraTA-7b-instruct-Q5_K_M-GGUF --hf-file salamandrata-7b-instruct-q5_k_m-imat.gguf -c 2048
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
./llama-cli --hf-repo egekocabas/salamandraTA-7b-instruct-Q5_K_M-GGUF --hf-file salamandrata-7b-instruct-q5_k_m-imat.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo egekocabas/salamandraTA-7b-instruct-Q5_K_M-GGUF --hf-file salamandrata-7b-instruct-q5_k_m-imat.gguf -c 2048
```
