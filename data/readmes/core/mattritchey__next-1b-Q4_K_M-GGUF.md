---
language:
- tr
- ar
- af
- az
- es
- en
- el
- ro
- ru
- rm
- th
- uk
- uz
- pl
- pt
- fa
- sk
- sl
- da
- de
- nl
- fr
- fi
- ka
- hi
- hu
- hy
- ja
- kk
- kn
- ko
- ku
- ky
- la
- lb
- id
- is
- it
- zh
- cs
- vi
- be
- bg
- bs
- ne
- mn
license: mit
tags:
- turkish
- türkiye
- english
- ai
- lamapi
- gemma3
- next
- next-x1
- efficient
- text-generation
- open-source
- 1b
- huggingface
- large-language-model
- llm
- causal
- transformer
- artificial-intelligence
- machine-learning
- ai-research
- natural-language-processing
- nlp
- finetuned
- lightweight
- creative
- summarization
- question-answering
- chat-model
- generative-ai
- optimized-model
- unsloth
- trl
- sft
- chemistry
- biology
- finance
- legal
- music
- art
- code
- climate
- medical
- agent
- text-generation-inference
- llama-cpp
- gguf-my-repo
pipeline_tag: text-generation
base_model: Lamapi/next-1b
---

# mattritchey/next-1b-Q4_K_M-GGUF
This model was converted to GGUF format from [`Lamapi/next-1b`](https://huggingface.co/Lamapi/next-1b) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Lamapi/next-1b) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo mattritchey/next-1b-Q4_K_M-GGUF --hf-file next-1b-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo mattritchey/next-1b-Q4_K_M-GGUF --hf-file next-1b-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo mattritchey/next-1b-Q4_K_M-GGUF --hf-file next-1b-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo mattritchey/next-1b-Q4_K_M-GGUF --hf-file next-1b-q4_k_m.gguf -c 2048
```
