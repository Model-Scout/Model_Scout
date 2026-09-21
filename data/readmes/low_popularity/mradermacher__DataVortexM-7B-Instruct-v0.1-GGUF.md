---
base_model: Edentns/DataVortexM-7B-Instruct-v0.1
datasets:
- beomi/KoAlpaca-v1.1a
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
<!-- ### tags:  -->
static quants of https://huggingface.co/Edentns/DataVortexM-7B-Instruct-v0.1

<!-- provided-files -->
weighted/imatrix quants are available at https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q2_K.gguf) | Q2_K | 2.8 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q3_K_S.gguf) | Q3_K_S | 3.3 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q3_K_M.gguf) | Q3_K_M | 3.6 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q3_K_L.gguf) | Q3_K_L | 3.9 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.IQ4_XS.gguf) | IQ4_XS | 4.0 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q4_K_S.gguf) | Q4_K_S | 4.2 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q4_K_M.gguf) | Q4_K_M | 4.5 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q5_K_S.gguf) | Q5_K_S | 5.1 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q5_K_M.gguf) | Q5_K_M | 5.2 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q6_K.gguf) | Q6_K | 6.0 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexM-7B-Instruct-v0.1-GGUF/resolve/main/DataVortexM-7B-Instruct-v0.1.Q8_0.gguf) | Q8_0 | 7.8 | fast, best quality |

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
