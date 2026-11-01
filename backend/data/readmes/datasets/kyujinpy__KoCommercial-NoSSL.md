---
language:
- ko
license: cc-by-nc-sa-4.0
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train-*
dataset_info:
  features:
    - name: input
      dtype: string
    - name: instruction
      dtype: string
    - name: output
      dtype: string
  splits:
    - name: train
      num_bytes: 187990458
      num_examples: 175454
  download_size: 110149618
  dataset_size: 187990458
---
# Dataset for kyujinpy/KoCommercial-NoSSL

## Info

**Dataset 개수:** 약 175K
  
**License:** CC-BY-NC-4.0 (*통합에 활용한 각 데이터셋은 모두 상업적 용도로 사용가능.)
  
**Dataset list(전부 상업적 용도로 이용가능)**  
1. [kyujinpy/KOpen-platypus](kyujinpy/KOpen-platypus) (*Except non-commercial datasets)
2. [beomi/KoAlpaca-v1.1a](https://huggingface.co/datasets/beomi/KoAlpaca-v1.1a) 
3. [HumanF-MarkrAI/WIKI_QA_Near_dedup](https://huggingface.co/datasets/HumanF-MarkrAI/WIKI_QA_Near_dedup)
4. [KorQuadv1.0](https://korquad.github.io/KorQuad%201.0/)
    
# Another Dataset
- [kyujinpy/KoCommercial-SSL](https://huggingface.co/datasets/kyujinpy/KoCommercial-SSL).  
- [MarkrAI/KoCommercial-Dataset](https://huggingface.co/datasets/MarkrAI/KoCommercial-Dataset).  
