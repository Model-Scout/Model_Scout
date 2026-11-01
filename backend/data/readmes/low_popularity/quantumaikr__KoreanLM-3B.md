---
language:
- ko
- en
pipeline_tag: text-generation
tags:
- llama
- korean
- foundation
---


<p align="center" width="100%">
<img src="https://i.imgur.com/snFDU0P.png" alt="KoreanLM icon" style="width: 500px; display: block; margin: auto; border-radius: 10%;">
</p>


# KoreanLM: 한국어 언어모델 프로젝트

KoreanLM은 한국어 언어모델을 개발하기 위한 오픈소스 프로젝트입니다. 현재 대부분의 언어모델들은 영어에 초점을 맞추고 있어, 한국어에 대한 학습이 상대적으로 부족하고 토큰화 과정에서 비효율적인 경우가 있습니다. 이러한 문제를 해결하고 한국어에 최적화된 언어모델을 제공하기 위해 KoreanLM 프로젝트를 시작하게 되었습니다.


## 프로젝트 목표

1. 한국어에 특화된 언어모델 개발: 한국어의 문법, 어휘, 문화적 특성을 반영하여 한국어를 더 정확하게 이해하고 생성할 수 있는 언어모델을 개발합니다.

2. 효율적인 토큰화 방식 도입: 한국어 텍스트의 토큰화 과정에서 효율적이고 정확한 분석이 가능한 새로운 토큰화 방식을 도입하여 언어모델의 성능을 향상시킵니다.

3. 거대 언어모델의 사용성 개선: 현재 거대한 사이즈의 언어모델들은 기업이 자사의 데이터를 파인튜닝하기 어려운 문제가 있습니다. 이를 해결하기 위해 한국어 언어모델의 크기를 조절하여 사용성을 개선하고, 자연어 처리 작업에 더 쉽게 적용할 수 있도록 합니다.


## 사용 방법

다음은 transformers 라이브러리를 통해 모델과 토크나이저를 로딩하는 예제입니다.

```python
import transformers
model = transformers.AutoModelForCausalLM.from_pretrained("quantumaikr/KoreanLM-3B")
tokenizer = transformers.AutoTokenizer.from_pretrained("quantumaikr/KoreanLM-3B")

```

## 기술 문의

hi@quantumai.kr

www.quantumai.kr