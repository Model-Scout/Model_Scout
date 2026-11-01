---
license: other
license_name: nvidia-open-model-license
license_link: https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
library_name: mlx-audio
pipeline_tag: automatic-speech-recognition
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
language:
  - en
  - es
  - de
  - fr
  - it
  - ar
  - ja
  - ko
  - pt
  - ru
  - hi
  - zh
  - vi
  - he
  - nl
  - cs
  - da
  - pl
  - 'no'
  - sv
  - th
  - tr
  - bg
  - el
  - et
  - fi
  - hr
  - hu
  - lt
  - lv
  - ro
  - sk
  - uk
  - mt
  - sl
tags:
  - mlx
  - mlx-audio
  - speech-to-text
  - asr
  - stt
  - transcription
  - streaming
  - fastconformer
  - rnnt
---

# mlx-community/nemotron-3.5-asr-streaming-0.6b-8bit

MLX conversion of [`nvidia/nemotron-3.5-asr-streaming-0.6b`](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) — NVIDIA's 600M-parameter
**cache-aware streaming FastConformer-RNNT** ASR with **language-ID prompt conditioning**,
covering 40 language-locales with punctuation and capitalization.

**This repo:** weights are **8-bit** quantized Linear/Embedding weights (group size 64); convolution and norm layers stay in bfloat16. Transcription quality matches the bf16 model at ~40% smaller size.

See the [original model card](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) for architecture, benchmarks, and intended use.

## Install

This model needs `mlx-audio` with Nemotron ASR support. It's merged into `main` but not in a
PyPI release yet (latest is 0.4.3), so for now install from GitHub:

```bash
pip install "git+https://github.com/Blaizzy/mlx-audio.git"
```

(Once the next release ships, `pip install -U mlx-audio` will work.)

## Use

```python
from mlx_audio.stt import load

model = load("mlx-community/nemotron-3.5-asr-streaming-0.6b-8bit")

# auto language detection (default)
print(model.generate("speech.wav").text)

# force a language via its prompt key (en-US, es-ES, zh-CN, fr-FR, ...)
print(model.generate("speech.wav", language="en-US").text)
```

CLI:

```bash
python -m mlx_audio.stt.generate --model mlx-community/nemotron-3.5-asr-streaming-0.6b-8bit --audio speech.wav --format txt
```

`generate(..., att_context_size=[left, right])` selects a trained look-ahead
(`[56,3]`, `[56,0]`, `[56,6]`, `[56,13]`); the default `[56,13]` gives the best offline accuracy.

## Available MLX formats

| Repo | Notes |
|------|-------|
| [`mlx-community/nemotron-3.5-asr-streaming-0.6b`](https://huggingface.co/mlx-community/nemotron-3.5-asr-streaming-0.6b) | full quality (bf16) |
| [`mlx-community/nemotron-3.5-asr-streaming-0.6b-8bit`](https://huggingface.co/mlx-community/nemotron-3.5-asr-streaming-0.6b-8bit) | 8-bit, matches bf16 |

## License & attribution

Original model © NVIDIA Corporation, released under the
[NVIDIA Open Model License](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). This is a format conversion of those weights;
the same license and terms apply. MLX conversion by
[@ARahim3](https://github.com/ARahim3) via [mlx-audio](https://github.com/ARahim3/mlx-audio).
