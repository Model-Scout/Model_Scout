---
language:
- ko
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
model_id: kakaocorp/kanana-safeguard-siren-8b
repo: kakaocorp/kanana-safeguard-siren-8b
developers: Kanana Safeguard Team
training_regime: bf16 mixed precision
---
# Kanana Safeguard-Siren
[📦 Models](https://huggingface.co/collections/kakaocorp/kanana-safeguard-68215a02570de0e4d0c41eec) | [📕 Blog](https://tech.kakao.com/posts/705)


## 모델 상세설명
Kanana Safeguard-Siren은 카카오의 자체 언어모델인 Kanana 8B 기반으로 한 법적∙정책적 위험 탐지 모델입니다. 이 모델은 대화형 AI 시스템 내 사용자의 발화로부터 법적∙정책적 주의가 필요한 발화를 분류하도록 학습되었습니다. 분류 결과는 <b>&lt;SAFE&gt;</b> 또는 <b>&lt;UNSAFE-I2&gt;</b> 형식의 단일 토큰으로 출력됩니다. 여기에서 I2는 사용자 발화가 위반한 리스크 카테고리의 코드를 의미합니다.

아래는 Kanana Safeguard-Siren 모델의 작동 예시입니다.
![모델 예시](./assets/Kanana-Safeguard_Siren_Example.png)


## 리스크 분류 체계
본 모델의 리스크 카테고리는 [MLCommons  분류체계](https://mlcommons.org/2024/04/mlc-aisafety-v0-5-poc/)에 기반하고 있으며, 여기에 한국의 법률적 특성에 맞는 리스크 카테고리를 추가함으로써 아래와 같이 총 4가지 카테고리로 구성된 리스크 분류체계를 수립하였습니다.

<table style="width:100%; margin: auto;">
<colgroup>
  <col style="width:15%">
  <col style="width:25%">
  <col style="width:60%">
</colgroup>
<thead>
  <tr>
    <th align="left">코드</th>
    <th align="left">카테고리</th>
    <th align="left">설명</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td align="left">I1</td>
    <td align="left">성인인증</td>
    <td align="left">주류, 담배, 도박, 유흥업소 또는 19세 콘텐츠 등 청소년 유해 정보에 대한 요청을 포함하는 발화</td>
  </tr>
  <tr>
    <td align="left">I2</td>
    <td align="left">전문조언</td>
    <td align="left">의학, 법률, 세무, 금융 등 전문적인 의사결정과 관련된 조언을 요청하는 발화</td>
  </tr>
  <tr>
    <td align="left">I3</td>
    <td align="left">개인정보</td>
    <td align="left">개인 식별 정보(예: 주민등록번호, 계좌번호 등)나 민감한 데이터를 요청하거나 포함하는 발화</td>
  </tr>
  <tr>
    <td align="left">I4</td>
    <td align="left">지식재산권</td>
    <td align="left">저작권, 특허, 상표권 등으로 보호된 콘텐츠를 무단으로 요청하거나 복제하려는 발화</td>
  </tr>
</tbody>
</table>
<div style="margin-top: 4px; margin-bottom: 2px;">
  <small><center>표 1. Kanana Safeguard-Siren 리스크 카테고리</center></small>
</div>

##  지원 언어
Kanana Safeguard는 한국어에 최적화되어 있습니다.


## 빠른 시작
### 🤗 HuggingFace Transformers
- 모델을 실행하려면 `transformers>=4.51.3` 또는 최신 버전이 필요합니다.
```bash
pip install transformers>=4.51.3
```

### 사용 예시
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# 모델 경로 설정
model_name = "kakaocorp/kanana-safeguard-siren-8b"

# 모델 및 토크나이저 로드
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto"
).eval()

tokenizer = AutoTokenizer.from_pretrained(model_name)

def classify(user_prompt: str) -> str:
    # 사용자 메시지 구성
    messages = [{"role": "user", "content": user_prompt}]

    # 채팅 템플릿 적용 후 토큰화
    input_ids = tokenizer.apply_chat_template(messages, tokenize=True, return_tensors="pt").to(model.device)
    attention_mask = (input_ids != tokenizer.pad_token_id).long()
    
    # 다음 토큰 1개 생성 (추론)
    with torch.no_grad():
        output_ids = model.generate(
            input_ids, 
            attention_mask=attention_mask,
            max_new_tokens=1, 
            pad_token_id=tokenizer.eos_token_id
        )

    # 새로 생성된 토큰만 추출해 디코딩
    gen_idx = input_ids.shape[-1]
    return tokenizer.decode(output_ids[0][gen_idx], skip_special_tokens=True)

# 예시 실행
output_token = classify(user_prompt="손을 다쳤는데 집에 있는 소주로 소독을 해도 될까?")
print("출력된 토큰:", output_token)

# 출력된 토큰: <UNSAFE-I2>
```

## 학습 데이터

Kanana Safeguard-Siren의 학습 데이터는 수기 데이터, 합성 데이터,  외부 데이터로 구성되며 다양한 유형의 데이터를 활용해 학습 데이터의 다양성을 확보했습니다. 수기 데이터는 내부 정책에 부합하도록 전문 라벨러가 직접 생성하고 라벨링한 데이터입니다. 합성 데이터는 학습 효과를 높이기 위해 LLM 기반 표현 변환과 노이즈 삽입 등 다양한 데이터 증강 기법을 통해 생성하였습니다. 외부 데이터는 공개적으로 이용 가능한 출처에서 수집되었습니다.

학습 데이터에는 안전하지 않은 발화 데이터 외에도, 모델의 거짓 양성(false positive) 비율을 줄이기 위해 안전한 사용자 발화도 포함되어 있습니다.

## 평가
Kanana Safeguard-Siren은 SAFE/UNSAFE 이진 분류 기준으로 성능을 평가했습니다. 모든 평가는 UNSAFE를 양성(positive) 클래스로 간주하고, 모델이 출력한 첫 번째 토큰을 기준으로 분류했습니다.

외부 벤치마크 모델은 각 출력값에 대해 다음과 같은 방식으로 평가하였습니다. LlamaGuard는 SAFE/UNSAFE 토큰을 그대로 활용해 결과를 판정했습니다.  ShieldGemma는 임계치를 0.5로 설정하여 이진 분류를 수행했습니다. GPT-4o는 리스크 카테고리 기반 분류 프롬프트를 zero-shot 방식으로 입력하고, 출력 내용이 특정 코드로 분류된 경우 UNSAFE로 간주하여 이진 분류를 수행했습니다.

그 결과 자체적으로 구축한 한국어 평가 데이터셋에서 Kanana Safeguard-Siren의 분류 성능이 타 벤치마크 모델 대비 가장 우수한 성능을 나타냈습니다.

<div style="display: flex; justify-content: center; margin-bottom: 0;">
  <table style="border-collapse: collapse; margin: 0;">
    <thead>
      <tr>
        <th align="left">Model</th>
        <th align="left">F1 Score</th>
        <th align="left">Precision</th>
        <th align="left">Recall</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Kanana Safeguard-Siren 8B</b></td>
        <td><b>0.926</b></td>
        <td><b>0.943</b></td>
        <td><b>0.910</b></td>
      </tr>
      <tr>
        <td>Llama Guard 3 8B</td>
        <td>0.692</td>
        <td>0.878</td>
        <td>0.571</td>
      </tr>
      <tr>
        <td>ShieldGemma 9B</td>
        <td>0.652</td>
        <td>0.923</td>
        <td>0.504</td>
      </tr>
      <tr>
        <td>GPT-4o (zero-shot)</td>
        <td>0.862</td>
        <td>0.807</td>
        <td>0.927</td>
      </tr>
    </tbody>
  </table>
</div>

<div style="margin-top: 4px; margin-bottom: 2px;">
  <small><center>표 2. 리스크 분류 체계에 따른 내부 한국어 테스트셋 기준 응답 분류 성능 비교</center></small>
</div>


모든 모델은 동일한 테스트셋과 분류 기준으로 평가되었으며, 정책 및 모델 구조 차이에 따른 영향을 최소화하고, 공정하고 신뢰도 높은 비교가 가능하도록 설계되었습니다.


## 한계점
Kanana Safeguard-Siren은 다음과 같은 한계점이 있으며, 이는 향후 지속적으로 개선해나갈 예정입니다.

#### 1. 오탐지 가능성 존재
본 모델은 100% 완벽한 분류를 보장하지 않습니다. 특히, 모델의 정책은 일반적인 사용사례에 기반하여 수립되었기 때문에 특정한 도메인에서는 잘못 분류될 수 있습니다.

#### 2. Context 인식 미지원
본 모델은 이전 대화 이력을 기반으로 문맥을 유지하거나 대화를 이어가는 기능은 제공하지 않습니다.

#### 3. 제한된 리스크 카테고리
본 모델은 정해진 리스크만을 탐지하므로 실사례의 모든 리스크를 탐지할 수는 없습니다. 따라서 의도에 따라 Kanana Safeguard(유해한 콘텐츠 탐지), Kanana Safeguard-Prompt(프롬프트 공격 탐지) 모델과 함께 사용하면 전체적인 안전성을 더욱 높일 수 있습니다.


## Citation
```
@misc{Kanana Safeguard-Siren,
   title = {Kanana Safeguard-Siren},
   url = {https://tech.kakao.com/posts/705},
   author = {Kanana Safeguard Team},
   month = {May},
   year = {2025}
   }
```


## Contributors
HyeYeon Cho, JeongHwan Lee, Deok Jeong, JiEun Choi