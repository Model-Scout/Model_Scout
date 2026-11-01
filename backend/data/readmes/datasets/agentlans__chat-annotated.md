---
license: cc-by-4.0
configs:
- config_name: main
  data_files:
  - path:
    - annot.jsonl.zst
    split: train
  default: true
- config_name: difficulty
  data_files:
  - path:
    - difficulty_train.jsonl.zst
    split: train
  - path:
    - difficulty_test.jsonl.zst
    split: test
- config_name: safety
  data_files:
  - path:
    - safety_train.jsonl.zst
    split: train
  - path:
    - safety_test.jsonl.zst
    split: test
- config_name: quality
  data_files:
  - path:
    - quality_train.jsonl.zst
    split: train
  - path:
    - quality_test.jsonl.zst
    split: test
- config_name: refusal
  data_files:
  - path:
    - refusal_train.jsonl.zst
    split: train
  - path:
    - refusal_test.jsonl.zst
    split: test
- config_name: accept
  data_files:
  - path:
    - accept_train.jsonl.zst
    split: train
  - path:
    - accept_test.jsonl.zst
    split: test
language:
- en
- zh
- ru
- ar
- es
- fr
- vi
- id
- pt
- ja
- fa
- de
- ko
- tr
- it
- pl
- ta
- si
- uk
- ro
task_categories:
- text-classification
- text-ranking
---
# Annotated Human-AI Chats


| Variable   | Mean   | Standard Deviation |
|------------|--------:|--------------------:|
| safety     | 6.5310 | 1.0179             |
| quality    | 7.8994 | 1.9667             |
| difficulty | 6.6519 | 2.1795             |

There are two columns for refusal:
- `refusal`: the categories from [agentlans/chat-refusal](https://huggingface.co/datasets/agentlans/chat-refusal)
- `refusal_classifier`: the output of
  - [agentlans/snowflake-arctic-embed-xs-refusal-classifier](https://huggingface.co/agentlans/snowflake-arctic-embed-xs-refusal-classifier) for English conversations
  - [agentlans/multilingual-e5-small-refusal-classifier](https://huggingface.co/agentlans/multilingual-e5-small-refusal-classifier) for non-English conversations

The `accept` column is true if safety > 5, quality > 6, and refusal_classifier is "Non-refusal".

| Language | Number of rows |
|:----------:|----------------:|
| en       | 50000          |
| zh       | 12372          |
| ru       | 11229          |
| ar       | 3207           |
| es       | 3138           |
| fr       | 2898           |
| vi       | 2674           |
| id       | 2570           |
| pt       | 2192           |
| ja       | 1237           |
| fa       | 1008           |
| de       | 957            |
| ko       | 802            |
| tr       | 770            |
| it       | 610            |
| pl       | 392            |
| ta       | 297            |
| si       | 266            |
| uk       | 223            |
| ro       | 206            |

| Source                              | Count |
|-------------------------------------|-------:|
| [allenai/WildChat](https://huggingface.co/datasets/allenai/WildChat)                    | 36508 |
| [QuixiAI/dolphin-distill](https://huggingface.co/datasets/QuixiAI/dolphin-distill)             | 16363 |
| [arcee-ai/The-Tome](https://huggingface.co/datasets/arcee-ai/The-Tome)                   | 8688  |
| [allenai/tulu-3-sft-mixture](https://huggingface.co/datasets/allenai/tulu-3-sft-mixture)          | 8375  |
| [Locutusque/hercules-v6.9](https://huggingface.co/datasets/Locutusque/hercules-v6.9)            | 7501  |
| [BAAI/Infinity-Instruct 7M_core](https://huggingface.co/datasets/BAAI/Infinity-Instruct)      | 7411  |
| [mlabonne/open-perfectblend](https://huggingface.co/datasets/mlabonne/open-perfectblend)          | 6789  |
| [NousResearch/Hermes-3-Dataset](https://huggingface.co/datasets/NousResearch/Hermes-3-Dataset)       | 5949  |
| [agentlans/DSULT-Core-ShareGPT-X](https://huggingface.co/datasets/agentlans/DSULT-Core-ShareGPT-X)     | 1473  |
| [openchat/openchat_sharegpt4_dataset](https://huggingface.co/datasets/openchat/openchat_sharegpt4_dataset) | 938   |