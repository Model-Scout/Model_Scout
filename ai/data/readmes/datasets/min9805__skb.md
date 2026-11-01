---
annotations_creators:
- expert-generated
language_creators:
- expert-generated
language:
- ko
license:
- cc-by-sa-4.0
multilinguality:
- monolingual
size_categories:
- 10K<n<100K
source_datasets:
- original
task_categories:
- fill-mask
- question-answering
- text-classification
- text-generation
- token-classification
task_ids:
- extractive-qa
- named-entity-recognition
- natural-language-inference
- parsing
- semantic-similarity-scoring
- text-scoring
- topic-classification
paperswithcode_id: klue
pretty_name: KLUE
tags:
- relation-extraction
dataset_info:
- config_name: ynat
  features:
  - name: guid
    dtype: string
  - name: title
    dtype: string
  - name: label
    dtype:
      class_label:
        names:
          '0': action_id:click.top_gnb.app_menu
          '1': action_id:page_show
          '2': action_id:rcu_event
          '3': page_id:home
          '4': action_body.result:잼키즈
          '5': action_body.result:유튜브
---