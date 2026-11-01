---
language:
- ko
---
# mathqa-ko
- `mathqa-ko` 데이터는 일반(general) 도메인의 QA 데이터셋입니다. Context와 Question이 주어졌을 때, 질문에 상응하는 답을 생성해야 합니다.
입력값으로는 text만이 주어집니다.

### Test Data의 구축
- 원본 데이터의 passage, question number(와 unit)을 그대로 사용합니다.
- Test를 위해 랜덤하게 90개를 선택하였습니다.

### 데이터 출처
- [숫자연산 기계독해 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71568)


# tableqa-ko
- `tableqa-ko` 데이터는 일반(general) 도메인의 QA 데이터셋입니다. Context와 Question이 주어졌을 때 질문에 상응하는 답을 생성해야 하며, 입력값으로는 text와 table이 함께 주어집니다.
`conversation_id`에 '`tableqa-short`'이 포함된 경우에는 3어절 이내의 짧은 답변을 생성해야 하는 반면, '`tableqa-long`'이 포함된 경우에는 장문의 텍스트를 생성해야 합니다.

### Test Data의 구축
- 원본데이터의 context와 question을 사용합니다. LLM의 자연스러운 답변을 위해 GPT-4로 자연스러운 답변을 생성하였습니다.
- Test를 위해 랜덤하게 104건의 데이터를 선태갛였고 tableqa-short은 32건, tableqa-long은 72건입니다.

### 데이터 출처
- [AIHUB의 표 정보 질의응답 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71565)


# 데이터의 비공개 사유
[AIhub의 데이터 이용정책](https://www.aihub.or.kr/intrcn/guid/usagepolicy.do?currMenu=151&topMenu=105)의 AI 허브 개방 데이터 > 데이터 이용정책 5항에 의거 테스트데이터를 공개할 수 없음을 고지합니다.