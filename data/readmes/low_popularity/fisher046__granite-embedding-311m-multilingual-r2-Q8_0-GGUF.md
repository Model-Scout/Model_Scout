---
language:
- ar
- az
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fr
- he
- hi
- hr
- hu
- id
- is
- it
- ja
- ka
- kk
- km
- ko
- lt
- lv
- mr
- ms
- nl
- 'no'
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- sw
- te
- th
- tl
- tr
- uk
- ur
- uz
- vi
- zh
library_name: sentence-transformers
license: apache-2.0
pipeline_tag: feature-extraction
tags:
- granite
- embeddings
- transformers
- multilingual
- mteb
- feature-extraction
- sentence-similarity
- matryoshka
- onnx
- openvino
- llama-cpp
- gguf-my-repo
base_model: ibm-granite/granite-embedding-311m-multilingual-r2
---

# fisher046/granite-embedding-311m-multilingual-r2-Q8_0-GGUF
This model was converted to GGUF format from [`ibm-granite/granite-embedding-311m-multilingual-r2`](https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo fisher046/granite-embedding-311m-multilingual-r2-Q8_0-GGUF --hf-file granite-embedding-311m-multilingual-r2-q8_0.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo fisher046/granite-embedding-311m-multilingual-r2-Q8_0-GGUF --hf-file granite-embedding-311m-multilingual-r2-q8_0.gguf -c 2048
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
./llama-cli --hf-repo fisher046/granite-embedding-311m-multilingual-r2-Q8_0-GGUF --hf-file granite-embedding-311m-multilingual-r2-q8_0.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo fisher046/granite-embedding-311m-multilingual-r2-Q8_0-GGUF --hf-file granite-embedding-311m-multilingual-r2-q8_0.gguf -c 2048
```
