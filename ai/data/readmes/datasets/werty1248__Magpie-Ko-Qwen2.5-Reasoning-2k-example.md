---
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: response
    dtype: string
  splits:
  - name: train
    num_bytes: 4399377
    num_examples: 1668
  download_size: 2041307
  dataset_size: 4399377
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
---

- 데이터 확인 및 테스트용


- 샘플 데이터 생성 ✅
  - temperature: 1.0
  - top_p: 1.0
- 한자/영어 필터링 ✅(수정필요)
  - 답변에도 한자/영어 필터링 적용해야 함
- 데이터 분포 확인 ✅
  - instruction에 대한 BGE-m3 embedding + T-SNE
- 문제 난이도 / 답변 퀄리티 확인
  - 풀 수 없는 문제 있음
  - 사소한 문법 오류 있음
  - 러시아어/아랍어 등 추가 필터링 필요
- 최종 데이터 생성(~100K)
  - Magpie-Align/Magpie-Qwen2-Pro-300K-Filtered: (1.0, 1.0), (1.1, 1.0), (1.2, 0.99)
 

![image/png](https://cdn-uploads.huggingface.co/production/uploads/6629154d55d7c289634b8c5d/gEwULC_ReSypbF6i_u09m.png)