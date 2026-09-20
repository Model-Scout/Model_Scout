---
tags:
- mms
language:
- ab
- af
- ak
- am
- ar
- as
- av
- ay
- az
- ba
- bm
- be
- bn
- bi
- bo
- sh
- br
- bg
- ca
- cs
- ce
- cv
- ku
- cy
- da
- de
- dv
- dz
- el
- en
- eo
- et
- eu
- ee
- fo
- fa
- fj
- fi
- fr
- fy
- ff
- ga
- gl
- gn
- gu
- zh
- ht
- ha
- he
- hi
- sh
- hu
- hy
- ig
- ia
- ms
- is
- it
- jv
- ja
- kn
- ka
- kk
- kr
- km
- ki
- rw
- ky
- ko
- kv
- lo
- la
- lv
- ln
- lt
- lb
- lg
- mh
- ml
- mr
- ms
- mk
- mg
- mt
- mn
- mi
- my
- zh
- nl
- 'no'
- 'no'
- ne
- ny
- oc
- om
- or
- os
- pa
- pl
- pt
- ms
- ps
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- qu
- ro
- rn
- ru
- sg
- sk
- sl
- sm
- sn
- sd
- so
- es
- sq
- su
- sv
- sw
- ta
- tt
- te
- tg
- tl
- th
- ti
- ts
- tr
- uk
- ms
- vi
- wo
- xh
- ms
- yo
- ms
- zu
- za
license: cc-by-nc-4.0
datasets:
- google/fleurs
metrics:
- wer
---

# Massively Multilingual Speech (MMS) - Finetuned ASR - FL102

