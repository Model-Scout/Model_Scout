---
language:
- ko
license: mit
tags:
- finance
- extractive-summarization
- sentence-extraction
- role-classification
- korean
- roberta
pipeline_tag: text-classification
base_model: klue/roberta-base
metrics:
- f1
- accuracy
---

# LQ-FSE-base: Korean Financial Sentence Extractor

금융 리포트, 금융 관련 뉴스에서 대표문장을 추출하고 역할(outlook, event, financial, risk)을 분류하는 모델입니다.

## Model Description

- **Base Model**: klue/roberta-base
- **Architecture**: Sentence Encoder (RoBERTa) + Inter-sentence Transformer (2 layers) + Dual Classifiers
- **Task**: Extractive Summarization + Role Classification (Multi-task)
- **Language**: Korean
- **Domain**: Financial Reports (증권 리포트), Financial News (금융 뉴스)

### Input Constraints

| Parameter | Value | Description |
|-----------|-------|-------------|
| Max sentence length | 128 tokens | 문장당 최대 토큰 수 (초과 시 truncation) |
| Max sentences per document | 30 | 문서당 최대 문장 수 (초과 시 앞 30개만 사용) |
| Input format | Plain text | 문장 부호(`.!?`) 기준으로 자동 분리 |

- **입력**: 한국어 금융 텍스트 (증권 리포트, 금융 뉴스 등)
- **출력**: 각 문장별 대표문장 점수 (0~1) + 역할 분류 (outlook/event/financial/risk)

### Performance

| Metric | Score |
|--------|-------|
| Extraction F1 | 0.705 |
| Role Accuracy | 0.851 |

### Role Labels

| Label | Description |
|-------|-------------|
| `outlook` | 전망/예측 문장 |
| `event` | 이벤트/사건 문장 |
| `financial` | 재무/실적 문장 |
| `risk` | 리스크 요인 문장 |

## Usage

```python
import re
import torch
from transformers import AutoConfig, AutoModel, AutoTokenizer

repo_id = "LangQuant/LQ-FSE-base"

# 모델 로드
config = AutoConfig.from_pretrained(repo_id, trust_remote_code=True)
model = AutoModel.from_pretrained(repo_id, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(repo_id)
model.eval()

# 입력 텍스트
text = (
    "삼성전자의 2024년 4분기 실적이 시장 예상을 상회했다. "
    "메모리 반도체 가격 상승으로 영업이익이 전분기 대비 30% 증가했다. "
    "HBM3E 양산이 본격화되면서 AI 반도체 시장 점유율이 확대될 전망이다."
)

# 문장 분리 및 토큰화
sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text.strip()) if s.strip()]
max_len, max_sent = config.max_length, config.max_sentences

padded = sentences[:max_sent]
num_real = len(padded)
while len(padded) < max_sent:
    padded.append("")

ids_list, mask_list = [], []
for s in padded:
    if s:
        enc = tokenizer(s, max_length=max_len, padding="max_length", truncation=True, return_tensors="pt")
    else:
        enc = {"input_ids": torch.zeros(1, max_len, dtype=torch.long),
               "attention_mask": torch.zeros(1, max_len, dtype=torch.long)}
    ids_list.append(enc["input_ids"])
    mask_list.append(enc["attention_mask"])

input_ids = torch.cat(ids_list).unsqueeze(0)
attention_mask = torch.cat(mask_list).unsqueeze(0)
doc_mask = torch.zeros(1, max_sent)
doc_mask[0, :num_real] = 1

# 추론
with torch.no_grad():
    scores, role_logits = model(input_ids, attention_mask, doc_mask)

role_labels = config.role_labels
for i, sent in enumerate(sentences):
    score = scores[0, i].item()
    role = role_labels[role_logits[0, i].argmax().item()]
    marker = "*" if score >= 0.5 else " "
    print(f"  {marker} [{score:.4f}] [{role:10s}] {sent}")
```

### Input Example

```
삼성전자의 2024년 4분기 실적이 시장 예상을 상회했다. 메모리 반도체 가격 상승으로 영업이익이 전분기 대비 30% 증가했다. HBM3E 양산이 본격화되면서 AI 반도체 시장 점유율이 확대될 전망이다.
```

### Output Example

```
  * [0.8732] [financial ] 삼성전자의 2024년 4분기 실적이 시장 예상을 상회했다.
  * [0.7145] [financial ] 메모리 반도체 가격 상승으로 영업이익이 전분기 대비 30% 증가했다.
  * [0.9021] [outlook   ] HBM3E 양산이 본격화되면서 AI 반도체 시장 점유율이 확대될 전망이다.
```

- `*` 표시: 대표문장으로 선정됨 (score ≥ 0.5)
- `[score]`: 대표문장 확률 (0~1, 높을수록 핵심 문장)
- `[role]`: 문장 역할 분류 (outlook / event / financial / risk)

## Disclaimer (면책 조항)

- 본 모델은 **연구 및 정보 제공 목적**으로만 제공됩니다.
- 본 모델의 출력은 **투자 조언, 금융 자문, 매매 추천이 아닙니다.**
- 모델의 예측 결과를 기반으로 한 투자 판단에 대해 LangQuant 및 개발자는 **어떠한 법적 책임도 지지 않습니다.**
- 모델의 정확성, 완전성, 적시성에 대해 보증하지 않으며, 실제 투자 의사결정 시 반드시 전문가의 조언을 구하시기 바랍니다.
- 금융 시장은 본질적으로 불확실하며, 과거 데이터로 학습된 모델이 미래 성과를 보장하지 않습니다.

## Usage Restrictions (사용 제한)

- **금지 사항:**
  - 본 모델을 이용한 시세 조종, 허위 정보 생성 등 불법적 목적의 사용
  - 자동화된 투자 매매 시스템의 단독 의사결정 수단으로 사용
  - 모델 출력을 전문 금융 자문인 것처럼 제3자에게 제공하는 행위
- **허용 사항:**
  - 학술 연구 및 교육 목적의 사용
  - 금융 텍스트 분석 파이프라인의 보조 도구로 활용
  - 사내 리서치/분석 업무의 참고 자료로 활용
- 상업적 사용 시 LangQuant에 사전 문의를 권장합니다.

## Contributors

- **[Taegyeong Lee](https://www.linkedin.com/in/taegyeong-lee/)** (taegyeong.leaf@gmail.com)
- **[Dong Young Kim](https://www.linkedin.com/in/dykim04/)** (dong-kim@student.42kl.edu.my) — Ecole 42
- **[Seunghyun Hwang](https://www.linkedin.com/in/seung-hyun-hwang-53700124a/)** (hsh1030@g.skku.edu) — DSSAL
