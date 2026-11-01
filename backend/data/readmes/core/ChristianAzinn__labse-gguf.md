---
base_model: sentence-transformers/labse
inference: false
language:
- multilingual
- af
- sq
- am
- ar
- hy
- as
- az
- eu
- be
- bn
- bs
- bg
- my
- ca
- ceb
- zh
- co
- hr
- cs
- da
- nl
- en
- eo
- et
- fi
- fr
- fy
- gl
- ka
- de
- el
- gu
- ht
- ha
- haw
- he
- hi
- hmn
- hu
- is
- ig
- id
- ga
- it
- ja
- jv
- kn
- kk
- km
- rw
- ko
- ku
- ky
- lo
- la
- lv
- lt
- lb
- mk
- mg
- ms
- ml
- mt
- mi
- mr
- mn
- ne
- no
- ny
- or
- fa
- pl
- pt
- pa
- ro
- ru
- sm
- gd
- sr
- st
- sn
- si
- sk
- sl
- so
- es
- su
- sw
- sv
- tl
- tg
- ta
- tt
- te
- th
- bo
- tr
- tk
- ug
- uk
- ur
- uz
- vi
- cy
- wo
- xh
- yi
- yo
- zu
license: apache-2.0
model_creator: sentence-transformers
model_name: labse
model_type: bert
quantized_by: ChristianAzinn
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- gguf
- mteb
- Sentence Transformers
- sentence-similarity
- sentence-transformers
- feature-extraction
---

# labse-gguf

