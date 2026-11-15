---
license: mit
base_model: microsoft/VibeVoice-ASR-BitNet
tags:
  - litert
  - tflite
  - bitnet
  - ternary
  - automatic-speech-recognition
  - on-device
  - android
language: [en, zh, fr, it, ko, pt, vi]
library_name: litert
pipeline_tag: automatic-speech-recognition
---

# VibeVoice-ASR-BitNet — LiteRT export

LiteRT (TFLite) conversion of [microsoft/VibeVoice-ASR-BitNet](https://huggingface.co/microsoft/VibeVoice-ASR-BitNet),
so the model runs on Android and Linux with **no ggml / llama.cpp dependency**.

The decoder is ternary (BitNet I2_S). LiteRT has no ternary kernel, and a normal
export turns it into an int8 matmul — keeping the *values*, discarding the
*packing*. Packing is the performance: batch-1 decode is memory-bandwidth-bound, so
a 1.31 B-parameter decoder moves ~328 MB per token at 2 bits versus ~1310 MB at
int8. These files keep the 2-bit packing, and the runtime consumes it through a
**custom op**.

Engine, kernel and export scripts:
[vieenrose/LiteRT · samples/asr/vibevoice](https://github.com/vieenrose/LiteRT/tree/vibevoice-ternary/litert/samples/asr/vibevoice)

## Contents

| file | what it is |
|---|---|
| `vibe_front_10s_q8.tflite` | audio front end — both tokenizer encoders + connectors, summed, per-channel int8, fixed 10 s window @ 24 kHz |
| `decoder_28L_512_c.tflite` | 28-layer decode step, ctx 512, one token per pass |
| `prefill_512_t16_c.tflite` | same but 16 tokens per pass, for prompt ingestion |
| `head_q8.tflite` | output norm + LM head, per-channel int8, weights baked in |
| `weights/dec_w*.bin` | packed ternary weights + per-row scales, bound at runtime |
| `dec_28L_manifest.txt` | input order for the decoder graphs |
| `embd_table.bin` | Q6_K token embedding table, dequantized one row at a time on the host |
| `vocab.json` | for byte-level BPE detokenization |

The decoder's weights ship **outside** the graph because LiteRT's dispatcher will
not hand constant tensors to a custom kernel; the head's are baked in because it
uses no custom op. Weights are mmap'd at load, so they stay clean file-backed pages.

## Measured

Boox Tab Mini C — Snapdragon 662, Cortex-A73, **ARMv8.0 without dotprod**, roughly
worst case for int8 SIMD. Back to back against the ggml build of the same model:

| | this export | ggml (`asr_infer`) |
|---|---|---|
| decode | **123.5 ms/token** | 123.1 |
| prefill (T=16) | **68 ms/token** | — |
| peak RSS | **786 MB** | 1297 MB |
| peak RssAnon | **241 MB** | 507 MB |

Parity on speed at **half the unevictable memory**, which is the figure that
decides whether an Android app survives memory pressure.

Those memory figures are **decode only**. Through the full pipeline on Android,
peak RssAnon is 906 MB: 173 MB of runtime/harness baseline, +55 MB compiling the
encoder, +231 MB compiling the head, +46 MB for the decoder graphs and their
330 MB of weights (fully zero-copy — 330.1 MB mmap'd, 0.0 MB copied), and
**+399 MB of encoder activations**. The front end, not the BitNet decoder,
dominates memory as well as time.

Note also that XNNPACK's `weight_cache_file_path` fails **silently** if the path
is not writable — no error, no warning, weights packed into anonymous memory
instead, and peak RssAnon goes 906 MB to 1552 MB. Check the file exists after
compiling.

End to end through an Android app, 60 s of English in 10 s windows, every pair
measured back to back on one device:

| | RTF | wall |
|---|---:|---:|
| first working version | 6.28 | 377 s |
| + big-core pinning before graph compile | 4.95 | 297 s |
| + idle GEMM workers park instead of spinning | 3.42 | 205 s |
| + wide encoder mask, batched prompt remainder | 3.23 | 194 s |
| + chat-prefix KV reused across windows | 2.93 | 176 s |
| + pause-snapped windows and a silence gate | **2.24** | **134 s** |

**2.8x, transcript byte-identical at every step.** Only the last row processes
less audio; the rest is the same work done properly.

Per 10 s window the budget is encode 14.6 s, prefill 10.3 s, decode 7.7 s. The
audio front end — **not** the BitNet part — is the largest single cost. Dropping
one of its two tokenizer encoders would halve it and does not work: the acoustic
and semantic branches are nearly orthogonal (cos 0.0435) and comparable in
magnitude, so each carries a large share of the summed features the decoder was
trained on.

BitNet shrinks the decoder's weights 4x, but on an ARMv8.0 core with no dotprod
the ternary kernel is compute-bound, so that reduction buys memory rather than
speed. Decode runs 212-249 ms/token against a ~124 ms floor set by streaming
328 MB of 2-bit weights; the LM head is only 42-46 ms/token of it.

## Fidelity

| stage | vs reference | note |
|---|---|---|
| audio front end | cosine **0.992** | vs f32; the shipped I8_S ggml build scores 0.958 |
| 28-layer decoder | cosine **0.994938** | vs a dense f32 reference, real embedding input |
| LM head | cosine **0.999421** | vs f32 |
| ternary GEMM | **bit-exact** | vs its scalar reference, every shape and thread count |

The int8 front end is *more* accurate than the ggml build it replaces, because
per-channel scales beat the single per-tensor scale I8_S uses.

## Caveats

* The encoder window is **fixed at 10 s**; longer audio must be windowed by the
  caller. Convolutions are causal, so a window needs left context and no lookahead.
  Widening it is not the free win it looks like: 30 s windows cut prompt tokens 25%
  and the encoder is linear in window length, but its activations are not free —
  peak RssAnon went 937 MB to 1739 MB and a 3.7 GB device killed the process
  mid-decode.
* The decoder graphs are **context-specific** — a ctx=128 prefill cannot be paired
  with a ctx=512 decode.
* The **chat template is mandatory**. Feeding audio features without the surrounding
  system/user/assistant turns produces fluent nonsense rather than a transcript.
* Transcript quality has been spot-checked, not benchmarked. WER against the
  reference implementation is not yet measured.
