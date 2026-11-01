---
base_model: Edentns/DataVortexS-10.7B-dpo-v1.11
language:
- ko
library_name: transformers
license: cc-by-nc-4.0
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
weighted/imatrix quants of https://huggingface.co/Edentns/DataVortexS-10.7B-dpo-v1.11

<!-- provided-files -->
static quants are available at https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ1_S.gguf) | i1-IQ1_S | 2.5 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ1_M.gguf) | i1-IQ1_M | 2.7 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 3.1 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ2_XS.gguf) | i1-IQ2_XS | 3.4 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ2_S.gguf) | i1-IQ2_S | 3.6 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ2_M.gguf) | i1-IQ2_M | 3.9 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q2_K.gguf) | i1-Q2_K | 4.2 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 4.3 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ3_XS.gguf) | i1-IQ3_XS | 4.6 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q3_K_S.gguf) | i1-Q3_K_S | 4.8 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ3_S.gguf) | i1-IQ3_S | 4.9 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ3_M.gguf) | i1-IQ3_M | 5.0 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q3_K_M.gguf) | i1-Q3_K_M | 5.4 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q3_K_L.gguf) | i1-Q3_K_L | 5.8 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-IQ4_XS.gguf) | i1-IQ4_XS | 6.0 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q4_0_4_4.gguf) | i1-Q4_0_4_4 | 6.3 | fast on arm, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q4_0_4_8.gguf) | i1-Q4_0_4_8 | 6.3 | fast on arm+i8mm, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q4_0_8_8.gguf) | i1-Q4_0_8_8 | 6.3 | fast on arm+sve, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q4_0.gguf) | i1-Q4_0 | 6.3 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q4_K_S.gguf) | i1-Q4_K_S | 6.3 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q4_K_M.gguf) | i1-Q4_K_M | 6.7 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q5_K_S.gguf) | i1-Q5_K_S | 7.6 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q5_K_M.gguf) | i1-Q5_K_M | 7.8 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.11-i1-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.11.i1-Q6_K.gguf) | i1-Q6_K | 9.0 | practically like static Q6_K |

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
