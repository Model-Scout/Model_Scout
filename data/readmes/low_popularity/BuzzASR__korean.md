---
language: ko
license: mit
library_name: transformers
pipeline_tag: automatic-speech-recognition
base_model: openai/whisper-large-v3
tags: [automatic-speech-recognition, whisper, korean, buzzasr]
datasets: [google/fleurs]
metrics: [cer, wer]
---

# BuzzASR — Korean

A monolingual automatic speech recognition model for **Korean**, fine-tuned from
[openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3). Part of **BuzzASR**,
a suite of 102 language-specialized ASR models (Findings of EMNLP 2026).

This model uses **simple fine-tuning (Whisper's tokenizer, ASR fine-tuning only)**.

> 🏆 **State-of-the-art (open-source).** On the combined FLEURS + Common Voice test set, this model
> achieves the lowest CER of every open system we compare against: Whisper-large-v3, Omnilingual 1B/7B, MMS, Qwen3-ASR, and Cohere Transcribe.

## Results (normalized CER / WER, %)

| Test set | CER | WER | Whisper-large-v3 (zero-shot) CER |
|---|---|---|---|
| FLEURS | 5.16 | 13.22 | 5.31 |
| Common Voice 25 | 4.24 | 14.11 | 6.01 |
| Combined | 4.61 | 13.74 | 5.72 |

~1.2x CER reduction over Whisper zero-shot on the combined test set.

## Usage

```python
import torch, torchaudio
from transformers import WhisperForConditionalGeneration, WhisperProcessor

model = WhisperForConditionalGeneration.from_pretrained("BuzzASR/korean", torch_dtype=torch.float16).to("cuda").eval()
proc  = WhisperProcessor.from_pretrained("BuzzASR/korean")

wav, sr = torchaudio.load("audio.wav")           # 16 kHz mono
feats = proc(wav[0], sampling_rate=16000, return_tensors="pt").input_features.to("cuda").half()
ids = model.generate(feats, num_beams=1, no_repeat_ngram_size=3, repetition_penalty=1.2)
print(proc.batch_decode(ids, skip_special_tokens=True)[0])
```
The language/task prompt is baked into the generation config, so no `language=` argument is needed.

## Training data
[FLEURS](https://huggingface.co/datasets/google/fleurs) + **Common Voice Corpus 25.0** (Mozilla, March 2025; https://commonvoice.mozilla.org/en/datasets), capped per the paper. Text-only data from the **Goldfish** corpus (Chang et al., 2026).

## Limitations
Monolingual (Korean only). Evaluated on FLEURS / Common Voice test splits; other domains or dialects may differ.

## Citation
Project page: https://lemn-lab.github.io/buzzasr-docs/
