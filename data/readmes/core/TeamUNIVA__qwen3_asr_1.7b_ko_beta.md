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

<a id="en"></a>
**English** | [한국어](#ko)

> **Update:** A further-trained successor to this model is available at [`TeamUNIVA/qwen3_asr_1.7b_ko`](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko). It was initialized from this model and achieves lower error rates on Korean benchmarks, so we recommend using it for new work.

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

# The language is detected automatically. To force Korean, pass
# language="Korean" (the full language name, as expected by qwen-asr).
results = model.transcribe(
    audio="path/to/audio.wav",
)

print(results[0].text)
```

## Limitations

- This model was fine-tuned specifically for Korean speech recognition; performance on other languages may be similar to the base model or require separate validation.
- Evaluation is based on the benchmark datasets listed above; results may differ in real-world production conditions (noise, speaker variability, etc.).

---

<a id="ko"></a>
## 한국어 (Korean)

[English](#en) | **한국어**

> **안내:** 이 모델을 추가로 학습한 후속 모델이 [`TeamUNIVA/qwen3_asr_1.7b_ko`](https://huggingface.co/TeamUNIVA/qwen3_asr_1.7b_ko)에 공개되어 있습니다. 이 모델에서 초기화하여 학습했으며 한국어 벤치마크에서 더 낮은 오류율을 보이므로, 새로 사용하신다면 후속 모델을 권장합니다.

이 모델은 `Qwen/Qwen3-ASR-1.7B`를 한국어 음성 데이터로 파인튜닝한 자동 음성 인식(ASR) 모델입니다. 한국어 벤치마크 전반에서 기본(base) 모델보다 낮은 오류율을 보이며, 영어(LibriSpeech)에서의 성능 저하는 미미합니다.

## 평가 결과

한국어는 CER(문자 오류율), 영어는 WER(단어 오류율)로 측정했으며, 두 지표 모두 낮을수록 좋습니다.

| 데이터셋 | 지표 | Qwen3-ASR-1.7B (base) | 본 모델 | 변화 (%p) |
| --- | --- | --- | --- | --- |
| clova_call | CER | 0.0448 | **0.0293** | -1.55 |
| common_voice_ko | CER | 0.0719 | **0.0628** | -0.91 |
| fleurs_ko | CER | 0.0142 | **0.0138** | -0.04 |
| ksponspeech | CER | 0.0865 | **0.0670** | -1.95 |
| zeroth | CER | 0.0264 | **0.0230** | -0.34 |
| **한국어 전체** | CER | **0.0686** | **0.0537** | **-1.49** |
| librispeech (영어, 참고용) | WER | 0.0250 | 0.0246 | -0.04 |

### 평가셋

위에서 사용한 공개 한국어 벤치마크 평가셋은 모두 사람이 전수 검수했습니다. 각 발화마다 TN/ITN(텍스트 정규화 / 역정규화) 이중 전사 여부를 확인하고, 품질이 낮은 샘플은 제외하고, 오전사는 수정했습니다. 이후 모든 발화를 TN 전사와 ITN 전사 각각에 대해 평가하고, 둘 중 점수가 더 좋은 쪽을 최종 집계에 사용했습니다. 검수 후 원본 8,489건 중 8,383건이 남았습니다(106건 제외).

| 데이터셋 | 유지된 레코드 수 |
| --- | --- |
| clova_call | 1,083 |
| common_voice_ko | 564 |
| fleurs_ko | 382 |
| zeroth | 449 |
| kspon_eval_clean | 2,946 |
| kspon_eval_other | 2,959 |
| **합계** | **8,383** |

## 사용법

base 모델과 동일한 `qwen-asr` 패키지를 사용합니다.

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

# 언어는 자동으로 감지됩니다. 한국어로 고정하려면
# language="Korean"을 전달하세요(qwen-asr가 요구하는 전체 언어 이름).
results = model.transcribe(
    audio="path/to/audio.wav",
)

print(results[0].text)
```

## 한계

- 이 모델은 한국어 음성 인식에 특화되어 파인튜닝되었습니다. 다른 언어에서의 성능은 base 모델과 비슷하거나 별도 검증이 필요할 수 있습니다.
- 평가는 위에 나열한 벤치마크 데이터셋을 기준으로 하며, 실제 운영 환경(소음, 화자 편차 등)에서는 결과가 다를 수 있습니다.
