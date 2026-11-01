---
base_model: mistralai/Mistral-Large-Instruct-2407
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
inference: false
language:
- en
- fr
- de
- es
- it
- pt
- zh
- ja
- ru
- ko
library_name: gguf
license: other
license_link: https://mistral.ai/licenses/MRL-0.1.md
license_name: mrl
pipeline_tag: text-generation
quantized_by: legraphista
tags:
- quantized
- GGUF
- quantization
- imat
- imatrix
- static
- 16bit
- 8bit
- 6bit
- 5bit
- 4bit
- 3bit
- 2bit
- 1bit
---

# Mistral-Large-Instruct-2407-IMat-GGUF
_Llama.cpp imatrix quantization of mistralai/Mistral-Large-Instruct-2407_

Original Model: [mistralai/Mistral-Large-Instruct-2407](https://huggingface.co/mistralai/Mistral-Large-Instruct-2407)    
Original dtype: `BF16` (`bfloat16`)  
Quantized by:  llama.cpp [b3452](https://github.com/ggerganov/llama.cpp/releases/tag/b3452)  
IMatrix dataset: [here](https://gist.githubusercontent.com/bartowski1182/eb213dccb3571f863da82e99418f81e8/raw/b2869d80f5c16fd7082594248e80144677736635/calibration_datav3.txt)  

- [Files](#files)
    - [IMatrix](#imatrix)
    - [Common Quants](#common-quants)
    - [All Quants](#all-quants)
- [Downloading using huggingface-cli](#downloading-using-huggingface-cli)
- [Inference](#inference)
    - [Llama.cpp](#llama-cpp)
- [FAQ](#faq)
    - [Why is the IMatrix not applied everywhere?](#why-is-the-imatrix-not-applied-everywhere)
    - [How do I merge a split GGUF?](#how-do-i-merge-a-split-gguf)

---

## Files

### IMatrix
Status: ✅ Available  
Link: [here](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/blob/main/imatrix.dat)

### Common Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [Mistral-Large-Instruct-2407.Q8_0/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q8_0) | Q8_0 | 130.28GB | ✅ Available | ⚪ Static | ✂ Yes
| [Mistral-Large-Instruct-2407.Q6_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q6_K) | Q6_K | 100.59GB | ✅ Available | ⚪ Static | ✂ Yes
| [Mistral-Large-Instruct-2407.Q4_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q4_K) | Q4_K | 73.22GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.Q3_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q3_K) | Q3_K | 59.10GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.Q2_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q2_K) | Q2_K | 45.20GB | ✅ Available | 🟢 IMatrix | ✂ Yes


### All Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [Mistral-Large-Instruct-2407.BF16/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.BF16) | BF16 | 245.23GB | ✅ Available | ⚪ Static | ✂ Yes
| [Mistral-Large-Instruct-2407.FP16/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.FP16) | F16 | 245.23GB | ✅ Available | ⚪ Static | ✂ Yes
| [Mistral-Large-Instruct-2407.Q8_0/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q8_0) | Q8_0 | 130.28GB | ✅ Available | ⚪ Static | ✂ Yes
| [Mistral-Large-Instruct-2407.Q6_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q6_K) | Q6_K | 100.59GB | ✅ Available | ⚪ Static | ✂ Yes
| [Mistral-Large-Instruct-2407.Q5_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q5_K) | Q5_K | 86.49GB | ✅ Available | ⚪ Static | ✂ Yes
| [Mistral-Large-Instruct-2407.Q5_K_S/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q5_K_S) | Q5_K_S | 84.36GB | ✅ Available | ⚪ Static | ✂ Yes
| [Mistral-Large-Instruct-2407.Q4_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q4_K) | Q4_K | 73.22GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.Q4_K_S/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q4_K_S) | Q4_K_S | 69.57GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.IQ4_NL/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.IQ4_NL) | IQ4_NL | 69.22GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.IQ4_XS/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.IQ4_XS) | IQ4_XS | 65.43GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.Q3_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q3_K) | Q3_K | 59.10GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.Q3_K_L/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q3_K_L) | Q3_K_L | 64.55GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.Q3_K_S/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q3_K_S) | Q3_K_S | 52.85GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.IQ3_M/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.IQ3_M) | IQ3_M | 55.28GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.IQ3_S/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.IQ3_S) | IQ3_S | 53.00GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.IQ3_XS/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.IQ3_XS) | IQ3_XS | 50.14GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.IQ3_XXS/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.IQ3_XXS) | IQ3_XXS | 47.01GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.Q2_K/*](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/tree/main/Mistral-Large-Instruct-2407.Q2_K) | Q2_K | 45.20GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [Mistral-Large-Instruct-2407.Q2_K_S.gguf](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/blob/main/Mistral-Large-Instruct-2407.Q2_K_S.gguf) | Q2_K_S | 41.61GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Large-Instruct-2407.IQ2_M.gguf](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/blob/main/Mistral-Large-Instruct-2407.IQ2_M.gguf) | IQ2_M | 41.62GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Large-Instruct-2407.IQ2_S.gguf](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/blob/main/Mistral-Large-Instruct-2407.IQ2_S.gguf) | IQ2_S | 38.38GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Large-Instruct-2407.IQ2_XS.gguf](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/blob/main/Mistral-Large-Instruct-2407.IQ2_XS.gguf) | IQ2_XS | 36.08GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Large-Instruct-2407.IQ2_XXS.gguf](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/blob/main/Mistral-Large-Instruct-2407.IQ2_XXS.gguf) | IQ2_XXS | 32.43GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Large-Instruct-2407.IQ1_M.gguf](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/blob/main/Mistral-Large-Instruct-2407.IQ1_M.gguf) | IQ1_M | 28.39GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Large-Instruct-2407.IQ1_S.gguf](https://huggingface.co/legraphista/Mistral-Large-Instruct-2407-IMat-GGUF/blob/main/Mistral-Large-Instruct-2407.IQ1_S.gguf) | IQ1_S | 25.96GB | ✅ Available | 🟢 IMatrix | 📦 No


## Downloading using huggingface-cli
If you do not have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"
```
Download the specific file you want:
```
huggingface-cli download legraphista/Mistral-Large-Instruct-2407-IMat-GGUF --include "Mistral-Large-Instruct-2407.Q8_0.gguf" --local-dir ./
```
If the model file is big, it has been split into multiple files. In order to download them all to a local folder, run:
```
huggingface-cli download legraphista/Mistral-Large-Instruct-2407-IMat-GGUF --include "Mistral-Large-Instruct-2407.Q8_0/*" --local-dir ./
# see FAQ for merging GGUF's
```

---

## Inference

### Llama.cpp
```
llama.cpp/main -m Mistral-Large-Instruct-2407.Q8_0.gguf --color -i -p "prompt here"
```

---

## FAQ

### Why is the IMatrix not applied everywhere?
According to [this investigation](https://www.reddit.com/r/LocalLLaMA/comments/1993iro/ggufs_quants_can_punch_above_their_weights_now/), it appears that lower quantizations are the only ones that benefit from the imatrix input (as per hellaswag results). 

### How do I merge a split GGUF?
1. Make sure you have `gguf-split` available
    - To get hold of `gguf-split`, navigate to https://github.com/ggerganov/llama.cpp/releases
    - Download the appropriate zip for your system from the latest release
    - Unzip the archive and you should be able to find `gguf-split`
2. Locate your GGUF chunks folder (ex: `Mistral-Large-Instruct-2407.Q8_0`)
3. Run `gguf-split --merge Mistral-Large-Instruct-2407.Q8_0/Mistral-Large-Instruct-2407.Q8_0-00001-of-XXXXX.gguf Mistral-Large-Instruct-2407.Q8_0.gguf`
    - Make sure to point `gguf-split` to the first chunk of the split.

---

Got a suggestion? Ping me [@legraphista](https://x.com/legraphista)!