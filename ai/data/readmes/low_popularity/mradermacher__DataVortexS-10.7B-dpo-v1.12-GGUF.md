---
base_model: Edentns/DataVortexS-10.7B-dpo-v1.12
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
static quants of https://huggingface.co/Edentns/DataVortexS-10.7B-dpo-v1.12

<!-- provided-files -->
weighted/imatrix quants are available at https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q2_K.gguf) | Q2_K | 4.1 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q3_K_S.gguf) | Q3_K_S | 4.8 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q3_K_M.gguf) | Q3_K_M | 5.3 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q3_K_L.gguf) | Q3_K_L | 5.8 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.IQ4_XS.gguf) | IQ4_XS | 5.9 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q4_0_4_4.gguf) | Q4_0_4_4 | 6.2 | fast on arm, low quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q4_K_S.gguf) | Q4_K_S | 6.2 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q4_K_M.gguf) | Q4_K_M | 6.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q5_K_S.gguf) | Q5_K_S | 7.5 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q5_K_M.gguf) | Q5_K_M | 7.7 |  |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q6_K.gguf) | Q6_K | 8.9 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.Q8_0.gguf) | Q8_0 | 11.5 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/DataVortexS-10.7B-dpo-v1.12-GGUF/resolve/main/DataVortexS-10.7B-dpo-v1.12.f16.gguf) | f16 | 21.6 | 16 bpw, overkill |

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
