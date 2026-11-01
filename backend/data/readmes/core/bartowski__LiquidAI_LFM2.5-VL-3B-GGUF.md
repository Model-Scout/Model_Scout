---
quantized_by: bartowski
pipeline_tag: image-text-to-text
base_model: LiquidAI/LFM2.5-VL-3B
language:
- ar
- zh
- en
- fr
- de
- hi
- id
- it
- ja
- ko
- pl
- pt
- ru
- es
- th
- vi
license_name: lfm1.0
tags:
- liquid
- lfm2.5
- edge
license_link: LICENSE
license: other
base_model_relation: quantized
---

## Llamacpp imatrix Quantizations of LFM2.5-VL-3B by LiquidAI

Using <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggml-org/llama.cpp/releases/tag/b10362">b10362</a> for quantization.

Original model: https://huggingface.co/LiquidAI/LFM2.5-VL-3B

**Model details:**
- Parameter count: 3B
- Input support: text, image (with mmproj file) - [details](#multimodal)
- MTP: no
- imatrix: yes - [details](#imatrix)

[How to run](#how-to-run)

## Prompt format

```
<|startoftext|><|im_start|>system
{system_prompt}<|im_end|>
<|im_start|>user
{prompt}<|im_end|>
<|im_start|>assistant
```

**Don't know which to choose?** Grab [Q4_K_M](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q4_K_M.gguf) (1.68GB) - usually a good mix of size and performance. Download instructions available [here](#downloading-using-the-hugging-face-cli)

## Available files:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [LiquidAI_LFM2.5-VL-3B-bf16.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-bf16.gguf) | bf16 | 5.40GB | false | Full BF16 weights. |
| [LiquidAI_LFM2.5-VL-3B-Q8_0.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q8_0.gguf) | Q8_0 | 2.87GB | false | Extremely high quality, generally unneeded but max available quant. |
| [LiquidAI_LFM2.5-VL-3B-Q6_K_L.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q6_K_L.gguf) | Q6_K_L | 2.30GB | false | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q6_K.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q6_K.gguf) | Q6_K | 2.24GB | false | Very high quality, near perfect, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q5_K_L.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q5_K_L.gguf) | Q5_K_L | 2.01GB | false | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q5_K_M.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q5_K_M.gguf) | Q5_K_M | 1.95GB | false | High quality, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q5_K_S.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q5_K_S.gguf) | Q5_K_S | 1.90GB | false | High quality, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q4_1.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q4_1.gguf) | Q4_1 | 1.75GB | false | Legacy format, similar performance to Q4_K_S but with improved tokens/watt on Apple silicon. |
| [LiquidAI_LFM2.5-VL-3B-Q4_K_L.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q4_K_L.gguf) | Q4_K_L | 1.75GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q4_K_M.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q4_K_M.gguf) | Q4_K_M | 1.68GB | false | Good quality, default size for most use cases, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q4_K_S.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q4_K_S.gguf) | Q4_K_S | 1.61GB | false | Slightly lower quality with more space savings, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q4_0.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q4_0.gguf) | Q4_0 | 1.60GB | false | Legacy format, kept for compatibility with older tools. |
| [LiquidAI_LFM2.5-VL-3B-IQ4_NL.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-IQ4_NL.gguf) | IQ4_NL | 1.60GB | false | Similar to IQ4_XS, but slightly larger. |
| [LiquidAI_LFM2.5-VL-3B-IQ4_XS.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-IQ4_XS.gguf) | IQ4_XS | 1.52GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [LiquidAI_LFM2.5-VL-3B-Q3_K_XL.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q3_K_XL.gguf) | Q3_K_XL | 1.52GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [LiquidAI_LFM2.5-VL-3B-Q3_K_L.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q3_K_L.gguf) | Q3_K_L | 1.45GB | false | Lower quality but usable, good for low RAM availability. |
| [LiquidAI_LFM2.5-VL-3B-Q3_K_M.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q3_K_M.gguf) | Q3_K_M | 1.37GB | false | Low quality. |
| [LiquidAI_LFM2.5-VL-3B-IQ3_M.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-IQ3_M.gguf) | IQ3_M | 1.29GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [LiquidAI_LFM2.5-VL-3B-Q3_K_S.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q3_K_S.gguf) | Q3_K_S | 1.28GB | false | Low quality, not recommended. |
| [LiquidAI_LFM2.5-VL-3B-IQ3_XS.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-IQ3_XS.gguf) | IQ3_XS | 1.23GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [LiquidAI_LFM2.5-VL-3B-Q2_K_L.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q2_K_L.gguf) | Q2_K_L | 1.17GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [LiquidAI_LFM2.5-VL-3B-IQ3_XXS.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-IQ3_XXS.gguf) | IQ3_XXS | 1.13GB | false | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [LiquidAI_LFM2.5-VL-3B-Q2_K.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-Q2_K.gguf) | Q2_K | 1.10GB | false | Very low quality but surprisingly usable. |
| [LiquidAI_LFM2.5-VL-3B-IQ2_M.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-IQ2_M.gguf) | IQ2_M | 1.02GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |

