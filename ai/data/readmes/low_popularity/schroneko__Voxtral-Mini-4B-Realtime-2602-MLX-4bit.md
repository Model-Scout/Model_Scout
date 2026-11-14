---
library_name: mlx
language:
  - en
  - fr
  - es
  - de
  - ru
  - zh
  - ja
  - it
  - pt
  - nl
  - ar
  - hi
  - ko
license: apache-2.0
inference: false
base_model: mistralai/Voxtral-Mini-4B-Realtime-2602
extra_gated_description: If you want to learn more about how we process your personal
  data, please read our <a href="https://mistral.ai/terms/">Privacy Policy</a>.
pipeline_tag: automatic-speech-recognition
tags:
  - mistral-common
  - mlx
---

# schroneko/Voxtral-Mini-4B-Realtime-2602-MLX-4bit

This model [schroneko/Voxtral-Mini-4B-Realtime-2602-MLX-4bit](https://huggingface.co/schroneko/Voxtral-Mini-4B-Realtime-2602-MLX-4bit) was converted to MLX format from [mistralai/Voxtral-Mini-4B-Realtime-2602](https://huggingface.co/mistralai/Voxtral-Mini-4B-Realtime-2602) using [voxmlx](https://github.com/awni/voxmlx).

## Use with voxmlx

```bash
pip install voxmlx
```

```python
from voxmlx import transcribe

text = transcribe("audio.flac", model_path="schroneko/Voxtral-Mini-4B-Realtime-2602-MLX-4bit")
print(text)
```
