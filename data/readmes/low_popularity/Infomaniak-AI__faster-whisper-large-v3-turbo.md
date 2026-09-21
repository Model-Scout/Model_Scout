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
license: mit
library_name: ctranslate2
---

# Whisper large-v3-turbo model for CTranslate2

This repository contains the conversion of [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) to the [CTranslate2](https://github.com/OpenNMT/CTranslate2) model format.

This model can be used in CTranslate2 or projects based on CTranslate2 such as [faster-whisper](https://github.com/systran/faster-whisper).

## Example with batch inference

```python
import time

from faster_whisper import WhisperModel, BatchedInferencePipeline
from faster_whisper.audio import decode_audio

model = WhisperModel("Infomaniak-AI/faster-whisper-large-v3-turbo",
                     device="cuda",
                     num_workers=4,
                     compute_type='float16')

batch = BatchedInferencePipeline(model=model,
                                 use_vad_model=True,
                                 chunk_length=30)

audio = decode_audio("audio.mp3", sampling_rate=model.feature_extractor.sampling_rate)
start_time = time.time()
segment_generator, info = batch.transcribe(audio,
                                           batch_size=32,
                                           beam_size=5,
                                           task="transcribe",
                                           word_timestamps=True,
                                           suppress_blank=True)
segments = []
text = ""
for segment in segment_generator:
    segments.append(segment)
    text = text + segment.text

print("--- %s seconds ---" % (time.time() - start_time))

```

## Conversion details

The original model was converted with the following command:

```
ct2-transformers-converter --model openai/whisper-large-v3-turbo --output_dir whisper-large-v3-turbo --copy_files tokenizer.json preprocessor_config.json --quantization float16
```

Note that the model weights are saved in FP16. This type can be changed when the model is loaded using the [`compute_type` option in CTranslate2](https://opennmt.net/CTranslate2/quantization.html).

## More information

**For more information about the original model, see its [model card](https://huggingface.co/openai/whisper-large-v3-turbo).**