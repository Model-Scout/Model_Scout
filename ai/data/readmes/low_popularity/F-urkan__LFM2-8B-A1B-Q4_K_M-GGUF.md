---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
- moe
- llama.cpp
- gguf
base_model: LiquidAI/LFM2-8B-A1B
---

# LFM2-8B-A1B-Q4_K_M-GGUF
Just a copy of Q4_K_M version "LiquidAI/LFM2-8B-A1B-GGUF".

With User-Friendly simple commands.

Requirements: 
  * linux or stable llama.cpp install with a version newer than 6709.
  * 5 gb vram or ram (cpu is enough)
  * 5 gb disk space

# Step-by-step usage

## Download Model

Option 1 (fast download speed): 120 mb/s

```bash
sudo apt install aria2 -y
aria2c -x 16 -s 16 -k 1M \
  "https://huggingface.co/F-urkan/LFM2-8B-A1B-Q4_K_M-GGUF/resolve/main/LFM2-8B-A1B-Q4_K_M.gguf" \
  -o LFM2-8B-A1B-Q4_K_M.gguf
```

Option 2 (slow but easy): 10 mb/s

```bash
wget https://huggingface.co/F-urkan/LFM2-8B-A1B-Q4_K_M-GGUF/resolve/main/LFM2-8B-A1B-Q4_K_M.gguf
```

Option 3 (Depend on your browser):

Just click auto download link:
[link](https://huggingface.co/F-urkan/LFM2-8B-A1B-Q4_K_M-GGUF/resolve/main/LFM2-8B-A1B-Q4_K_M.gguf?download=true)


## Get llama.cpp

If your llama.cpp version is newer than b6709 you can skip.

### With brew

Install brew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" # if brew is installed you can skip.
export PATH="/home/linuxbrew/.linuxbrew/bin:$PATH"
```

Install llama.cpp:

```
brew install llama.cpp
```

### Manual

Prefer that:
[https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)

Short version:
```bash
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release -j
cd build && sudo make install
```

## Run

### Server

```bash
llama-server -m LFM2-8B-A1B-Q4_K_M.gguf --port 10000 --no-mmap --jinja --temp 0 -c 4096 -ngl 0
```

### Cli

```bash
llama-cli -m LFM2-8B-A1B-Q4_K_M.gguf --no-mmap --jinja --temp 0 -c 4096 -ngl 0
```