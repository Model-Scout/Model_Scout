---
language:
- ko
tags:
- counsel
- chat
- conversation
- ko
- korean
- dialogue
- talk
- friend
- friendly
license: mit
task_categories:
- question-answering
- summarization
- translation
---

# Korean Chat Friendly Dataset

## Dataset Summary
The **Korean Chat Friendly** dataset is a curated combination of two publicly available datasets:
1. [Korean Safe Conversation](https://huggingface.co/datasets/jojo0217/korean_safe_conversation)
2. [Mental Health Counseling Conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations)

This dataset was created by translating and summarizing the original conversations and then modifying the tone to resemble friendly conversations between friends. It is ideal for applications related to conversational AI, natural language understanding, and empathetic dialogue modeling in Korean.

## Dataset Structure
- **Files**: 
  - `summarized_safe_conversation.csv`: Contains summarized, friendly-tone conversations derived from the original Korean Safe Conversations dataset.
  - `summarized_translated_counseling.csv`: Contains translated, summarized, and tone-modified conversations based on the Mental Health Counseling dataset.
- **Columns**:
  - `short_question`: The input questions or conversational prompts.
  - `short_answer`: The corresponding friendly responses.
  
- **Splits**: 
  - The dataset currently has only a `train` split.
  
- **Dataset Sizes**: 
  - `summarized_safe_conversation.csv`: 6.32 MB
  - `summarized_translated_counseling.csv`: 406 KB

## Supported Tasks and Leaderboards
This dataset is well-suited for several tasks, including:
- **Question Answering**: Friendly responses to common queries or concerns.
- **Summarization**: Creating short and casual responses for conversational agents.
- **Translation**: For models that work on Korean-English translations, especially in conversational settings.

## Languages
- **Korean** (`ko`)

## Dataset Usage
To use this dataset, you can load it using the Hugging Face `datasets` library:

```python
from datasets import load_dataset

dataset = load_dataset("jaewanlee/korean_chat_friendly", data_files="dataset.csv")

```
# Citation

If you use this dataset in your work, please consider citing the original datasets and this dataset as follows:

```
@misc{korean_chat_friendly,
  author = {Jaewan Lee},
  title = {Korean Chat Friendly},
  year = {2024},
  url = {https://huggingface.co/datasets/jaewanlee/korean_chat_friendly}
}

@misc{korean_safe_conversation,
  author = {Jojo0217},
  title = {Korean Safe Conversation},
  url = {https://huggingface.co/datasets/jojo0217/korean_safe_conversation}
}

@misc{mental_health_counseling_conversations,
  author = {Amod},
  title = {Mental Health Counseling Conversations},
  url = {https://huggingface.co/datasets/Amod/mental_health_counseling_conversations}
}
```

# Models Trained on This Dataset

You can use this dataset to fine-tune models for conversational tasks in Korean. If you have fine-tuned models using this dataset, feel free to add them here.