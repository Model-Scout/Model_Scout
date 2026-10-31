---
language:
- hi
- ta
- te
- kn
- ml
- bn
- mr
- gu
- ur
- pa
- en
- es
- fr
- de
- it
- pt
- ru
- nl
- pl
- zh
- ja
- ko
- ar
license: cc-by-4.0
task_categories:
- automatic-speech-recognition
configs:
- config_name: voxpopuli
  data_files:
  - split: train
    path: "voxpopuli/**/*.parquet"
- config_name: indicvoices
  data_files:
  - split: train
    path: "indicvoices/**/*.parquet"
- config_name: shrutilipi
  data_files:
  - split: train
    path: "shrutilipi/**/*.parquet"
- config_name: mls
  data_files:
  - split: train
    path: "mls/**/*.parquet"
- config_name: fleurs
  data_files:
  - split: train
    path: "fleurs/**/*.parquet"
- config_name: gigaspeech
  data_files:
  - split: train
    path: "gigaspeech/**/*.parquet"
- config_name: rasa
  data_files:
  - split: train
    path: "rasa/**/*.parquet"
- config_name: libritts_r_100
  data_files:
  - split: train
    path: "libritts_r_100/**/*.parquet"
- config_name: libritts_r_360
  data_files:
  - split: train
    path: "libritts_r_360/**/*.parquet"
- config_name: emilia
  data_files:
  - split: train
    path: "emilia/**/*.parquet"
- config_name: nst
  data_files:
  - split: train
    path: "nst/**/*.parquet"
- config_name: codemixed
  data_files:
  - split: train
    path: "codemixed/**/*.parquet"
- config_name: hinglish
  data_files:
  - split: train
    path: "hinglish/**/*.parquet"
- config_name: airline_ivr
  data_files:
  - split: train
    path: "airline_ivr/**/*.parquet"
- config_name: indic_voices
  data_files:
  - split: train
    path: "indic_voices/**/*.parquet"
- config_name: spring_inx_bn_r1
  data_files:
  - split: train
    path: "spring_inx_bn_r1/**/*.parquet"
- config_name: spring_inx_bn_r2
  data_files:
  - split: train
    path: "spring_inx_bn_r2/**/*.parquet"
- config_name: spring_inx_mr_r1
  data_files:
  - split: train
    path: "spring_inx_mr_r1/**/*.parquet"
- config_name: spring_inx_mr_r2
  data_files:
  - split: train
    path: "spring_inx_mr_r2/**/*.parquet"
- config_name: spring_inx_pa_r1
  data_files:
  - split: train
    path: "spring_inx_pa_r1/**/*.parquet"
- config_name: spring_inx_pa_r2
  data_files:
  - split: train
    path: "spring_inx_pa_r2/**/*.parquet"

---

# ramanv-tts-all-raw

Multi-source speech corpus for ASR/STT training. Real human speech across 60+ languages.
