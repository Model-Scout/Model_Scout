---
quantized_by: bartowski
pipeline_tag: image-text-to-text
base_model: mistralai/Mistral-Small-4-119B-2603
license: apache-2.0
language:
- ar
- en
- fr
- es
- de
- it
- pt
- nl
- ja
- ko
- zh
tags:
- vLLM
base_model_relation: quantized
---

## Llamacpp imatrix Quantizations of Mistral-Small-4-119B-2603 by mistralai

Using <a href="https://github.com/ggml-org/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggml-org/llama.cpp/releases/tag/b8388">b8388</a> for quantization.

Original model: https://huggingface.co/mistralai/Mistral-Small-4-119B-2603

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/82ae9b520227f57d79ba04add13d0d0d)

Run them in your choice of tools:

- [llama.cpp](https://github.com/ggml-org/llama.cpp)
- [LM Studio](https://lmstudio.ai/)
- [koboldcpp](https://github.com/LostRuins/koboldcpp)
- [Jan AI](https://www.jan.ai/)
- [Text Generation Web UI](https://github.com/oobabooga/text-generation-webui)
- [LoLLMs](https://github.com/ParisNeo/lollms)

Note: if it's a newly supported model, you may need to wait for an update from the developers.

## What's new:

Re-uploaded `Q4_1` with fixes, something about Mistral 4 does not work with later layers of `FFN_DOWN_EXPS` being `Q4_1` (results in nan while doing PPL and broken generation)

Because of that, `Q4_1` will not be going back up unless I can find what's fundamentally broken about `Q4_1` on later layers

## Prompt format

```
<s>[SYSTEM_PROMPT]{system_prompt}[/SYSTEM_PROMPT][MODEL_SETTINGS]{"reasoning_effort": "none"}[/MODEL_SETTINGS][INST]{prompt}[/INST]
```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Mean KLD | 99.9% KLD | Mean Δp | Same Top P | Description |
| -------- | ---------- | --------- | ----- | -------: | --------: | ------: | ---------: | ----------- |
| [Mistral-Small-4-119B-2603-Q8_0.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q8_0) | Q8_0 | 126.47GB | true | — | — | — | — | Extremely high quality, generally unneeded but max available quant. |
| [Mistral-Small-4-119B-2603-Q6_K_L.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q6_K_L) | Q6_K_L | 103.07GB | true | 0.0496 | 1.5382 | -0.028% | 91.48% | Uses Q8_0 for embed and output weights. Very high quality, near perfect, *recommended*. |
| [Mistral-Small-4-119B-2603-Q6_K.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q6_K) | Q6_K | 102.81GB | true | 0.0526 | 1.4584 | -0.046% | 91.03% | Very high quality, near perfect, *recommended*. |
| [Mistral-Small-4-119B-2603-Q5_K_L.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q5_K_L) | Q5_K_L | 85.37GB | true | 0.0590 | 1.6532 | -0.077% | 90.62% | Uses Q8_0 for embed and output weights. High quality, *recommended*. |
| [Mistral-Small-4-119B-2603-Q5_K_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q5_K_M) | Q5_K_M | 85.04GB | true | 0.0644 | 1.7651 | -0.104% | 90.09% | High quality, *recommended*. |
| [Mistral-Small-4-119B-2603-Q5_K_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q5_K_S) | Q5_K_S | 82.22GB | true | 0.0747 | 1.8440 | -0.197% | 89.32% | High quality, *recommended*. |
| [Mistral-Small-4-119B-2603-Q4_K_L.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q4_K_L) | Q4_K_L | 73.04GB | true | 0.0862 | 2.1930 | -0.238% | 88.55% | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [Mistral-Small-4-119B-2603-Q4_K_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q4_K_M) | Q4_K_M | 72.64GB | true | 0.0943 | 2.3572 | -0.284% | 88.10% | Good quality, default size for most use cases, *recommended*. |
| [Mistral-Small-4-119B-2603-Q4_K_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q4_K_S) | Q4_K_S | 69.88GB | true | 0.1111 | 2.5516 | -0.454% | 86.99% | Slightly lower quality with more space savings, *recommended*. |
| [Mistral-Small-4-119B-2603-Q4_0.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q4_0) | Q4_0 | 67.71GB | true | 0.1579 | 3.3253 | -0.916% | 84.65% | *Re-uploaded fixed* Legacy format, offers online repacking for ARM and AVX CPU inference. |
| [Mistral-Small-4-119B-2603-IQ4_NL.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-IQ4_NL) | IQ4_NL | 67.46GB | true | 0.1292 | 2.8837 | -0.538% | 86.18% | Similar to IQ4_XS, but slightly larger. Offers online repacking for ARM CPU inference. |
| [Mistral-Small-4-119B-2603-IQ4_XS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-IQ4_XS) | IQ4_XS | 63.79GB | true | 0.1326 | 2.8648 | -0.502% | 85.92% | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Mistral-Small-4-119B-2603-Q3_K_XL.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q3_K_XL) | Q3_K_XL | 57.37GB | true | 0.1891 | 3.8506 | -1.241% | 83.33% | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [Mistral-Small-4-119B-2603-IQ3_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-IQ3_M) | IQ3_M | 56.96GB | true | 0.1923 | 3.8533 | -1.253% | 83.14% | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [Mistral-Small-4-119B-2603-Q3_K_L.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q3_K_L) | Q3_K_L | 56.90GB | true | 0.1970 | 4.0469 | -1.193% | 83.00% | Lower quality but usable, good for low RAM availability. |
| [Mistral-Small-4-119B-2603-Q3_K_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q3_K_M) | Q3_K_M | 54.56GB | true | 0.1781 | 3.6817 | -1.021% | 83.72% | Low quality. |
| [Mistral-Small-4-119B-2603-Q3_K_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-Q3_K_S) | Q3_K_S | 52.00GB | true | 0.1884 | 3.7636 | -1.058% | 83.29% | Low quality, not recommended. |
| [Mistral-Small-4-119B-2603-IQ3_XS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/tree/main/mistralai_Mistral-Small-4-119B-2603-IQ3_XS) | IQ3_XS | 51.75GB | true | 0.2102 | 3.9446 | -1.403% | 82.44% | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [Mistral-Small-4-119B-2603-IQ3_XXS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-IQ3_XXS.gguf) | IQ3_XXS | 49.87GB | false | 0.2253 | 4.1906 | -1.588% | 81.79% | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [Mistral-Small-4-119B-2603-Q2_K_L.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-Q2_K_L.gguf) | Q2_K_L | 42.59GB | false | 0.3009 | 5.3592 | -2.548% | 79.08% | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [Mistral-Small-4-119B-2603-Q2_K.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-Q2_K.gguf) | Q2_K | 42.07GB | false | 0.3165 | 5.4220 | -2.654% | 78.60% | Very low quality but surprisingly usable. |
| [Mistral-Small-4-119B-2603-IQ2_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-IQ2_M.gguf) | IQ2_M | 41.63GB | false | 0.4121 | 6.3932 | -3.666% | 75.61% | Relatively low quality, uses SOTA techniques to be surprisingly usable. |
| [Mistral-Small-4-119B-2603-IQ2_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-IQ2_S.gguf) | IQ2_S | 38.14GB | false | 0.5322 | 7.3299 | -4.936% | 72.47% | Low quality, uses SOTA techniques to be usable. |
| [Mistral-Small-4-119B-2603-IQ2_XS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-IQ2_XS.gguf) | IQ2_XS | 37.02GB | false | 0.5337 | 7.6213 | -5.340% | 72.23% | Low quality, uses SOTA techniques to be usable. |
| [Mistral-Small-4-119B-2603-IQ2_XXS.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-IQ2_XXS.gguf) | IQ2_XXS | 33.66GB | false | 0.6182 | 8.3521 | -6.642% | 70.12% | Very low quality, uses SOTA techniques to be usable. |
| [Mistral-Small-4-119B-2603-IQ1_M.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-IQ1_M.gguf) | IQ1_M | 29.53GB | false | 0.9290 | 10.3507 | -10.592% | 63.55% | Extremely low quality, *not* recommended. |
| [Mistral-Small-4-119B-2603-IQ1_S.gguf](https://huggingface.co/bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF/blob/main/mistralai_Mistral-Small-4-119B-2603-IQ1_S.gguf) | IQ1_S | 26.88GB | false | 1.0729 | 11.1168 | -13.094% | 60.74% | Extremely low quality, *not* recommended. |


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
huggingface-cli download bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF --include "mistralai_Mistral-Small-4-119B-2603-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/mistralai_Mistral-Small-4-119B-2603-GGUF --include "mistralai_Mistral-Small-4-119B-2603-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (mistralai_Mistral-Small-4-119B-2603-Q8_0) or download them all in place (./)

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
