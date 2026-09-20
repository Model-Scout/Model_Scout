---
language:
- ko
license: mit
library_name: transformers
tags:
- whisper
- automatic-speech-recognition
- korean
- disfluency-detection
- speech
- asr
base_model: openai/whisper-large-v3-turbo
pipeline_tag: automatic-speech-recognition
model-index:
- name: SeloWhisper-ko-disfluency
  results:
  - task:
      type: automatic-speech-recognition
      name: Korean ASR with Disfluency Detection
    dataset:
      type: korean-conversational-speech
      name: Held-out clean set
    metrics:
    - type: cer
      value: 0.1653
    - type: wer
      value: 0.3300
    - type: f1
      value: 0.8792
      name: Disfluency F1
  - task:
      type: automatic-speech-recognition
      name: Korean ASR with Disfluency Detection
    dataset:
      type: korean-conversational-speech
      name: Held-out noisy set
    metrics:
    - type: cer
      value: 0.1529
    - type: wer
      value: 0.3558
    - type: f1
      value: 0.9226
      name: Disfluency F1
---

# SeloWhisper-ko-disfluency

Korean ASR with inline disfluency detection, fine-tuned from [`openai/whisper-large-v3-turbo`](https://huggingface.co/openai/whisper-large-v3-turbo).

Transcribes Korean speech while emitting 10 special tokens for fillers, repetitions, and laughter directly inside the transcript.

> **Note.** Methodology, training data, and analysis are reserved for an upcoming paper. This repository releases only the model weights and the inference recipe.

---

## Model Specification

| | |
|---|---|
| Base model | `openai/whisper-large-v3-turbo` |
| Architecture | Whisper encoder–decoder (encoder 32 L / decoder 4 L, d_model 1280) |
| Parameters | ~809 M |
| Vocabulary | 51,867 base + 10 disfluency tokens + dedicated `<\|pad\|>` |
| Language | Korean (`ko`) |
| Sampling rate | 16 kHz, mono |
| Max target length | 448 tokens |
| Released checkpoint | step 2,500 (selected by held-out disfluency F1) |

---

## Disfluency Tokens

| Token | Korean cue | Meaning |
|---|---|---|
| `<ah>`  | 아 | filler "ah" |
| `<uh>`  | 어 | filler "uh" |
| `<um>`  | 음 | filler "um" |
| `<gue>` | 그 | filler "geu" |
| `<jeo>` | 저 | filler "jeo" |
| `<mwo>` | 뭐 | filler "mwo" |
| `<mak>` | 막 | filler "mak" |
| `<repeat>` | — | repeated word / syllable |
| `<laugh>`  | — | laughter |
| `<other>`  | — | other disfluency |

Tokens are registered as `additional_special_tokens`. A dedicated `<|pad|>` token is introduced so EOS is preserved during label masking.

---

## Usage

```python
import torch, torchaudio
from transformers import WhisperProcessor, WhisperForConditionalGeneration

MODEL_ID = "rearleg/SeloWhisper-ko-disfluency"

processor = WhisperProcessor.from_pretrained(MODEL_ID)
model = WhisperForConditionalGeneration.from_pretrained(MODEL_ID).eval()

device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

waveform, sr = torchaudio.load("sample.wav")
if sr != 16000:
    waveform = torchaudio.functional.resample(waveform, sr, 16000)
    sr = 16000
if waveform.shape[0] > 1:
    waveform = waveform.mean(dim=0, keepdim=True)

inputs = processor(
    waveform.squeeze().numpy(),
    sampling_rate=sr,
    return_tensors="pt",
).to(device)

with torch.no_grad():
    generated = model.generate(
        inputs["input_features"],
        max_length=448,
        num_beams=1,
        do_sample=False,
    )

# Keep special tokens so disfluencies remain visible
transcription = processor.batch_decode(generated, skip_special_tokens=False)[0]
print(transcription)
```

**Decode with `skip_special_tokens=False`** to keep disfluency tags visible. Strip Whisper meta tokens (`<|ko|>`, `<|transcribe|>`, `<|notimestamps|>`, `<|endoftext|>`) manually if you only want the disfluency annotations.

This release ships a `generation_config.json` with `forced_decoder_ids`, `suppress_tokens`, and `begin_suppress_tokens` already cleared — no extra unsetting is required at inference time.

---

## Performance (checkpoint-2500)

Evaluated on held-out Korean conversational speech.

| Split | CER | WER | sWER | sCER | Filler P | Filler R | **Filler F1** |
|---|---|---|---|---|---|---|---|
| Clean | 0.1653 | 0.3300 | 0.3785 | 0.1250 | 0.9118 | 0.8488 | **0.8792** |
| Noisy | 0.1529 | 0.3558 | 0.4391 | 0.1224 | 0.9420 | 0.9039 | **0.9226** |

**Metric definitions**

- **CER** — character error rate, whitespace included.
- **WER** — word error rate. Each disfluency token is treated as a single unit (substituted to a single private-use character during scoring) to avoid penalty inflation.
- **sWER** — WER after whitespace normalization, anchoring hypothesis spacing to the reference.
- **sCER** — CER on whitespace-stripped syllable streams (Korean-specific).
- **Filler P / R / F1** — counter-based across the 10 disfluency tokens: TP = `min(ref_count, hyp_count)` per token, summed globally; FP / FN computed symmetrically.

---

## Limitations

- Optimized for Korean spontaneous speech; not tuned for broadcast news, code-switching, or non-Korean speech.
- Like all Whisper-family models, hallucination is possible on silent or very short clips — a VAD or RMS-based silence filter upstream is recommended.

---

## License

MIT — see `LICENSE` for the full text.

---

## Citation

```bibtex
@misc{cheon2025selowhisper,
  title        = {SeloWhisper-ko-disfluency: Korean ASR with Inline Disfluency Detection},
  author       = {Cheon, Changhyun},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/rearleg/SeloWhisper-ko-disfluency}}
}
```

Whisper:

```bibtex
@article{radford2022whisper,
  title   = {Robust Speech Recognition via Large-Scale Weak Supervision},
  author  = {Radford, Alec and Kim, Jong Wook and Xu, Tao and Brockman, Greg
             and McLeavey, Christine and Sutskever, Ilya},
  journal = {arXiv preprint arXiv:2212.04356},
  year    = {2022}
}
```
