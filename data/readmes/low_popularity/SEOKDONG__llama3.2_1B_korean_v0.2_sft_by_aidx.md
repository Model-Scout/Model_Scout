---
library_name: transformers
tags:
- korean
- 1B
- ko
license: apache-2.0
language:
- ko
metrics:
- accuracy
base_model:
- meta-llama/Llama-3.2-1B
pipeline_tag: text-generation
---
### ⛱   해당 모델은은 LlaMA3.2 1B를 Foundation 모델로 하는 한국어 및 한국의 다양한 
### 문화에 적용할 수 있도록 하기 위해
### 개발 되었으며 자체 제작한 53개 영역의 한국어 데이터를 활용하여 한국 사회 가치와 
### 문화를 이해하는 모델 입니다. Thanks for ktds✌

### V0.2 Epoch=2
                

# ❶ 모델 설명
- 모델명 및 주요기능:
  해당 모델은은 LlaMA3.2 1B 모델을 기반으로 SFT 방식으로 파인튜닝된 모델입니다.
  한국어와 한국의 다양한 문화적 맥락을 이해하도록 설계되었으며 ✨✨, 자체 제작한 53개 영역의 한국어
  데이터를 활용해 한국 사회의 가치와 문화를 반영합니다.
  주요 기능으로는 텍스트 생성, 대화 추론, 문서 요약, 질의응답, 감정 분석 및 자연어 처리 관련 다양한 작업을 지원하며,
  활용 분야는 법률, 재무, 과학, 교육, 비즈니스, 문화 연구 등 다양한 분야에서 응용될 수 있습니다.
- 모델 아키텍처:
  해당 모델은 LlaMA3.2 1B 모델을 기반으로, 파라미터 수는 10억 개(1B)로 구성된 고성능 언어 모델입니다.
  이 모델은LlaMA3.2 1B를 파운데이션 모델로 삼아, SFT(지도 미세 조정) 방식을 통해 한국어와 한국 문화에 특화된 성능을 발휘하도록 훈련되었습니다.
  LlaMA3.2 1B의 경량화된 구조는 빠른 추론 속도와 메모리 효율성을 보장하며, 다양한 자연어 처리 작업에 적합하게 최적화되어 있습니다.
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

base_model = "SEOKDONG/llama3.2_1B_korean_v0.2_sft_by_aidx"
    
model = AutoModelForCausalLM.from_pretrained(base_LLM_model)
tokenizer = AutoTokenizer.from_pretrained(base_LLM_model)

from tqdm import tqdm
for i in tqdm(range(0,1)): #len(answer_list))):
    input_text =  """
    당신은 AI 비서입니다. 다음 질문에 맞는 답변을 고르세요. 답변은 1,2,3,4 중에 하나만 선택하세요. 
    다음 중 탄수화물의 일종으로, 포도당의 이중 결합으로 구성되어 있으며 자주 사용되는 설탕의 성분은 무엇인가? 
    선택지: 1. 셀룰로오스 2. 자당 3. 녹말 4. 글리코겐 답변:"""
    
    inputs = tokenizer(input_text, return_tensors="pt")
    inputs = inputs.to("cuda:0")
    # 3. 모델을 사용한 추론
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=1024,temperature=0.1, do_sample=True, repetition_penalty=1.10)
    # 4. 결과 디코딩
    result = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(result.split("답변:")[1].strip())

    결과: '2. 자당입니다. 자당은 포도당이 두 개의 이중 결합으로 이루어진 형태로 존재하며, 주로 설탕의 주요 성분으로 사용됩니다. 
        셀룰로오스는 단백질, 녹말은 식물성 단백질, 글리코겐은 지방과 관련된 단백질로, 모두 설탕의 성분이 아닙니다. 따라서 정답은 2입니다.'
</code></pre>