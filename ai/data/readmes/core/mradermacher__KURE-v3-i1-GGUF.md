---
base_model: nlpai-lab/KURE-v3
language:
- ko
- en
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- matryoshka
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
weighted/imatrix quants of https://huggingface.co/nlpai-lab/KURE-v3

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#KURE-v3-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/KURE-v3-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.imatrix.gguf) | imatrix | 0.1 | imatrix file (for creating your own quants) |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ1_S.gguf) | i1-IQ1_S | 0.5 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ1_M.gguf) | i1-IQ1_M | 0.5 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 0.5 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ2_XS.gguf) | i1-IQ2_XS | 0.5 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ2_S.gguf) | i1-IQ2_S | 0.6 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ2_M.gguf) | i1-IQ2_M | 0.6 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q2_K_S.gguf) | i1-Q2_K_S | 0.6 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 0.6 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q2_K.gguf) | i1-Q2_K | 0.6 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ3_XS.gguf) | i1-IQ3_XS | 0.7 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ3_S.gguf) | i1-IQ3_S | 0.7 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q3_K_S.gguf) | i1-Q3_K_S | 0.7 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ3_M.gguf) | i1-IQ3_M | 0.7 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q3_K_M.gguf) | i1-Q3_K_M | 0.7 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q3_K_L.gguf) | i1-Q3_K_L | 0.8 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ4_XS.gguf) | i1-IQ4_XS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-IQ4_NL.gguf) | i1-IQ4_NL | 0.8 | prefer IQ4_XS |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q4_0.gguf) | i1-Q4_0 | 0.8 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q4_K_S.gguf) | i1-Q4_K_S | 0.8 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q4_K_M.gguf) | i1-Q4_K_M | 0.8 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q4_1.gguf) | i1-Q4_1 | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q5_K_S.gguf) | i1-Q5_K_S | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q5_K_M.gguf) | i1-Q5_K_M | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/KURE-v3-i1-GGUF/resolve/main/KURE-v3.i1-Q6_K.gguf) | i1-Q6_K | 1.0 | practically like static Q6_K |

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
