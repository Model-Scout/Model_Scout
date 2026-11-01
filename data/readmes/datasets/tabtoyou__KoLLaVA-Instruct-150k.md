---
license: cc-by-nc-4.0
task_categories:
- visual-question-answering
- question-answering
language:
- ko
pretty_name: Korean Visual Instruct
---


# Korean Visual Instruct 150K Dataset Card

🌋[LLaVA](https://llava-vl.github.io/)의 Instruction-following Dataset을 한국어로 번역한 데이터셋입니다. (feat. DeepL)


### 1. Conversation
 - 이미지에 대해 질문하는 사람과 이에 답하는 Assistant 사이의 대화 형식으로 디자인합니다. 대답은 Assistant가 이미지를 보고 질문에 대답하는 것과 같은 어조이며, 이미지의 시각적인 정보(객체의 유형, 수, 행동, 위치, 객체간의 상대적인 위치 등)에 대해 다양한 질문을 합니다. 또한 명확하게 답변이 있는 질문만 고려합니다.

### 2. Detailed description
 - 이미지에 대한 풍부하고 포괄적인 설명을 내포하게 디자인 했습니다. 이러한 자세한 설명을 요구하는 여러 promt 리스트를 만든 뒤 그중 하나를 샘플해 답을 생성합니다.

### 3. Complex reasoning
 - 위의 두 가지 유형은 시각적 content 자체에 중점을 두는데요. Complex reasoning에서는 이를 기반으로 심층 추론 질문을 추가로 생성합니다. 답변은 타당한 논리를 갖춘 단계별 추론 프로세스를 요구합니다.


## Done
- Detail_23k
- Conversation_58k
- Complex_resoning_77k
- ko_llava_instruct_150k

## Project Repo
- Github Repo : [tabtoyou/KoLLaVA](https://github.com/tabtoyou/KoLLaVA)

### License
- Attribution-NonCommercial 4.0 International | OpenAI [policy](https://openai.com/policies/terms-of-use) 준수