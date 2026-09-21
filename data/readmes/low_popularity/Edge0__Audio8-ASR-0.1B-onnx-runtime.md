---
tags:
- automatic-speech-recognition
- audio
- asr
- onnx
- onnxruntime
- quantized
- int8
- int4
- english
- chinese
- cantonese
- french
- japanese
- german
- korean
language:
- en
- zh
- yue
- fr
- ja
- de
- ko
library_name: onnx
pipeline_tag: automatic-speech-recognition
license: cc-by-nc-4.0
repository: https://github.com/AutoArk/open-audio-opd
---

<div align="center">

# Audio8-ASR-0.1B ONNX Runtime

[![GitHub](https://img.shields.io/badge/GitHub-AutoArk%2Fopen--audio--opd-blue?logo=github)](https://github.com/AutoArk/open-audio-opd)
[![arXiv](https://img.shields.io/badge/arXiv-2605.28139-b31b1b?logo=arxiv)](https://arxiv.org/abs/2605.28139)
[![License](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)

</div>

Audio8-ASR-0.1B ONNX Runtime is a self-contained local inference package for
multilingual automatic speech recognition. It includes ONNX Runtime inference code,
a browser UI, a local HTTP API, tokenizer/config files, and decoder/audio-head
precision variants.

The model is a multilingual ASR model with support for English, Chinese,
Cantonese, French, Japanese, German, and Korean.

This repository does not require the original training repository or a separate
source checkpoint at runtime. Everything needed for CPU ONNX inference is in
`model_bundle/`.

This repository is intended to be used through the included ONNX Runtime code.
It is not a Transformers `AutoModel` source release.

The root `config.json` is included for Hugging Face Hub metadata and download
accounting. Runtime graph metadata is stored in `model_bundle/metadata.json`.

## Related Repositories

- [Audio8-ASR-0.1B](https://huggingface.co/AutoArk-AI/Audio8-ASR-0.1B): main model repository.
- [Audio8-ASR-0.1B-iOS-ANE](https://huggingface.co/AutoArk-AI/Audio8-ASR-0.1B-iOS-ANE): iPhone-ready, out-of-the-box ASR demo and Swift SDK. The demo is designed to keep runtime memory footprint around 200 MB on device.
- [AutoArk/open-audio-opd](https://github.com/AutoArk/open-audio-opd): shared GitHub project for Audio8 public releases.

## Contents

- `model_bundle/`: tokenizer, feature extractor config, ONNX graphs, and numpy weights.
- `asr_onnx_runtime.py`: ONNX Runtime ASR engine.
- `server.py`: FastAPI local web/API server.
- `static/`: browser UI with file upload, microphone recording, precision switching, hotwords, and memory panels.
- `transcribe_file.py`: single-file CLI and minimal Python helper.
- `hotword/`: optional decode-time hotword trie boosting helper.
- `run_local.sh`: local WebUI launch helper.
- `smoke_test.sh`: health + ASR API smoke test for a user-provided audio file.
- `measure_precision_memory.py`: optional fresh-process RSS measurement helper.

## Included ONNX Variants

Decoder cache graphs:

- `fp32`: `lm_cache_prefill.onnx`, `lm_cache_decode.onnx`
- `int8`: `lm_cache_prefill_int8.onnx`, `lm_cache_decode_int8.onnx`
- `int4`: `lm_cache_prefill_int4.onnx`, `lm_cache_decode_int4.onnx`

Audio tower graphs:

- `fp32`: `audio_hidden.onnx`
- `int8`: `audio_hidden_int8.onnx`

The default runtime path is decoder `int8` plus audio tower `int8`. Decoder
`int4` is included for lower peak memory, while decoder `fp32` is included as a
full-precision reference path.

## Install

Use Python 3.10+. Python 3.12 is recommended.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements-onnx.txt
```

With `uv`:

```bash
uv venv --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements-onnx.txt
source .venv/bin/activate
```

With conda:

```bash
conda create -n audio8-asr-onnx python=3.12
conda activate audio8-asr-onnx
python3 -m pip install -r requirements-onnx.txt
```

## Run WebUI

```bash
./run_local.sh
```

Open:

```text
http://127.0.0.1:7860
```

If the port is busy:

```bash
PORT=7870 ./run_local.sh
```

## Command Line

Transcribe one local audio file without starting the WebUI:

```bash
python3 transcribe_file.py /path/to/audio.wav --max_new_tokens 128
```

Print the full result JSON:

```bash
python3 transcribe_file.py /path/to/audio.wav --json
```

Force a precision combination:

```bash
python3 transcribe_file.py /path/to/audio.wav \
  --cache_precision int8 \
  --audio_precision int8
```

Enable optional hotword biasing:

```bash
python3 transcribe_file.py /path/to/audio.wav \
  --hotwords "term_one,term_two" \
  --json
```

## Use From Python

```python
from pathlib import Path

from asr_onnx_runtime import OnnxCacheAsrEngine


engine = OnnxCacheAsrEngine(
    "model_bundle",
    cache_precision="int8",
    audio_precision="int8",
)
result = engine.transcribe(
    Path("/path/to/audio.wav").read_bytes(),
    language=None,
    max_new_tokens=128,
    hotwords=None,
)
print(result["text"])
```

The lower-level `OnnxAsrEngine` class is available for the full-context
fallback graph. Prefer `OnnxCacheAsrEngine` for normal local inference.

## HTTP API

Start the server with `./run_local.sh`, then call `POST /asr` with multipart
form data:

```bash
curl --noproxy "*" -fsS -X POST http://127.0.0.1:7860/asr \
  -F "audio=@/path/to/audio.wav" \
  -F "max_new_tokens=128" \
  -F "cache_precision=int8" \
  -F "audio_precision=int8" \
  | python3 -m json.tool
```

Form fields:

- `audio`: required audio file. WAV is recommended; `librosa`/`soundfile` handle common formats.
- `language`: optional compatibility field. The current ONNX runtime ignores
  this value and lets the model infer the spoken language from audio.
- `max_new_tokens`: optional generation cap; default is `128`.
- `cache_precision`: optional decoder precision, one of `fp32`, `int8`, `int4`, `auto`.
- `audio_precision`: optional audio tower precision, one of `fp32`, `int8`, `auto`.
- `hotwords`: optional comma-separated hotwords. Omit or leave empty to disable.
- `hotword_topk`: optional top-k gate for applying boosts; default is `50`.
- `hotword_start_boost`: optional first-token boost; default is `6.0`.
- `hotword_continuation_boost`: optional continuation-token boost; default is `8.0`.

Useful endpoints:

- `GET /health`: readiness and selected runtime.
- `GET /api/runtime`: selected graphs, provider, and available precision variants.
- `POST /api/reload`: switch backend/precision without restarting the process.
- `GET /metrics`: process/system memory metrics plus runtime info.

Important response fields:

- `text`: normalized transcript for application use.
- `raw`: raw decoded model text before normalization.
- `elapsed_seconds`: inference time inside the runtime.
- `audio_seconds`: decoded audio duration after loading/resampling.
- `generated_tokens`, `hit_stop`, `stop_token_id`: generation diagnostics.
- `backend`, `cache_precision`, `audio_precision`, `providers`: selected runtime path.
- `request_peak_rss_bytes`: latest request RSS high-water mark.
- `hotword`: hotword tokenization/boost metadata when hotwords are enabled, otherwise `null`.

## Hotwords

Hotwords are an opt-in decode-time feature. They do not change model weights,
ONNX graphs, or the prompt. The runtime tokenizes each hotword with the bundled
tokenizer, builds a prefix trie, and adds a top-k gated logit boost during
decoding. If no hotwords are provided, the decode path is unchanged except that
the response includes `"hotword": null`.

The WebUI exposes two hotword strength levels:

- `Normal`: default logit boost.
- `Strong`: stronger biasing for difficult names or rare terms.

Strong hotword biasing may force incorrect hotwords, hallucinate, or repeat
text. Use it only when the target terms are known in advance.

## Runtime Defaults

```text
ASR_BACKEND=auto
ASR_CACHE_PRECISION=int8
ASR_AUDIO_PRECISION=int8
```

Available variants:

- decoder: `fp32`, `int8`, `int4`
- audio tower: `fp32`, `int8`

Force a specific combination:

```bash
ASR_BACKEND=onnx_cache ASR_CACHE_PRECISION=fp32 ASR_AUDIO_PRECISION=fp32 ./run_local.sh
ASR_BACKEND=onnx_cache ASR_CACHE_PRECISION=int8 ASR_AUDIO_PRECISION=int8 ./run_local.sh
ASR_BACKEND=onnx_cache ASR_CACHE_PRECISION=int4 ASR_AUDIO_PRECISION=int8 ./run_local.sh
```

## Runtime Limits

- Audio is loaded as mono and resampled to 16 kHz.
- Audio longer than 30 seconds is truncated by the runtime bundle metadata.
- Cached decoder context is capped at 512 total tokens. If prompt audio tokens
  plus `max_new_tokens` exceed that limit, the runtime raises an error.
- CPU ONNX Runtime is the verified default path. GPU use requires installing a
  compatible ONNX Runtime GPU package and selecting an available provider.

## License

This project is released under the Creative Commons Attribution-NonCommercial
4.0 International License (CC BY-NC 4.0). Commercial use is not permitted under
this license. See `LICENSE`.

## Notes

- `requirements-onnx.txt` is pinned for reproducible local behavior.
- Runtime audio loading tries `librosa.load` first for consistent decoding.
- `run_local.sh` sets `NO_PROXY/no_proxy` for localhost inside the service
  process only; it does not change system proxy settings.
- Browser recording uploads WAV/RIFF audio. The UI records PCM with Web Audio,
  waits a short flush after Stop, then appends silence before encoding WAV.
- The UI memory panels report process RSS for CPU ONNX inference. `Peak RSS` is
  the service high-water mark; `Request Peak` is the latest request peak.

## Quick Checks

Syntax/import check:

```bash
python3 -m py_compile \
  asr_onnx_runtime.py \
  server.py \
  measure_precision_memory.py \
  transcribe_file.py
```

API smoke test with your own audio file:

```bash
./run_local.sh
./smoke_test.sh 127.0.0.1 7860 /path/to/audio.wav
```

Run one precision memory measurement:

```bash
python3 measure_precision_memory.py \
  --bundle_dir model_bundle \
  --audio /path/to/audio.wav \
  --cache_precision int8 \
  --audio_precision int8
```
