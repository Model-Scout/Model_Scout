---
language:
- ko
license: apache-2.0
size_categories:
- 10K<n<100K
task_categories:
- text-generation
pretty_name: 한국어 문체 인스트럭스 튜닝 데이터셋
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: train
    num_bytes: 42360074.57709055
    num_examples: 28978
  download_size: 26072915
  dataset_size: 42360074.57709055
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# 한국어 문체 데이터셋

여러 분야의 문체(문학, 일상적 대화, 고전시가 등)를 포함한 합성 데이터셋입니다. 모델에게 여러 문체를 출력하는 능력을 가르치기 위해 제작되었습니다. 훈련시키실 때, 일반 인스트럭스 데이터셋과 혼용해서 사용하시는 것을 추천드립니다.

이 데이터셋은 `apache-2` 라이선스로 자유롭게 이용하실 수 있습니다. 데이터는 [Glaive](https://glaive.ai) 플랫폼을 통해 합성되었고, 한글이 아닌 출력은 걸러냈습니다.