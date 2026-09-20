---
base_model: thelamapi/next-12b
datasets:
- mlabonne/FineTome-100k
- ITCL/FineTomeOs
- Gryphe/ChatGPT-4o-Writing-Prompts
- dongguanting/ARPO-SFT-54K
- GreenerPastures/All-Your-Base-Full
- Gryphe/Opus-WritingPrompts
- HuggingFaceH4/MATH-500
- mlabonne/smoltalk-flat
- mlabonne/natural_reasoning-formatted
- OpenSPG/KAG-Thinker-training-dataset
- uclanlp/Brief-Pro
- CognitiveKernel/CognitiveKernel-Pro-SFT
- SuperbEmphasis/Claude-4.0-DeepSeek-R1-RP-SFWish
- QuixiAI/dolphin-r1
- mlabonne/lmsys-arena-human-sft-55k
language:
- tr
- en
- de
- ka
- el
- ku
- es
- sl
- sk
- af
- da
- nl
- fa
- fi
- fr
- ga
- hi
- hu
- hy
- ja
- kg
- kk
- ko
- ky
- la
- lb
- id
- it
- is
- za
- zh
- zu
- cs
- vi
- be
- bg
- bs
- ne
- mn
- rm
- ro
- ru
- te
- th
- tk
- tt
- uk
- uz
- ug
- pl
- pt
- no
library_name: transformers
license: mit
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- turkish
- türkiye
- english
- ai
- lamapi
- gemma3
- next
- next-x1
- efficient
- text-generation
- open-source
- 12b
- huggingface
- large-language-model
- llm
- causal
- transformer
- artificial-intelligence
- machine-learning
- ai-research
- natural-language-processing
- language
- multilingual
- multimodal
- nlp
- finetuned
- lightweight
- creative
- summarization
- question-answering
- chat
- generative-ai
- optimized
- unsloth
- trl
- sft
- chemistry
- code
- biology
- finance
- legal
- music
- art
- state-of-the-art
- climate
- medical
- agent
- text-generation-inference
- merge
- dense
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
static quants of https://huggingface.co/thelamapi/next-12b

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#next-12b-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/next-12b-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.mmproj-Q8_0.gguf) | mmproj-Q8_0 | 0.7 | multi-modal supplement |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.mmproj-f16.gguf) | mmproj-f16 | 1.0 | multi-modal supplement |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q2_K.gguf) | Q2_K | 4.9 |  |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q3_K_S.gguf) | Q3_K_S | 5.6 |  |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q3_K_M.gguf) | Q3_K_M | 6.1 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q3_K_L.gguf) | Q3_K_L | 6.6 |  |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.IQ4_XS.gguf) | IQ4_XS | 6.7 |  |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q4_K_S.gguf) | Q4_K_S | 7.0 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q4_K_M.gguf) | Q4_K_M | 7.4 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q5_K_S.gguf) | Q5_K_S | 8.3 |  |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q5_K_M.gguf) | Q5_K_M | 8.5 |  |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q6_K.gguf) | Q6_K | 9.8 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/next-12b-GGUF/resolve/main/next-12b.Q8_0.gguf) | Q8_0 | 12.6 | fast, best quality |

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
