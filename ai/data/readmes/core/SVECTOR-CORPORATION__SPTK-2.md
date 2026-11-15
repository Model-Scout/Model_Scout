---
license: other
license_name: svector
license_link: LICENSE
pipeline_tag: automatic-speech-recognition
tags:
- SVECTOR
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
---

# SPTK-2

**SPTK-2** is an open multilingual automatic speech recognition (ASR) model developed by **SVECTOR**.  
It supports (after revised) 96 languages and offers improved accuracy, timestamp precision, and energy efficiency compared to previous models.

📄 Read the paper: [SPTK: A Framework for Universal Multilingual ASR (2025)](https://huggingface.co/SVECTOR-CORPORATION/SPTK-2/SPTK.pdf)

---

## 🧪 Example Usage

```python
from transformers import AutoProcessor, AutoModelForSpeechSeq2Seq
import torchaudio

processor = AutoProcessor.from_pretrained("SVECTOR-CORPORATION/SPTK-2")
model = AutoModelForSpeechSeq2Seq.from_pretrained("SVECTOR-CORPORATION/SPTK-2")

# Load and preprocess audio
audio, sr = torchaudio.load("your_audio_file.mp3")
inputs = processor(audio[0], sampling_rate=sr, return_tensors="pt")

# Generate transcription
with torch.no_grad():
    predicted_ids = model.generate(inputs.input_values)

# Decode output
print(processor.batch_decode(predicted_ids, skip_special_tokens=True))
```

---

## 📦 Model Details

- Model type: Encoder-decoder
- Architecture: E-Branchformer + Sparse MoE decoder
- Languages: 99+
- Supports transcription, translation, timestamps
- Released: April 2025

---

## 📜 License

This model is licensed under the **SVECTOR Proprietary License**.  
For research or commercial use, please contact [licence@svector.co.in](mailto:licence@svector.co.in).

---

## 🔗 Related

- 🌐 [SVECTOR Official Website](https://www.svector.co.in)