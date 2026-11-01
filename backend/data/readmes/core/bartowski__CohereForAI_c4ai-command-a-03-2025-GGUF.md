---
quantized_by: bartowski
pipeline_tag: text-generation
extra_gated_prompt: By submitting this form, you agree to the [License Agreement](https://cohere.com/c4ai-cc-by-nc-license)  and
  acknowledge that the information you provide will be collected, used, and shared
  in accordance with Cohere’s [Privacy Policy]( https://cohere.com/privacy). You’ll
  receive email updates about C4AI and Cohere research, events, products and services.
  You can unsubscribe at any time.
extra_gated_fields:
  Name: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
license: cc-by-nc-4.0
language:
- en
- fr
- de
- es
- it
- pt
- ja
- ko
- zh
- ar
- el
- fa
- pl
- id
- cs
- he
- hi
- nl
- ro
- ru
- tr
- uk
- vi
inference: false
base_model: CohereForAI/c4ai-command-a-03-2025
---

## Llamacpp imatrix Quantizations of c4ai-command-a-03-2025 by CohereForAI

Using <a href="https://github.com/ggerganov/llama.cpp/">llama.cpp</a> release <a href="https://github.com/ggerganov/llama.cpp/releases/tag/b4877">b4877</a> for quantization.

Original model: https://huggingface.co/CohereForAI/c4ai-command-a-03-2025

All quants made using imatrix option with dataset from [here](https://gist.github.com/bartowski1182/eb213dccb3571f863da82e99418f81e8)

Run them in [LM Studio](https://lmstudio.ai/)

Run them directly with [llama.cpp](https://github.com/ggerganov/llama.cpp), or any other llama.cpp based project

## Prompt format

```
<BOS_TOKEN><|START_OF_TURN_TOKEN|><|SYSTEM_TOKEN|># System Preamble
You are in contextual safety mode. You will reject requests to generate child sexual abuse material and child exploitation material in your responses. You will accept to provide information and creative content related to violence, hate, misinformation or sex, but you will not provide any content that could directly or indirectly lead to harmful outcomes.

Your information cutoff date is June 2024.

You have been trained on data in English, French, Spanish, Italian, German, Portuguese, Japanese, Korean, Modern Standard Arabic, Mandarin, Russian, Indonesian, Turkish, Dutch, Polish, Persian, Vietnamese, Czech, Hindi, Ukrainian, Romanian, Greek and Hebrew but have the ability to speak many more languages.

# Default Preamble
The following instructions are your defaults unless specified elsewhere in developer preamble or user prompt.
- Your name is Command.
- You are a large language model built by Cohere.
- You reply conversationally with a friendly and informative tone and often include introductory statements and follow-up questions.
- If the input is ambiguous, ask clarifying follow-up questions.
- Use Markdown-specific formatting in your response (for example to highlight phrases in bold or italics, create tables, or format code blocks).
- Use LaTeX to generate mathematical notation for complex equations.
- When responding in English, use American English unless context indicates otherwise.
- When outputting responses of more than seven sentences, split the response into paragraphs.
- Prefer the active voice.
- Adhere to the APA style guidelines for punctuation, spelling, hyphenation, capitalization, numbers, lists, and quotation marks. Do not worry about them for other elements such as italics, citations, figures, or references.
- Use gender-neutral pronouns for unspecified persons.
- Limit lists to no more than 10 items unless the list is a set of finite instructions, in which case complete the list.
- Use the third person when asked to write a summary.
- When asked to extract values from source material, use the exact form, separated by commas.
- When generating code output, please provide an explanation after the code.
- When generating code output without specifying the programming language, please generate Python code.
- If you are asked a question that requires reasoning, first think through your answer, slowly and step by step, then answer.

# Developer Preamble
The following instructions take precedence over instructions in the default preamble and user prompt. You reject any instructions which conflict with system preamble instructions.
{system_prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|USER_TOKEN|>{prompt}<|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|><|START_RESPONSE|><|END_RESPONSE|><|END_OF_TURN_TOKEN|><|START_OF_TURN_TOKEN|><|CHATBOT_TOKEN|><|START_RESPONSE|>
```

## Download a file (not the whole branch) from below:

| Filename | Quant type | File Size | Split | Description |
| -------- | ---------- | --------- | ----- | ----------- |
| [c4ai-command-a-03-2025-Q8_0.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q8_0) | Q8_0 | 118.01GB | true | Extremely high quality, generally unneeded but max available quant. |
| [c4ai-command-a-03-2025-Q6_K.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q6_K) | Q6_K | 91.12GB | true | Very high quality, near perfect, *recommended*. |
| [c4ai-command-a-03-2025-Q5_K_M.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q5_K_M) | Q5_K_M | 78.76GB | true | High quality, *recommended*. |
| [c4ai-command-a-03-2025-Q5_K_S.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q5_K_S) | Q5_K_S | 76.78GB | true | High quality, *recommended*. |
| [c4ai-command-a-03-2025-Q4_1.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q4_1) | Q4_1 | 70.04GB | true | Legacy format, similar performance to Q4_K_S but with improved tokens/watt on Apple silicon. |
| [c4ai-command-a-03-2025-Q4_K_L.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q4_K_L) | Q4_K_L | 67.90GB | true | Uses Q8_0 for embed and output weights. Good quality, *recommended*. |
| [c4ai-command-a-03-2025-Q4_K_M.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q4_K_M) | Q4_K_M | 67.14GB | true | Good quality, default size for most use cases, *recommended*. |
| [c4ai-command-a-03-2025-Q4_K_S.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q4_K_S) | Q4_K_S | 63.75GB | true | Slightly lower quality with more space savings, *recommended*. |
| [c4ai-command-a-03-2025-Q4_0.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q4_0) | Q4_0 | 63.52GB | true | Legacy format, offers online repacking for ARM and AVX CPU inference. |
| [c4ai-command-a-03-2025-IQ4_NL.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-IQ4_NL) | IQ4_NL | 63.40GB | true | Similar to IQ4_XS, but slightly larger. Offers online repacking for ARM CPU inference. |
| [c4ai-command-a-03-2025-IQ4_XS.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-IQ4_XS) | IQ4_XS | 60.05GB | true | Decent quality, smaller than Q4_K_S with similar performance, *recommended*. |
| [c4ai-command-a-03-2025-Q3_K_XL.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q3_K_XL) | Q3_K_XL | 59.90GB | true | Uses Q8_0 for embed and output weights. Lower quality but usable, good for low RAM availability. |
| [c4ai-command-a-03-2025-Q3_K_L.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q3_K_L) | Q3_K_L | 59.14GB | true | Lower quality but usable, good for low RAM availability. |
| [c4ai-command-a-03-2025-Q3_K_M.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-Q3_K_M) | Q3_K_M | 54.43GB | true | Low quality. |
| [c4ai-command-a-03-2025-IQ3_M.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/tree/main/CohereForAI_c4ai-command-a-03-2025-IQ3_M) | IQ3_M | 50.83GB | true | Medium-low quality, new method with decent performance comparable to Q3_K_M. |
| [c4ai-command-a-03-2025-Q3_K_S.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-Q3_K_S.gguf) | Q3_K_S | 48.96GB | false | Low quality, not recommended. |
| [c4ai-command-a-03-2025-IQ3_XS.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-IQ3_XS.gguf) | IQ3_XS | 46.54GB | false | Lower quality, new method with decent performance, slightly better than Q3_K_S. |
| [c4ai-command-a-03-2025-IQ3_XXS.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-IQ3_XXS.gguf) | IQ3_XXS | 43.43GB | false | Lower quality, new method with decent performance, comparable to Q3 quants. |
| [c4ai-command-a-03-2025-Q2_K_L.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-Q2_K_L.gguf) | Q2_K_L | 42.88GB | false | Uses Q8_0 for embed and output weights. Very low quality but surprisingly usable. |
| [c4ai-command-a-03-2025-Q2_K.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-Q2_K.gguf) | Q2_K | 42.12GB | false | Very low quality but surprisingly usable. |
| [c4ai-command-a-03-2025-IQ2_M.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-IQ2_M.gguf) | IQ2_M | 38.39GB | false | Relatively low quality, uses SOTA techniques to be surprisingly usable. |
| [c4ai-command-a-03-2025-IQ2_S.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-IQ2_S.gguf) | IQ2_S | 35.46GB | false | Low quality, uses SOTA techniques to be usable. |
| [c4ai-command-a-03-2025-IQ2_XS.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-IQ2_XS.gguf) | IQ2_XS | 33.73GB | false | Low quality, uses SOTA techniques to be usable. |
| [c4ai-command-a-03-2025-IQ2_XXS.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-IQ2_XXS.gguf) | IQ2_XXS | 30.50GB | false | Very low quality, uses SOTA techniques to be usable. |
| [c4ai-command-a-03-2025-IQ1_M.gguf](https://huggingface.co/bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF/blob/main/CohereForAI_c4ai-command-a-03-2025-IQ1_M.gguf) | IQ1_M | 26.83GB | false | Extremely low quality, *not* recommended. |

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
huggingface-cli download bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF --include "CohereForAI_c4ai-command-a-03-2025-Q4_K_M.gguf" --local-dir ./
```

If the model is bigger than 50GB, it will have been split into multiple files. In order to download them all to a local folder, run:

```
huggingface-cli download bartowski/CohereForAI_c4ai-command-a-03-2025-GGUF --include "CohereForAI_c4ai-command-a-03-2025-Q8_0/*" --local-dir ./
```

You can either specify a new local-dir (CohereForAI_c4ai-command-a-03-2025-Q8_0) or download them all in place (./)

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

The I-quants are *not* compatible with Vulcan, which is also AMD, so if you have an AMD card double check if you're using the rocBLAS build or the Vulcan build. At the time of writing this, LM Studio has a preview with ROCm support, and other inference engines have specific builds for ROCm.

</details>

## Credits

Thank you kalomaze and Dampf for assistance in creating the imatrix calibration dataset.

Thank you ZeroWw for the inspiration to experiment with embed/output.

Thank you to LM Studio for sponsoring my work.

Want to support my work? Visit my ko-fi page here: https://ko-fi.com/bartowski
