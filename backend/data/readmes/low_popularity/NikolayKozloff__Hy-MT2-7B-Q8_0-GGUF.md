---
library_name: transformers
tags:
- translation
- llama-cpp
- gguf-my-repo
language:
- zh
- en
- fr
- pt
- es
- ja
- tr
- ru
- ar
- ko
- th
- it
- de
- vi
- ms
- id
- tl
- hi
- pl
- cs
- nl
- km
- my
- fa
- gu
- ur
- te
- mr
- he
- bn
- ta
- uk
- bo
- kk
- mn
- ug
base_model: tencent/Hy-MT2-7B
---

# NikolayKozloff/Hy-MT2-7B-Q8_0-GGUF
This model was converted to GGUF format from [`tencent/Hy-MT2-7B`](https://huggingface.co/tencent/Hy-MT2-7B) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/tencent/Hy-MT2-7B) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo NikolayKozloff/Hy-MT2-7B-Q8_0-GGUF --hf-file hy-mt2-7b-q8_0.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo NikolayKozloff/Hy-MT2-7B-Q8_0-GGUF --hf-file hy-mt2-7b-q8_0.gguf -c 2048
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
./llama-cli --hf-repo NikolayKozloff/Hy-MT2-7B-Q8_0-GGUF --hf-file hy-mt2-7b-q8_0.gguf -p "The meaning to life and the universe is"
```
or
```
./llama-server --hf-repo NikolayKozloff/Hy-MT2-7B-Q8_0-GGUF --hf-file hy-mt2-7b-q8_0.gguf -c 2048
```
