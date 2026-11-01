---
base_model: onelevelstudio/ML-E5-0.3B
language:
- multilingual
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- no
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
library_name: transformers
license: mit
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- mteb
- Sentence Transformers
- sentence-similarity
- sentence-transformers
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
static quants of https://huggingface.co/onelevelstudio/ML-E5-0.3B

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#ML-E5-0.3B-GGUF).***

weighted/imatrix quants seem not to be available (by me) at this time. If they do not show up a week or so after the static ones, I have probably not planned for them. Feel free to request them by opening a Community Discussion.
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q2_K.gguf) | Q2_K | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q3_K_S.gguf) | Q3_K_S | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q3_K_M.gguf) | Q3_K_M | 0.3 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.IQ4_XS.gguf) | IQ4_XS | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q3_K_L.gguf) | Q3_K_L | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q4_K_S.gguf) | Q4_K_S | 0.3 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q4_K_M.gguf) | Q4_K_M | 0.3 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q5_K_S.gguf) | Q5_K_S | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q5_K_M.gguf) | Q5_K_M | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q6_K.gguf) | Q6_K | 0.3 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.Q8_0.gguf) | Q8_0 | 0.4 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/ML-E5-0.3B-GGUF/resolve/main/ML-E5-0.3B.f16.gguf) | f16 | 0.7 | 16 bpw, overkill |

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
