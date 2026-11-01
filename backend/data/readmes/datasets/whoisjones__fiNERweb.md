---
language:
- vi
- ta
- or
- sk
- af
- cs
- ga
- pt
- so
- sl
- cy
- fy
- uk
- is
- la
- hy
- bg
- tr
- uz
- nl
- ps
- be
- en
- xh
- jv
- hi
- my
- br
- ur
- sr
- zh
- ka
- hr
- ml
- km
- te
- ru
- ar
- de
- fr
- om
- sw
- az
- gl
- ko
- sd
- fi
- lv
- eo
- kk
- lt
- mk
- eu
- am
- he
- si
- ne
- yi
- sq
- it
- kn
- mn
- ja
- gu
- su
- ro
- sa
- ku
- ky
- ug
- gd
- es
- et
- th
- sv
- hu
- bs
- bn
- ca
- mr
- da
- pl
- el
- ms
- mg
- pa
- lo
- fa
- tl
- as
- id
license: mit
task_categories:
- token-classification
task_ids:
- named-entity-recognition
pretty_name: fiNERweb
size_categories:
- 1M<n<10M
dataset_info:
  features:
  - name: id
    dtype: string
  - name: text
    dtype: string
  - name: char_spans
    list:
    - name: start
      dtype: int64
    - name: end
      dtype: int64
    - name: label
      dtype: string
  splits:
  - name: mal
    num_bytes: 10988079
    num_examples: 27552
  - name: fra
    num_bytes: 4793600
    num_examples: 17885
  - name: ukr
    num_bytes: 6035756
    num_examples: 20003
  - name: hin
    num_bytes: 11556081
    num_examples: 30792
  - name: xho
    num_bytes: 5930615
    num_examples: 18487
  - name: guj
    num_bytes: 9864178
    num_examples: 25568
  - name: gaz
    num_bytes: 5033472
    num_examples: 16706
  - name: kat
    num_bytes: 8956878
    num_examples: 20671
  - name: hrv
    num_bytes: 4594398
    num_examples: 18838
  - name: heb
    num_bytes: 4747085
    num_examples: 16205
  - name: cat
    num_bytes: 4411234
    num_examples: 15593
  - name: tam
    num_bytes: 10898710
    num_examples: 25519
  - name: swh
    num_bytes: 5068676
    num_examples: 16694
  - name: ces
    num_bytes: 4594695
    num_examples: 22326
  - name: hun
    num_bytes: 5567520
    num_examples: 22662
  - name: lit
    num_bytes: 4762887
    num_examples: 20819
  - name: hye
    num_bytes: 9159056
    num_examples: 25277
  - name: san
    num_bytes: 15198872
    num_examples: 48483
  - name: lat
    num_bytes: 5612705
    num_examples: 21752
  - name: kir
    num_bytes: 7013247
    num_examples: 21111
  - name: ory
    num_bytes: 11750541
    num_examples: 31800
  - name: ron
    num_bytes: 4789476
    num_examples: 18459
  - name: snd
    num_bytes: 6344942
    num_examples: 15893
  - name: ben
    num_bytes: 12581965
    num_examples: 33778
  - name: vie
    num_bytes: 4840020
    num_examples: 16319
  - name: khm
    num_bytes: 17585526
    num_examples: 7254
  - name: por
    num_bytes: 4639618
    num_examples: 17438
  - name: jav
    num_bytes: 5822270
    num_examples: 23097
  - name: mkd
    num_bytes: 6381228
    num_examples: 16600
  - name: sin
    num_bytes: 9319352
    num_examples: 20700
  - name: bul
    num_bytes: 6763389
    num_examples: 20744
  - name: rus
    num_bytes: 6315004
    num_examples: 21145
  - name: arb
    num_bytes: 7341293
    num_examples: 16814
  - name: als
    num_bytes: 4282647
    num_examples: 16278
  - name: uzn
    num_bytes: 5161601
    num_examples: 20005
  - name: som
    num_bytes: 4886400
    num_examples: 13960
  - name: slk
    num_bytes: 4535444
    num_examples: 21532
  - name: urd
    num_bytes: 11709964
    num_examples: 28469
  - name: swe
    num_bytes: 4933678
    num_examples: 22862
  - name: tha
    num_bytes: 18299284
    num_examples: 33943
  - name: cmn
    num_bytes: 16193685
    num_examples: 58081
  - name: pan
    num_bytes: 11989455
    num_examples: 26560
  - name: uig
    num_bytes: 9941561
    num_examples: 17970
  - name: yid
    num_bytes: 6648141
    num_examples: 15470
  - name: mlg
    num_bytes: 5257840
    num_examples: 17081
  - name: asm
    num_bytes: 13255321
    num_examples: 21265
  - name: pbt
    num_bytes: 6289071
    num_examples: 15945
  - name: fry
    num_bytes: 4031696
    num_examples: 19169
  - name: nld
    num_bytes: 4732850
    num_examples: 23568
  - name: lao
    num_bytes: 14486755
    num_examples: 16634
  - name: ell
    num_bytes: 6279057
    num_examples: 16767
  - name: tel
    num_bytes: 11123904
    num_examples: 29658
  - name: bre
    num_bytes: 4611079
    num_examples: 19882
  - name: fil
    num_bytes: 4700672
    num_examples: 17929
  - name: eng
    num_bytes: 5380790
    num_examples: 21227
  - name: lvs
    num_bytes: 5017112
    num_examples: 20943
  - name: ekk
    num_bytes: 5264744
    num_examples: 24011
  - name: zsm
    num_bytes: 5485790
    num_examples: 20680
  - name: khk
    num_bytes: 7397728
    num_examples: 19717
  - name: fas
    num_bytes: 6765896
    num_examples: 16912
  - name: pol
    num_bytes: 4388931
    num_examples: 20319
  - name: afr
    num_bytes: 5118702
    num_examples: 21944
  - name: npi
    num_bytes: 13798158
    num_examples: 32460
  - name: kor
    num_bytes: 8047701
    num_examples: 27262
  - name: slv
    num_bytes: 4398338
    num_examples: 19526
  - name: gle
    num_bytes: 4964082
    num_examples: 18444
  - name: ckb
    num_bytes: 7834728
    num_examples: 14946
  - name: mya
    num_bytes: 24356484
    num_examples: 10896
  - name: dan
    num_bytes: 4856403
    num_examples: 21810
  - name: ind
    num_bytes: 5811049
    num_examples: 22569
  - name: isl
    num_bytes: 4919235
    num_examples: 21210
  - name: spa
    num_bytes: 4572228
    num_examples: 15494
  - name: bos
    num_bytes: 4407762
    num_examples: 17820
  - name: jpn
    num_bytes: 14998998
    num_examples: 49948
  - name: gla
    num_bytes: 4700957
    num_examples: 18237
  - name: cym
    num_bytes: 4438189
    num_examples: 17779
  - name: amh
    num_bytes: 11478123
    num_examples: 26246
  - name: tur
    num_bytes: 5674709
    num_examples: 21376
  - name: srp
    num_bytes: 3710767
    num_examples: 16374
  - name: eus
    num_bytes: 5243815
    num_examples: 22329
  - name: kan
    num_bytes: 10914954
    num_examples: 25603
  - name: azj
    num_bytes: 5303089
    num_examples: 20548
  - name: deu
    num_bytes: 5442292
    num_examples: 23301
  - name: epo
    num_bytes: 5242581
    num_examples: 21662
  - name: kaz
    num_bytes: 7707638
    num_examples: 24845
  - name: ita
    num_bytes: 4618930
    num_examples: 17663
  - name: mar
    num_bytes: 10499156
    num_examples: 28353
  - name: sun
    num_bytes: 5598614
    num_examples: 20384
  - name: glg
    num_bytes: 4709154
    num_examples: 15734
  - name: fin
    num_bytes: 5166172
    num_examples: 26286
  - name: bel
    num_bytes: 6195546
    num_examples: 19894
  download_size: 270832118
  dataset_size: 677042018
