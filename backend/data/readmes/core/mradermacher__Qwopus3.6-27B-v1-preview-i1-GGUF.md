---
base_model: Jackrong/Qwopus3.6-27B-v1-preview
datasets:
- Kassadin88/Claude-Distillation-Dataset
- Jackrong/GLM-5.1-Reasoning-1M-Cleaned
- Jackrong/Kimi-K2.5-Reasoning-1M-Cleaned
- Jackrong/Qwen3.5-reasoning-700x
language:
- en
- zh
- ja
- ko
- es
- ru
library_name: transformers
license: apache-2.0
license_link: https://huggingface.co/Qwen/Qwen3.6-27B/blob/main/LICENSE
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- qwen
- qwen3.6
- qwopus
- reasoning
- instruct
- conversational
- vision-language-model
- multimodal
- image-text-to-text
- transformers
- safetensors
- unsloth
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
weighted/imatrix quants of https://huggingface.co/Jackrong/Qwopus3.6-27B-v1-preview

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Qwopus3.6-27B-v1-preview-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-GGUF

**This is a vision model - mmproj files (if any) will be in the [static repository](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-GGUF).**
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.imatrix.gguf) | imatrix | 0.1 | imatrix file (for creating your own quants) |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ1_S.gguf) | i1-IQ1_S | 7.2 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ1_M.gguf) | i1-IQ1_M | 7.7 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 8.5 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ2_XS.gguf) | i1-IQ2_XS | 9.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ2_S.gguf) | i1-IQ2_S | 9.5 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ2_M.gguf) | i1-IQ2_M | 10.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q2_K_S.gguf) | i1-Q2_K_S | 10.3 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q2_K.gguf) | i1-Q2_K | 10.8 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 11.3 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ3_XS.gguf) | i1-IQ3_XS | 12.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q3_K_S.gguf) | i1-Q3_K_S | 12.2 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ3_S.gguf) | i1-IQ3_S | 12.5 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ3_M.gguf) | i1-IQ3_M | 12.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q3_K_M.gguf) | i1-Q3_K_M | 13.4 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q3_K_L.gguf) | i1-Q3_K_L | 14.4 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-IQ4_XS.gguf) | i1-IQ4_XS | 15.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q4_0.gguf) | i1-Q4_0 | 15.6 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q4_K_S.gguf) | i1-Q4_K_S | 15.7 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q4_K_M.gguf) | i1-Q4_K_M | 16.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q4_1.gguf) | i1-Q4_1 | 17.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q5_K_S.gguf) | i1-Q5_K_S | 18.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q5_K_M.gguf) | i1-Q5_K_M | 19.3 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus3.6-27B-v1-preview-i1-GGUF/resolve/main/Qwopus3.6-27B-v1-preview.i1-Q6_K.gguf) | i1-Q6_K | 22.2 | practically like static Q6_K |

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
