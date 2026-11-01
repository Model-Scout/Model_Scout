---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
dataset_info:
  features:
  - name: id
    dtype: string
  - name: input
    dtype: string
  - name: output
    dtype: string
  - name: instruction
    dtype: string
  splits:
  - name: train
    num_bytes: 79087758
    num_examples: 51170
  download_size: 39384183
  dataset_size: 79087758
---
# Dataset Card for "KOR-gugugu-platypus-set"

## Pre-processing
```
# Make the special text lists, manually.
[\n\t-=+,#/\＄?:^$.@*\"–∼①②③④⑤ⓐⓑⓒ㉮㉯㉰㈜®...TL;DR...∂Σ∩∅φμσℝλΛ≥℃∉⊂θ±€Øπ√≠≤ε∈∫ωηαβ÷≈×ˇ̊°²/]
```  
- 위의 정규표현식을 이용하여, 한국어 및 영어를 제외한 다양한 외국어, 이모지, 특수 문자 등등 제거.  
- 번역 task 최대한 제거. (~번역 task는 한국어로 번역하면 거의 100% 오류)  
- [gugugu-ko](https://huggingface.co/datasets/squarelike/OpenOrca-gugugo-ko)의 GPT4 번역 결과에서 약 20k sampling.  
- 데이터셋 이용하셔서 모델이나 데이터셋을 만드실 때, 간단한 출처 표기를 해주신다면 연구에 큰 도움이 됩니다😭😭  

---
# References
- Thank you for [squarelike/OpenOrca-gugugo-ko](https://huggingface.co/datasets/squarelike/OpenOrca-gugugo-ko)  
- My dataset [kyujinpy/KOR-OpenOrca-Platypus-v3](https://huggingface.co/datasets/kyujinpy/KOR-OpenOrca-Platypus-v3)  