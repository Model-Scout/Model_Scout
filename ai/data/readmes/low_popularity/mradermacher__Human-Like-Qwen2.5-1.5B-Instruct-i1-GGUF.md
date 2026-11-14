---
base_model: yasserrmd/Human-Like-Qwen2.5-1.5B-Instruct
datasets:
- HumanLLMs/Human-Like-DPO-Dataset
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
library_name: transformers
license: other
quantized_by: mradermacher
tags:
- autotrain
- text-generation-inference
- text-generation
- peft
---
## About

<!-- ### quantize_version: 2 -->
<!-- ### output_tensor_quantised: 1 -->
<!-- ### convert_type: hf -->
<!-- ### vocab_type:  -->
<!-- ### tags: nicoboss -->
weighted/imatrix quants of https://huggingface.co/yasserrmd/Human-Like-Qwen2.5-1.5B-Instruct

<!-- provided-files -->
static quants are available at https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-GGUF
## Usage

If you are unsure how to use GGUF files, refer to one of [TheBloke's
READMEs](https://huggingface.co/TheBloke/KafkaLM-70B-German-V0.1-GGUF) for
more details, including on how to concatenate multi-part files.

## Provided Quants

(sorted by size, not necessarily quality. IQ-quants are often preferable over similar sized non-IQ quants)

| Link | Type | Size/GB | Notes |
|:-----|:-----|--------:|:------|
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ1_S.gguf) | i1-IQ1_S | 0.5 | for the desperate |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ1_M.gguf) | i1-IQ1_M | 0.6 | mostly desperate |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ2_XXS.gguf) | i1-IQ2_XXS | 0.6 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ2_XS.gguf) | i1-IQ2_XS | 0.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ2_S.gguf) | i1-IQ2_S | 0.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ2_M.gguf) | i1-IQ2_M | 0.7 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q2_K_S.gguf) | i1-Q2_K_S | 0.7 | very low quality |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ3_XXS.gguf) | i1-IQ3_XXS | 0.8 | lower quality |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q2_K.gguf) | i1-Q2_K | 0.8 | IQ3_XXS probably better |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ3_XS.gguf) | i1-IQ3_XS | 0.8 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q3_K_S.gguf) | i1-Q3_K_S | 0.9 | IQ3_XS probably better |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ3_S.gguf) | i1-IQ3_S | 0.9 | beats Q3_K* |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ3_M.gguf) | i1-IQ3_M | 0.9 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q3_K_M.gguf) | i1-Q3_K_M | 0.9 | IQ3_S probably better |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q3_K_L.gguf) | i1-Q3_K_L | 1.0 | IQ3_M probably better |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ4_XS.gguf) | i1-IQ4_XS | 1.0 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-IQ4_NL.gguf) | i1-IQ4_NL | 1.0 | prefer IQ4_XS |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q4_0.gguf) | i1-Q4_0 | 1.0 | fast, low quality |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q4_K_S.gguf) | i1-Q4_K_S | 1.0 | optimal size/speed/quality |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q4_K_M.gguf) | i1-Q4_K_M | 1.1 | fast, recommended |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q4_1.gguf) | i1-Q4_1 | 1.1 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q5_K_S.gguf) | i1-Q5_K_S | 1.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q5_K_M.gguf) | i1-Q5_K_M | 1.2 |  |
| [GGUF](https://huggingface.co/mradermacher/Human-Like-Qwen2.5-1.5B-Instruct-i1-GGUF/resolve/main/Human-Like-Qwen2.5-1.5B-Instruct.i1-Q6_K.gguf) | i1-Q6_K | 1.4 | practically like static Q6_K |

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
