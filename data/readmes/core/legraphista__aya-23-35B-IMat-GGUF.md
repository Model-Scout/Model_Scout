---
base_model: CohereForAI/aya-23-35B
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
- imatrix
- static
---

# aya-23-35B-IMat-GGUF
_Llama.cpp imatrix quantization of CohereForAI/aya-23-35B_

Original Model: [CohereForAI/aya-23-35B](https://huggingface.co/CohereForAI/aya-23-35B)  
Original dtype: `FP16` (`float16`)  
Quantized by: llama.cpp [b2998](https://github.com/ggerganov/llama.cpp/releases/tag/b2998)  
IMatrix dataset: [here](https://gist.githubusercontent.com/legraphista/d6d93f1a254bcfc58e0af3777eaec41e/raw/d380e7002cea4a51c33fffd47db851942754e7cc/imatrix.calibration.medium.raw)  

## Files

### IMatrix
Status: ✅ Available  
Link: [here](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/imatrix.dat) 

### Common Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [aya-23-35B.Q8_0/*](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/tree/main/aya-23-35B.Q8_0) | Q8_0 | 37.18GB | ✅ Available | ⚪ No | ✂ Yes
| [aya-23-35B.Q6_K.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q6_K.gguf) | Q6_K | 28.71GB | ✅ Available | ⚪ No | 📦 No
| [aya-23-35B.Q4_K.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q4_K.gguf) | Q4_K | 21.53GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.Q3_K.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q3_K.gguf) | Q3_K | 17.62GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.Q2_K.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q2_K.gguf) | Q2_K | 13.82GB | ✅ Available | 🟢 Yes | 📦 No


### All Quants
| Filename | Quant type | File Size | Status | Uses IMatrix | Is Split |
| -------- | ---------- | --------- | ------ | ------------ | -------- |
| [aya-23-35B.FP16/*](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/tree/main/aya-23-35B.FP16) | F16 | 69.97GB | ✅ Available | ⚪ No | ✂ Yes
| [aya-23-35B.Q5_K.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q5_K.gguf) | Q5_K | 25.01GB | ✅ Available | ⚪ No | 📦 No
| [aya-23-35B.Q5_K_S.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q5_K_S.gguf) | Q5_K_S | 24.34GB | ✅ Available | ⚪ No | 📦 No
| [aya-23-35B.Q4_K_S.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q4_K_S.gguf) | Q4_K_S | 20.38GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.Q3_K_L.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q3_K_L.gguf) | Q3_K_L | 19.15GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.Q3_K_S.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q3_K_S.gguf) | Q3_K_S | 15.86GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.Q2_K_S.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.Q2_K_S.gguf) | Q2_K_S | 12.74GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ4_NL.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ4_NL.gguf) | IQ4_NL | 20.23GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ4_XS.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ4_XS.gguf) | IQ4_XS | 19.20GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ3_M.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ3_M.gguf) | IQ3_M | 16.70GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ3_S.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ3_S.gguf) | IQ3_S | 15.86GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ3_XS.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ3_XS.gguf) | IQ3_XS | 15.09GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ3_XXS.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ3_XXS.gguf) | IQ3_XXS | 13.83GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ2_M.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ2_M.gguf) | IQ2_M | 12.68GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ2_S.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ2_S.gguf) | IQ2_S | 11.84GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ2_XS.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ2_XS.gguf) | IQ2_XS | 11.10GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ2_XXS.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ2_XXS.gguf) | IQ2_XXS | 10.19GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ1_M.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ1_M.gguf) | IQ1_M | 9.15GB | ✅ Available | 🟢 Yes | 📦 No
| [aya-23-35B.IQ1_S.gguf](https://huggingface.co/legraphista/aya-23-35B-IMat-GGUF/blob/main/aya-23-35B.IQ1_S.gguf) | IQ1_S | 8.52GB | ✅ Available | 🟢 Yes | 📦 No


## Downloading using huggingface-cli
First, make sure you have hugginface-cli installed:
```
pip install -U "huggingface_hub[cli]"
```
Then, you can target the specific file you want:
```
huggingface-cli download legraphista/aya-23-35B-IMat-GGUF --include "aya-23-35B.Q8_0.gguf" --local-dir ./
```
If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:
```
huggingface-cli download legraphista/aya-23-35B-IMat-GGUF --include "aya-23-35B.Q8_0/*" --local-dir aya-23-35B.Q8_0
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
2. Locate your GGUF chunks folder (ex: `aya-23-35B.Q8_0`)
3. Run `gguf-split --merge aya-23-35B.Q8_0/aya-23-35B.Q8_0-00001-of-XXXXX.gguf aya-23-35B.Q8_0.gguf`
    - Make sure to point `gguf-split` to the first chunk of the split.

---

Got a suggestion? Ping me [@legraphista](https://x.com/legraphista)!