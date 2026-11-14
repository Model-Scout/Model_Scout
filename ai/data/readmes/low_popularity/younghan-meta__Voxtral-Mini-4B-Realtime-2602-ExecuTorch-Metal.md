---
license: apache-2.0
tags:
  - executorch
  - metal
  - apple-silicon
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

# Voxtral-Mini-4B-Realtime-2602-ExecuTorch-Metal

Pre-exported [ExecuTorch](https://github.com/pytorch/executorch) `.pte` files
for [Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
with **Metal** backend (Apple GPU). Supports both offline and streaming
transcription with GPU acceleration on macOS Apple Silicon.

For the XNNPACK (CPU) variant, see
[Voxtral-Mini-4B-Realtime-2602-ExecuTorch-XNNPACK](https://huggingface.co/younghan-meta/Voxtral-Mini-4B-Realtime-2602-ExecuTorch-XNNPACK).

## Installation

Install ExecuTorch from source with Metal backend support:

```bash
git clone https://github.com/pytorch/executorch/ ~/executorch
cd ~/executorch && EXECUTORCH_BUILD_KERNELS_TORCHAO=1 TORCHAO_BUILD_EXPERIMENTAL_MPS=1 ./install_executorch.sh
```

Build the runner with Metal:

```bash
cd ~/executorch && make voxtral_realtime-metal
```

Install `libomp` (required by the AOTInductor kernels):

```bash
brew install libomp
export DYLD_LIBRARY_PATH=/usr/lib:$(brew --prefix libomp)/lib
```

## Download

```bash
pip install huggingface_hub
huggingface-cli download younghan-meta/Voxtral-Mini-4B-Realtime-2602-ExecuTorch-Metal --local-dir ~/voxtral_metal
```

## Run

> All run commands require `DYLD_LIBRARY_PATH` set as shown in the installation step.

### Offline transcription

```bash
DYLD_LIBRARY_PATH=/usr/lib:$(brew --prefix libomp)/lib \
  cmake-out/examples/models/voxtral_realtime/voxtral_realtime_runner \
    --model_path ~/voxtral_metal/model-metal-fpa4w.pte \
    --tokenizer_path ~/voxtral_metal/tekken.json \
    --preprocessor_path ~/voxtral_metal/preprocessor.pte \
    --audio_path ~/voxtral_metal/poem.wav
```

### Streaming transcription (from file)

```bash
DYLD_LIBRARY_PATH=/usr/lib:$(brew --prefix libomp)/lib \
  cmake-out/examples/models/voxtral_realtime/voxtral_realtime_runner \
    --model_path ~/voxtral_metal/model-metal-fpa4w-streaming.pte \
    --tokenizer_path ~/voxtral_metal/tekken.json \
    --preprocessor_path ~/voxtral_metal/preprocessor-streaming.pte \
    --audio_path ~/voxtral_metal/poem.wav \
    --streaming
```

### Live microphone (macOS)

```bash
ffmpeg -f avfoundation -i ":0" -ar 16000 -ac 1 -f f32le -nostats -loglevel error pipe:1 | \
  DYLD_LIBRARY_PATH=/usr/lib:$(brew --prefix libomp)/lib \
  cmake-out/examples/models/voxtral_realtime/voxtral_realtime_runner \
    --model_path ~/voxtral_metal/model-metal-fpa4w-streaming.pte \
    --tokenizer_path ~/voxtral_metal/tekken.json \
    --preprocessor_path ~/voxtral_metal/preprocessor-streaming.pte \
    --mic
```

## Performance (Apple Silicon Mac, 20s audio)

| Mode | TTFT | Gen Tokens | Gen Rate (tok/s) | Total Inference |
|------|------|------------|------------------|-----------------|
| Offline | 2.121s | 377 | 40.82 | 11.356s |
| Streaming | 0.304s | 260 | 16.18 | 16.374s |

## Export Commands

These models were exported with:

```bash
# Offline
python examples/models/voxtral_realtime/export_voxtral_rt.py \
    --model-path ~/models/Voxtral-Mini-4B-Realtime-2602 \
    --backend metal \
    --output-dir ./voxtral_rt_metal_offline \
    --qlinear-encoder fpa4w \
    --qlinear fpa4w

# Streaming
python examples/models/voxtral_realtime/export_voxtral_rt.py \
    --model-path ~/models/Voxtral-Mini-4B-Realtime-2602 \
    --backend metal \
    --streaming \
    --output-dir ./voxtral_rt_metal_streaming \
    --qlinear-encoder fpa4w \
    --qlinear fpa4w
```

## Troubleshooting

- **`Library not loaded: @rpath/libc++.1.dylib`** — Add `/usr/lib` to `DYLD_LIBRARY_PATH`:
  ```bash
  export DYLD_LIBRARY_PATH=/usr/lib:$(brew --prefix libomp)/lib
  ```

- **`Library not loaded: libomp.dylib`** — Install OpenMP via Homebrew:
  ```bash
  brew install libomp
  ```

- **Audio format** — Input must be 16kHz mono WAV. Convert with:
  ```bash
  ffmpeg -i input.mp3 -ar 16000 -ac 1 output.wav
  ```

## More Info

- [Official ExecuTorch Voxtral Realtime guide](https://github.com/pytorch/executorch/tree/main/examples/models/voxtral_realtime)
- [Original model](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602)
- [Mistral technical report](https://arxiv.org/abs/2602.11298)
