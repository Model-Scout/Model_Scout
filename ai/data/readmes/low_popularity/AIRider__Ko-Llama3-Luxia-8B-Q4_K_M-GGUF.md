---
language:
- en
- ko
license: llama3
tags:
- saltlux
- luxia
- meta
- llama-3
- pytorch
- llama-cpp
- gguf-my-repo
pipeline_tag: text-generation
---

# AIRider/Ko-Llama3-Luxia-8B-Q4_K_M-GGUF
This model was converted to GGUF format from [`saltlux/Ko-Llama3-Luxia-8B`](https://huggingface.co/saltlux/Ko-Llama3-Luxia-8B) using llama.cpp

## Use with llama.cpp
Install llama.cpp through brew.
```bash
brew install ggerganov/ggerganov/llama.cpp
```
Invoke the llama.cpp server or the CLI.
CLI:
```bash
llama-cli --hf-repo AIRider/Ko-Llama3-Luxia-8B-Q4_K_M-GGUF --model ko-llama3-luxia-8b-q4_k_m.gguf -p "The meaning to life and the universe is"
```
Server:
```bash
llama-server --hf-repo AIRider/Ko-Llama3-Luxia-8B-Q4_K_M-GGUF --model ko-llama3-luxia-8b-q4_k_m.gguf -c 2048
```
Note: You can also use this checkpoint directly through the [usage steps](https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#usage) listed in the Llama.cpp repo as well.
```
git clone https://github.com/ggerganov/llama.cpp && \
cd llama.cpp && \
make && \
./main -m ko-llama3-luxia-8b-q4_k_m.gguf -n 128
```
