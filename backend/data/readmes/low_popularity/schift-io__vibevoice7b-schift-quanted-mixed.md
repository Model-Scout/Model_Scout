---
license: mit
base_model: microsoft/VibeVoice-ASR-Streaming-7B
tags:
- gguf
- quantized
- automatic-speech-recognition
- speaker-diarization
language:
- ko
- en
- zh
- ja
---

# VibeVoice-ASR-Streaming-7B — Mixed-Precision Quantized (6GB, self-contained)

Experimental artifact, but **self-contained**: this repo alone is enough to run real
speech-to-text with speaker diarization — no separate download of
[microsoft/VibeVoice-ASR-Streaming-7B](https://huggingface.co/microsoft/VibeVoice-ASR-Streaming-7B)
is needed. It bundles:

- `vibevoice7b-schift-quanted-mixed.gguf` — the Qwen2 text decoder + lm_head, mixed-precision
  quantized to 6GB (was ~14GB at bf16).
- `audio_components.safetensors` (2.1GB, bf16) — the acoustic tokenizer, semantic tokenizer,
  and both connectors, unmodified from the original checkpoint.
- `config.json` + tokenizer files — everything `load_full_model.py` needs to reconstruct the
  full `VibeVoiceASRForConditionalGeneration` and call `model.streaming_generate(...)` directly.

Total download: **~8.4GB**, vs. ~17GB for the original bf16 checkpoint.

## What this is

- The decoder (`language_model` + `lm_head`) was extracted from the official 7B checkpoint
  and verified to match a vanilla `Qwen2ForCausalLM` exactly (0 missing / 0 unexpected keys).
- Quantized with `llama.cpp`, mixed per-tensor-kind precision guided by a Korean imatrix
  calibration built from the model's own JSON transcription schema:
  - `ffn_gate` / `ffn_up` → Q8_0
  - `attn_k` / `attn_q` → Q4_K
  - `attn_v` / `attn_output` / `ffn_down` → IQ3_XXS
  - token embedding / output → Q8_0
- Result: **6.02 GB** decoder (vs. ~14GB at bf16), perplexity within noise of full-precision
  f16 on the calibration set (318.3 vs. 318.6).
- Audio components (tokenizers + connectors) are kept at bf16, unquantized — they're small
  (2.1GB) and this repo doesn't touch them beyond re-packaging.

## Real-audio validation (not just perplexity)

Run end-to-end through `model.streaming_generate()` on 20 real Korean broadcast-panel-discussion
utterances (AIHub, multi-speaker, continuous conversational context, character-level CER with
speaker-label tokens stripped):

| | CER |
|---|---|
| Original bf16 decoder | 19.39% |
| **This GGUF (6GB, mixed precision)** | **19.27%** |

Essentially identical — within sample noise (n=20). Quantization did not measurably
hurt recognition quality on this test.

## Speaker diarization validation

The CER numbers above strip `Speaker N:` labels before scoring — they measure content
transcription only, not diarization. Diarization was measured separately with cpCER
(concatenated minimum-permutation CER, the CHiME6/NOTSOFAR standard): text is grouped by
speaker label (hypothesis vs. ground-truth), and the hypothesis-speaker→ground-truth-speaker
mapping is searched over all permutations to find the one minimizing total CER (label IDs
are arbitrary, so this permutation-invariant matching is required).

| | cpCER (diarization + transcription combined) | Speaker-count mismatches |
|---|---|---|
| Original bf16 decoder | 37.14% | 10/20 |
| **This GGUF (6GB, mixed precision)** | **34.41%** | 10/20 |

Quantization does not measurably hurt diarization either — GGUF and original are on par
(sample-level variance is large but there's no systematic direction).

⚠️ **The base VibeVoice-7B checkpoint's own diarization is imperfect**, independent of this
quantization: on 10 of 20 samples it merges or splits the true speaker count (e.g. reports
2 speakers when there were 3). Samples where the speaker count is correct score 5-20% cpCER;
samples where it's wrong jump to 28-137%. This is a base-model characteristic this repo
inherits unchanged, not something introduced by quantization.

## Usage

```bash
pip install torch transformers safetensors gguf
pip install git+https://github.com/microsoft/VibeVoice.git   # model code (not weights)
```

```python
from huggingface_hub import snapshot_download
repo_dir = snapshot_download("schift-io/vibevoice7b-schift-quanted-mixed")

from load_full_model import load_full_model   # ships in this repo
model, processor = load_full_model(repo_dir)

# model.streaming_generate(...) — see the VibeVoice repo's
# demo/vibevoice_asr_streaming_inference_from_file.py for the full call pattern
```

`load_full_model.py` builds the architecture from `config.json`, loads the audio components
from `audio_components.safetensors`, dequantizes the GGUF decoder in pure Python
(`gguf_to_qwen2model.py`, via the `gguf` PyPI package — no `llama.cpp` binary needed), and
wires it all into one ready-to-run model. No network access to the original checkpoint
is required.

## What this is not

- Not officially supported by Microsoft. Independent experiment, shared as-is.
- Not a speaker-diarization/head-split architecture — that work is separate,
  unpublished, and still experimental (untrained/unvalidated).
- No further quantization variants (Q4_K_M, IQ2_XXS, etc. were tried and were worse;
  this mixed config was the best found).

## License

MIT, inherited from the base model (`microsoft/VibeVoice-ASR-Streaming-7B`). See `LICENSE`.
