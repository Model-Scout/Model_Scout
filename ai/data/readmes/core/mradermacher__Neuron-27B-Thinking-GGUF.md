---
base_model: Neura-Tech-AI/Neuron-27B-Thinking
language:
- en
- hi
- zh
- es
- fr
- de
- ar
- ja
- ko
- pt
- ru
- it
- tr
- id
- vi
- th
- pl
- nl
- sv
- da
- no
- fi
- cs
- ro
- hu
- el
- he
- fa
- ur
- bn
- ta
- te
- mr
- gu
- pa
- ml
- kn
- uk
- bg
- sr
- hr
- sk
- sl
- ms
- tl
- sw
- af
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- neuron
- neura-tech-ai
- 27B
- text-generation
- qwen3
- conversational
- reasoning
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
static quants of https://huggingface.co/Neura-Tech-AI/Neuron-27B-Thinking

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Neuron-27B-Thinking-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/Neuron-27B-Thinking-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q2_K.gguf) | Q2_K | 11.0 |  |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q3_K_S.gguf) | Q3_K_S | 12.4 |  |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q3_K_M.gguf) | Q3_K_M | 13.6 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q3_K_L.gguf) | Q3_K_L | 14.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.IQ4_XS.gguf) | IQ4_XS | 15.5 |  |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q4_K_S.gguf) | Q4_K_S | 15.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q4_K_M.gguf) | Q4_K_M | 16.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q5_K_S.gguf) | Q5_K_S | 19.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q5_K_M.gguf) | Q5_K_M | 19.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q6_K.gguf) | Q6_K | 22.5 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/Neuron-27B-Thinking-GGUF/resolve/main/Neuron-27B-Thinking.Q8_0.gguf) | Q8_0 | 29.1 | fast, best quality |

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
