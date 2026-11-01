---
base_model: k08200/gaon-1.7b-v2-translate-big
language:
- ko
- en
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- korean
- translation
- from-scratch
- qwen3-architecture
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
static quants of https://huggingface.co/k08200/gaon-1.7b-v2-translate-big

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#gaon-1.7b-v2-translate-big-GGUF).***

weighted/imatrix quants seem not to be available (by me) at this time. If they do not show up a week or so after the static ones, I have probably not planned for them. Feel free to request them by opening a Community Discussion.
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q2_K.gguf) | Q2_K | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q3_K_S.gguf) | Q3_K_S | 1.0 |  |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q3_K_M.gguf) | Q3_K_M | 1.0 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q3_K_L.gguf) | Q3_K_L | 1.1 |  |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.IQ4_XS.gguf) | IQ4_XS | 1.1 |  |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q4_K_S.gguf) | Q4_K_S | 1.2 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q4_K_M.gguf) | Q4_K_M | 1.2 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q5_K_S.gguf) | Q5_K_S | 1.3 |  |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q5_K_M.gguf) | Q5_K_M | 1.4 |  |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q6_K.gguf) | Q6_K | 1.5 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.Q8_0.gguf) | Q8_0 | 1.9 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/gaon-1.7b-v2-translate-big-GGUF/resolve/main/gaon-1.7b-v2-translate-big.f16.gguf) | f16 | 3.5 | 16 bpw, overkill |

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
