---
base_model: mistralai/Voxtral-Mini-4B-Realtime-2602
language:
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - it
  - nl
  - pt
  - zh
  - ja
  - ko
  - ru
library_name: mlx
license: apache-2.0
pipeline_tag: automatic-speech-recognition
tags:
  - mlx
  - mlx-audio
  - speech-to-text
  - streaming
  - realtime
  - voxtral
---

# Voxtral Mini 4B Realtime 4bit (bfloat16)

This is a **4-bit quantized, bfloat16-base** [MLX](https://github.com/ml-explore/mlx) conversion of [mistralai/Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602).

Compared to the older `mlx-community/Voxtral-Mini-4B-Realtime-2602-4bit` checkpoint, this one keeps the faster `mlx-audio` runtime layout: quantized `tok_embeddings`, plus `bfloat16` non-quantized weights and quantization scales.

In local `mlx-audio` streaming benchmarks on a few real audio samples, it ran about `3x` faster overall than the older `mlx-community` variant, with similar transcription output.

Runs via [mlx-audio](https://github.com/Blaizzy/mlx-audio).

## Which variant should you pick?

| Chip           | Recommended                                                                                                                              | Why                                                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **M3 / M4+**   | **This repo (`-4bit`, bf16)**                                                                                                            | bf16 has a native ALU on M3/M4; same speed as fp16 with a wider exponent range (safer numerics).                         |
| **M1 / M2**    | [`iris-sfg/Voxtral-Mini-4B-Realtime-2602-4bit-fp16`](https://huggingface.co/iris-sfg/Voxtral-Mini-4B-Realtime-2602-4bit-fp16)            | Metal on M1/M2 has no native bf16 ALU; bf16 ops fall back to a slower path. The fp16 variant stays on the fast GPU path. |

Only the non-quantized weights differ between the two repos (norms, biases, scales, some embeddings). The quantized mat-mul weights are bit-identical. Transcription output is byte-identical on a 20 s French clip at temperature 0 (verified locally).

## Conversion

Source model:

- `mistralai/Voxtral-Mini-4B-Realtime-2602`

Local conversion command:

```bash
python -m mlx_audio.convert \
  --hf-path mistralai/Voxtral-Mini-4B-Realtime-2602 \
  --mlx-path /path/to/Voxtral-Mini-4B-Realtime-2602-4bit \
  --quantize \
  --q-group-size 64 \
  --q-bits 4 \
  --model-domain stt
```

Quantization config:

- bits: `4`
- group size: `64`
- mode: `affine`

## Files

This repository intentionally contains only the MLX runtime artifacts needed for inference:

- `model.safetensors`
- `model.safetensors.index.json`
- `config.json`
- `generation_config.json`
- `params.json`
- `processor_config.json`
- `tekken.json`

## Usage

```bash
pip install "mlx-audio[stt]"
```

```python
from mlx_audio.stt.utils import load_model

model = load_model("path-or-hf-repo")
result = model.generate("audio.wav")
print(result.text)
```

## Notes

- Base model license remains Apache 2.0.
- Verify latency and decode behavior against your local benchmarks before publishing as a canonical variant.
