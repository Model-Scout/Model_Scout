---
dataset_info:
- config_name: tableqa
  features:
  - name: messages
    list:
    - name: content
      list:
      - name: image_url
        struct:
        - name: url
          dtype: string
      - name: text
        dtype: string
      - name: type
        dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 1909602675
    num_examples: 957
  - name: test
    num_bytes: 506976164
    num_examples: 240
  download_size: 194448054
  dataset_size: 2416578839
- config_name: tableqa_base64
  features:
  - name: messages
    list:
    - name: content
      list:
      - name: base64
        dtype: string
      - name: text
        dtype: string
      - name: type
        dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 1909599326
    num_examples: 957
  - name: test
    num_bytes: 506975324
    num_examples: 240
  download_size: 194447334
  dataset_size: 2416574650
configs:
- config_name: tableqa
  data_files:
  - split: train
    path: tableqa/train-*
  - split: test
    path: tableqa/test-*
- config_name: tableqa_base64
  data_files:
  - split: train
    path: tableqa_base64/train-*
  - split: test
    path: tableqa_base64/test-*
license: cc-by-sa-4.0
task_categories:
- text-generation
- summarization
- table-question-answering
language:
- ko
tags:
- finance
- legal
size_categories:
- 1K<n<10K
---

# 📊 Finance-Legal-MRC Chat Template

이 데이터셋은 문서 내 표 이미지와 문맥 정보를 기반으로, LLM이 description, title, summary, key_entities를 생성하도록 학습하기 위해 구성된 **Chat Template 형식의 Instruction Dataset**입니다.  
질문은 `user`가 주고, 정형화된 답변은 `assistant`가 응답하는 구조이며, 일부 메시지에는 표 이미지(`image_url`)가 포함됩니다.

---

## 📁 Dataset Overview

- **데이터 수**: 1,197개 (train/test 8:2 split)
- **언어**: Korean (한국어)
- **형식**: OpenAI/ChatGPT-style `messages` 구조
- **입력 정보**: 문맥(context) + 표 이미지(image_url)
- **출력 목표**:
  - `description`: 자연어로 푼 설명
  - `title`: 표를 대표하는 제목
  - `summary`: 주요 요약
  - `key_entities`: 핵심 엔티티 목록

---

## 🧱 Data Structure

각 샘플은 다음과 같은 메시지로 구성됩니다:

```json
{
  "messages": [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are a helpful assistant and specialized at table data in the document. Answer in Korean."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "[지시사항] 문서와 표를 기반으로 description, title, summary, key_entities를 생성하라..."
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/png;base64,..."  // base64 인코딩된 표 이미지
          }
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "{\"description\": \"...\", \"title\": \"...\", \"summary\": \"...\", \"key_entities\": [\"...\", \"...\"]}"
        }
      ]
    }
  ]
}
````

---

## 🛠 Use Case

이 데이터셋은 다음과 같은 목적에 사용할 수 있습니다:

* 🧠 Table-based Instruction Tuning
* 📌 Multimodal Input Handling (text + image)
* 🔎 Table Summarization / TIG (Table Info Generation)
* 🧪 CoT 기반 Table Reasoning 학습

---

## 📎 Tags

`table-data`, `chat-template`, `instruction-tuning`, `korean`, `multimodal`, `base64-image`, `structured-generation`, `openai-format`

---

## 📜 License

CC BY 4.0
저작자 표시 시 자유롭게 수정, 재배포, 파생작 사용이 가능합니다.

---

## ✍️ Author

* Dataset Curator: [@didi0di](https://huggingface.co/didi0di)
* Source: Internal task-specific synthetic data

```