configs:
- config_name: default
  data_files:
  - split: mal
    path: data/mal-*
  - split: fra
    path: data/fra-*
  - split: ukr
    path: data/ukr-*
  - split: hin
    path: data/hin-*
  - split: xho
    path: data/xho-*
  - split: guj
    path: data/guj-*
  - split: gaz
    path: data/gaz-*
  - split: kat
    path: data/kat-*
  - split: hrv
    path: data/hrv-*
  - split: heb
    path: data/heb-*
  - split: cat
    path: data/cat-*
  - split: tam
    path: data/tam-*
  - split: swh
    path: data/swh-*
  - split: ces
    path: data/ces-*
  - split: hun
    path: data/hun-*
  - split: lit
    path: data/lit-*
  - split: hye
    path: data/hye-*
  - split: san
    path: data/san-*
  - split: lat
    path: data/lat-*
  - split: kir
    path: data/kir-*
  - split: ory
    path: data/ory-*
  - split: ron
    path: data/ron-*
  - split: snd
    path: data/snd-*
  - split: ben
    path: data/ben-*
  - split: vie
    path: data/vie-*
  - split: khm
    path: data/khm-*
  - split: por
    path: data/por-*
  - split: jav
    path: data/jav-*
  - split: mkd
    path: data/mkd-*
  - split: sin
    path: data/sin-*
  - split: bul
    path: data/bul-*
  - split: rus
    path: data/rus-*
  - split: arb
    path: data/arb-*
  - split: als
    path: data/als-*
  - split: uzn
    path: data/uzn-*
  - split: som
    path: data/som-*
  - split: slk
    path: data/slk-*
  - split: urd
    path: data/urd-*
  - split: swe
    path: data/swe-*
  - split: tha
    path: data/tha-*
  - split: cmn
    path: data/cmn-*
  - split: pan
    path: data/pan-*
  - split: uig
    path: data/uig-*
  - split: yid
    path: data/yid-*
  - split: mlg
    path: data/mlg-*
  - split: asm
    path: data/asm-*
  - split: pbt
    path: data/pbt-*
  - split: fry
    path: data/fry-*
  - split: nld
    path: data/nld-*
  - split: lao
    path: data/lao-*
  - split: ell
    path: data/ell-*
  - split: tel
    path: data/tel-*
  - split: bre
    path: data/bre-*
  - split: fil
    path: data/fil-*
  - split: eng
    path: data/eng-*
  - split: lvs
    path: data/lvs-*
  - split: ekk
    path: data/ekk-*
  - split: zsm
    path: data/zsm-*
  - split: khk
    path: data/khk-*
  - split: fas
    path: data/fas-*
  - split: pol
    path: data/pol-*
  - split: afr
    path: data/afr-*
  - split: npi
    path: data/npi-*
  - split: kor
    path: data/kor-*
  - split: slv
    path: data/slv-*
  - split: gle
    path: data/gle-*
  - split: ckb
    path: data/ckb-*
  - split: mya
    path: data/mya-*
  - split: dan
    path: data/dan-*
  - split: ind
    path: data/ind-*
  - split: isl
    path: data/isl-*
  - split: spa
    path: data/spa-*
  - split: bos
    path: data/bos-*
  - split: jpn
    path: data/jpn-*
  - split: gla
    path: data/gla-*
  - split: cym
    path: data/cym-*
  - split: amh
    path: data/amh-*
  - split: tur
    path: data/tur-*
  - split: srp
    path: data/srp-*
  - split: eus
    path: data/eus-*
  - split: kan
    path: data/kan-*
  - split: azj
    path: data/azj-*
  - split: deu
    path: data/deu-*
  - split: epo
    path: data/epo-*
  - split: kaz
    path: data/kaz-*
  - split: ita
    path: data/ita-*
  - split: mar
    path: data/mar-*
  - split: sun
    path: data/sun-*
  - split: glg
    path: data/glg-*
  - split: fin
    path: data/fin-*
  - split: bel
    path: data/bel-*
