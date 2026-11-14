---
base_model: saidutta69/LFM3-VL-2B-heretic
language:
- en
- ar
- zh
- fr
- de
- it
- ja
- ko
- pt
- es
- vi
- th
- id
- hi
- ru
- pl
library_name: transformers
license: other
license_link: https://huggingface.co/LiquidAI/LFM3-VL-2B/blob/main/LICENSE
license_name: lfm1.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- liquid
- lfm3
- lfm3-vl
- vision-language
- vlm
- multimodal
- image-text-to-text
- edge
- on-device
- ocr
- document
- video
- heretic
- uncensored
- decensored
- abliterated
- reproducible
- gguf
- local-llm
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags: nicoboss -->
<!-- ### quants:  Q2_K IQ3_M Q4_K_S IQ3_XXS Q3_K_M small-IQ4_NL Q4_K_M IQ2_M Q6_K IQ4_XS Q2_K_S IQ1_M Q3_K_S IQ2_XXS Q3_K_L IQ2_XS Q5_K_S IQ2_S IQ1_S Q5_K_M Q4_0 IQ3_XS Q4_1 IQ3_S -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
weighted/imatrix quants of https://huggingface.co/saidutta69/LFM3-VL-2B-heretic

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#LFM3-VL-2B-heretic-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-GGUF

**This is a vision model - mmproj files (if any) will be in the [static repository](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-GGUF).**
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.imatrix.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.imatrix.gguf) | imatrix | 0.1 | imatrix file (for creating your own quants) |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ1_S.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ1_S.gguf) | i1-IQ1_S | 1.1 | for the desperate |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ1_M.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ1_M.gguf) | i1-IQ1_M | 1.1 | mostly desperate |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ2_XXS.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 1.2 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ2_XS.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ2_XS.gguf) | i1-IQ2_XS | 1.3 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ2_S.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ2_S.gguf) | i1-IQ2_S | 1.4 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ2_M.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ2_M.gguf) | i1-IQ2_M | 1.4 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q2_K_S.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q2_K_S.gguf) | i1-Q2_K_S | 1.5 | very low quality |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ3_XXS.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 1.6 | lower quality |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q2_K.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q2_K.gguf) | i1-Q2_K | 1.6 | IQ3_XXS probably better |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ3_XS.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ3_XS.gguf) | i1-IQ3_XS | 1.8 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ3_S.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ3_S.gguf) | i1-IQ3_S | 1.8 | beats Q3_K* |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q3_K_S.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q3_K_S.gguf) | i1-Q3_K_S | 1.8 | IQ3_XS probably better |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ3_M.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ3_M.gguf) | i1-IQ3_M | 1.8 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q3_K_M.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q3_K_M.gguf) | i1-Q3_K_M | 1.9 | IQ3_S probably better |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q3_K_L.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q3_K_L.gguf) | i1-Q3_K_L | 2.0 | IQ3_M probably better |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ4_XS.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ4_XS.gguf) | i1-IQ4_XS | 2.1 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-IQ4_NL.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-IQ4_NL.gguf) | i1-IQ4_NL | 2.2 | prefer IQ4_XS |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q4_0.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q4_0.gguf) | i1-Q4_0 | 2.2 | fast, low quality |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q4_K_S.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q4_K_S.gguf) | i1-Q4_K_S | 2.2 | optimal size/speed/quality |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q4_K_M.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q4_K_M.gguf) | i1-Q4_K_M | 2.3 | fast, recommended |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q4_1.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q4_1.gguf) | i1-Q4_1 | 2.4 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q5_K_S.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q5_K_S.gguf) | i1-Q5_K_S | 2.6 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q5_K_M.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q5_K_M.gguf) | i1-Q5_K_M | 2.6 |  |
| [PART 1](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/LFM3-VL-2B-heretic.i1-Q6_K.gguf) [PART 2](https://huggingface.co/mradermacher/LFM3-VL-2B-heretic-i1-GGUF/resolve/main/lfm3-vl-2b-heretic.i1-Q6_K.gguf) | i1-Q6_K | 3.0 | practically like static Q6_K |

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
this work in my free time. Additional thanks to [@nicoboss](https://huggingface.co/nicoboss) for giving me access to his private supercomputer, enabling me to provide many more imatrix quants, at much higher quality, than I would otherwise be able to.

<!-- end -->
