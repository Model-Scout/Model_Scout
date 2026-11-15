---
base_model: Outlier-Ai/Outlier-10B-V2
datasets:
- Open-Orca/OpenOrca
language:
- en
- zh
- fr
- es
- pt
- de
- it
- ru
- ja
- ko
- ar
- vi
- th
- nl
- pl
library_name: transformers
license: apache-2.0
mradermacher:
  readme_rev: 1
quantized_by: mradermacher
tags:
- superseded
- archival
- mixture-of-experts
- moe
- ternary
- 1-bit
- qwen2.5
- outlier
- outlier-moe
- research
- overlay
- sparse
- local-llm
- on-device
- apple-silicon
- mac
- text-generation
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
static quants of https://huggingface.co/Outlier-Ai/Outlier-10B-V2

<!-- provided-files -->

***For a convenient overview and download list, visit our [model page for this model](https://hf.tst.eu/model#Outlier-10B-V2-GGUF).***

weighted/imatrix quants seem not to be available (by me) at this time. If they do not show up a week or so after the static ones, I have probably not planned for them. Feel free to request them by opening a Community Discussion.
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Outlier-10B-V2-GGUF/resolve/main/Outlier-10B-V2.TQ1_0.gguf) | TQ1_0 | 2.2 | tighteR TERNANY packing |
| [GGUF](https://huggingface.co/mradermacher/Outlier-10B-V2-GGUF/resolve/main/Outlier-10B-V2.TQ2_0.gguf) | TQ2_0 | 2.5 | faster ternany packing |

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
