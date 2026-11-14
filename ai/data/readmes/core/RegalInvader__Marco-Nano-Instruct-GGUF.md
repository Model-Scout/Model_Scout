---
license: apache-2.0
base_model: ATH-MaaS/Marco-Nano-Instruct
base_model_relation: quantized
library_name: gguf
pipeline_tag: text-generation
language:
- en
- zh
- ar
- de
- es
- fr
- ko
- ja
- pt
- tr
- id
- it
- nl
- pl
- ru
- vi
- th
- he
- uk
- ms
- bn
- cs
- ur
- kk
- el
- ro
- hu
- ne
- az
tags:
- gguf
- llama.cpp
- pocketpal
- on-device
- moe
- multilingual
- quantization
- distillation
- 1-bit
- 2-bit
- 3-bit
---

# Marco-Nano-Instruct · 1-, 2- and 3-bit GGUF for phones

These are low-bit builds of [Marco-Nano-Instruct](https://huggingface.co/ATH-MaaS/Marco-Nano-Instruct), a
multilingual mixture-of-experts model with 8B parameters, 0.6B active per token, 232 experts and 29 languages.

The routed experts are 96% of the weights. Rather than simply rounding them, we **trained them in their low-bit formats** by distilling from the original
model. This keeps far more of the model than llama.cpp's own quantisations at the same size.

As only 0.6B parameters are active per token, the 3-bit file runs at **24.8 tokens/s on a Pixel 10a**. On the same
phone and settings, Google's Gemma 4 E2B QAT does 12.1 and Qwen3.5-4B does 5.2.

They run in stock llama.cpp and in [PocketPal](https://github.com/a-ghorbani/pocketpal-ai) 1.21.2 or later.

## Files

| File | Size | Experts | Training | KL to the original | Pixel 10a (tok/s) | Use it when |
|---|---|---|---|---|---|---|
| `Marco-Nano-Instruct-3bit-IQ3_S.gguf` | 4.02 GB | IQ3_S, down projection IQ4_NL | codebook scales, 24M tokens | 0.0277 | 24.8 | You want the best quality. It is within noise of the 8-bit original on every test |
| `Marco-Nano-Instruct-2bit-IQ2_S.gguf` | 3.46 GB | IQ2_S, down projection IQ4_NL | codebook scales, 50M tokens | 0.0566 | not timed | You want most of the 3-bit's quality in less memory (best 2-bit at code) |
| `Marco-Nano-Instruct-2bit-IQ2_XXS.gguf` | 3.14 GB | IQ2_XXS, down projection IQ4_NL | codebook scales, 44M tokens (the last 4M on checked maths and code) | 0.0914 | 31.6 | You want quality and speed together (best 2-bit at maths) |
| `Marco-Nano-Instruct-2bit-Q2_0.gguf` | 2.54 GB | Q2_0 | full quantisation-aware training, 200M tokens | 0.196 | 32.2 | Memory is tight |
| `Marco-Nano-Instruct-1bit-TQ1_0.gguf` | 2.18 GB | ternary TQ1_0 (1.69 bits per weight), down projection Q2_0 | full quantisation-aware training, 200M tokens (the last 10M on checked maths and code) | 0.243 | 36.6 | You want the smallest, fastest file and can give up maths and code |

- Every file keeps attention and the (tied) embeddings at Q8_0, the router and norms at f32, and the original chat
  template.
- We call the TQ1_0 file "1-bit" for short. It is ternary (each weight is −1, 0 or +1), stored at 1.69 bits per weight,
  and its down projections are 2-bit (Q2_0).
- **KL** is the KL divergence (nats per token) from the original bf16 model's next-token distribution, measured with
  llama.cpp's `--kl-divergence` on 40 held-out multilingual sequences of 4,096 tokens. Lower is closer. For scale, a
  Q8_0 of the original scores 0.0076.
- The Pixel 10a speeds are generation tokens/s from PocketPal's benchmark (512 prompt / 128 generated tokens, 4 CPU
  threads, f16 KV cache).
- **Update, 28 Oct:** the 1-bit file was replaced by one trained to 200M tokens, the last 10M on checked maths and
  code. Against the first upload it gains 6.8 points on GSM8K, 6.2 on MATH-500 and 8.5 on IFEval, and its KL fell from 0.264 to 0.243.
  However, it loses 3.2 points on Belebele, mostly in Hungarian (56.5 to 48.0).

## Running them

### PocketPal

The quickest start is the ready-made [Marco-Nano Pal](https://palshub.ai/pals/30cad63c-602a-44ba-8db0-0bb6cae0f124) on
PalsHub. It uses the 2-bit IQ2_XXS file and sets the temperature, top-p and repeat penalty from step 3. The CPU threads
(step 2) are an app setting, so you still need to set them yourself.

1. Download a file. You can add it from Hugging Face inside PocketPal by searching for this repository, or
   alternatively download it in a browser and add it to PocketPal as a local model.
2. **Set the CPU threads to the number of fast cores (4 on a Pixel).** PocketPal's default of 6 runs about half as fast
   on Tensor phones (the 2-bit IQ2_XXS does 31.6 tok/s at 4 threads and 16.8 at 6), because the extra threads end up waiting
   on the slow cores.
3. **Use temperature 0.7, top-p 0.9 and repeat penalty 1.1.**
   - We tested the 3-bit file, a 2-bit IQ2_XXS build and a 1-bit build on 72 prompts with the same seeds (Urdu,
     Turkish, Bengali and Nepali, other languages, and JSON).
   - At temperature 0.7, the repeat penalty cut looping replies from 9 to 2 (3-bit), 12 to 3 (2-bit) and 26 to 3
     (1-bit).
   - **Avoid low temperatures.** At temperature 0.3 without the penalty, 26 (3-bit), 27 (2-bit) and 45 (1-bit) of the 72
     replies looped.
   - Cap replies at about 1,024–1,536 tokens, as in some languages the model keeps going rather than stopping.
4. Keep the KV cache at f16 or Q8_0. Q8_0 halves the cache memory for almost no loss in quality. **Do not use a Q4_0 key
   cache, as it breaks the model.**
5. Keep conversations under about 8K tokens. The model was trained and tested up to 8K and quality drops beyond that.
6. **Optional: give it a system prompt so it knows its own name.** Without one it often says it is GPT-4o, like the
   original. With this one, 41 of 42 identity replies named Marco-Nano:
   `You are Marco-Nano, a small open-source AI assistant running locally on this device. You are Marco-Nano-Instruct, made
   by Alibaba International Digital Commerce, compressed to run on phones. Answer questions about who you are and who
   made you with this.`

### Ollama (tested on v0.40.12)

- The IQ3_S, IQ2_S, IQ2_XXS and Q2_0 files import and run. Ollama uses the chat template stored in the file, so a
  two-line Modelfile is all you need:

  ```
  FROM ./Marco-Nano-Instruct-3bit-IQ3_S.gguf
  PARAMETER repeat_penalty 1.1
  ```

  Then run `ollama create marco-3bit -f Modelfile` and `ollama run marco-3bit`.
- Pulling straight from this repo with `ollama run hf.co/RegalInvader/Marco-Nano-Instruct-GGUF:IQ3_S` (or `:IQ2_S`,
  `:IQ2_XXS`, `:Q2_0`) should also work, however we have not tested it.
- **The 1-bit TQ1_0 file does not load in Ollama** (it reports an unsupported tensor). Use llama.cpp or PocketPal
  for that one.

### llama.cpp

```bash
llama-cli -m Marco-Nano-Instruct-3bit-IQ3_S.gguf -c 8192 --jinja
llama-server -m Marco-Nano-Instruct-2bit-IQ2_XXS.gguf -c 8192 --jinja   # OpenAI-compatible server
```

**Compatibility.** We tested all five files with llama.cpp b11385, the version PocketPal 1.21.2 ships. The Q2_0 file
uses mainline llama.cpp's Q2_0 (groups of 64, 2.25 bits per weight). Some forks define a different, incompatible type
under the same Q2_0 name (for example with groups of 128), and such a fork may load this file and produce garbage
without an error. For the Q2_0 file, use mainline llama.cpp b11385 or newer. The IQ3_S, IQ2_S, IQ2_XXS and TQ1_0
formats are older and work in any recent mainline build.

## Speed

PocketPal 1.21.2 benchmark on a Pixel 10a (Tensor G4, 8 GB) with 4 CPU threads, f16 KV cache and 512/128:

| File | Size | Prompt (tok/s) | Generation (tok/s) |
|---|---|---|---|
| **3-bit IQ3_S (this repo)** | 4.02 GB | 56.7 | 24.8 |
| **2-bit IQ2_XXS (this repo)** | 3.14 GB | 83.4 | 31.6 |
| **2-bit Q2_0 (this repo)** | 2.54 GB | 86.4 | 32.2 |
| **1-bit TQ1_0 (this repo)** | 2.18 GB | 99.7 | 36.6 |
| Qwen3.5-4B Q4_K_M | 2.74 GB | 24.8 | 5.2 |
| Gemma 4 E2B QAT Q4_0 | 3.35 GB | 66.9 | 12.1 |
| Qwen3.5-2B Q4_K_M | 1.28 GB | 81.1 | 14.4 |
| Bonsai-4B Q1_0 | 0.57 GB | 34.6 | 9.9 |
| Qwen3-1.7B Q5_K_M | 1.47 GB | 53.1 | 12.1 |

On a 16-core desktop CPU (llama.cpp, `llama-bench -p 512 -n 128`) the 2-bit IQ2_XXS generates about 90 tokens/s and
reads prompts at about 1,000 tokens/s.

On an M1 MacBook Air (8 GB) with llama.cpp b12119 (`llama-bench -p 512 -n 128`, 3 runs each), on the GPU through Metal
and on the CPU with 4 threads:

| File | Metal prompt (tok/s) | Metal generation (tok/s) | CPU prompt (tok/s) | CPU generation (tok/s) |
|---|---|---|---|---|
| **3-bit IQ3_S** | 1023 | 72.1 | 270 | 65.8 |
| **2-bit IQ2_S** | 1045 | 71.3 | 293 | 68.1 |
| **2-bit IQ2_XXS** | 1041 | 74.2 | 322 | 73.1 |
| **2-bit Q2_0** | 1098 | 83.6 | 382 | 83.3 |
| **1-bit TQ1_0** | 424 | 40.1 | 275 | 88.8 |

On a Mac, run every file on the GPU apart from the 1-bit. llama.cpp's Metal support for TQ1_0 is slow, so set the GPU
layers to 0 for that file, where it generates at 88.8 tokens/s on the CPU.

## Quality

Every model below got the same questions through its own chat template, with thinking off and greedy decoding.
- **Multiple choice:** we start the reply with "The answer is" and limit the next token to the option letters.
- **GSM8K and MATH-500:** we check the final answer (MATH-500 with math-verify).
- **IFEval:** Google's checks.
- **Comparison models** use their publisher's GGUF at llama.cpp's default quantisation.
- **Noise:** with these sample sizes, differences under about 3 points (MMLU-Redux, Belebele), 2 points (MMLU-Pro,
  Global-MMLU-Lite), 4 points (GSM8K-250, MATH-500, IFEval) or 7 points (HumanEval+) are within noise (two standard
  errors).

**Knowledge, languages and maths:**
- MMLU-Redux: 1,000 questions.
- Global-MMLU-Lite: 400 each in Chinese, Arabic, Korean, Hungarian and Bengali.
- Belebele: 200 each in the same five languages.
- GSM8K: 250 questions.

| Model | File | MMLU-Redux | Global-MMLU-Lite (5) | Belebele (5) | GSM8K-250 |
|---|---|---|---|---|---|
| **3-bit IQ3_S (this repo)** | 4.02 GB | 61.9 | 51.3 | 72.8 | 87.2 |
| **2-bit IQ2_S (this repo)** | 3.46 GB | 60.9 | 48.7 | 67.0 | 84.4 |
| **2-bit IQ2_XXS (this repo)** | 3.14 GB | 60.1 | 48.0 | 66.5 | 90.4 |
| **2-bit Q2_0 (this repo)** | 2.54 GB | 55.2 | 44.2 | 58.0 | 68.4 |
| **1-bit TQ1_0 (this repo)** | 2.18 GB | 51.1 | 42.2 | 54.5 | 70.8 |
| Marco-Nano-Instruct Q8_0 (the original, 8-bit) | 8.53 GB | 62.4 | 52.8 | 73.0 | 87.2 |
| Qwen3.5-4B Q4_K_M | 2.74 GB | 77.4 | 61.5 | 83.3 | 96.0 |
| Ministral 3 3B Q4_K_M | 2.15 GB | 67.9 | 54.7 | 75.6 | 91.6 |
| Gemma 4 E2B QAT Q4_0 | 3.35 GB | 60.4 | 49.5 | 65.7 | 91.2 |
| Qwen3.5-2B Q4_K_M | 1.28 GB | 61.8 | 49.6 | 66.5 | 79.2 |
| LFM2.5-8B-A1B Q4_K_M | 5.16 GB | 60.1 | 41.6 | 49.0 | 86.4 |
| Bonsai-4B Q1_0 | 0.57 GB | 54.6 | 38.4 | 55.0 | 83.6 |
| Qwen3-1.7B Q5_K_M | 1.47 GB | 60.1 | 43.9 | 55.7 | 84.0 |

**Harder tests:**
- MMLU-Pro: 2,000 questions, direct answer.
- Global-MMLU: 1,000 each in German, Spanish, French, Japanese and Russian.
- MATH-500.
- IFEval: 541 prompts.

| Model | File | MMLU-Pro | Global-MMLU (5 more) | MATH-500 | IFEval (prompt) | IFEval (instr.) |
|---|---|---|---|---|---|---|
| **3-bit IQ3_S (this repo)** | 4.02 GB | 34.9 | 54.5 | 68.8 | 61.4 | 71.9 |
| **2-bit IQ2_S (this repo)** | 3.46 GB | 34.1 | 53.0 | 66.0 | 59.1 | 69.3 |
| **2-bit IQ2_XXS (this repo)** | 3.14 GB | 34.2 | 51.4 | 64.2 | 59.0 | 69.2 |
| **2-bit Q2_0 (this repo)** | 2.54 GB | 29.4 | 45.5 | 46.6 | 51.6 | 61.2 |
| **1-bit TQ1_0 (this repo)** | 2.18 GB | 27.7 | 42.8 | 39.4 | 52.9 | 63.7 |
| Marco-Nano-Instruct Q8_0 (the original, 8-bit) | 8.53 GB | 35.5 | 54.8 | 70.4 | 62.1 | 71.9 |
| Qwen3.5-4B Q4_K_M | 2.74 GB | 46.7 | 66.5 | 81.0 | 81.5 | 86.8 |
| Ministral 3 3B Q4_K_M | 2.15 GB | 38.1 | 57.2 | 67.2 | 50.3 | 63.7 |
| Gemma 4 E2B QAT Q4_0 | 3.35 GB | 28.6 | 48.4 | 67.2 | 77.8 | 84.7 |
| Qwen3.5-2B Q4_K_M | 1.28 GB | 30.6 | 48.3 | 63.8 | 66.5 | 75.3 |
| LFM2.5-8B-A1B Q4_K_M | 5.16 GB | 31.2 | 47.9 | 74.4 | 67.8 | 76.9 |
| Bonsai-4B Q1_0 | 0.57 GB | 29.0 | 44.3 | 54.0 | 71.3 | 80.2 |
| Qwen3-1.7B Q5_K_M | 1.47 GB | 26.8 | 48.0 | 73.8 | 64.1 | 73.6 |

**Code** (HumanEval+ and MBPP+, EvalPlus's tests run in a sandbox, pass@1):

| Model | File | HumanEval+ | MBPP+ |
|---|---|---|---|
| **3-bit IQ3_S (this repo)** | 4.02 GB | 63.2 | 48.5 |
| **2-bit IQ2_S (this repo)** | 3.46 GB | 62.0 | 43.0 |
| **2-bit IQ2_XXS (this repo)** | 3.14 GB | 52.1 | 38.7 |
| **2-bit Q2_0 (this repo)** | 2.54 GB | 32.5 | 23.3 |
| **1-bit TQ1_0 (this repo)** | 2.18 GB | 30.1 | 34.0 |
| Marco-Nano-Instruct Q8_0 (the original, 8-bit) | 8.53 GB | 61.3 | 49.9 |
| Qwen3.5-4B Q4_K_M | 2.74 GB | 75.5 | 60.7 |
| Ministral 3 3B Q4_K_M | 2.15 GB | 74.8 | 56.2 |
| Gemma 4 E2B QAT Q4_0 | 3.35 GB | 75.5 | 56.5 |
| Qwen3.5-2B Q4_K_M | 1.28 GB | 49.1 | 44.6 |
| LFM2.5-8B-A1B Q4_K_M | 5.16 GB | 63.8 | 58.1 |
| Bonsai-4B Q1_0 | 0.57 GB | 72.4 | 52.5 |
| Qwen3-1.7B Q5_K_M | 1.47 GB | 66.3 | 46.4 |

**What the tables show**
- **The 3-bit is within noise of the 8-bit original on every test here,** code included, at under half the size.
- **Languages are this model's main strength.** In Belebele and the five extra Global-MMLU languages, the 3-bit
  (72.8 and 54.5) is well ahead of Gemma 4 E2B (65.7, 48.4) and Qwen3.5-2B (66.5, 48.3). The IQ2 files are level with
  them on Belebele and Global-MMLU-Lite, and ahead on the five extra languages. The 3-bit and IQ2_XXS also generate
  1.7–2.6× faster on the phone.
- **Checked worked solutions help at 2 bits.** Finishing the IQ2_XXS file's training on verified maths answers took
  GSM8K from 84.4 to 90.4, above the original's 87.2. At 3 bits the same data changed nothing, which stands to reason
  as the 3-bit was already level with the original.
- **Instruction following and code are its weak spots,** and this is true of the original as well. Gemma 4 E2B,
  Qwen3.5-4B and even Bonsai-4B score higher on both IFEval and HumanEval+.
- **The 1-bit and Q2_0 files trade maths and code for size.** Their GSM8K, MATH-500 and HumanEval+ scores drop much
  more than their knowledge and language scores, so use the 3-bit or IQ2_S for maths and code.
  - Bonsai-4B (0.57 GB) beats the 1-bit at English, maths, code and instruction following.
  - The 1-bit's case is speed (36.6 tokens/s against Bonsai-4B's 9.9 on the same phone) and Global-MMLU-Lite in the
    five languages (42.2 against 38.4). On Belebele the two are level (54.5 against 55.0).
- **Ministral 3 3B is stronger than Marco itself at knowledge, languages and code.** However, it is a dense 3B model,
  so on a phone CPU it should generate several times slower than Marco's 0.6B active parameters. We did not time it
  on the Pixel.
- **Qwen3.5-4B is the strongest model here,** but it only manages 5.2 tokens/s on the Pixel, 4.8× slower than the
  3-bit.

Overall, the 3-bit gives the original model's quality at under half the size, and generates 1.7–2× faster than
Gemma 4 E2B and Qwen3.5-2B on the phone, whilst the smaller files trade maths and code for memory and speed.

## Against llama.cpp's own quantisations

Every file here had to beat llama.cpp's own quantisation of the original at about the same size or smaller (for Q2_0,
the closest llama.cpp file is 0.01 GB smaller), otherwise it
was not published. Same KL measurement as above:

| This repo | KL | llama.cpp's own file | Its size | Its KL |
|---|---|---|---|---|
| 3-bit IQ3_S, 4.02 GB | 0.0277 | IQ3_S experts, IQ4_NL down projection (imatrix) | 4.33 GB | 0.0353 |
| 2-bit IQ2_S, 3.46 GB | 0.0566 | IQ2_S experts, IQ4_NL down projection (imatrix) | 3.77 GB | 0.0963 |
| 2-bit IQ2_XXS, 3.14 GB | 0.0914 | IQ2_XXS experts, IQ4_NL down projection (imatrix) | 3.45 GB | 0.173 |
| 2-bit Q2_0, 2.54 GB | 0.196 | IQ1_M (imatrix), the closest size | 2.53 GB | 1.43 |
| 1-bit TQ1_0, 2.18 GB | 0.243 | nothing that small (the smallest is IQ1_S) | 2.41 GB | 1.55 |

## How they were made

**3-bit and 2-bit IQ files (codebook training).** These are the IQ3_S, IQ2_S and IQ2_XXS files.
- We start from llama.cpp's own imatrix quantisation of the original in the same format.
- We keep its codes (which grid point each group of weights uses).
- We train the block scales by distillation, minimising the KL divergence from the original's next-token distribution
  over 24–50M tokens of multilingual text and the original's own answers. The learning rate stays constant and then
  decays over the last 4–10M tokens.
- Then attention and the embeddings get converted to Q8_0.
- Training cut the KL of llama.cpp's own file by 22% (IQ3_S), 41% (IQ2_S) and 47% (IQ2_XXS).

**1-bit and Q2_0 files (quantisation-aware training).**
- The expert weights were trained on the target grid, starting from round-to-nearest, by distilling from the original.
  The loss is forward KL to its next-token distribution plus 0.1 × cross-entropy, with the cross-entropy switched off
  on the original's answers that a verifier marked wrong.
- Optimiser: AdamW with 8-bit states, a constant learning rate and a decay over the last 5%.
- The router and the embeddings were frozen.
- 200M tokens each. The 1-bit's last 10M tokens came from the checked maths and code set described below.

**Training data:**
- Multilingual web text: FineWeb-2, FineWeb2-HQ, FineWeb-Edu, Fineweb-Edu-Chinese.
- Maths and code: FineMath, MegaMath.
- Human chat: Aya, OpenAssistant.
- The original model's own answers to prompts from Aya, NVIDIA's Nemotron RL sets, DAPO-Math and the GSM8K and MATH
  train splits, most of them translated into the 28 non-English languages.

English is about a third of the tokens. Everything was decontaminated against the evaluation sets.

**The 2-bit IQ2_XXS file's last 4M tokens** came from a second set of the original's answers, each one checked:
- Maths against reference answers (NuminaMath-1.5, DeepMath).
- Code against tests in a sandbox (TACO and MBPP, with MBPP+ benchmark tasks excluded by id).
- Plus instruction-following, knowledge, reasoning and multilingual prompts (Tulu 3, NVIDIA Nemotron, HelpSteer,
  Reasoning Gym, Aya).

That took its GSM8K score from 84.4 to 90.4 compared with the same file trained on the first data, at a KL cost of
0.0008.

**How KL improves with training tokens.** The chart and fits below come from the training curves of the codebook
formats, measured before attention and the embeddings were converted to Q8_0, so the shipped files in the Files table
are about 0.001 higher. The shipped IQ2_XXS is a separate run (40M tokens, then 4M on the checked data). The fits are
KL(N) = floor + a·N^(−b), with N in millions of tokens:

![KL against training tokens for each format, with llama.cpp's own file as the dashed line](kl_vs_tokens.png)

| Format | llama.cpp's start | Floor | KL at 20M / 50M / 100M (fit) |
|---|---|---|---|
| IQ2_XXS | 0.173 | 0.078 | 0.098 / 0.089 / 0.085 |
| IQ2_S | 0.096 | 0.051 | 0.060 / 0.056 / 0.054 |
| IQ3_S | 0.035 | — | best at 24M (20M, then a 4M decay): 0.0265, then no further gain |

Across formats the floor comes out at about 0.22 × (llama.cpp's KL)^0.62. A format whose llama.cpp KL is already
below about 0.019 (IQ4_XS) gains nothing.

**Compute:** the 1-bit and Q2_0 files were each trained on a single GX10 (NVIDIA GB10). The codebook files only need
a few GPU-hours each.

**Code:** the codebook and quantiser code (GGUF reading and writing, bit-exact with llama.cpp) and the benchmark and
evaluation scripts are in this repo's `code/` folder (Apache-2.0). The training code is not published.

## Limitations

- **Context:** stick to 8K tokens or less. Quality falls off past ~8K, in these files and in the original.
- **No thinking mode:** like the original instruct model, these files answer directly.
- **Maths at 1 and 2 bits:** the 1-bit and Q2_0 files lose a lot more on maths than on knowledge or languages.
- **Hungarian and Bengali** lose the most of the five tested languages at 2 bits.
- **iPhones and iPads:** untested. Macs are covered in Speed (M1, Metal and CPU).
- **It may say it is GPT-4o.** Asked who it is, the original Marco-Nano-Instruct usually says OpenAI made it (27 of 42
  replies in our check), and these files inherit that. It is Marco-Nano-Instruct from Alibaba International Digital
  Commerce. The system prompt in PocketPal step 6 fixes most of it.

## Licence and credits

- **Licence:** Apache-2.0, same as the original. These are modified weights of
  [ATH-MaaS/Marco-Nano-Instruct](https://huggingface.co/ATH-MaaS/Marco-Nano-Instruct). The expert weights were
  retrained in low-bit formats and the other weights requantised. All credit for the model itself goes to its authors.
- **Built with** [llama.cpp](https://github.com/ggml-org/llama.cpp) for the GGUF formats and the KL measurement, and
  the datasets above under their own licences.

## Support

These were trained on one person's spare hardware and a few dollars of rented GPU time. If they are useful to you,
you can support more of this work (GPU time, testing on more phones) here:

[![Support on Ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/regalinvader)

PocketPal benchmark results from your own phone (Benchmark tab, 512/128) are just as welcome. Open a discussion on this
repo with the device name and the numbers.
