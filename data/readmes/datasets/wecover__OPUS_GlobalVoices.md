---
configs:
- config_name: default
  data_files:
  - split: train
    path: '*/*/train.parquet'
  - split: valid
    path: '*/*/valid.parquet'
  - split: test
    path: '*/*/test.parquet'
- config_name: am
  data_files:
  - split: train
    path: '*/*am*/train.parquet'
  - split: test
    path: '*/*am*/test.parquet'
  - split: valid
    path: '*/*am*/valid.parquet'
- config_name: ar
  data_files:
  - split: train
    path: '*/*ar*/train.parquet'
  - split: test
    path: '*/*ar*/test.parquet'
  - split: valid
    path: '*/*ar*/valid.parquet'
- config_name: bn
  data_files:
  - split: train
    path: '*/*bn*/train.parquet'
  - split: test
    path: '*/*bn*/test.parquet'
  - split: valid
    path: '*/*bn*/valid.parquet'
- config_name: ca
  data_files:
  - split: train
    path: '*/*ca*/train.parquet'
  - split: test
    path: '*/*ca*/test.parquet'
  - split: valid
    path: '*/*ca*/valid.parquet'
- config_name: de
  data_files:
  - split: train
    path: '*/*de*/train.parquet'
  - split: test
    path: '*/*de*/test.parquet'
  - split: valid
    path: '*/*de*/valid.parquet'
- config_name: el
  data_files:
  - split: train
    path: '*/*el*/train.parquet'
  - split: test
    path: '*/*el*/test.parquet'
  - split: valid
    path: '*/*el*/valid.parquet'
- config_name: en
  data_files:
  - split: train
    path: '*/*en*/train.parquet'
  - split: test
    path: '*/*en*/test.parquet'
  - split: valid
    path: '*/*en*/valid.parquet'
- config_name: es
  data_files:
  - split: train
    path: '*/*es*/train.parquet'
  - split: test
    path: '*/*es*/test.parquet'
  - split: valid
    path: '*/*es*/valid.parquet'
- config_name: fa
  data_files:
  - split: train
    path: '*/*fa*/train.parquet'
  - split: test
    path: '*/*fa*/test.parquet'
  - split: valid
    path: '*/*fa*/valid.parquet'
- config_name: fr
  data_files:
  - split: train
    path: '*/*fr*/train.parquet'
  - split: test
    path: '*/*fr*/test.parquet'
  - split: valid
    path: '*/*fr*/valid.parquet'
- config_name: hi
  data_files:
  - split: train
    path: '*/*hi*/train.parquet'
  - split: test
    path: '*/*hi*/test.parquet'
  - split: valid
    path: '*/*hi*/valid.parquet'
- config_name: hu
  data_files:
  - split: train
    path: '*/*hu*/train.parquet'
  - split: test
    path: '*/*hu*/test.parquet'
  - split: valid
    path: '*/*hu*/valid.parquet'
- config_name: id
  data_files:
  - split: train
    path: '*/*id*/train.parquet'
  - split: test
    path: '*/*id*/test.parquet'
  - split: valid
    path: '*/*id*/valid.parquet'
- config_name: it
  data_files:
  - split: train
    path: '*/*it*/train.parquet'
  - split: test
    path: '*/*it*/test.parquet'
  - split: valid
    path: '*/*it*/valid.parquet'
- config_name: mg
  data_files:
  - split: train
    path: '*/*mg*/train.parquet'
  - split: test
    path: '*/*mg*/test.parquet'
  - split: valid
    path: '*/*mg*/valid.parquet'
- config_name: mk
  data_files:
  - split: train
    path: '*/*mk*/train.parquet'
  - split: test
    path: '*/*mk*/test.parquet'
  - split: valid
    path: '*/*mk*/valid.parquet'
- config_name: my
  data_files:
  - split: train
    path: '*/*my*/train.parquet'
  - split: test
    path: '*/*my*/test.parquet'
  - split: valid
    path: '*/*my*/valid.parquet'
- config_name: nl
  data_files:
  - split: train
    path: '*/*nl*/train.parquet'
  - split: test
    path: '*/*nl*/test.parquet'
  - split: valid
    path: '*/*nl*/valid.parquet'
- config_name: pl
  data_files:
  - split: train
    path: '*/*pl*/train.parquet'
  - split: test
    path: '*/*pl*/test.parquet'
  - split: valid
    path: '*/*pl*/valid.parquet'
- config_name: pt
  data_files:
  - split: train
    path: '*/*pt*/train.parquet'
  - split: test
    path: '*/*pt*/test.parquet'
  - split: valid
    path: '*/*pt*/valid.parquet'
- config_name: ru
  data_files:
  - split: train
    path: '*/*ru*/train.parquet'
  - split: test
    path: '*/*ru*/test.parquet'
  - split: valid
    path: '*/*ru*/valid.parquet'
