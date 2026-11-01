---
dataset_info:
  features:
  - name: sentences
    sequence: string
  - name: labels
    sequence: string
  splits:
  - name: test
    num_bytes: 1305703
    num_examples: 14
  download_size: 397229
  dataset_size: 1305703
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
language:
- ko
tags:
- finance
pretty_name: MinDS-Clustering-ko
size_categories:
- n<1K
---

## MinDS-Clustering-ko

- Utilized user questions and intents from the 'Finance/Insurance' category of [**AIHub's complaint Q&A dataset**](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=98).  
- Constructed a dataset for clustering **user intents** based on their queries.  
- The intent labels are structured as follows:  
  - Transaction inquiry and management
  - Account and card-related services 
  - Financial transactions and incidents
  - Loan-related inquiries
  - Insurance and financial product inquiries
  - Insurance claims and compensation
  - Loss and theft reports
  - Product subscription-related inquiries
  - Product information and inquiries
  - Product cancellation and modification
  - Transfer and remittance services
  - Authentication and financial transaction services
  - Automobile and accident handling
  - Balance and account balance inquiries
  - Certificate and financial document issuance
  - Withdrawal and cash services
- Applied a similar label structure for comparison with [FinanceMTEB/MInDS-14-en](https://huggingface.co/datasets/FinanceMTEB/MInDS-14-en) dataset.

