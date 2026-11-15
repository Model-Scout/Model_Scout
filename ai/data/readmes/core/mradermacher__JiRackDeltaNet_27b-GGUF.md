---
base_model: CMSManhattan/JiRackDeltaNet_27b
language:
- en
- zh
- ja
- ko
- fr
- es
- pt
- de
- it
- ru
- ar
- vi
- th
library_name: transformers
license: mit
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- text-generation
- deltanet
- qwen3.8
- gguf
- cpu
- efficient
- low-memory
- ternary
- bitnet
- jirack
- web-ui
- routing
- tool-call
- robotics
- ollama
- ternary-weights
- ternary-transformer
- quantization
- 1.58-bit
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
<!-- ### quants:  TQ1_0 TQ2_0 -->
<!-- ### quants_skip:  -->
<!-- ### skip_mmproj:  -->
static quants of https://huggingface.co/CMSManhattan/JiRackDeltaNet_27b

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#JiRackDeltaNet_27b-GGUF).***

weighted/imatrix quants seem not to be available (by me) at this time. If they do not show up a week or so after the static ones, I have probably not planned for them. Feel free to request them by opening a Community Discussion.
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/JiRackDeltaNet_27b-GGUF/resolve/main/JiRackDeltaNet_27b.TQ1_0.gguf) | TQ1_0 | 7.1 | tighteR TERNANY packing |
| [GGUF](https://huggingface.co/mradermacher/JiRackDeltaNet_27b-GGUF/resolve/main/JiRackDeltaNet_27b.TQ2_0.gguf) | TQ2_0 | 8.3 | faster ternany packing |

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