Download a specific file:

```
hf download bartowski/LiquidAI_LFM2.5-VL-3B-GGUF --include "LiquidAI_LFM2.5-VL-3B-Q4_K_M.gguf" --local-dir ./
```

## Downloading using the Hugging Face CLI

<details>
  <summary>Click to view download instructions</summary>

First, make sure you have the Hugging Face CLI installed:

```
pip install -U "huggingface_hub[cli]"
```

Download a specific file:

```
hf download bartowski/LiquidAI_LFM2.5-VL-3B-GGUF --include "LiquidAI_LFM2.5-VL-3B-Q4_K_M.gguf" --local-dir ./
```

</details>

## How to run

These quants run with [llama.cpp](https://github.com/ggml-org/llama.cpp) - installable in one line via [llama.app](https://llama.app/):

```
curl -LsSf https://llama.app/install.sh | sh
llama-server -hf bartowski/LiquidAI_LFM2.5-VL-3B-GGUF:Q4_K_M
```

llama-server includes a built-in chat web UI, served at http://localhost:8080 by default.

These quants were made with llama.cpp release b10362 - if this model's architecture is newly supported, you'll need that release or newer to run them.

They also work in: [LM Studio](https://lmstudio.ai/) · [koboldcpp](https://github.com/LostRuins/koboldcpp) · [ramalama](https://github.com/containers/ramalama) · [Jan AI](https://www.jan.ai/) · [Text Generation Web UI](https://github.com/oobabooga/text-generation-webui) · [LoLLMs](https://github.com/ParisNeo/lollms) · [Atomic Chat](https://atomic.chat/)

## Multimodal

This model supports image input. Alongside the quants, this repo includes the multimodal projector files [mmproj-LiquidAI_LFM2.5-VL-3B-f16.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/mmproj-LiquidAI_LFM2.5-VL-3B-f16.gguf) and [mmproj-LiquidAI_LFM2.5-VL-3B-bf16.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/mmproj-LiquidAI_LFM2.5-VL-3B-bf16.gguf), which pair with any quant above.

llama.cpp downloads the mmproj automatically when using `-hf` as shown above; if you're loading files manually, pass it with `--mmproj`.

## imatrix

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/82ae9b520227f57d79ba04add13d0d0d). The imatrix is available here: [LiquidAI_LFM2.5-VL-3B-imatrix.gguf](https://huggingface.co/bartowski/LiquidAI_LFM2.5-VL-3B-GGUF/blob/main/LiquidAI_LFM2.5-VL-3B-imatrix.gguf).

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

## ARM/AVX information

llama.cpp automatically "repacks" weights into an interleaved layout at load time for faster inference on ARM and AVX machines - details in [this PR](https://github.com/ggml-org/llama.cpp/pull/9921). This once required downloading special Q4_0_4_4/4_8/8_8 files; those are long gone. Online repacking now covers Q4_0, IQ4_NL, and most K-quants, so no special quant choice is needed for CPU inference.

## Which file should I choose?

<details>
  <summary>Click here for details</summary>

An older (early 2024) but still useful write-up with charts comparing quant performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

Hugging Face can also do this math for you: add your hardware in your [Local Apps settings](https://huggingface.co/settings/local-apps) and the model page will show which files fit.

Next, you'll need to decide if you want to use an 'I-quant' or a 'K-quant'.

If you don't want to think too much, grab one of the K-quants. These are in format 'QX_K_X', like Q5_K_M.

If you want to get more into the weeds, you can check out this extremely useful feature chart:

[llama.cpp feature matrix](https://github.com/ggml-org/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

</details>

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset.

Thank you ZeroWw for the inspiration to experiment with embed/output.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
