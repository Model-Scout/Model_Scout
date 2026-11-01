---
base_model: microsoft/VibeVoice-ASR-Streaming-7B
license: mit
library_name: gguf
pipeline_tag: automatic-speech-recognition
language:
  - en
  - zh
  - es
  - pt
  - de
  - ja
  - ko
  - fr
  - ru
  - it
tags:
  - gguf
  - vibevoice
  - asr
  - speech-to-text
  - streaming
  - rust
---

# VibeVoice-ASR-Streaming-7B GGUF

Unofficial GGUF conversion of
[`microsoft/VibeVoice-ASR-Streaming-7B`](https://huggingface.co/microsoft/VibeVoice-ASR-Streaming-7B)
for the native Rust implementation in
[`Liyulingyue/rust-model-inference`](https://github.com/Liyulingyue/rust-model-inference).

The model performs streaming, speaker-attributed automatic speech recognition
for Chinese, English, French, German, Italian, Japanese, Korean, Portuguese,
Russian, and Spanish. It can also use context terms supplied through the Rust
CLI's `--prompt` option.

## Files

Both files are required for ASR inference.

| File | Size | Contents |
| --- | ---: | --- |
| `VibeVoice-ASR-Streaming-7B-Q8_0.gguf` | 7.54 GiB | Qwen2.5 decoder: 198 Q8_0 tensors and 141 F32 tensors |
| `mmproj-VibeVoice-ASR-Streaming-7B-BF16.gguf` | 1.33 GiB | Acoustic/semantic encoders and speech connectors: 562 BF16 tensors |

The LLM has 28 layers, a hidden size of 3584, a context length of 131072, and
a vocabulary size of 152064. The mmproj expects 24 kHz audio and uses a custom
`vibevoice_asr` audio projector.

## Compatibility

The validated runtime is `rust-model-inference` after merged
[PR #47](https://github.com/Liyulingyue/rust-model-inference/pull/47).

The LLM uses llama.cpp-style Qwen2 tensor names, but the end-to-end ASR model
is **not compatible with stock llama.cpp**. The audio encoder/projector is a
VibeVoice-specific mmproj that requires the Rust implementation above.

## Rust Usage

```bash
git clone https://github.com/Liyulingyue/rust-model-inference.git
cd rust-model-inference

cargo run --release --bin rust-model-inference -- \
  --model /path/to/VibeVoice-ASR-Streaming-7B-Q8_0.gguf \
  --mmproj /path/to/mmproj-VibeVoice-ASR-Streaming-7B-BF16.gguf \
  --audio /path/to/input.wav \
  --temp 0 \
  --max-tokens 128 \
  --threads 8 \
  --out transcription.txt
```

The current CLI accepts PCM16 WAV input. It downmixes multi-channel input and
resamples it to the model's 24 kHz sample rate. `--max-tokens` is the maximum
number of generated tokens per streaming chunk.

Use `--prompt` to provide names or domain terms as recognition context:

```bash
  --prompt "Microsoft,VibeVoice"
```

For reproducible encoder latents, set:

```bash
export VIBEVOICE_ASR_DETERMINISTIC=1
```

## Conversion

The converter reads the original sharded BF16 safetensors through mmap and
does not require PyTorch:

```bash
python3 tools/vibevoice/convert_vibevoice_asr.py \
  /path/to/VibeVoice-ASR-Streaming-7B \
  --out-dir /path/to/output
```

The language decoder is quantized to GGML Q8_0. The acoustic and semantic
encoders and connectors remain BF16. The unused acoustic tokenizer decoder is
not included because ASR does not synthesize audio.

## Alignment

The Rust implementation was checked against the original BF16 safetensors on
a fixed prompt and audio fixture:

| Checkpoint | Result |
| --- | ---: |
| Decoder layer 0 hidden NRMSE | 0.005884 |
| Worst decoder layer hidden NRMSE (layer 25) | 0.023366 |
| Decoder layer 27 hidden NRMSE | 0.015076 |
| Final normalized hidden NRMSE | 0.020717 |
| Full 152064-value logits NRMSE | 0.009781 |
| Maximum absolute logits error | 0.196437 |

The top-8 token ordering matched exactly:

```text
[58, 151665, 715, 42474, 39379, 32622, 43504, 37073]
```

The BF16 audio encoder Oracle covered 12 checkpoints with a maximum absolute
error of 0.000070.

These are numerical comparisons, not bitwise equality. Q8_0 weight and
activation quantization necessarily differs from the original BF16 model. The
decoder comparison covers the final sequence row at every layer for one fixed
fixture; it does not claim exhaustive equality for every input or internal
Q/K/V tensor.

## Checksums

```text
255ca05bb3b4f34ab02922da5bc3f4ac6de489552175cc013c1a1db7e69d9514  VibeVoice-ASR-Streaming-7B-Q8_0.gguf
020e256a28f9ccb1e0ad658467545a6a81bd9d3ca2f52cb4ba146712afc1699b  mmproj-VibeVoice-ASR-Streaming-7B-BF16.gguf
```

## Limitations

- Only the CPU inference path has been validated for this conversion.
- Quantization can change recognition output relative to the BF16 checkpoint.
- The Rust CLI currently requires PCM16 WAV files; microphone/WebSocket serving
  is not included in this model repository.
- Review the original model card for intended use, evaluation, and responsible
  use guidance.

## License and Attribution

The source model is provided by Microsoft under the MIT License. This
repository redistributes converted model weights under the same license. See
[`LICENSE`](./LICENSE) and the
[original model card](https://huggingface.co/microsoft/VibeVoice-ASR-Streaming-7B).

