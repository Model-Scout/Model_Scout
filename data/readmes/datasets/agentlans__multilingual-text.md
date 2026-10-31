---
configs:
- config_name: arb_Arab
  data_files:
  - path:
    - arb_Arab.jsonl.zst
    split: train
- config_name: ben_Beng
  data_files:
  - path:
    - ben_Beng.jsonl.zst
    split: train
- config_name: deu_Latn
  data_files:
  - path:
    - deu_Latn.jsonl.zst
    split: train
- config_name: eng_Latn
  data_files:
  - path:
    - eng_Latn.jsonl.zst
    split: train
- config_name: fra_Latn
  data_files:
  - path:
    - fra_Latn.jsonl.zst
    split: train
- config_name: hin_Deva
  data_files:
  - path:
    - hin_Deva.jsonl.zst
    split: train
- config_name: ind_Latn
  data_files:
  - path:
    - ind_Latn.jsonl.zst
    split: train
- config_name: ita_Latn
  data_files:
  - path:
    - ita_Latn.jsonl.zst
    split: train
- config_name: jpn_Jpan
  data_files:
  - path:
    - jpn_Jpan.jsonl.zst
    split: train
- config_name: por_Latn
  data_files:
  - path:
    - por_Latn.jsonl.zst
    split: train
- config_name: rus_Cyrl
  data_files:
  - path:
    - rus_Cyrl.jsonl.zst
    split: train
- config_name: spa_Latn
  data_files:
  - path:
    - spa_Latn.jsonl.zst
    split: train
- config_name: swh_Latn
  data_files:
  - path:
    - swh_Latn.jsonl.zst
    split: train
- config_name: zho_Hans
  data_files:
  - path:
    - zho_Hans.jsonl.zst
    split: train
- config_name: kor_Hang
  data_files:
  - path:
    - kor_Hang.jsonl.zst
    split: train
- config_name: pes_Arab
  data_files:
  - path:
    - pes_Arab.jsonl.zst
    split: train
- config_name: tha_Thai
  data_files:
  - path:
    - tha_Thai.jsonl.zst
    split: train
- config_name: tur_Latn
  data_files:
  - path:
    - tur_Latn.jsonl.zst
    split: train
- config_name: urd_Arab
  data_files:
  - path:
    - urd_Arab.jsonl.zst
    split: train
- config_name: vie_Latn
  data_files:
  - path:
    - vie_Latn.jsonl.zst
    split: train
- config_name: heb_Hebr
  data_files:
  - path:
    - heb_Hebr.jsonl.zst
    split: train
- config_name: pan_Guru
  data_files:
  - path:
    - pan_Guru.jsonl.zst
    split: train
- config_name: pol_Latn
  data_files:
  - path:
    - pol_Latn.jsonl.zst
    split: train
- config_name: tam_Taml
  data_files:
  - path:
    - tam_Taml.jsonl.zst
    split: train
- config_name: tgl_Latn
  data_files:
  - path:
    - tgl_Latn.jsonl.zst
    split: train
- config_name: ukr_Cyrl
  data_files:
  - path:
    - ukr_Cyrl.jsonl.zst
    split: train
- config_name: amh_Ethi
  data_files:
  - path:
    - amh_Ethi.jsonl.zst
    split: train
- config_name: hau_Latn
  data_files:
  - path:
    - hau_Latn.jsonl.zst
    split: train
- config_name: jav_Latn
  data_files:
  - path:
    - jav_Latn.jsonl.zst
    split: train
- config_name: mar_Deva
  data_files:
  - path:
    - mar_Deva.jsonl.zst
    split: train
- config_name: mya_Mymr
  data_files:
  - path:
    - mya_Mymr.jsonl.zst
    split: train
- config_name: nld_Latn
  data_files:
  - path:
    - nld_Latn.jsonl.zst
    split: train
- config_name: ron_Latn
  data_files:
  - path:
    - ron_Latn.jsonl.zst
    split: train
- config_name: tel_Telu
  data_files:
  - path:
    - tel_Telu.jsonl.zst
    split: train
- config_name: yor_Latn
  data_files:
  - path:
    - yor_Latn.jsonl.zst
    split: train
- config_name: zsm_Latn
  data_files:
  - path:
    - zsm_Latn.jsonl.zst
    split: train
license: odc-by
language:
- am
- ar
- bn
- de
- en
- es
- fa
- fr
- ha
- he
- hi
- id
- it
- ja
- jv
- ko
- mr
- ms
- my
- nl
- pa
- pl
- pt
- ro
- ru
- sw
- ta
- te
- th
- tl
- tr
- uk
- ur
- vi
- yo
- zh
task_categories:
- text-generation
- text-classification
tags:
- multilingual
- text
- corpus
- language
---
# Multilingual Text Dataset

This dataset contains a curated selection of rows from multiple input datasets, where each row includes a text chunk of approximately 2000 tokens (as measured by Llama 3.1 tokenizer) verified to be written in the correct language. Only rows with properly classified language chunks are retained, ensuring high-quality multilingual data for analysis or model training.

### Preprocessing Steps
- Normalized whitespace, punctuation, Unicode characters, and bullet points  
- Replaced sensitive information such as emails, phone numbers, and URLs with placeholders  
- Language detection performed with the lid218e.bin FastText model  
- Downloaded 20&thinsp;000 chunks from each dataset
- Duplicate chunks were removed  

### Example Entry (mya_Mymr split)
```json
{
  "uuid": "6d1baa56-f2d9-4122-ba9a-5ba518fbe199",
  "text": "်ပွားပြီး အိတ်ချ်အိုင်ဗွီရှိပြီး တီဘီကူးစက်ခံရသူ ၃၀% တွင် တီဘီရောဂါဖြစ်ပွားသည်။\nတီဘီရောဂါသည် လူဦးရေထူထပ်ခြင်းနှင့် အာဟာရချို့တဲ့ခြင်းများနှင့်လည်း ဆက်စပ်နေသည်။ ...",
  "language": "mya_Mymr",
  "dataset": "wikimedia/wikipedia",
  "config": "20231101.my"
}
```