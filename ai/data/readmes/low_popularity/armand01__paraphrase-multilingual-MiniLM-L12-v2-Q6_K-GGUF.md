---
language:
- multilingual
- ar
- bg
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
- gl
- gu
- he
- hi
- hr
- hu
- hy
- id
- it
- ja
- ka
- ko
- ku
- lt
- lv
- mk
- mn
- mr
- ms
- my
- nb
- nl
- pl
- pt
- ro
- ru
- sk
- sl
- sq
- sr
- sv
- th
- tr
- uk
- ur
- vi
license: apache-2.0
library_name: sentence-transformers
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
- llama-cpp
- gguf-my-repo
language_bcp47:
- fr-ca
- pt-br
- zh-cn
- zh-tw
pipeline_tag: sentence-similarity
---

NOTE: Don't download, it doesn't work.

# armand01/paraphrase-multilingual-MiniLM-L12-v2-Q6_K-GGUF
This model was converted to GGUF format from [`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2) for more details on the model.
## Use with llama.cpp

Install llama.cpp through brew.

```bash
brew install ggerganov/ggerganov/llama.cpp
```
Invoke the llama.cpp server or the CLI.

CLI:

```bash
llama-cli --hf-repo armand01/paraphrase-multilingual-MiniLM-L12-v2-Q6_K-GGUF --model paraphrase-multilingual-minilm-l12-v2.Q6_K.gguf -p "The meaning to life and the universe is"
```

Server:

```bash
llama-server --hf-repo armand01/paraphrase-multilingual-MiniLM-L12-v2-Q6_K-GGUF --model paraphrase-multilingual-minilm-l12-v2.Q6_K.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

```
git clone https://github.com/ggerganov/llama.cpp &&             cd llama.cpp &&             make &&             ./main -m paraphrase-multilingual-minilm-l12-v2.Q6_K.gguf -n 128
```
