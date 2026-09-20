---
library_name: transformers
license: cc-by-4.0
datasets:
- google/WaxalNLP
metrics:
- wer
- cer
language:
- am
- ti
- om
base_model:
- facebook/w2v-bert-2.0
pipeline_tag: automatic-speech-recognition
tags:
- multilingual
---

<!-- <div align="center" style="line-height: 1; transform: scale(1.5);">
<h2> Automatic Speech Recognition for Ethiopian Languages 🇪🇹
</div> -->

<div align="center">
<img src="ethio-asr-logo.png" alt="Ethio-ASR Logo" width="600">
</div>
    
<div align="center" style="line-height: 1; transform: scale(1.4);">
  <a href="https://huggingface.co/datasets/google/WaxalNLP" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-ffc107?color=ffca28&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  <a href="https://huggingface.co/spaces/badrex/Ethio-ASR-multilingual-demo" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-ffc107?color=c62828&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  <a href="https://creativecommons.org/licenses/by/4.0/deed.en" style="margin: 2px;">
    <img alt="License" src="https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<h3 style="text-align: center; font-size: 24px; color:#C70039;">
arXiv 📖 <a href="https://arxiv.org/pdf/2603.23654">[ preprint ]</a>
</h3>

## ⚒️ Model Description 

Ethio-ASR is a suite of multilingual Automatic Speech Recognition (ASR) models that support five Ethiopian languages: Amharic, Tigrinya, Afaan Oromo, Sidama, and Wolaytta. 
The ASR model in this repo is based on the [wav2vec2‑bert-2.0](https://huggingface.co/facebook/w2v-bert-2.0) pre-trained model by fine-tuning it on the [WAXAL Speech Dataset](https://huggingface.co/datasets/google/WaxalNLP).

- **Developed by:** Ethio-ASR Team
- **Task:** Speech Recognition (ASR) and Language Identification (LID)
- **Languages:** Amharic, Tigrinya, Afaan Oromo, Sidama, and Wolaytta
- **License:** CC-BY-4.0
- **Finetuned from:** facebook/w2v-bert-2.0


## 📈 Evaluation on WAXAL Test Set
*📌 ASR model in this HF repo*
| Model | # Params | Amharic | Tigrinya | Oromo | Wolaytta | Sidaama | Avg. |
|------|----------|----------|-----------|--------|-----------|----------|------|
| Ethio-ASR (afrihubert) | 92M | 30.95 | 42.42 | 27.57 | 40.44 | 34.02 | 35.08 |
| Ethio-ASR (mms-300) | 300M | 30.19 | 41.62 | 26.41 | 39.10 | 32.66 | 33.99 |
| Ethio-ASR (mms-1b) | 1B | 26.14 | 37.63 | **23.69** | **37.51** | **31.02** | 31.20 |
| **Ethio-ASR (w2v-bert-2.0)** 📌 | 600M | **22.92** | **35.22** | 24.44 | 38.19 | 31.65 | **30.48** | 



## 🚀 Examples 
|  | Language | Audio | Human Transcription | ASR Transcription |
|----------|----------------------|--------|----------------|----------------|
| 1 | Oromo | <audio controls src="https://huggingface.co/spaces/badrex/Ethio-ASR-multilingual/resolve/main/examples/DbtqAzRPsJ2XbDuH7sXe.wav"></audio> | Suuraan asii gaditti argaa jirru kun lafa gurgurtaa kuduraa fi muduraa dha. Kuduraa fi muduraan nyaataaf kan baay'ee namatti toluudha. Nyaachuudhaaf illee kuduraa fi muduraan baay'ee filataamaa dha. Kanaaf, kuduraa fi muduraa kana baay'een jaalladha. Baay'ee nyaachuuf illee baay'een fedha guddaa qaba. | [ORM] suurran asii gaditti argaa jirru kun lafa gurgurtaa kuduraafi muduraadha. kuduraaf muduraa nyaataaf kan baay'ee namatti toludha. nyaachuudhaaf illee kuduraaf muduraan baay'ee filatamaadha. kanaaf kuduraaf muduraa kan baay'een jaalladha baay'ee nyaachuuf illee baay'een fedha guddaa qaba. |
| 2 | Amharic | <audio controls src="https://huggingface.co/spaces/badrex/Ethio-ASR-multilingual/resolve/main/examples/0ToRFBqckIvUuytPUE2n.wav"></audio> | ሰዎች ቤታቸውን ለማስጌጥ የተለያዩ ጨርቆችን ይጠቀማሉ። ጨርቆች ቤቶችን ለማስጌጥ የሚጠቅሙት የተለያዩ የቅርፅ በመስጠት፣ እንደ ዚግዛግ ቅርጽ በማስደርግ፣ እንደ ቢራቢሮ ነገሮችን በመስራት፣ ግድግዳ ላይ በመለጠፍ፣ በማንጠልጠል ለቤቱ ውበት ይሰጣሉ። | [AMH] ሰሰዎች ቤታቸውን ለማስጌጥ የተለያዩ ጨርቆችን ይጠቀማሉ። ጨርቆች ቤቶችን ለማስጌጥ የሚጠቅሙት የተለያየ ቅርጽ በመስጠት እንደ ዚግዛግ ቅርጽ በማስደረግ እንደ ቢራ ቢሮ ነገሮችን በመስራት ግድግዳ ላይ በመለጠፍ በማንጠልጠል ለቤቱ ውበት ይሰጣሉ። |
| 3 | Wolaytta | <audio controls src="https://huggingface.co/spaces/badrex/Ethio-ASR-multilingual/resolve/main/examples/0TwCoHqIQxM1wuAtvrHB.wav"></audio> | Issi heeraani asaa naatussi dumma dumma ayfiyan be'iyobati de'oososna. Hegeetuppekka meretaanne merettaa heeraara gayttiyabata be'iyaba gidikko issi heeraani mitatta woykko dumma dumma adil'e ciishshata be'iyode keehippe lo'oosonanne ubbakka ufaysoosona. | [WAL] issi heeran asaa naatussi dumma dumma ayfiyan be'iyobati de'oosona. hegeetuppekka meretaanne meretaa heeraara gayttiyaabata be'iyaaba gidikko issi heeran mittata woykko dumma dumma adile ciishshabata be'iyode keehippe lo'oosonanne ubbakka ufayssoosona. |
| 4 | Tigrinya | <audio controls src="https://huggingface.co/spaces/badrex/Ethio-ASR-multilingual/resolve/main/examples/0J1gXqu5KM7shtOIxGu8.wav"></audio> | እዙይ እንርእዮ ዘለና ምስሊ ናይ ደመራ ምስሊ እንትከውን ኣብ ባዓል መስቀል ዝክበር ብዓል እዩ። ሃይማኖታዊ ብዓልን ባህላዊ ሂደት ዘለዎ ገይሩ ዝካየድ እዩ። ካብ ዝተፈላለየ ዓይነት ሓሰራት ዕንፀይትታት ብምእካብ ዝቃፀል ዓብዪ ባህላዊን ሃይማኖታውን ዝኮነ ብዓል እዩ። | [TIR] እዚ እንሪኦ ዘለና ምስሊ ናይ ደመራ ምስሊ እንትኸውን ኣብ በዓል መስቀል ዝኽበር በዓል እዩ። ሃይማኖታዊ በዓልን ባህላውን ሂደት ዘለዎ  ዝካየድ እዩ። ካብ ዝተፈላለዩ ዓይነት ሓሰራት ዕንጨይትታት ብምእካብ ዝቃፀል ዓብይ ባህላዊን ሃይማኖታውን ዝኮነ በዓል እዩ። |
| 5 | Oromo | <audio controls src="https://huggingface.co/spaces/badrex/Ethio-ASR-multilingual/resolve/main/examples/3GOOx4V3enU2uq05o8L1.wav"></audio> | Fakkii kanarraa kan arginu hangafa Oromoo kan ta’e godina Booranaa keessatti uffata naannoo godina Booranaatiin faayamanii abbootiin bokkuu isaanii qabatanii, haadholiin immoo siinqee isaanii qabatanii kan dhaabbachaa jiranidha. | [ORM] fakkii kanarraa kan arginu hangafa oromoo kan ta'e godina booranaa keessatti uffata naannoo godina booranaatiin faayamanii abbootiin bokkuu isaanii qabatanii haadholiin immoo siiqee isaanii qabatanii kan dhaabbachaa jiranidha. |
| 6 | Sidaama | <audio controls src="https://huggingface.co/spaces/badrex/Ethio-ASR-multilingual/resolve/main/examples/02wm5tT3zBP4aXNSeQJ4.wav"></audio> | Daganna maate yaa mayyaate? Daganna maate yee su'ma fushshihu ayeeti? Daganna maate hiiko heedhanno? Daganna maate yinihu mayiraati? Daganna maate ayira horo uyitanno? | [SID] daganna maate yaa mayyaate? daganna maate yee su'ma fushshihu ayeeti? daganna maate hiikko heedhanno? daganna maate yinihu mayraati? daganna maate ayira horo uyitanno |


## 🎧 Direct Use

``` python
from transformers import AutoModelForCTC, AutoProcessor
import torchaudio, torch

processor = AutoProcessor.from_pretrained("badrex/Ethio-ASR-multilingual-600M")
model = AutoModelForCTC.from_pretrained("badrex/Ethio-ASR-multilingual-600M")

audio, sr = torchaudio.load("audio.wav")
inputs = processor(audio.squeeze(), sampling_rate=sr, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits

pred_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(pred_ids)[0]

print(transcription)
```

## 🔧 Downstream Use

-   Voice assistants
-   Accessibility tools
-   Research baselines

## 🚫 Out‑of‑Scope Use

-   Languages outside Amharic, Tigrinya, Afaan Oromo, Sidama, and Wolaytta.
-   High‑stakes deployments without human review
-   Noisy audio without speech enhancement 


## ⚠️ Risks & Limitations

Performance might vary across dialects, genders, ages, and recording quality.



## 📌 Citation

``` bibtex
@misc{ethio_asr_2026,
  author = {
    Abdullah, Badr M. and
    Azime, Israel Abebe and
    Tonja, Atnafu Lambebo and
    Alabi, Jesujoba O. and
    Alemu, Abel Mulat and
    Hagos, Eyob G. and
    Balcha, Bontu Fufa and
    Nerea, Mulubrhan A. and
    Yadeta, Debela Desalegn and
    Marilign, Dagnachew Mekonnen and
    Fentahun, Amanuel Temesgen and
    Kebede, Tadesse and
    Gebru, Israel D. and
    Woldeyohannis, Michael Melese and
    Sewunetie, Walelign Tewabe and
    Möbius, Bernd and
    Klakow, Dietrich
  },
  title = {Ethio-ASR: Joint Multilingual Speech Recognition and Language Identification for Ethiopian Languages},
  year = {2026},
  howpublished = {\url{https://huggingface.co/badrex/Ethio-ASR-multilingual-600M}}
}
```