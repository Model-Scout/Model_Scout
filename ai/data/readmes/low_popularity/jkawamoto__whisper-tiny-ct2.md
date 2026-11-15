---
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
- no
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
- ctranslate2
license: apache-2.0
base_model: openai/whisper-tiny
base_model_relation: quantized
---
# whisper-tiny-ct2

This is a version of [`openai/whisper-tiny`](https://huggingface.co/openai/whisper-tiny)
converted for use with [CTranslate2](https://github.com/OpenNMT/CTranslate2).

The conversion was performed using the following command:

```
ct2-transformers-converter --model openai/whisper-tiny --output_dir whisper-tiny-ct2 \
    --copy_files generation_config.json preprocessor_config.json tokenizer_config.json \
    tokenizer.json vocabulary.json
```

## License
This adaptation is based on [`openai/whisper-tiny`](https://huggingface.co/openai/whisper-tiny),
originally provided under the Apache 2.0 License. 
Modifications were made for compatibility with CTranslate2. 
Despite these modifications, this adapted version continues to be distributed under the Apache 2.0 License,
honoring the original licensing terms.
