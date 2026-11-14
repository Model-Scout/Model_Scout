---
language:
  - ko
license: cc-by-sa-4.0
base_model: klue/roberta-large
pipeline_tag: text-classification
tags:
  - news
  - economics
  - framing
  - korean
  - distillation
metrics:
  - f1
  - accuracy
---

# klue-roberta-framing-3class

한국어 **경제 뉴스의 프레이밍(논조)**을 긍정·중립·부정 3가지로 분류하는 모델입니다.
같은 사실을 긍정적인 틀 또는 부정적인 틀로 제시하는 **가치 프레이밍(valence framing)**을 다룹니다.
예를 들어 "GDP 2.3% 성장"을 "견조한 성장세"로 쓰면 긍정, "성장 둔화 우려"로 쓰면 부정입니다.

순천향대학교 컴퓨터소프트웨어공학과 졸업작품 「경제 뉴스 편향 탐지 및 주가 영향 분석 시스템」의 일부입니다.
코드: https://github.com/likeramm/econ-framing-bias

## 라벨

| id | label | 정의 |
|----|-------|------|
| 0 | `negative` (부정) | 둔화·하락·우려·위기의 틀로 서술 |
| 1 | `neutral` (중립) | 기자의 해석이 최소화된 사실·수치 전달, 또는 양측을 병렬 제시하고 평가 유보 |
| 2 | `positive` (긍정) | 성장·회복·개선·안도의 틀로 서술. 우려를 언급해도 완화·방어로 마무리 |

판정의 핵심 원칙은 **"사건이 아니라 서술을 본다"**입니다. 나쁜 사건이라도 수치와 경과만 건조하게 전달하면 중립입니다.

## 사용법

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

repo = "likeramm/klue-roberta-framing-3class"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo).eval()

def classify(title, content=""):
    # 학습과 같은 입력 형식: "제목 [SEP] 본문 앞 500자", 최대 256 토큰
    text = f"{title} [SEP] {content[:500]}" if len(content.strip()) > 10 else title
    enc = tok(text, max_length=256, truncation=True, return_tensors="pt")
    with torch.no_grad():
        probs = torch.softmax(model(**enc).logits, dim=-1)[0]
    return {model.config.id2label[i]: round(p.item(), 4) for i, p in enumerate(probs)}

classify("2분기 GDP 2.3%…성장 둔화 우려 확대, 불확실성 고조")
```

## 학습

- **방법**: LLM 라벨을 소형 모델로 옮기는 지식 증류. `klue/roberta-large`를 파인튜닝했습니다.
- **데이터**: 2016~2026년 한국 경제 뉴스 13,268건 (38개 매체, 15개 경제 이벤트)
  - 라벨: **gpt-5.5**가 라벨링 가이드라인 프롬프트(v2)로 판정한 결과 (OpenAI Batch API)
  - 평가용 기사(사람 라벨 골든셋 600건, 반사실 테스트셋 원본)는 학습에서 제외
  - 학습 8,866 / 검증 1,900 / 테스트 1,901 (층화 분할, seed 42). 검증셋으로 모델을 고르고, 테스트셋으로 최종 보고
- **입력**: `제목 [SEP] 본문 앞 500자`, 최대 256 토큰
- **설정**: lr 1e-5, batch 4 × gradient accumulation 2, 최대 6 epoch(조기 종료 patience 2), 클래스 가중 교차엔트로피, FP16, RTX 4060

## 성능

**테스트셋 (n=1,901, 정답 = gpt-5.5 라벨)**

| | F1 |
|---|---|
| 부정 | 0.912 |
| 중립 | 0.775 |
| 긍정 | 0.853 |
| **Macro-F1** | **0.847** |
| Accuracy | 0.864 |

**사람 라벨과의 일치도 (파일럿 50건, 학습 제외)**: 정확도 0.74, Cohen's κ 0.58

> 테스트 점수는 **gpt-5.5의 판단을 얼마나 잘 재현하는지**를 뜻합니다. 정답이 LLM 라벨이므로
> 이 모델의 실제 정확도는 LLM 라벨의 품질을 넘을 수 없습니다. 사람 평가자 기준의 검증은 진행 중입니다.

## 한계

- **확률이 과신되어 있습니다.** 학습 손실이 매우 낮아(약 0.08) 출력 확률이 0.99 이상으로 몰리는 경우가 많습니다. 확률을 "확신의 정도"로 해석하지 마세요.
- **중립이 가장 어렵습니다.** 사람과 LLM의 판단도 중립에서 가장 많이 엇갈립니다.
- **사건의 좋고 나쁨에 끌리는 경향**이 있습니다. "GDP 2.3% 성장 발표"처럼 건조한 사실 보도를 긍정으로 분류하기도 합니다. 학습 라벨(v2 프롬프트)의 경향을 물려받은 것으로, 강도어 방향 규칙(R0-a)과 인용 규칙(R0-b)을 추가한 v3 가이드라인과는 차이가 있습니다.
- **거시 경제 뉴스**로 학습했습니다. 개별 기업 뉴스, 다른 분야 뉴스, 다른 시기에는 성능이 떨어질 수 있습니다.

## 용도

뉴스 프레이밍 연구, 매체 간 보도 비교, 미디어 리터러시 도구에 쓰기 위한 모델입니다.
**투자 판단에 쓰지 마세요.** 이 프로젝트의 분석에서 뉴스 논조는 이후 주가 방향을 예측하지 못했습니다.
