---
license: mit
language:
- ko
base_model:
- klue/bert-base
pipeline_tag: feature-extraction
tags:
- medical
---
# 🍊 SapBERT-Ko-EN

## 1. Intro

한국어 모델을 이용한 **SapBERT**(Self-alignment pretraining for BERT)입니다.    
한·영 의료 용어 사전인 KOSTOM을 사용해 한국어 용어와 영어 용어를 정렬했습니다.     
참고: [SapBERT](https://aclanthology.org/2021.naacl-main.334.pdf), [Original Code](https://github.com/cambridgeltl/sapbert)   

## 2. SapBERT-KO-EN
**SapBERT**는 수많은 의료 동의어를 동일한 의미로 처리하기 위한 사전 학습 방법론입니다.     
**SapBERT-KO-EN**는 **한·영 혼용체의 의료 기록**을 처리하기 위해 한·영 의료 용어를 정렬했습니다.

※ 자세한 설명 및 학습 코드: [Github](https://github.com/millet04/SapBERT-KO-EN)

## 3. Training


모델 학습에 활용한 베이스 모델 및 하이퍼 파라미터는 다음과 같습니다.

- Model : klue/bert-base
- Epochs : 1
- Batch Size : 64
- Max Length : 64
- Dropout : 0.1
- Pooler : 'cls'
- Eval Step : 100
- Threshold : 0.8
- Scale Positive Sample : 1
- Scale Negative Sample : 60

SapBERT-KO-EN에 후속 **Fine-tuning**을 진행하는 방식으로 특정 테스크에 적용할 수 있습니다. 

※ 영어 용어의 경우 대부분 알파벳 단위로 처리합니다.    
※ 동일한 질병을 가리키는 용어 간의 유사도를 상대적으로 크게 평가합니다.

```python
import numpy as np
from transformers import AutoModel, AutoTokenizer

model_path = 'snumin44/sap-bert-ko-en'
model = AutoModel.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

query = '간경화'

targets = [
    'liver cirrhosis',
    '간경변',
    'liver cancer',
    '간암',
    'brain tumor',
    '뇌종양'
]

query_feature = tokenizer(query, return_tensors='pt')
query_outputs = model(**query_feature, return_dict=True)
query_embeddings = query_outputs.pooler_output.detach().numpy().squeeze()

def cos_sim(A, B):
    return np.dot(A, B) / (np.linalg.norm(A) * np.linalg.norm(B))

for idx, target in enumerate(targets):
    target_feature = tokenizer(target, return_tensors='pt')
    target_outputs = model(**target_feature, return_dict=True)
    target_embeddings = target_outputs.pooler_output.detach().numpy().squeeze()
    similarity = cos_sim(query_embeddings, target_embeddings)
    print(f"Similarity between query and target {idx}: {similarity:.4f}")
```
```
Similarity between query and target 0: 0.7145
Similarity between query and target 1: 0.7186
Similarity between query and target 2: 0.6183
Similarity between query and target 3: 0.6972
Similarity between query and target 4: 0.3929
Similarity between query and target 5: 0.4260
```

## Citing
```
@inproceedings{liu2021self,
	title={Self-Alignment Pretraining for Biomedical Entity Representations},
	author={Liu, Fangyu and Shareghi, Ehsan and Meng, Zaiqiao and Basaldella, Marco and Collier, Nigel},
	booktitle={Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies},
	pages={4228--4238},
	month = jun,
	year={2021}
}
```
