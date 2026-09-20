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
- baar1
- 150m
- multilingual
- text-generation
- lightweight
license: other
license_name: non-commercial-only
license_link: LICENSE
---

# BAAR1-150M

**BAAR1-150M** is a lightweight multilingual language model designed for fast, resource-efficient inference across 11 languages. Optimized for low latency and minimal compute environments, it enables responsive real-time generation on edge devices and standard cloud GPUs.

**BAAR1-150M**은 11개 언어를 지원하는 초경량 다국어 언어 모델입니다. 저사양 하드웨어 및 리소스 제약 환경에서도 빠르고 안정적인 동작이 가능하도록 경량화되어, 실시간 텍스트 생성 환경에 최적화되어 있습니다.

> ⚠️ **Experimental Test Release / 실험적 테스트 모델**  
> This checkpoint is an **experimental test build (Proof-of-Concept)** released strictly for latency evaluation, research, and multilingual inference testing. Outputs may exhibit incomplete phrasing or factual errors and are not intended for production deployments.  
> 본 가중치는 다국어 추론 지연 시간 검증 및 기술 실증을 위한 실험용 테스트 체크포인트(PoC)입니다. 프로토타입 단계이므로 사실 관계 왜곡이나 문장 미완성이 발생할 수 있으며, 상용 배포용이 아닌 연구 및 성능 검증 목적으로 공개되었습니다.

---

## 📊 Live Sample Inference (11개국 실시간 추론 테스트 결과)

*Hardware: Single NVIDIA Tesla T4 | FP16 Inference*

| Language | Prompt | Generated Output | Latency |
| :--- | :--- | :--- | :--- |
| **KO** (Korean) | 넌 누구니? | `AI로서 나는 물리적인 존재이며, 제가 할 수 있는 일은` | ~614.5ms |
| **EN** (English) | What is artificial intelligence? | `Artificial intelligence, often abbreviated as AI` | ~687.4ms |
| **JA** (Japanese) | 日本の首都はどこですか？ | `日本の首見ることは東京ですが約 20 , 587 km` | ~702.8ms |
| **ZH** (Chinese) | 人工智能的主要特点是什么？ | `人人的主要思想是理解和解释人类语言和行为的能力` | ~782.3ms |
| **ES** (Spanish) | ¿Cuál es la capital de España? | `La capital del España, también conocida como la capital de` | ~511.2ms |
| **PT** (Portuguese) | Qual é a capital do Brasil? | `A capital do Brasil, também conocida como Canciller, é` | ~513.1ms |
| **DE** (German) | Was ist künstliche Intelligenz? | `Künstliche Intelligenz, auch bekannt` | ~521.5ms |
| **RU** (Russian) | Какая столица России? | `Столица России, штат Калифорния, является` | ~522.0ms |
| **HI** (Hindi) | भारत की राजधानी क्या है? | `भारत, जनमंद और बढसे संबंधित है, एक देश जो अपने इतिहास` | ~518.2ms |
| **VI** (Vietnamese) | Thủ đô của Việt Nam là gì? | `Việt Nam, còn được gọi là Chiến tranh Tây` | ~536.6ms |
| **TH** (Thai) | เมืองหลวงของประเทศไทยคืออะไร? | `เมืองที่มีชีวิตชลีของประเทศคือโตเกียว` | ~343.6ms |

---

## 📄 License & Commercial Terms (라이선스 및 상업적 이용 안내)

- **Non-Commercial Use Only (비상업적 연구·개인 이용 한정)**:  
  This model is strictly available for **non-commercial, educational, and research purposes only**. Any form of monetization (direct or indirect) without an explicit commercial license is strictly prohibited.  
  본 모델은 **순수 연구, 교육 및 개인 비영리 목적에 한해 무료로 사용**할 수 있습니다. 사전 허가 없는 일체의 수익 창출 행위(직·간접적 상업적 이용)는 엄격히 금지됩니다.

- **Monetization & Commercial Licensing Inquiries (수익 창출 및 상용 라이선스 문의)**:  
  If you wish to **monetize, integrate this model into commercial products, provide paid services/APIs, or require enterprise-level support**, you must obtain a separate commercial license. Please reach out via email for licensing terms and enterprise adoption.  
  본 모델을 활용하여 **수익을 창출하고자 하거나, 상용 서비스/유료 제품에 탑재, 또는 기업용 맞춤 적용 및 기술 지원이 필요한 경우** 반드시 별도의 상용 라이선스를 취득하셔야 합니다. 도입 및 라이선스 발급은 아래 이메일로 문의해 주시기 바랍니다.
  - **Commercial Inquiries (상용 라이선스 문의)**: [admin@099.kr](mailto:admin@099.kr)

---

## ⚠️ Notes (안내 사항)

- **Pre-trained Model**: This model is a base pre-trained checkpoint. For specific tasks, factual alignment, or structured dialogue, task-specific fine-tuning (SFT) or Retrieval-Augmented Generation (RAG) is recommended.
- **기초 사전학습 모델**: 본 가중치는 사전학습 단계의 베이스 모델입니다. 특정 도메인 작업, 사실 관계 검증 및 정교한 대화 생성이 필요한 경우 파인튜닝(SFT) 또는 검색 증강 생성(RAG) 파이프라인과의 연계를 권장합니다.

---

## 💼 Opportunities & Contact (채용 제안 및 투자 문의)

This project demonstrates practical competency in custom model architecture design, end-to-end distributed training optimization, and efficient multi-language serving under compute constraints.

I am actively seeking **AI Engineering / Research opportunities, team recruitment offers, and project investment/partnerships**.

- **Model Adoption & Licensing (도입 및 라이선스 문의)**: [admin@099.kr](mailto:admin@099.kr)
- **Recruitment & Hiring Inquiries (채용 및 포지션 제안)**: [admin@099.kr](mailto:admin@099.kr)
- **Investment & Technical Collaboration (투자, 파트너십 및 기술 협업)**: [admin@099.kr](mailto:admin@099.kr)

*제한된 하드웨어 리소스 환경에서 고효율 다국어 모델 아키텍처를 직접 설계하고 훈련 파이프라인을 엔드투엔드로 구축할 수 있는 AI 엔지니어입니다. 저의 기술적 역량 영입(채용)이나 프로젝트 협업/투자에 관심이 있으신 기업 및 팀의 연락을 기다립니다.*