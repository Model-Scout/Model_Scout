---
base_model: thelamapi/next2.5
datasets:
- mlabonne/FineTome-100k
- CognitiveKernel/CognitiveKernel-Pro-SFT
- OpenSPG/KAG-Thinker-training-dataset
- Gryphe/ChatGPT-4o-Writing-Prompts
language:
- tr
- en
- de
- es
- fr
- ru
- zh
- ja
- ko
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- turkish
- türkiye
- reasoning
- vision-language
- vlm
- multimodal
- lamapi
- next2.5
- qwen3.5
- gemma-3
- text-generation
- image-text-to-text
- open-source
- 4b
- edge-ai
- large-language-model
- llm
- thinking-mode
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
static quants of https://huggingface.co/thelamapi/next2.5

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#next2.5-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/next2.5-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.mmproj-Q8_0.gguf) | mmproj-Q8_0 | 0.5 | multi-modal supplement |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.mmproj-f16.gguf) | mmproj-f16 | 0.8 | multi-modal supplement |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q2_K.gguf) | Q2_K | 1.9 |  |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q3_K_S.gguf) | Q3_K_S | 2.2 |  |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q3_K_M.gguf) | Q3_K_M | 2.4 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q3_K_L.gguf) | Q3_K_L | 2.5 |  |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.IQ4_XS.gguf) | IQ4_XS | 2.6 |  |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q4_K_S.gguf) | Q4_K_S | 2.7 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q4_K_M.gguf) | Q4_K_M | 2.8 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q5_K_S.gguf) | Q5_K_S | 3.1 |  |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q5_K_M.gguf) | Q5_K_M | 3.2 |  |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q6_K.gguf) | Q6_K | 3.6 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.Q8_0.gguf) | Q8_0 | 4.6 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/next2.5-GGUF/resolve/main/next2.5.f16.gguf) | f16 | 8.5 | 16 bpw, overkill |

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
