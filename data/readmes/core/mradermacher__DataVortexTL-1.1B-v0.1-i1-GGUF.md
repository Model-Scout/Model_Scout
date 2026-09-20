---
base_model: Edentns/DataVortexTL-1.1B-v0.1
datasets:
- beomi/KoAlpaca-v1.1a
- jojo0217/korean_rlhf_dataset
- kyujinpy/OpenOrca-KO
- nlpai-lab/kullm-v2
language:
- ko
library_name: transformers
license: cc-by-nc-sa-4.0
quantized_by: mradermacher
tags:
- text-generation
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags: nicoboss -->
weighted/imatrix quants of https://huggingface.co/Edentns/DataVortexTL-1.1B-v0.1

<!-- provided-files -->
static quants are available at https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ1_S.gguf) | i1-IQ1_S | 0.4 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ1_M.gguf) | i1-IQ1_M | 0.4 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 0.4 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ2_XS.gguf) | i1-IQ2_XS | 0.5 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ2_S.gguf) | i1-IQ2_S | 0.5 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ2_M.gguf) | i1-IQ2_M | 0.5 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q2_K.gguf) | i1-Q2_K | 0.5 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 0.5 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ3_XS.gguf) | i1-IQ3_XS | 0.6 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q3_K_S.gguf) | i1-Q3_K_S | 0.6 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ3_S.gguf) | i1-IQ3_S | 0.6 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ3_M.gguf) | i1-IQ3_M | 0.6 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q3_K_M.gguf) | i1-Q3_K_M | 0.6 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q3_K_L.gguf) | i1-Q3_K_L | 0.7 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-IQ4_XS.gguf) | i1-IQ4_XS | 0.7 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q4_0_4_4.gguf) | i1-Q4_0_4_4 | 0.7 | fast on arm, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q4_0_4_8.gguf) | i1-Q4_0_4_8 | 0.7 | fast on arm+i8mm, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q4_0_8_8.gguf) | i1-Q4_0_8_8 | 0.7 | fast on arm+sve, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q4_0.gguf) | i1-Q4_0 | 0.7 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q4_K_S.gguf) | i1-Q4_K_S | 0.7 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q4_K_M.gguf) | i1-Q4_K_M | 0.8 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q5_K_S.gguf) | i1-Q5_K_S | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q5_K_M.gguf) | i1-Q5_K_M | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF/resolve/main/DataVortexTL-1.1B-v0.1.i1-Q6_K.gguf) | i1-Q6_K | 1.0 | practically like static Q6_K |

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
