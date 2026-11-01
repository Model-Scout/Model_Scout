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
<!-- ### tags: nicoboss -->
<!-- ### quants:  Q2_K IQ3_M Q4_K_S IQ3_XXS Q3_K_M small-IQ4_NL Q4_K_M IQ2_M Q6_K IQ4_XS Q2_K_S IQ1_M Q3_K_S IQ2_XXS Q3_K_L IQ2_XS Q5_K_S IQ2_S IQ1_S Q5_K_M Q4_0 IQ3_XS Q4_1 IQ3_S -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
weighted/imatrix quants of https://huggingface.co/thelamapi/next-70b

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#next-70b-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/next-70b-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.imatrix.gguf) | imatrix | 0.1 | imatrix file (for creating your own quants) |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ1_S.gguf) | i1-IQ1_S | 15.4 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ1_M.gguf) | i1-IQ1_M | 16.9 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 19.2 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ2_XS.gguf) | i1-IQ2_XS | 21.2 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ2_S.gguf) | i1-IQ2_S | 22.3 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ2_M.gguf) | i1-IQ2_M | 24.2 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q2_K_S.gguf) | i1-Q2_K_S | 24.6 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q2_K.gguf) | i1-Q2_K | 26.5 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 27.6 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ3_XS.gguf) | i1-IQ3_XS | 29.4 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ3_S.gguf) | i1-IQ3_S | 31.0 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q3_K_S.gguf) | i1-Q3_K_S | 31.0 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ3_M.gguf) | i1-IQ3_M | 32.0 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q3_K_M.gguf) | i1-Q3_K_M | 34.4 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q3_K_L.gguf) | i1-Q3_K_L | 37.2 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-IQ4_XS.gguf) | i1-IQ4_XS | 38.0 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q4_0.gguf) | i1-Q4_0 | 40.2 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q4_K_S.gguf) | i1-Q4_K_S | 40.4 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q4_K_M.gguf) | i1-Q4_K_M | 42.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q4_1.gguf) | i1-Q4_1 | 44.4 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q5_K_S.gguf) | i1-Q5_K_S | 48.8 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q5_K_M.gguf) | i1-Q5_K_M | 50.0 |  |
| [GGUF](https://huggingface.co/mradermacher/next-70b-i1-GGUF/resolve/main/next-70b.i1-Q6_K.gguf) | i1-Q6_K | 58.0 | practically like static Q6_K |

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
