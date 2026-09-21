---
license: mit
language:
- en
- ja
- zh
- ko
metrics:
- accuracy
base_model: google-bert/bert-base-multilingual-cased
pipeline_tag: text-classification
tags:
- sex
- filename
- dectection
- content
- mbert
- Multilingual
---
# Model Card for Model ID

Detect sexual content in text or file names.

## Model Details

### Model Description

- **Developed by:** liu wei
- **License:** MIT
- **Finetuned from model:** bert-base-multilingual-cased
- **Task:** Simple Classification
- **Language:** Multilingual
- **Max Length:** 128
- **Updated Time:** 2024-8-22 

### Model Training Information
- **Training Dataset Size:** 100,000 manually annotated data with noise
- **Data Distribution:** 50:50
- **Batch Size:** 8
- **Epochs:** 5
- **Accuracy:** 92%
- **F1:** 92%


<a href="https://ko-fi.com/ugetai" target="_blank" rel="noopener noreferrer">Buy me a cup of coffee,thanks</a>


## Uses

- Supports multiple languages, such as English, Chinese, Japanese, etc. 
- Use for detect content submitted by users in forums, magnetic search engines, cloud disks, etc. 
- Detect semantics and variant content, Porn movie numbers or variant file names.
- Compared with GPT4O-mini, The detection accuracy is greatly improved.

### Examples

- Example **English**
```python
predict("Tiffany Doll - Wine Makes Me Anal (31.03.2018)_1080p.mp4")
```
```json
{
    "predictions": 1,
    "label": "Sexual"
}
```

- Example **Chinese**
```python
predict("橙子 · 保安和女业主的一夜春宵。路见不平拔刀相助，救下苏姐，以身相许！")
```
```json
{
    "predictions": 1,
    "label": "Sexual"
}
```

- Example **Japanese**
```python
predict("MILK-217-UNCENSORED-LEAKピタコス Gカップ痴女 完全着衣で濃密5PLAY 椿りか 580 2.TS")
```
```json
{
    "predictions": 1,
    "label": "Sexual"
}
```

- Example **Porn Movie Numbers**
```python
predict("DVAJ-548_CH_SD")
```
```json
{
    "predictions": 1,
    "label": "Sexual"
}
```


## How to Get Started with the Model


### step 1: 
Create a python file under this model, such as 'use_model.py'
```python
import torch
from transformers import BertForSequenceClassification, BertTokenizer

# load model
tokenizer = BertTokenizer.from_pretrained("uget/sexual_content_dection")
model = BertForSequenceClassification.from_pretrained("uget/sexual_content_dection")

def predict(text):
    encoding = tokenizer(text, return_tensors="pt")
    encoding = {k: v.to(model.device) for k,v in encoding.items()}

    outputs = model(**encoding)
    probs = torch.sigmoid(outputs.logits)
    
    predictions = torch.argmax(probs, dim=-1)
    label_map = {0: "None", 1: "Sexual"}
    predicted_label = label_map[predictions.item()]
    print(f"Predictions:{predictions.item()}, Label:{predicted_label}")
    return {"predictions": predictions.item(), "label": predicted_label}

predict("Tiffany Doll - Wine Makes Me Anal (31.03.2018)_1080p.mp4")

```
### step 2:
Run
```shell
python3 use_model.py
```

Response JSON
```json
{
    "predictions": 1,
    "label": "Sexual"
}
```

### Explanation
The results only include two situations: 
- predictions-0   **Not Dectection** sexual content; 
- predictions-1   **Sexual** content was detected.

<a href="https://ko-fi.com/ugetai" target="_blank" rel="noopener noreferrer">Buy me a cup of coffee,thanks</a>
## Model Card Contact
Email: jack813@gmail.com