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
- 9m
- multilingual
- text-generation
- ultra-lightweight
- edge-ai
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

<h1 align="center">BAAR2-9M</h1>

<p align="center">
  🌐 <b>Official Website:</b> <a href="https://baar.uk/model/">https://baar.uk/model/</a></br>
  📄 <b>License:</b> Non-Commercial Only (Contact for Commercial Pricing)
</p>

---

## 📌 Model Overview

**BAAR2-9M** is an ultra-compact multilingual conversational model designed to enable real-time chat under minimal hardware conditions. With just **9 million (9M) parameters**, it brings lightweight, interactive dialogue capabilities across **11 languages** to extreme resource-constrained environments, embedded devices, and on-device platforms where standard LLMs cannot operate.

**BAAR2-9M**은 최소한의 하드웨어 여건과 극단적인 리소스 제약 환경에서도 **11개 언어**로 실시간 대화(Chat)가 가능하도록 설계된 900만(9M) 파라미터 규모의 초경량 다국어 언어 모델입니다. 일반적인 대형 모델 구동이 불가능한 초저사양 엣지 및 임베디드 기기에서도 즉각적인 대화형 추론과 초경량 실시간 RAG 시스템 구축을 지원합니다.

---

## 📊 Live Sample Inference

*Hardware: Single NVIDIA Tesla T4 | FP16 Inference*

| Task / Category | Prompt | Generated Output | Latency |
| :--- | :--- | :--- | :--- |
| **한국어 일반 QA** | 대한민국의 수도는 어디인가요? | `대한민국의 수도는 1920년 6월 11일에 유럽` | ~325.2ms |
| **영어 일반 QA** | What is artificial intelligence? | `A metal consisting of a metal consisting of a` | ~314.0ms |
| **일상어 번역 요청** | 안녕이 영어로 뭐야? | `안녕은 영어로 Hello 입니다.` | ~245.3ms |
| **일상어 번역 요청 2** | 사과가 영어로 뭐야? | `사과는 영어로 apple 입니다.` | ~216.1ms |
| **영->한 번역 요청** | What is 'Seoul' in Korean? | `'Seoul' in Korean is 서울.` | ~227.6ms |
| **일본어 일반 QA** | 日本の首都はどこですか？ | `日本の首都は、 大阪市に公立` | ~325.1ms |
| **중국어 일반 QA** | 人工智能的主要特点是什么？ | `人工智能是一种可再生能源的主要` | ~348.4ms |
| **스페인어 일반 QA** | ¿Cuál es la capital de España? | `España is un capital of medior and el capital` | ~294.3ms |
| **러시아어 일반 QA** | Какая столица России? | `Столица России — это предложение, кото` | ~321.3ms |
| **힌디어 일반 QA** | भारत की राजधानी क्या है? | `भारत की राजधानी के दौरान भारत के बाद प्राणी` | ~290.9ms |

---

## 🔍 Retrieval-Augmented Generation (RAG) Benchmark

This benchmark demonstrates real-time integration between vector retrieval and the **BAAR2-9M** ultra-lightweight generation model, proving near-instantaneous contextual response generation even with just a 9M parameter footprint.

실시간 벡터 검색(Retrieval)과 **BAAR2-9M** 초경량 생성 엔진을 연동한 RAG 파이프라인 테스트 결과입니다. 900만 파라미터 크기에서도 외부 문맥(Context)을 전달받아 서브-세컨드(Sub-second) 단위의 극단적인 반응 속도를 발휘합니다.

