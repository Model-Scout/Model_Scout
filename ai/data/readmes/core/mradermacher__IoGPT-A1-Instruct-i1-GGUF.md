---
base_model: galaxyMindAiLabs/IoGPT-A1-Instruct
language:
- en
- fr
- de
- es
- pt
- it
- ja
- ko
- ru
- zh
- ar
- fa
- id
- ms
- ne
- pl
- ro
- sr
- sv
- tr
- uk
- vi
- hi
- bn
library_name: transformers
license: apache-2.0
model_name: IoGPT-Instruct
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- sft
- trl
- agent
- text-generation
- question-answering
- mistral
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
weighted/imatrix quants of https://huggingface.co/galaxyMindAiLabs/IoGPT-A1-Instruct

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#IoGPT-A1-Instruct-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/IoGPT-A1-Instruct-GGUF

**This is a vision model - mmproj files (if any) will be in the [static repository](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-GGUF).**
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.imatrix.gguf) | imatrix | 0.1 | imatrix file (for creating your own quants) |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ1_S.gguf) | i1-IQ1_S | 5.4 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ1_M.gguf) | i1-IQ1_M | 5.9 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 6.6 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ2_XS.gguf) | i1-IQ2_XS | 7.3 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ2_S.gguf) | i1-IQ2_S | 7.6 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ2_M.gguf) | i1-IQ2_M | 8.2 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q2_K_S.gguf) | i1-Q2_K_S | 8.4 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q2_K.gguf) | i1-Q2_K | 9.0 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 9.4 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ3_XS.gguf) | i1-IQ3_XS | 10.0 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q3_K_S.gguf) | i1-Q3_K_S | 10.5 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ3_S.gguf) | i1-IQ3_S | 10.5 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ3_M.gguf) | i1-IQ3_M | 10.8 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q3_K_M.gguf) | i1-Q3_K_M | 11.6 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q3_K_L.gguf) | i1-Q3_K_L | 12.5 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-IQ4_XS.gguf) | i1-IQ4_XS | 12.9 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q4_0.gguf) | i1-Q4_0 | 13.6 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q4_K_S.gguf) | i1-Q4_K_S | 13.6 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q4_K_M.gguf) | i1-Q4_K_M | 14.4 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q4_1.gguf) | i1-Q4_1 | 15.0 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q5_K_S.gguf) | i1-Q5_K_S | 16.4 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q5_K_M.gguf) | i1-Q5_K_M | 16.9 |  |
| [GGUF](https://huggingface.co/mradermacher/IoGPT-A1-Instruct-i1-GGUF/resolve/main/IoGPT-A1-Instruct.i1-Q6_K.gguf) | i1-Q6_K | 19.4 | practically like static Q6_K |

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
