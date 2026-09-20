---
base_model: yanolja/YanoljaNEXT-Rosetta-4B-2511
language:
- ar
- bg
- zh
- cs
- da
- nl
- en
- fi
- fr
- de
- el
- gu
- he
- hi
- hu
- id
- it
- ja
- ko
- fa
- pl
- pt
- ro
- ru
- sk
- es
- sv
- tl
- th
- tr
- uk
- vi
library_name: transformers
license: gemma
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- translation
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
static quants of https://huggingface.co/yanolja/YanoljaNEXT-Rosetta-4B-2511

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#YanoljaNEXT-Rosetta-4B-2511-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q2_K.gguf) | Q2_K | 1.8 |  |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q3_K_S.gguf) | Q3_K_S | 2.0 |  |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q3_K_M.gguf) | Q3_K_M | 2.2 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q3_K_L.gguf) | Q3_K_L | 2.3 |  |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.IQ4_XS.gguf) | IQ4_XS | 2.4 |  |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q4_K_S.gguf) | Q4_K_S | 2.5 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q4_K_M.gguf) | Q4_K_M | 2.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q5_K_S.gguf) | Q5_K_S | 2.9 |  |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q5_K_M.gguf) | Q5_K_M | 2.9 |  |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q6_K.gguf) | Q6_K | 3.3 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.Q8_0.gguf) | Q8_0 | 4.2 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/YanoljaNEXT-Rosetta-4B-2511-GGUF/resolve/main/YanoljaNEXT-Rosetta-4B-2511.f16.gguf) | f16 | 7.9 | 16 bpw, overkill |

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
