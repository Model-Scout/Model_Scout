---
library_name: peft
license: apache-2.0
base_model: openai/whisper-large-v3-turbo
language:
- ko
tags:
- automatic-speech-recognition
- asr
- korean
- medical
- surgical
- operating-room
- whisper
- lora
- peft
datasets:
- vitaldb/synthetic-k-or-speech-audio
metrics:
- cer
pipeline_tag: automatic-speech-recognition
---

# Whisper-large-v3-turbo Korean OR Speech LoRA

LoRA adapter for [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) fine-tuned on **Synthetic K-OR Speech Audio v1**, a Korean operating-room speech corpus.

## Results

Test split: 800 clips (200 utterances × 4 voices, utterance-id stratified, seed 20260503).

| ASR | CER | vs Whisper baseline |
|---|---|---|
| Qwen3-ASR-1.7B + LoRA | 0.0334 | -59.8% |
| **Whisper-v3-turbo + this adapter** | **0.0431** | **-48.0%** |
| Whisper-v3-turbo + this adapter + Hotwords | 0.0483 | -41.8% |
| Whisper-v3-turbo + Hotwords (no LoRA) | 0.0790 | -4.7% |
| Whisper-v3-turbo (baseline) | 0.0829 | — |

CER by code-switching style:

| cs_style | Baseline | This adapter |
|---|---|---|
| `none` (pure Korean) | 0.041 | 0.028 |
| `phonetic_kr` (음차) | 0.076 | 0.031 |
| `mixed` (KR+EN) | 0.132 | 0.074 |
| `english` | 0.462 | 0.308 |

## Usage

```bash
pip install transformers peft librosa
```

```python
import torch, librosa
from peft import PeftModel
from transformers import WhisperForConditionalGeneration, WhisperProcessor

base = "openai/whisper-large-v3-turbo"
adapter = "vitaldb/whisper-v3-turbo-kor-or-lora"

processor = WhisperProcessor.from_pretrained(base, language="ko", task="transcribe")
model = WhisperForConditionalGeneration.from_pretrained(base, torch_dtype=torch.bfloat16)
model = PeftModel.from_pretrained(model, adapter).to("cuda").eval()
forced = processor.get_decoder_prompt_ids(language="ko", task="transcribe")

y, _ = librosa.load("clip.wav", sr=16000, mono=True)
feats = processor(y, sampling_rate=16000, return_tensors="pt").input_features.to("cuda", dtype=torch.bfloat16)
with torch.no_grad():
    gen = model.generate(input_features=feats, max_new_tokens=128, forced_decoder_ids=forced)
text = processor.tokenizer.batch_decode(gen, skip_special_tokens=True)[0].strip()
print(text)
```

**Note**: hotwords (Whisper `prompt_ids`) on top of this adapter degrades CER (+12% relative). Do not combine.

## Training

- **Base model**: openai/whisper-large-v3-turbo (MIT-licensed)
- **Trainable params**: 13.9M / 822.8M (1.69%)
- **Target modules**: `q_proj`, `k_proj`, `v_proj`, `out_proj`, `fc1`, `fc2`
- **LoRA rank / alpha / dropout**: 16 / 32 / 0.05
- **Optimizer**: AdamW, learning rate 1e-4, warmup 100 steps
- **Schedule**: 3 epochs, batch 4 × grad_accum 4 (effective 16), bf16, gradient checkpointing
- **Hardware**: NVIDIA RTX 4090 24 GB
- **Train time**: ~18 minutes
- **Train data**: 6,400 clips (1,600 utterances × 4 voices) from Synthetic K-OR Speech Audio v1

## Dataset

Trained on Synthetic K-OR Speech Audio v1 — 8,000 audio clips (2,000 utterances × 4 voice profiles) synthesized from Synthetic K-OR Speech Corpus v1.0 text via Qwen3-TTS.

## Limitations

- Trained on **synthetic** TTS audio, not real OR recordings.
- Single-institution lexicon (SNUH conventions).
- Apply with caution to truly out-of-distribution audio.

## License

Apache-2.0.

## Citation

```bibtex
@misc{kor_or_whisper_lora_2026,
  title  = {Whisper-large-v3-turbo Korean OR Speech LoRA Adapter},
  author = {VitalDB / Seoul National University Hospital, Department of Anesthesiology and Pain Medicine},
  year   = {2026},
  publisher = {Hugging Face},
  url    = {https://huggingface.co/vitaldb/whisper-v3-turbo-kor-or-lora}
}
```

## Acknowledgement

This work was supported by the Korea ARPA-H Project through the Korea Health Industry Development Institute (KHIDI), funded by the Ministry of Health and Welfare, Republic of Korea (Grant No. 2460006561).
