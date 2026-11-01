---
dataset_info:
- config_name: corpus
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: NanoClimateFEVER
    num_bytes: 3591837
    num_examples: 3408
  - name: NanoDBPedia
    num_bytes: 1696874
    num_examples: 6045
  - name: NanoFEVER
    num_bytes: 4468102
    num_examples: 4996
  - name: NanoFiQA2018
    num_bytes: 2919833
    num_examples: 4598
  - name: NanoHotpotQA
    num_bytes: 1454406
    num_examples: 5090
  - name: NanoMSMARCO
    num_bytes: 1223067
    num_examples: 5043
  - name: NanoNFCorpus
    num_bytes: 2617249
    num_examples: 2953
  - name: NanoNQ
    num_bytes: 2012592
    num_examples: 5035
  - name: NanoQuoraRetrieval
    num_bytes: 273698
    num_examples: 5046
  - name: NanoSCIDOCS
    num_bytes: 1355295
    num_examples: 2210
  - name: NanoArguAna
    num_bytes: 2467897
    num_examples: 3635
  - name: NanoSciFact
    num_bytes: 2559907
    num_examples: 2919
  - name: NanoTouche2020
    num_bytes: 7492610
    num_examples: 5745
  download_size: 34133367
  dataset_size: 34133367
- config_name: qrels
  features:
  - name: query-id
    dtype: string
  - name: corpus-id
    dtype: string
  splits:
  - name: NanoClimateFEVER
    num_bytes: 4217
    num_examples: 148
  - name: NanoDBPedia
    num_bytes: 22607
    num_examples: 1158
  - name: NanoFEVER
    num_bytes: 3188
    num_examples: 57
  - name: NanoFiQA2018
    num_bytes: 3118
    num_examples: 123
  - name: NanoHotpotQA
    num_bytes: 3861
    num_examples: 100
  - name: NanoMSMARCO
    num_bytes: 2571
    num_examples: 50
  - name: NanoNFCorpus
    num_bytes: 13680
    num_examples: 2518
  - name: NanoNQ
    num_bytes: 2493
    num_examples: 57
  - name: NanoQuoraRetrieval
    num_bytes: 2749
    num_examples: 70
  - name: NanoSCIDOCS
    num_bytes: 14384
    num_examples: 244
  - name: NanoArguAna
    num_bytes: 3816
    num_examples: 50
  - name: NanoSciFact
    num_bytes: 2562
    num_examples: 56
  - name: NanoTouche2020
    num_bytes: 18062
    num_examples: 932
  download_size: 97308
  dataset_size: 97308
- config_name: queries
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: NanoClimateFEVER
    num_bytes: 7977
    num_examples: 50
  - name: NanoDBPedia
    num_bytes: 4269
    num_examples: 50
  - name: NanoFEVER
    num_bytes: 4942
    num_examples: 50
  - name: NanoFiQA2018
    num_bytes: 5162
    num_examples: 50
  - name: NanoHotpotQA
    num_bytes: 7662
    num_examples: 50
  - name: NanoMSMARCO
    num_bytes: 4091
    num_examples: 50
  - name: NanoNFCorpus
    num_bytes: 3427
    num_examples: 50
  - name: NanoNQ
    num_bytes: 4833
    num_examples: 50
  - name: NanoQuoraRetrieval
    num_bytes: 4919
    num_examples: 50
  - name: NanoSCIDOCS
    num_bytes: 7526
    num_examples: 50
  - name: NanoArguAna
    num_bytes: 41933
    num_examples: 50
  - name: NanoSciFact
    num_bytes: 6480
    num_examples: 50
  - name: NanoTouche2020
    num_bytes: 4019
    num_examples: 49
  download_size: 107240
  dataset_size: 107240
configs:
- config_name: corpus
  data_files:
  - split: NanoClimateFEVER
    path: corpus/NanoClimateFEVER-*
  - split: NanoDBPedia
    path: corpus/NanoDBPedia-*
  - split: NanoFEVER
    path: corpus/NanoFEVER-*
  - split: NanoFiQA2018
    path: corpus/NanoFiQA2018-*
  - split: NanoHotpotQA
    path: corpus/NanoHotpotQA-*
  - split: NanoMSMARCO
    path: corpus/NanoMSMARCO-*
  - split: NanoNFCorpus
    path: corpus/NanoNFCorpus-*
  - split: NanoNQ
    path: corpus/NanoNQ-*
  - split: NanoQuoraRetrieval
    path: corpus/NanoQuoraRetrieval-*
  - split: NanoSCIDOCS
    path: corpus/NanoSCIDOCS-*
  - split: NanoArguAna
    path: corpus/NanoArguAna-*
  - split: NanoSciFact
    path: corpus/NanoSciFact-*
  - split: NanoTouche2020
    path: corpus/NanoTouche2020-*
