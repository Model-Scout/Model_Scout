---
base_model: GuminiResearch/Gumini-1B-Base
datasets:
- HuggingFaceFW/fineweb-edu
- uonlp/CulturaX
- wikimedia/wikipedia
language:
- ko
- en
library_name: transformers
license: other
license_link: https://huggingface.co/Qwen/Qwen2.5-3B/blob/main/LICENSE
license_name: qwen-research
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- text-generation
- korean
- bilingual
- qwen2
- built-with-qwen
- continued-pretraining
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
static quants of https://huggingface.co/GuminiResearch/Gumini-1B-Base

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Gumini-1B-Base-inherit-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q2_K.gguf) | Q2_K | 0.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q3_K_S.gguf) | Q3_K_S | 0.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q3_K_M.gguf) | Q3_K_M | 0.7 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q3_K_L.gguf) | Q3_K_L | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.IQ4_XS.gguf) | IQ4_XS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q4_K_S.gguf) | Q4_K_S | 0.8 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q4_K_M.gguf) | Q4_K_M | 0.8 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q5_K_S.gguf) | Q5_K_S | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q5_K_M.gguf) | Q5_K_M | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q6_K.gguf) | Q6_K | 1.0 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.Q8_0.gguf) | Q8_0 | 1.3 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/Gumini-1B-Base-inherit-GGUF/resolve/main/Gumini-1B-Base-inherit.f16.gguf) | f16 | 2.3 | 16 bpw, overkill |

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
