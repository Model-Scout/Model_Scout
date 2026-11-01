---
language: ko
tags:
- causal-lm
- etm
license: mit
datasets:
- beomi/kowikitext-qa-ref-detail-preview
- HAERAE-HUB/KOREAN-WEBTEXT
inference:
  parameters:
    temperature: 0.7
    top_k: 64
    top_p: 0.9
    repetition_penalty: 1.1
    max_new_tokens: 40
inference_providers:
- cpu
- gpu
- t4
- a10g
library_name: transformers
widget:
  - text: "안녕"
---
# ETM-Korean
소형 텍스트 디코더 LM  
- 200 MB causal LM trained on Korean web text.
- 학습 데이터: beomi/kowikitext-qa-ref-detail-preview, HAERAE-HUB/KOREAN-WEBTEXT 일부  
- HAERAE-HUB/KOREAN-WEBTEXT 데이터셋 기준: train_ce 4.934 | val_ce 4.835 | val_ppl 125.79 | d1 1.000 | d2 1.000 | rep 0.000 | char_ppl 26.78

## Example
```python
# %% ETM Inference
import torch
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("EleutherAI/polyglot-ko-1.3b")

# 1️⃣ 모델 로드
repo_id = "idah4/etm-korean-tiny"
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = AutoModelForCausalLM.from_pretrained(
    repo_id,
    trust_remote_code=True
).to(device).eval()

def encode(text):
    return torch.tensor(
        tokenizer(text)["input_ids"],
        dtype=torch.long
    ).unsqueeze(0).to(device)

def decode(ids):
    return tokenizer.decode(ids.tolist(), skip_special_tokens=True)

# 3️⃣ 텍스트 생성 함수
@torch.no_grad()
def generate_text(prompt: str, 
    temperature=0.8,
    top_k=40,
    top_p=0.95,
    repetition_penalty=2.0,
    max_new_tokens=100,):

    input_ids = encode(prompt)
    out = model.generate(
        input_ids,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        top_k=top_k
    )
    text_out = decode(out[0])
    return text_out

# 4️⃣ 시연
# 4️⃣ 시연
prompt = "나: 나는 사람이야. 너는 정체가 뭐니?\n너:"
result = generate_text(
    prompt,
    max_new_tokens=40,
    temperature=0.7,
    top_k=32,
    top_p=0.9,
    repetition_penalty=1.1
)


print("📝 Prompt:", prompt)
print("💬 Generated:\n", result)


📝 Prompt: 나: 나는 사람이야. 너는 정체가 뭐니?
너:
💬 Generated:
 나: 나는 사람이야. 너는 정체가 뭐니?
너:
이런 말� 들은 일은 없다. 그들이 원하는 일, 즉 그렇게 당신의 삶에 대한 질문이 있었어요
“내 마음은 좋고, 그래서 좋겠