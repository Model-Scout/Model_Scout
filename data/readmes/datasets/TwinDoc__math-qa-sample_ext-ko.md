---
dataset_info:
  features:
  - name: mediatype
    dtype: string
  - name: medianame
    dtype: string
  - name: category
    dtype: string
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: calculation_type
    dtype: string
  - name: answer
    dtype: string
  - name: gen_answer
    dtype: string
  - name: input_token_len
    dtype: int64
  - name: output_token_len
    dtype: int64
  - name: ori_index
    dtype: int64
  splits:
  - name: train
    num_bytes: 2988068
    num_examples: 1000
  download_size: 1637687
  dataset_size: 2988068
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-nc-sa-4.0
task_categories:
- question-answering
language:
- ko
tags:
- economy
- mathQA
size_categories:
- 1K<n<10K
---

## 데이터 출처

- AI-HUB 에서 다운로드 받은 **숫자연산 기계독해 데이터** 를 사용해서 만든 데이터입니다.
- 경제 > Train > json 파일을 DataFrame 형태로 변형하여 전처리 및 답변 생성을 하였습니다.
  - Raw 데이터의 answer 정보를 참고하여 답변을 생성하였습니다.
  - 답변 생성 시 gpt-4o 를 활용했습니다.
- 저작권에 의해 본 데이터는 외부 반출 및 타인의 acess 승낙은 불허합니다.

## 데이터 설명

- 본 데이터의 Type 은 `'단서추출'` 로만 구성되어 있습니다.
- 데이터 예시
  
```
### context ###
서울시가 민속 대명절인 추석을 맞아 내달 1일부터 20일까지 상생상회(매장), 네이버(온라인), 롯데백화점(매장)과 함께 팔도특산물로 구성된 명절 직거래장터를 진행한다고 31일 밝혔다.
팔도특산물을 구매할 수 있는 지역상생 거점공간인 '상생상회' 매장에서는 상주, 제주 등 14개 시도의 117개 농가에서 생산한 총 416개 상품을 판매한다.
상주 곶감, 산청 상황버섯, 논산 딸기식초 등 각 지역을 대표하는 특산물로 구성된 추석 선물세트와 건나물, 약과, 전통주 등 제수상품을 원가보다 최대 50% 할인된 가격에 구입할 수 있다.
네이버에서는 전국 128개 농가의 지역 농수산식품 128개 품목을 구입할 수 있는 온라인 특별전을 1일부터 12일까지 진행한다. 추석 선물세트 뿐만 아니라 농수축산 및 가공식품 등 다양한 지역 상품을 구입할 수 있다.
또한 네이버 쇼핑라이브 방송을 통해 가평 홍로사과, 상주 샤인머스켓 등 추석 선물세트 판매방송도 진행한다. 1일부터 8일 중 5회 방송 예정이며, 생산자와 소비자가 실시간으로 소통하며 구매 가능하다.
롯데백화점에서는 전국 총 32개 지점에 배치된 추석 선물세트 카탈로그 '추석마중'를 통하여 전국 9개 농가, 9개 품목을 내달 20일까지 구입할 수 있다. 롯데 추석선물 카탈로그에 소개 되는 제품은 그동안 '시시호시' 판매코너에서 인기리에 판매됐던 서산 감태 세트부터 충주 사과한과, 영광 굴비 세트, 상주 곶감 세트 등 지역의 우수 농특산물로 구성됐다.
김광덕 서울시 도시농업과장은 “추석을 맞아 지역의 우수 농특산물 판매를 촉진하고, 코로나19로 판로확보에 어려움을 지역 농가의 어려움을 돕기 위해 특별전을 마련하게 됐다”면서 “지속적인 온오프라인 판로 지원을 통해 지역과 서울, 농어민과 소비자가 모두 상생할 수 있도록 노력하겠다” 고 말했다.


### question ###
상생상회 매장에서 판매되는 농가 생산 상품수는 네이버에서 판매되는 상품 수 보다 몇 % 더 많은가?


{'calculation': '(416-128)/128*100',
 'calculation_type': '단서추출',
 'end_index': 369,
 'start_index': 104,
 'text': "팔도특산물을 구매할 수 있는 지역상생 거점공간인 '상생상회' 매장에서는 상주, 제주 등 14개 시도의 117개 농가에서 "
         '생산한 총 416개 상품을 판매한다.\n'
         '상주 곶감, 산청 상황버섯, 논산 딸기식초 등 각 지역을 대표하는 특산물로 구성된 추석 선물세트와 건나물, 약과, 전통주 '
         '등 제수상품을 원가보다 최대 50% 할인된 가격에 구입할 수 있다.\n'
         '네이버에서는 전국 128개 농가의 지역 농수산식품 128개 품목을 구입할 수 있는 온라인 특별전을 1일부터 12일까지 '
         '진행한다.'}



### gen_answer ###
상생상회 매장에서 판매되는 농가 생산 상품 수는 총 416개입니다. 반면, 네이버에서는 128개의 농수산식품 품목을 판매합니다. 따라서 상생상회 매장에서 판매되는 상품 수는 네이버에서 판매되는 상품 수보다 더 많습니다.

이를 퍼센트로 계산하면 다음과 같습니다:

\[ \frac{(416 - 128)}{128} \times 100 = 225\% \]

즉, 상생상회 매장에서 판매되는 농가 생산 상품 수는 네이버에서 판매되는 상품 수보다 225% 더 많습니다. 이는 상생상회가 다양한 지역의 특산물을 더 많이 제공하고 있음을 의미합니다.
```

