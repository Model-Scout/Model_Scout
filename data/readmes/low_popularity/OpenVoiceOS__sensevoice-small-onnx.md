---
license: other
license_name: funasr-model-license
license_link: https://github.com/modelscope/FunASR/blob/main/MODEL_LICENSE
base_model: FunAudioLLM/SenseVoiceSmall
base_model_relation: quantized
library_name: onnx
pipeline_tag: automatic-speech-recognition
tags:
  - onnx
  - onnx-asr
  - ctc
  - funasr
language:
  - zh
  - en
  - yue
  - ja
  - ko
---

# SenseVoiceSmall ONNX

ONNX export of [`FunAudioLLM/SenseVoiceSmall`](https://huggingface.co/FunAudioLLM/SenseVoiceSmall)
for [onnx-asr](https://github.com/istupakov/onnx-asr), model type `sensevoice`.

SenseVoiceSmall is a non-autoregressive speech model. One encoder pass and one CTC
greedy collapse give the transcript, so there is no decoder loop. It also reports the
spoken language, an emotion and an audio event.

Languages: Chinese, Cantonese, English, Japanese, Korean.

## Files

| File | Size | Notes |
| --- | --- | --- |
| `model.onnx` + `model.onnx_data` | 941 MB | fp32 |
| `model_int8.onnx` | 241 MB | dynamic int8, weights only (`MatMul` and `Gemm`) |
| `vocab.txt` | 25055 tokens | SentencePiece pieces, id 0 renamed to `<blk>` |
| `config.json` | | model type, prompt id tables |

## Usage

```python
import onnx_asr

model = onnx_asr.load_model("sensevoice", "OpenVoiceOS/sensevoice-small-onnx")
print(model.recognize("audio.wav"))

# language detection is automatic, or force one
print(model.recognize("audio.wav", language="zh"))
# inverse text normalization adds punctuation and digits
print(model.recognize("audio.wav", use_itn=True))
```

The detected language, emotion, audio event and text-normalization mode are the first
four entries of `result.tokens` when you call `recognize` with timestamps:

```python
result = model.recognize("audio.wav", timestamps=True)
print(result.tokens[:4])   # ['<|zh|>', '<|NEUTRAL|>', '<|Speech|>', '<|woitn|>']
print(result.text)         # rich tokens are not in the text
```

## Graph contract

| Input | Type | Shape | Meaning |
| --- | --- | --- | --- |
| `features` | f32 | `(B, T, 80)` | kaldi fbank, the onnx-asr `wespeaker` preprocessor |
| `features_lens` | i64 | `(B,)` | valid frames per item |
| `language` | i64 | `(B,)` | FunASR lid embedding index (`auto` 0, `zh` 3, `en` 4, `yue` 7, `ja` 11, `ko` 12) |
| `textnorm` | i64 | `(B,)` | 14 `withitn`, 15 `woitn` |

| Output | Type | Shape |
| --- | --- | --- |
| `logprobs` | f32 | `(B, ceil(T/6) + 4, 25055)` |
| `logprobs_lens` | i64 | `(B,)` |

The FunASR `WavFrontend` does three things: a kaldi fbank, a low frame rate stack
(`lfr_m` 7, `lfr_n` 6) and the `am.mvn` mean-variance statistics. Only the fbank stays
outside the graph, because onnx-asr already computes exactly that fbank for
`wespeaker` (hamming window, `snip_edges`, dither 0, preemphasis 0.97, 400/160/512,
80 mel bins, `log(max(x, eps))`). The LFR stack and the CMVN are folded into
`model.onnx`, together with the four prompt frames.

Batch padding is replaced in-graph by each item's last valid frame before the LFR
stack, which is what the FunASR right-padding does. Batched and single-clip results
are therefore identical.

The graph accepts any frame count `T` of 1 or more. The LFR stack pads the sequence up
to the next multiple of 6 with the last valid frame, and the pad width is clamped at
zero, so a frame count that already fills the last window needs no pad.

## License and attribution

The **weights are not Apache-2.0 and not an OSI-approved open-source license.** They
are a conversion of `FunAudioLLM/SenseVoiceSmall`, which is released by Alibaba Group
under the **FunASR Model Open Source License Agreement, version 1.1**
([text](https://github.com/modelscope/FunASR/blob/main/MODEL_LICENSE)). Read it before
you use this model. The terms that matter, as written:

* You may use, copy, modify and share the model.
* You **must attribute the source and author** and **retain the model names**. This
  repository keeps the name SenseVoice and credits Alibaba Group and the FunASR
  project, as required.
* The model is provided "for reference and learning purposes only". Alibaba Group
  accepts no responsibility for direct or indirect losses, and you carry all risk.
* Section 4.2 forfeits your license if you engage in "unjustified denigration,
  malicious smearing, or baseless insults" against the software. This is a
  conduct-based termination clause. No OSI-approved license has one, so this model
  cannot be called open source.
* Section 6 lets Alibaba Group revise the agreement at any time by publishing a new
  version, and continued use counts as acceptance.
* Section 7 names the governing law only as "[Country/Region]", an unfilled
  placeholder in the published text.

Nothing in this export changes those terms. Only the onnx-asr runtime code is
Apache-2.0; it lives in the onnx-asr repository, not here.

Model: Copyright (C) 2023-2028 Alibaba Group. All rights reserved.
Original model: <https://huggingface.co/FunAudioLLM/SenseVoiceSmall>
Project: <https://github.com/modelscope/FunASR>
