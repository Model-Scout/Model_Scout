---
language:
- ko
license: apache-2.0
task_categories:
- question-answering
- multiple-choice
- text-generation
dataset_info:
- config_name: mcqa
  features:
  - name: reference
    dtype: string
  - name: question
    dtype: string
  - name: options
    sequence: string
  - name: reasoning_process
    dtype: string
  - name: n_options
    dtype: int64
  - name: answer
    dtype: string
  - name: step
    dtype: int64
  - name: value
    dtype: int64
  - name: type
    dtype: string
  splits:
  - name: train
    num_bytes: 46733377
    num_examples: 42463
  download_size: 22153268
  dataset_size: 46733377
- config_name: qa
  features:
  - name: reference
    dtype: string
  - name: question
    dtype: string
  - name: answer_A
    dtype: string
  - name: answer_B
    dtype: string
  - name: preference
    dtype: string
  - name: preference_desc
    dtype: string
  - name: value
    dtype: int64
  - name: type
    dtype: string
  splits:
  - name: train
    num_bytes: 164002895
    num_examples: 44870
  download_size: 78226614
  dataset_size: 164002895
- config_name: validation
  features:
  - name: question
    dtype: string
  - name: options
    sequence: string
  - name: reasoning_process
    dtype: string
  - name: answer
    dtype: string
  - name: task
    dtype: string
  - name: n_options
    dtype: string
  - name: type
    dtype: string
  splits:
  - name: train
    num_bytes: 96378
    num_examples: 112
  download_size: 52314
  dataset_size: 96378
configs:
- config_name: mcqa
  data_files:
  - split: train
    path: mcqa/train-*
- config_name: qa
  data_files:
  - split: train
    path: qa/train-*
- config_name: validation
  data_files:
  - split: train
    path: validation/train-*
tags:
- finance
- accounting
- stock
- quant
- economics
---
# FinShibainu Datset Card

+ github: [https://github.com/aiqwe/FinShibainu](https://github.com/aiqwe/FinShibainu)
+ model: [https://huggingface.co/aiqwe/FinShibainu](https://huggingface.co/aiqwe/FinShibainu)

[KRX LLM 경진대회 리더보드](https://krxbench.koscom.co.kr/)에서 우수상을 수상한 shibainu24 모델의 데이터셋 Repository입니다.  
모델에 대한 내용은 [https://huggingface.co/aiqwe/FinShibainu](https://huggingface.co/aiqwe/FinShibainu)를 참조해주세요.  
데이터셋 수집 및 학습에 관련된 코드는 [https://github.com/aiqwe/FinShibainu](https://github.com/aiqwe/FinShibainu)에 자세하게 공개되어 있습니다.

## DPO
Preference의 A는 `answer_A`, B는 `answer_B` 컬럼입니다.
- `answer_A`: Reference와 질문을 함께 제공받은 gpt 답변. Reference에 의존적이고 짧지만 정확한 답변을 생성함
- `answer_B`: Reference없이 질문만 제공받은 gpt의 답변. 좀더 창의적인 긴 답변을 생성하나 보다 정확하지 못함
Choosen 데이터는 `preference` 컬럼을 기준으로 전처리하면됩니다.


# References
각 Reference들은 다음 링크로 연결되어 있습니다.  

| reference                      | url                                                                                    |
|:-------------------------------|:---------------------------------------------------------------------------------------|
| 한국은행_경제금융_용어_700선   | [Link](https://www.bok.or.kr/portal/bbs/B0000249/view.do?nttId=235017&menuNo=200765)   |
| KRX_규정                       | [Link](https://law.krx.co.kr/las/TopFrame.jsp&KRX)                                     |
| KRX_비정기간행물               | [Link](http://open.krx.co.kr/contents/OPN/04/04020000/OPN04020000.jsp)                 |
| KRX_청소년을위한_증권투자      | [Link](https://main.krxverse.co.kr/_contents/ACA/02/02010200/file/220104_teen.pdf)     |
| KRX_초보투자자_증권따라잡기    | [Link](https://main.krxverse.co.kr/_contents/ACA/02/02010200/file/220104_beginner.pdf) |
| 지식경제용어사전               | [Link](https://terms.naver.com/list.naver?cid=43668&categoryId=43668)                  |
| 재무회계_목차기반_자체생성     | [Link](-)                                                                              |
| 시사경제용어사전               | [Link](https://terms.naver.com/list.naver?cid=43665&categoryId=43665)                  |
| 사업보고서_사업의내용          | [Link](https://opendart.fss.or.kr/)                                                    |
| web_text_synthetic_dataset_50k | [Link](https://huggingface.co/datasets/Cartinoe5930/web_text_synthetic_dataset_50k)    |
| 금융감독용어사전               | [Link](https://terms.naver.com/list.naver?cid=42088&categoryId=42088)                  |

# config_name
- `mcqa`: `shibainu24` 모델의 MCQA 학습에 사용된 데이터
- `qa`: `shibainu24` 모델의 QA학습에 사용된 데이터
- `validation`: `shibainu24` 모델 Checkpoint 테스트시 사용한 Validation 데이터(MCQA 형태)

# columns
## MCQA
- `reference`: 참조 문서명
- `question`: 질문
- `options`: 선택지
- `reasoning_process`: 풀이 과정. 모델의 Reasoning 과정을 생성
- `n_options`: `options`의 선택지 갯수
- `answer`: 선택한 정답
- `step`: 단계 구분(step이 0인 경우는 예선에 사용한 데이터이며 step=1 프롬프트와 동일함)
- `value`: 교육적 가치 평가 결과
- `type`: 'mcqa' 데이터 타입

## QA
- `reference`: 참조 문서명
- `question`: 질문 
- `answer_A`: Reference를 기반으로 생성한 첫번째 답변
- `answer_B`: Reference 없이 질문만으로 생성한 두번째 답변
- `preference`: Preference 선택 값
  - `A`: `old_ansewr`를 선호
  - `B`: `answer`를 선호
  - `E`: 동등
- `preference_desc`: Preference의 근거
- `value`: 교육적 가치 평가 결과
- `type`: 'qa' 데이터 타입

# Citation
```bibitex
@misc{jaylee2024finshibainu,
  author = {Jay Lee},
  title = {FinShibainu: Korean specified finance model},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  url = {https://github.com/aiqwe/FinShibainu}
}
```