---
license: apache-2.0
base_model:
  - Qwen/Qwen3-ASR-1.7B
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

# Qwen3-ASR-1.7B GGUF for speech.cpp

These files run only in [speech.cpp](https://github.com/nyosegawa/speech.cpp) 0.7.0 or later, and the Q6_K, Q5_K and Q4_K files in 0.8.0 or later. Their layout is speech.cpp's own, so llama.cpp, LM Studio, Ollama and other programs that read GGUF cannot run them.

It holds Qwen's [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) in one file. It writes the text of speech in 30 languages, finds the language itself, and can be told the names and terms the audio holds.

## Use

Install speech.cpp ([install](https://github.com/nyosegawa/speech.cpp#install)), then:

```sh
speech asr qwen3-asr-1.7b utterance.wav
speech asr qwen3-asr-1.7b:q4_k --language ja utterance.wav
speech serve qwen3-asr-1.7b --open
```

`qwen3-asr-1.7b` is the name speech.cpp gives this model; `speech` fetches the Q8_0 file from this repository the first time, and `qwen3-asr-1.7b:q4_k` or another type of the table below fetches that type instead. A path to a downloaded file works as well. The options, the worker and the HTTP API are in speech.cpp's documentation: [Qwen3-ASR](https://github.com/nyosegawa/speech.cpp/blob/main/docs/models/qwen3-asr.md), [command line](https://github.com/nyosegawa/speech.cpp/blob/main/docs/cli.md) and [server](https://github.com/nyosegawa/speech.cpp/blob/main/docs/server.md).

## Files

| File | Contents | Size | speech.cpp from | SHA-256 |
|---|---|---|---|---|
| `Qwen3-ASR-1.7B-Q8_0.gguf` (the file the name fetches) | the frontend, the encoder, the projector, the decoder and the tokenizer; the matrices and the token embeddings in Q8_0 | 2.18 GB (2,176,109,216 bytes) | 0.7.0 | `5f219b78a1d9c3b9e97da27708b36f8a0bc1bfc1650b541c0a6dbaf87c9a62d0` |
| `Qwen3-ASR-1.7B-Q6_K.gguf` | the frontend, the encoder, the projector, the decoder and the tokenizer; the matrices and the token embeddings in Q6_K | 1.68 GB (1,683,632,800 bytes) | 0.8.0 | `2a05df6866d3e033ca3ca2bc8f9573abf57b431328e85ccc40eb367e93bdc987` |
| `Qwen3-ASR-1.7B-Q5_K.gguf` | the frontend, the encoder, the projector, the decoder and the tokenizer; the matrices and the token embeddings in Q5_K | 1.41 GB (1,413,565,088 bytes) | 0.8.0 | `985f7cdf65cbbb578a4b5eeef52e4c08725bb212dbaba26dc759e50c61e70e40` |
| `Qwen3-ASR-1.7B-Q4_K.gguf` | the frontend, the encoder, the projector, the decoder and the tokenizer; the matrices and the token embeddings in Q4_K | 1.16 GB (1,159,383,712 bytes) | 0.8.0 | `38f6f0ca89e51c4adee8313016a580b297f42753829b93fce7e820668bf4c8b7` |
| `Qwen3-ASR-1.7B-Q8_0.gguf.json` | the output of `speech info --json` for the Q8_0 file | 911 bytes | | `8ae9d64dfa7f1f3e6a102210c67e33a49b0597c3ac753d796d0fff1e7e83d683` |
| `Qwen3-ASR-1.7B-Q6_K.gguf.json` | the output of `speech info --json` for the Q6_K file | 911 bytes | | `339287bf510a6df5b4e727a11a209cc978a69c074666c6424b67e80958b64db3` |
| `Qwen3-ASR-1.7B-Q5_K.gguf.json` | the output of `speech info --json` for the Q5_K file | 911 bytes | | `9517cd2522a136114cf70e4c176f63397df95af8b01b720d988615c0ab9d2118` |
| `Qwen3-ASR-1.7B-Q4_K.gguf.json` | the output of `speech info --json` for the Q4_K file | 911 bytes | | `ff5b21f1b4027c62c6fc184dc3a0bfb1f357f0e506b7c5c4bc28af375c787c6b` |

A request needs the GGUF file alone; the JSON file lets a program show the model or choose a file without downloading it.

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
| Q8_0 | 2.18 GB | 2.34 GB | 9.49% | 4.67% |
| Q6_K | 1.68 GB | 1.85 GB | 9.52% | 4.72% |
| Q5_K | 1.41 GB | 1.58 GB | 9.85% | 4.96% |
| Q4_K | 1.16 GB | 1.32 GB | 11.21% | 5.96% |

## Speed

speech-bench on 2026-10-08: Common Voice 8.0's Japanese test set, Q8_0, one utterance at a time, the language left to the model.

| Device | Median | p90 |
|---|---|---|
| Apple M5, Metal | 0.309 s | 0.544 s |
| RTX 2080, Vulkan | 0.155 s | 0.286 s |

## Source

Converted by speech.cpp's `reference/qwen3-asr/convert.py Qwen3-ASR-1.7B`, whose environment pins transformers 5.18.0 and qwen-asr 0.0.6, from [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) at `7278e1e70fe206f11671096ffdd38061171dd6e5`, to F32, from which `speech quantize --type <type>` wrote each file. Every constant the C++ reads is in the file, from the checkpoint or, where it has none, from the official code.

The 0.6B model, which is faster and takes less memory, is `qwen3-asr-0.6b` in [sakasegawa/Qwen3-ASR-0.6B-GGUF](https://huggingface.co/sakasegawa/Qwen3-ASR-0.6B-GGUF).

## License

The weights are the Qwen team's, under the Apache License 2.0, as the official checkpoint is. See [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) for the model and its terms. These files change the format of the weights and quantize them; they do not retrain them.
