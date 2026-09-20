---
quantized_by: bartowski
pipeline_tag: text-generation
language:
- en
- zh
- ko
- fr
- es
- ru
- ja
- de
- it
- pt
- pl
- id
- nl
- vi
tags:
- nvidia
- llama3.3
license_name: nvidia-open-model-license
datasets:
- nvidia/HelpSteer3
base_model: nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual
base_model_relation: quantized
license: other
inference: false
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
fine-tuning: false
---

## Llamacpp imatrix Quantizations of Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual by nvidia

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b5856">b5856</a> for quantization.

Original model: https://huggingface.co/nvidia/Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

Run them directly with [llama.cpp](https://github.com/ggerganov/llama.cpp), or any other llama.cpp based project

## Prompt format

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

detailed thinking on<|eot_id|><|start_header_id|>user<|end_header_id|>


You are a skilled little expert at scoring responses. You should evaluate given responses based on the given judging criteria.
Given the context of the conversation (the last turn is the User’s query) and one or two responses from the Assistant, you need to refer to the [Helpfulness Scoring Guidelines] to score each individual response.
If there are two responses, you need to also give a ranking score based on the [Ranking Scoring Guidelines].
Before scoring, please analyze step by step. Your scoring needs to be as strict as possible.

[Helpfulness Scoring Guidelines]

When evaluating Helpfulness, consider the following factors:

- Correctness/Completeness: Is the response accurate and complete?
- Coherence/Clarity: Is the response clear, coherent, and easy to understand?
- Instruction following: Does the response follow the instructions and fulfill the user's request?
- Relevance: Is the response relevant to the user's query/input?
- Level of Detail and Creativity: Does the response provide enough detail without being too verbose? Does it show creativity but not hallucinations?

**Score 5: Extremely Helpful**

- The response is extremely helpful and completely aligned with the spirit of what the prompt was asking for.
- It accurately acts on the user's request, without unnecessary information.
- If a user request is not possible/in line with desired model behavior, a helpful response provides useful context and rationale.

**Score 4: Mostly Helpful**

- The response is mostly helpful and mainly aligned with what the user was looking for.
- There is still some room for improvement, but the response is generally useful.

**Score 3: Partially Helpful**

- The response is partially helpful but misses the overall goal of the user's query/input in some way.
- The response did not fully satisfy what the user was looking for.

**Score 2: Borderline Unhelpful**

- The response is borderline unhelpful and mostly does not capture what the user was looking for.
- However, it is still usable and helpful in a small way.

**Score 1: Not Helpful**

- The response is not useful or helpful at all.
- The response completely missed the essence of what the user wanted.

[Ranking Scoring Guidelines]

Ranking score is used to rank the two responses based on their helpfulness. Even if you give the same individual helpfulness score for both responses, you need to differentiate them strictly.
The ranking score is a number between 1 and 6, where:
1 = Response 1 is much better than Response 2
2 = Response 1 is better than Response 2
3 = Response 1 is slightly better than Response 2
4 = Response 2 is slightly better than Response 1
5 = Response 2 is better than Response 1
6 = Response 2 is much better than Response 1

#### Conversation Context ####
User: {prompt}
Assistant: 

#### Responses to be Scored ####
#### Output Format Requirements ####
First give your analysis on each responses in the format of:
[The Begin of Analysis on Response i]
Analysis on the i-th response
[The End of Analysis on Response i]

Then give the scores of each response in order, separate by comma in the boxed, adhering this format:
[The Begin of Individual Scores]
\boxed{x, y} if there exists 2 responses
[The End of Individual Scores]

If there are two responses, give the relative ranking score in the format of:
[The Begin of Ranking Score]
\boxed{z} 
[The End of Ranking Score]
You don't need to give a ranking score if only one response is provided.<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-bf16.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/tree/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-bf16) | bf16 | 99.74GB | true | Full BF16 weights. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q8_0.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/tree/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q8_0) | Q8_0 | 52.99GB | true | Extremely high quality, generally unneeded but max available quant. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q6_K.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q6_K.gguf) | Q6_K | 40.92GB | false | Very high quality, near perfect, *recommended*. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q5_K_M.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q5_K_M.gguf) | Q5_K_M | 35.39GB | false | High quality, *recommended*. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q5_K_S.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q5_K_S.gguf) | Q5_K_S | 34.43GB | false | High quality, *recommended*. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_1.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_1.gguf) | Q4_1 | 31.38GB | false | Legacy format, similar performance to Q4_K_S but with improved tokens/watt on Apple silicon. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_K_L.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_K_L.gguf) | Q4_K_L | 31.00GB | false | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_K_M.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_K_M.gguf) | Q4_K_M | 30.22GB | false | Good quality, default size for most use cases, *recommended*. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_K_S.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_K_S.gguf) | Q4_K_S | 28.63GB | false | Slightly lower quality with more space savings, *recommended*. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_0.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_0.gguf) | Q4_0 | 28.46GB | false | Legacy format, offers online repacking for ARM and AVX CPU inference. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ4_NL.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ4_NL.gguf) | IQ4_NL | 28.38GB | false | Similar to IQ4_XS, but slightly larger. Offers online repacking for ARM CPU inference. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q3_K_XL.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q3_K_XL.gguf) | Q3_K_XL | 27.19GB | false | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ4_XS.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ4_XS.gguf) | IQ4_XS | 26.87GB | false | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q3_K_L.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q3_K_L.gguf) | Q3_K_L | 26.27GB | false | Lower quality but usable, good for low RAM availability. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q3_K_M.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q3_K_M.gguf) | Q3_K_M | 24.31GB | false | Low quality. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ3_M.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ3_M.gguf) | IQ3_M | 22.66GB | false | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q3_K_S.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q3_K_S.gguf) | Q3_K_S | 21.96GB | false | Low quality, not recommended. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ3_XS.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ3_XS.gguf) | IQ3_XS | 20.91GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q2_K_L.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q2_K_L.gguf) | Q2_K_L | 19.77GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ3_XXS.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ3_XXS.gguf) | IQ3_XXS | 19.52GB | false | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q2_K.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q2_K.gguf) | Q2_K | 18.74GB | false | Very low quality but surprisingly usable. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ2_M.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ2_M.gguf) | IQ2_M | 17.16GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ2_S.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ2_S.gguf) | IQ2_S | 15.85GB | false | Low quality, uses SOTA techniques to be usable. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ2_XS.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ2_XS.gguf) | IQ2_XS | 15.08GB | false | Low quality, uses SOTA techniques to be usable. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ2_XXS.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ2_XXS.gguf) | IQ2_XXS | 13.66GB | false | Very low quality, uses SOTA techniques to be usable. |
| [Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ1_M.gguf](https://huggingface.co/bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF/blob/main/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-IQ1_M.gguf) | IQ1_M | 12.02GB | false | Extremely low quality, *not* recommended. |

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
huggingface-cli download bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF --include "nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-GGUF --include "nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (nvidia_Llama-3_3-Nemotron-Super-49B-GenRM-Multilingual-Q8_0) or download them all in place (./)

</details>

## ARM/AVX information

Previously, you would download Q4_0_4_4/4_8/8_8, and these would have their weights interleaved in memory in order to improve performance on ARM and AVX machines by loading up more data in one pass.

Now, however, there is something called "online repacking" for weights. details in [this PR](https://github.com/ggerganov/llama.cpp/pull/9921). If you use Q4_0 and your hardware would benefit from repacking weights, it will do it automatically on the fly.

As of llama.cpp build [b4282](https://github.com/ggerganov/llama.cpp/releases/tag/b4282) you will not be able to run the Q4_0_X_X files and will instead need to use Q4_0.

Additionally, if you want to get slightly better quality for , you can use IQ4_NL thanks to [this PR](https://github.com/ggerganov/llama.cpp/pull/10541) which will also repack the weights for ARM, though only the 4_4 for now. The loading time may be slower but it will result in an overall speed incrase.

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

[llama.cpp feature matrix](https://github.com/ggerganov/llama.cpp/wiki/Feature-matrix)

But basically, if you're aiming for below Q4, and you're running cuBLAS (Nvidia) or rocBLAS (AMD), you should look towards the I-quants. These are in format IQX_X, like IQ3_M. These are newer and offer better performance for their size.

These I-quants can also be used on CPU, but will be slower than their K-quant equivalent, so speed vs performance is a tradeoff you'll have to decide.

</details>

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset.

Thank you ZeroWw for the inspiration to experiment with embed/output.

Thank you to LM Studio for sponsoring my work.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
