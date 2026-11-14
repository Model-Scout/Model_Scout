---
language:
- ko
license: gemma
library_name: transformers
tags:
- gemma
- pytorch
- instruct
- finetune
- translation
- llama-cpp
- gguf-my-repo
base_model: lemon-mint/gemma-ko-1.1-2b-it
widget:
- messages:
  - role: user
    content: Translate into Korean:Hamsters don't eat cats.
pipeline_tag: text-generation
---

# andreass123/gemma-2b-translation-v0.150-Q4_K_M-GGUF
This model was converted to GGUF format from [`lemon-mint/gemma-2b-translation-v0.150`](https://huggingface.co/lemon-mint/gemma-2b-translation-v0.150) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/lemon-mint/gemma-2b-translation-v0.150) for more details on the model.
## Use with llama.cpp

Install llama.cpp through brew.

```bash
brew install ggerganov/ggerganov/llama.cpp
```
Invoke the llama.cpp server or the CLI.

CLI:

```bash
llama-cli --hf-repo andreass123/gemma-2b-translation-v0.150-Q4_K_M-GGUF --model gemma-2b-translation-v0.150.Q4_K_M.gguf -p "The meaning to life and the universe is"
```

Server:

```bash
llama-server --hf-repo andreass123/gemma-2b-translation-v0.150-Q4_K_M-GGUF --model gemma-2b-translation-v0.150.Q4_K_M.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

```
git clone https://github.com/ggerganov/llama.cpp &&             cd llama.cpp &&             make &&             ./main -m gemma-2b-translation-v0.150.Q4_K_M.gguf -n 128
```
