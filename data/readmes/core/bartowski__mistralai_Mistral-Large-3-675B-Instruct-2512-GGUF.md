---
quantized_by: bartowski
pipeline_tag: image-text-to-text
tags:
- mistral-common
base_model: mistralai/Mistral-Large-3-675B-Instruct-2512
inference: false
language:
- en
- fr
- es
- de
- it
- pt
- nl
- zh
- ja
- ko
- ar
license: apache-2.0
extra_gated_description: >-
  If you want to learn more about how we process your personal data, please read
  our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
base_model_relation: quantized
---

## Llamacpp imatrix Quantizations of Mistral-Large-3-675B-Instruct-2512 by mistralai

Using <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggml-org/llama.cpp/releases/tag/b7268">b7268</a> for quantization.

Original model: https://huggingface.co/mistralai/Mistral-Large-3-675B-Instruct-2512-BF16

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8) combined with a subset of combined_all_small.parquet from Ed Addario [here](https://huggingface.co/datasets/eaddario/imatrix-calibration/blob/main/combined_all_small.parquet)

Run them in [LM Studio](https://lmstudio.ai/)

Run them directly with [llama.cpp](https://github.com/ggml-org/llama.cpp), or any other llama.cpp based project

## Prompt format

No prompt format found, check original model page

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [Mistral-Large-3-675B-Instruct-2512-Q8_0.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q8_0) | Q8_0 | 715.68GB | true | Extremely high quality, generally unneeded but max available quant. |
| [Mistral-Large-3-675B-Instruct-2512-Q6_K.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q6_K) | Q6_K | 554.86GB | true | Very high quality, near perfect, *recommended*. |
| [Mistral-Large-3-675B-Instruct-2512-Q5_K_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q5_K_M) | Q5_K_M | 480.76GB | true | High quality, *recommended*. |
| [Mistral-Large-3-675B-Instruct-2512-Q4_1.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q4_1) | Q4_1 | 423.00GB | true | Legacy format, similar performance to Q4_K_S but with improved tokens/watt on Apple silicon. |
| [Mistral-Large-3-675B-Instruct-2512-Q4_K_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q4_K_M) | Q4_K_M | 411.35GB | true | Good quality, default size for most use cases, *recommended*. |
| [Mistral-Large-3-675B-Instruct-2512-Q4_K_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q4_K_S) | Q4_K_S | 396.12GB | true | Slightly lower quality with more space savings, *recommended*. |
| [Mistral-Large-3-675B-Instruct-2512-Q4_0.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q4_0) | Q4_0 | 388.39GB | true | Legacy format, offers online repacking for ARM and AVX CPU inference. |
| [Mistral-Large-3-675B-Instruct-2512-IQ4_NL.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ4_NL) | IQ4_NL | 382.45GB | true | Similar to IQ4_XS, but slightly larger. Offers online repacking for ARM CPU inference. |
| [Mistral-Large-3-675B-Instruct-2512-IQ4_XS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ4_XS) | IQ4_XS | 361.95GB | true | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Mistral-Large-3-675B-Instruct-2512-Q3_K_XL.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q3_K_XL) | Q3_K_XL | 322.50GB | true | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [Mistral-Large-3-675B-Instruct-2512-Q3_K_L.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q3_K_L) | Q3_K_L | 321.68GB | true | Lower quality but usable, good for low RAM availability. |
| [Mistral-Large-3-675B-Instruct-2512-Q3_K_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q3_K_M) | Q3_K_M | 309.90GB | true | Low quality. |
| [Mistral-Large-3-675B-Instruct-2512-IQ3_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ3_M) | IQ3_M | 309.86GB | true | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [Mistral-Large-3-675B-Instruct-2512-Q3_K_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q3_K_S) | Q3_K_S | 295.34GB | true | Low quality, not recommended. |
| [Mistral-Large-3-675B-Instruct-2512-IQ3_XS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ3_XS) | IQ3_XS | 279.13GB | true | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [Mistral-Large-3-675B-Instruct-2512-IQ3_XXS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ3_XXS) | IQ3_XXS | 269.62GB | true | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [Mistral-Large-3-675B-Instruct-2512-Q2_K_L.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q2_K_L) | Q2_K_L | 240.74GB | true | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [Mistral-Large-3-675B-Instruct-2512-Q2_K.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-Q2_K) | Q2_K | 239.83GB | true | Very low quality but surprisingly usable. |
| [Mistral-Large-3-675B-Instruct-2512-IQ2_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ2_M) | IQ2_M | 216.21GB | true | Relatively low quality, uses SOTA techniques to be surprisingly usable. |
| [Mistral-Large-3-675B-Instruct-2512-IQ2_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ2_S) | IQ2_S | 190.77GB | true | Low quality, uses SOTA techniques to be usable. |
| [Mistral-Large-3-675B-Instruct-2512-IQ2_XS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ2_XS) | IQ2_XS | 189.54GB | true | Low quality, uses SOTA techniques to be usable. |
| [Mistral-Large-3-675B-Instruct-2512-IQ2_XXS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ2_XXS) | IQ2_XXS | 165.15GB | true | Very low quality, uses SOTA techniques to be usable. |
| [Mistral-Large-3-675B-Instruct-2512-IQ1_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ1_M) | IQ1_M | 148.49GB | true | Extremely low quality, *not* recommended. |
| [Mistral-Large-3-675B-Instruct-2512-IQ1_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF/tree/main/mistralai_Mistral-Large-3-675B-Instruct-2512-IQ1_S) | IQ1_S | 142.27GB | true | Extremely low quality, *not* recommended. |

## Embed/output weights

Some of these quants (Q3_K_XL, Q4_K_L etc) are the standard quantization method with the embeddings and output weights quantized to Q8_0 instead of what they would normally default to.

## Downloading using huggingface-cli

<details>
  <summary>Click to view download instructions</summary>

First, make sure you have hugginface-cli installed:

```
pip install -U "huggingface_hub[cli]"
```

Then, you can target the specific file you want:

```
huggingface-cli download bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF --include "mistralai_Mistral-Large-3-675B-Instruct-2512-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/mistralai_Mistral-Large-3-675B-Instruct-2512-GGUF --include "mistralai_Mistral-Large-3-675B-Instruct-2512-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (mistralai_Mistral-Large-3-675B-Instruct-2512-Q8_0) or download them all in place (./)

</details>

## ARM/AVX information

Previously, you would download Q4_0_4_4/4_8/8_8, and these would have their weights interleaved in memory in order to improve performance on ARM and AVX machines by loading up more data in one pass.

Now, however, there is something called "online repacking" for weights. details in [this PR](https://github.com/ggml-org/llama.cpp/pull/9921). If you use Q4_0 and your hardware would benefit from repacking weights, it will do it automatically on the fly.

As of llama.cpp build [b4282](https://github.com/ggml-org/llama.cpp/releases/tag/b4282) you will not be able to run the Q4_0_X_X files and will instead need to use Q4_0.

Additionally, if you want to get slightly better quality for , you can use IQ4_NL thanks to [this PR](https://github.com/ggml-org/llama.cpp/pull/10541) which will also repack the weights for ARM, though only the 4_4 for now. The loading time may be slower but it will result in an overall speed incrase.

<details>
  <summary>Click to view Q4_0_X_X information (deprecated</summary>

I'm keeping this section to show the potential theoretical uplift in performance from using the Q4_0 with online repacking.

<details>
  <summary>Click to view benchmarks on an AVX2 system (EPYC7702)</summary>

| model                          |       size |     params | backend    | threads |          test |                  t/s |  % (vs Q4_0)  |
| ------------------------------ | ---------: | ---------: | ---------- | ------: | ------------: | -------------------: |-------------: |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         pp512 |        204.03 ± 1.03 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |        pp1024 |        282.92 ± 0.19 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |        pp2048 |        259.49 ± 0.44 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg128 |         39.12 ± 0.27 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg256 |         39.31 ± 0.69 |          100% |
| qwen2 3B Q4_0                  |   1.70 GiB |     3.09 B | CPU        |      64 |         tg512 |         40.52 ± 0.03 |          100% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         pp512 |        301.02 ± 1.74 |          147% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |        pp1024 |        287.23 ± 0.20 |          101% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |        pp2048 |        262.77 ± 1.81 |          101% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg128 |         18.80 ± 0.99 |           48% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg256 |         24.46 ± 3.04 |           83% |
| qwen2 3B Q4_K_M                |   1.79 GiB |     3.09 B | CPU        |      64 |         tg512 |         36.32 ± 3.59 |           90% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         pp512 |        271.71 ± 3.53 |          133% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |        pp1024 |       279.86 ± 45.63 |          100% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |        pp2048 |        320.77 ± 5.00 |          124% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg128 |         43.51 ± 0.05 |          111% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg256 |         43.35 ± 0.09 |          110% |
| qwen2 3B Q4_0_8_8              |   1.69 GiB |     3.09 B | CPU        |      64 |         tg512 |         42.60 ± 0.31 |          105% |

Q4_0_8_8 offers a nice bump to prompt processing and a small bump to text generation

</details>

</details>

## Which file should I choose?

<details>
  <summary>Click here for details</summary>

A great write up with charts showing various performances is provided by Artefact2 [here](https://gist.github.com/Artefact2/b5f810600771265fc1e39442288e8ec9)

The first thing to figure out is how big a model you can run. To do this, you'll need to figure out how much RAM and/or VRAM you have.

If you want your model running as FAST as possible, you'll want to fit the whole thing on your GPU's VRAM. Aim for a quant with a file size 1-2GB smaller than your GPU's total VRAM.

If you want the absolute maximum quality, add both your system RAM and your GPU's VRAM together, then similarly grab a quant with a file size 1-2GB Smaller than that total.

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

Thank you to LM Studio for sponsoring my work.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski