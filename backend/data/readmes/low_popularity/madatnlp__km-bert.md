---
language:
- ko
tags:
- biology
---
# Model Card for Model ID


이 모델은 KM-BERT의 모델을 다운 받아, 임의로 허깅페이스 모델의 형태로 사용하기 좋게 변환한 모델 입니다.
<br>

모델은 그대로이고, 토크나이저는 논문에 나와 있는대로, snunlp/KR-BERT-char16424 것을 가져왔습니다
<br>

KM-BERT를 사용해볼 수 있게 공유해주신 저자분께 감사드립니다.
<br>

문제 발생 시 수정하거나, 또는 저자님의 요청시 허브에서 내릴 수도 있습니다.
<br>

## Model Details


bing 활용 요약:

이 문서는 다음과 같은 내용을 다룹니다:

한국어 의료 자연어 처리를 위한 사전 훈련된 BERT 모델. <br>
이 모델은 의료 분야에서 사용되는 한국어 텍스트를 분석하기 위해 KR-BERT 모델을 기반으로 한국어 의료 코퍼스로 사전 훈련한 KM-BERT라고 합니다. <br>
이 모델은 의료 교과서, 건강 정보 뉴스, 의료 연구 논문 등 세 가지 유형의 문서로 구성된 약 1억 1천 6백만 단어의 한국어 의료 코퍼스를 사용했습니다. <br>

내부 평가와 외부 평가. <br>
이 모델은 MLM과 NSP라는 두 가지 비지도 사전 훈련 과제를 수행하고, 새로운 한국어 의료 코퍼스와 MedSTS 데이터셋을 이용하여 언어 이해 능력을 내부 평가했습니다. <br>
또한, 한국어 의료 의미론적 텍스트 유사도(MedSTS) 데이터셋과 한국어 의료 개체 인식(NER) 데이터셋을 이용하여 하류 과제에 대한 성능을 외부 평가했습니다. <br>
결과적으로, KM-BERT는 기존의 언어 모델들보다 우수한 성능을 보였습니다. <br>

언어별 및 분야별 관점. <br>
M-BERT는 다양한 언어에 대한 NLP 과제에 높은 전이성을 보이지만, 언어별 BERT 모델들이 M-BERT보다 더 나은 성능을 보인다는 것이 증명되었습니다. <br>
1. 한국어는 영어와 같은 인도유럽어와는 다른 단어 순서를 가지고 있기 때문에, 한국어에 특화된 BERT 모델이 필요합니다. <br>
2. 또한, SciBERT나 LEGAL-BERT와 같은 분야별 BERT 임베딩이 BERT보다 전문 용어와 용법에 대한 이해력을 향상시킨다는 것이 밝혀졌습니다. <br>
3. 이러한 연구 결과들은 한국어 의료 분야에 적합한 BERT 모델 개발의 필요성과 효과성을 보여줍니다. <br>


### Model Sources [optional]


- **Repository:** https://github.com/KU-RIAS/KM-BERT-Korean-Medical-BERT <br>
- **Paper:** https://www.nature.com/articles/s41598-022-17806-8 <br>


## Citation [optional]


@article{KMBERT, <br>
    title={KM-BERT: A Pre-trained BERT for Korean Medical Natural Language Processing}, <br>
    author={TBD}, <br>
    year={TBD}, <br>
    journal={TBD}, <br>
    volume={TBD} <br>
  }