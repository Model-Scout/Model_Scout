---
language: 
- id
- jv
- sun
datasets:
- mozilla-foundation/common_voice_7_0
- openslr
- magic_data
- titml
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- hf-asr-leaderboard
- id
- jv
- robust-speech-event
- speech
- su
license: apache-2.0
model-index:
- name: Wav2Vec2 Indonesian Javanese and Sundanese by Indonesian NLP
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 6.1
      type: common_voice
      args: id
    metrics:
    - name: Test WER
      type: wer
      value: 4.056
    - name: Test CER
      type: cer
      value: 1.472
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: id
    metrics:
    - name: Test WER
      type: wer
      value: 4.492
    - name: Test CER
      type: cer
      value: 1.577
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: id
    metrics:
    - name: Test WER
      type: wer
      value: 48.94
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: id
    metrics:
    - name: Test WER
      type: wer
      value: 68.95
---

# Multilingual Speech Recognition for Indonesian Languages

This is the model built for the project 
[Multilingual Speech Recognition for Indonesian Languages](https://github.com/indonesian-nlp/multilingual-asr).
It is a fine-tuned [facebook/wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53)
model on the [Indonesian Common Voice dataset](https://huggingface.co/datasets/common_voice), 
[High-quality TTS data for Javanese - SLR41](https://huggingface.co/datasets/openslr), and
[High-quality TTS data for Sundanese - SLR44](https://huggingface.co/datasets/openslr) datasets.

We also provide a [live demo](https://huggingface.co/spaces/indonesian-nlp/multilingual-asr) to test the model.

When using this model, make sure that your speech input is sampled at 16kHz.

## Usage
The model can be used directly (without a language model) as follows:
```python
import torch
import torchaudio
from datasets import load_dataset
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

test_dataset = load_dataset("common_voice", "id", split="test[:2%]")

processor = Wav2Vec2Processor.from_pretrained("indonesian-nlp/wav2vec2-indonesian-javanese-sundanese")
model = Wav2Vec2ForCTC.from_pretrained("indonesian-nlp/wav2vec2-indonesian-javanese-sundanese")

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the aduio files as arrays
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(speech_array).squeeze().numpy()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)
inputs = processor(test_dataset[:2]["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

with torch.no_grad():
    logits = model(inputs.input_values, attention_mask=inputs.attention_mask).logits

predicted_ids = torch.argmax(logits, dim=-1)

print("Prediction:", processor.batch_decode(predicted_ids))
print("Reference:", test_dataset[:2]["sentence"])
```


## Evaluation

The model can be evaluated as follows on the Indonesian test data of Common Voice.

```python
import torch
import torchaudio
from datasets import load_dataset, load_metric
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import re

test_dataset = load_dataset("common_voice", "id", split="test")
wer = load_metric("wer")

processor = Wav2Vec2Processor.from_pretrained("indonesian-nlp/wav2vec2-indonesian-javanese-sundanese")
model = Wav2Vec2ForCTC.from_pretrained("indonesian-nlp/wav2vec2-indonesian-javanese-sundanese") 
model.to("cuda")

chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\'\”\�]'

resampler = torchaudio.transforms.Resample(48_000, 16_000)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def speech_file_to_array_fn(batch):
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower()
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = resampler(speech_array).squeeze().numpy()
    return batch

test_dataset = test_dataset.map(speech_file_to_array_fn)

# Preprocessing the datasets.
# We need to read the audio files as arrays
def evaluate(batch):
    inputs = processor(batch["speech"], sampling_rate=16_000, return_tensors="pt", padding=True)

    with torch.no_grad():
        logits = model(inputs.input_values.to("cuda"), attention_mask=inputs.attention_mask.to("cuda")).logits

    pred_ids = torch.argmax(logits, dim=-1)
    batch["pred_strings"] = processor.batch_decode(pred_ids)
    return batch

result = test_dataset.map(evaluate, batched=True, batch_size=8)

print("WER: {:2f}".format(100 * wer.compute(predictions=result["pred_strings"], references=result["sentence"])))
```

**Test Result**: 11.57 %

## Training

The Common Voice `train`, `validation`, and ... datasets were used for training as well as ... and ...  # TODO

The script used for training can be found [here](https://github.com/cahya-wirawan/indonesian-speech-recognition) 
(will be available soon)
