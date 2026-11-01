---
language:
- multilingual
- af
- sq
- am
- ar
- hy
- as
- az
- eu
- be
- bn
- bs
- bg
- my
- ca
- ceb
- zh
- co
- hr
- cs
- da
- nl
- en
- eo
- et
- fi
- fr
- fy
- gl
- ka
- de
- el
- gu
- ht
- ha
- haw
- he
- hi
- hmn
- hu
- is
- ig
- id
- ga
- it
- ja
- jv
- kn
- kk
- km
- rw
- ko
- ku
- ky
- lo
- la
- lv
- lt
- lb
- mk
- mg
- ms
- ml
- mt
- mi
- mr
- mn
- ne
- 'no'
- ny
- or
- fa
- pl
- pt
- pa
- ro
- ru
- sm
- gd
- sr
- st
- sn
- si
- sk
- sl
- so
- es
- su
- sw
- sv
- tl
- tg
- ta
- tt
- te
- th
- bo
- tr
- tk
- ug
- uk
- ur
- uz
- vi
- cy
- wo
- gd
- sr
- st
- sn
- si
- sk
- sl
- so
- es
- su
- sw
- sv
- tl
- tg
- ta
- tt
- te
- th
- bo
- tr
- tk
- ug
- uk
- ur
- gd
- sr
- st
- sn
- si
- sk
- sl
- so
- es
- su
- sw
- sv
- tl
- tg
- ta
- tt
- te
- th
- bo
- tr
- tk
- ug
- uk
- ur
- uz
- vi
- cy
- wo
- gd
- sr
- st
- sn
- si
- sk
- sl
- so
- es
- su
- sw
- sv
- tl
- tg
- ta
- tt
- te
- th
- bo
- tr
- tk
- ug
- uk
- ur
- uz
- vi
- uz
- vi
- cy
- wo
- xh
- xh
- yi
- yo
- zu
pipeline_tag: sentence-similarity
tags:
- bert
- sentence_embedding
- multilingual
- sartify
- sentence-similarity
- sentence
license: apache-2.0
library_name: sentence-transformers
---

# AviLaBSE

## Model description

This is a unified model trained to add other row resourced language dimensions. It can be used to map more than 130 languages to a shared vector space. The pre-training process combines masked language modeling with translation language modeling. The model is useful for getting multilingual sentence embeddings and for bi-text retrieval.

- **Model**: [HuggingFace's model hub](https://huggingface.co/sartifyllc/AviLaBSE).
- **Paper**: [arXiv](https://arxiv.org/abs/2007.01852).
<!-- - **Original TF model**: [TensorFlow Hub](https://tfhub.dev/google/LaBSE/2). -->
<!-- - **Blog post**: [Google AI Blog](https://ai.googleblog.com/2020/08/language-agnostic-bert-sentence.html). -->
- **Developed by:** [Sartify LLC](https://huggingface.co/sartifyllc/)

## Usage

Using the model:

```python
import torch
from transformers import BertModel, BertTokenizerFast


tokenizer = BertTokenizerFast.from_pretrained("sartifyllc/AviLaBSE")
model = BertModel.from_pretrained("sartifyllc/AviLaBSE")
model = model.eval()

english_sentences = [
    "dog",
    "Puppies are nice.",
    "I enjoy taking long walks along the beach with my dog.",
]
english_inputs = tokenizer(english_sentences, return_tensors="pt", padding=True)

with torch.no_grad():
    english_outputs = model(**english_inputs)
```

To get the sentence embeddings, use the pooler output:

```python
english_embeddings = english_outputs.pooler_output
```

Output for other row resourced languages:

```python
swahili_sentences = [
    "mbwa",
    "Mbwa ni mzuri.",
    "Ninafurahia kutembea kwa muda mrefu kando ya pwani na mbwa wangu.",
]
zulu_sentences = [
    "inja",
    "Inja iyavuma.",
    "Ngithanda ukubhema izinyawo ezidlula emanzini nabanye nomfana wami.",
]

igbo_sentences = [
    "nwa nkịta",
    "Nwa nkịta dị ọma.",
    "Achọrọ m gaa n'okirikiri na ụzọ nke oke na mgbidi na nwa nkịta m."
]

swahili_inputs = tokenizer(swahili_sentences, return_tensors="pt", padding=True)
zulu_inputs = tokenizer(zulu_sentences, return_tensors="pt", padding=True)
igbo_inputs=tokenizer(igbo_sentences, return_tensors="pt", padding=True)

with torch.no_grad():
    swahili_outputs = model(**swahili_inputs)
    zulu_outputs = model(**zulu_inputs)
    igbo_outputs =model(**igbo_inputs)

swahili_embeddings = swahili_outputs.pooler_output
zulu_embeddings = zulu_outputs.pooler_output
igbo_embeddings=igbo_outputs.pooler_output
```

For similarity between sentences, an L2-norm is recommended before calculating the similarity:

```python
import torch.nn.functional as F

def similarity(embeddings_1, embeddings_2):
    normalized_embeddings_1 = F.normalize(embeddings_1, p=2)
    normalized_embeddings_2 = F.normalize(embeddings_2, p=2)
    return torch.matmul(
        normalized_embeddings_1, normalized_embeddings_2.transpose(0, 1)
    )


print(similarity(english_embeddings, swahili_embeddings))
print(similarity(english_embeddings, zulu_embeddings))
print(similarity(swahili_embeddings, igbo_embeddings))
```

## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  (2): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.Tanh'})
  (3): Normalize()
)
```