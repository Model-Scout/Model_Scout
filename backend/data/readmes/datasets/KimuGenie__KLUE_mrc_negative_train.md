---
dataset_info:
  features:
  - name: title
    dtype: string
  - name: context
    dtype: string
  - name: question
    dtype: string
  - name: id
    dtype: string
  - name: answers
    struct:
    - name: answer_start
      sequence: int64
    - name: text
      sequence: string
  - name: document_id
    dtype: int64
  - name: hard_negative_text
    sequence: string
  - name: hard_negative_document_id
    sequence: int64
  - name: hard_negative_title
    sequence: string
  splits:
  - name: train
    num_bytes: 205021808
    num_examples: 3952
  - name: validation
    num_bytes: 12329366
    num_examples: 240
  download_size: 124133126
  dataset_size: 217351174
license: cc-by-4.0
task_categories:
- question-answering
language:
- ko
---
# Dataset Card for "KLUE_mrc_negative_train"

KLUE mrc train dataset에 BM25을 이용해서 question에 대한 hard negative text 20개를 추가한 데이터입니다.

BM25로 hard negative text를 찾았고, preprocessing을 통해 중복 데이터를 최대한 삭제했습니다.

사용한 BM25의 정보는 아래와 같습니다.

|top-k|top-10|top-20|top-50|top-100|
|-|-|-|-|-|
|accuracy(%)|92.1|95.0|97.1|98.8|


# Citation
```
@misc{park2021klue,
      title={KLUE: Korean Language Understanding Evaluation}, 
      author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jungwoo Ha and Kyunghyun Cho},
      year={2021},
      eprint={2105.09680},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
