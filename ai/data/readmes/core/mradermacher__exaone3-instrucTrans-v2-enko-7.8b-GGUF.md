---
base_model: Translation-EnKo/exaone3-instrucTrans-v2-enko-7.8b
datasets:
- nayohan/aihub-en-ko-translation-12m
- nayohan/instruction_en_ko_translation_1.4m
- Translation-EnKo/trc_uniform_313k_eval_45_filtered
language:
- en
- ko
library_name: transformers
quantized_by: mradermacher
tags:
- translation
- enko
- ko
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags:  -->
static quants of https://huggingface.co/Translation-EnKo/exaone3-instrucTrans-v2-enko-7.8b

<!-- provided-files -->
weighted/imatrix quants are available at https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q2_K.gguf) | Q2_K | 3.2 |  |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q3_K_S.gguf) | Q3_K_S | 3.6 |  |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q3_K_M.gguf) | Q3_K_M | 4.0 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q3_K_L.gguf) | Q3_K_L | 4.3 |  |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.IQ4_XS.gguf) | IQ4_XS | 4.4 |  |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q4_K_S.gguf) | Q4_K_S | 4.6 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q4_K_M.gguf) | Q4_K_M | 4.9 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q5_K_S.gguf) | Q5_K_S | 5.5 |  |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q5_K_M.gguf) | Q5_K_M | 5.7 |  |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q6_K.gguf) | Q6_K | 6.5 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.Q8_0.gguf) | Q8_0 | 8.4 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF/resolve/main/exaone3-instrucTrans-v2-enko-7.8b.f16.gguf) | f16 | 15.7 | 16 bpw, overkill |

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
