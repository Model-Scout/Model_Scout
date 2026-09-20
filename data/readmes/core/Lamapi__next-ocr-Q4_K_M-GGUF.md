---
tags:
- text-generation-inference
- transformers
- unsloth
- qwen3_vl
- trl
- sft
- chemistry
- code
- climate
- art
- biology
- finance
- legal
- music
- medical
- agent
- llama-cpp
- gguf-my-repo
license: apache-2.0
language:
- en
- ab
- aa
- ae
- af
- ak
- am
- an
- ar
- as
- av
- ay
- az
- ba
- be
- bg
- bh
- bi
- bm
- bn
- bo
- br
- bs
- ca
- ce
- ch
- co
- cr
- cs
- cu
- cv
- cy
- da
- de
- dv
- dz
- ee
- el
- eo
- es
- et
- eu
- fa
- ff
- fi
- fj
- fo
- fr
- fy
- ga
- gd
- gl
- gn
- gv
- ha
- he
- hi
- ho
- gu
- hr
- ht
- hu
- hz
- hy
- id
- ia
- ig
- ie
- ik
- ii
- is
- io
- iu
- it
- jv
- ja
- kg
- ka
- kj
- ki
- kl
- kk
- kn
- km
- kr
- ko
- ku
- ks
- kw
- kv
- la
- ky
- lg
- lb
- ln
- li
- lt
- lo
- lv
- lu
- mg
- mi
- mh
- ml
- mk
- mr
- mn
- mt
- ms
- na
- my
- nd
- nb
- ng
- nl
- ne
- 'no'
- nn
- nv
- nr
- oc
- oj
- om
- ny
- os
- or
- pa
- pi
- pl
- ps
- pt
- rm
- rn
- qu
- ro
- ru
- sn
- rw
- so
- sa
- sc
- sd
pipeline_tag: image-text-to-text
library_name: transformers
base_model: Lamapi/next-ocr
---

# Lamapi/next-ocr-Q4_K_M-GGUF
This model was converted to GGUF format from [`Lamapi/next-ocr`](https://huggingface.co/Lamapi/next-ocr) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Lamapi/next-ocr) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Lamapi/next-ocr-Q4_K_M-GGUF --hf-file next-ocr-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Lamapi/next-ocr-Q4_K_M-GGUF --hf-file next-ocr-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo Lamapi/next-ocr-Q4_K_M-GGUF --hf-file next-ocr-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Lamapi/next-ocr-Q4_K_M-GGUF --hf-file next-ocr-q4_k_m.gguf -c 2048
```
