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
    num_bytes: 52262
    num_examples: 204
  download_size: 19986
  dataset_size: 52262
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
license: mit
language:
- ko
---

# flare-fiqasa-ko


### 데이터 설명

- `flare-fiqasa-ko` 데이터는 금융 도메인 뉴스 헤드라인의 감성을 예측(sentiment analysis)하는 데이터셋입니다.
입력값은 text로만 이루어져 있습니다.

- 한국어 데이터를 생성하기 위해, 우선 사내 언어 번역 모델 Allganize Translator을 활용하여 [ChanceFocus/flare-fiqasa](https://huggingface.co/datasets/ChanceFocus/flare-fiqasa)의 test set을 번역했습니다.
오역된 데이터를 직접 제거하였고, 그 결과 204개의 평가 데이터가 생성되었습니다.


### 데이터 출처
- [ChanceFocus/flare-fiqasa](https://huggingface.co/datasets/ChanceFocus/flare-fiqasa)


### 데이터 예시
```
{
  'conversation_id': 'fiqasa938',
  'conversations': array([
    {
      'from': 'human',
      'value': '''다음 재무 게시물의 감정은 무엇인가요? 긍정, 부정 또는 중립인가요?
              텍스트: $BBRY 실제로 부채가 없고 현금 3.1달러를 포함하면 주당 0.03달러의 손실을 입었습니다.
              정답:'''
    },
    {
      'from': 'gpt',
      'value': '부정'
    }
  ], dtype=object)
}

```