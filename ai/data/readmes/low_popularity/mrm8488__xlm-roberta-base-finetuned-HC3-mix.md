---
license: openrail
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - no
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi

datasets:
- Hello-SimpleAI/HC3
metrics:
- f1
pipeline_tag: text-classification

widget:
- text: "La Guerra Civil Española, que tuvo lugar entre 1936 y 1939, fue un conflicto sangriento y divisivo en el que se enfrentaron las fuerzas republicanas y las fuerzas nacionalistas lideradas por Francisco Franco. El origen de la guerra se remonta a las tensiones políticas y sociales que se habían ido acumulando en España durante años, incluyendo la lucha entre la izquierda y la derecha, el descontento popular con el gobierno y la crisis económica.\nEl estallido de la guerra civil se produjo después de las elecciones de febrero de 1936, en "
- text: "Cristóbal Colón fue un navegante, cartógrafo y almirante español que llevó a cabo cuatro viajes transatlánticos entre 1492 y 1504. Es conocido por haber sido el primer europeo en llegar a América, aunque en realidad no fue el primer ser humano en alcanzar el continente, ya que los pueblos indígenas ya habitaban allí desde hacía miles de años.\nColón nació en la ciudad italiana de Génova en 1451. Aunque no se sabe con certeza dónde recibió su formación, se cree que tuvo una educación marinera y cartográfica. A mediados de la década de 1470, se trasladó a España, donde trabajó como piloto y cartógrafo para la Casa de Contratación de las Indias, una institución encargada de las relaciones comerciales entre España y América."
- text: "Para usar un modelo pre-entrenado de la pipeline de clasificación de texto de Hugging Face, primero debe instalar la última versión de la biblioteca Hugging Face utilizando el comando !pip install transformers en su terminal o consola."
---

# XLM-RoBERTa (base) fine-tuned on HC3 for ChatGPT text detection

**XLM-RoBERTa** (base) fine-tuned on [Hello-SimpleAI](https://huggingface.co/Hello-SimpleAI) **HC3** corpus for **ChatGPT** text detection.

All credit to [Hello-SimpleAI](https://huggingface.co/Hello-SimpleAI) for their huge work!

## F1 score on test dataset: 0.9736

## The model
XLM-RoBERTa model pre-trained on 2.5TB of filtered CommonCrawl data containing 100 languages. It was introduced in the paper Unsupervised Cross-lingual Representation Learning at Scale by Conneau et al. and first released in this repository.

## The dataset

#### Human ChatGPT Comparison Corpus (HC3)
The first human-ChatGPT comparison corpus, named **HC3** dataset by [Hello-SimpleAI](https://huggingface.co/Hello-SimpleAI)

This dataset is introduced in the paper: 
- Paper: [***How Close is ChatGPT to Human Experts? Comparison Corpus, Evaluation, and Detection***](https://arxiv.org/abs/2301.07597)


## Metrics
|metric| value|
|------|------|
|F1    |0.9736|

## Usage
```py
from transformers import pipeline

ckpt = "mrm8488/xlm-roberta-base-finetuned-HC3-mix"

detector = pipeline('text-classification', model=ckpt)

text = "Here your text..."

result = detector(text)

print(result)
```



## Citation
```
@misc {manuel_romero_2023,
	author       = { {Manuel Romero} },
	title        = { xlm-roberta-base-finetuned-HC3-mix (Revision b18de48) },
	year         = 2023,
	url          = { https://huggingface.co/mrm8488/xlm-roberta-base-finetuned-HC3-mix },
	doi          = { 10.57967/hf/0306 },
	publisher    = { Hugging Face }
}
```