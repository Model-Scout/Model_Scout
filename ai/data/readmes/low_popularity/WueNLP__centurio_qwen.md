---
library_name: transformers
license: apache-2.0
language:
- multilingual
- af
- am
- ar
- as
- azb
- be
- bg
- bm
- bn
- bo
- bs
- ca
- ceb
- cs
- cy
- da
- de
- du
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- ga
- gd
- gl
- ha
- hi
- hr
- ht
- hu
- id
- ig
- is
- it
- iw
- ja
- jv
- ka
- ki
- kk
- km
- ko
- la
- lb
- ln
- lo
- lt
- lv
- mi
- mr
- ms
- mt
- my
- 'no'
- oc
- pa
- pl
- pt
- qu
- ro
- ru
- sa
- sc
- sd
- sg
- sk
- sl
- sm
- so
- sq
- sr
- ss
- sv
- sw
- ta
- te
- th
- ti
- tl
- tn
- tpi
- tr
- ts
- tw
- uk
- ur
- uz
- vi
- war
- wo
- xh
- yo
- zh
- zu
base_model:
- Qwen/Qwen2.5-7B-Instruct
- timm/ViT-SO400M-14-SigLIP-384
pipeline_tag: image-text-to-text
---

# Centurio Qwen

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->

- **Model type:** Centurio is an open-source multilingual large vision-language model.
- **Training Data:** COMING SOON 
- **Languages:** The model was trained with the following 100 languages: `af, am, ar, ar-eg, as, azb, be, bg, bm, bn, bo, bs, ca, ceb, cs, cy, da, de, du, el, en, eo, es, et, eu, fa, fi, fr, ga, gd, gl, ha, hi, hr, ht, hu, id, ig, is, it, iw, ja, jv, ka, ki, kk, km, ko, la, lb, ln, lo, lt, lv, mi, mr, ms, mt, my, no, oc, pa, pl, pt, qu, ro, ru, sa, sc, sd, sg, sk, sl, sm, so, sq, sr, ss, sv, sw, ta, te, th, ti, tl, tn, tpi, tr, ts, tw, uk, ur, uz, vi, war, wo, xh, yo, zh, zu
`
- **License:** This work is released under the Apache 2.0 license. 

### Model Sources 

<!-- Provide the basic links for the model. -->

- **Repository:** [gregor-ge.github.io/Centurio](https://gregor-ge.github.io/Centurio)
- **Paper:** [arXiv](https://arxiv.org/abs/2501.)

## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

The model can be used directly through the `transformers` library with our custom code. 

```python
from transformers import AutoModelForCausalLM, AutoProcessor
import timm
from PIL import Image    
import requests

url = "https://upload.wikimedia.org/wikipedia/commons/b/bd/Golden_Retriever_Dukedestiny01_drvd.jpg"
image = Image.open(requests.get(url, stream=True).raw)

model_name = "WueNLP/centurio_qwen"

processor = AutoProcessor.from_pretrained(model_name, trust_remote_code=True)

## Appearance of images in the prompt are indicates with '<image_placeholder>'!
prompt = "<image_placeholder>\nBriefly describe the image in German."

messages = [
    {"role": "system", "content": "You are a helpful assistant."},  # This is the system prompt used during our training.
    {"role": "user", "content": prompt}
]

text = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True
)

model_inputs = processor(text=[text], images=[image] return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=128
)

generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

```

#### Multiple Images
We natively support multi-image inputs. You only have to 1) include more `<image_placeholder>` while 2) passing all images of the *entire batch* as a flat list:

```python
[...]
# Variables reused from above.

processor.tokenizer.padding_side = "left" # default is 'right' but has to be 'left' for batched generation to work correctly!

image_multi_1, image_multi_2 = [...] # prepare additional images

prompt_multi = "What is the difference between the following images?\n<image_placeholder><image_placeholder>\nAnswer in German."

messages_multi = [
    {"role": "system", "content": "You are a helpful assistant."}, 
    {"role": "user", "content": prompt_multi}
]

text_multi = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = processor(text=[text, text_multi], images=[image, image_multi_1, image_multi_2] return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=128
)

[...]

```




## Bias, Risks, and Limitations

- General biases, risks, and limitations of large vision-language models like hallucinations or biases from training data apply.
- This is a research project and *not* recommended for production use.
- Multilingual: Performance and generation quality can differ widely between languages. 
- OCR: Model struggles both with small text and writing in non-Latin scripts.


## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

```
@article{centurio2025,
  author       = {Gregor Geigle and
                  Florian Schneider and
                  Carolin Holtermann and
                  Chris Biemann and
                  Radu Timofte and
                  Anne Lauscher and
                  Goran Glava\v{s}},
  title        = {Centurio: On Drivers of Multilingual Ability of Large Vision-Language Model},
  journal      = {arXiv},
  volume       = {abs/2501.05122},
  year         = {2025},
  url          = {https://arxiv.org/abs/2501.05122},
  eprinttype    = {arXiv},
  eprint       = {2501.05122},
}
```