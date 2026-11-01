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
    num_bytes: 217945
    num_examples: 455
  download_size: 105791
  dataset_size: 217945
configs:
- config_name: default
  data_files:
  - split: test
    path: data/test-*
language:
- ko
---


# financial-mmlu-ko

- `financial-mmlu-ko` 데이터는 금융 도메인의 다중 선택(Multiple Choice) 데이터셋입니다. 질문과 선택지가 주어졌을 때, 답을 찾는 객관식 문제입니다. 입력값은 text이며, 아래 Fewshot 예시의 텍스트를 system prompt 혹은 context로 함께 제공할 수 있습니다.
- 한국어 데이터를 생성하기 위해, 여러 금융 문제가 있는 공공 사이트의 문제들을 크롤링하여 수집, 검수(104건)하였습니다. 그리고 Wikipedia와 공공사이트들의 금융사전/보고서들을 기반으로 GPT-4로 문제를 생성하고 사람이 검수하였습니다.(315건)
  

### 데이터 출처

- [한국어 wikipedia 금융 분류](https://ko.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EA%B8%88%EC%9C%B5) 
- [한국은행 경제연구 보고서](https://www.bok.or.kr/portal/bbs/P0002454/list.do?menuNo=200431)
- [경제배움e - 퀴즈로 배우는 시사.경제](https://www.econedu.go.kr/mec/ots/brd/list.do?mnuBaseId=MNU0000286&tplSer=ac73e13e-2d3c-485c-b7fe-a5823b527ead)


### 데이터 예시
```
{
  'conversation_id': 'financial_mmlu_0',
  'conversations': array([
    {
      'from': 'human',
      'value': '금리의 종류에 대한 설명으로 바르지 않은 것은?\n
            1. 변동금리는 시장금리 변동에 따른 위험을 자금공급자가 부담하게 된다\n
            2. 피셔방정식에 의하면 실질금리는 명목금리에서 기대인플레이션을 차감하면\n 구할 수 있다.\n
            3. 복리는 원금에 대한 이자뿐 아니라 이자에 대한 이자도 함께 계산하는 방법이\n다.\n
            4. 실효금리는 이자지급방법, 상환방법, 수수료, 세금 등을 감안한 후 차입자가\n실질적으로 부담하는 순자금조달비용을 말한다.\n
            5. 채권시장에서는 금리보다 수익률이라는 용어를 더 많이 사용한다.'
    },
    {
      'from': 'gpt',
      'value': '1'
    }
  ], dtype=object)
}

```

### Fewshot 예시
```
You are a financial expert.
You must answer the user's question correctly.
Answer the user's question with a number.
 
Example 1=\"\"\"
User: 다음은 통화기능 중 어느 것과 관련성이 높은가?
장래에 지급해야 하는 채무는 화폐로 표시할 수 있다. 
이는 화폐의 액면가치가 노동력이나 물품과 달리 소멸되거나 변질되지 않기 때문이다.
1. 교환의 매개 수단
2. 가치척도의 수단
3. 가치저장의 수단
4. 이연지급의 수단
5. 투자수단
Assistant: 4
\"\"\"

Example 2=\"\"\"
User: ( )은(는) 2006년 2월 앨런 그리스펀 뒤를 이어 미국 중앙은행인 연방준비제도이사회(FRB)의 의장이 된 벤 버냉키(Ben Shalom Bernanke)의 별명이다. 이 별명에 걸맞게 2조 달러가 넘는 자금을 시장에 뿌려 미국 금융시장을 벼랑 끝에서 건져내는 데 성공했다는 평가도 받고 있다.
1. 헬리콥터 벤
2. 전투기 벤
3. 열기구 벤
4. 비행기 벤
Assistant: 1
\"\"\"

```

License
- Wikipedia: CC BY-SA 4.0
- [한국은행 저작권 보호방침](https://www.bok.or.kr/portal/main/contents.do?menuNo=200228)