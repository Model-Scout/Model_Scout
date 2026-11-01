---
dataset_info:
  features:
  - name: ori_index
    dtype: int64
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
  splits:
  - name: train
    num_bytes: 1777475
    num_examples: 1000
  download_size: 974043
  dataset_size: 1777475
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

- 본 데이터의 Type 은 `'가산/감산'` 로만 구성되어 있습니다.
- 데이터 예시
  
```
### context ###
2분기 순이익만 떼서 보면 증가세가 더욱 뚜렷하다. 신한금융은 9961억원, KB금융은 9911억원으로 1분기보다 각각 8.5%, 17.2% 늘었다. 하나금융은 6584억원, 우리금융은 6103억원으로 증가율은 각각 20.6%, 7.3%이다. 특히 KB금융은 분기 기준 사상 최대 실적을 올렸다.
수출 부진에 미·중 무역전쟁, 일본 수출규제 등의 내우외환이 겹쳐 저조한 성적표를 받은 일반 기업들과 달리 금융지주사들만 웃는 모습이다. 금융지주사들이 성적표에 제각각 '역대 최대'라는 수식어를 붙있을 수 있었던 원동력은 은행 담보대출 위주의 이자 수익 덕분이다. 이자 이익은 올해 상반기에도 증가세를 이어갔다. 신한·KB금융의 상반기 이자 이익은 각각 3조9041억원, 4조5492억원으로 지난해보다 5.6%, 4.8% 늘었다. 우리금융은 2조9309억원이었다. 하나금융은 지난해보다 5.3% 많은 2조8866억원을 기록했다. 이들 4개 금융 그룹이 상반기에 거둔 이자 이익은 총 14조2700억여원에 이른다.


### question ###
2분기 신한금융과 KB금융의 순이익의 합은 얼마인가?


### answer ###
{'number': {'calculation': '996100000000+991100000000', 'calculation_type': '가산/감산', 'number': '1987200000000', 'transcription': '일조구천팔백칠십이억', 'unit': '원'}, 'date': None, 'spans': None}


### gen_answer ###
2분기 신한금융과 KB금융의 순이익을 합산하면 1조9872억 원입니다. 신한금융의 순이익은 9961억 원, KB금융의 순이익은 9911억 원으로, 두 금융사의 순이익을 더한 값입니다.
```

## 답변 생성 코드

```
## model choice
model = "gpt-4o"

## system prompt 입력
system_string = '##context## and ##question## 이 주어지면, ##json answer## 참고하여 친절하고 상세한 답변을 만들어주세요. 답변에는 근거가 포함된 상세한 설명이 있어야 합니다.'

question = '''##context##
{context}

##question##
{question}'''

answer = '''##json answer##
{json_answer}
해당 정보에서 calculation, number, transcription, unit 정보를 참고하여 자연스럽고 친절하며 상세한 답변을 생성하겠습니다.

##text answer##
{text_answer}'''


## context for one shot
one_shot_question = question.format(
    context = new_df.context[5],
    question = new_df.question[5]
)
one_shot_answer = answer.format(
    json_answer = eval(new_df.answer[5]).get("number"),
    text_answer = '통계청에 따르면, 4월과 5월의 월 평균 소매 판매액은 43조2045억 원으로, 1분기의 월 평균 소매 판매액인 40조957억 원에 비해 3조1088억 원 증가했습니다.'
)


## context for two shot
two_shot_question = question.format(
    context = new_df.context[12],
    question = new_df.question[12]
)
two_shot_answer = answer.format(
    json_answer = eval(new_df.answer[12]).get("number"),
    text_answer = '국토부가 지난 4월 실시한 수도권 5개 단지 신혼부부·다자녀 특별공급 당첨자 대상 표본 점검 결과, 임신진단서를 제출해 당첨된 83건 중 8건이 허위서류에 의한 부정청약으로 적발되었습니다. 따라서 부정청약이 아닌 건수는 75건입니다.'
)

## 생성하고자 하는 question 입력
current_question = question.format(
    context = new_df.context[index],
    question = new_df.question[index]
)
## 생성하고자 하는 answer 입력
current_answer = answer.format(
    json_answer = eval(new_df.answer[index]).get("number"),
    text_answer = ''
)

## 답변 생성
completion = client.chat.completions.create(
    model= model,
    messages= [
        {"role": "system", "content": system_string},
        {"role": "user", "content": one_shot_question},
        {"role": "assistant", "content": one_shot_answer},
        {"role": "user", "content": two_shot_question},
        {"role": "assistant", "content": two_shot_answer},
        {"role": "user", "content": current_question},
        {"role": "assistant", "content": current_answer}
    ],
    temperature = 0,
    # timeout = 40,
    n = 1
)
```

## License

<img src="https://huggingface.co/datasets/TwinDoc/math-qa-sample_addsub-ko/resolve/main/license__icon.png"  width="324">

The content of this project, created by AGILESODA, is licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).