- config_name: sr
  data_files:
  - split: train
    path: '*/*sr*/train.parquet'
  - split: test
    path: '*/*sr*/test.parquet'
  - split: valid
    path: '*/*sr*/valid.parquet'
- config_name: sw
  data_files:
  - split: train
    path: '*/*sw*/train.parquet'
  - split: test
    path: '*/*sw*/test.parquet'
  - split: valid
    path: '*/*sw*/valid.parquet'
- config_name: tr
  data_files:
  - split: train
    path: '*/*tr*/train.parquet'
  - split: test
    path: '*/*tr*/test.parquet'
  - split: valid
    path: '*/*tr*/valid.parquet'
- config_name: ur
  data_files:
  - split: train
    path: '*/*ur*/train.parquet'
  - split: test
    path: '*/*ur*/test.parquet'
  - split: valid
    path: '*/*ur*/valid.parquet'
- config_name: zhs
  data_files:
  - split: train
    path: '*/*zhs*/train.parquet'
  - split: test
    path: '*/*zhs*/test.parquet'
  - split: valid
    path: '*/*zhs*/valid.parquet'
- config_name: zht
  data_files:
  - split: train
    path: '*/*zht*/train.parquet'
  - split: test
    path: '*/*zht*/test.parquet'
  - split: valid
    path: '*/*zht*/valid.parquet'
- config_name: bg
  data_files:
  - split: train
    path: '*/*bg*/train.parquet'
  - split: test
    path: '*/*bg*/test.parquet'
  - split: valid
    path: '*/*bg*/valid.parquet'
- config_name: cs
  data_files:
  - split: train
    path: '*/*cs*/train.parquet'
  - split: test
    path: '*/*cs*/test.parquet'
  - split: valid
    path: '*/*cs*/valid.parquet'
- config_name: da
  data_files:
  - split: train
    path: '*/*da*/train.parquet'
  - split: test
    path: '*/*da*/test.parquet'
  - split: valid
    path: '*/*da*/valid.parquet'
- config_name: eo
  data_files:
  - split: train
    path: '*/*eo*/train.parquet'
  - split: test
    path: '*/*eo*/test.parquet'
  - split: valid
    path: '*/*eo*/valid.parquet'
- config_name: he
  data_files:
  - split: train
    path: '*/*he*/train.parquet'
  - split: test
    path: '*/*he*/test.parquet'
  - split: valid
    path: '*/*he*/valid.parquet'
- config_name: km
  data_files:
  - split: train
    path: '*/*km*/train.parquet'
  - split: test
    path: '*/*km*/test.parquet'
  - split: valid
    path: '*/*km*/valid.parquet'
- config_name: ko
  data_files:
  - split: train
    path: '*/*ko*/train.parquet'
  - split: test
    path: '*/*ko*/test.parquet'
  - split: valid
    path: '*/*ko*/valid.parquet'
- config_name: ku
  data_files:
  - split: train
    path: '*/*ku*/train.parquet'
  - split: test
    path: '*/*ku*/test.parquet'
  - split: valid
    path: '*/*ku*/valid.parquet'
- config_name: ne
  data_files:
  - split: train
    path: '*/*ne*/train.parquet'
  - split: test
    path: '*/*ne*/test.parquet'
  - split: valid
    path: '*/*ne*/valid.parquet'
- config_name: or
  data_files:
  - split: train
    path: '*/*or*/train.parquet'
  - split: test
    path: '*/*or*/test.parquet'
  - split: valid
    path: '*/*or*/valid.parquet'
- config_name: pa
  data_files:
  - split: train
    path: '*/*pa*/train.parquet'
  - split: test
    path: '*/*pa*/test.parquet'
  - split: valid
    path: '*/*pa*/valid.parquet'
- config_name: ro
  data_files:
  - split: train
    path: '*/*ro*/train.parquet'
  - split: test
    path: '*/*ro*/test.parquet'
  - split: valid
    path: '*/*ro*/valid.parquet'
- config_name: sq
  data_files:
  - split: train
    path: '*/*sq*/train.parquet'
  - split: test
    path: '*/*sq*/test.parquet'
  - split: valid
    path: '*/*sq*/valid.parquet'
- config_name: sv
  data_files:
  - split: train
    path: '*/*sv*/train.parquet'
  - split: test
    path: '*/*sv*/test.parquet'
  - split: valid
    path: '*/*sv*/valid.parquet'
language:
- am
- ar
- bg
- bn
- ca
- cs
- da
- de
- el
- en
- eo
- es
- fa
- fr
- he
- hi
- hu
- id
- it
- km
- ko
- ku
- mg
- mk
- my
- ne
- nl
- or
- pa
- pt
- pl
- ro
- ru
- sq
- sr
- sv
- sw
- tr
- ur
- zh
---