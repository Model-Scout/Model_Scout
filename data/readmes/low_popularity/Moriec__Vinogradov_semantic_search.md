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
- no
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
- xh
- yi
- yo
- zu
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
library_name: sentence-transformers
license: apache-2.0
---

Нейронная модель Виноградова Дмитрия для определения семантического сходства пар запросов. Построение производится через 384-мерное векторное пространство. 
Api функционал через SentenceTransformers. Токенизатор присутствует


## Full Model Architecture
```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False})
  (2): Dense({'in_features': 768, 'out_features': 768, 'bias': True, 'activation_function': 'torch.nn.modules.activation.Tanh'})
  (3): Normalize()
)
```

