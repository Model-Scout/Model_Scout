---
base_model: nayohan/llama3-8b-it-translation-general-en-ko-1sent
datasets:
- nayohan/aihub-en-ko-translation-1.2m
language:
- en
- ko
library_name: transformers
license: llama3
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
static quants of https://huggingface.co/nayohan/llama3-8b-it-translation-general-en-ko-1sent

<!-- provided-files -->
weighted/imatrix quants are available at https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-i1-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q2_K.gguf) | Q2_K | 3.3 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q3_K_S.gguf) | Q3_K_S | 3.8 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q3_K_M.gguf) | Q3_K_M | 4.1 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q3_K_L.gguf) | Q3_K_L | 4.4 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.IQ4_XS.gguf) | IQ4_XS | 4.6 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q4_K_S.gguf) | Q4_K_S | 4.8 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q4_K_M.gguf) | Q4_K_M | 5.0 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q5_K_S.gguf) | Q5_K_S | 5.7 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q5_K_M.gguf) | Q5_K_M | 5.8 |  |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q6_K.gguf) | Q6_K | 6.7 | very good quality |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.Q8_0.gguf) | Q8_0 | 8.6 | fast, best quality |
| [GGUF](https://huggingface.co/mradermacher/llama3-8b-it-translation-general-en-ko-1sent-GGUF/resolve/main/llama3-8b-it-translation-general-en-ko-1sent.f16.gguf) | f16 | 16.2 | 16 bpw, overkill |

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
