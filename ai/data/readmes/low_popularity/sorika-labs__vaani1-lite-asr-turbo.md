---
language:
- hi
- en
- zh
- ja
- ko
- es
- fr
- de
- ru
- ar
- bn
- ta
- te
- mr
- gu
- ur
- kn
- ml
- pa
- multilingual
license: mit
tags:
- audio
- automatic-speech-recognition
- speech-recognition
- faster-whisper
- ctranslate2
- multilingual
- hindi
- chinese
- japanese
- korean
- indic
- vaani
- sorika-labs
datasets:
- ai4bharat/kathbath
- google/fleurs
metrics:
- wer
- cer
model-index:
- name: Vaani1-Lite-ASR-Turbo
  results:
  - task:
      type: automatic-speech-recognition
      name: Speech Recognition
    dataset:
      name: AI4Bharat Kathbath Hindi Valid
      type: ai4bharat/kathbath
    metrics:
    - type: wer
      value: 12.68
      name: WER
    - type: cer
      value: 5.76
      name: CER
---

# ⚡ Vaani1-Lite-ASR-Turbo (Multilingual)
### High-Speed Production Engine by **Sorika Labs**
**CTranslate2 (faster-whisper) format of [`sorika-labs/vaani1-lite-asr`](https://huggingface.co/sorika-labs/vaani1-lite-asr)**

`Vaani1-Lite-ASR-Turbo` is the official CTranslate2-optimized release of the **Vaani1-Lite-ASR** model. It provides **4x-5x faster inference**, cuts memory consumption by **50% (only ~484MB)**, and delivers real-time speech-to-text with latency under **150ms** across **99+ languages** (Hindi, English, Chinese, Japanese, Korean, Spanish, etc.).

---

## 🌍 Multilingual Capabilities

- **Hindi (`hi`):** SOTA fine-tuned accuracy (**12.68% WER**, beats Whisper-Large-v3).
- **English (`en`):** **3.70% WER** (Zero catastrophic forgetting).
- **East Asian (`zh`, `ja`, `ko`):** Full transcription support for Chinese, Japanese, and Korean.
- **Indic Languages:** Bengali, Tamil, Telugu, Marathi, Gujarati, Urdu, Kannada, Malayalam, Punjabi.
- **Auto-Detection:** Automatically identifies the spoken language from audio.

---

## 🚀 Quickstart: Real-Time Transcription

Install `faster-whisper`:
```bash
pip install faster-whisper
```

Transcribe with Python:
```python
from faster_whisper import WhisperModel

# Load the turbo model on CPU (uses ~250MB RAM)
model = WhisperModel("sorika-labs/vaani1-lite-asr-turbo", device="cpu", compute_type="int8")

# Transcribe Hindi, English, Chinese, Korean, or Auto-Detect:
segments, info = model.transcribe("sample_audio.wav", vad_filter=True)

print(f"Detected Language: {info.language} ({info.language_probability:.2f})")
for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
```

---

## 🔗 Models in this Family

| Model | Format | Best For | Link |
| :--- | :--- | :--- | :--- |
| **`Vaani1-Lite-ASR`** | PyTorch / Transformers | Fine-tuning, PyTorch pipelines, Colab demo | [Hugging Face](https://huggingface.co/sorika-labs/vaani1-lite-asr) |
| **`Vaani1-Lite-ASR-Turbo`** | CTranslate2 / INT8 / FP16 | Production APIs, Web Apps, Edge & Real-time bots | [Hugging Face](https://huggingface.co/sorika-labs/vaani1-lite-asr-turbo) |

---

## 📜 License & Developer

- **License:** MIT (Permissive open source)
- **Developer:** Sorika Labs