This checkpoint is a model fine-tuned for multi-lingual ASR and part of Facebook's [Massive Multilingual Speech project](https://research.facebook.com/publications/scaling-speech-technology-to-1000-languages/).
This checkpoint is based on the [Wav2Vec2 architecture](https://huggingface.co/docs/transformers/model_doc/wav2vec2) and makes use of adapter models to transcribe 100+ languages.
The checkpoint consists of **1 billion parameters** and has been fine-tuned from [facebook/mms-1b](https://huggingface.co/facebook/mms-1b) on 102 languages of [Fleurs](https://huggingface.co/datasets/google/fleurs).

## Table Of Content

- [Example](#example)
- [Supported Languages](#supported-languages)
- [Model details](#model-details)
- [Additional links](#additional-links)

## Example

This MMS checkpoint can be used with [Transformers](https://github.com/huggingface/transformers) to transcribe audio of 1107 different 
languages. Let's look at a simple example.

First, we install transformers and some other libraries
```
pip install torch accelerate torchaudio datasets
pip install --upgrade transformers
````

**Note**: In order to use MMS you need to have at least `transformers >= 4.30` installed. If the `4.30` version
is not yet available [on PyPI](https://pypi.org/project/transformers/) make sure to install `transformers` from 
source:
```
pip install git+https://github.com/huggingface/transformers.git
```

Next, we load a couple of audio samples via `datasets`. Make sure that the audio data is sampled to 16000 kHz.

```py
from datasets import load_dataset, Audio

# English
stream_data = load_dataset("mozilla-foundation/common_voice_13_0", "en", split="test", streaming=True)
stream_data = stream_data.cast_column("audio", Audio(sampling_rate=16000))
en_sample = next(iter(stream_data))["audio"]["array"]

# French
stream_data = load_dataset("mozilla-foundation/common_voice_13_0", "fr", split="test", streaming=True)
stream_data = stream_data.cast_column("audio", Audio(sampling_rate=16000))
fr_sample = next(iter(stream_data))["audio"]["array"]
```

Next, we load the model and processor

```py
from transformers import Wav2Vec2ForCTC, AutoProcessor
import torch

model_id = "facebook/mms-1b-fl102"

processor = AutoProcessor.from_pretrained(model_id)
model = Wav2Vec2ForCTC.from_pretrained(model_id)
```

Now we process the audio data, pass the processed audio data to the model and transcribe the model output, just like we usually do for Wav2Vec2 models such as [facebook/wav2vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h)

```py
inputs = processor(en_sample, sampling_rate=16_000, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs).logits

ids = torch.argmax(outputs, dim=-1)[0]
transcription = processor.decode(ids)
# 'joe keton disapproved of films and buster also had reservations about the media'
```

We can now keep the same model in memory and simply switch out the language adapters by calling the convenient [`load_adapter()`]() function for the model and [`set_target_lang()`]() for the tokenizer. We pass the target language as an input - "fra" for French.

```py
processor.tokenizer.set_target_lang("fra")
model.load_adapter("fra")

inputs = processor(fr_sample, sampling_rate=16_000, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs).logits

ids = torch.argmax(outputs, dim=-1)[0]
transcription = processor.decode(ids)
# "ce dernier est volé tout au long de l'histoire romaine"
```

In the same way the language can be switched out for all other supported languages. Please have a look at:
```py
processor.tokenizer.vocab.keys()
```

For more details, please have a look at [the official docs](https://huggingface.co/docs/transformers/main/en/model_doc/mms).

## Supported Languages

This model supports 102 languages. Unclick the following to toogle all supported languages of this checkpoint in [ISO 639-3 code](https://en.wikipedia.org/wiki/ISO_639-3).
You can find more details about the languages and their ISO 649-3 codes in the [MMS Language Coverage Overview](https://dl.fbaipublicfiles.com/mms/misc/language_coverage_mms.html).
<details>
  <summary>Click to toggle</summary>

- afr
- amh
- ara
- asm
- ast
- azj-script_latin
- bel
- ben
- bos
- bul
- cat
- ceb
- ces
- ckb
- cmn-script_simplified
- cym
- dan
- deu
- ell
- eng
- est
- fas
- fin
- fra
- ful
- gle
- glg
- guj
- hau
- heb
- hin
- hrv
- hun
- hye
- ibo
- ind
- isl
- ita
- jav
- jpn
- kam
- kan
- kat
- kaz
- kea
- khm
- kir
- kor
- lao
- lav
- lin
- lit
- ltz
- lug
- luo
- mal
- mar
- mkd
- mlt
- mon
- mri
- mya
- nld
- nob
- npi
- nso
- nya
- oci
- orm
- ory
- pan
- pol
- por
- pus
- ron
- rus
- slk
- slv
- sna
- snd
- som
- spa
- srp-script_latin
- swe
- swh
- tam
- tel
- tgk
- tgl
- tha
- tur
- ukr
- umb
- urd-script_arabic
- uzb-script_latin
- vie
- wol
- xho
- yor
- yue-script_traditional
- zlm
- zul

</details>

## Model details

- **Developed by:** Vineel Pratap et al.
- **Model type:** Multi-Lingual Automatic Speech Recognition model
- **Language(s):** 100+ languages, see [supported languages](#supported-languages)
- **License:** CC-BY-NC 4.0 license
- **Num parameters**: 1 billion
- **Audio sampling rate**: 16,000 kHz
- **Cite as:**

      @article{pratap2023mms,
        title={Scaling Speech Technology to 1,000+ Languages},
        author={Vineel Pratap and Andros Tjandra and Bowen Shi and Paden Tomasello and Arun Babu and Sayani Kundu and Ali Elkahky and Zhaoheng Ni and Apoorv Vyas and Maryam Fazel-Zarandi and Alexei Baevski and Yossi Adi and Xiaohui Zhang and Wei-Ning Hsu and Alexis Conneau and Michael Auli},
      journal={arXiv},
      year={2023}
      }

## Additional Links

- [Blog post](https://ai.facebook.com/blog/multilingual-model-speech-recognition/)
- [Transformers documentation](https://huggingface.co/docs/transformers/main/en/model_doc/mms).
- [Paper](https://arxiv.org/abs/2305.13516)
- [GitHub Repository](https://github.com/facebookresearch/fairseq/tree/main/examples/mms#asr)
- [Other **MMS** checkpoints](https://huggingface.co/models?other=mms)
- MMS base checkpoints:
  - [facebook/mms-1b](https://huggingface.co/facebook/mms-1b)
  - [facebook/mms-300m](https://huggingface.co/facebook/mms-300m)
- [Official Space](https://huggingface.co/spaces/facebook/MMS)
