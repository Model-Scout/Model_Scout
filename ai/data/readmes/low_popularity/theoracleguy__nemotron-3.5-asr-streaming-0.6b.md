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
- "no"
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
- openvox
- apple-silicon
---

# theoracleguy/nemotron-3.5-asr-streaming-0.6b

MLX-compatible version of [`nvidia/nemotron-3.5-asr-streaming-0.6b`](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b), prepared for use with **OpenVox** and other Apple Silicon workflows using [`mlx-audio`](https://github.com/Blaizzy/mlx-audio).

Nemotron 3.5 ASR Streaming is NVIDIA's 600M-parameter **cache-aware streaming FastConformer-RNNT** speech recognition model with **language-ID prompt conditioning**.

It supports 40 language-locales along with punctuation and capitalization.

**This repository contains bfloat16 weights for full-quality inference.**

For architecture details, benchmarks, training information, limitations, and intended use, see the [original NVIDIA model card](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b).

## OpenVox

This model is distributed through the [`theoracleguy`](https://huggingface.co/theoracleguy) Hugging Face repository for use with **OpenVox**, a local AI voice platform for Mac, iPad, and Windows.

OpenVox is designed around local AI processing, allowing supported speech and voice workflows to run directly on your device.

This repository can also be used independently with `mlx-audio`.

## Install

This model requires `mlx-audio` with Nemotron ASR support.

If your installed PyPI version does not yet include Nemotron support, install the latest version directly from GitHub:

```bash
pip install -U "git+https://github.com/Blaizzy/mlx-audio.git"