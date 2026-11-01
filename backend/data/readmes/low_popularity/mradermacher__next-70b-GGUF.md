---
base_model: thelamapi/next-70b
datasets:
- mlabonne/FineTome-100k
- Gryphe/ChatGPT-4o-Writing-Prompts
- uclanlp/Brief-Pro
- neulab/agent-data-collection
- openai/gsm8k
- HuggingFaceH4/MATH-500
- princeton-nlp/SWE-bench_Verified
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
- ai
- lamapi
- next
- next-x1
- text-generation
- open-source
- 70b
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
static quants of https://huggingface.co/thelamapi/next-70b

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#next-70b-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/next-70b-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q2_K.gguf) | Q2_K | 26.5 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q3_K_S.gguf) | Q3_K_S | 31.0 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q3_K_M.gguf) | Q3_K_M | 34.4 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q3_K_L.gguf) | Q3_K_L | 37.2 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.IQ4_XS.gguf) | IQ4_XS | 38.4 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q4_K_S.gguf) | Q4_K_S | 40.4 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q4_K_M.gguf) | Q4_K_M | 42.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q5_K_S.gguf) | Q5_K_S | 48.8 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q5_K_M.gguf) | Q5_K_M | 50.0 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q6_K.gguf) | Q6_K | 58.0 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/next-70b-GGUF/resolve/main/next-70b.Q8_0.gguf) | Q8_0 | 75.1 | fast, best quality |

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
