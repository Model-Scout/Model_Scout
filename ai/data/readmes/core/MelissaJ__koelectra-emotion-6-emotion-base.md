---
library_name: transformers
license: apache-2.0
language:
- ko
base_model:
- monologg/koelectra-base-v3-discriminator
---
# KoELECTRA Emotion Classification (기쁨/분노/상처/불안/당황/슬픔)

## 모델 개요
이 모델은 **KoELECTRA-base-v3**를 기반으로 파인튜닝된 한국어 감정 분류 모델입니다.  
입력 문장을 6가지 감정 범주 중 하나로 분류합니다:

- 기쁨
- 분노
- 상처
- 불안
- 당황
- 슬픔

## 학습 데이터
- **감성 대화 말뭉치 (Korean Emotional Conversation Corpus, AI Hub)**  
  한국지능정보사회진흥원(NIA)에서 구축한 대화 기반 감정 레이블 데이터셋  
- 데이터셋 출처: [AI Hub 감성 대화 말뭉치](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=86)  
- 클래스 분포:
  - 불안: 9,320  
  - 분노: 9,160  
  - 상처: 9,143  
  - 슬픔: 9,125  
  - 당황: 8,756  
  - 기쁨: 6,126  

## 학습 설정
- Epoch: 100 (최적 성능은 2~3 epoch 구간에서 관측)  
- Optimizer: AdamW  
- Learning rate: 5e-5  
- Batch size: train 32 / eval 64  
- Weight decay: 0.01  
- Mixed precision: FP16 (GPU)  

## 성능
Validation set 기준:

| Epoch | Training Loss | Validation Loss | Accuracy | F1 Macro |
|------:|--------------:|----------------:|---------:|---------:|
| 1     | 1.1211        | 1.1623          | 0.5613   | 0.5733   |
| 2     | 1.0241        | 1.1424          | 0.5789   | 0.5928   |
| 3     | 0.9386        | 1.1948          | 0.5789   | 0.5968   |
| ...   | ...           | ...             | ...      | ...      |
| 90    | 0.0077        | 5.2280          | 0.5727   | 0.5866   |
| 100   | 0.0008        | 5.3633          | 0.5654   | 0.5796   |

- **최고 성능 (F1 Macro ≈ 0.5968)**: Epoch 3  
- 이후 epoch에서는 Validation Loss가 급격히 증가 → **과적합** 경향  

## 사용법
```python
from transformers import pipeline
pipe = pipeline("text-classification", model="MelissaJ/koelectra-emotion-6-emotion-base")
text = "그런일이 있으셨다니 매우 슬프시겠어요"
print(pipe(text))
# [{'label': '슬픔', 'score': 0.8857910633087158}]