---
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: chosen
    dtype: string
  - name: rejected
    dtype: string
  splits:
  - name: train
    num_bytes: 91300170
    num_examples: 28797
  - name: validation
    num_bytes: 12230414
    num_examples: 3888
  download_size: 41052516
  dataset_size: 103530584
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
task_categories:
- question-answering
language:
- ko
tags:
- card
- finance
- dpo
size_categories:
- 1M<n<10M
---
# Card-Callcenter-DPO-Dataset

## Dataset Summary
This dataset is derived from call center data provided by Card, processed for Direct Preference Optimization (DPO) tasks. It contains 28,797 training samples and 3,888 validation samples, totaling 32,685 instances. The data consists of anonymized call center conversations with sensitive information (e.g., names, account numbers) masked for privacy. The dataset is designed to evaluate customer satisfaction levels ("만족", "미흡", "해결 불가", "추가 상담 필요") based on dialogue interactions.

## Licensing
The dataset is subject to the AI Hub license terms. It is intended for research and non-commercial use only unless otherwise permitted by AI Hub. Please refer to the original license at the AI Hub website for detailed conditions.

## Source
This dataset is derived from AI Hub (https://www.aihub.or.kr/aihubdata/data/view.do?dataSetSn=71844) and is used under the terms of its license. All major sensitive information has been non-identifiable. Users are advised to review the AI Hub license agreement for permissible use cases.

## Supported Tasks
- Text classification
- Preference optimization (DPO)

## Languages
- Korean

## Dataset Structure
- `prompt`: Call center conversation transcript with a follow-up question to evaluate satisfaction.
- `chosen`: Preferred response indicating customer satisfaction level.
- `rejected`: Non-preferred response for DPO training.

## Dataset Statistics
Total Samples: 32,685
Train Samples: 28,797
Validation Samples: 3,888