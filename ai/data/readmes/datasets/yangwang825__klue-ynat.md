---
task_categories:
- text-classification
language:
- ko
dataset_info:
  features:
    - name: text
      dtype: string
    - name: label
      dtype:
        class_label:
          names:
            '0': IT과학
            '1': 경제
            '2': 사회
            '3': 생활문화
            '4': 세계
            '5': 스포츠
            '6': 정치
---