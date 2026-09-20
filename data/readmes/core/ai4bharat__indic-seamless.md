---
license: cc-by-nc-4.0
library_name: transformers
datasets:
- ai4bharat/NPTEL
- ai4bharat/IndicVoices-ST
- ai4bharat/WordProject
- ai4bharat/Spoken-Tutorial
- ai4bharat/Mann-ki-Baat
- ai4bharat/Vanipedia
- ai4bharat/UGCE-Resources
pipeline_tag: automatic-speech-recognition
language:
- en
- as
- bn
- gu
- hi
- ta
- te
- ur
- kn
- ml
- mr
- sd
- ne
---
# IndicSeamless for Speech-to-Text Translation

<a target="_blank" href="https://huggingface.co/spaces/ai4bharat/indic-seamless">
  <img src="https://huggingface.co/datasets/huggingface/badges/raw/main/open-in-hf-spaces-sm.svg" alt="Open in HuggingFace"/>
</a>

## Model Overview
This repository hosts the **IndicSeamless** model which is a SeamlessM4T-v2 finetuned on the **BhasaAnuvaad** dataset for **speech-to-text translation (STT)** across **Indian languages**. The dataset was filtered using the following thresholds before training:

- **Alignment Score**: 0.8
- **Mining Score**: 0.6

### Performance Highlights
- The model **outperforms the base SeamlessM4Tv2 model** and all competing STT systems, including cascaded approaches.
- It **achieves a new SOTA on Fleurs and significantly surpasses all other systems on the BhasaAnuvaad test set, which includes a diverse range of data from new domains.**

## Model Usage
### Installation
Ensure you have the required dependencies installed:
```bash
pip install torch torchaudio transformers datasets
```

### Loading the Model
```python
import torchaudio
from transformers import SeamlessM4Tv2ForSpeechToText
from transformers import SeamlessM4TTokenizer, SeamlessM4TFeatureExtractor

model = SeamlessM4Tv2ForSpeechToText.from_pretrained("ai4bharat/indic-seamless").to("cuda")
processor = SeamlessM4TFeatureExtractor.from_pretrained("ai4bharat/indic-seamless")
tokenizer = SeamlessM4TTokenizer.from_pretrained("ai4bharat/indic-seamless")
```

### Single Audio Inference
```python
audio, orig_freq = torchaudio.load("../10002398547238927970.wav")
audio = torchaudio.functional.resample(audio, orig_freq=orig_freq, new_freq=16_000) # must be a 16 kHz waveform array
audio_inputs = processor(audio, sampling_rate=16_000, return_tensors="pt").to("cuda")

text_out = model.generate(**audio_inputs, tgt_lang="hin")[0].cpu().numpy().squeeze()
print(tokenizer.decode(text_out, clean_up_tokenization_spaces=True, skip_special_tokens=True))
```

### Inference on Fleurs Dataset
```python
from datasets import load_dataset

dataset = load_dataset("google/fleurs", "hi_in", split="test")

def process_audio(example):
    audio = example["audio"]["array"]
    audio_inputs = processor(audio, sampling_rate=16_000, return_tensors="pt").to("cuda")
    text_out = model.generate(**audio_inputs, tgt_lang="hin")[0].cpu().numpy().squeeze()
    return {"predicted_text": tokenizer.decode(text_out, clean_up_tokenization_spaces=True, skip_special_tokens=True)}

dataset = dataset.map(process_audio)
dataset = dataset.remove_columns(["audio"])
dataset.to_csv("fleurs_hi_predictions.csv")
```

### Batch Translation using Fleurs
```python
from datasets import load_dataset
import torch

def process_batch(batch):
    audio_arrays = [audio["array"] for audio in batch["audio"]]
    audio_inputs = processor(audio_arrays, sampling_rate=16_000, return_tensors="pt", padding=True).to("cuda")
    text_outs = model.generate(**audio_inputs, tgt_lang="hin")
    batch["predicted_text"] = [tokenizer.decode(text_out.cpu().numpy().squeeze(), clean_up_tokenization_spaces=True, skip_special_tokens=True) for text_out in text_outs]
    return batch

def batch_translate(language_code="hi_in", tgt_lang="hin"):
    dataset = load_dataset("google/fleurs", language_code, split="test")
    dataset = dataset.map(process_batch, batched=True, batch_size=8)
    return dataset["predicted_text"]

# Example usage
target_language = "hi_in"
translations = batch_translate(target_language, tgt_lang="hin")
print(translations)
```

## Citation

If you use BhasaAnuvaad in your work, please cite us:

```bibtex
@misc{jain2024bhasaanuvaadspeechtranslationdataset,
      title={BhasaAnuvaad: A Speech Translation Dataset for 13 Indian Languages}, 
      author={Sparsh Jain and Ashwin Sankar and Devilal Choudhary and Dhairya Suman and Nikhil Narasimhan and Mohammed Safi Ur Rahman Khan and Anoop Kunchukuttan and Mitesh M Khapra and Raj Dabre},
      year={2024},
      eprint={2411.04699},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.04699}, 
}
```


## License

This model is released under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license.