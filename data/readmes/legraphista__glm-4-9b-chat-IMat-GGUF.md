---
base_model: THUDM/glm-4-9b-chat
inference: false
language:
- zh
- en
library_name: gguf
license: other
license_link: https://huggingface.co/THUDM/glm-4-9b-chat/blob/main/LICENSE
license_name: glm-4
pipeline_tag: text-generation
quantized_by: legraphista
tags:
- glm
- chatglm
- thudm
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

# glm-4-9b-chat-IMat-GGUF
_Llama.cpp imatrix quantization of THUDM/glm-4-9b-chat_

Original Model: [THUDM/glm-4-9b-chat](https://huggingface.co/THUDM/glm-4-9b-chat)    
Original dtype: `BF16` (`bfloat16`)  
Quantized by: [https://github.com/ggerganov/llama.cpp/pull/6999](https://github.com/ggerganov/llama.cpp/pull/6999)  
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
Link: [here](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/imatrix.dat)

### Common Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [glm-4-9b-chat.Q8_0.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q8_0.gguf) | Q8_0 | 9.99GB | ✅ Available | ⚪ Static | 📦 No
| [glm-4-9b-chat.Q6_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q6_K.gguf) | Q6_K | 8.26GB | ✅ Available | ⚪ Static | 📦 No
| [glm-4-9b-chat.Q4_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q4_K.gguf) | Q4_K | 6.25GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.Q3_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q3_K.gguf) | Q3_K | 5.06GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.Q2_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q2_K.gguf) | Q2_K | 3.99GB | ✅ Available | 🟢 IMatrix | 📦 No


### All Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [glm-4-9b-chat.BF16.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.BF16.gguf) | BF16 | 18.81GB | ✅ Available | ⚪ Static | 📦 No
| [glm-4-9b-chat.FP16.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.FP16.gguf) | F16 | 18.81GB | ✅ Available | ⚪ Static | 📦 No
| [glm-4-9b-chat.Q8_0.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q8_0.gguf) | Q8_0 | 9.99GB | ✅ Available | ⚪ Static | 📦 No
| [glm-4-9b-chat.Q6_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q6_K.gguf) | Q6_K | 8.26GB | ✅ Available | ⚪ Static | 📦 No
| [glm-4-9b-chat.Q5_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q5_K.gguf) | Q5_K | 7.14GB | ✅ Available | ⚪ Static | 📦 No
| [glm-4-9b-chat.Q5_K_S.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q5_K_S.gguf) | Q5_K_S | 6.69GB | ✅ Available | ⚪ Static | 📦 No
| [glm-4-9b-chat.Q4_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q4_K.gguf) | Q4_K | 6.25GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.Q4_K_S.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q4_K_S.gguf) | Q4_K_S | 5.75GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ4_NL.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ4_NL.gguf) | IQ4_NL | 5.46GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ4_XS.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ4_XS.gguf) | IQ4_XS | 5.25GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.Q3_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q3_K.gguf) | Q3_K | 5.06GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.Q3_K_L.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q3_K_L.gguf) | Q3_K_L | 5.28GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.Q3_K_S.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q3_K_S.gguf) | Q3_K_S | 4.59GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ3_M.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ3_M.gguf) | IQ3_M | 4.81GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ3_S.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ3_S.gguf) | IQ3_S | 4.59GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ3_XS.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ3_XS.gguf) | IQ3_XS | 4.43GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ3_XXS.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ3_XXS.gguf) | IQ3_XXS | 4.26GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.Q2_K.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q2_K.gguf) | Q2_K | 3.99GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.Q2_K_S.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.Q2_K_S.gguf) | Q2_K_S | 3.96GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ2_M.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ2_M.gguf) | IQ2_M | 3.93GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ2_S.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ2_S.gguf) | IQ2_S | 3.77GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ2_XS.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ2_XS.gguf) | IQ2_XS | 3.61GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ2_XXS.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ2_XXS.gguf) | IQ2_XXS | 3.43GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ1_M.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ1_M.gguf) | IQ1_M | 3.22GB | ✅ Available | 🟢 IMatrix | 📦 No
| [glm-4-9b-chat.IQ1_S.gguf](https://huggingface.co/legraphista/glm-4-9b-chat-IMat-GGUF/blob/main/glm-4-9b-chat.IQ1_S.gguf) | IQ1_S | 3.10GB | ✅ Available | 🟢 IMatrix | 📦 No


## Downloading using huggingface-cli
If you do not have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"
```
Download the specific file you want:
```
huggingface-cli download legraphista/glm-4-9b-chat-IMat-GGUF --include "glm-4-9b-chat.Q8_0.gguf" --local-dir ./
```
If the model file is big, it has been split into multiple files. In order to download them all to a local folder, run:
```
huggingface-cli download legraphista/glm-4-9b-chat-IMat-GGUF --include "glm-4-9b-chat.Q8_0/*" --local-dir ./
# see FAQ for merging GGUF's
```

---

## Inference

### Simple chat template
```
[gMASK]<sop><|user|>
{user_prompt}<|assistant|>
{assistant_response}<|user|>
{next_user_prompt}
```

### Chat template with system prompt
```
[gMASK]<sop><|system|>
{system_prompt}<|user|>
{user_prompt}<|assistant|>
{assistant_response}<|user|>
{next_user_prompt}
```

### Llama.cpp
```
llama.cpp/main -m glm-4-9b-chat.Q8_0.gguf --color -i -p "prompt here (according to the chat template)"
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
2. Locate your GGUF chunks folder (ex: `glm-4-9b-chat.Q8_0`)
3. Run `gguf-split --merge glm-4-9b-chat.Q8_0/glm-4-9b-chat.Q8_0-00001-of-XXXXX.gguf glm-4-9b-chat.Q8_0.gguf`
    - Make sure to point `gguf-split` to the first chunk of the split.

---

Got a suggestion? Ping me [@legraphista](https://x.com/legraphista)!