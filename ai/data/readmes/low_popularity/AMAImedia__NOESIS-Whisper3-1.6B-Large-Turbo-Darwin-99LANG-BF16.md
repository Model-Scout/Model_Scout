---
license: mit
base_model:
  - openai/whisper-large-v3
  - openai/whisper-large-v3-turbo
datasets:
  - openai/whisper-multilingual
pipeline_tag: automatic-speech-recognition
language:
  - en
  - zh
  - de
  - es
  - ru
  - ko
  - fr
  - ja
  - pt
  - tr
  - pl
  - ca
  - nl
  - ar
  - sv
  - it
  - id
  - hi
  - fi
  - vi
  - he
  - uk
  - el
  - ms
  - cs
  - ro
  - da
  - hu
  - ta
  - 'no'
  - th
  - ur
  - hr
  - bg
  - lt
  - la
  - mi
  - ml
  - cy
  - sk
  - te
  - fa
  - lv
  - bn
  - sr
  - az
  - sl
  - kn
  - et
  - mk
  - br
  - eu
  - is
  - hy
  - ne
  - mn
  - bs
  - kk
  - sq
  - sw
  - gl
  - mr
  - pa
  - si
  - km
  - sn
  - yo
  - so
  - af
  - oc
  - ka
  - be
  - tg
  - sd
  - gu
  - am
  - yi
  - lo
  - uz
  - fo
  - ht
  - ps
  - tk
  - nn
  - mt
  - sa
  - lb
  - my
  - bo
  - tl
  - mg
  - as
  - tt
  - haw
  - ln
  - ha
  - ba
  - jw
  - su
tags:
  - speech-recognition
  - asr
  - multilingual
  - 99-languages
  - whisper
  - whisper-large-v3
  - whisper-large-v3-turbo
  - encoder-average
  - merge
  - noesis
  - dubbing
  - bf16
  - dhcf-fno
library_name: transformers
release_date: 2026-08-28
---

## NOESIS / AMAImedia

Released as part of the **NOESIS Professional Multilingual Dubbing Automation Platform** (framework: DHCF-FNO — Deterministic Hybrid Control Framework for Frozen Neural Operators).