```text
================================================================================
🚀 [Starting Real-Time RAG Q&A (BAAR2-9M)]
================================================================================

[1/4] 👤 질문: 아이폰 16 프로 가장 싼 모델 얼마부터 시작해?
   🔍 검색 문서 (유사도 0.67 | ⏱️ 79.0ms): "아이폰 16 프로는 항공우주 등급 티타늄 디자인으로 제작되었으며 출고가는 128GB 모델 기준 155만 원부..."
   🤖 AI 답변: 저는 A18 Pro 칩을 탑재하고 있습니다. (⏱️ 298.2ms)
--------------------------------------------------------------------------------

[2/4] 👤 질문: 신입사원이 연차 쓰려면 며칠 전에 승인받아야 해?
   🔍 검색 문서 (유사도 0.79 | ⏱️ 18.1ms): "사내 취업규칙 제18조에 따라 근속 1년 미만 신규 입사자는 매월 개근 시 1일씩 총 11일의 연차가 부여됩..."
   🤖 AI 답변: 전 세계 입사원이 부서장 승인받아야  (⏱️ 429.1ms)
--------------------------------------------------------------------------------

[3/4] 👤 질문: 지구가 자전하는 과학적 이유가 뭐야?
   🔍 검색 문서 (유사도 0.65 | ⏱️ 16.8ms): "태양계 형성 시기인 약 45억 년 전 거대한 가스와 먼지로 이루어진 원시 성운이 중력으로 수축하면서 각운동량..."
   🤖 AI 답변: 개인적으로, 이러한 원시 성우동량은 각 과 (⏱️ 425.0ms)
--------------------------------------------------------------------------------

[4/4] 👤 질문: 스페인의 수도는 어디인가요?
   🔍 검색 문서 (유사도 0.81 | ⏱️ 20.0ms): "스페인은 남유럽 이베리아반도에 위치한 입헌군주제 국가입니다. 국토 면적은 약 50만 제곱킬로미터에 달하며, ..."
   🤖 AI 답변: 개인적으로, 국토 면적은 남유럽의 경제 발 (⏱️ 449.9ms)
--------------------------------------------------------------------------------
```

---

## 📄 License & Commercial Terms (라이선스 및 상업적 도입 안내)

- **Non-Commercial Use Only (비상업적 연구·개인 이용 한정)**:  
  This model is strictly provided for **non-commercial, research, and educational purposes only**. Any commercial use without a separate commercial agreement is strictly prohibited.  
  본 모델은 **순수 연구, 교육 및 개인 비영리 목적에 한해서만 무료로 제공**됩니다. 사전 허가 없는 일체의 영리적 이용은 엄격히 금지됩니다.

- **Commercial Licensing & Inquiries for Revenue-Generating Entities (매출 발생 기업 및 상용화 도입 문의)**:  
  **If your organization generates revenue, or if you plan to incorporate this model into commercial products, services, or paid APIs, you are required to purchase a commercial license.** Please contact us directly via email for enterprise licensing and integration support.  
  **기업/사업체에 매출이 발생하고 있거나, 본 모델을 상용 서비스·유료 제품·수익 창출 목적의 시스템에 도입하고자 하시는 경우 반드시 별도의 상용 라이선스를 취득하셔야 합니다.** 도입 조건 및 기업용 라이선스 발급은 아래 이메일로 문의해 주시기 바랍니다.
  - **도입 및 상용 라이선스 문의 (Commercial Inquiries)**: [admin@099.kr](mailto:admin@099.kr)
  - **공식 웹사이트 (Official Website)**: [https://baar.uk/model/](https://baar.uk/model/)

---

## ⚠️ Notes (안내 사항)

- **Pre-trained Model**: This model is a compact base pre-trained checkpoint. For specialized tasks, factual precision, or task completion, task-specific fine-tuning (SFT) or Retrieval-Augmented Generation (RAG) pipelines are recommended.
- **기초 사전학습 모델**: 본 모델은 9M 규모의 베이스 사전학습 체크포인트입니다. 정교한 작업 수행, 사실 관계 검증 및 완성도 높은 대화 생성이 필요한 경우 도메인 파인튜닝(SFT) 또는 검색 증강 생성(RAG) 파이프라인 결합을 권장합니다.

---

## 💼 Opportunities & Contact (채용 제안 및 투자 문의)

This project demonstrates practical competency in designing custom micro-scale architectures, end-to-end multi-language pre-training, and ultra-low-latency deployment under extreme compute constraints.

I am actively seeking **AI Engineering / Research opportunities, recruitment offers, and technical partnerships**.

- **공식 웹사이트 (Official Website)**: [https://baar.uk/model/](https://baar.uk/model/)
- **기업 도입 및 라이선스 문의 (Commercial Adoption)**: [admin@099.kr](mailto:admin@099.kr)
- **채용 및 포지션 제안 (Recruitment & Hiring)**: [admin@099.kr](mailto:admin@099.kr)
- **투자 및 기술 협력 문의 (Investment & Partnerships)**: [admin@099.kr](mailto:admin@099.kr)

*극단적인 저사양 리소스 환경에서도 즉각 작동하는 고효율 다국어 모델 아키텍처를 설계하고, 데이터 정제부터 학습·서빙까지 전 과정을 직접 구현하는 AI 엔지니어입니다. 기술 도입, 채용 제안 및 협업에 관심 있는 기업과 팀의 문의를 환영합니다.*