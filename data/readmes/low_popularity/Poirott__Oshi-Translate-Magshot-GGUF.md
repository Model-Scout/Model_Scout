---
license: apache-2.0
language:
  - ja
  - en
  - zh
  - yue
  - ko
library_name: gguf
tags:
  - translation
  - subtitles
  - livestream
  - llama.cpp
base_model:
  - tencent/Hy-MT2-7B
  - tencent/Hy-MT2-1.8B
---

# Oshi Translate Magshot GGUF

Magshot is the local subtitle-translation model family used by Oshi Translate. These models are intended for short, spontaneous livestream and VOD speech, not for general chat or instruction following.

## Active and rollback artifacts

| File | Profile | Size | Recommended VRAM | SHA-256 |
|---|---|---:|---:|---|
| `Magshot-03-0813-Q4_K_M.gguf` | Active dated 7B release; adopted with documented exceptions | 4.31 GiB | 6 GiB or more | `A6C6378274BF63257D03DCFD23D85E128F49C51A61FD9C7B794A7EB89B87199F` |
| `Magshot-Lite-0826-Q4_K_M.gguf` | Active dated low-memory release; adopted with documented exceptions | 1.06 GiB | 2 GiB or more | `E0368DD3181C889FDB1BCAD69564C15FF5688768148F0BD8FA96996CBD0A83B4` |
| `Magshot-Lite-Q4_K_M.gguf` | Preserved Lite 02 rollback artifact | 1.06 GiB | 2 GiB or more | `85F21CBDDAEBA48C6C99E02469108CB27465BF5816B942F01A0E103D1A52F9B0` |
| `Magshot-03-Q4_K_M.gguf` | Preserved rollback artifact | 4.31 GiB | 6 GiB or more | `5496F70B9591ABE12B4292D46523092C90929C3B0D5BE7B097726526B71DB5DE` |

The VRAM values are user-facing guidance, not automatic selection rules. Oshi Translate lets users choose either model and saves that choice.

Magshot-03-0813 and Magshot-Lite-0826 are `adopted_with_exception`: `formal_gates_passed` is false for both. Lite 0826 improved Challenge84 chrF-lite from `41.05` to `43.56`, required-term retention from `29.63%` to `37.96%`, and reduced forbidden-term cases from `22` to `20`; its combined 116-case chrF-lite improved from `41.90` to `43.87` and required-term retention from `34.42%` to `40.26%`. Its anonymous review is incomplete, the Fixed32 paired interval is inconclusive, and per-case regressions remain. The checked distribution manifests are evidence only until the guarded publication commit succeeds. Rollback artifacts Magshot Lite 02, Magshot 03, and the 0805 snapshots remain preserved.

## Experimental 0805 snapshots

These snapshots are `review_pending`, not adopted or defaults, and failed formal mechanical gates. Do not treat either as an improvement on the stable/legacy artifacts.

| File | Status | Size | SHA-256 |
|---|---|---:|---|
| `Magshot-03-0805-Q4_K_M.gguf` | review_pending; not adopted; formal gates failed | 4.31 GiB | `36E0A2D9C0A5E5718807AA70F24AF2515A9DFA69E887FD8F0414334288C06CF0` |
| `Magshot_Lite_0805_beta-Q4_K_M.gguf` | review_pending; not adopted; formal gates failed; independent audit passed | 1.06 GiB | `79B398D020715C2FAFD06A17900DFCF73C1E28DB5A17E05F9F66FFD68CAED060` |

The published Lite beta is the checkpoint-65 artifact. A prior same-normalized local beta has SHA-256 `EEA1CC231948E05E81BEB06670326ECD037C7E1E1D5FBF8AD034B34BE4250411`; it is distinct, unadopted, and is not the published beta. The independent Lite audit does not override its failed formal gates. Sanitized manifests bind the artifacts and evaluation evidence without local paths.

## Lineage

- Magshot 03 is a fine-tuned derivative of [`tencent/Hy-MT2-7B`](https://huggingface.co/tencent/Hy-MT2-7B).
- Magshot Lite is a fine-tuned derivative of [`tencent/Hy-MT2-1.8B`](https://huggingface.co/tencent/Hy-MT2-1.8B).
- The subtitle-oriented training set was synthetically generated, filtered, and iteratively reviewed with blind human comparisons.
- Both artifacts use GGUF `Q4_K_M` quantization for llama.cpp.

## Intended use

- Real-time translation of finalized ASR segments from livestreams and VODs
- Japanese, English, Mandarin Chinese, Cantonese, and Korean translation directions supported by Oshi Translate
- Casual or polite subtitle register selected by the application

These models can mistranslate names, slang, ASR errors, incomplete speech, and domain-specific terminology. Do not use them for medical, legal, emergency, or other high-stakes translation.

## Runtime

Oshi Translate uses a fixed Hy-MT2-compatible translation prompt and sends only finalized speech text plus limited recent context. The models are not designed to answer questions or follow instructions embedded in the source dialogue.

Vulkan acceleration is supported through llama.cpp on compatible NVIDIA, AMD Radeon, and Intel GPUs. CPU fallback is available but may be slower.

## License

The upstream Hy-MT2 repositories identify their models as Apache License 2.0. These fine-tuned model artifacts are distributed under Apache License 2.0 and retain the upstream attribution and license notices.

Oshi Translate application code is separately licensed under the MIT License.
