---
base_model: CohereForAI/c4ai-command-r-plus-08-2024
extra_gated_prompt: "By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)\
  \  and acknowledge that the information you provide will be collected, used, and\
  \ shared in accordance with Cohere\u2019s [Privacy Policy]( https://cohere.com/privacy)."
inference: false
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
library_name: gguf
license: cc-by-nc-4.0
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

# c4ai-command-r-plus-08-2024-IMat-GGUF
_Llama.cpp imatrix quantization of CohereForAI/c4ai-command-r-plus-08-2024_

Original Model: [CohereForAI/c4ai-command-r-plus-08-2024](https://huggingface.co/CohereForAI/c4ai-command-r-plus-08-2024)    
Original dtype: `FP16` (`float16`)  
Quantized by:  llama.cpp [b3645](https://github.com/ggerganov/llama.cpp/releases/tag/b3645)  
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
Link: [here](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/imatrix.dat)

### Common Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| c4ai-command-r-plus-08-2024.Q8_0 | Q8_0 | - | ⏳ Processing | ⚪ Static | -
| [c4ai-command-r-plus-08-2024.Q6_K/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q6_K) | Q6_K | 85.17GB | ✅ Available | ⚪ Static | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q4_K/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q4_K) | Q4_K | 62.75GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q3_K/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q3_K) | Q3_K | 50.98GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q2_K.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.Q2_K.gguf) | Q2_K | 39.50GB | ✅ Available | 🟢 IMatrix | 📦 No


### All Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [c4ai-command-r-plus-08-2024.FP16/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.FP16) | F16 | 207.64GB | ✅ Available | ⚪ Static | ✂ Yes
| c4ai-command-r-plus-08-2024.Q8_0 | Q8_0 | - | ⏳ Processing | ⚪ Static | -
| [c4ai-command-r-plus-08-2024.Q6_K/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q6_K) | Q6_K | 85.17GB | ✅ Available | ⚪ Static | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q5_K/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q5_K) | Q5_K | 73.62GB | ✅ Available | ⚪ Static | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q5_K_S/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q5_K_S) | Q5_K_S | 71.80GB | ✅ Available | ⚪ Static | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q4_K/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q4_K) | Q4_K | 62.75GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q4_K_S/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q4_K_S) | Q4_K_S | 59.64GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.IQ4_NL/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.IQ4_NL) | IQ4_NL | 59.32GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.IQ4_XS/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.IQ4_XS) | IQ4_XS | 56.20GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q3_K/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q3_K) | Q3_K | 50.98GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q3_K_L/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q3_K_L) | Q3_K_L | 55.40GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.Q3_K_S/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.Q3_K_S) | Q3_K_S | 45.85GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.IQ3_M/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.IQ3_M) | IQ3_M | 47.68GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.IQ3_S/*](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/tree/main/c4ai-command-r-plus-08-2024.IQ3_S) | IQ3_S | 45.96GB | ✅ Available | 🟢 IMatrix | ✂ Yes
| [c4ai-command-r-plus-08-2024.IQ3_XS.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.IQ3_XS.gguf) | IQ3_XS | 43.60GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.IQ3_XXS.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.IQ3_XXS.gguf) | IQ3_XXS | 40.66GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.Q2_K.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.Q2_K.gguf) | Q2_K | 39.50GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.Q2_K_S.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.Q2_K_S.gguf) | Q2_K_S | 36.60GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.IQ2_M.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.IQ2_M.gguf) | IQ2_M | 36.04GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.IQ2_S.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.IQ2_S.gguf) | IQ2_S | 33.32GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.IQ2_XS.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.IQ2_XS.gguf) | IQ2_XS | 31.63GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.IQ2_XXS.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.IQ2_XXS.gguf) | IQ2_XXS | 28.61GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.IQ1_M.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.IQ1_M.gguf) | IQ1_M | 25.22GB | ✅ Available | 🟢 IMatrix | 📦 No
| [c4ai-command-r-plus-08-2024.IQ1_S.gguf](https://huggingface.co/legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF/blob/main/c4ai-command-r-plus-08-2024.IQ1_S.gguf) | IQ1_S | 23.18GB | ✅ Available | 🟢 IMatrix | 📦 No


## Downloading using huggingface-cli
If you do not have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"
```
Download the specific file you want:
```
huggingface-cli download legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF --include "c4ai-command-r-plus-08-2024.Q8_0.gguf" --local-dir ./
```
If the model file is big, it has been split into multiple files. In order to download them all to a local folder, run:
```
huggingface-cli download legraphista/c4ai-command-r-plus-08-2024-IMat-GGUF --include "c4ai-command-r-plus-08-2024.Q8_0/*" --local-dir ./
# see FAQ for merging GGUF's
```

---

## Inference

### Simple chat template
```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{user_prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>{assistant_response}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{next_user_prompt}<|END_OF_TURN_TOKEN|>
```

### Chat template with system prompt
```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|>{system_prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{user_prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|>{assistant_response}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{next_user_prompt}<|END_OF_TURN_TOKEN|>
```

### Llama.cpp
```
llama.cpp/main -m c4ai-command-r-plus-08-2024.Q8_0.gguf --color -i -p "prompt here (according to the chat template)"
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
2. Locate your GGUF chunks folder (ex: `c4ai-command-r-plus-08-2024.Q8_0`)
3. Run `gguf-split --merge c4ai-command-r-plus-08-2024.Q8_0/c4ai-command-r-plus-08-2024.Q8_0-00001-of-XXXXX.gguf c4ai-command-r-plus-08-2024.Q8_0.gguf`
    - Make sure to point `gguf-split` to the first chunk of the split.

---

Got a suggestion? Ping me [@legraphista](https://x.com/legraphista)!