- config_name: mal
  data_files: "data/mal-*"
- config_name: fra
  data_files: "data/fra-*"
- config_name: ukr
  data_files: "data/ukr-*"
- config_name: hin
  data_files: "data/hin-*"
- config_name: xho
  data_files: "data/xho-*"
- config_name: guj
  data_files: "data/guj-*"
- config_name: gaz
  data_files: "data/gaz-*"
- config_name: kat
  data_files: "data/kat-*"
- config_name: hrv
  data_files: "data/hrv-*"
- config_name: heb
  data_files: "data/heb-*"
- config_name: cat
  data_files: "data/cat-*"
- config_name: tam
  data_files: "data/tam-*"
- config_name: swh
  data_files: "data/swh-*"
- config_name: ces
  data_files: "data/ces-*"
- config_name: hun
  data_files: "data/hun-*"
- config_name: lit
  data_files: "data/lit-*"
- config_name: hye
  data_files: "data/hye-*"
- config_name: san
  data_files: "data/san-*"
- config_name: lat
  data_files: "data/lat-*"
- config_name: kir
  data_files: "data/kir-*"
- config_name: ory
  data_files: "data/ory-*"
- config_name: ron
  data_files: "data/ron-*"
- config_name: snd
  data_files: "data/snd-*"
- config_name: ben
  data_files: "data/ben-*"
