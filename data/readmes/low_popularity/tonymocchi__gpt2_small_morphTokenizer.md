---
language:
- ko
base_model:
- openai-community/gpt2
tags:
- text-generation
- pytorch
---

# GPT-2 Small for Korean Elementary School (1st Grade)

미래앤 초등학교 국정교과서 1학년 과정에 수록된 2,400 문장으로 파인튜닝(Fine-tuning)한 모델입니다.

### 모델 정보
- **Base Model:** GPT-2 (Original)
- **Dataset:** 초등학교 1학년 국정교과서 (미래앤) 문장 2,400개
- **Tokenizer:** GPT-2 기본 토크나이저 (Vanilla)

### 사용 예시 (Usage)
- 토큰파일.txt는 토큰파일.zip을 풀면 있습니다
  
```python
from transformers import AutoTokenizer, AutoModelForCausalLM

repo_id = "tonymocchi/gpt2_small_morphTokenizer"

# 1. 토크나이저 및 모델 로드
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForCausalLM.from_pretrained(repo_id)

# 2. 입력 텍스트 처리
input_text = "선생님과 함께"
inputs = tokenizer(input_text, return_tensors="pt")

# 3. 텍스트 생성
outputs = model.generate(
    **inputs,
    max_length=50,       # 최대 생성 길이
    do_sample=True,      # 확률적 샘플링 (다양한 문장 생성)
    temperature=0.7,     # 창의성 조절 (1.0에 가까울수록 창의적)
    top_k=50             # 상위 50개 확률 단어 중에서 선택
)

# 4. 결과 출력
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)