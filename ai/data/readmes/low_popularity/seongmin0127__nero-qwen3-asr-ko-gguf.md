---
license: apache-2.0
language:
- ko
base_model:
- TeamUNIVA/qwen3_asr_1.7b_ko
- Qwen/Qwen3-ForcedAligner-0.6B
pipeline_tag: automatic-speech-recognition
tags:
- gguf
- crispasr
- qwen3-asr
---

# Qwen3-ASR Korean GGUF for Nero

GGUF conversions used by the Nero meeting recorder for Korean transcription after recording.
They run with the CrispASR CLI (`--backend qwen3-1.7b`, `-am` for word timestamps).
No fine-tuning or other weight changes were made beyond the format conversion and
quantization described below.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| `qwen3-asr-1.7b-ko-q8-audiof16.gguf` | 2800109184 | `e401fc3718c3802f5e20eb9c6502d407e932bc9001bb33247e08454bd01b6bd4` |
| `qwen3-forced-aligner-0.6b-q8_0.gguf` | 985594624 | `2efc3eb0db6eddb875e468e67dbc5a9ebcc840b94a583d1c336d0694cbeb7321` |

## Sources

| File | Original model | Revision |
| --- | --- | --- |
| `qwen3-asr-1.7b-ko-q8-audiof16.gguf` | [TeamUNIVA/qwen3_asr_1.7b_ko](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko) (Apache-2.0) | `ac8f5e5185a66a5caedb229ef435affdbacccf3c` |
| `qwen3-forced-aligner-0.6b-q8_0.gguf` | [Qwen/Qwen3-ForcedAligner-0.6B](https://huggingface.co/Qwen/Qwen3-ForcedAligner-0.6B) (Apache-2.0) | `c7cbfc2048c462b0d63a45797104fc9db3ad62b7` |

TeamUNIVA/qwen3_asr_1.7b_ko is a Korean fine-tune of Qwen/Qwen3-ASR-1.7B (Apache-2.0).

## Changes

Both files were produced with [CrispASR](https://github.com/CrispStrobe/CrispASR) v0.8.50
(commit `5c96e5521c6ab40ab53b91eeec54ced9c30562b5`, MIT).

1. Conversion of the original safetensors checkpoints to F16 GGUF:
   `models/convert-qwen3-asr-to-gguf.py --input <checkpoint> --output <name>-f16.gguf`
2. Quantization:
   - ASR: `crispasr-quantize qwen3-asr-1.7b-ko-f16.gguf qwen3-asr-1.7b-ko-q8-audiof16.gguf q8_0 --tensor-type '^audio\.=f16'`
     (audio encoder tensors kept at F16, all other tensors Q8_0)
   - Aligner: `crispasr-quantize qwen3-forced-aligner-0.6b-f16.gguf qwen3-forced-aligner-0.6b-q8_0.gguf q8_0`

Quantizing every tensor of the ASR model to Q8_0 dropped sentences in testing, so its
audio encoder stays at F16.

## License

Apache License 2.0, the license of both original models. See `LICENSE`. Copyright of the
original weights remains with their authors (Qwen team, Alibaba; TeamUNIVA).