## 답변 생성 코드

```
## model choice
model = "gpt-4o"

## Prompt template
system_string = '##context## and ##question## 이 주어지면, ##json answer## 참고하여 친절하고 상세한 답변을 만들어주세요. 답변에는 근거가 포함된 상세한 설명이 있어야 합니다.'

question = '''##context##
{context}

##question##
{question}'''

answer = '''##json answer##
{json_answer}
해당 정보에서 계산의 결과는 calculation 값을 참고해야 하며, 답변을 위한 상세 설명을 위해서는 text 값을 참고해서 친절하고 상세한 답변을 생성해야 합니다.

##text answer##
{text_answer}'''


## context for one shot
one_shot_question = question.format(
    context = new_df.context[6],
    question = new_df.question[6]
)
one_shot_answer = answer.format(
    json_answer = eval(new_df.answer[6]).get("spans")[0],
    text_answer = "경기도가 올해부터 시행하는 '착한 임대인 지원사업'에 따르면, 50만 원 이상 100만 원 미만의 임대료를 인하한 임대인에게는 10만 원의 인센티브가 지급됩니다. 반면, 700만 원 이상 임대료를 인하한 임대인에게는 50만 원의 인센티브가 지급됩니다.\n\n따라서, 50만 원 이상 100만 원 미만 임대료를 인하한 임대인에게 지급되는 인센티브는 700만 원 이상 인하한 경우에 지급되는 인센티브의 20%입니다. 이는 10만 원을 50만 원으로 나누고 100을 곱한 결과로 계산할 수 있습니다:\n\n\\[ \\frac{10만 원}{50만 원} \\times 100 = 20\\% \\]\n\n이 계산을 통해, 50만 원 이상 100만 원 미만 임대료를 인하한 임대인에게 지급되는 인센티브가 700만 원 이상 인하한 경우 대비 20%임을 알 수 있습니다."
)

## 생성하고자 하는 question 입력
current_question = question.format(
    context = new_df.context[index],
    question = new_df.question[index]
)
## 생성하고자 하는 answer 입력
current_answer = answer.format(
    json_answer = eval(new_df.answer[index]).get("spans")[0],
    text_answer = ''
)


## 답변 생성
completion = client.chat.completions.create(
    model= model,
    messages= [
        {"role": "system", "content": system_string},
        {"role": "user", "content": one_shot_question},
        {"role": "assistant", "content": one_shot_answer},
        {"role": "user", "content": current_question},
        {"role": "assistant", "content": current_answer}
    ],
    temperature = 0,
    # timeout = 40,
    n = 1
)
```

## License

<img src="https://huggingface.co/datasets/TwinDoc/math-qa-sample_ext-ko/resolve/main/license__icon.png"  width="324">

The content of this project, created by AGILESODA, is licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).