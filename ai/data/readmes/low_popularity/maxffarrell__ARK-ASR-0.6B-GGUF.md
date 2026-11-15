---
license: apache-2.0
base_model: Edge0/ARK-ASR-0.6B
pipeline_tag: automatic-speech-recognition
language:
- zh
- en
- de
- ja
- fr
- ko
- es
- pl
- it
- ro
- hu
- cs
- nl
- fi
- hr
- sk
- sl
- et
- lt
tags:
- gguf
- arkasr
- transcribe.cpp
---

# ARK-ASR-0.6B GGUF candidate

## Original authors and conversion credits

**ARK-ASR is the work of AutoArk and research authors Yu Lin, Yiming Wang,
Runyuan Cai, and Xiaodong Zeng.** Original model:
[Edge0/ARK-ASR-0.6B](https://huggingface.co/Edge0/ARK-ASR-0.6B) ·
[Original project](https://github.com/AutoArk/open-audio-opd) ·
[Research paper](https://arxiv.org/abs/2605.28139).

**This conversion reuses harshav's ARK GGUF converter and runtime** from
[ARK-ASR-3B-GGUF](https://huggingface.co/harshav/ARK-ASR-3B-GGUF), built on
[the transcribe.cpp authors' native engine](https://github.com/handy-computer/transcribe.cpp).
**maxffarrell contributed the 0.6B adaptation, quantization, validation and
packaging**, with Codex assistance—not the original model or research.

**Licenses:** original weights are Apache-2.0; converter/runtime are MIT.
See [full attribution and research citation](ATTRIBUTION.md), [NOTICE](NOTICE),
[weight license](LICENSE) and [converter license](CONVERTER-LICENSE).
The v2 GGUF embeds these credits and source links so they travel with the file.

Community Q8 conversion of [Edge0/ARK-ASR-0.6B](https://huggingface.co/Edge0/ARK-ASR-0.6B),
prepared for a draft Hex integration. No retraining. Not affiliated with the
original authors, and not a canonical handy-computer artifact.

**Requires an ARK-enabled runtime.** Stock llama.cpp, whisper.cpp and released
transcribe-cpp 0.2.4 cannot load it. Use the candidate runtime at
[maxffarrell/transcribe.cpp](https://github.com/maxffarrell/transcribe.cpp/tree/19f301609c06126e5071d1de5acdd95c714eec05),
revision `19f301609c06126e5071d1de5acdd95c714eec05`.
[Upstream draft PR](https://github.com/handy-computer/transcribe.cpp/pull/191).

## File

`ark-asr-0.6b-Q8_0-v2.gguf`: 1,372,882,944 bytes.
SHA-256: `20a9954ce65e0e724a836194a12ad10879ca746c133dcea54e0d15f2132a94bd`.

The 0.6B name describes the decoder; the full model also contains the audio
encoder and adapter. Q8 linear weights, F16 tied embedding/output matrix and
convolutions, F32 norms/biases/frontend tensors.

## Run

```sh
git clone https://github.com/maxffarrell/transcribe.cpp
cd transcribe.cpp
git checkout 19f301609c06126e5071d1de5acdd95c714eec05
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DTRANSCRIBE_BUILD_EXAMPLES=ON
cmake --build build --target transcribe-cli -j 8
hf download maxffarrell/ARK-ASR-0.6B-GGUF ark-asr-0.6b-Q8_0-v2.gguf --local-dir models/ark
build/bin/transcribe-cli --backend metal -m models/ark/ark-asr-0.6b-Q8_0-v2.gguf audio.wav
```

Use `--backend cpu` for CPU inference. Input frontend: mono 16 kHz.
Long recordings use overlapping windows of at most 30 seconds. Language is
inferred from audio; forced-language steering, translation, streaming and
timestamps are not supported by this candidate.

## Validation and limitations

Six public short samples from transcribe.cpp (JFK, Mandarin, Japanese, Korean,
noise and silence) produced exactly matching text in the original PyTorch
checkpoint, F16 GGUF and this Q8 GGUF. The Q8 JFK transcript also matched on
CPU and Metal. A 197-second public English speech clip completed through the
runtime's overlapping-window path on Metal. The existing 45 runtime CTests
passed. See `validation.json` for the compared text.

Reference agreement is not a ground-truth WER measurement. The original model
and both GGUF precisions emitted Japanese text for the Korean sample and
`嗯。` for noise and silence. Automatic language detection and hallucination
on nonspeech remain material limitations. The publisher's 19-language list
is coverage metadata, not validation of all languages. Long-audio completion
does not establish parity against an unchunked reference. Full tensor parity,
WER evaluation and upstream port acceptance remain incomplete. Treat this as
an experimental model, not an accuracy or speed recommendation.

## Reproduce

Source: `Edge0/ARK-ASR-0.6B@45776b56d58cdfb2e2eb632f7e110f38684633e0`.
Original `model.safetensors` SHA-256:
`57a86ce1c2f2c2d6ebb7ad9642c9e951a5109625122b48c9180126a28787673d`.

```sh
uv run convert-arkasr-to-gguf.py --input Edge0/ARK-ASR-0.6B \
  --revision 45776b56d58cdfb2e2eb632f7e110f38684633e0 \
  --variant ark-asr-0.6b --outtype q8_0 --output ark-asr-0.6b-Q8_0-v2.gguf
```

The included converter reuses harshav's work from
[ARK-ASR-3B-GGUF](https://huggingface.co/harshav/ARK-ASR-3B-GGUF), with variant,
revision and capability metadata adapted for 0.6B. Its source archive is pinned
in `conversion.json`. Converter/runtime license: MIT (`CONVERTER-LICENSE`);
weights: Apache-2.0 (`LICENSE`). Original architecture, training and evaluation:
[AutoArk/open-audio-opd](https://github.com/AutoArk/open-audio-opd).

This community conversion and its draft integration were prepared with Codex
at the contributor's request.

## Earlier artifact

`ark-asr-0.6b-Q8_0.gguf` is retained unchanged for existing pinned consumers.
Use `ark-asr-0.6b-Q8_0-v2.gguf` for embedded attribution. Every tensor in v2
is byte-identical to the earlier file; only descriptive metadata changed.
