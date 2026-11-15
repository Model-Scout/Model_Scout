---
pipeline_tag: text-generation
language:
- ko
- en
- ja
- zh
- es
- pt
- de
- ru
- hi
- vi
- th
tags:
- baar2
- 150m
- multilingual
- text-generation
- lightweight
- rag
license: other
license_name: non-commercial-only
license_link: LICENSE
---

<p align="center">
  <a href="https://baar.uk/model/">
    <img src="https://cdn.jsdelivr.net/npm/minicon1@latest/logo/baar.png" alt="BAAR Logo" width="180">
  </a>
</p>

<h1 align="center">BAAR2-150M</h1>

<p align="center">
  🌐 <b>Official Website:</b> <a href="https://baar.uk/model/">https://baar.uk/model/</a></br>
  📄 <b>License:</b> Non-Commercial Only (Contact for Commercial Pricing)
</p>

---

## 📌 Model Overview

**BAAR2-150M** is a lightweight multilingual language model designed for fast, resource-efficient inference across 11 languages. Optimized for low latency and minimal compute environments, it enables responsive real-time generation on edge devices, mobile platforms, and resource-constrained servers.

**BAAR2-150M** 은 저사양 하드웨어 및 리소스 제약 환경에서도 빠르고 안정적인 동작이 가능하도록 설계된 1.5억(150M) 파라미터 규모의 초경량 다국어 언어 모델입니다. 지연 시간(Latency)을 최소화하여 온디바이스(Edge), 실시간 대화, 경량 RAG(검색 증강 생성) 시스템 등에 최적화되어 있습니다.

---

## 📊 Live Sample Inference

*Hardware: Single NVIDIA Tesla T4 | FP16 Inference*

| Task / Category | Prompt | Generated Output | Latency |
| :--- | :--- | :--- | :--- |
| **Korean General QA** | 대한민국의 수도는 어디인가요? | `대한민국의 수도는 서울입니다. 개인적으로, 이 지역의 수도가 너` | ~1451.0ms |
| **English General QA** | What is artificial intelligence? | `A comprehensive machine that is designed to perform tasks that normally require` | ~671.2ms |
| **KO-to-EN Translation (1)** | 안녕이 영어로 뭐야? | `안녕은 영어로 Hello 입니다.` | ~390.0ms |
| **KO-to-EN Translation (2)** | 사과가 영어로 뭐야? | `사과는 영어로 apple 입니다.` | ~359.4ms |
| **EN-to-KO Translation** | What is 'Seoul' in Korean? | `A company that is a company that operates in the United` | ~571.1ms |
| **Japanese General QA** | 日本の首都はどこですか？ | `日本の首都は、 東京都双方にあり` | ~661.0ms |

---

## 🔍 Retrieval-Augmented Generation (RAG) Benchmark

This benchmark demonstrates the end-to-end performance of coupling a real-time vector retrieval pipeline with **BAAR2-150M** generation. It highlights the ultra-low latency response times and context-utilization capabilities achievable within an ultra-lightweight 150M-parameter footprint.

실시간 벡터 검색(Retrieval)과 **BAAR2-150M** 생성을 결합한 RAG 파이프라인 테스트 결과입니다. 150M 파라미터 경량 모델의 극대화된 추론 속도와 외부 문맥(Context) 활용 능력을 보여줍니다.

