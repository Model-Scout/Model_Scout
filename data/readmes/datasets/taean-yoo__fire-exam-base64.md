---
language:
  - ko
license: cc-by-4.0
size_categories:
  - 1K<n<10K
task_categories:
  - question-answering
  - multiple-choice
pretty_name: Fire Exam QA with Images
tags:
  - fire-service
  - multimodal
  - korean
dataset_info:
  features:
    - name: question_id 
      dtype: string
    - name: question 
      dtype: string
    - name: options
      sequence: string
    - name: answer
      dtype: string
    - name: image 
      dtype: image 
---
# 🔥 Fire Exam Dataset with Images

이 데이터셋은 소방공무원 시험 문제를 기반으로 구성된 멀티모달 QA 데이터셋입니다.  
각 샘플은 문제 텍스트, 선택지, 정답, 그리고 시각 정보를 담은 이미지 파일 경로를 포함하고 있습니다.
