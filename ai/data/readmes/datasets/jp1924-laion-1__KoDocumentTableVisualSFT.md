---
dataset_info:
  config_name: SFT
  features:
  - name: id
    dtype: int32
  - name: image
    dtype: image
  - name: conversations
    list:
    - name: role
      dtype: string
    - name: content
      dtype: string
  - name: metadata
    struct:
    - name: class
      dtype: string
    - name: code
      dtype: string
    - name: created
      dtype: string
    - name: doc_id
      dtype: int32
    - name: doc_published
      dtype: int32
    - name: doc_source
      dtype: string
    - name: doc_title
      dtype: string
    - name: ori_html
      dtype: string
    - name: sim_html
      dtype: string
    - name: col_num
      dtype: int32
    - name: row_num
      dtype: int32
  splits:
  - name: train
    num_bytes: 6147314529.54
    num_examples: 60142
  - name: validation
    num_bytes: 684950343.31
    num_examples: 6613
  download_size: 4512113112
  dataset_size: 6832264872.85
configs:
- config_name: SFT
  data_files:
  - split: train
    path: SFT/train-*
  - split: validation
    path: SFT/validation-*
task_categories:
- table-question-answering
- image-to-text
language:
- ko
---
[ImageTextToTextPipeline](https://huggingface.co/docs/transformers/main/chat_templating_multimodal#imagetexttotextpipeline)을 참고해서 conversations를 제작했다.    
그래서 데이터를 사용할때 json.loads를 활용해서 각 turn을 불러와야한다.