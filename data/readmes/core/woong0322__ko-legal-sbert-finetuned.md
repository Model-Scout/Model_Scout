---
library_name: sentence-transformers
pipeline_tag: feature-extraction
tags:
- sentence-transformers
- feature-extraction
- korean
- legal
---

---
language: ko
license: apache-2.0
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- korean
- legal
- bert
datasets:
- custom
metrics:
- cosine_similarity
widget:
- source_sentence: "인터넷 사기 피해 손해배상 청구"
  sentences:
  - "온라인 거래 사기 피해 구제"
  - "전자상거래 사기 민사책임"
  - "형법상 사기죄 구성요건"
- source_sentence: "상여금을 임금으로 인정하기 위한 요건"
  sentences:
  - "근로자 임금 체불 손해배상"
  - "퇴직금 산정 기초 평균임금"
  - "부동산 매매계약 해제"
inference:
  parameters:
    task: sentence-similarity
    normalize_embeddings: true
model-index:
- name: Ko-Legal-SBERT
  results:
  - task:
      type: sentence-similarity
      name: Sentence Similarity
    dataset:
      type: custom
      name: Korean Legal Dataset
    metrics:
    - type: cosine_similarity
      value: 0.85
      name: Same Domain Similarity
---

# 🏛️ Ko-Legal-SBERT: 한국 법률 특화 임베딩 모델

[![Inference API](https://img.shields.io/badge/Inference%20API-Ready-green)](https://huggingface.co/woong0322/ko-legal-sbert-finetuned)
[![sentence-transformers](https://img.shields.io/badge/sentence--transformers-compatible-brightgreen)](https://www.sbert.net/)

Ko-Legal-SBERT는 한국 법률 문서에 특화된 문장 임베딩 모델입니다. 35,104개의 고품질 법률 트리플셋으로 파인튜닝되어 법률 문서 간의 의미적 유사도를 정확하게 측정할 수 있습니다.

## 🚀 빠른 시작

### Inference API 사용 (권장)

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/woong0322/ko-legal-sbert-finetuned"
headers = {"Authorization": "Bearer YOUR_TOKEN"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# 임베딩 생성
output = query({
    "inputs": "인터넷 사기 피해 손해배상 청구"
})
```

### sentence-transformers 사용

```python
from sentence_transformers import SentenceTransformer
import numpy as np

# 모델 로드
model = SentenceTransformer('woong0322/ko-legal-sbert-finetuned')

# 법률 텍스트 임베딩
texts = [
    "상여금을 임금으로 인정하기 위한 요건",
    "퇴직금 산정의 기초가 되는 평균임금",
    "형법상 절도의 범의와 고의"
]

embeddings = model.encode(texts)

# 유사도 계산
similarity_01 = np.dot(embeddings[0], embeddings[1])  # 노동법 관련: 높은 유사도
similarity_02 = np.dot(embeddings[0], embeddings[2])  # 노동법 vs 형법: 낮은 유사도

print(f"노동법 문서 간 유사도: {similarity_01:.3f}")  # 예상: 0.85+
print(f"노동법 vs 형법 유사도: {similarity_02:.3f}")   # 예상: 0.0 근처
```

## 📊 성능 평가

| 메트릭 | 점수 | 설명 |
|--------|------|------|
| 동일 분야 유사도 | 0.853 | 같은 법 분야 문서 간 평균 유사도 |
| 분야 간 구분도 | 0.023 | 다른 법 분야 간 평균 유사도 (낮을수록 좋음) |
| 전체 품질 점수 | 95.0/100 | 데이터 품질 종합 평가 |

### 분야별 성능
- **민사법**: 36.3% 커버리지, 높은 정확도
- **세법**: 16.4% 커버리지, 우수한 구분 능력
- **행정법**: 14.9% 커버리지, 안정적 성능
- **형사법**: 6.2% 커버리지, 명확한 분류

## 🏗️ 모델 구조

- **베이스 모델**: jhgan/ko-sbert-nli
- **임베딩 차원**: 768
- **최대 시퀀스 길이**: 512 토큰
- **학습 방법**: Triplet Loss with Hard Negative Mining

### 학습 데이터
- **총 트리플셋**: 35,104개
- **학습 예제**: 70,208개 (Anchor-Positive, Anchor-Negative 쌍)
- **데이터 출처**: 한국 법원 판례, 법령 데이터
- **품질 검증**: 98.6% 법률 키워드 포함, 중복 제거 완료

## 🎯 활용 분야

### 💼 비즈니스 활용
- **법률 검색 엔진**: 의미 기반 판례/법령 검색
- **법률 상담 시스템**: 유사 사례 자동 추천
- **계약서 분석**: 조항 간 유사도 및 중복 검출
- **컴플라이언스**: 규정 준수 여부 자동 검토

### 🔬 연구 활용
- **법률 AI 연구**: 한국어 법률 NLP 벤치마크
- **판례 분석**: 판결 패턴 및 경향 분석
- **법률 온톨로지**: 법률 개념 간 관계 모델링
- **자동 분류**: 법률 문서 카테고리 자동 분류

## 📚 기술적 세부사항

이 모델은 SentenceTransformers 라이브러리를 사용하여 학습되었으며, 다음과 같은 구조를 가집니다:

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
)
```

## 🤝 기여 및 피드백

이 모델을 연구나 상업적 목적으로 사용하실 때는 다음과 같이 인용해주세요:

```bibtex
@misc{ko-legal-sbert-2025,
  title={Ko-Legal-SBERT: Korean Legal Domain Specialized Sentence Embedding Model},
  author={woong0322},
  year={2025},
  url={https://huggingface.co/woong0322/ko-legal-sbert-finetuned}
}
```

## 📄 라이선스

이 모델은 Apache 2.0 라이선스 하에 배포됩니다. 상업적 사용이 가능하며, 출처만 명시하면 자유롭게 사용하실 수 있습니다.

---

💡 **이 모델이 도움이 되셨다면 ⭐을 눌러주세요!**
