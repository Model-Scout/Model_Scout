---
base_model: afkfatih/LFM2-8B-A1B-TR
datasets:
- afkfatih/turkish-gemma-51k
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
- tr
library_name: transformers
license: other
license_link: LICENSE
license_name: lfm1.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- text-generation
- turkish
- lora
- sft
- mixture-of-experts
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
static quants of https://huggingface.co/afkfatih/LFM2-8B-A1B-TR

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#LFM2-8B-A1B-TR-GGUF).***

weighted/imatrix quants seem not to be available (by me) at this time. If they do not show up a week or so after the static ones, I have probably not planned for them. Feel free to request them by opening a Community Discussion.
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q2_K.gguf) | Q2_K | 3.2 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q3_K_S.gguf) | Q3_K_S | 3.7 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q3_K_M.gguf) | Q3_K_M | 4.1 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q3_K_L.gguf) | Q3_K_L | 4.4 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.IQ4_XS.gguf) | IQ4_XS | 4.6 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q4_K_S.gguf) | Q4_K_S | 4.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q4_K_M.gguf) | Q4_K_M | 5.1 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q5_K_S.gguf) | Q5_K_S | 5.9 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q5_K_M.gguf) | Q5_K_M | 6.0 |  |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q6_K.gguf) | Q6_K | 6.9 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.Q8_0.gguf) | Q8_0 | 9.0 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/LFM2-8B-A1B-TR-GGUF/resolve/main/LFM2-8B-A1B-TR.f16.gguf) | f16 | 16.8 | 16 bpw, overkill |

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
