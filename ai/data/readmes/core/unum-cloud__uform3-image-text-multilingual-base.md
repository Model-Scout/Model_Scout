---
license: apache-2.0
language:
- en
- ar
- hy
- zh
- fr
- de
- he
- hi
- id
- it
- ja
- ko
- fa
- pl
- pt
- ru
- es
- th
- tr
- uk
- vi
pipeline_tag: feature-extraction
tags:
- clip
- vision
datasets:
- sbu_captions
- visual_genome
- ChristophSchuhmann/MS_COCO_2017_URL_TEXT
- Ziyang/yfcc15m
---

<h1 align="center">UForm</h1>
<h3 align="center">
Pocket-Sized Multimodal AI<br/>
For Content Understanding and Generation<br/>
In Python, JavaScript, and Swift<br/>
</h3>

---

The `uform3-image-text-multilingual-base` UForm model is a tiny vision and multilingual language encoder, covering __21 languages__, mapping them into a shared vector space.
This model produces up to __256-dimensional embeddings__ and is made of:

* Text encoder: 12-layer BERT for up to 50 input tokens.
* Visual encoder: ViT-B/16 for images of 224 x 224 resolution.

Unlike most CLIP-like multomodal models, this model shares 4 layers between the text and visual encoder to allow for more data- and parameter-efficient training.
Also unlike most models, UForm provides checkpoints compatible with PyTorch, ONNX, and CoreML, covering the absolute majority of AI-capable devices, with pre-quantized weights and inference code.
If you need a larger, more accurate, or multilingual model, check our [HuggingFace Hub](https://huggingface.co/unum-cloud/).
For more details on running the model, check out the [UForm GitHub repository](https://github.com/unum-cloud/uform/).

## Evaluation

For all evaluations, the multimodal part was used unless otherwise stated.

### Monolingual

| Dataset |  Recall@1 |  Recall@5 | Recall@10 |
| :-------- | ------: | --------: | --------: |
| Zero-Shot Flickr | 0.558 | 0.813 | 0.874 |
| MS-COCO ¹ | 0.401 | 0.680 | 0.781 |

> ¹ It's important to note, that the MS-COCO train split was present in the training data.

### Multilingual

Recall@10 on the [XTD-10](https://github.com/adobe-research/Cross-lingual-Test-Dataset-XTD10) dataset:

|  English |   German |  Spanish |   French |  Italian |  Russian | Japanese |   Korean |  Turkish |  Chinese | Polish |
| -------: | -------: | -------: | -------: | -------: | -------: | -------: | -------: | -------: | -------: | ------:|
|     96.1 |     93.5 |     95.7 |     94.1 |     94.4 |     90.4 |     90.2 |     91.3 |     95.2 |     93.8 |   95.8 |

Recall@1, Recall@5, and Recall@10 on the [COCO-SM](https://github.com/kimihailv/coco-sm/tree/main) dataset:

| Target Language       | OpenCLIP @ 1 | UForm @ 1     | OpenCLIP @ 5 | UForm @ 5     | OpenCLIP @ 10 | UForm @ 10     | Speakers |
| :-------------------- | -----------: | ------------: | -----------: | -------------:| ------------: | --------------:| -------: |
| Arabic             |         22.7 |      **31.7** |         44.9 |      **57.8** |          55.8 |       **69.2** |    274 M |
| Armenian           |          5.6 |      **22.0** |         14.3 |      **44.7** |          20.2 |       **56.0** |      4 M |
| Chinese            |         27.3 |      **32.2** |         51.3 |      **59.0** |          62.1 |       **70.5** |  1'118 M |
| English            |     **37.8** |          37.7 |         63.5 |      **65.0** |          73.5 |       **75.9** |  1'452 M |
| French             |         31.3 |      **35.4** |         56.5 |      **62.6** |          67.4 |       **73.3** |    274 M |
| German             |         31.7 |      **35.1** |         56.9 |      **62.2** |          67.4 |       **73.3** |    134 M |
| Hebrew             |         23.7 |      **26.7** |         46.3 |      **51.8** |          57.0 |       **63.5** |      9 M |
| Hindi              |         20.7 |      **31.3** |         42.5 |      **57.9** |          53.7 |       **69.6** |    602 M |
| Indonesian         |         26.9 |      **30.7** |         51.4 |      **57.0** |          62.7 |       **68.6** |    199 M |
| Italian            |         31.3 |      **34.9** |         56.7 |      **62.1** |          67.1 |       **73.1** |     67 M |
| Japanese           |         27.4 |      **32.6** |         51.5 |      **59.2** |          62.6 |       **70.6** |    125 M |
| Korean             |         24.4 |      **31.5** |         48.1 |      **57.8** |          59.2 |       **69.2** |     81 M |
| Persian            |         24.0 |      **28.8** |         47.0 |      **54.6** |          57.8 |       **66.2** |     77 M |
| Polish             |         29.2 |      **33.6** |         53.9 |      **60.1** |          64.7 |       **71.3** |     41 M |
| Portuguese         |         31.6 |      **32.7** |         57.1 |      **59.6** |          67.9 |       **71.0** |    257 M |
| Russian            |         29.9 |      **33.9** |         54.8 |      **60.9** |          65.8 |       **72.0** |    258 M |
| Spanish            |         32.6 |      **35.6** |         58.0 |      **62.8** |          68.8 |       **73.7** |    548 M |
| Thai               |         21.5 |      **28.7** |         43.0 |      **54.6** |          53.7 |       **66.0** |     61 M |
| Turkish            |         25.5 |      **33.0** |         49.1 |      **59.6** |          60.3 |       **70.8** |     88 M |
| Ukranian           |         26.0 |      **30.6** |         49.9 |      **56.7** |          60.9 |       **68.1** |     41 M |
| Vietnamese         |         25.4 |      **28.3** |         49.2 |      **53.9** |          60.3 |       **65.5** |     85 M |
|                       |              |               |              |               |               |                |          |
| Mean                  |     26.5±6.4 |  **31.8±3.5** |     49.8±9.8 |  **58.1±4.5** |     60.4±10.6 |   **69.4±4.3** |        - |
| Google Translate      |     27.4±6.3 |  **31.5±3.5** |     51.1±9.5 |  **57.8±4.4** |     61.7±10.3 |   **69.1±4.3** |        - |
| Microsoft Translator  |     27.2±6.4 |  **31.4±3.6** |     50.8±9.8 |  **57.7±4.7** |     61.4±10.6 |   **68.9±4.6** |        - |
| Meta NLLB             |     24.9±6.7 |  **32.4±3.5** |    47.5±10.3 |  **58.9±4.5** |     58.2±11.2 |   **70.2±4.3** |        - |

For a deeper comparison of output ranking check the following table for the Normalized Discounted Cumulative Gains for the first 20 results - NDCG@20:

|               |     Arabic |     Armenian |     Chinese |     French |     German |     Hebrew |     Hindi |     Indonesian |     Italian |     Japanese |     Korean |     Persian |     Polish |     Portuguese |     Russian |     Spanish |     Thai |     Turkish |     Ukranian |     Vietnamese |   Mean (all) | Mean (Google Translate) | Mean(Microsoft Translator) | Mean(NLLB)
| :------------ | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: | ----: |
| OpenCLIP NDCG | 0.639 | 0.204 | 0.731 | 0.823 | 0.806 | 0.657 | 0.616 | 0.733 | 0.811 | 0.737 | 0.686 | 0.667 | 0.764 | 0.832 | 0.777 | 0.849 | 0.606 | 0.701 | 0.704 | 0.697 | 0.716 ± 0.149 | 0.732 ± 0.145 | 0.730 ± 0.149 | 0.686 ± 0.158
| UForm NDCG    | 0.868 | 0.691 | 0.880 | 0.932 | 0.927 | 0.791 | 0.879 | 0.870 | 0.930 | 0.885 | 0.869 | 0.831 | 0.897 | 0.897 | 0.906 | 0.939 | 0.822 | 0.898 | 0.851 | 0.818 | 0.875 ± 0.064 | 0.869 ± 0.063 | 0.869 ± 0.066 | 0.888 ± 0.064


## Installation

```bash
pip install "uform[torch,onnx]"
```

## Usage

To load the model:

```python
from uform import get_model, Modality

import requests
from io import BytesIO
from PIL import Image

model_name = 'unum-cloud/uform3-image-text-multilingual-base'
modalities = [Modality.TEXT_ENCODER, Modality.IMAGE_ENCODER]
processors, models = get_model(model_name, modalities=modalities)

model_text = models[Modality.TEXT_ENCODER]
model_image = models[Modality.IMAGE_ENCODER]
processor_text = processors[Modality.TEXT_ENCODER]
processor_image = processors[Modality.IMAGE_ENCODER]
```

To encode the content:

```python
text = 'a cityscape bathed in the warm glow of the sun, with varied architecture and a towering, snow-capped mountain rising majestically in the background'
image_url = 'https://media-cdn.tripadvisor.com/media/photo-s/1b/28/6b/53/lovely-armenia.jpg'
image_url = Image.open(BytesIO(requests.get(image_url).content))

image_data = processor_image(image)
text_data = processor_text(text)
image_features, image_embedding = model_image.encode(image_data, return_features=True)
text_features, text_embedding = model_text.encode(text_data, return_features=True)
```
