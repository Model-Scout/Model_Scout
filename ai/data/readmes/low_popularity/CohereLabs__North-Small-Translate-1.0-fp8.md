---
inference: false
library_name: transformers
language:
- en
- sq
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- es
- et
- fa
- fi
- fil
- fr
- ga
- he
- hi
- hr
- hu
- id
- is
- it
- ja
- ko
- lt
- lv
- ms
- mt
- nl
- 'no'
- pa
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
language_bcp47:
- zh-Hant
- zh-Hans
license: cc-by-nc-4.0
tags:
- translation
- conversational
- chat
base_model: CohereLabs/North-Small-Translate-1.0
base_model_relation: quantized
extra_gated_prompt: >-
  By submitting this form, you agree to the [License
  Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and acknowledge that the
  information you provide will be collected, used, and shared in accordance with
  Cohere’s [Privacy Policy]( https://cohere.com/privacy). You’ll receive email
  updates about Cohere Labs and Cohere research, events, products and services.
  You can unsubscribe at any time.
extra_gated_fields:
  Name: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
---

# **Model Card for North Small Translate (FP8)**

## **Model Summary**

North Small Translate is an open weights research release of a sparse Mixture-of-Experts model with 25 billion active parameters and 218 billion total parameters, specialized for high-quality machine translation across 50 languages. This repository holds the **FP8** checkpoint.

Developed by: [Cohere](https://cohere.com/) and [Cohere Labs](https://cohere.com/research)

* Point of Contact: [**Cohere Labs**](mailto:labs@cohere.com)
* License: [CC BY-NC 4.0](https://cohere.com/cohere-labs-cc-by-nc-license), requires also adhering to **[Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)**
* Model: North-Small-Translate-1.0-fp8
* Model Size: 25B active parameters, 218B total parameters
* Context length: 16K input & 16K output
* Quantization: FP8 (W8A8)

**Try North Small Translate**

You can try out North Small Translate before downloading the weights in our hosted [Hugging Face Space](https://huggingface.co/spaces/CohereLabs/North-Small-Translate-1.0).

**Available quantizations**

The following quantizations are available, with example minimum GPU requirements.

| Quantization | Blackwell | Hopper |
| :---- | :---- | :---- |
| [BF16 (16-bit)](https://huggingface.co/CohereLabs/North-Small-Translate-1.0) | 4 x B200 | 8 x H100 |
| [FP8 (8-bit)](https://huggingface.co/CohereLabs/North-Small-Translate-1.0-fp8) | 2 x B200 | 4 x H100 |
| [NVFP4 W4A16 (4-bit weights)](https://huggingface.co/CohereLabs/North-Small-Translate-1.0-w4a16) | 1 x B200 | 2 x H100 |

All three variants are the checkpoints Cohere serves in production for this model.

**Usage**

To use this model in transformers, please use our [BF16 model weights](https://huggingface.co/CohereLabs/North-Small-Translate-1.0). This FP8 checkpoint is designed to be served with vLLM.

**vLLM**

Accurate response parsing requires installing [Cohere's `melody` library](https://pypi.org/project/cohere-melody/).

```shell
uv pip install vllm
uv pip install cohere_melody>=0.9.0
```

Then the vLLM server can be started with the following command:

```shell
# This is for H100, adjust tp for your device
vllm serve CohereLabs/North-Small-Translate-1.0-fp8 \
  -tp 4 \
  --max-model-len 32768 \
  --tool-call-parser cohere_command4 \
  --reasoning-parser cohere_command4 \
  --enable-auto-tool-choice
```

We recommend greedy decoding, which is what the production deployment of this model uses.

**System instructions**

The chat template applies a default system instruction that names the model and sets its safety defaults. You can replace it by passing your own `platform_instruction_override` when applying the chat template, for example through vLLM's `chat_template_kwargs`. Per-conversation instructions can also be supplied as an ordinary `system` message, which is appended after the default instruction rather than replacing it.

## **Model Details**

**Input**: Text only.

**Output**: Model generates text.

**Model Architecture**: North Small Translate is a decoder-only sparse Mixture-of-Experts Transformer model. With 25B active parameters and 218B total parameters, it has 128 experts, of which 8 are activated per token, alongside shared experts applied to every token. The attention layers interleave sliding-window attention layers (window size 4096) using Rotary Positional Embeddings with global attention layers without positional embeddings, in a 3:1 ratio, as first introduced in Command A. The router applies a sigmoid activation over the expert logits and normalizes over the selected top-k. The model was post-trained specifically for translation quality.

**Quantization Methodology:** This checkpoint uses FP8 W8A8 quantization in the `compressed-tensors` format: 8-bit float weights with per-channel static scales, and 8-bit float activations with per-token dynamic scales. Every linear layer is quantized except the MoE routers and the output head, which are kept at higher precision because they are small and disproportionately sensitive. This halves the memory footprint relative to BF16, from roughly 437GB to 220GB.

**Languages covered:** The model supports translation across 50 languages: English, Albanian, Arabic, Bulgarian, Bengali, Catalan, Czech, Danish, German, Greek, Spanish, Estonian, Persian, Finnish, Filipino, French, Irish, Hebrew, Hindi, Croatian, Hungarian, Indonesian, Icelandic, Italian, Japanese, Korean, Lithuanian, Latvian, Malay, Maltese, Dutch, Norwegian, Punjabi, Polish, Portuguese, Romanian, Russian, Slovak, Slovenian, Serbian, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Traditional Chinese, Simplified Chinese.

**Context Length:** North Small Translate supports a context length of 16K input & 16K output.

## **Evaluation**

**Figure 1. WMT26 performance across all evaluated languages.** North Small Translate scores 83.60, increasing to 84.36 with the agentic multi-pass translation workflow. Figure and evaluation details are from the [North Small Translate launch blog post](https://cohere.com/blog/north-small-translate).

![WMT26 all-languages scores comparing North Small Translate with other translation models](https://cdn-uploads.huggingface.co/production/uploads/noauth/6_Ot_-cH-dfo_JThtCHZ2.png)

## **Model Card Contact**

For errors or additional questions about details in this model card, contact [labs@cohere.com](mailto:labs@cohere.com).

## **Terms of Use:**

We hope that the release of this model will make community-based research efforts more accessible, by releasing the weights of a highly performant translation model to researchers all over the world. This model is governed by a [CC BY-NC 4.0](https://cohere.com/c4ai-cc-by-nc-license) License (Non-Commercial) with an acceptable use addendum, *and also requires adhering to [Cohere Lab's Acceptable Use Policy](https://docs.cohere.com/docs/c4ai-acceptable-use-policy)*. If you are interested in commercial use, please contact [Cohere's Sales team](https://cohere.com/contact-sales).

## **Try it now:**

You can use North Small Translate in our dedicated [Hugging Face Space](https://huggingface.co/spaces/CohereLabs/North-Small-Translate-1.0).
