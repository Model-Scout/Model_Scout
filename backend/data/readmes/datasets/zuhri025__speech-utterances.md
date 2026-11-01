---
license: cc-by-nc-sa-4.0
task_categories:
  - audio-classification
language:
  - en
  - ko
  - pt
tags:
  - non-speech
  - vocal-sounds
  - emotion
  - human-voice
  - webdataset
size_categories:
  - 10K<n<100K
configs:
  - config_name: all
    default: true
    data_files:
      - split: train
        path:
          - "NonSpeech7k/train/*.tar"
          - "NonSpeech7k/test/*.tar"
          - "VocalSound/*.tar"
          - "DeeplyNonverbalVocalization/*.tar"
          - "EmoGator/*.tar"
          - "Expresso/*.tar"
          - "VIVAE/*.tar"
  - config_name: NonSpeech7k
    data_files:
      - split: train
        path: "NonSpeech7k/train/*.tar"
      - split: test
        path: "NonSpeech7k/test/*.tar"
  - config_name: VocalSound
    data_files:
      - split: train
        path: "VocalSound/*.tar"
  - config_name: DeeplyNonverbalVocalization
    data_files:
      - split: train
        path: "DeeplyNonverbalVocalization/*.tar"
  - config_name: EmoGator
    data_files:
      - split: train
        path: "EmoGator/*.tar"
  - config_name: Expresso
    data_files:
      - split: train
        path: "Expresso/*.tar"
  - config_name: VIVAE
    data_files:
      - split: train
        path: "VIVAE/*.tar"
---

# Speech Utterances Dataset Collection

A collection of human non-speech vocal sound datasets in WebDataset format, useful for audio classification tasks involving vocal expressions, emotions, and non-verbal sounds.

## Subsets

### all (default)
All datasets concatenated together (~75k samples total).

### NonSpeech7k
- **Samples**: 7,014 (train: 6,289, test: 725)
- **Classes**: Breathing, Coughing, Crying, Laughing, Screaming, Sneezing, Yawning
- **Source**: [Zenodo](https://zenodo.org/records/6967442)
- **License**: CC BY-NC-SA 4.0

### VocalSound
- **Samples**: 21,024
- **Classes**: Laughter, Sigh, Cough, Throat clearing, Sneeze, Sniff
- **Speakers**: 3,365 from 60 countries
- **Source**: [GitHub](https://github.com/YuanGongND/vocalsound)
- **License**: CC BY-SA 4.0

### DeeplyNonverbalVocalization
- **Samples**: 726 (5% subset of full dataset)
- **Classes**: 16 (teeth-chattering, teeth-grinding, tongue-clicking, nose-blowing, coughing, yawning, throat-clearing, sighing, lip-popping, lip-smacking, panting, crying, laughing, sneezing, moaning, screaming)
- **Source**: [OpenSLR](https://www.openslr.org/99/)
- **License**: CC BY-NC-ND 4.0

### EmoGator
- **Samples**: 32,130
- **Classes**: 30 emotion categories (Adoration, Amusement, Anger, Awe, Confusion, Contempt, Contentment, Desire, Disappointment, Disgust, Distress, Ecstasy, Elation, Embarrassment, Fear, Guilt, Interest, Neutral, Pain, Pride, Realization, Relief, Romantic Love, Sadness, Serenity, Shame, Surprise Negative, Surprise Positive, Sympathy, Triumph)
- **Contributors**: 357
- **Source**: [GitHub](https://github.com/fredbuhl/EmoGator)
- **License**: Apache 2.0

### Expresso
- **Samples**: 12,293
- **Styles**: 26 expressive styles (angry, animal, awe, bored, calm, child, confused, default, desire, disgusted, enunciated, fast, fearful, happy, laughing, narration, non_verbal, projected, sad, sarcastic, singing, sleepy, sympathetic, whisper, etc.)
- **Speakers**: 4 (2 male, 2 female)
- **Source**: [Expresso](https://speechbot.github.io/expresso)
- **License**: CC BY-NC 4.0

### VIVAE
- **Samples**: 1,565
- **Emotions**: achievement, anger, fear, pain, pleasure, surprise
- **Intensity levels**: low, moderate, strong, peak
- **Speakers**: 10
- **Source**: [Zenodo](https://zenodo.org/record/4066235)
- **License**: CC BY 4.0

## Format

All datasets are stored in WebDataset format:
- **Audio**: FLAC, 48kHz, 16-bit, mono
- **Metadata**: JSON with "text" key containing labels

## Usage

```python
from datasets import load_dataset

# Load all datasets concatenated (default)
ds = load_dataset("gijs/speech-utterances")

# Load a specific subset
ds = load_dataset("gijs/speech-utterances", "Expresso")
ds = load_dataset("gijs/speech-utterances", "NonSpeech7k")

# Access individual examples
print(ds['train'][0])
```

## Citations

Please cite the original datasets when using this collection:

- **NonSpeech7k**: Rashid et al. (2023). Nonspeech7k dataset. IET Signal Processing.
- **VocalSound**: Gong et al. (2022). Vocalsound. ICASSP 2022.
- **DeeplyNonverbalVocalization**: Deeply Inc. Vocal Characterizer Dataset.
- **EmoGator**: Buhl et al. (2023). arXiv:2301.00508
- **Expresso**: Nguyen et al. (2023). EXPRESSO. INTERSPEECH 2023.
- **VIVAE**: Holz et al. (2020). VIVAE corpus. Zenodo.
