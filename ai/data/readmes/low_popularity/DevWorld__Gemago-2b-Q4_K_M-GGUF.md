---
language:
- ko
- en
license:
- apache-2.0
- gemma
tags:
- gemma
- llama-cpp
- gguf-my-repo
datasets:
- traintogpb/aihub-koen-translation-integrated-base-10m
pipeline_tag: translation
widget:
- text: 'Korean:

    나라의 말이 중국과 달라 문자와 서로 통하지 아니하다.


    English:

    '
  example_title: K2E
- text: 'English:

    Mr. and Mrs. Dursley were proud to say that they were perfectly normal.


    Korean:

    '
  example_title: E2K
inference:
  parameters:
    max_length: 200
---

# DevWorld/Gemago-2b-Q4_K_M-GGUF
This model was converted to GGUF format from [`DevWorld/Gemago-2b`](https://huggingface.co/DevWorld/Gemago-2b) using llama.cpp via the ggml.ai's [GGUF-my-repo](https://huggingface.co/spaces/ggml-org/gguf-my-repo) space.
Refer to the [original model card](https://huggingface.co/DevWorld/Gemago-2b) for more details on the model.
## Use with llama.cpp

Install llama.cpp through brew.

```bash
brew install ggerganov/ggerganov/llama.cpp
```
Invoke the llama.cpp server or the CLI.

CLI:

```bash
llama-cli --hf-repo DevWorld/Gemago-2b-Q4_K_M-GGUF --model gemago-2b.Q4_K_M.gguf -p "The meaning to life and the universe is"
```

Server:

```bash
llama-server --hf-repo DevWorld/Gemago-2b-Q4_K_M-GGUF --model gemago-2b.Q4_K_M.gguf -c 2048
```

Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.

```
git clone https://github.com/ggerganov/llama.cpp &&             cd llama.cpp &&             make &&             ./main -m gemago-2b.Q4_K_M.gguf -n 128
```
