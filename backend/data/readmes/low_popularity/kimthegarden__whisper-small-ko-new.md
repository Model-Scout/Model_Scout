---
license: mit
language:
- ko
metrics:
- cer
base_model:
- SungBeom/whisper-small-ko
- kimthegarden/whisper-korean-stt-v2-250626
pipeline_tag: automatic-speech-recognition
---
# Model Card for whisper-small-ko-finetuned

This is a fine-tuned version of the [`SungBeom/whisper-small-ko`](https://huggingface.co/SungBeom/whisper-small-ko) model on a custom Korean speech recognition dataset.  
It performs automatic speech recognition (ASR) for Korean audio data and achieves strong performance on the validation set.

---

## Model Details

### Model Description

This model is based on the Whisper-small architecture and fine-tuned on 62,327 Korean audio-transcript pairs using Hugging Face Transformers and PyTorch.  
It is designed for general-domain Korean speech recognition (conversational, broadcast, news, etc.).

- **Developed by:** [Jeongwon Kim]
- **Shared by:** [kimthegarden]
- **Model type:** Encoder-decoder Transformer (WhisperForConditionalGeneration)
- **Language(s):** Korean (`ko`)
- **License:** MIT
- **Fine-tuned from model:** `SungBeom/whisper-small-ko`

---

## Model Sources

- **Repository:** [https://huggingface.co/kimthegarden/whisper-small-ko-low-qual-voice]
- **Notebook:** Fine-tuned using a custom `whisper_finetuning.ipynb`
- **Demo [optional]:** [Gradio or Streamlit demo link if available]

---

## Uses

### Direct Use

- Korean automatic speech recognition (ASR)
- Offline or batch transcription of Korean speech data
- Integration into Korean-language voice assistant systems

### Downstream Use

- Further fine-tuning on domain-specific datasets (e.g. legal, medical, education)
- Research into Korean ASR model robustness or multilingual Whisper models

### Out-of-Scope Use

- Transcription of non-Korean speech (this model is Korean-only)
- Real-time streaming ASR (not latency-optimized)
- Zero-shot or few-shot adaptation to other languages

---

## Bias, Risks, and Limitations

- The model may show reduced accuracy on:
  - Regional dialects or accents not represented in the training data
  - Very noisy environments
  - Children’s speech or non-native pronunciation
- The model has not been tested for fairness across different speakers (gender, age, etc.)

### Recommendations

We recommend testing the model on your specific data domain before deployment.  
Additional fine-tuning or data filtering may be required for sensitive use cases (e.g. education, healthcare).

---

## How to Get Started with the Model

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch

model = WhisperForConditionalGeneration.from_pretrained("your-username/whisper-small-ko-finetuned")
processor = WhisperProcessor.from_pretrained("your-username/whisper-small-ko-finetuned")

# Input: 16kHz waveform (float32 numpy or tensor)
inputs = processor(audio_waveform, sampling_rate=16000, return_tensors="pt")

with torch.no_grad():
    predicted_ids = model.generate(inputs.input_features)

transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
print(transcription[0])
```

---
## Contact
jwk20001007@gmail.com