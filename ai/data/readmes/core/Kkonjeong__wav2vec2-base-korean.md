
---
library_name: transformers
datasets:
- kresnik/zeroth_korean
language:
- ko
metrics:
- cer
---

# Model Card for wav2vec2-base-korean

## Model Details

### Model Description

This model is a fine-tuned version of Facebook's wav2vec2-base model, adapted for Korean language recognition using the Zeroth-Korean dataset. The model has been trained to transcribe Korean speech into text, specifically utilizing the unique jamo characters of the Korean language.

- **Developed by:** [jeonghyeon Park, Jaeyoung Kim]
- **Model type:** Speech-to-Text
- **Language(s) (NLP):** Korean
- **License:** Apache 2.0
- **Finetuned from model [optional]:** facebook/wav2vec2-base

### Model Sources

- **Repository:** [github.com/KkonJJ/wav2vec2-base-korean]

## Uses

### Direct Use

The model can be directly used for transcribing Korean speech to text without additional fine-tuning. It is particularly useful for applications requiring accurate Korean language recognition such as voice assistants, transcription services, and language learning tools.

### Downstream Use [optional]

This model can be integrated into larger systems that require speech recognition capabilities, such as automated customer service, voice-controlled applications, and more.

### Out-of-Scope Use

This model is not suitable for recognizing languages other than Korean or for tasks that require understanding context beyond the transcription of spoken Korean.

## Bias, Risks, and Limitations

### Recommendations

Users should be aware of the limitations of the model, including potential biases in the training data which may affect the accuracy for certain dialects or speakers. It is recommended to evaluate the model's performance on a representative sample of the intended application domain.

## How to Get Started with the Model

To get started with the model, use the code below:

```python
!pip install transformers[torch] accelerate -U
!pip install datasets torchaudio -U
!pip install jiwer jamo
!pip install tensorboard

import torch
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torchaudio
from jamo import h2j, j2hcj

model_name = "Kkonjeong/wav2vec2-base-korean"
model = Wav2Vec2ForCTC.from_pretrained(model_name)
processor = Wav2Vec2Processor.from_pretrained(model_name)

model.to("cuda")
model.eval()

def load_and_preprocess_audio(file_path):
    speech_array, sampling_rate = torchaudio.load(file_path)
    if sampling_rate != 16000:
        resampler = torchaudio.transforms.Resample(sampling_rate, 16000)
        speech_array = resampler(speech_array)
    input_values = processor(speech_array.squeeze().numpy(), sampling_rate=16000).input_values[0]
    return input_values

def predict(file_path):
    input_values = load_and_preprocess_audio(file_path)
    input_values = torch.tensor(input_values).unsqueeze(0).to("cuda")
    with torch.no_grad():
        logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)[0]
    return transcription

audio_file_path = "your_audio_file.wav"
transcription = predict(audio_file_path)
print("Transcription:", transcription)
```

## Training Details

### Training Data

The model was trained using the Zeroth-Korean dataset, a collection of Korean speech data. This dataset includes audio recordings and their corresponding transcriptions.

### Training Procedure

#### Preprocessing

Special characters were removed from the transcriptions, and the text was converted to jamo characters to better align with the Korean language's phonetic structure.

#### Training Hyperparameters

- **Training regime:** Mixed precision (fp16)
- **Batch size:** 32
- **Learning rate:** 1e-4
- **Number of epochs:** 10

## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model was evaluated using the test split of the Zeroth-Korean dataset.

#### Metrics

The primary evaluation metric used was the Character Error Rate (CER), which measures the percentage of characters that are incorrect in the transcription compared to the reference text.

### Results

- **Final CER:** 0.073

#### Summary

The model achieved a CER of 7.3%, indicating good performance on the Zeroth-Korean dataset.

## Environmental Impact

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute).

- **Hardware Type:** NVIDIA A100
- **Hours used:** Approximately  8hours

## Technical Specifications

### Model Architecture and Objective

The model architecture is based on wav2vec2.0, designed to convert audio input into text output by modeling the phonetic structure of speech.

### Compute Infrastructure

#### Hardware

- **GPUs:** NVIDIA A100

#### Software

- **Framework:** PyTorch
- **Libraries:** Transformers, Datasets, Torchaudio, Jiwer, Jamo


**BibTeX:**

```bibtex
@misc{your_bibtex_key,
  author = {Your Name},
  title = {wav2vec2-base-korean},
  year = {2024},
  publisher = {Hugging Face},
  note = {https://huggingface.co/Kkonjeong/wav2vec2-base-korean}
}
```

**APA:**

Your Name. (2024). wav2vec2-base-korean. Hugging Face. https://huggingface.co/Kkonjeong/wav2vec2-base-korean

## Model Card Authors [optional]

[jeonghyeon Park, Jaeyoung Kim]

## Model Card Contact

For more information, contact [shshjhjh4455@gmail.com, kbs00717@gmail.com].
