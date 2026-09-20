---
license: cc-by-nc-4.0
base_model:
- Qwen/Qwen3-1.7B
- google/siglip2-so400m-patch16-384
library_name: transformers
tags:
- multimodal
- conversational
- ncsoft
- ncai
- varco
pipeline_tag: image-text-to-text
language:
- en
- ko
---

# VARCO-VISION-2.0-1.7B

<div align="center">
   <img src="./varco-vision.png" width="100%" style="background-color:white; padding:10px;" />
</div>

## Introduction
**VARCO-VISION-2.0** is a multimodal AI model capable of understanding both images and text to answer user queries. It supports multi-image inputs, enabling effective processing of complex content such as documents, tables, and charts. The model demonstrates strong comprehension in both Korean and English, with significantly improved text generation capabilities and a deeper understanding of Korean cultural context. Compared to its predecessor, performance has been notably enhanced across various benchmarks, and its usability in real-world scenarios—such as everyday Q&A and information summarization—has also improved.

In addition to the 14B full-scale model, a lightweight 1.7B version is available for on-device use, making it accessible on personal devices such as smartphones and PCs. VARCO-VISION-2.0 is a powerful open-weight AI model built for Korean users and is freely available for a wide range of applications.

## 🚨News🎙️
- 📝 2025-09-12: We published the technical report of VARCO-VISION-2.0 at [link](https://arxiv.org/abs/2509.10105)
- 🛠️ 2025-08-22: We updated the checkpoint of VARCO-VISION-2.0-1.7B for improved performance.
- 📰 2025-07-28: We released VARCO-VISION-2.0-1.7B-OCR at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B-OCR)
- 📰 2025-07-28: We released VARCO-VISION-2.0-1.7B at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-1.7B)
- 🛠️ 2025-07-18: We updated the checkpoint of VARCO-VISION-2.0-14B for improved performance.
- 📰 2025-07-16: We released VARCO-VISION-2.0-14B at [link](https://huggingface.co/NCSOFT/VARCO-VISION-2.0-14B)
- 📰 2025-07-16: We released GME-VARCO-VISION-Embedding at [link](https://huggingface.co/NCSOFT/GME-VARCO-VISION-Embedding)

## Key Features
- **Multi-image Understanding**: Newly added support for multi-image inputs enables the model to analyze multiple images simultaneously and make more holistic and context-aware decisions.
- **Korean Language Specialization**: The model is further specialized for Korean, with a deeper understanding of Korean language, context, and culture. Korean text generation has been significantly improved, resulting in more natural, fluent, and accurate responses.
- **OCR with Text Localization**: Unlike typical models that only recognize and generate text from images, VARCO-VISION-2.0 can also identify the position of the text and provide bounding boxes around it. This makes it especially useful for document understanding, signage interpretation, and structured visual data.
- **Enhanced Safety**: The model now offers improved handling of harmful or sexually explicit content, ensuring safer and more reliable interactions.

<div align="center">
    <img src="./figure.png" width="100%" />
</div>

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
We used [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) for evaluation whenever possible, and conducted our own implementations only for benchmarks not supported by the toolkit, **ensuring fair comparisons** with various open-weight models.
Please note that for certain benchmarks involving LLM-based evaluation (e.g., LLaVABench), results may not be exactly reproducible due to variations in the underlying LLM behavior.

### Korean Benchmark
| Benchmark     | InternVL3-2B | Ovis2-2B | VARCO-VISION-2.0-1.7B |
| :-----------: | :----------: | :------: | :-------------------: |
| K-MMBench_DEV | *76.9*       | 68.4     | **77.9**              |
| K-MMStar      | **50.1**     | 10.9     | *40.8*                |
| K-SEED        | *69.2*       | 34.5     | **70.7**              |
| K-LLaVA-W     | 47.6         | *67.2*   | **73.5**              |
| K-DTCBench    | **68.8**     | 44.6     | *64.2*                |
| ***AVERAGE*** | *62.5*       | 45.1     | **65.4**              |

### English Benchmark
| Benchmark       | InternVL3-2B | Ovis2-2B | VARCO-VISION-2.0-1.7B |
| :-------------: | :----------: | :------: | :-------------------: |
| MMStar          | **61.1**     | *56.7*   | 54.5                  |
| MMMU_VAL        | **48.7**     | *45.6*   | 44.1                  |
| MathVista       | 57.6         | **64.1** | *61.1*                |
| OCRBench        | *83.1*       | **87.3** | 83.0                  |
| AI2D            | *78.6*       | **82.7** | 76.0                  |
| HallusionBench  | 41.9         | **50.2** | *43.0*                |
| MMVet           | **67.0**     | *58.3*   | 52.7                  |
| SEEDBench_IMG   | **75.0**     | 74.4     | *74.5*                |
| LLaVABench      | 72.1         | *76.6*   | **77.3**              |
| RealWorldQA     | 65.1         | *66.0*   | **66.8**              |
| POPE            | **90.1**     | 87.8     | *88.6*                |
| ScienceQA_TEST  | **95.8**     | *91.2*   | 84.0                  |
| SEEDBench2_Plus | 64.8         | **67.4** | *66.9*                |
| BLINK           | **53.1**     | *47.9*   | 47.2                  |
| TextVQA_VAL     | *78.6*       | **80.0** | 77.0                  |
| ChartQA_TEST    | *76.0*       | **81.4** | 75.7                  |
| Q-Bench1_VAL    | 71.9         | **76.3** | *72.3*                |
| A-Bench_VAL     | *74.3*       | **76.2** | 72.4                  |
| DocVQA_TEST     | *88.2*       | **91.9** | 83.5                  |
| InfoVQA_TEST    | 66.9         | **71.7** | 65.0                  |
| ***AVERAGE***   | *70.5*       | **71.7** | 68.3                  |

### Text-only Benchmark
| Benchmark       | InternVL3-2B | Ovis2-2B | VARCO-VISION-2.0-1.7B |
| :-------------: | :----------: | :------: | :-------------------: |
| MMLU            | **59.9**     | 12.9     | *55.3*                |
| MT-Bench        | *62.8*       | 61.4     | **72.3**              |
| KMMLU           | **38.0**     | *31.1*   | 10.4                  |
| KoMT-Bench      | 29.1         | *34.4*   | **59.1**              |
| LogicKor        | 25.6         | *31.2*   | **53.7**              |
| ***AVERAGE***   | *43.1*       | 34.2     | **50.2**              |

> **Note:** Some models show unusually low performance on the MMLU benchmark. This is primarily due to their failure to correctly follow the expected output format when only few-shot exemplars are provided in the prompts. Please take this into consideration when interpreting the results.

### Korean Cultural Benchmark
| Benchmark        | InternVL3-2B | Ovis2-2B | VARCO-VISION-2.0-1.7B |
| :--------------: | :----------: | :------: | :-------------------: |
| K-Viscuit        | *60.0*       | **64.1** | 57.7                  |
| PangeaBench (ko) | **66.2**     | 63.1     | *63.8*                |
| ***AVERAGE***    | *63.1*       | **63.6** | 60.8                  |

### OCR Benchmark
| Benchmark     | PaddleOCR | EasyOCR | VARCO-VISION-2.0-1.7B |
| :-----------: | :-------: | :-----: | :-------------------: |
| CORD          | *91.4*    | 77.8    | **96.2**              |
| ICDAR2013     | *92.0*    | 85.0    | **95.9**              |
| ICDAR2015     | **73.7**  | 57.9    | **73.7**              |
| ***AVERAGE*** | *85.7*    | 73.6    | **88.6**              |

## Usage
To use this model, we recommend installing `transformers` version **4.53.1 or higher**. While it may work with earlier versions, using **4.53.1 or above is strongly recommended**, especially to ensure optimal performance for the **multi-image feature**.

The basic usage is **identical to** [LLaVA-OneVision](https://huggingface.co/docs/transformers/main/en/model_doc/llava_onevision#usage-example):

```python
import torch
from transformers import AutoProcessor, LlavaOnevisionForConditionalGeneration

model_name = "NCSOFT/VARCO-VISION-2.0-1.7B"
model = LlavaOnevisionForConditionalGeneration.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    attn_implementation="sdpa",
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_name)

conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "url": "https://huggingface.co/NCSOFT/VARCO-VISION-2.0-14B/resolve/main/demo.jpg"},
            {"type": "text", "text": "각 박스마다 한 줄씩 색상과 글자를 정확하게 출력해주세요."},
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
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.decode(generate_ids_trimmed[0], skip_special_tokens=True)
print(output)
```

<details>
<summary>Multi image inference</summary>

```python
conversation = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image1.jpg"},
            {"type": "image", "image": "file:///path/to/image2.jpg"},
            {"type": "text", "text": "이미지 간의 유사점을 파악하세요."},
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
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.decode(generate_ids_trimmed[0], skip_special_tokens=True)
print(output)
```
</details>

<details>
<summary>Batch inference</summary>
All inputs in a batch must have the same modality structure—for example, text-only with text-only, single-image with single-image, and multi-image with multi-image—to ensure correct batch inference.

```python
conversation_1 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image1.jpg"},
            {"type": "text", "text": "이미지를 설명해주세요."},
        ],
    },
]
conversation_2 = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": "file:///path/to/image2.jpg"},
            {"type": "text", "text": "이 이미지에 표시된 것은 무엇인가요?"},
        ],
    },
]
inputs = processor.apply_chat_template(
    [conversation_1, conversation_2],
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    padding=True,
    return_tensors="pt"
).to(model.device, torch.float16)
generate_ids = model.generate(**inputs, max_new_tokens=1024)
generate_ids_trimmed = [
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.batch_decode(generate_ids_trimmed, skip_special_tokens=True)
print(output)
```
</details>

<details>
<summary>OCR inference</summary>

```python
from PIL import Image
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
    out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generate_ids)
]
output = processor.decode(generate_ids_trimmed[0], skip_special_tokens=False)
print(output)
```
</details>

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