- config_name: vie
  data_files: "data/vie-*"
- config_name: khm
  data_files: "data/khm-*"
- config_name: por
  data_files: "data/por-*"
- config_name: jav
  data_files: "data/jav-*"
- config_name: mkd
  data_files: "data/mkd-*"
- config_name: sin
  data_files: "data/sin-*"
- config_name: bul
  data_files: "data/bul-*"
- config_name: rus
  data_files: "data/rus-*"
- config_name: arb
  data_files: "data/arb-*"
- config_name: als
  data_files: "data/als-*"
- config_name: uzn
  data_files: "data/uzn-*"
- config_name: som
  data_files: "data/som-*"
- config_name: slk
  data_files: "data/slk-*"
- config_name: urd
  data_files: "data/urd-*"
- config_name: swe
  data_files: "data/swe-*"
- config_name: tha
  data_files: "data/tha-*"
- config_name: cmn
  data_files: "data/cmn-*"
- config_name: pan
  data_files: "data/pan-*"
- config_name: uig
  data_files: "data/uig-*"
- config_name: yid
  data_files: "data/yid-*"
- config_name: mlg
  data_files: "data/mlg-*"
- config_name: asm
  data_files: "data/asm-*"
- config_name: pbt
  data_files: "data/pbt-*"
- config_name: fry
  data_files: "data/fry-*"
- config_name: nld
  data_files: "data/nld-*"
- config_name: lao
  data_files: "data/lao-*"
- config_name: ell
  data_files: "data/ell-*"
- config_name: tel
  data_files: "data/tel-*"
- config_name: bre
  data_files: "data/bre-*"
- config_name: fil
  data_files: "data/fil-*"
- config_name: eng
  data_files: "data/eng-*"
- config_name: lvs
  data_files: "data/lvs-*"
- config_name: ekk
  data_files: "data/ekk-*"
- config_name: zsm
  data_files: "data/zsm-*"
- config_name: khk
  data_files: "data/khk-*"
- config_name: fas
  data_files: "data/fas-*"
- config_name: pol
  data_files: "data/pol-*"
- config_name: afr
  data_files: "data/afr-*"
- config_name: npi
  data_files: "data/npi-*"
- config_name: kor
  data_files: "data/kor-*"
- config_name: slv
  data_files: "data/slv-*"
- config_name: gle
  data_files: "data/gle-*"
- config_name: ckb
  data_files: "data/ckb-*"
- config_name: mya
  data_files: "data/mya-*"
- config_name: dan
  data_files: "data/dan-*"
- config_name: ind
  data_files: "data/ind-*"
- config_name: isl
  data_files: "data/isl-*"
- config_name: spa
  data_files: "data/spa-*"
- config_name: bos
  data_files: "data/bos-*"
- config_name: jpn
  data_files: "data/jpn-*"
- config_name: gla
  data_files: "data/gla-*"
- config_name: cym
  data_files: "data/cym-*"