```text
===========================================================================
🚀 [Starting Real-Time RAG Q&A]
===========================================================================

[1/4] 👤 질문: 아이폰 16 프로 가장 싼 모델 얼마부터 시작해?
   🔍 검색된 문서 (유사도 0.67 | ⏱️ 231.1ms):
      "아이폰 16 프로는 항공우주 등급 티타늄 디자인으로 제작되었으며 출고가는 128GB 모델 기준 155만 원부터 시작합..."
   🤖 AI 답변: 제 개인적인 견해로는, 아이폰 16은 가격이 높고 가볍지  (⏱️ 928.1ms)
---------------------------------------------------------------------------

[2/4] 👤 질문: 신입사원이 연차 쓰려면 며칠 전에 승인받아야 해?
   🔍 검색된 문서 (유사도 0.79 | ⏱️ 52.5ms):
      "사내 취업규칙 제18조에 따라 근속 1년 미만 신규 입사자는 매월 개근 시 1일씩 총 11일의 연차가 부여됩니다. 연..."
   🤖 AI 답변: 1. 연차 쓰려면 2. 인트라넷을 사용하는 것이 좋  (⏱️ 530.3ms)
---------------------------------------------------------------------------

[3/4] 👤 질문: 지구가 자전하는 과학적 이유가 뭐야?
   🔍 검색된 문서 (유사도 0.65 | ⏱️ 16.0ms):
      "태양계 형성 시기인 약 45억 년 전 거대한 가스와 먼지로 이루어진 원시 성운이 중력으로 수축하면서 각운동량 보존 법..."
   🤖 AI 답변: 우주 공간에는 약 450,000년이 있습니다.  (⏱️ 421.5ms)
---------------------------------------------------------------------------

[4/4] 👤 질문: 스페인의 수도는 어디인가요?
   🔍 검색된 문서 (유사도 0.81 | ⏱️ 11.3ms):
      "스페인은 남유럽 이베리아반도에 위치한 입헌군주제 국가입니다. 국토 면적은 약 50만 제곱킬로미터에 달하며, 국가의 행..."
   🤖 AI 답변: 스페인의 수도는 마드리드입니다.  (⏱️ 271.8ms)
---------------------------------------------------------------------------
```

---

## 📄 License & Commercial Terms (라이선스 및 상업적 이용 안내)

- **Non-Commercial Use Only (비상업적 연구·개인 이용 한정)**:  
  This model is strictly available for **non-commercial, educational, and research purposes only**. Any form of monetization (direct or indirect) without an explicit commercial license is strictly prohibited.  
  본 모델은 **순수 연구, 교육 및 개인 비영리 목적에 한해 무료로 사용**할 수 있습니다. 사전 허가 없는 일체의 수익 창출 행위(직·간접적 상업적 이용)는 엄격히 금지됩니다.

- **Monetization & Commercial Licensing Inquiries (수익 창출 및 상용 라이선스 문의)**:  
  If you wish to **monetize, integrate this model into commercial products, provide paid services/APIs, or require enterprise-level support**, you must obtain a separate commercial license. Please reach out via email for licensing terms and enterprise adoption.  
  본 모델을 활용하여 **수익을 창출하고자 하거나, 상용 서비스/유료 제품에 탑재, 또는 기업용 맞춤 적용 및 기술 지원이 필요한 경우** 반드시 별도의 상용 라이선스를 취득하셔야 합니다. 도입 및 라이선스 발급은 아래 이메일로 문의해 주시기 바랍니다.
  - **Commercial Inquiries (상용 라이선스 문의)**: [admin@099.kr](mailto:admin@099.kr)
  - **Official Website (공식 웹사이트)**: [https://baar.uk/model/](https://baar.uk/model/)

---

## ⚠️ Notes (안내 사항)

- **Pre-trained Model**: This model is a base pre-trained checkpoint. For specific tasks, factual alignment, or structured dialogue, task-specific fine-tuning (SFT) or Retrieval-Augmented Generation (RAG) is recommended.
- **기초 사전학습 모델**: 본 가중치는 사전학습 단계의 베이스 모델입니다. 특정 도메인 작업, 사실 관계 검증 및 정교한 대화 생성이 필요한 경우 파인튜닝(SFT) 또는 검색 증강 생성(RAG) 파이프라인과의 연계를 권장합니다.

---

## 💼 Opportunities & Contact (채용 제안 및 투자 문의)

This project demonstrates practical competency in custom model architecture design, end-to-end distributed training optimization, and efficient multi-language serving under compute constraints.

I am actively seeking **AI Engineering / Research opportunities, team recruitment offers, and project investment/partnerships**.

- **Official Model Site (모델 공식 웹사이트)**: [https://baar.uk/model/](https://baar.uk/model/)
- **Model Adoption & Licensing (도입 및 라이선스 문의)**: [admin@099.kr](mailto:admin@099.kr)
- **Recruitment & Hiring Inquiries (채용 및 포지션 제안)**: [admin@099.kr](mailto:admin@099.kr)
- **Investment & Technical Collaboration (투자, 파트너십 및 기술 협업)**: [admin@099.kr](mailto:admin@099.kr)

*제한된 하드웨어 리소스 환경에서 고효율 다국어 모델 아키텍처를 직접 설계하고 훈련 파이프라인을 엔드투엔드로 구축할 수 있는 AI 엔지니어입니다. 저의 기술적 역량 영입(채용)이나 프로젝트 협업/투자에 관심이 있으신 기업 및 팀의 연락을 기다립니다.*