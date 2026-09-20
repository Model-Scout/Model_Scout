---
license: apache-2.0
base_model: Qwen/Qwen3-ForcedAligner-0.6B
language:
  - zh
  - en
  - yue
  - fr
  - de
  - it
  - ja
  - ko
  - pt
  - ru
  - es
tags:
  - forced-alignment
  - speech-to-text
  - audio
  - timestamps
  - gguf
  - ggml
  - qwen3
pipeline_tag: automatic-speech-recognition
library_name: ggml
---

# Qwen3-ForcedAligner-0.6B — GGUF (CrispASR)

GGUF conversions of [`Qwen/Qwen3-ForcedAligner-0.6B`](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B) — a single-pass forced aligner that takes any (audio, transcript) pair and predicts per-word/per-token timestamps. Reuses the Qwen3-ASR audio encoder + 28-layer LLM body but swaps the lm_head from `(vocab, d)` to `(5000, d)`: each `<timestamp>` placeholder you embed in the input gets a 5000-class softmax over `class * 80 ms` timestamps.

Plug it into [CrispASR](https://github.com/CrispStrobe/CrispASR) via `-am qwen3-forced-aligner-*.gguf` to get word-level timing on **any** transcription backend — voxtral, voxtral4b, qwen3-asr, granite, parakeet, canary, cohere, even whisper. It's an alternative to the existing `canary-ctc-aligner` second-pass with broader language coverage and 80-ms resolution.

## What's in the box

| File | Size | Quantization | Notes |
|---|---|---|---|
| `qwen3-forced-aligner-0.6b-f16.gguf` | 1.84 GB | F16 | Reference precision; matches PyTorch bfloat16 within float-noise tolerance |
| `qwen3-forced-aligner-0.6b-q8_0.gguf` | 0.99 GB | Q8_0 | Effectively lossless |
| `qwen3-forced-aligner-0.6b-q5_0.gguf` | 0.64 GB | Q5_0 | Slightly slower than Q4_K but a bit more accurate on edge cases |
| `qwen3-forced-aligner-0.6b-q4_k.gguf` | 0.53 GB | Q4_K | 3.5× compressed; smallest reasonable choice |

All four contain:

* The full audio encoder (24 layers, d_model 1024, 16 heads, 4096 ff)
* The Qwen3 0.6B LLM body (28 layers, d_model 1024, 16 heads / 8 KV heads, 3072 ff, 152K vocab, RoPE θ=1e6)
* The 5000-class **forced-alignment** lm_head (instead of the 152K-class lm_head used by the regular ASR variants)
* Full GPT-2-style BPE vocab + merges, mel filterbank, and Hann window

## How it differs from the ASR models

Same body, different head:

| | Qwen3-ASR-0.6B / 1.7B | Qwen3-ForcedAligner-0.6B |
|---|---|---|
| Audio encoder | 24-layer, d_model 1024 | identical |
| Text decoder | Qwen3 28-layer | identical body |
| `lm_head` shape | `(vocab=152K, d)` | **`(5000, d)`** — timestamp classes |
| Inference mode | Autoregressive (decode token by token) | **Single forward pass** over the whole input |
| Use case | Audio → text | (Audio, text) → per-word timestamps |
| Output | Generated tokens | argmax(lm_head)·80 ms at each `<timestamp>` placeholder |

The CrispASR C++ runtime auto-detects which variant a loaded GGUF is by reading the lm_head shape from `output.weight.ne[1]` — no separate backend, no separate library.

## Use with CrispASR

```bash
# Build crispasr (one-time)
git clone https://github.com/CrispStrobe/CrispASR
cd CrispASR
cmake -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build -j$(nproc) --target whisper-cli

# Word-level SRT from any transcription backend, using FA for timing.
# `-am` (--aligner-model) auto-routes to the qwen3-fa path when the
# filename contains "forced-aligner" (case-insensitive).

# voxtral 3B + Qwen3-FA timing
./build/bin/crispasr --backend voxtral \
    -m voxtral-mini-3b-2507-q8_0.gguf \
    -f my_audio.wav \
    -am qwen3-forced-aligner-0.6b-q4_k.gguf \
    -osrt -ml 1

# parakeet + Qwen3-FA (parakeet has its own native word timestamps, but
# you can override them with FA on the same audio)
./build/bin/crispasr --backend parakeet \
    -m parakeet-tdt-0.6b-v3-q4_k.gguf \
    -f my_audio.wav \
    -am qwen3-forced-aligner-0.6b-q4_k.gguf \
    -osrt -ml 1

# Granite, qwen3-asr, voxtral4b, cohere, canary all work the same way.
```

The Python equivalent on the upstream side is `Qwen3ForcedAligner.align(audio, text, language)` from `qwen-asr`. Our C++ wrapper does the whole pipeline (mel → encoder → prompt build with `<timestamp>` placeholders → embed + audio splice → single FA forward → argmax at placeholder positions → ms conversion) in one call to `qwen3_asr_align_words(ctx, samples, n_samples, words[], n_words, out_start_ms, out_end_ms)`.

## Languages

Same as upstream Qwen3-ForcedAligner: Chinese, English, Cantonese, French, German, Italian, Japanese, Korean, Portuguese, Russian, Spanish (11 languages).

The current C++ wrapper uses **whitespace pre-tokenization** for splitting the transcript into words. This works well for English and the other Latin/Cyrillic-script languages but is sub-optimal for Chinese / Japanese where the upstream Python uses character-level / morphological tokenizers (`tokenize_japanese`, `tokenize_korean` via soynlp). Adding char-level tokenization for CJK languages is a follow-up tracked in the CrispASR repo.

## How it was made

```bash
# 1. Download the base model from HF
hf download Qwen/Qwen3-ForcedAligner-0.6B --local-dir ./Qwen3-ForcedAligner-0.6B

# 2. Convert to F16 GGUF (the qwen3-asr converter handles both ASR and
#    ForcedAligner variants — sizes are read from config.json so the
#    same script handles both checkpoints)
python models/convert-qwen3-asr-to-gguf.py \
    --input ./Qwen3-ForcedAligner-0.6B \
    --output qwen3-forced-aligner-0.6b-f16.gguf

# 3. Quantize
./build/bin/crispasr-quantize qwen3-forced-aligner-0.6b-f16.gguf qwen3-forced-aligner-0.6b-q8_0.gguf q8_0
./build/bin/crispasr-quantize qwen3-forced-aligner-0.6b-f16.gguf qwen3-forced-aligner-0.6b-q5_0.gguf q5_0
./build/bin/crispasr-quantize qwen3-forced-aligner-0.6b-f16.gguf qwen3-forced-aligner-0.6b-q4_k.gguf q4_k
```

The C++ side needed two small additions to support FA models alongside ASR models in the existing qwen3 backend:

1. **Flexible lm_head shape.** `qwen3_asr_load_model` now reads the actual `output.weight.ne[1]` instead of asserting it equals `llm.vocab_size`. For ASR models the two are equal (152K); for FA models the head is 5000 wide.

2. **Single-pass aligner forward.** A new `qwen3_asr_run_aligner()` extern "C" entry point runs `build_graph_llm_kv(..., last_token_only=false)` so the lm_head sees every token position, not just the last. The result is a `(5000, T)` logit matrix; `qwen3_asr_align_words()` reads argmax at the positions where `input_id == 151705` (`<timestamp>` placeholder) and converts to ms via `class * 80`.

## Verification

End-to-end on samples/jfk.wav with voxtral as the transcription backend:

```bash
crispasr --backend voxtral -m voxtral-mini-3b-2507-q8_0.gguf \
    -f samples/jfk.wav \
    -am qwen3-forced-aligner-0.6b-q4_k.gguf -ml 1
```

```
[00:00:00.320 --> 00:00:00.560]  And
[00:00:00.960 --> 00:00:00.960]  so,
[00:00:00.960 --> 00:00:01.280]  my
[00:00:01.360 --> 00:00:01.680]  fellow
[00:00:02.080 --> 00:00:02.160]  Americans,
... (10 s total, 21 words)
```

Same audio with all four quants produces near-identical timing — the worst spread between F16 and Q4_K on this clip is 80 ms (one alignment-class step).

## License

Apache-2.0, same as upstream Qwen3-ForcedAligner-0.6B.

## Citation

```bibtex
@misc{qwen3asr,
    title  = {Qwen3-ASR},
    author = {Qwen Team},
    year   = {2026},
    url    = {https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B}
}
```

## Provenance and EU AI Act Art. 53 note

- **Upstream model:** [Qwen/Qwen3-ForcedAligner-0.6B](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B) — published by `Qwen`.
- **Upstream licence:** `apache-2.0`. This repository redistributes under the same terms; it grants no rights the upstream licence does not.
- **What was done here:** format conversion and/or quantisation only (GGUF/GGML). No training, no fine-tuning, no merging, no distillation, no change to architecture, vocabulary or capability. Only the numeric representation of the upstream weights differs.
- **Training data:** documented — where it is documented at all — by the upstream provider; see the upstream model card. No training data was used, added or selected by this repository.
- **Provider status:** under Regulation (EU) 2024/1689 the upstream authors remain the provider of this model. Converting the serialisation format does not make this repository the provider of a new general-purpose AI model, and no such claim is made. Questions about training content, copyright policy or model capability belong upstream.