- config_name: amh
  data_files: "data/amh-*"
- config_name: tur
  data_files: "data/tur-*"
- config_name: srp
  data_files: "data/srp-*"
- config_name: eus
  data_files: "data/eus-*"
- config_name: kan
  data_files: "data/kan-*"
- config_name: azj
  data_files: "data/azj-*"
- config_name: deu
  data_files: "data/deu-*"
- config_name: epo
  data_files: "data/epo-*"
- config_name: kaz
  data_files: "data/kaz-*"
- config_name: ita
  data_files: "data/ita-*"
- config_name: mar
  data_files: "data/mar-*"
- config_name: sun
  data_files: "data/sun-*"
- config_name: glg
  data_files: "data/glg-*"
- config_name: fin
  data_files: "data/fin-*"
- config_name: bel
  data_files: "data/bel-*"
---

# fiNERweb

## Dataset Description

fiNERweb is a multilingual named entity recognition dataset containing annotated text in multiple languages. Each example contains:
- Original text
- Character spans for entities

## Dataset Structure

Each example contains:
```python
{
    "text": str,  # Original text
    "char_spans": List[Dict],  # Character-level entity spans
}
```

## Usage

```python
from datasets import load_dataset
dataset = load_dataset("whoisjones/fiNERweb", "eng")  # For English

# Access the data
print(dataset["train"][0])
```

## Citation

If you use this dataset, please cite:
```bibtex
@misc{golde2025finerwebdatasetsartifactsscalable,
      title={FiNERweb: Datasets and Artifacts for Scalable Multilingual Named Entity Recognition}, 
      author={Jonas Golde and Patrick Haller and Alan Akbik},
      year={2025},
      eprint={2512.13884},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2512.13884}, 
}
```

## Languages

- mal: Malayalam
- fra: French
- ukr: Ukrainian
- hin: Hindi
- xho: Xhosa
- guj: Gujarati
- gaz: Oromo (West Central Oromo)
- kat: Georgian
- hrv: Croatian
- heb: Hebrew
- cat: Catalan
- tam: Tamil
- swh: Swahili
- ces: Czech
- hun: Hungarian
- lit: Lithuanian
- hye: Armenian
- san: Sanskrit
- lat: Latin
- kir: Kyrgyz
- ory: Odia (Oriya)
- ron: Romanian
- snd: Sindhi
- ben: Bengali
- vie: Vietnamese
- khm: Khmer
- por: Portuguese
- jav: Javanese
- mkd: Macedonian
- sin: Sinhala
- bul: Bulgarian
- rus: Russian
- arb: Arabic (Modern Standard)
- als: Alemannic German
- uzn: Uzbek (Northern)
- som: Somali
- slk: Slovak
- urd: Urdu
- swe: Swedish
- tha: Thai
- cmn: Mandarin Chinese
- pan: Punjabi
- uig: Uyghur
- yid: Yiddish
- mlg: Malagasy
- asm: Assamese
- pbt: Pashto (Southern)
- fry: Western Frisian
- nld: Dutch
- lao: Lao
- ell: Greek (Modern)
- tel: Telugu
- bre: Breton
- fil: Filipino
- eng: English
- lvs: Latvian
- ekk: Estonian
- zsm: Malay (Standard)
- khk: Mongolian (Khalkha)
- fas: Persian (Farsi)
- pol: Polish
- afr: Afrikaans
- npi: Nepali
- kor: Korean
- slv: Slovenian
- gle: Irish
- ckb: Kurdish (Central, Sorani)
- mya: Burmese
- dan: Danish
- ind: Indonesian
- isl: Icelandic
- spa: Spanish
- bos: Bosnian
- jpn: Japanese
- gla: Scottish Gaelic
- cym: Welsh
- amh: Amharic
- tur: Turkish
- srp: Serbian
- eus: Basque
- kan: Kannada
- azj: Azerbaijani (North)
- deu: German
- epo: Esperanto
- kaz: Kazakh
- ita: Italian
- mar: Marathi
- sun: Sundanese
- glg: Galician
- fin: Finnish
- bel: Belarusian
