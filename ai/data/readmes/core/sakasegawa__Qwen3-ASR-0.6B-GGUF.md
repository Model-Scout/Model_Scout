---
license: apache-2.0
base_model:
  - Qwen/Qwen3-ASR-0.6B
base_model_relation: quantized
pipeline_tag: automatic-speech-recognition
language:
  - ar
  - cs
  - da
  - de
  - el
  - en
  - es
  - fa
  - fi
  - fil
  - fr
  - hi
  - hu
  - id
  - it
  - ja
  - ko
  - mk
  - ms
  - nl
  - pl
  - pt
  - ro
  - ru
  - sv
  - th
  - tr
  - vi
  - yue
  - zh
tags:
  - gguf
  - ggml
  - speech.cpp
  - qwen3-asr
---

# Qwen3-ASR-0.6B GGUF for speech.cpp

These files run only in [speech.cpp](https://github.com/nyosegawa/speech.cpp) 0.7.0 or later, and the Q6_K, Q5_K and Q4_K files in 0.8.0 or later. Their layout is speech.cpp's own, so llama.cpp, LM Studio, Ollama and other programs that read GGUF cannot run them.

It holds Qwen's [Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B) in one file. It writes the text of speech in 30 languages, finds the language itself, and can be told the names and terms the audio holds.

## Use

Install speech.cpp ([install](https://github.com/nyosegawa/speech.cpp#install)), then:

```sh
speech asr qwen3-asr-0.6b utterance.wav
speech asr qwen3-asr-0.6b:q4_k --language ja utterance.wav
speech serve qwen3-asr-0.6b --open
```

`qwen3-asr-0.6b` is the name speech.cpp gives this model; `speech` fetches the Q8_0 file from this repository the first time, and `qwen3-asr-0.6b:q4_k` or another type of the table below fetches that type instead. A path to a downloaded file works as well. The options, the worker and the HTTP API are in speech.cpp's documentation: [Qwen3-ASR](https://github.com/nyosegawa/speech.cpp/blob/main/docs/models/qwen3-asr.md), [command line](https://github.com/nyosegawa/speech.cpp/blob/main/docs/cli.md) and [server](https://github.com/nyosegawa/speech.cpp/blob/main/docs/server.md).

## Files

| File | Contents | Size | speech.cpp from | SHA-256 |
|---|---|---|---|---|
| `Qwen3-ASR-0.6B-Q8_0.gguf` (the file the name fetches) | the frontend, the encoder, the projector, the decoder and the tokenizer; the matrices and the token embeddings in Q8_0 | 0.84 GB (841,502,336 bytes) | 0.7.0 | `416e10c15b4a3d9002bd337d18fc450233fdf68502b6e10d1379d2789838afd0` |
| `Qwen3-ASR-0.6B-Q6_K.gguf` | the frontend, the encoder, the projector, the decoder and the tokenizer; the matrices and the token embeddings in Q6_K | 0.68 GB (681,496,704 bytes) | 0.8.0 | `8bd6c92f19ef50e65b1f489d2427bc611d122eaf967ccc7f1b7e8f8996112a79` |
| `Qwen3-ASR-0.6B-Q5_K.gguf` | the frontend, the encoder, the projector, the decoder and the tokenizer; the matrices and the token embeddings in Q5_K | 0.59 GB (593,751,680 bytes) | 0.8.0 | `bb75c2612468e1940753a605ab81655d2a139e1a926a9ca721e7f3079787ca90` |
| `Qwen3-ASR-0.6B-Q4_K.gguf` | the frontend, the encoder, the projector, the decoder and the tokenizer; the matrices and the token embeddings in Q4_K | 0.51 GB (511,168,128 bytes) | 0.8.0 | `981c7842de271f53684ff83362c4c9a2d84394d4d7acadabddaa1d3a7b51c0fa` |
| `Qwen3-ASR-0.6B-Q8_0.gguf.json` | the output of `speech info --json` for the Q8_0 file | 909 bytes | | `3175ead67ea73cc66576b533cab81b553b4609e690bb6f1a5cc226103a103ac6` |
| `Qwen3-ASR-0.6B-Q6_K.gguf.json` | the output of `speech info --json` for the Q6_K file | 909 bytes | | `2ff8d859af8c03ace500181a63dadc386630c4aacd148d5431cae6ff1a13a88f` |
| `Qwen3-ASR-0.6B-Q5_K.gguf.json` | the output of `speech info --json` for the Q5_K file | 909 bytes | | `602bfaba28f78a1d08488fa7d12d32bb3fbb096f4a434205832f974d49f127dd` |
| `Qwen3-ASR-0.6B-Q4_K.gguf.json` | the output of `speech info --json` for the Q4_K file | 909 bytes | | `23ea4edb8a2a3dc970bddbc1e5219aae87d3151f7f57a1f35c8bb5c2083273bf` |

In the Q6_K, Q5_K and Q4_K files the encoder's and the projector's matrices, whose rows of 896 values are not whole blocks of 256, are Q8_0. A request needs the GGUF file alone; the JSON file lets a program show the model or choose a file without downloading it.

## Languages

The model recognizes 30 languages, and 22 Chinese dialects under `zh` or `auto`. A request may force one, which then steers the model, or leave it to the model.

| Code | Language | Code | Language | Code | Language |
|---|---|---|---|---|---|
| `ar` | Arabic | `fr` | French | `pl` | Polish |
| `cs` | Czech | `hi` | Hindi | `pt` | Portuguese |
| `da` | Danish | `hu` | Hungarian | `ro` | Romanian |
| `de` | German | `id` | Indonesian | `ru` | Russian |
| `el` | Greek | `it` | Italian | `sv` | Swedish |
| `en` | English | `ja` | Japanese | `th` | Thai |
| `es` | Spanish | `ko` | Korean | `tr` | Turkish |
| `fa` | Persian | `mk` | Macedonian | `vi` | Vietnamese |
| `fi` | Finnish | `ms` | Malay | `yue` | Cantonese |
| `fil` | Filipino | `nl` | Dutch | `zh` | Chinese |

## Accuracy

Every stage is checked against transformers' tensors on 10 inputs from FLEURS' test split (ja_jp, en_us, cmn_hans_cn
and de_de, and two near-silent cuts), each with four requests, on an Apple M5:

| Weights | Text from the audio, 0.6B and 1.7B |
|---|---|
| F32 on the CPU, F32 or F16 on Metal | the official text on all 80 requests |
| Q8_0 on the CPU | the official text on 37 and 35 of 40 |
| Q8_0 on Metal | the official text on 37 and 40 of 40 |

Where a Q8_0 text differs, the official choice between two tokens was within the arithmetic's error of a tie.

Each type, measured by speech-bench on 2026-10-12 on an Apple M5 with Metal, on the 4,483 utterances of Common Voice 8.0's Japanese test set, trimmed to the voice. The memory is the peak memory footprint of `speech` for one request.

| Type | Size | Memory | CER | CER, other spellings accepted |
|---|---|---|---|---|
| Q8_0 | 0.84 GB | 1.00 GB | 11.89% | 7.05% |
| Q6_K | 0.68 GB | 0.84 GB | 12.01% | 7.02% |
| Q5_K | 0.59 GB | 0.75 GB | 12.49% | 7.57% |
| Q4_K | 0.51 GB | 0.67 GB | 14.23% | 8.66% |

## Speed

speech-bench on 2026-10-08: Common Voice 8.0's Japanese test set, Q8_0, one utterance at a time, the language left to the model.

| Device | Median | p90 |
|---|---|---|
| Apple M5, Metal | 0.132 s | 0.231 s |
| RTX 2080, Vulkan | 0.087 s | 0.158 s |

## Source

Converted by speech.cpp's `reference/qwen3-asr/convert.py Qwen3-ASR-0.6B`, whose environment pins transformers 5.18.0 and qwen-asr 0.0.6, from [Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B) at `5eb144179a02acc5e5ba31e748d22b0cf3e303b0`, to F32, from which `speech quantize --type <type>` wrote each file. Every constant the C++ reads is in the file, from the checkpoint or, where it has none, from the official code.

The 1.7B model, which is more accurate, is `qwen3-asr-1.7b` in [sakasegawa/Qwen3-ASR-1.7B-GGUF](https://huggingface.co/sakasegawa/Qwen3-ASR-1.7B-GGUF).

## License

The weights are the Qwen team's, under the Apache License 2.0, as the official checkpoint is. See [Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B) for the model and its terms. These files change the format of the weights and quantize them; they do not retrain them.
