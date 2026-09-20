---
license: cc-by-nc-4.0
base_model:
- Qwen/Qwen3-1.7B
- google/siglip2-so400m-patch16-384
library_name: transformers
tags:
- multimodal
- OCR
- ncsoft
- ncai
- varco
pipeline_tag: image-text-to-text
language:
- en
- ko
---

# VARCO-VISION-2.0-1.7B-OCR

<div align="center">
   <img src="./varco-vision.png" width="100%" style="background-color:white; padding:10px;" />
</div>

## Introduction
**VARCO-VISION-2.0-1.7B-OCR** is a lightweight yet powerful OCR-specialized model derived from VARCO-VISION-2.0-1.7B, designed to deliver efficient and accurate text recognition in real-world scenarios. Unlike conventional vision-language models (VLMs) that primarily focus on transcribing visible text, this model performs both recognition and spatial localization by detecting bounding boxes around each character, enabling structured, layout-aware OCR outputs.

The model supports both Korean and English, making it well-suited for multilingual environments where mixed-script documents are common. Each recognized character is paired with its precise position in the image, formatted as `<char>{characters}</char><bbox>{x1}, {y1}, {x2}, {y2}</bbox>`, where the coordinates correspond to the top-left (`x1`, `y1`) and bottom-right (`x2`, `y2`) corners of the character's bounding box.

While VARCO-VISION-2.0-14B demonstrates strong OCR capabilities as part of its broader multimodal reasoning skills, deploying such a large model for single-task use cases can be computationally inefficient. VARCO-VISION-2.0-1.7B-OCR addresses this with a task-optimized design that retains high accuracy while significantly reducing resource requirements, making it ideal for real-time or resource-constrained applications.

![image/gif](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B-OCR/resolve/main/examples.gif)

## 🚨News🎙️
- 📝 2025-09-12: We published the technical report of VARCO-VISION-2.0 at [link](https://arxiv.org/abs/2509.10105)
- 🛠️ 2025-08-22: We updated the checkpoint of VARCO-VISION-2.0-1.7B for improved performance.
- 📰 2025-07-28: We released VARCO-VISION-2.0-1.7B-OCR at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B-OCR)
- 📰 2025-07-28: We released VARCO-VISION-2.0-1.7B at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B)
- 🛠️ 2025-07-18: We updated the checkpoint of VARCO-VISION-2.0-14B for improved performance.
- 📰 2025-07-16: We released VARCO-VISION-2.0-14B at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-14B)
- 📰 2025-07-16: We released GME-VARCO-VISION-Embedding at [link](https://huggingface.co/NCSOFT/GME-VARCO-VISION-Embedding)

## VARCO-VISION-2.0 Family
| Model Name                 | Base Models (Vision / Language)                                                                                                               | HF Link                                                          |
| :------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------: |
| VARCO-VISION-2.0-14B       | [siglip2-so400m-patch16-384](https://huggingface.co/google/siglip2-so400m-patch16-384) / [Qwen3-14B ](https://huggingface.co/Qwen/Qwen3-14B)  | [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-14B)       |
| VARCO-VISION-2.0-1.7B      | [siglip2-so400m-patch16-384](https://huggingface.co/google/siglip2-so400m-patch16-384) / [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B)      |
| VARCO-VISION-2.0-1.7B-OCR  | [siglip2-so400m-patch16-384](https://huggingface.co/google/siglip2-so400m-patch16-384) / [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) | [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B-OCR)  |
| GME-VARCO-VISION-Embedding | [Qwen2-VL-7B-Instruct](https://huggingface.co/Qwen/Qwen2-VL-7B-Instruct)                                                                      | [link](https://huggingface.co/NCSOFT/GME-VARCO-VISION-Embedding) |

## Model Architecture
VARCO-VISION-2.0 follows the architecture of [LLaVA-OneVision](https://arxiv.org/abs/2408.03326).

## Evaluation

### OCR Benchmark
| Benchmark | CLOVA OCR | PaddleOCR | EasyOCR | VARCO-VISION-2.0-1.7B-OCR |
| :-------: | :--------:| :-------: | :-----: | :-----------------------: |
| CORD      | *93.9*    | 91.4      | 77.8    | **95.6**                  |
| ICDAR2013 | *94.4*    | 92.0      | 85.0    | **95.5**                  |
| ICDAR2015 | **84.1**  | 73.7      | 57.9    | *75.4*                    |

## Usage
To use this model, we recommend installing `transformers` version **4.53.1 or higher**.
Additionally, for best results, we **recommend upscaling input images to a minimum resolution of *2,304*** on the longer side if they are smaller.

```python
import torch
from PIL import Image
from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration

model_name = "NCSOFT/VARCO-VISION-2.0-1.7B-OCR"
model = LlavaOnevisionForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    attn_implementation="sdpa",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_name)

image = Image.open("file:///path/to/image.jpg")

# Image upscaling for OCR performance boost
w, h = image.size
target_size = 2304
if max(w, h) < target_size:
    scaling_factor = target_size / max(w, h)
    new_w = int(w * scaling_factor)
    new_h = int(h * scaling_factor)
    image = image.resize((new_w, new_h))

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "<ocr>"},
        ],
    },
]

inputs = processor.apply_chat_template(
    conversation,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device, torch.float16)

generate_ids = model.generate(**inputs, max_new_tokens=1024)
generate_ids_trimmed = [
    out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.decode(generate_ids_trimmed[0], skip_special_tokens=False)
print(output)
```

## Citation
```bibtex
@misc{cha2025varcovision20technicalreport,
      title={VARCO-VISION-2.0 Technical Report}, 
      author={Young-rok Cha and Jeongho Ju and SunYoung Park and Jong-Hyeon Lee and Younghyun Yu and Youngjune Kim},
      year={2025},
      eprint={2509.10105},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2509.10105}, 
}
```
