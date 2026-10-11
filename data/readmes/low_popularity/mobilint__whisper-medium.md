---
library_name: transformers
license: apache-2.0
language:
- en
- zh
- de
- es
- ru
- ko
- fr
- ja
- pt
- tr
- pl
- ca
- nl
- ar
- sv
- it
- id
- hi
- fi
- vi
- he
- uk
- el
- ms
- cs
- ro
- da
- hu
- ta
- 'no'
- th
- ur
- hr
- bg
- lt
- la
- mi
- ml
- cy
- sk
- te
- fa
- lv
- bn
- sr
- az
- sl
- kn
- et
- mk
- br
- eu
- is
- hy
- ne
- mn
- bs
- kk
- sq
- sw
- gl
- mr
- pa
- si
- km
- sn
- yo
- so
- af
- oc
- ka
- be
- tg
- sd
- gu
- am
- yi
- lo
- uz
- fo
- ht
- ps
- tk
- nn
- mt
- sa
- lb
- my
- bo
- tl
- mg
- as
- tt
- haw
- ln
- ha
- ba
- jw
- su
base_model:
- openai/whisper-medium
base_model_relation: quantized
pipeline_tag: automatic-speech-recognition
tags:
- mobilint
---

<div align="center">
  <a href="https://mobilint.com">
    <img src="https://raw.githubusercontent.com/mobilint/.github/main/assets/Mobilint_Logo_Primary.png" 
         width="50%" 
         alt="mobilint" />
  </a>
</div>


# About
This repository provides a model compiled and optimized for Mobilint NPU hardware.  
The model is packaged for deployment on Mobilint’s acceleration stack and is intended to be used within that environment.