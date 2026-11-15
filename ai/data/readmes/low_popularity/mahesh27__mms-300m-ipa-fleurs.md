---
license: apache-2.0
language:
- afr
- amh
- ara
- ast
- aze
- bel
- bul
- ben
- cat
- ceb
- ckb
- cmn
- ces
- cym
- dan
- deu
- ell
- eng
- spa
- est
- fas
- ful
- fin
- fra
- gle
- glg
- hau
- heb
- hin
- hrv
- hun
- hye
- ind
- ita
- jpn
- jav
- kat
- kaz
- khm
- kan
- kor
- kir
- lug
- lao
- lit
- lav
- mri
- mkd
- mal
- mon
- mar
- msa
- mlt
- mya
- nob
- nep
- nld
- nya
- orm
- ori
- pan
- pol
- pus
- por
- ron
- rus
- slv
- sna
- som
- swe
- swa
- tam
- tel
- tgk
- tha
- tur
- ukr
- urd
- uzb
- vie
- wol
- xho
- yor
- yue
- zul
datasets:
- google/fleurs
- mahesh27/fleurs-ipa
base_model:
- facebook/mms-300m
pipeline_tag: automatic-speech-recognition
---

Phoneme model (IPA) for 85 languages from FLEURS. 

### Example Usage

```python
import os
import torch
from datasets import load_dataset
from transformers import AutoProcessor, AutoModelForCTC


MODEL = "mahesh27/mms-300m-ipa-fleurs"
LANG = "de_de"


# 1. Load model and German adapter
processor = AutoProcessor.from_pretrained(MODEL)
model = AutoModelForCTC.from_pretrained(MODEL, device_map="auto")

model.load_adapter(LANG)
model.eval()


# 2. Get first German test utterance from Google FLEURS
fleurs_audio = load_dataset(
    "google/fleurs",
    LANG,
    split="test",
    streaming=True,
)

sample = next(iter(fleurs_audio))

audio = sample["audio"]["array"]
sample_rate = sample["audio"]["sampling_rate"]



# 3. Load FLEURS-IPA completely and find matching utterance
fleurs_ipa = load_dataset("mahesh27/fleurs-ipa", split="test")

audio_filename = os.path.basename(sample["audio"]["path"])

match = fleurs_ipa.filter(
    lambda x: x["audio_file"] == audio_filename and x["id"] == sample["id"]
)[0]

print("\nGold IPA:")
print(match['ipa'])

print("\nGold Word Segmented:")
print(match['word_segmented'])


# 4. Run the audio through the model
inputs = processor(
    audio,
    sampling_rate=sample_rate,
    return_tensors="pt",
)

inputs = {
    k: v.to(model.device)
    for k, v in inputs.items()
}

with torch.inference_mode():
    logits = model(**inputs).logits

pred_ids = torch.argmax(logits, dim=-1)
prediction = processor.batch_decode(pred_ids)[0]

print("\nPrediction:")
print(prediction)
```

```
Gold IPA:
fyʁ diː bestən ausixtən auf hoŋkkoŋ soltən siː diː insel feɐlasən und t͡sum ɡeːɡənyːbeɐliːɡəndən uːfeʁ fon kovloːn faːʀən

Gold Word Segmented:
für die besten aussichten auf hongkong sollten sie die insel verlassen und zum gegenüberliegenden ufer von kowloon fahren

Prediction:
fyʁ diː bestən aussixtən auf ʁonkoŋɡ soltən siː diː insel feɐlasən undt͡sum ɡeːɡeːnyːbeɐleːɡəndən uːfeʁ fon koflun faːʀən
```

Alignments can be performed using [ctc-segmentation](https://github.com/lumaku/ctc-segmentation) (following Wav2vec2 example code under 'Usage')

### Citation

```
@inproceedings{akavarapu-etal-2026-phoneme,
    title = "Phoneme- and Word-Level Metrics Using Self-Supervised Speech Representations for Forced Alignment Evaluation",
    author = {Akavarapu, V.S.D.S.Mahesh  and
      Daniel, Michael  and
      J{\"a}ger, Gerhard},
    editor = "Lee, Hung-Yi  and
      Dev, Sunipa  and
      Li, Jessy  and
      Elliott, Desmond",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {EMNLP} 2026",
    month = oct,
    year = "2026",
    address = "Budapest, Hungary",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-emnlp.279/",
    pages = "5865--5892",
    ISBN = "979-8-89176-462-0",
}
```