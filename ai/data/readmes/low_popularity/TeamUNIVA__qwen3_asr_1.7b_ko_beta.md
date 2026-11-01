---
language:
- ko
license: apache-2.0
base_model: Qwen/Qwen3-ASR-1.7B
pipeline_tag: automatic-speech-recognition
tags:
- automatic-speech-recognition
- speech
- korean
- qwen3-asr
---

# TeamUNIVA/qwen3_asr_1.7b_ko_beta

This model is a fine-tune of `Qwen/Qwen3-ASR-1.7B` on Korean speech data for automatic speech recognition (ASR). It achieves lower error rates than the base model across Korean benchmarks, with negligible degradation on English (LibriSpeech).

## Evaluation Results

Korean scores are measured in CER (Character Error Rate); the English score is measured in WER (Word Error Rate). Lower is better for both metrics.

| Dataset | Metric | Qwen3-ASR-1.7B (base) | This model | Change (%p) |
| --- | --- | --- | --- | --- |
| clova_call | CER | 0.0448 | **0.0293** | -1.55 |
| common_voice_ko | CER | 0.0719 | **0.0628** | -0.91 |
| fleurs_ko | CER | 0.0142 | **0.0138** | -0.04 |
| ksponspeech | CER | 0.0865 | **0.0670** | -1.95 |
| zeroth | CER | 0.0264 | **0.0230** | -0.34 |
| **Korean total** | CER | **0.0686** | **0.0537** | **-1.49** |
| librispeech (English, reference) | WER | 0.0250 | 0.0246 | -0.04 |

### Evaluation Set

All open Korean benchmark evaluation sets used above were fully reviewed by hand: each utterance was checked for dual TN/ITN (text normalization / inverse text normalization) transcripts, low-quality samples were filtered out, and mis-transcriptions were corrected. Every utterance was then evaluated against both the TN and ITN transcripts, and the better-scoring transcript of the pair was used for the final aggregated result. After this review, 8,383 of the original 8,489 records were retained (106 excluded):

| Dataset | Retained records |
| --- | --- |
| clova_call | 1,083 |
| common_voice_ko | 564 |
| fleurs_ko | 382 |
| zeroth | 449 |
| kspon_eval_clean | 2,946 |
| kspon_eval_other | 2,959 |
| **Total** | **8,383** |

## Usage

Uses the same `qwen-asr` package as the base model.

```bash
pip install -U qwen-asr
```

```python
import torch
from qwen_asr import Qwen3ASRModel

model = Qwen3ASRModel.from_pretrained(
    "TeamUNIVA/qwen3_asr_1.7b_ko_beta",
    dtype=torch.bfloat16,
    device_map="cuda:0",
    max_inference_batch_size=32,
    max_new_tokens=256,
)

results = model.transcribe(
    audio="path/to/audio.wav",
    language="ko",
)

print(results[0].text)
```

## Limitations

- This model was fine-tuned specifically for Korean speech recognition; performance on other languages may be similar to the base model or require separate validation.
- Evaluation is based on the benchmark datasets listed above; results may differ in real-world production conditions (noise, speaker variability, etc.).