Model creator: [sentence-transformers](https://huggingface.co/sentence-transformers)

Original model: [labse](https://huggingface.co/sentence-transformers/labse)

## Original Description

The language-agnostic BERT sentence embedding encodes text into high dimensional vectors. The model is trained and optimized to produce similar representations exclusively for bilingual sentence pairs that are translations of each other. So it can be used for mining for translations of a sentence in a larger corpus.

## Description

This repo contains GGUF format files for the labse embedding model.

These files were converted and quantized with llama.cpp [PR 5500](https://github.com/ggerganov/llama.cpp/pull/5500), commit [34aa045de](https://github.com/ggerganov/llama.cpp/pull/5500/commits/34aa045de44271ff7ad42858c75739303b8dc6eb), on a consumer RTX 4090.

This model supports up to 512 tokens of context.

## Compatibility

These files are compatible with [llama.cpp](https://github.com/ggerganov/llama.cpp) as of commit [4524290e8](https://github.com/ggerganov/llama.cpp/commit/4524290e87b8e107cc2b56e1251751546f4b9051), as well as [LM Studio](https://lmstudio.ai/) as of version 0.2.19.

# Meta-information
## Explanation of quantisation methods
<details>
  <summary>Click to see details</summary>
The methods available are:
* GGML_TYPE_Q2_K - "type-1" 2-bit quantization in super-blocks containing 16 blocks, each block having 16 weight. Block scales and mins are quantized with 4 bits. This ends up effectively using 2.5625 bits per weight (bpw)
* GGML_TYPE_Q3_K - "type-0" 3-bit quantization in super-blocks containing 16 blocks, each block having 16 weights. Scales are quantized with 6 bits. This end up using 3.4375 bpw.
* GGML_TYPE_Q4_K - "type-1" 4-bit quantization in super-blocks containing 8 blocks, each block having 32 weights. Scales and mins are quantized with 6 bits. This ends up using 4.5 bpw.
* GGML_TYPE_Q5_K - "type-1" 5-bit quantization. Same super-block structure as GGML_TYPE_Q4_K resulting in 5.5 bpw
* GGML_TYPE_Q6_K - "type-0" 6-bit quantization. Super-blocks with 16 blocks, each block having 16 weights. Scales are quantized with 8 bits. This ends up using 6.5625 bpw
Refer to the Provided Files table below to see what files use which methods, and how.
</details>

## Provided Files
| Name | Quant method | Bits | Size | Max RAM required | Use case |
| ---- | ---- | ---- | ---- | ---- | ----- |
| Name | Quant method | Bits | Size | Use case |
| [labse.Q2_K.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q2_K.gguf) | Q2_K | 2 | 364 MB | smallest, significant quality loss - not recommended for most purposes |
| [labse.Q3_K_S.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q3_K_S.gguf) | Q3_K_S | 3 | 368 MB | very small, high quality loss |
| [labse.Q3_K_M.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q3_K_M.gguf) | Q3_K_M | 3 | 374 MB | very small, high quality loss |
| [labse.Q3_K_L.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q3_K_L.gguf) | Q3_K_L | 3 | 379 MB | small, substantial quality loss |
| [labse.Q4_0.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q4_0.gguf) | Q4_0 | 4 | 379 MB | legacy; small, very high quality loss - prefer using Q3_K_M |
| [labse.Q4_K_S.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q4_K_S.gguf) | Q4_K_S | 4 | 380 MB | small, greater quality loss |
| [labse.Q4_K_M.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q4_K_M.gguf) | Q4_K_M | 4 | 384 MB | medium, balanced quality - recommended |
| [labse.Q5_0.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q5_0.gguf) | Q5_0 | 5 | 390 MB | legacy; medium, balanced quality - prefer using Q4_K_M |
| [labse.Q5_K_S.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q5_K_S.gguf) | Q5_K_S | 5 | 390 MB | large, low quality loss - recommended |
| [labse.Q5_K_M.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q5_K_M.gguf) | Q5_K_M | 5 | 392 MB | large, very low quality loss - recommended |
| [labse.Q6_K.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q6_K.gguf) | Q6_K | 6 | 401 MB | very large, extremely low quality loss |
| [labse.Q8_0.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse.Q8_0.gguf) | Q8_0 | 8 | 515 MB | very large, extremely low quality loss - recommended |
| [labse.Q8_0.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse_fp16.gguf) | fp16 | 16 | 955 MB | enormous, pretty much the original model - not recommended |
| [labse.Q8_0.gguf](https://huggingface.co/ChristianAzinn/labse-gguf/blob/main/labse_fp32.gguf) | fp32 | 32 | 1.89 GB | enormous, pretty much the original model - not recommended |

# Examples
## Example Usage with  `llama.cpp`

To compute a single embedding, build llama.cpp and run:
```shell
./embedding -ngl 99 -m [filepath-to-gguf].gguf -p 'search_query: What is TSNE?'
```

You can also submit a batch of texts to embed, as long as the total number of tokens does not exceed the context length. Only the first three embeddings are shown by the `embedding` example.

`texts.txt`:
```
search_query: What is TSNE?
search_query: Who is Laurens Van der Maaten?
```

Compute multiple embeddings:
```shell
./embedding -ngl 99 -m [filepath-to-gguf].gguf -f texts.txt
```

## Example Usage with LM Studio

Download the 0.2.19 beta build from here: [Windows](https://releases.lmstudio.ai/windows/0.2.19/beta/LM-Studio-0.2.19-Setup-Preview-1.exe) [MacOS](https://releases.lmstudio.ai/mac/arm64/0.2.19/beta/LM-Studio-darwin-arm64-0.2.19-Preview-1.zip) [Linux](https://releases.lmstudio.ai/linux/0.2.19/beta/LM_Studio-0.2.19-Preview-1.AppImage)

Once installed, open the app. The home should look like this:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6584f042b378d311dccea501/QGkYvH242S0c_clPqX9Ip.png)

Search for either "ChristianAzinn" in the main search bar or go to the "Search" tab on the left menu and search the name there.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6584f042b378d311dccea501/11hLos1JNMyZ1q2K9ICss.png)

Select your model from those that appear (this example uses `bge-small-en-v1.5-gguf`) and select which quantization you want to download. Since this model is pretty small, I recommend Q8_0, if not f16/32. Generally, the lower you go in the list (or the bigger the number gets), the larger the file and the better the performance.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6584f042b378d311dccea501/hu9DuVYahQ-QpII5P8mVD.png)

You will see a green checkmark and the word "Downloaded" once the model has successfully downloaded, which can take some time depending on your network speeds.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6584f042b378d311dccea501/7fmXkLDmGTNVyG3oqB4--.png)

Once this model is finished downloading, navigate to the "Local Server" tab on the left menu and open the loader for text embedding models. This loader does not appear before version 0.2.19, so ensure you downloaded the correct version.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6584f042b378d311dccea501/OrzvqQIhB9p-aMq2G6Lxd.png)

Select the model you just downloaded from the dropdown that appears to load it. You may need to play with configuratios in the right-side menu, such as GPU offload if it doesn't fit entirely into VRAM.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6584f042b378d311dccea501/TM4dO4DFP1xqZD1GWBqeI.png)

All that's left to do is to hit the "Start Server" button:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6584f042b378d311dccea501/6TZvnX84rZKZ0TwVVLFnw.png)

And if you see text like that shown below in the console, you're good to go! You can use this as a drop-in replacement for the OpenAI embeddings API in any application that requires it, or you can query the endpoint directly to test it out.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6584f042b378d311dccea501/kD47WaH-tzpr4qaAm-pMn.png)

Example curl request to the API endpoint:
```shell
curl http://localhost:1234/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "input": "Your text string goes here",
    "model": "model-identifier-here"
  }'
```

For more information, see the LM Studio [text embedding documentation](https://lmstudio.ai/docs/text-embeddings).


## Acknowledgements

Thanks to the LM Studio team and everyone else working on open-source AI.

This README is inspired by that of [nomic-ai-embed-text-v1.5-gguf](https://huggingface.co/nomic-ai/nomic-embed-text-v1.5-gguf), another excellent embedding model, and those of the legendary [TheBloke](https://huggingface.co/TheBloke).