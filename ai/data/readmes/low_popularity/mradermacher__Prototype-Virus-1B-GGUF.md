---
base_model: UmbrellaInc/Prototype-Virus-1B
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
- ar
- af
- az
- es
- en
- el
- ro
- ru
- rm
- th
- uk
- uz
- pl
- pt
- fa
- sk
- sl
- da
- de
- nl
- fr
- fi
- ka
- hi
- hu
- hy
- ja
- kk
- kn
- ko
- ku
- ky
- la
- lb
- id
- is
- it
- zh
- cs
- vi
- be
- bg
- bs
- ne
- mn
library_name: transformers
license: gemma
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- next
- next-x1
- efficient
- open-source
- 1b
- huggingface
- large-language-model
- llm
- causal
- artificial-intelligence
- machine-learning
- ai-research
- natural-language-processing
- nlp
- finetuned
- lightweight
- creative
- summarization
- question-answering
- chat-model
- generative-ai
- optimized-model
- unsloth
- trl
- sft
- chemistry
- biology
- finance
- legal
- music
- art
- code
- climate
- medical
- agent
- text-generation-inference
- text-generation
- transformers
- safetensors
- gemma3
- mergekit
- merge
- uncensored
- heretic
- abliterated
- roleplay
- nsfw
- trash
- prototype
- virus
- progenitor
- low-end
- conversational
- Not-For-All-Audiences
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
static quants of https://huggingface.co/UmbrellaInc/Prototype-Virus-1B

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Prototype-Virus-1B-GGUF).***

weighted/imatrix quants are available at https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q3_K_S.gguf) | Q3_K_S | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q2_K.gguf) | Q2_K | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.IQ4_XS.gguf) | IQ4_XS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q3_K_M.gguf) | Q3_K_M | 0.8 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q3_K_L.gguf) | Q3_K_L | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q4_K_S.gguf) | Q4_K_S | 0.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q4_K_M.gguf) | Q4_K_M | 0.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q5_K_S.gguf) | Q5_K_S | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q5_K_M.gguf) | Q5_K_M | 1.0 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q6_K.gguf) | Q6_K | 1.1 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.Q8_0.gguf) | Q8_0 | 1.2 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF/resolve/main/Prototype-Virus-1B.f16.gguf) | f16 | 2.1 | 16 bpw, overkill |

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
