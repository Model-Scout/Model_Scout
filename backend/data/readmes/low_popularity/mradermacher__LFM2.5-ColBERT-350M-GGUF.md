---
base_model: LiquidAI/LFM2.5-ColBERT-350M
language:
- en
- es
- de
- fr
- it
- pt
- ar
- sv
- no
- ja
- ko
library_name: transformers
license: other
license_link: LICENSE
license_name: lfm1.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- liquid
- lfm2
- lfm2.5
- edge
- ColBERT
- PyLate
- sentence-transformers
- multi-vector
- sentence-similarity
- feature-extraction
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
static quants of https://huggingface.co/LiquidAI/LFM2.5-ColBERT-350M

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#LFM2.5-ColBERT-350M-GGUF).***

weighted/imatrix quants seem not to be available (by me) at this time. If they do not show up a week or so after the static ones, I have probably not planned for them. Feel free to request them by opening a Community Discussion.
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q2_K.gguf) | Q2_K | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q3_K_S.gguf) | Q3_K_S | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q3_K_M.gguf) | Q3_K_M | 0.3 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q3_K_L.gguf) | Q3_K_L | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.IQ4_XS.gguf) | IQ4_XS | 0.3 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q4_K_S.gguf) | Q4_K_S | 0.3 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q4_K_M.gguf) | Q4_K_M | 0.3 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q5_K_S.gguf) | Q5_K_S | 0.4 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q5_K_M.gguf) | Q5_K_M | 0.4 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q6_K.gguf) | Q6_K | 0.4 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.Q8_0.gguf) | Q8_0 | 0.5 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/LFM2.5-ColBERT-350M-GGUF/resolve/main/LFM2.5-ColBERT-350M.f16.gguf) | f16 | 0.8 | 16 bpw, overkill |

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
