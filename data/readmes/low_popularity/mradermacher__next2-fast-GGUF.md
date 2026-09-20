---
base_model: thelamapi/next2-fast
datasets:
- mlabonne/FineTome-100k
- ITCL/FineTomeOs
- Gryphe/ChatGPT-4o-Writing-Prompts
- dongguanting/ARPO-SFT-54K
- OpenSPG/KAG-Thinker-training-dataset
- uclanlp/Brief-Pro
- CognitiveKernel/CognitiveKernel-Pro-SFT
- QuixiAI/dolphin-r1
language:
- en
- tr
- de
- fr
- es
- it
- pt
- ru
- zh
- ja
- ko
- hi
- ar
- nl
- pl
- uk
- vi
- th
- id
- cs
library_name: transformers
license: mit
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- global-ai
- multilingual
- vision-language-model
- multimodal
- lamapi
- next-2-fast
- next-series
- 4b
- efficient
- gemma-3
- transformer
- text-generation
- reasoning
- artificial-intelligence
- nlp
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
static quants of https://huggingface.co/thelamapi/next2-fast

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#next2-fast-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/next2-fast-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.mmproj-Q8_0.gguf) | mmproj-Q8_0 | 0.7 | multi-modal supplement |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.mmproj-f16.gguf) | mmproj-f16 | 1.0 | multi-modal supplement |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q2_K.gguf) | Q2_K | 1.8 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q3_K_S.gguf) | Q3_K_S | 2.0 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q3_K_M.gguf) | Q3_K_M | 2.2 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q3_K_L.gguf) | Q3_K_L | 2.3 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.IQ4_XS.gguf) | IQ4_XS | 2.4 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q4_K_S.gguf) | Q4_K_S | 2.5 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q4_K_M.gguf) | Q4_K_M | 2.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q5_K_S.gguf) | Q5_K_S | 2.9 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q5_K_M.gguf) | Q5_K_M | 2.9 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q6_K.gguf) | Q6_K | 3.3 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.Q8_0.gguf) | Q8_0 | 4.2 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/next2-fast-GGUF/resolve/main/next2-fast.f16.gguf) | f16 | 7.9 | 16 bpw, overkill |

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
