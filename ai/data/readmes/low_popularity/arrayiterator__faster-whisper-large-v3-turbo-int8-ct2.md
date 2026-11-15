---
license: mit
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
tags:
- audio
- automatic-speech-recognition
- faster-whisper
- 8-bit
pipeline_tag: automatic-speech-recognition
base_model:
- openai/whisper-large-v3-turbo
library_name: ctranslate2
---

# CTranslate2 Conversion of whisper-large-v3-turbo (INT8 Quantization)

This model is converted from [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) to the CTranslate2 format using INT8 quantization, primarily for use with [faster-whisper](https://github.com/SYSTRAN/faster-whisper.git)

## Model Details

For more details about the model, see its original [model card](https://huggingface.co/openai/whisper-large-v3-turbo)

## Conversion Details

The original model was converted using the following command:  
```
ct2-transformers-converter --model whisper-large-v3-turbo --copy_files tokenizer.json preprocessor_config.json --output_dir faster-whisper-large-v3-turbo-int8-ct2 --quantization int8
```