---
license: other
license_name: openmdw-1.1
license_link: >-
  https://openmdw.ai/license/1-1/
library_name: nemo
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
- speech-recognition
- cache-aware ASR
- automatic-speech-recognition
- streaming-asr
- multilingual
- speech
- audio
- FastConformer
- RNNT
- Parakeet
- ASR
- pytorch
- NeMo
- Websocket
- ONNX
base_model: nvidia/nemotron-3.5-asr-streaming-0.6b
pipeline_tag: automatic-speech-recognition
---

# Nemotron Streaming ASR

Minimal local WebSocket runtime and clients for [NVIDIA Nemotron 3.5 ASR Streaming](https://huggingface.co/nvidia/nemotron-3.5-asr-streaming-0.6b) FP32 ONNX artifacts.

This package contains Python runtime code, WebSocket clients, audio frontend utilities, and validation scripts. It does not package model weights, ONNX files, debug captures, local logs, release zips, or reference repos.

## Install

CPU server/client install:

```bash
python -m pip install -e '.[test]'
```

Microphone client support:

```bash
python -m pip install -e '.[mic,test]'
```

GPU/CUDA server support is optional:

```bash
python -m pip install -e '.[gpu,test]'
```

Use `docs/gpu_cuda.md` to verify `onnxruntime` and CUDA provider availability before starting a CUDA server.

## Model Directory Contract

The server expects `--model-dir models` by default. The directory is intentionally local and ignored by `.gitignore`; do not include it in package artifacts. Required files:

- `NemoPreprocessor128.onnx`
- `encoder-model.onnx`
- `encoder-model.data`
- `decoder_joint-model.onnx`
- `tokenizer.model`
- `vocab.txt`
- `config.json`
- `io_contract.json`

The runtime validates the ONNX IO contract, cache inputs, `prompt_index`, vocabulary shape, and blank token placement before inference.

Each cache-aware duration is a separate FP32 bundle. Native Nemotron look-aheads
are 80, 320, 560, and 1120 ms. The 160 ms `[56,1]` export is retained only as a
diagnostic artifact because NeMo does not declare that lookahead as supported;
a 160 ms transport profile should use two lossless 80 ms model steps. The
runtime rejects a requested encoder step that does not match its loaded bundle.

## Runtime Profile

`config.json` is the validated server profile. It selects CPU by default, a
560 ms primary bundle, an 80 ms visible-partial bundle, 20 ms client frames,
`en-US` prompting, a 0.6-second wall probe deadline, and a 0.9-second raw
maximum gate. Audio capture, transcript logging, and silence gating are all
disabled by default. CLI flags override profile values for local experiments.

## Commands

Start the selected CPU/WebSocket profile:

```bash
nemotron-asr-server --config config.json
```

Override execution or add the selected low-latency sidecar explicitly:

```bash
nemotron-asr-server --config config.json --execution-provider cpu \
  --encoder-step-ms 560 --speculative-model-dir models/candidate-80ms \
  --speculative-encoder-step-ms 80
nemotron-asr-server --config config.json --execution-provider cuda
```

Stream a WAV file:

```bash
nemotron-asr-client-file --url ws://127.0.0.1:8765 --wav examples/sample.wav --language en-US --print-transcript
```

Run the microphone client:

```bash
nemotron-asr-client-mic --url ws://127.0.0.1:8765 --language en-US --frontend-preset nemotron_safe --print-transcript
```

Run the local evaluation matrix when model files and a reference transcript are available:

```bash
nemotron-asr-eval-matrix --wav examples/sample.wav --reference examples/sample_transcript.txt --model-dir models
```

Debug utilities remain under `scripts/`; see `docs/package_contents.md`.

Source-timed streaming replay and frozen paired comparison are documented in
[`docs/streaming_asr_replay.md`](docs/streaming_asr_replay.md). Replay evidence
is explicitly labelled deterministic and never presented as true-live latency.
The documented WebSocket runner exercises the same cases through the local
client/server boundary and keeps private transcripts under ignored logs.
The completed 520-case latency, correctness, partition, fold, and WebSocket
results are summarized in
[`docs/streaming_asr_research_results.md`](docs/streaming_asr_research_results.md).
For a latency/accuracy WebSocket profile, add
`--speculative-encoder-step-ms 80` to the server while retaining the verified
final encoder geometry. On CPU, the server bounds sidecar inference to the
first visible event and then queues/replays the final decoder stream without
drops. The paced WebSocket wall deadline reserves transport time before the
0.9-second observation gate.

## Performance Summary

The frozen 520-case K-fold projection contains 174 development, 105
validation, and 241 testing cases. Correctness uses the exact paired Voxtral
ASR rows and identical normalization.

| metric | Nemotron 3.5 Streaming ASR | Voxtral ASR |
| --- | ---: | ---: |
| micro normalized WER | 7.035% | 4.738% |
| micro normalized CER | 3.414% | 2.114% |
| macro normalized WER | 6.930% | 4.471% |
| macro normalized CER | 3.524% | 2.026% |
| normalized exact match | 20.00% | 24.62% |
| normalized S / D / I | 855 / 416 / 239 | 563 / 347 / 107 |
| WER wins / ties / losses | 93 / 200 / 227 | paired reference |

Nemotron latency passes both required transports: deterministic source replay
is `0.540 s` mean and `0.800 s` raw maximum over 520/520 cases; paced WebSocket
WAV replay is `0.721 s` mean, `0.789 s` p95, and `0.837 s` raw maximum over
241/241 testing cases. The latter exercises the live client/server transport
but is not microphone truth. The correctness gate fails because Nemotron does
not lower WER or CER and does not improve macro correctness. See
[`docs/streaming_asr_research_results.md`](docs/streaming_asr_research_results.md)
for partition, fold, speed, and geometry results.

## Provider Selection

`config.json` selects `cpu` for this CPU-only deployment. `auto` uses
`CUDAExecutionProvider` with CPU fallback when ONNX Runtime reports CUDA,
otherwise it uses `CPUExecutionProvider`. `cpu` forces CPU. `cuda` requires
CUDA and exits with a clean user-facing error if unavailable.

The selected provider list is logged at server startup and model load.

## Recommended ASR Modes

Use continuous ASR input with `nemotron_safe` as the current stable candidate:

```bash
nemotron-asr-client-mic --frontend-preset nemotron_safe --asr-input-mode continuous --print-transcript
```

`vad_island` with `island_fast` is available for latency experiments, but it remains experimental:

```bash
nemotron-asr-client-mic --frontend-preset nemotron_safe --asr-input-mode vad_island --vad-island-send-policy island_fast --print-transcript
```

Silence dropping/gating is disabled by default.

## EC2 Server + WSL Client Quickstart

On EC2, bind the server to loopback and use SSH port forwarding from the WSL machine:

```bash
nemotron-asr-server --host 127.0.0.1 --port 8765 --model-dir models --execution-provider auto
```

From WSL:

```bash
ssh -N -L 8765:127.0.0.1:8765 ubuntu@<ec2-public-dns>
nemotron-asr-client-mic --url ws://127.0.0.1:8765 --frontend-preset nemotron_safe --print-transcript
```

Do not hardcode public IP addresses in repo files; use environment-specific shell history or deployment configuration.

## Privacy

Audio capture flags are opt-in because they may write private speech to disk. Avoid `--capture-input-wav`, `--capture-raw-wav`, `--capture-processed-wav`, `--capture-received-audio-dir`, and transcript logging unless the capture location and retention policy are clear.

## Validation

Before claiming a release or handoff, run:

```bash
python -m compileall nemotron_asr scripts realtime_test.py realtime_test_mic.py nemotron_server.py nemotron_client_file.py nemotron_client_mic.py
pytest -q
python scripts/quality_gate.py --model-dir models --coverage-min 80
python scripts/quality_gate.py --model-dir models --coverage-min 90
```

The 90% gate includes every active Python implementation file and requires
both aggregate and per-file coverage to reach 90%.

## Citation

### BibTeX

```bibtex
@software{lumbantobing2026nemotronstreamingasrmultilingual,
  author       = {Patrick Lumbantobing},
  title        = {Nemotron Streaming ASR Multilingual},
  year         = {2026},
  organization = {VertoX AI},
  url          = {https://huggingface.co/vertox-ai/nemotron-streaming-asr-multilingual},
  license      = {OpenMDW-1.1}
}
```

## Author

**Patrick Lumbantobing**  
VertoX AI
