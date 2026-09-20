---
language:
- tr
- en
- de
- ka
- el
- ku
- es
- sl
- sk
- af
- da
- nl
- fa
- fi
- fr
- ga
- hi
- hu
- hy
- ja
- kg
- kk
- ko
- ky
- la
- lb
- id
- it
- is
- za
- zh
- zu
- cs
- vi
- be
- bg
- bs
- ne
- mn
- rm
- ro
- ru
- te
- th
- tk
- tt
- uk
- uz
- ug
- pl
- pt
- 'no'
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
- 4b
- huggingface
- large-language-model
- llm
- causal
- transformer
- artificial-intelligence
- machine-learning
- ai-research
- natural-language-processing
- language
- multilingual
- multimodal
- nlp
- finetuned
- lightweight
- creative
- summarization
- question-answering
- chat
- generative-ai
- optimized
- unsloth
- trl
- sft
- chemistry
- code
- biology
- finance
- legal
- music
- art
- state-of-the-art
- climate
- medical
- agent
- text-generation-inference
- merge
- dense
- llama-cpp
- gguf-my-repo
pipeline_tag: image-text-to-text
datasets:
- mlabonne/FineTome-100k
- ITCL/FineTomeOs
- Gryphe/ChatGPT-4o-Writing-Prompts
- dongguanting/ARPO-SFT-54K
- GreenerPastures/All-Your-Base-Full
- Gryphe/Opus-WritingPrompts
- HuggingFaceH4/MATH-500
- mlabonne/smoltalk-flat
- mlabonne/natural_reasoning-formatted
- OpenSPG/KAG-Thinker-training-dataset
- uclanlp/Brief-Pro
- CognitiveKernel/CognitiveKernel-Pro-SFT
- SuperbEmphasis/Claude-4.0-DeepSeek-R1-RP-SFWish
- QuixiAI/dolphin-r1
- mlabonne/lmsys-arena-human-sft-55k
library_name: transformers
base_model: Lamapi/next-4b
---

# Lamapi/next-4b-Q4_K_M-GGUF
This model was converted to GGUF format from [`Lamapi/next-4b`](https://huggingface.co/Lamapi/next-4b) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/Lamapi/next-4b) for more details on the model.

## Use with llama.cpp
Install llama.cpp through brew (works on Mac and Linux)

```bash
brew install llama.cpp

```
Invoke the llama.cpp server or the CLI.

### CLI:
```bash
llama-cli --hf-repo Lamapi/next-4b-Q4_K_M-GGUF --hf-file next-4b-q4_k_m.gguf -p "The meaning to life and the universe is"
```

### Server:
```bash
llama-server --hf-repo Lamapi/next-4b-Q4_K_M-GGUF --hf-file next-4b-q4_k_m.gguf -c 2048
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
./llama-cli --hf-repo Lamapi/next-4b-Q4_K_M-GGUF --hf-file next-4b-q4_k_m.gguf -p "The meaning to life and the universe is"
```
or 
```
./llama-server --hf-repo Lamapi/next-4b-Q4_K_M-GGUF --hf-file next-4b-q4_k_m.gguf -c 2048
```
