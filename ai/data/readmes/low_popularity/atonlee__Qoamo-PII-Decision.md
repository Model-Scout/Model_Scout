---
license: apache-2.0
language:
- ko
- en
library_name: transformers
pipeline_tag: text-classification
base_model:
- skt/A.X-Encoder-base
base_model_relation: finetune
tags:
- pii
- privacy
- guardrail
- decision-model
- on-device
- onnx
---

# Qoamo-PII-Decision

A routing model that catches personal data in Korean and English requests before they leave the device. Built on [skt/A.X-Encoder-base](https://huggingface.co/skt/A.X-Encoder-base) (ModernBERT, 149M parameters), it was fine-tuned as a decision model that answers questions about a text with a probability for every option.

It can be asked four things about a text (whether it contains personal data, whether it contains a strong identifier, its tier, and which of 33 types it holds), and the answers decide whether the text is sent as is, masked and then sent, or blocked. The decision is made from the first three questions; the types are asked only when needed. Locating the values is not its job. For a text it marks as containing personal data, [atonlee/koelectra-ko-pii-ner](https://huggingface.co/atonlee/koelectra-ko-pii-ner), built on the same tier1 and tier2 criteria, finds and masks the values. This keeps the fast filtering decision separate from precise masking by NER.

On the official KDPII test split, it scored an F1 of 0.951 at telling whether a sentence contains personal data, the highest among the compared models. The weights are a single safetensors file (bf16). If you need ONNX, use one of the four in `onnx/` (float32 · FP16 · INT8 · UINT8).

## News

**🔥 2026.10 Update**

- **English**: it now judges English text as well as Korean.
- **Types 23 → 33**: passwords, API keys or tokens, and verification codes or OTPs are asked about separately. Phone numbers are split into regular, business or toll-free, and short public numbers, and personal numbers into employee, member or customer, student or exam, and patient numbers, among others.
- **Decision and tier together**: `decide` returns the tier (tier1 · tier2 · none) along with the decision (보냄 · 확인 · 막음). With `with_types=True` it returns the types as well.
- **Asking with different criteria**: ask about several types as one (`has`), leave some types out (`has_pii_except`), or regroup the tiers into up to 4 levels (`tier`).
- **Long texts**: with `document=True`, a text of up to 2,000 characters is judged in one go. A longer one is split on line breaks and the strictest decision is returned.
- **Ready-to-use code**: load it with `AutoModel.from_pretrained(..., trust_remote_code=True)` and use it in one line with `model.decide(text)`.
- **Accuracy**: KDPII F1 0.896 → 0.951 (10 types 0.918 → 0.955). Every sentence holding a tier1 value was caught.

## Questions

The model can be asked four things about a text and gives a probability for every option.

- **`pii_any` — contains personal data?** (예 yes · 아니오 no)
- **`pii_t1` — contains a strong identifier?** (예 · 아니오)
- **`pii_tier` — tier** (tier1 · tier2 · none): picks the single highest tier in the text.
- **`type_*` — 33 types** (예 · 아니오 for each type)

`decide` asks only the first three; with `with_types=True` it also asks the 33 types. The questions never see each other, so the answers are the same however many are asked together, and asking fewer is faster.

### Tiers and types

| tier | meaning | recommended handling | types |
| --- | --- | --- | --- |
| tier1 | the value alone identifies a person or can cause harm | do not send off-device | resident registration number (주민등록번호), alien registration number (외국인등록번호), passport number (여권번호), driver's licence number (운전면허번호), i-PIN (아이핀), domestic ID number (국내 신분번호), foreign ID number (외국 신분번호), card number (카드번호), card expiry date (카드 유효기간), CVC, account number (계좌번호), password (비밀번호), API key or token (API 키·토큰), verification code or OTP (인증번호·OTP) |
| tier2 | identifies a person when combined with other information | find and mask it with NER, then send | name (이름), email (이메일), regular phone number (일반 전화번호), business or toll-free number (대표번호), short public number (특수번호), address (주소), postal code (우편번호), date of birth (생년월일), age (나이), gender (성별), employee number (사번), member or customer number (회원·고객번호), student or exam number (학생·응시번호), patient number (환자번호), other personal number (그 밖의 사람 번호), user ID (사용자 ID), URL, IP address (IP 주소), vehicle number (차량번호) |
| none | no personal data | send as is | — |

In code, use the Korean names in parentheses (CVC and URL as written); they are the names in `model.types`.

### Four answers per text

| text | contains personal data? (yes) | strong identifier (yes) | tier | types (yes ≥ 0.5) | decision |
| --- | ---: | ---: | --- | --- | --- |
| 박지훈 대리한테 010-4821-3307 로 문자 보내 줘 | 0.999 | 0.000 | tier2 (0.999) | name 0.995 · regular phone number 0.994 | 확인 |
| 내 주민번호 901023-1234567 로 등록 | 0.999 | 0.999 | tier1 (0.998) | resident registration number 0.950 | 막음 |
| 이번 주말에 비 오는지 알려 줘 | 0.002 | 0.000 | none (0.997) | none | 보냄 |
| Send the signed contract to david.kim@acme.io | 0.996 | 0.000 | tier2 (0.999) | email 0.997 | 확인 |

### Asking with different criteria

The tiers above are the default, and the 보냄 · 확인 · 막음 decision was tuned with them. The best results come from using the default tiers as they are. If your policy differs, there are three ways to change the criteria.

- **Grouping** (`has`): ask in one go whether any of several types, such as phone number, email and address, is present. On groups it had not seen in training, it was right 99% of the time. To treat some types more strictly, ask with this and raise the tier in your code.
- **Excluding** (`has_pii_except`, or leaving types out in `tier`): leave some types out, so that, for example, a text with only a name does not count as personal data. On texts holding the left-out types it was right 97% of the time or more.
- **Changing the tiers** (`tier`): move types between tiers. Use up to 4 levels, named tier1, tier2, tier3, tier4 and none. It is less accurate on texts that hold the moved types. In particular, a type moved up to tier1 tends to stay in its original tier when another tier2 value is present, so use grouping to raise a type.

The fourth and fifth examples under Usage show how. The question wording (the instructions in `pii_config.json`) can be changed too, but this is not recommended.

## Usage

Load it with `trust_remote_code=True`. Only the files it needs are downloaded, not `onnx/`. `decide` gives the decision and the tier from three questions.

```bash
pip install "transformers>=5.1" torch
```

```python
from transformers import AutoModel

model = AutoModel.from_pretrained("atonlee/Qoamo-PII-Decision", trust_remote_code=True)

for text in ["내일 오후 세 시에 팀 회의 잡아 줘",
             "박지훈 대리한테 010-4821-3307 로 문자 보내 줘",
             "내 주민번호 901023-1234567 로 등록",
             "Send the signed contract to david.kim@acme.io"]:
    r = model.decide(text)
    print(f"{r.route} | {r.tier} | {text}")
```

Output:

```text
보냄 | none | 내일 오후 세 시에 팀 회의 잡아 줘
확인 | tier2 | 박지훈 대리한테 010-4821-3307 로 문자 보내 줘
막음 | tier1 | 내 주민번호 901023-1234567 로 등록
확인 | tier2 | Send the signed contract to david.kim@acme.io
```

To see the types as well, pass `with_types=True`. It asks 36 questions and is several times slower.

```python
r = model.decide("박지훈 대리한테 010-4821-3307 로 문자 보내 줘", with_types=True)
print(r.route, r.tier, r.types)
```

Output:

```text
확인 tier2 ['이름', '일반 전화번호']
```

Judge a long text with `document=True`. A single corporate card number in the middle of the email is enough to block the whole email.

```python
mail = """팀장님, 지난주 부산 출장 정산 건으로 메일 드립니다.

일정은 10월 6일부터 8일까지 2박 3일이었고, 협력사 두 곳과 미팅을 진행했습니다.
교통비는 KTX 왕복 119,600원, 숙박비는 2박 236,000원, 식대는 84,000원입니다.
영수증 원본은 내일 오전 중에 경영지원팀 정산함에 넣어 두겠습니다.

숙박비는 법인카드 4518-3207-6614-2093 으로 결제했고, 나머지는 개인 카드로 냈습니다.
개인 결제분은 이번 달 급여와 함께 넣어 주시면 됩니다.

미팅 결과는 따로 정리해서 금요일 회의 때 공유드리겠습니다.
감사합니다."""

r = model.decide(mail, document=True, with_types=True)
print(r.route, r.tier, r.types)
```

Output:

```text
막음 tier1 ['카드번호']
```

To treat contact details more strictly, ask whether there are any and raise the tier if so. Only the second, third and fourth texts, which hold contact details, move up to tier1; the text with only a name and the text with an account number stay as they were.

```python
texts = ["김민수 팀장님께 오늘 회의록 보내 드려",
         "박지훈 대리한테 010-4821-3307 로 문자 보내 줘",
         "견적서 jiyoung.park@gmail.com 으로 보내 줘",
         "서울 강남구 테헤란로 152 12층으로 서류 보냈어",
         "신한 110-482-339201 로 월세 55만 원 보내 줘",
         "내일 오후 세 시에 팀 회의 잡아 줘"]
contact_types = ["일반 전화번호", "이메일", "주소"]

for text in texts:
    before = model.decide(text).tier
    after = "tier1" if model.has(text, contact_types, name="연락처") else before
    print(f"{before} → {after} | {text}")
```

Output:

```text
tier2 → tier2 | 김민수 팀장님께 오늘 회의록 보내 드려
tier2 → tier1 | 박지훈 대리한테 010-4821-3307 로 문자 보내 줘
tier2 → tier1 | 견적서 jiyoung.park@gmail.com 으로 보내 줘
tier2 → tier1 | 서울 강남구 테헤란로 152 12층으로 서류 보냈어
tier1 → tier1 | 신한 110-482-339201 로 월세 55만 원 보내 줘
none → none | 내일 오후 세 시에 팀 회의 잡아 줘
```

To stop counting names as personal data, ask with the default tiers minus names. The first text, which holds only a name, becomes none, and the second, with a name and a phone number, stays tier2 because of the phone number.

```python
custom_tiers = {"tier1": model.tiers["tier1"],
                "tier2": [t for t in model.tiers["tier2"] if t != "이름"]}

for text in texts:
    print(f"{model.decide(text).tier} → {model.tier(text, custom_tiers)} | {text}")
```

Output:

```text
tier2 → none | 김민수 팀장님께 오늘 회의록 보내 드려
tier2 → tier2 | 박지훈 대리한테 010-4821-3307 로 문자 보내 줘
tier2 → tier2 | 견적서 jiyoung.park@gmail.com 으로 보내 줘
tier2 → tier2 | 서울 강남구 테헤란로 152 12층으로 서류 보냈어
tier1 → tier1 | 신한 110-482-339201 로 월세 55만 원 보내 줘
none → none | 내일 오후 세 시에 팀 회의 잡아 줘
```

- `r.scores` holds the probability of every option for the questions asked.
- When the decision is 확인, find and mask the personal data with NER, then send.
- With `document=True`, a text over 2,000 characters is split on line breaks, each piece is judged, and the strictest decision and tier are returned (the pieces are in `r.pieces`).
- You can ask only the questions you need, like `model.ask(text, ["pii_any", "pii_t1"])`. The `decide` rule then does not apply.
- To leave ONNX out when downloading the whole repository, use `snapshot_download(..., ignore_patterns=["onnx/*"])`.

## Evaluation

We measured whether a sentence contains personal data on the official test split of [KDPII](https://zenodo.org/records/10968609) (CC BY 4.0). Sentences were selected based on our types and the 10 common types (3,998 sentences for our types, 3,737 for the 10 types). KDPII was not used to train this model. Widely used PII detection, decision and guard models on Hugging Face were run on the same sentences and scored the same way.

| model | size | precision | recall | F1 (our types) | F1 (10 types) |
| --- | ---: | ---: | ---: | ---: | ---: |
| **Qoamo-PII-Decision** | 149M | 0.954 | 0.947 | **0.951** | **0.955** |
| perplexity-ai/PII-Tracer | about 600M | 0.665 | 0.783 | 0.719 | 0.739 |
| LiquidAI/LFM2.5-Encoder-350M-PII-Detector | 350M | 0.940 | 0.503 | 0.655 | 0.738 |
| convaiinnovations/laya (Korean question) | 322M | 0.205 | 0.998 | 0.340 | 0.259 |
| Qwen/Qwen3Guard-Gen-0.6B | 0.6B | 0.556 | 0.231 | 0.326 | 0.357 |
| SupersonicLabs/Julia-1 (English question) | 144M | 0.178 | 0.523 | 0.266 | 0.205 |
| fastino/GLiNER2.5-multi-Decide (English question) | 287M | 0.279 | 0.217 | 0.244 | 0.214 |
| openai/privacy-filter (reference) | 1.4B | 0.813 | 0.612 | 0.698 | 0.775 |
| OpenMed/privacy-filter-multilingual (reference) | 1.4B | 0.530 | 0.869 | 0.658 | 0.602 |

- **F1 (our types)**: name · phone · mobile · email · vehicle number · IP · user ID · date of birth · age · gender · resident registration number · alien registration number · passport number · driver's licence number · card number · account number
- **F1 (10 types)**: name · phone · mobile · email · resident registration number · alien registration number · passport number · driver's licence number · card number · account number

## Data

Training data includes the following.

- [BCCard/privacy-filter-openpii-masking](https://huggingface.co/datasets/BCCard/privacy-filter-openpii-masking) (CC BY 4.0)
- [nvidia/Nemotron-PII](https://huggingface.co/datasets/nvidia/Nemotron-PII) (CC BY 4.0)
- [clinc/clinc_oos](https://huggingface.co/datasets/clinc/clinc_oos) (CC BY 3.0)

## License

Apache-2.0
