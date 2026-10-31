---
license: cc-by-nc-4.0
language:
- en
- ms
- zh
- ru
- id
- ar
- ja
- ko
multilinguality:
- multilingual
task_categories:
- automatic-speech-recognition
- translation
---

# Multi-Language Dialogue Episodes Dataset

## Dataset Description

This dataset contains dialogue episodes with multi-language transcripts and separated speaker audio.

### Features

- **24,076 dialogue segments** from 138 videos
- **Multi-language transcripts** in 9 languages
- **Separated speakers** - 2-channel audio
- **Multi-channel audio** - stereo WAV files (24kHz)

### Usage

```python
from datasets import load_dataset

ds = load_dataset("khursanirevo/dialogue-episodes")
sample = ds["train"][0]

# Play audio
from IPython.display import Audio
Audio(sample["audio"]["array"], rate=sample["audio"]["sampling_rate"])
```

## License

CC-BY-NC-4.0
