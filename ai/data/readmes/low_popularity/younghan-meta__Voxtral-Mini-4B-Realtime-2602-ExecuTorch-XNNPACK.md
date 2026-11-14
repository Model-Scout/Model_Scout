---
license: apache-2.0
tags:
  - executorch
  - xnnpack
  - speech-to-text
  - streaming
  - on-device
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
pipeline_tag: automatic-speech-recognition
base_model: mistralai/Voxtral-Mini-4B-Realtime-2602
---

# Voxtral-Mini-4B-Realtime-2602-ExecuTorch-XNNPACK

Pre-exported [ExecuTorch](https://github.com/pytorch/executorch) `.pte` files
for [Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
with **XNNPACK** backend (CPU). Supports both offline and streaming transcription
on any platform with a CPU — no GPU required.

For the Metal (Apple GPU) variant, see
[Voxtral-Mini-4B-Realtime-2602-ExecuTorch-Metal](https://huggingface.co/younghan-meta/Voxtral-Mini-4B-Realtime-2602-ExecuTorch-Metal).

## Installation

Install ExecuTorch from source:

```bash
git clone https://github.com/pytorch/executorch/ ~/executorch
cd ~/executorch && ./install_executorch.sh
```

Build the runner with XNNPACK:

```bash
cd ~/executorch && make voxtral_realtime-cpu
```

## Download

```bash
pip install huggingface_hub
huggingface-cli download younghan-meta/Voxtral-Mini-4B-Realtime-2602-ExecuTorch-XNNPACK --local-dir ~/voxtral_xnnpack
```

## Run

### Offline transcription

```bash
cmake-out/examples/models/voxtral_realtime/voxtral_realtime_runner \
    --model_path ~/voxtral_xnnpack/model-xnnpack-8da4w.pte \
    --tokenizer_path ~/voxtral_xnnpack/tekken.json \
    --preprocessor_path ~/voxtral_xnnpack/preprocessor.pte \
    --audio_path ~/voxtral_xnnpack/poem.wav
```

### Streaming transcription (from file)

```bash
cmake-out/examples/models/voxtral_realtime/voxtral_realtime_runner \
    --model_path ~/voxtral_xnnpack/model-xnnpack-8da4w-streaming.pte \
    --tokenizer_path ~/voxtral_xnnpack/tekken.json \
    --preprocessor_path ~/voxtral_xnnpack/preprocessor-streaming.pte \
    --audio_path ~/voxtral_xnnpack/poem.wav \
    --streaming
```

### Live microphone (macOS)

```bash
ffmpeg -f avfoundation -i ":0" -ar 16000 -ac 1 -f f32le -nostats -loglevel error pipe:1 | \
  cmake-out/examples/models/voxtral_realtime/voxtral_realtime_runner \
    --model_path ~/voxtral_xnnpack/model-xnnpack-8da4w-streaming.pte \
    --tokenizer_path ~/voxtral_xnnpack/tekken.json \
    --preprocessor_path ~/voxtral_xnnpack/preprocessor-streaming.pte \
    --mic
```

## Performance (Apple Silicon Mac, 20s audio)

| Mode | TTFT | Gen Tokens | Gen Rate (tok/s) | Total Inference |
|------|------|------------|------------------|-----------------|
| Offline | 6.698s | 377 | 26.94 | 20.690s |
| Streaming | 0.096s | 261 | 11.01 | 23.798s |

## Export Commands

These models were exported with:

```bash
# Offline
python examples/models/voxtral_realtime/export_voxtral_rt.py \
    --model-path ~/models/Voxtral-Mini-4B-Realtime-2602 \
    --backend xnnpack \
    --output-dir ./voxtral_rt_xnnpack_offline \
    --qlinear-encoder 8da4w \
    --qlinear 8da4w \
    --qembedding 8w

# Streaming
python examples/models/voxtral_realtime/export_voxtral_rt.py \
    --model-path ~/models/Voxtral-Mini-4B-Realtime-2602 \
    --backend xnnpack \
    --streaming \
    --output-dir ./voxtral_rt_xnnpack_streaming \
    --qlinear-encoder 8da4w \
    --qlinear 8da4w \
    --qembedding 8w
```

## More Info

- [Official ExecuTorch Voxtral Realtime guide](https://github.com/pytorch/executorch/tree/main/examples/models/voxtral_realtime)
- [Original model](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
- [Mistral technical report](https://arxiv.org/abs/2602.11298)
