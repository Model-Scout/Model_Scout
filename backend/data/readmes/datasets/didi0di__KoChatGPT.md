---
license: unknown
dataset_info:
  features:
  - name: prompt
    dtype: string
  - name: completion
    dtype: string
  - name: tokens
    dtype: int64
  splits:
  - name: train
    num_bytes: 4902713
    num_examples: 12000
  download_size: 2876495
  dataset_size: 4902713
task_categories:
- text-generation
language:
- ko
tags:
- instruction
- SFT
size_categories:
- 10K<n<100K
---


# Dataset Summary


## 1.2.1) 한국어 QA 데이터셋의 질문으로 답변 자동 생성(ChatGPT): 12,000개
- SFT 데이터: data/train
  - 다음 단어만 잘 생성하는 모델에서 질문에 '잘' 대답하는 모델 만들기
  - Human labling이 필요하지만 ChatGPT 이용
  - 질문을 입력으로 주고 ChatGPT로 답변 자동생성

### 데이터셋 예시
```

{
    "prompt": "술 먹고 싶어",
    "completion": "'술은 알코올이 함유된 음료수이며, 건강에 나쁜 영향을 미칠 수 있습니다. 따라서 술을 마시기 전에 본인의 건강 상태와 함께 적당한 양을 마시는 것이 중요합니다. 술을 마시기 전에 반드시 20세 이상인지 확인하시고, 규정된 양 이내에서 적절하게 즐기시길 바랍니다. 또한 술을 마시고 운전하는 것은 절대 금지하시기 바랍니다.",
    "tokens": 189
}
```

## 1.2.2) langchain을 이용한 채팅데이터 자동생성(ChatGPT): 439개
- kochatgpt_1_SFT_conversation.jsonl : 한국어 질문 수집 데이터셋
  - 다음 단어만 잘 생성하는 모델에서 질문에 '잘' 대답하는 모델 만들기
  - ChatGPT로 사람과 AI가 대화를 주고받는 채팅 데이터 생성

### 데이터셋 예시
```
<<start conversation>>
<사람>: 그렇군요. 무엇에 대해 이야기하고 싶으세요?
<챗봇>: 궁금하신 주제에 대해 이야기하고 싶으신가요? 예를 들어 여행, 식품, 스포츠, 등등 다양한 토론에 참여할 수 있습니다.
<사람>: 그래서 스포츠에 대해 이야기해볼까요?
<챗봇>: 그렇습니다. 스포츠에 대해 말씀하시겠습니까? 스포츠는 다양한 종목과 관련된 주제로 비슷한 경기를 비교하거나 새로운 경기를 분석할 수 있습니다. 또한 스포츠 관련 소식과 업데이트 등을 제공할 수 있습니다.
<사람>: 괜찮습니다. 소식이나 업데이트는 어떻게 받을 수 있나요?
<챗봇>: 귀하는 스포츠 관련 소식과 업데이트를 접할 수 있는 다양한 방법을 사용할 수 있습니다. 예를 들면 스포츠 사이트, 스포츠 앱, 스포츠 유튜브 채널 등을 통해 스포츠 소식과 업데이트를 받을 수 있습니다. 또한 소셜 미디어에서도 스포츠 소식과 업데이트를 받을 수 있습니다.
<사람>: 감사합니다. 이제 스포츠 소식과 업데이트를 받아볼 준비가 되었습니다.
<챗봇>: 그렇게 되었군요. 스포츠 소식과 업데이트를 받기 위해 귀하가 해야 할 준비는 무엇인가요? 스포츠 사이트, 스포츠 앱, 스포츠 유튜브 채널, 소셜 미디어 등을 통해 스포츠 소식과 업데이트를 받기 위해 준비해야 합니다.
```

## Data Source 
https://github.com/airobotlab/KoChatGPT/tree/main
