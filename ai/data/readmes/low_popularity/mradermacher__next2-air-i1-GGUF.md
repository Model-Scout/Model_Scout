---
base_model: thelamapi/next2-air
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
- next2-air
- qwen3.5
- text-generation
- image-text-to-text
- open-source
- 2b
- edge-ai
- large-language-model
- llm
- thinking-mode
- fast-inference
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
weighted/imatrix quants of https://huggingface.co/thelamapi/next2-air

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#next2-air-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/next2-air-GGUF

**This is a vision model - mmproj files (if any) will be in the [static repository](https://huggingface.co/mradermacher/next2-air-GGUF).**
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.imatrix.gguf) | imatrix | 0.1 | imatrix file (for creating your own quants) |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ1_S.gguf) | i1-IQ1_S | 0.7 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ1_M.gguf) | i1-IQ1_M | 0.8 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ2_XS.gguf) | i1-IQ2_XS | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ2_S.gguf) | i1-IQ2_S | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ2_M.gguf) | i1-IQ2_M | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 1.0 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q2_K_S.gguf) | i1-Q2_K_S | 1.0 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q2_K.gguf) | i1-Q2_K | 1.0 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ3_XS.gguf) | i1-IQ3_XS | 1.1 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q3_K_S.gguf) | i1-Q3_K_S | 1.1 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ3_S.gguf) | i1-IQ3_S | 1.1 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ3_M.gguf) | i1-IQ3_M | 1.2 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q3_K_M.gguf) | i1-Q3_K_M | 1.2 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q3_K_L.gguf) | i1-Q3_K_L | 1.2 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ4_XS.gguf) | i1-IQ4_XS | 1.3 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-IQ4_NL.gguf) | i1-IQ4_NL | 1.3 | prefer IQ4_XS |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q4_0.gguf) | i1-Q4_0 | 1.3 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q4_K_S.gguf) | i1-Q4_K_S | 1.3 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q4_K_M.gguf) | i1-Q4_K_M | 1.4 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q4_1.gguf) | i1-Q4_1 | 1.4 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q5_K_S.gguf) | i1-Q5_K_S | 1.5 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q5_K_M.gguf) | i1-Q5_K_M | 1.5 |  |
| [GGUF](https://huggingface.co/mradermacher/next2-air-i1-GGUF/resolve/main/next2-air.i1-Q6_K.gguf) | i1-Q6_K | 1.7 | practically like static Q6_K |

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
