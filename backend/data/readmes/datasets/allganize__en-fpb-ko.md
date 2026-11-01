---
dataset_info:
  features:
  - name: conversation_id
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: test
    num_bytes: 333061
    num_examples: 944
  download_size: 109275
  dataset_size: 333061
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
license: mit
language:
- ko
---


# en-fpb-ko

### 데이터 설명

- `en-fpb-ko` 데이터는 금융 뉴스로부터의 문장을 '긍정', '중립', '부정' 중 하나로 분류하는 감성 분류 (sentiment analysis) 데이터셋입니다.
입력값으로는 text만 주어집니다.

- 한국어 데이터를 생성하기 위해, 먼저 사내 언어 번역 모델인 Allganize Translator를 활용하여 [ChanceFocus/en-fpb](https://huggingface.co/datasets/ChanceFocus/en-fpb)의 test set을 한국어로 번역하였습니다. 
오역된 데이터를 직접 제거하였고, 그 결과 944개의 평가 데이터가 생성되었습니다. 
  

### 데이터 출처
- [ChanceFocus/en-fpb](https://huggingface.co/datasets/ChanceFocus/en-fpb)


### 데이터 예시
```
{
  'conversation_id': 'fpb3876',
  'conversations': array([
    {
      'from': 'human',
      'value': '''금융 뉴스 기사에서 발췌한 이 문장의 정서를 분석하세요. 부정, 긍정 또는 중립 중 하나로 답을 제시하세요.
              텍스트: 회사 간의 오랜 협력 관계를 확대하는 새로운 계약에는 Larox에서 Etteplan으로 특정 엔지니어링 및 문서 기능의 이전이 포함됩니다.
              정답:'''
    },
    {
      'from': 'gpt',
      'value': '긍정'
    }
  ], dtype=object)
}

```