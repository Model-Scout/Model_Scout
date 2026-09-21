---
base_model: DJLougen/LFM2-24B-A2B-REAP
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- pt
library_name: transformers
license: other
license_link: https://www.liquid.ai/lfm1.0
license_name: lfm1.0
model_type: lfm2_moe
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- lfm2
- liquid
- moe
- reap
- pruned
- gguf
- mlx
- edge
- text-generation
- transformers
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
static quants of https://huggingface.co/DJLougen/LFM2-24B-A2B-REAP

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#LFM2-24B-A2B-REAP-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q2_K.gguf) | Q2_K | 4.6 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q3_K_S.gguf) | Q3_K_S | 5.5 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q3_K_M.gguf) | Q3_K_M | 6.0 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q3_K_L.gguf) | Q3_K_L | 6.5 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.IQ4_XS.gguf) | IQ4_XS | 6.8 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q4_K_S.gguf) | Q4_K_S | 7.1 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q4_K_M.gguf) | Q4_K_M | 7.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q5_K_S.gguf) | Q5_K_S | 8.6 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q5_K_M.gguf) | Q5_K_M | 8.9 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q6_K.gguf) | Q6_K | 10.3 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/LFM2-24B-A2B-REAP-GGUF/resolve/main/LFM2-24B-A2B-REAP.Q8_0.gguf) | Q8_0 | 13.2 | fast, best quality |

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
