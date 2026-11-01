---
language:
- ko
dataset_info:
  features:
  - name: index
    dtype: int64
  - name: question
    dtype: string
  - name: image
    dtype: image
  - name: answer
    dtype: string
  splits:
  - name: dev
    num_bytes: 102449207.875
    num_examples: 4329
  download_size: 96073232
  dataset_size: 102449207.875
configs:
- config_name: default
  data_files:
  - split: dev
    path: data/dev-*
---

[NCSOFT/K-MMBench](https://huggingface.co/datasets/NCSOFT/K-MMBench) 를 쓰기 좋게 바꾸어놓았습니다.

아래 코드를 이용하였습니다.
```python
from datasets import load_dataset, DatasetDict, Dataset
from huggingface_hub import login; login(token="YOUR TOKEN")

dataset = load_dataset("NCSOFT/K-MMBench")

def process_dataset(dataset):
    # 새로운 데이터 준비
    new_data = {
        'index': [],
        'question': [],
        'image': [],
        'answer': []
    }
    
    for item in dataset:
        # 필요한 필드 추출
        index = item['index']
        original_question = item['question']
        hint = item.get('hint', '')
        a = item['A']
        b = item['B']
        c = item.get('C', '')  # C와 D는 선택적일 수 있음
        d = item.get('D', '')
        answer = item['answer']
        image = item['image']
        
        # 새로운 형식의 질문 만들기
        formatted_question = ""
        if hint:
            formatted_question += f"힌트: {hint}\n"
        formatted_question += f"질문: {original_question}\nOptions:\nA. {a}\nB. {b}"
        
        if c:  # C 옵션이 있는 경우
            formatted_question += f"\nC. {c}"
        
        if d:  # D 옵션이 있는 경우
            formatted_question += f"\nD. {d}"
            
        formatted_question += "\n주어진 선택지 중 해당 옵션의 문자로 직접 답하세요."
        
        # 새 데이터에 추가
        new_data['index'].append(index)
        new_data['question'].append(formatted_question)
        new_data['image'].append(image)
        new_data['answer'].append(answer)
    
    # 새로운 Dataset 생성
    return Dataset.from_dict(new_data)

# 각 분할(split)별로 처리
new_datasets = {}
for split_name, split_dataset in dataset.items():
    new_datasets[split_name] = process_dataset(split_dataset)

# 새로운 DatasetDict 만들기
new_dataset_dict = DatasetDict(new_datasets)

new_dataset_dict.push_to_hub("Ryoo72/K-MMBench")
```