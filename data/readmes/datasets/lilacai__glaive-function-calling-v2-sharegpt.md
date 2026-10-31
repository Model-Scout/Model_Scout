---
dataset_info:
  features:
  - name: chat
    dtype: string
  - name: system
    dtype: string
  - name: __hfsplit__
    dtype: string
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  splits:
  - name: train
    num_bytes: 509687903
    num_examples: 112960
  download_size: 196572451
  dataset_size: 509687903
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
# Dataset Card for "glaive-function-calling-v2-sharegpt"

This dataset takes the [glaive/glaive-function-calling-v2](https://huggingface.co/datasets/glaiveai/glaive-function-calling-v2) dataset and formats it with ShareGPT using [Lilac](https://lilacml.com/)

The accompanying notebook can be found [here](https://github.com/lilacai/lilac/blob/main/notebooks/GlaiveToShareGPT.ipynb).

The original columns "system" and "chat" still exist on the dataset.

There are 4 types of roles in the ShareGPT format:
- system
- user
- human
- function call

The original dataset has a column called 'chat' with the following structure:
```
USER: Hi, I need help with calculating a tip. My bill is $50 and I want to leave a 20% tip. 


ASSISTANT: Sure, let me calculate that for you. <|endoftext|>


ASSISTANT: <functioncall> {"name": "calculate_tip", "arguments": '{"bill_amount": 50, "tip_percentage": 20}'} <|endoftext|>


FUNCTION RESPONSE: {"tip_amount": 10}


ASSISTANT: Based on the bill amount and the tip percentage you provided, the tip you should leave is $10. <|endoftext|>
```

This dataset is a version that converts it into the ShareGPT format:
```
conversations: [{
  'from': "user",
  'value': 'Hi, I need help with calculating a tip. My bill is $50 and I want to leave a 20% tip.'
}, {
  'from': 'assistant',
  'value': 'Sure, let me calculate that for you. <|endoftext|>'
}, {
  'from': 'assistant',
  'value': '<functioncall> {"name": "calculate_tip", "arguments": '{"bill_amount": 50, "tip_percentage": 20}'} <|endoftext|>'
}, {
  'from': 'assistant',
  'value': '<functioncall> {"name": "calculate_tip", "arguments": '{"bill_amount": 50, "tip_percentage": 20}'} <|endoftext|>'
}, {
  'from': 'function response',
  'value': '{"tip_amount": 10}',
}, {
  'from': assistant',
  'value': 'Based on the bill amount and the tip percentage you provided, the tip you should leave is $10. <|endoftext|>'
}]
```

[More Information needed](https://github.com/huggingface/datasets/blob/main/CONTRIBUTING.md#how-to-contribute-to-the-dataset-cards)