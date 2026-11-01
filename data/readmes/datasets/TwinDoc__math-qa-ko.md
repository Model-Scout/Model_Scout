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
  splits:
  - name: train
    num_bytes: 302532422
    num_examples: 168555
  download_size: 171217683
  dataset_size: 302532422
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
- 100K<n<1M
---

## 데이터 출처

- AI-HUB 에서 다운로드 받은 **숫자연산 기계독해 데이터** 입니다.
- 경제 > Train > json 파일을 DataFrame 형태로 변형하여 수정 없이 업로드하였습니다.
- 저작권에 의해 본 데이터는 외부 반출 및 타인의 acess 승낙은 불허합니다.

## 데이터 설명

- 본 데이터의 Type 은 `['양자/다자비교', '비율연산', '단서추출', '날짜추출', '가산/감산', '날짜가산/감산', '경계추출']` 로 구성되어 있습니다.
- '단서추출' 데이터 예시
  
```
{'idx': 'kpf.02100351.20220202090230002',
 'mediatype': '뉴스',
 'medianame': '이투데이',
 'category': '경제',
 'source': 'https://www.etoday.co.kr/news/view/2101739',
 'date': '2022-02-02',
 'title': '"고객이 직접 아이디어 제안"…SSG닷컴, 디자인ㆍ친환경 공모전 진행',
 'passage': "SSG닷컴은 고객이 직접 아이디어를 제안할 수 있는 디자인 공모전 및 친환경 아이디어 공모전을 동시 진행한다고 2일 밝혔다.\n총 상금 규모는 5000여만 원에 달하며 수상자 100여 명을 선정할 예정이다.\n우선 3일부터 20일까지 '제 1회 이마트몰 디자인 공모전'을 개최한다. 쓱배송의 쓱케치북을 주제로 선정해 SSG닷컴 당일 시간대 지정 배송 서비스인 쓱배송에 적용할 수 있는 디자인을 공모 받는다.\n디자인 주제는 캐릭터, 쓱배송, 장보기 등 3가지다. SSG닷컴 회원 누구나 참여할 수 있으며 ID당 최대 3개 작품까지 응모할 수 있다. 수상자 발표는 다음달 17일 예정이다.\n총 상금 규모는 3000만 원이다. 1등 쓱카소상 3명에게는 SSG머니 500만 원, 2등 쓱크리에이터 6명은 SSG머니 100만 원을 제공한다. 3등 쓱케치상 12명은 SSG머니 50만 원, 4등 쓱린이상 30명에게는 SSG머니 30만 원을 증정한다.\n추가로 28일까지 환경재단과 함께 '지쓱 가능한 세상을 위한 친환경 아이디어 공모전'도 시행한다. 자유 형식으로 구성해 누구나 쉽게 아이디어를 응모할 수 있다. SSG닷컴 직원 및 외부 환경전문가로 구성된 심사위원회를 거쳐 당선작을 선발한다. 내달 18일 이후 수상자 발표 예정이다.\n대상 1명에게 상금 500만 원, 최우수상 2명은 상금 300만 원, 우수상 6명은 상금 100만 원을 지급한다. 특별상 40명에게는 신세계상품권 5만 원을 증정한다.\n김진설 SSG닷컴 마케팅담당은 “'쓱닷컴이 내 회사'라는 생각을 가질 수 있는 공모전을 통해 자연스럽게 '팬슈머'를 확보하고 브랜드 충성도를 높일 수 있을 것으로 기대한다”며 “당선작은 향후 쓱닷컴이 진행하는 프로모션에 활용 예정이다”고 했다.",
 'qa_pairs': [{'query_id': 'cb1f217d-941b-4289-8ccd-6fc445a576a3',
   'question': 'SSG닷컴이 진행하는 제 1회 이마트몰 디자인 공모전에서 1등 수상자가 받는 SSG머니는 총상금 대비 몇 %인가?',
   'answer': {'number': None,
    'date': None,
    'spans': [{'calculation': '5000000/30000000*100',
      'calculation_type': '단서추출',
      'text': "우선 3일부터 20일까지 '제 1회 이마트몰 디자인 공모전'을 개최한다. 쓱배송의 쓱케치북을 주제로 선정해 SSG닷컴 당일 시간대 지정 배송 서비스인 쓱배송에 적용할 수 있는 디자인을 공모 받는다.\n디자인 주제는 캐릭터, 쓱배송, 장보기 등 3가지다. SSG닷컴 회원 누구나 참여할 수 있으며 ID당 최대 3개 작품까지 응모할 수 있다. 수상자 발표는 다음달 17일 예정이다.\n총 상금 규모는 3000만 원이다. 1등 쓱카소상 3명에게는 SSG머니 500만 원, 2등 쓱크리에이터 6명은 SSG머니 100만 원을 제공한다.",
      'start_index': 115,
      'end_index': 407}]}}]}
```

## 데이터 변환 코드

- AI-HUB 에서 다운로드 받은 json 파일을 DataFrame 형태로 변형 시 사용한 코드입니다.

```
import json

import pandas as pd
from collections import defaultdict

def convert2df(json_file):
    data_dict = defaultdict(list)
    
    for data in json_file.get('data'):
        mediatype = data.get('mediatype')
        medianame = data.get('medianame')
        category = data.get('category')
        title = data.get('title')
        context = data.get('passage')

        if len(data.get('qa_pairs')) > 1:
            import pdb; pdb.set_trace()
        else:
            answer = data.get('qa_pairs')[0].get('answer')
            question = data.get('qa_pairs')[0].get('question')
            
        if answer.get('spans') is not None:
            calculation_type = answer.get('spans')[0].get('calculation_type')
        elif answer.get('number') is not None:
            calculation_type = answer.get('number').get('calculation_type')
        elif answer.get('date') is not None:
            calculation_type = answer.get('date').get('calculation_type')
        else:
            import pdb; pdb.set_trace()

        data_dict['mediatype'].append(mediatype)
        data_dict['medianame'].append(medianame)
        data_dict['category'].append(category)
        data_dict['title'].append(title)
        data_dict['context'].append(context)
        data_dict['question'].append(question)
        data_dict['calculation_type'].append(calculation_type)
        data_dict['answer'].append(answer)
    return data_dict

data_dict = convert2df(json_file)
df = pd.DataFrame(data_dict)
```

## License

<img src="https://huggingface.co/datasets/TwinDoc/math-qa-ko/resolve/main/license__icon.png"  width="324">

The content of this project, created by AGILESODA, is licensed under the [Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/).