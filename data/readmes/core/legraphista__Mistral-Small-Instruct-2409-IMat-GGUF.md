---
base_model: mistralai/Mistral-Small-Instruct-2409
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

# Mistral-Small-Instruct-2409-IMat-GGUF
_Llama.cpp imatrix quantization of mistralai/Mistral-Small-Instruct-2409_

Original Model: [mistralai/Mistral-Small-Instruct-2409](https://huggingface.co/mistralai/Mistral-Small-Instruct-2409)    
Original dtype: `BF16` (`bfloat16`)  
Quantized by:  llama.cpp [b3785](https://github.com/ggerganov/llama.cpp/releases/tag/b3785)  
IMatrix dataset: [here](https://gist.githubusercontent.com/bartowski1182/eb213dccb3571f863da82e99418f81e8/raw/b2869d80f5c16fd7082594248e80144677736635/calibration_datav3.txt)  

- [Files](#files)
    - [IMatrix](#imatrix)
    - [Common Quants](#common-quants)
    - [All Quants](#all-quants)
- [Downloading using huggingface-cli](#downloading-using-huggingface-cli)
- [Inference](#inference)
    - [Simple chat template](#simple-chat-template)
    - [Chat template with system prompt](#chat-template-with-system-prompt)
    - [Llama.cpp](#llama-cpp)
- [FAQ](#faq)
    - [Why is the IMatrix not applied everywhere?](#why-is-the-imatrix-not-applied-everywhere)
    - [How do I merge a split GGUF?](#how-do-i-merge-a-split-gguf)

---

## Files

### IMatrix
Status: ✅ Available  
Link: [here](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/imatrix.dat)

### Common Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [Mistral-Small-Instruct-2409.Q8_0.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q8_0.gguf) | Q8_0 | 23.64GB | ✅ Available | ⚪ Static | 📦 No
| [Mistral-Small-Instruct-2409.Q6_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q6_K.gguf) | Q6_K | 18.25GB | ✅ Available | ⚪ Static | 📦 No
| [Mistral-Small-Instruct-2409.Q4_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q4_K.gguf) | Q4_K | 13.34GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.Q3_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q3_K.gguf) | Q3_K | 10.76GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.Q2_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q2_K.gguf) | Q2_K | 8.27GB | ✅ Available | 🟢 IMatrix | 📦 No


### All Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [Mistral-Small-Instruct-2409.BF16.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.BF16.gguf) | BF16 | 44.50GB | ✅ Available | ⚪ Static | 📦 No
| [Mistral-Small-Instruct-2409.FP16.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.FP16.gguf) | F16 | 44.50GB | ✅ Available | ⚪ Static | 📦 No
| [Mistral-Small-Instruct-2409.Q8_0.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q8_0.gguf) | Q8_0 | 23.64GB | ✅ Available | ⚪ Static | 📦 No
| [Mistral-Small-Instruct-2409.Q6_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q6_K.gguf) | Q6_K | 18.25GB | ✅ Available | ⚪ Static | 📦 No
| [Mistral-Small-Instruct-2409.Q5_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q5_K.gguf) | Q5_K | 15.72GB | ✅ Available | ⚪ Static | 📦 No
| [Mistral-Small-Instruct-2409.Q5_K_S.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q5_K_S.gguf) | Q5_K_S | 15.32GB | ✅ Available | ⚪ Static | 📦 No
| [Mistral-Small-Instruct-2409.Q4_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q4_K.gguf) | Q4_K | 13.34GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.Q4_K_S.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q4_K_S.gguf) | Q4_K_S | 12.66GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ4_NL.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ4_NL.gguf) | IQ4_NL | 12.61GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ4_XS.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ4_XS.gguf) | IQ4_XS | 11.94GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.Q3_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q3_K.gguf) | Q3_K | 10.76GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.Q3_K_L.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q3_K_L.gguf) | Q3_K_L | 11.73GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.Q3_K_S.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q3_K_S.gguf) | Q3_K_S | 9.64GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ3_M.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ3_M.gguf) | IQ3_M | 10.06GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ3_S.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ3_S.gguf) | IQ3_S | 9.69GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ3_XS.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ3_XS.gguf) | IQ3_XS | 9.18GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ3_XXS.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ3_XXS.gguf) | IQ3_XXS | 8.60GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.Q2_K.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q2_K.gguf) | Q2_K | 8.27GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.Q2_K_S.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.Q2_K_S.gguf) | Q2_K_S | 7.65GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ2_M.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ2_M.gguf) | IQ2_M | 7.62GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ2_S.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ2_S.gguf) | IQ2_S | 7.04GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ2_XS.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ2_XS.gguf) | IQ2_XS | 6.65GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ2_XXS.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ2_XXS.gguf) | IQ2_XXS | 6.00GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ1_M.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ1_M.gguf) | IQ1_M | 5.27GB | ✅ Available | 🟢 IMatrix | 📦 No
| [Mistral-Small-Instruct-2409.IQ1_S.gguf](https://huggingface.co/legraphista/Mistral-Small-Instruct-2409-IMat-GGUF/blob/main/Mistral-Small-Instruct-2409.IQ1_S.gguf) | IQ1_S | 4.83GB | ✅ Available | 🟢 IMatrix | 📦 No


## Downloading using huggingface-cli
If you do not have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"
```
Download the specific file you want:
```
huggingface-cli download legraphista/Mistral-Small-Instruct-2409-IMat-GGUF --include "Mistral-Small-Instruct-2409.Q8_0.gguf" --local-dir ./
```
If the model file is big, it has been split into multiple files. In order to download them all to a local folder, run:
```
huggingface-cli download legraphista/Mistral-Small-Instruct-2409-IMat-GGUF --include "Mistral-Small-Instruct-2409.Q8_0/*" --local-dir ./
# see FAQ for merging GGUF's
```

---

## Inference

### Simple chat template
```
<s>[INST] {user_prompt}[/INST] {assistant_response}</s>[INST] {next_user_prompt}[/INST]
```

### Chat template with system prompt
```
<s>[INST] {user_prompt}[/INST] {assistant_response}</s>[INST] {system_prompt}

{next_user_prompt}[/INST]
```

### Llama.cpp
```
llama.cpp/main -m Mistral-Small-Instruct-2409.Q8_0.gguf --color -i -p "prompt here (according to the chat template)"
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
2. Locate your GGUF chunks folder (ex: `Mistral-Small-Instruct-2409.Q8_0`)
3. Run `gguf-split --merge Mistral-Small-Instruct-2409.Q8_0/Mistral-Small-Instruct-2409.Q8_0-00001-of-XXXXX.gguf Mistral-Small-Instruct-2409.Q8_0.gguf`
    - Make sure to point `gguf-split` to the first chunk of the split.

---

Got a suggestion? Ping me [@legraphista](https://x.com/legraphista)!