---
base_model: CMSManhattan/JiRackUltra_14b
language:
- en
- zh
- ja
- ko
- fr
- es
- pt
- de
- it
- ru
- ar
- vi
- th
library_name: transformers
license: mit
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- text-generation
- ternary
- bitnet
- 1.58bit
- cpu
- gguf
- qwen2.5
- deepseek
- efficient
- low-memory
- jirack
- web-ui
- routing
- tool-call
- robotics
- NVIDIA Inception Program Member
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
<!-- ### quants:  x-f16 Q4_K_S Q2_K Q8_0 Q6_K Q3_K_M Q3_K_S Q3_K_L Q4_K_M Q5_K_S Q5_K_M IQ4_XS -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
static quants of https://huggingface.co/CMSManhattan/JiRackUltra_14b

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#JiRackUltra_14b-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/JiRackUltra_14b-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q2_K.gguf) | Q2_K | 5.9 |  |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q3_K_S.gguf) | Q3_K_S | 6.8 |  |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q3_K_M.gguf) | Q3_K_M | 7.4 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q3_K_L.gguf) | Q3_K_L | 8.0 |  |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.IQ4_XS.gguf) | IQ4_XS | 8.3 |  |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q4_K_S.gguf) | Q4_K_S | 8.7 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q4_K_M.gguf) | Q4_K_M | 9.1 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q5_K_S.gguf) | Q5_K_S | 10.4 |  |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q5_K_M.gguf) | Q5_K_M | 10.6 |  |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q6_K.gguf) | Q6_K | 12.2 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/JiRackUltra_14b-GGUF/resolve/main/JiRackUltra_14b.Q8_0.gguf) | Q8_0 | 15.8 | fast, best quality |

Here is a handy graph by ikawrakow comparing some lower-quality quant
types (lower is better):

![image.png](https://www.nethype.de/huggingface_embed/quantpplgraph.png)

And here are Artefact2's thoughts on the matter:
https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9

## FAQ / Model Request

See https://huggingface.co/mradermacher/model_requests for some answers to
questions you might have and/or if you want some other model quantized.

## Thanks

I thank my company, [nethype GmbH](https://www.nethype.de/), for letting
me use its servers and providing upgrades to my workstation to enable
this work in my free time.

<!-- end -->
