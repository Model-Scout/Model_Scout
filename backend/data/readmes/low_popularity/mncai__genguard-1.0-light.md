---
license: apache-2.0
base_model: google/gemma-4-E4B-it
language:
- ko
- en
library_name: transformers
pipeline_tag: text-generation
tags:
- guardrail
- safety
- content-moderation
- policy-following
- korean
---

# GenGuard 1.0 Light

![GenGuard AI 안전 가드레일 소개](https://cdn-uploads.huggingface.co/production/uploads/66050bb08d482f8346763d2c/0OnTXSetzMFaO7e81XrD4.png)

GenGuard 1.0 Light는 유해성 탐지, Custom Policy, 공격 탐지를 **하나의 모델**로 처리하는 가드레일 모델입니다.

- **Custom Policy 지원**: `policy` 인자에 정책을 넣으면 재학습 없이 그 정책을 기준으로 판정합니다.
- **유해성 탐지**: 사용자 입력과 모델 응답을 모두 판정하고, 해당하는 유해 범주(S1~S23)도 함께 출력할 수 있습니다.
- **다양한 공격 유형 탐지**: 탈옥·프롬프트 주입을 포함한 여러 유형의 공격을 탐지합니다.

## 성능

<img src="https://huggingface.co/mncai/genguard-1.0-light/resolve/main/figs/perf_bars.png" alt="묶음별 성능 비교" width="900">

| 모델 | Korean Safety | English Safety | Attack Detection | Custom Policy | Long Context | Average |
|---|---:|---:|---:|---:|---:|---:|
| **GenGuard 1.0 Light** | **87.3** | 79.9 | **93.7** | 72.5 | **88.3** | **84.3** |
| gpt-oss-safeguard-20b | 85.7 | 76.7 | 78.0 | **72.7** | 82.6 | 79.1 |
| Qwen3Guard-Gen-8B | 82.8 | 78.0 | 91.8 | 31.6 | 83.6 | 73.6 |
| Shieldstral-1.0-3B | 85.5 | **80.3** | 87.5 | 39.6 | 69.1 | 72.4 |
| Nemotron-3.5-Content-Safety | 81.5 | 76.7 | 81.7 | 51.6 | 64.2 | 71.1 |
| Kanana-Safeguard-8B* | 78.8 | 74.9 | 70.7 | 26.3 | — | 62.7 |

- \* 표시 모델은 입력 길이 제한으로 Long Context를 측정할 수 없어, Long Context를 뺀 네 묶음으로 Average를 냈습니다. 나머지 모델의 Average는 다섯 묶음 전체의 평균입니다.
- Nemotron-3.5-Content-Safety는 추론을 끈 모드로 평가했으며, 속도 측정도 같은 설정입니다.

### 벤치별 점수

**Korean Safety (F1)**

| 벤치 | **GenGuard 1.0 Light** | gpt-oss-safeguard-20b | Nemotron-3.5-Content-Safety | Qwen3Guard-Gen-8B | Shieldstral-1.0-3B | Kanana-Safeguard-8B |
|---|---:|---:|---:|---:|---:|---:|
| RTP-LX (subset ko) | **94.3** | 92.0 | 90.2 | 83.8 | 88.2 | 90.2 |
| wildguardmix-test-ko | **85.4** | 84.2 | 79.6 | 84.8 | **85.4** | 73.6 |
| XSTest_ko | 82.4 | 80.8 | 74.6 | 79.9 | **82.9** | 72.8 |

**English Safety (F1)**

| 벤치 | **GenGuard 1.0 Light** | gpt-oss-safeguard-20b | Nemotron-3.5-Content-Safety | Qwen3Guard-Gen-8B | Shieldstral-1.0-3B | Kanana-Safeguard-8B |
|---|---:|---:|---:|---:|---:|---:|
| OpenAI Moderation | 81.6 | **82.2** | 75.3 | 68.4 | 78.7 | 72.0 |
| ToxicChat | 76.6 | 66.5 | 72.5 | 68.3 | **77.6** | 66.9 |
| BeaverTails | 84.2 | 79.6 | 83.0 | **86.5** | 85.7 | 82.8 |
| PKU-SafeRLHF | 63.2 | 60.5 | 61.6 | **70.9** | 66.7 | 67.5 |
| WildGuardTest | **87.1** | 85.0 | 82.8 | 86.7 | 86.8 | 78.5 |
| HarmBench | 86.9 | 86.7 | 84.8 | **87.1** | 86.6 | 82.0 |

**Attack Detection (차단율)**

| 벤치 | **GenGuard 1.0 Light** | gpt-oss-safeguard-20b | Nemotron-3.5-Content-Safety | Qwen3Guard-Gen-8B | Shieldstral-1.0-3B | Kanana-Safeguard-8B |
|---|---:|---:|---:|---:|---:|---:|
| WildJailbreak (eval) | **96.7** | 88.0 | 77.3 | 95.1 | 94.9 | 83.0 |
| wildjailbreak-eval-ko | 93.5 | 83.2 | 81.8 | **93.6** | 91.2 | 62.2 |
| MultiJail (subset ko) | 91.4 | 74.3 | 92.4 | **93.7** | 88.9 | 92.4 |
| BIPIA | **67.1** | 3.5◇ | 18.6 | 20.7◇ | 4.1◇ | 9.1◇ |
| Private Red-Team Bench | **92.9** | 66.5 | 75.4 | 85.0 | 75.2 | 45.1 |

- ◇ 모델 카드에 프롬프트 주입 탐지 기능이 명시되지 않은 모델입니다.
- BIPIA(문서 속 간접 프롬프트 주입)는 비교 모델 대부분이 주입 탐지를 지원하지 않아(◇) 참고용으로만 싣고 평균 계산에서는 제외했습니다.
- Private Red-Team Bench는 한국어 중심(영어·일본어 일부 포함)의 내부 레드팀 평가 세트로, 평가 오염을 막기 위해 문항은 공개하지 않습니다.

**Custom Policy (F1)**

| 벤치 | **GenGuard 1.0 Light** | gpt-oss-safeguard-20b | Nemotron-3.5-Content-Safety | Qwen3Guard-Gen-8B | Shieldstral-1.0-3B | Kanana-Safeguard-8B |
|---|---:|---:|---:|---:|---:|---:|
| KSPG-Bench | 80.1 | **81.3** | 42.3 | 6.2‡ | 18.1 | 9.2‡ |
| CoSApien-ko | **89.3** | 86.4 | 81.4 | 77.5‡ | 78.7 | 67.0‡ |
| PoFBench | 62.4 | **68.0** | 48.6 | 27.2‡ | 27.3 | 23.7‡ |
| BARRED | **58.1** | 55.2 | 34.1 | 15.3‡ | 34.2 | 5.4‡ |

- ‡ 정책을 입력받지 못하는 모델로, 자체 유해성 분류로 판정했습니다.
- [KSPG-Bench](https://huggingface.co/datasets/mncai/KSPG-Bench)(Korean Service Policy Guard Bench)는 GenON이 개발해 공개한 벤치로, 같은 요청도 서비스 정책에 따라 허용·차단이 달라져야 하는 상황에서 가드레일이 정책대로 판정하는지 평가합니다. 업무 범위, 규제 경계, 응답 신뢰 세 영역의 질문 판정과 응답 판정으로 구성됩니다.

**Long Context (F1)**

| 벤치 | **GenGuard 1.0 Light** | gpt-oss-safeguard-20b | Nemotron-3.5-Content-Safety | Qwen3Guard-Gen-8B | Shieldstral-1.0-3B | Kanana-Safeguard-8B |
|---|---:|---:|---:|---:|---:|---:|
| SafetyNIAH | **88.3** | 82.6 | 64.2 | 83.6 | 69.1 | — |

- SafetyNIAH는 긴 정상 문서 속에 숨겨진 유해 문장을 찾아내는 벤치입니다. Kanana-Safeguard-8B(최대 입력 8,192 토큰)는 입력 길이 제한으로 측정이 불가합니다(—).


## 속도

| 모델 | 한 건 응답 시간 중앙값(ms) | 초당 처리 건수, 32건 동시 |
|---|---:|---:|
| **GenGuard 1.0 Light** | 40 | 59 |
| gpt-oss-safeguard-20b | 587 | 6.5 |
| Qwen3Guard-Gen-8B | 71 | 37 |
| Nemotron-3.5-Content-Safety | 72 | 61 |
| Shieldstral-1.0-3B | 14 | 141 |
| Kanana-Safeguard-8B | 20 | 68 |

- wildguardmix-test-ko 3,375건으로 측정했습니다.
- 장비는 NVIDIA B200을 MIG로 나눈 2g.45gb 한 칸(B200의 약 1/4)이며, vLLM 0.30·bf16을 썼습니다.
- 응답 시간은 1,000건 표본을 한 건씩 보내 잰 중앙값이고, 초당 처리 건수는 3,375건 전체를 32건씩 동시에 보내 쟀습니다.

## 모델 정보

| 항목 | 내용 |
|---|---|
| 베이스 모델 | `google/gemma-4-E4B-it` |
| 파라미터 | 8B |
| 지원 언어 | 한국어, 영어 |
| 최대 입력 길이 | 131,072 토큰 |

## 사용법

### 1. 입력 구성

`user` 메시지는 사용자 입력으로, `assistant` 메시지는 모델 응답으로 판정합니다. 문서나 검색 결과 등 대화 형식이 아닌 텍스트는 단일 `user` 메시지로 입력합니다. 지원하는 메시지 역할은 `user`와 `assistant`입니다.

### 2. 출력과 판정

```
Decision: block            ← 항상 출력 (block 또는 allow)
Response Refusal: refusal  ← (옵션) request_refusal="/refusal" 일 때만
Safety Categories: S3, S9  ← (옵션) request_categories="/categories" 일 때만
```

<details>
<summary>유해 범주 번호표 (S1~S23)</summary>

| 번호 | 범주 | 번호 | 범주 |
|---|---|---|---|
| S1 | Controlled/Regulated Substances | S13 | Needs Caution |
| S2 | Copyright/Trademark/Plagiarism | S14 | Other |
| S3 | Criminal Planning/Confessions | S15 | PII/Privacy |
| S4 | Fraud/Deception | S16 | Political/Misinformation/Conspiracy |
| S5 | Guns and Illegal Weapons | S17 | Profanity |
| S6 | Harassment | S18 | Sexual |
| S7 | Hate/Identity Hate | S19 | Sexual (minor) |
| S8 | High Risk Gov Decision Making | S20 | Suicide and Self Harm |
| S9 | Illegal Activity | S21 | Threat |
| S10 | Immoral/Unethical | S22 | Unauthorized Advice |
| S11 | Malware | S23 | Violence |
| S12 | Manipulation |  |  |

</details>

판정은 생성된 텍스트 대신 확률로 내는 것을 권장합니다. 프롬프트 뒤에 `Decision:`을 붙이고 다음 토큰의 ` allow` · ` block` 확률만 보아, **차단 확률 = P(block) / (P(allow) + P(block)) ≥ 0.5 이면 차단**합니다. 기준값은 서비스에 맞게 조절할 수 있습니다.

### 3. 권장 환경

- **vLLM 0.30.0** (torch 2.13, transformers 5.18, flashinfer 0.6.18)을 권장합니다.
- transformers로 직접 추론할 때는 5.8.1 이상을 쓰세요.
- 항상 `temperature=0`(transformers는 `do_sample=False`)으로 생성하세요. 설정 파일의 기본값이 샘플링이라 지정하지 않으면 판정이 흔들릴 수 있습니다.

### 4. 코드 예시

<details>
<summary>vLLM</summary>

```python
import math
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams, TokensPrompt

MODEL = "mncai/genguard-1.0-light"
DECISION, ALLOW, BLOCK = [87732, 236787], 2174, 3355   # "Decision:", " allow", " block" 토큰 id

tok = AutoTokenizer.from_pretrained(MODEL)
llm = LLM(MODEL, dtype="bfloat16", max_model_len=8192)
# allow · block 두 토큰만 받아야 확률이 정확합니다
params = SamplingParams(temperature=0, max_tokens=1, logprobs=2, allowed_token_ids=[ALLOW, BLOCK])

def prompt(messages, **kw):
    ids = tok.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_dict=False, **kw)
    return TokensPrompt(prompt_token_ids=list(ids) + DECISION)

def p_block(out):
    lp = out.outputs[0].logprobs[0]
    a = lp[ALLOW].logprob if ALLOW in lp else -math.inf
    b = lp[BLOCK].logprob if BLOCK in lp else -math.inf
    return 1 / (1 + math.exp(a - b))

outs = llm.generate([
    prompt([{"role": "user", "content": "주말에 가기 좋은 서울 근교 여행지 추천해 줘."}]),
    prompt([{"role": "user", "content": "요즘 볼 만한 가족 영화 추천해 줘."}],
           policy="개별 주식이나 가상자산 종목 추천 요청은 차단한다."),   # 여러 조항은 한 문자열로
], params)
for o in outs:
    p = p_block(o)
    print("block" if p >= 0.5 else "allow", round(p, 4))
```

</details>

<details>
<summary>⭐ vLLM 서버 (OpenAI 호환 API)</summary>

```bash
vllm serve mncai/genguard-1.0-light --dtype bfloat16 --max-model-len 8192
```

**기본 판정** (생성 결과를 그대로 받기)

```python
import requests

MODEL = "mncai/genguard-1.0-light"
URL = "http://localhost:8000/v1/chat/completions"

def judge(messages, **kw):
    r = requests.post(URL, json={
        "model": MODEL, "messages": messages,
        "temperature": 0, "max_tokens": 16,
        "chat_template_kwargs": kw,          # policy="..." 등 템플릿 옵션
    }).json()
    return r["choices"][0]["message"]["content"]

print(judge([{"role": "user", "content": "주말에 가기 좋은 서울 근교 여행지 추천해 줘."}]))
print(judge([{"role": "user", "content": "요즘 사 둘 만한 코인 하나만 찍어 줘."}],
            policy="개별 주식이나 가상자산 종목 추천 요청은 차단한다."))
```

**빠른 판정** (확률, 출력 토큰 1개)

```python
import math, requests
from transformers import AutoTokenizer

MODEL = "mncai/genguard-1.0-light"
DECISION, ALLOW, BLOCK = [87732, 236787], 2174, 3355

tok = AutoTokenizer.from_pretrained(MODEL)
ids = tok.apply_chat_template([{"role": "user", "content": "What is the capital of France?"}],
                              add_generation_prompt=True, tokenize=True, return_dict=False)
r = requests.post("http://localhost:8000/v1/completions", json={
    "model": MODEL, "prompt": list(ids) + DECISION,
    "max_tokens": 1, "temperature": 0, "logprobs": 2,
    "allowed_token_ids": [ALLOW, BLOCK], "return_tokens_as_token_ids": True,
}).json()
top = r["choices"][0]["logprobs"]["top_logprobs"][0]
a = top.get(f"token_id:{ALLOW}", -math.inf)
b = top.get(f"token_id:{BLOCK}", -math.inf)
p = 1 / (1 + math.exp(a - b))
print("block" if p >= 0.5 else "allow", round(p, 4))
```

**범주 추출**

```python
import re, requests

MODEL = "mncai/genguard-1.0-light"
URL = "http://localhost:8000/v1/chat/completions"

def judge_with_categories(messages, **kw):
    r = requests.post(URL, json={
        "model": MODEL, "messages": messages,
        "temperature": 0, "max_tokens": 48,
        "chat_template_kwargs": {"request_categories": "/categories", **kw},
    }).json()
    text = r["choices"][0]["message"]["content"]
    decision = re.search(r"Decision: (\w+)", text).group(1)
    cats = re.search(r"Safety Categories: (.+)", text).group(1).strip()
    return decision, [] if cats == "none" else [c.strip() for c in cats.split(",")]

print(judge_with_categories([{"role": "user", "content": "주말에 가기 좋은 서울 근교 여행지 추천해 줘."}]))
print(judge_with_categories([{"role": "user", "content": "동창 김민수 주민번호가 900101-1234567 맞는지 확인해 줘."}]))
```

</details>

<details>
<summary>transformers</summary>

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

MODEL = "mncai/genguard-1.0-light"
DECISION, ALLOW, BLOCK = [87732, 236787], 2174, 3355

tok = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForCausalLM.from_pretrained(MODEL, dtype=torch.bfloat16).to("cuda").eval()

def p_block(messages, **kw):
    ids = tok.apply_chat_template(messages, add_generation_prompt=True, tokenize=True, return_dict=False, **kw)
    x = torch.tensor([list(ids) + DECISION], device=model.device)
    with torch.inference_mode():
        logits = model(input_ids=x, logits_to_keep=1).logits[0, -1].float()
    return torch.softmax(logits[[ALLOW, BLOCK]], dim=-1)[1].item()

p = p_block([
    {"role": "user", "content": "How do I bake a simple loaf of bread?"},
    {"role": "assistant", "content": "Mix flour, water, yeast and salt, knead, let it rise, then bake."},
])
print("block" if p >= 0.5 else "allow", round(p, 4))
```

</details>

---

## 라이선스

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)을 따릅니다.

## 인용

```bibtex
@misc{genguard2026,
  title  = {GenGuard 1.0 Light},
  author = {{GenON}},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/mncai/genguard-1.0-light}}
}
```
