---
dataset_info:
  features:
  - name: image
    dtype: image
  - name: id
    dtype: int64
  - name: caption_ko
    dtype: string
  - name: captions_ko
    sequence: string
  - name: captions_en
    sequence: string
  splits:
  - name: train
    num_bytes: 13990978862.039
    num_examples: 82783
  - name: validation
    num_bytes: 6603067389.408
    num_examples: 40504
  download_size: 20150633676
  dataset_size: 20594046251.447
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
task_categories:
- image-to-text
- text-to-image
language:
- ko
- en
tags:
- coco
- image caption
pretty_name: Ko COCO BAL
size_categories:
- 100K<n<1M
license: cc
---
# Ko COCO BAL
본 데이터셋은 기존의 [MS COCO의 영어 캡션을 한국어 문장으로 번역(AIHub)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=261)한 데이터셋의 한국어 묘사문을 통합하여 하나의 문장으로 생성한 데이터셋 입니다. 
생성된 문장은 `GPT-4o mini`를 이용하여 다음의 프롬프트를 이용해 재생성 하였습니다. 

```plain
다음은 어떠한 이미지에 대해 글자로 묘사해놓은 정보이다. 
모든 정보를 이용하여 텍스트의 모든 정보가 하나의 문장으로 변환하여라. 
위의 정보 이외의 출력은 하지 않으며, 중복되는 정보는 기입하지 않는다. 
단, 특정한 장소의 고유명사, 인물의 고유명사와 같은 정보는 반영하지 않은다.

{SENTENCES}

하나의 문장으로 변환된 결과:"
```

데이터셋 구성은 다음과 같습니다. 

| 항목          | 설명                                                 |
| ----------- | -------------------------------------------------- |
| id          | 데이터셋 고유 ID.<br>                                    |
| image       | PIL을 이용해 읽어온 이미지 객체. <br>                          |
| captions_en | MS COCO의 원본 영문 설명 리스트. <br>                        |
| captions_ko | `captions_en`의 기계 번역본 리스트. <br>                    |
| caption_ko  | `GPT-4o mini`를 이용해 `captions_ko`의 내용을 통합한 문장. <br> |