---
license: apache-2.0
base_model: mistralai/Voxtral-Mini-4B-Realtime-2602
base_model_relation: quantized
pipeline_tag: automatic-speech-recognition
library_name: mlx-audio
tags:
  - mlx
  - mlx-audio
  - voxtral
  - streaming
  - realtime
  - speech-recognition
language:
  - en
  - fr
  - es
  - de
  - ru
  - zh
  - ja
  - it
  - pt
  - nl
  - ar
  - hi
  - ko
---

# Voxtral-Mini-4B-Realtime-2602 — MLX 8-bit

8-bit MLX quantization of [mistralai/Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602),
Mistral's streaming speech-to-text model, for Apple Silicon with [mlx-audio](https://github.com/Blaizzy/mlx-audio).

**Why this conversion:** on a 64 GB M5 Pro, the fp16 MLX weights cannot keep up with live speech (0.47× real time), so a
streamed transcript falls further and further behind. This 8-bit version keeps up and matches fp16 accuracy on real
French voices (numbers below). A lighter [6-bit version](https://huggingface.co/flo5k5/Voxtral-Mini-4B-Realtime-2602-MLX-6bit)
keeps up too, with slightly lower accuracy at long transcription delays.

It is in the mlx-audio format (`model_type: voxtral_realtime`). As of October 2026 no 8-bit
version existed in mlx-community.

## Conversion

From [mlx-community/Voxtral-Mini-4B-Realtime-2602-fp16](https://huggingface.co/mlx-community/Voxtral-Mini-4B-Realtime-2602-fp16),
with mlx-audio at commit [`94c7716`](https://github.com/Blaizzy/mlx-audio/commit/94c7716212b2228f178d2f9c7619a591fd1b0b78)
(0.5.7) and MLX 0.32.3:

```bash
python -m mlx_audio.convert \
  --hf-path mlx-community/Voxtral-Mini-4B-Realtime-2602-fp16 \
  --mlx-path Voxtral-Mini-4B-Realtime-2602-MLX-8bit \
  -q --q-bits 8
```

Affine quantization, 8 bits, group size 64. Size: 4.6 GB in memory (fp16: 8.9 GB).

## Measurements

Apple M5 Pro, 64 GB. 120-clip sample of the Common Voice 17 French test set (120 speakers, 12 min, clips with ≥ 2 up-votes
and no down-vote), word error rate on lower-cased text without punctuation.

**Streaming**, served by [oMLX](https://github.com/jundot/omlx) over its realtime WebSocket
(`/v1/audio/transcriptions/realtime`, 480 ms transcription delay), audio sent at speaking pace in 80 ms packets:

| | fp16 | 6-bit | **8-bit** |
|---|---|---|---|
| First text after audio starts (median, 40 clips) | 5.4 s | 1.8 s | **1.8 s** |
| Final text after speech ends (median) | 8.8 s | 0.27 s | **0.32 s** |
| Lag of the text behind the voice, 79 s stream (median / p90) | 130 s / 161 s | 0.12 s / 2.6 s | **0.02 s / 2.2 s** |
| WER of the streamed text (mean per clip) | 9.7 % | 8.6 % | **8.8 %** |

**Accuracy by transcription delay** (mlx-audio streaming session, 40 clips):

| Delay | 240 ms | 480 ms | 960 ms | 2400 ms |
|---|---|---|---|---|
| fp16 WER | 10.4 % | 9.2 % | 6.3 % | 6.0 % |
| 6-bit WER | 10.6 % | 8.5 % | 6.8 % | 6.8 % |
| **8-bit WER** | **10.4 %** | **8.7 %** | **6.3 %** | **6.3 %** |

The sample is small (40 clips for streaming), so differences of about one point are within noise. The lag of the long
stream is estimated assuming a steady speaking rate: at time t, with c of the C final characters received, the text covers
about c/C of the speech duration. Only French was measured; the conversion does not touch the other languages, but they
were not checked.

## Usage

mlx-audio:

```python
from mlx_audio.stt.utils import load_model

model = load_model("flo5k5/Voxtral-Mini-4B-Realtime-2602-MLX-8bit")
print(model.generate("speech.wav", language="fr").text)

# streaming
session = model.create_streaming_session(transcription_delay_ms=480)
session.feed(samples_16khz_float32)   # call repeatedly as audio arrives
for delta in session.step(max_decode_tokens=8):
    print(delta, end="")
```

oMLX: place the folder in your model directory; it is discovered as an `audio_stt` model and served on
`/v1/audio/transcriptions` and on the realtime WebSocket `/v1/audio/transcriptions/realtime`.

## License

Apache 2.0, as the original model. All credit for the model goes to [Mistral AI](https://huggingface.co/mistralai);
this repository only changes the numeric precision of the weights.
