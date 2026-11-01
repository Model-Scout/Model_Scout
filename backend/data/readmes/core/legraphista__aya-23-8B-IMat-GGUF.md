---
base_model: CohereForAI/aya-23-8B
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
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
library_name: gguf
license: cc-by-nc-4.0
pipeline_tag: text-generation
quantized_by: legraphista
tags:
- quantized
- GGUF
- imatrix
- quantization
- imat
- static
---

# aya-23-8B-IMat-GGUF
_Llama.cpp imatrix quantization of CohereForAI/aya-23-8B_

Original Model: [CohereForAI/aya-23-8B](https://huggingface.co/CohereForAI/aya-23-8B)  
Original dtype: `FP16` (`float16`)  
Quantized by: llama.cpp [b2998](https://github.com/ggerganov/llama.cpp/releases/tag/b2998)  
IMatrix dataset: [here](https://gist.githubusercontent.com/legraphista/d6d93f1a254bcfc58e0af3777eaec41e/raw/d380e7002cea4a51c33fffd47db851942754e7cc/imatrix.calibration.medium.raw)  

## Files

### IMatrix
Status: ✅ Available  
Link: [here](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/imatrix.dat) 

### Common Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [aya-23-8B.Q8_0.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q8_0.gguf) | Q8_0 | 8.54GB | ✅ Available | ⚪ No | 📦 No
| [aya-23-8B.Q6_K.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q6_K.gguf) | Q6_K | 6.60GB | ✅ Available | ⚪ No | 📦 No
| [aya-23-8B.Q4_K.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q4_K.gguf) | Q4_K | 5.06GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.Q3_K.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q3_K.gguf) | Q3_K | 4.22GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.Q2_K.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q2_K.gguf) | Q2_K | 3.44GB | ✅ Available | 🟢 Yes | 📦 No


### All Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [aya-23-8B.FP16.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.FP16.gguf) | F16 | 16.07GB | ✅ Available | ⚪ No | 📦 No
| [aya-23-8B.Q5_K.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q5_K.gguf) | Q5_K | 5.80GB | ✅ Available | ⚪ No | 📦 No
| [aya-23-8B.Q5_K_S.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q5_K_S.gguf) | Q5_K_S | 5.67GB | ✅ Available | ⚪ No | 📦 No
| [aya-23-8B.Q4_K_S.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q4_K_S.gguf) | Q4_K_S | 4.83GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.Q3_K_L.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q3_K_L.gguf) | Q3_K_L | 4.53GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.Q3_K_S.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q3_K_S.gguf) | Q3_K_S | 3.87GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.Q2_K_S.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.Q2_K_S.gguf) | Q2_K_S | 3.25GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ4_NL.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ4_NL.gguf) | IQ4_NL | 4.81GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ4_XS.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ4_XS.gguf) | IQ4_XS | 4.60GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ3_M.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ3_M.gguf) | IQ3_M | 3.99GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ3_S.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ3_S.gguf) | IQ3_S | 3.89GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ3_XS.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ3_XS.gguf) | IQ3_XS | 3.72GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ3_XXS.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ3_XXS.gguf) | IQ3_XXS | 3.41GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ2_M.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ2_M.gguf) | IQ2_M | 3.08GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ2_S.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ2_S.gguf) | IQ2_S | 2.90GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ2_XS.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ2_XS.gguf) | IQ2_XS | 2.80GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ2_XXS.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ2_XXS.gguf) | IQ2_XXS | 2.59GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ1_M.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ1_M.gguf) | IQ1_M | 2.35GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-8B.IQ1_S.gguf](https://huggingface.co/legraphista/aya-23-8B-IMat-GGUF/blob/main/aya-23-8B.IQ1_S.gguf) | IQ1_S | 2.21GB | ✅ Available | 🟢 Yes | 📦 No


## Downloading using huggingface-cli
First, make sure you have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"
```
Then, you can target the specific file you want:
```
huggingface-cli download legraphista/aya-23-8B-IMat-GGUF --include "aya-23-8B.Q8_0.gguf" --local-dir ./
```
If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:
```
huggingface-cli download legraphista/aya-23-8B-IMat-GGUF --include "aya-23-8B.Q8_0/*" --local-dir aya-23-8B.Q8_0
# see FAQ for merging GGUF's
```

## FAQ

### Why is the IMatrix not applied everywhere?
According to [this investigation](https://www.reddit.com/r/LocalLLaMA/comments/1993iro/ggufs_quants_can_punch_above_their_weights_now/), it appears that lower quantizations are the only ones that benefit from the imatrix input (as per hellaswag results). 

### How do I merge a split GGUF?
1. Make sure you have `gguf-split` available
    - To get hold of `gguf-split`, navigate to https://github.com/ggerganov/llama.cpp/releases
    - Download the appropriate zip for your system from the latest release
    - Unzip the archive and you should be able to find `gguf-split`
2. Locate your GGUF chunks folder (ex: `aya-23-8B.Q8_0`)
3. Run `gguf-split --merge aya-23-8B.Q8_0/aya-23-8B.Q8_0-00001-of-XXXXX.gguf aya-23-8B.Q8_0.gguf`
    - Make sure to point `gguf-split` to the first chunk of the split.

---

Got a suggestion? Ping me [@legraphista](https://x.com/legraphista)!