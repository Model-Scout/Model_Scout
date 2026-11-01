---
language:
- ko
- en
- zh
---
## Description

본 데이터셋은 현재 대규모 언어 모델(LLM)이 장문 문서를 처리하고 복잡한 추론을 수행할 때 나타나는 핵심적인 한계를 보완하기 위해 구축되었습니다. 중국어, 영어, 한국어의 3개 언어로 구성된 총 7,500개의 고품질 학습 데이터를 포함하고 있습니다. 각 데이터는 장문의 텍스트를 기반으로 하며, 여러 문단과 문서에 걸쳐 정보를 종합하고 여러 단계의 논리적 추론 과정을 거쳐야 답변할 수 있는 질문으로 구성되어 있습니다. 본 데이터셋은 모델의 장거리 문맥 이해, 관련 정보 검색 및 추출, 논리적 추론 경로 구성, 근거 정보의 출처 추적 능력을 종합적이고 체계적으로 평가하는 데 활용할 수 있습니다.

자세한 내용은 아래 링크를 참고해 주세요: https://ko.nexdata.ai/datasets/llm/2121?source=hf.kr

## Specifications

### Content

장문 문서 멀티홉 추론 QA 데이터셋

### Data Size

7,500

### Data Fields

id, context, file_count, question, answer, reasoning_chain, supporting_evidence, hops

### Language

ZH, EN, KO

### Format

JSON

# Licensing Information

상업용 라이선스