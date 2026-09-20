---
base_model: Jackrong/Qwopus-GLM-18B-Healed
language:
- en
- zh
- ko
- ja
- fr
- de
- es
library_name: transformers
license: apache-2.0
model_type: qwen3_5
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- merge
- frankenmerge
- qwen3.5
- reasoning
- text-generation
- conversational
- unsloth
- agent
- tool-use
- chain-of-thought
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
<!-- ### quants:  x-f16 Q4_K_S Q2_K Q8_0 Q6_K Q3_K_M Q3_K_S Q3_K_L Q4_K_M Q5_K_S Q5_K_M IQ4_XS -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj: 1 -->
static quants of https://huggingface.co/Jackrong/Qwopus-GLM-18B-Healed

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Qwopus-GLM-18B-Healed-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q2_K.gguf) | Q2_K | 6.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q3_K_S.gguf) | Q3_K_S | 7.3 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q3_K_M.gguf) | Q3_K_M | 8.1 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q3_K_L.gguf) | Q3_K_L | 8.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.IQ4_XS.gguf) | IQ4_XS | 9.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q4_K_S.gguf) | Q4_K_S | 9.4 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q4_K_M.gguf) | Q4_K_M | 9.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q5_K_S.gguf) | Q5_K_S | 11.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q5_K_M.gguf) | Q5_K_M | 11.5 |  |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q6_K.gguf) | Q6_K | 13.1 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/Qwopus-GLM-18B-Healed-GGUF/resolve/main/Qwopus-GLM-18B-Healed.Q8_0.gguf) | Q8_0 | 17.0 | fast, best quality |

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