- config_name: qrels
  data_files:
  - split: NanoClimateFEVER
    path: qrels/NanoClimateFEVER-*
  - split: NanoDBPedia
    path: qrels/NanoDBPedia-*
  - split: NanoFEVER
    path: qrels/NanoFEVER-*
  - split: NanoFiQA2018
    path: qrels/NanoFiQA2018-*
  - split: NanoHotpotQA
    path: qrels/NanoHotpotQA-*
  - split: NanoMSMARCO
    path: qrels/NanoMSMARCO-*
  - split: NanoNFCorpus
    path: qrels/NanoNFCorpus-*
  - split: NanoNQ
    path: qrels/NanoNQ-*
  - split: NanoQuoraRetrieval
    path: qrels/NanoQuoraRetrieval-*
  - split: NanoSCIDOCS
    path: qrels/NanoSCIDOCS-*
  - split: NanoArguAna
    path: qrels/NanoArguAna-*
  - split: NanoSciFact
    path: qrels/NanoSciFact-*
  - split: NanoTouche2020
    path: qrels/NanoTouche2020-*
- config_name: queries
  data_files:
  - split: NanoClimateFEVER
    path: queries/NanoClimateFEVER-*
  - split: NanoDBPedia
    path: queries/NanoDBPedia-*
  - split: NanoFEVER
    path: queries/NanoFEVER-*
  - split: NanoFiQA2018
    path: queries/NanoFiQA2018-*
  - split: NanoHotpotQA
    path: queries/NanoHotpotQA-*
  - split: NanoMSMARCO
    path: queries/NanoMSMARCO-*
  - split: NanoNFCorpus
    path: queries/NanoNFCorpus-*
  - split: NanoNQ
    path: queries/NanoNQ-*
  - split: NanoQuoraRetrieval
    path: queries/NanoQuoraRetrieval-*
  - split: NanoSCIDOCS
    path: queries/NanoSCIDOCS-*
  - split: NanoArguAna
    path: queries/NanoArguAna-*
  - split: NanoSciFact
    path: queries/NanoSciFact-*
  - split: NanoTouche2020
    path: queries/NanoTouche2020-*
  default: true
language:
- ko
task_categories:
- text-retrieval
tags:
- sentence-transformers
- NanoBEIR
- retrieval
---

# NanoBEIR-ko (Preprocessed)

한국어 NanoBEIR 벤치마크 데이터셋 (전처리된 쿼리 포함)

## Usage

```python
from datasets import load_dataset

queries = load_dataset("sionic-ai/NanoBEIR-ko", "queries", split="NanoClimateFEVER")
corpus = load_dataset("sionic-ai/NanoBEIR-ko", "corpus", split="NanoClimateFEVER")
qrels = load_dataset("sionic-ai/NanoBEIR-ko", "qrels", split="NanoClimateFEVER")
```

## Preprocessing Pipeline

- **Phase 1**: Format Detection & Conversion (Gemini 2.5 Flash)
  - 포맷 감지: QUESTION, KEYWORD, STATEMENT 분류
  - STATEMENT → QUESTION 변환
- **Phase 2**: Quality Validation & Fix (GPT-4o)
  - 부적절한 수정 감지 및 재수정

## Examples

| Subset | Original | Preprocessed |
|--------|----------|--------------|
| NanoClimateFEVER | 알래스카에서 갈색 곰들은 더 일찍 익는 엘더베리를 먹기 위해 먹이 섭취 습관을 바꾸고 있다. | 알래스카에서 갈색 곰들은 더 일찍 익는 엘더베리를 먹기 위해 먹이 섭취 습관을 바꾸고 있나요? |
| NanoClimateFEVER | 극지방의 빙하와 고산지대의 평원이 녹으면 메탄 가스가 위험하게 방출될 수 있다. | 극지방의 빙하와 고산지대의 평원이 녹으면 메탄 가스가 위험하게 방출될까요? |
| NanoClimateFEVER | 해빙은 과학자들과 기후 모델이 예상했던 것보다 훨씬 더 빠른 속도로 줄어들고 있다. | 해빙은 과학자들과 기후 모델이 예상했던 것보다 훨씬 더 빠른 속도로 줄어들고 있나요? |
| NanoClimateFEVER | 풍력 에너지의 탄소 발자국은 상당하다. | 풍력 에너지의 탄소 발자국은 상당한가? |
