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
<!-- ### tags: nicoboss -->
<!-- ### quants:  Q2_K IQ3_M Q4_K_S IQ3_XXS Q3_K_M small-IQ4_NL Q4_K_M IQ2_M Q6_K IQ4_XS Q2_K_S IQ1_M Q3_K_S IQ2_XXS Q3_K_L IQ2_XS Q5_K_S IQ2_S IQ1_S Q5_K_M Q4_0 IQ3_XS Q4_1 IQ3_S -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
weighted/imatrix quants of https://huggingface.co/UmbrellaInc/Prototype-Virus-1B

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Prototype-Virus-1B-i1-GGUF).***

static quants are available at https://huggingface.co/mradermacher/Prototype-Virus-1B-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.imatrix.gguf) | imatrix | 0.1 | imatrix file (for creating your own quants) |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ1_S.gguf) | i1-IQ1_S | 0.7 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ1_M.gguf) | i1-IQ1_M | 0.7 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ2_XS.gguf) | i1-IQ2_XS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ2_S.gguf) | i1-IQ2_S | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ2_M.gguf) | i1-IQ2_M | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q2_K_S.gguf) | i1-Q2_K_S | 0.8 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 0.8 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q3_K_S.gguf) | i1-Q3_K_S | 0.8 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ3_S.gguf) | i1-IQ3_S | 0.8 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ3_XS.gguf) | i1-IQ3_XS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q2_K.gguf) | i1-Q2_K | 0.8 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ3_M.gguf) | i1-IQ3_M | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ4_XS.gguf) | i1-IQ4_XS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-IQ4_NL.gguf) | i1-IQ4_NL | 0.8 | prefer IQ4_XS |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q4_0.gguf) | i1-Q4_0 | 0.8 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q3_K_M.gguf) | i1-Q3_K_M | 0.8 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q3_K_L.gguf) | i1-Q3_K_L | 0.9 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q4_1.gguf) | i1-Q4_1 | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q4_K_S.gguf) | i1-Q4_K_S | 0.9 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q4_K_M.gguf) | i1-Q4_K_M | 0.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q5_K_S.gguf) | i1-Q5_K_S | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q5_K_M.gguf) | i1-Q5_K_M | 1.0 |  |
| [GGUF](https://huggingface.co/mradermacher/Prototype-Virus-1B-i1-GGUF/resolve/main/Prototype-Virus-1B.i1-Q6_K.gguf) | i1-Q6_K | 1.1 | practically like static Q6_K |

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
