---
datasets:
- AIDX-ktds/ko_leaderboard
base_model: meta-llama/Llama-3.1-8B-Instruct
base_model_relation: finetune
pipeline_tag: text-generation
language:
- ko
license: apache-2.0
metrics:
- accuracy
tags:
- ko_leaderboard
- upstage/open-ko-llm-leaderboard
- open-ko-llm-leaderboard
---
### ⛱   해당 모델은은 LlaMA3.1을 Foundation 모델로 하는 한국어 및 한국의 다양한 
### 문화에 적용할 수 있도록 하기 위해
### 개발 되었으며 자체 제작한 53개 영역의 한국어 데이터를 활용하여 한국 사회 가치와 
### 문화를 이해하는 모델 입니다. Thanks for ktds✌

### V1.4 학습데이터 추가: 280K, Epoch=3
                

# ❶ 모델 설명
- 모델명 및 주요기능:
  해당 모델은은 LlaMA3.1 모델을 기반으로 SFT 방식으로 파인튜닝된 모델입니다.
  한국어와 한국의 다양한 문화적 맥락을 이해하도록 설계되었으며 ✨✨, 자체 제작한 53개 영역의 한국어
  데이터를 활용해 한국 사회의 가치와 문화를 반영합니다.
  주요 기능으로는 텍스트 생성, 대화 추론, 문서 요약, 질의응답, 감정 분석 및 자연어 처리 관련 다양한 작업을 지원하며,
  활용 분야는 법률, 재무, 과학, 교육, 비즈니스, 문화 연구 등 다양한 분야에서 응용될 수 있습니다.
- 모델 아키텍처:
  해당 모델은 LlaMA3.1 8B 모델을 기반으로, 파라미터 수는 80억 개(8B)로 구성된 고성능 언어 모델입니다.
  이 모델은LlaMA3.1 8B를 파운데이션 모델로 삼아, SFT(지도 미세 조정) 방식을 통해 한국어와 한국 문화에 특화된 성능을 발휘하도록 훈련되었습니다.
  LlaMA3.1 8B의 경량화된 구조는 빠른 추론 속도와 메모리 효율성을 보장하며, 다양한 자연어 처리 작업에 적합하게 최적화되어 있습니다.
  이 아키텍처는 텍스트 생성, 질의응답, 문서 요약, 감정 분석과 같은 다양한 작업에서 탁월한 성능을 보여줍니다.

# ❷ 학습 데이터
- 해당 모델은은 자체 개발한 총 3.6GB 크기의 데이터를 바탕으로 학습되었습니다. 모두 233만 건의 QnA, 요약, 분류 등 데이터를 포함하며,
  그 중 133만 건은 53개 영역의 객관식 문제로 구성되었습니다. 이 영역에는 한국사, 사회, 재무, 법률, 세무, 수학, 생물, 물리, 화학 등이 포함되며,
  Chain of Thought 방식으로 학습되었습니다. 또한 130만 건의 주관식 문제는 한국사, 재무, 법률, 세무, 수학 등 38개 영역에 걸쳐 학습되었습니다.
  학습 데이터 중 한국의 사회 가치와 인간의 감정을 이해하고 지시한 사항에 따라 출력할 수 있는 데이터를 학습하였습니다.
- 학습 Instruction Datasets Format: 
  <pre><code>{"prompt": "prompt text", "completion": "ideal generated text"}</code></pre>
    
# ❸ 사용 사례
  해당 모델은 다양한 응용 분야에서 사용될 수 있습니다. 예를 들어:
- 교육 분야: 역사, 수학, 과학 등 다양한 학습 자료에 대한 질의응답 및 설명 생성.
- 비즈니스: 법률, 재무, 세무 관련 질의에 대한 답변 제공 및 문서 요약.
- 연구 및 문화: 한국 사회와 문화에 맞춘 자연어 처리 작업, 감정 분석, 문서 생성 및 번역.
- 고객 서비스: 사용자와의 대화 생성 및 맞춤형 응답 제공.
- 이 모델은 다양한 자연어 처리 작업에서 높은 활용도를 가집니다.

# ❹ 한계 ⛈⛈
- 해당 모델은 한국어와 한국 문화에 특화되어 있으나, 
  특정 영역(예: 최신 국제 자료, 전문 분야)의 데이터 부족으로 인해 다른 언어 또는
  문화에 대한 응답의 정확성이 떨어질 수 있습니다.
  또한, 복잡한 논리적 사고를 요구하는 문제에 대해 제한된 추론 능력을 보일 수 있으며,
  편향된 데이터가 포함될 경우 편향된 응답이 생성될 가능성도 존재합니다.

# ❺ 사용 방법
  <pre><code>
  from transformers import AutoModel, AutoTokenizer
  
  tokenizer = AutoTokenizer.from_pretrained("SEOKDONG/llama3.0_korean_v1.0_sft")
  model = AutoModel.from_pretrained("SEOKDONG/llama3.0_korean_v1.0_sft")

    input_text =  """ 「국민건강보험법」제44조, 「국민건강보험법 시행령」제19조,「약관의 규제에 관한 법률」제5조, 「상법」제54조 참조 판단 해줘""" + " 답변:"
    inputs = tokenizer(input_text, return_tensors="pt")
  with torch.no_grad():
        outputs = model.generate(**inputs, max_length=1024,  temperature=0.5, do_sample=True, repetition_penalty=1.15)
   
  result = tokenizer.decode(outputs[0], skip_special_tokens=True)
  print(result)
</code></pre>

Llama 3.1 is licensed under the Llama 3.1 Community License,
Copyright © Meta Platforms, Inc. All Rights Reserved.