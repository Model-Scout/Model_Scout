
---
language: 
- zh
- en
- yue
- ar
- de
- fr
- es
- pt
- id
- it
- ko
- ru
- th
- vi
- ja
- tr
- hi
- ms
- nl
- sv
- da
- fi
- pl
- cs
- fil
- fa
- el
- hu
- mk
- ro
tags:
- audio
- speech
- automatic-speech-recognition
---

license: apache-2.0
---

# OVOS - Qwen3 ASR 0.6B Q5_K_M (GGUF)

This model is a quantized gguf-format export of [Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B)
for ease of use in edge devices and CPU-based inference environments.
The original model is transformed into gguf with F16 tensors by the script [convert_hf_to_gguf.py](https://github.com/femelo/qwen3-asr.cpp/blob/main/scripts/convert_hf_to_gguf.py)
and then further quantized, if needed, using the tool [quantize](https://github.com/femelo/qwen3-asr.cpp/blob/main/src/quantize.cpp) from the same repo.

# Requirements

The requirements can be installed as

```bash
$ pip install git+https://github.com/femelo/py-qwen3-asr-cpp
```

# Usage

```python
from py_qwen3_asr_cpp.model import Qwen3ASRModel

# Initialize the model (it handles downloading from this repo)
model = Qwen3ASRModel(
    asr_model="qwen3-asr-0.6b-q5-k-m",
    n_threads=4
)

# Transcribe from file
result = model.transcribe("audio.mp3")
print(f"Detected Language: {result.language}")
print(f"Transcription: {result.text}")
```

Refer to [https://github.com/femelo/py-qwen3-asr-cpp](https://github.com/femelo/py-qwen3-asr-cpp) for more details.

# Licensing

The license is derived from the original model: Apache 2.0. For more details, please refer to [Qwen/Qwen3-ASR-0.6B](https://huggingface.co/Qwen/Qwen3-ASR-0.6B).

