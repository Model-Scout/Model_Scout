---
license: cc-by-nc-4.0
language:
- bg
- zh
- hr
- da
- nl
- et
- fa
- ja
- ko
task_categories:
- text-classification
pretty_name: Multilingual Word-in-Context (WordNet)
configs:
- config_name: default
  sep: "\t"
  data_files:
  - split: valid
    path: "**/*_valid.csv"
  - split: test
    path: "**/*_test.csv"
    
- config_name: bg
  sep: "\t"
  data_files:
  - split: valid
    path: "bulgarian_bg/bg_valid.csv"
  - split: test
    path: "bulgarian_bg/bg_test.csv"

- config_name: zh
  sep: "\t"
  data_files:
  - split: valid
    path: "chinese_zh/zh_valid.csv"
  - split: test
    path: "chinese_zh/zh_test.csv"

- config_name: hr
  sep: "\t"
  data_files:
  - split: valid
    path: "croatian_hr/hr_valid.csv"
  - split: test
    path: "croatian_hr/hr_test.csv"

- config_name: da
  sep: "\t"
  data_files:
  - split: valid
    path: "danish_da/da_valid.csv"
  - split: test
    path: "danish_da/da_test.csv"

- config_name: nl
  sep: "\t"
  data_files:
  - split: valid
    path: "dutch_nl/nl_valid.csv"
  - split: test
    path: "dutch_nl/nl_test.csv"

- config_name: et
  sep: "\t"
  data_files:
  - split: valid
    path: "estonian_et/et_valid.csv"
  - split: test
    path: "estonian_et/et_test.csv"

- config_name: fa
  sep: "\t"
  data_files:
  - split: valid
    path: "farsi_fa/fa_valid.csv"
  - split: test
    path: "farsi_fa/fa_test.csv"

- config_name: ja
  sep: "\t"
  data_files:
  - split: valid
    path: "japanese_ja/ja_valid.csv"
  - split: test
    path: "japanese_ja/ja_test.csv"

- config_name: ko
  sep: "\t"
  data_files:
  - split: valid
    path: "korean_ko/ko_valid.csv"
  - split: test
    path: "korean_ko/ko_test.csv"
---

# Multilingual Word-in-Context (WordNet)

Refer to the [documentation](https://pilehvar.github.io/xlwic/) and [paper](https://aclanthology.org/2020.emnlp-main.584/) for more information.