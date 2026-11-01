---
base_model: thelamapi/next-32b
datasets:
- mlabonne/FineTome-100k
- CognitiveKernel/CognitiveKernel-Pro-SFT
- OpenSPG/KAG-Thinker-training-dataset
- Gryphe/ChatGPT-4o-Writing-Prompts
- QuixiAI/dolphin-r1
- uclanlp/Brief-Pro
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
license: mit
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- turkish
- türkiye
- reasoning
- ai
- lamapi
- gemma3
- next
- next-x1
- text-generation
- open-source
- 32b
- large-language-model
- llm
- transformer
- artificial-intelligence
- machine-learning
- nlp
- multilingual
- instruction-tuned
- chat
- generative-ai
- optimized
- trl
- sft
- cognitive
- analytical
- enterprise
- industrial
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
static quants of https://huggingface.co/thelamapi/next-32b

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#next-32b-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/next-32b-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q2_K.gguf) | Q2_K | 12.4 |  |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q3_K_S.gguf) | Q3_K_S | 14.5 |  |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q3_K_M.gguf) | Q3_K_M | 16.1 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q3_K_L.gguf) | Q3_K_L | 17.4 |  |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.IQ4_XS.gguf) | IQ4_XS | 18.0 |  |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q4_K_S.gguf) | Q4_K_S | 18.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q4_K_M.gguf) | Q4_K_M | 19.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q5_K_S.gguf) | Q5_K_S | 22.7 |  |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q5_K_M.gguf) | Q5_K_M | 23.3 |  |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q6_K.gguf) | Q6_K | 27.0 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/next-32b-GGUF/resolve/main/next-32b.Q8_0.gguf) | Q8_0 | 34.9 | fast, best quality |

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
