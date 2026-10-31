---
task_categories:
  - question-answering
configs:
  - config_name: default
    data_files:
      - split: test
        path: "data/*.csv"
  - config_name: AR_XY
    data_files:
      - split: test
        path: "data/mmmlu_AR_XY.csv"
  - config_name: BN_BD
    data_files:
      - split: test
        path: "data/mmmlu_BN_BD.csv"
  - config_name: DE_DE
    data_files:
      - split: test
        path: "data/mmmlu_DE_DE.csv"
  - config_name: ES_LA
    data_files:
      - split: test
        path: "data/mmmlu_ES_LA.csv"
  - config_name: FR_FR
    data_files:
      - split: test
        path: "data/mmmlu_FR_FR.csv"
  - config_name: HI_IN
    data_files:
      - split: test
        path: "data/mmmlu_HI_IN.csv"
  - config_name: ID_ID
    data_files:
      - split: test
        path: "data/mmmlu_ID_ID.csv"
  - config_name: IT_IT
    data_files:
      - split: test
        path: "data/mmmlu_IT_IT.csv"
  - config_name: JA_JP
    data_files:
      - split: test
        path: "data/mmmlu_JA_JP.csv"
  - config_name: KO_KR
    data_files:
      - split: test
        path: "data/mmmlu_KO_KR.csv"
  - config_name: PT_BR
    data_files:
      - split: test
        path: "data/mmmlu_PT_BR.csv"
  - config_name: SW_KE
    data_files:
      - split: test
        path: "data/mmmlu_SW_KE.csv"
  - config_name: YO_NG
    data_files:
      - split: test
        path: "data/mmmlu_YO_NG.csv"
  - config_name: ZH_CN
    data_files:
      - split: test
        path: "data/mmmlu_ZH_CN.csv"
language:
  - ar
  - bn
  - de
  - es
  - fr
  - hi
  - id
  - it
  - ja
  - ko
  - pt
  - sw
  - yo
  - zh
license: mit
---