- **Founder:** Ilia Bolotnikov
- **Organization:** [AMAImedia.com](https://www.amaimedia.com)
- **X (Twitter):** [@AMAImediacom](https://x.com/AMAImediacom)
- **LinkedIn:** [Ilia Bolotnikov](https://www.linkedin.com/in/ilia-bolotnikov)
- **Telegram:** [@AMAImediacom](https://t.me/AMAImediacom)
- **NOESIS version:** v15.9
- **Release date:** 2026-08-28
- **Last updated:** 2026-08-29

# NOESIS-Whisper3-1.6B-Large-Turbo-Darwin-99LANG-BF16

> **Encoder-averaged Whisper merge** of [`openai/whisper-large-v3`](https://huggingface.co/openai/whisper-large-v3) and [`openai/whisper-large-v3-turbo`](https://huggingface.co/openai/whisper-large-v3-turbo). It combines v3-full multilingual robustness with Turbo's distilled representations while keeping v3-full's 32-layer decoder for high-quality generation. This is the BF16 authoritative master copy for the NOESIS bundle.

## Use case

This model is the **multilingual ASR auxiliary** in NOESIS dubbing pipelines. It is used for language identification, word-level timestamping, validated baseline transcription, and fallback transcription for the 99 Whisper-supported languages. It loads with vanilla `transformers.WhisperForConditionalGeneration.from_pretrained` and fits comfortably on a 6 GB consumer GPU in BF16.

| Property | Value |
|---|---|
| Architecture | `WhisperForConditionalGeneration` |
| Official model class | Whisper Large-v3 / Large-v3-Turbo encoder-averaged merge |
| Actual stored parameters | **1,543,490,560 (~1.543B)** |
| Hugging Face display | **2B params** (automatic rounded display) |
| Encoder layers | 32, averaged from v3-full and Turbo with weights 0.55 / 0.45 |
| Decoder layers | 32, retained from v3-full |
| `d_model` | 1280 |
| Vocabulary | 51,866 |
| Languages | 99, multilingual |
| Format | safetensors, BF16 |
| Full repository size | **3.091 GB decimal (2.879 GiB)**; `model.safetensors` is 3.087 GB decimal |
| Estimated VRAM | Approximately 2.0 GB for BF16 inference |

## Supported languages

The bundle covers the 99-language Whisper multilingual set. The local model metadata lists the primary NOESIS operating languages as English, Russian, Chinese, Japanese, Korean, Spanish, French, German, Portuguese, Italian, Arabic, Hindi, Bengali, Turkish, Vietnamese, Thai, Indonesian, Dutch, Polish, Ukrainian, Persian, Romanian, Greek, Swedish, Hebrew, Czech, Hungarian, Finnish, Norwegian, and Danish. Whisper's tokenizer and processor files remain authoritative for the complete supported-language mapping.

## NOESIS-VC-ONE ASR family

All measurements below are from Common Voice 25.0 RU dev on an RTX 3060 6 GB, dated 2026-05-08.

| Model | Format | Size | VRAM peak | Inference | Coverage | Status |
|---|:---:|---:|---:|---|---:|:---:|
| [omniASR-CTC 300M NF4](../NOESIS-omniASR-CTC-300M-NF4) | NF4 | 0.20 GB | 0.41 GB | CER 14.81% | 1600+ languages | ✅ |
| [omniASR-CTC 1B NF4](../NOESIS-omniASR-CTC-1B-NF4) | NF4 | 0.57 GB | 0.84 GB | CER 11.11% | 1600+ languages | ✅ |
| [omniASR-CTC 3B NF4](../NOESIS-omniASR-CTC-3B-NF4) | NF4 | 1.79 GB | 2.18 GB | CER 4.63% | 1600+ languages | ✅ |
| [omniASR-CTC 7B NF4](../NOESIS-omniASR-CTC-7B-NF4) | NF4 | 3.72 GB | 4.02 GB | **CER 3.70%** | 1600+ languages | ✅ |
| **Whisper3 Darwin BF16** — this bundle | BF16 | **3.091 GB decimal (2.879 GiB)** | ~2.0 GB | WER ~5–7% RU | 99 languages | ✅ |

For primary transcription across 1600+ languages, use **omniASR-CTC 7B**. Whisper Darwin is the auxiliary path for language-ID detection, word-level timestamps, and validated high-resource-language baselines.

## Why BF16, not NF4

The bundle is intentionally kept in BF16 rather than NF4. It already fits in approximately 2 GB VRAM, runs at roughly 0.05–0.10 real-time factor, loads through the native Transformers path, and preserves decoder quality. Whisper's autoregressive decoder is more sensitive to quantization noise than CTC heads; NF4 may add approximately 0.5–1 percentage point WER. This model is the authoritative BF16 source for any future smaller variant.

If a smaller VRAM footprint is required, use an upstream Whisper V3-Turbo quantized variant instead of recompressing this merge.

## Merge strategy

| Component | Strategy | Source |
|---|---|---|
| Encoder | Per-tensor weighted average, v3-full 0.55 and Turbo 0.45 | Both upstream models |
| Decoder | Kept unchanged | `openai/whisper-large-v3` |
| Output | BF16 safetensors | NOESIS bundle |

Turbo was distilled from v3-full, so the encoder task vectors are linearly compatible. Averaging the encoders combines v3-full multilingual robustness with Turbo's distilled representations. The v3-full decoder preserves maximum generation quality with 32 layers versus Turbo's four.

The encoder-averaging recipe is documented in the provenance and citation sections below. The local deployment folder intentionally contains only the runtime files required by Transformers; no separate merge-trace JSON is shipped in this folder.

## Bundle contents

```text
.
├── README.md
├── LICENSE                         # MIT (OpenAI Whisper) + NOESIS attribution
├── model.safetensors               # BF16 weights, ~3.087 GB decimal (2.875 GiB)
├── config.json                     # WhisperForConditionalGeneration
├── generation_config.json
├── preprocessor_config.json
├── processor_config.json
├── tokenizer.json
└── tokenizer_config.json
```

This local bundle is intentionally trimmed to the files required by the shipped processor and model configuration. The original merge recipe is retained in this README; files not present in the local folder are not claimed as part of this repository.

## Quick start with Transformers

```python
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor
import torch

bundle = "B:/Downloads/Portable/NOESIS-VC-ONE/models/llm/NOESIS-3.5B-A0.5B-DUBBING-FILM/NOESIS-Whisper3-1.6B-Large-Turbo-Darwin-99LANG-BF16"
processor = AutoProcessor.from_pretrained(bundle)
model = AutoModelForSpeechSeq2Seq.from_pretrained(
    bundle,
    torch_dtype=torch.bfloat16,
    device_map="cuda:0",
)

# audio: 16 kHz mono numpy array or torch tensor
inputs = processor(audio, sampling_rate=16000, return_tensors="pt").to("cuda:0", torch.bfloat16)
with torch.no_grad():
    ids = model.generate(inputs.input_features, language="ru", task="transcribe")
text = processor.batch_decode(ids, skip_special_tokens=True)[0]
print(text)
```

## NOESIS context

In the NOESIS dubbing pipeline, this Whisper merge serves as the **multilingual ASR teacher** in knowledge-distillation runs for NOESIS ASR specialists. The averaged encoder improves soft-label quality across high-resource dubbing languages compared with either standalone Whisper variant. Production transcription uses [omniASR-CTC 7B NF4](../NOESIS-omniASR-CTC-7B-NF4); Whisper Darwin runs in parallel for language identification and timestamping.

## Sealed rules

- `R-WHISPER-FP16-AUX` — this bundle is the auxiliary BF16 ASR; the primary production route is omniASR-CTC 7B NF4.
- `R-MIT-OPENAI-PRESERVE` — the encoder-averaged derivative is redistributed under the same MIT terms as upstream OpenAI Whisper.
- `R-DUBBING-FILM-SCOPE` — this model is positioned for long-form, multi-speaker film-dubbing ASR pipelines, not only single-utterance benchmarks.

## Provenance

| Step | Source / output |
|---|---|
| Encoder source A | `openai/whisper-large-v3` — 32 layers, FP16 |
| Encoder source B | `openai/whisper-large-v3-turbo` — 32 layers, distilled |
| Decoder source | `openai/whisper-large-v3` — 32 layers, FP16 |
| Encoder merge | Per-tensor weighted average, w(v3)=0.55, w(turbo)=0.45 |
| Decoder strategy | Turbo decoder dropped; v3-full decoder kept as-is |
| Output dtype | BF16 |
| Build trace | Documented in this README; no separate trace file is included in the local folder |
| NOESIS version at merge | v14.7 (2026-04) |
| Last updated in source README | 2026-08-29 (NOESIS v15.9; BF16 rename) |

## Citation

```bibtex
@misc{radford2023whisper,
  title  = {Robust Speech Recognition via Large-Scale Weak Supervision},
  author = {Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman,
            Greg and McLeavey, Christine and Sutskever, Ilya},
  year   = {2023},
  url    = {https://openai.com/research/whisper}
}

@misc{noesis2026whisperdarwin,
  title  = {NOESIS DHCF-FNO :: Whisper3 1.6B Large Turbo Darwin (encoder-averaged merge, BF16)},
  author = {Bolotnikov, Ilia and AMAImedia},
  year   = {2026},
  note   = {Encoder-averaged merge of openai/whisper-large-v3 and
            openai/whisper-large-v3-turbo (w=0.55/0.45) with v3-full
            decoder kept; BF16 redistribution under MIT. NOESIS v15.9.},
  url    = {https://amaimedia.com}
}
```

## License

**MIT License.** Original Whisper weights © **OpenAI** (2022). Encoder-averaged merge, packaging, and NOESIS provenance © **AMAImedia (NOESIS DHCF-FNO project)**. The MIT terms apply to the upstream and derivative bundle; see `LICENSE` for the complete text.

## References

[1]: https://huggingface.co/openai/whisper-large-v3 "OpenAI Whisper large-v3"
[2]: https://huggingface.co/openai/whisper-large-v3-turbo "OpenAI Whisper large-v3-turbo"
[3]: https://openai.com/research/whisper "Robust Speech Recognition via Large-Scale Weak Supervision"

<!-- NOESIS-THEOREM-SPLIT-NOTICE 2026-05-20 -->
---
> Theorem references from the original bundle remain available under the NOESIS project documentation. The historical theorem split notice is retained here to preserve the source card's documentation marker.
<!-- /NOESIS-THEOREM-SPLIT-NOTICE -->
