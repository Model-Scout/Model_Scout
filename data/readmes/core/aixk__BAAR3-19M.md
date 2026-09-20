---
pipeline_tag: text-generation
language:
- de
- en
- es
- fr
- ja
- ko
- zh
- it
- nl
- pl
- pt
- ru
- ar
- bg
- el
- hi
- sw
- th
- tr
- vi
tags:
- baar3
- 19m
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

<h1 align="center">BAAR3-19M</h1>

<p align="center">
  🌐 <b>Official Website:</b> <a href="https://baar.uk/model/">https://baar.uk/model/</a></br>
  📄 <b>License:</b> Non-Commercial Only (Contact for Commercial Pricing)
</p>

---

## 📌 Model Overview

**BAAR3-19M** is an ultra-compact multilingual conversational model designed to enable real-time interactive generation under minimal hardware constraints. Scaling to **19 million (19M) parameters**, it expands multi-language dialogue capabilities across **20 languages**: German (de), English (en), Spanish (es), French (fr), Japanese (ja), Korean (ko), Chinese (zh), Italian (it), Dutch (nl), Polish (pl), Portuguese (pt), Russian (ru), Arabic (ar), Bulgarian (bg), Greek (el), Hindi (hi), Swahili (sw), Thai (th), Turkish (tr), and Vietnamese (vi).

**BAAR3-19M**은 극단적인 하드웨어 제약 환경에서도 **20개 다국어**로 실시간 대화(Chat)가 가능하도록 설계된 1,900만(19M) 파라미터 규모의 초경량 언어 모델입니다. 일반 LLM 구동이 불가능한 초저사양 엣지 기기, 임베디드 장비, 온디바이스 환경에서 즉각적인 추론과 초경량 실시간 RAG 파이프라인 구축을 지원합니다.

- **지원 언어 (20 Languages)**: 한국어(ko), 영어(en), 일본어(ja), 중국어(zh), 스페인어(es), 프랑스어(fr), 독일어(de), 이탈리아어(it), 네덜란드어(nl), 폴란드어(pl), 포르투갈어(pt), 러시아어(ru), 아랍어(ar), 불가리아어(bg), 그리스어(el), 힌디어(hi), 스와힐리어(sw), 태국어(th), 튀르키예어(tr), 베트남어(vi)

---

## 📊 Live Sample Inference

*Hardware: Single NVIDIA Tesla T4 | FP16 Inference*

| Task / Category | Prompt (질문) | Generated Output (생성 답변) | Latency |
| :--- | :--- | :--- | :--- |
| **한국어 일반 QA** | 대한민국의 수도는 어디인가요? | `대한민국의 수도는 여러 가지 이유로 간주되며 여러` | ~368.5ms |
| **영어 일반 QA** | What is artificial intelligence? | `Artificial intelligence is a type of artificial` | ~334.3ms |
| **일본어 일반 QA** | 日本の首都はどこですか？ | `日本の首都は、 多くの場合、` | ~338.1ms |
| **중국어 일반 QA** | 人工智能的主要特点是什么？ | `人工智能的主要特点是 ， 它涉及使用` | ~332.8ms |
| **스페인어 일반 QA** | ¿Cuál es la capital de España? | `España is la capital de España and is un prin` | ~327.8ms |
| **프랑스어 일반 QA** | Quelle est la capitale de la France ? | `La capitalise de la France is the capital of` | ~331.8ms |
| **독일어 일반 QA** | Was ist die Hauptstadt von Deutschland? | `Hauptstadt von Deutschland is a metaphor of the` | ~352.5ms |
| **이탈리아어 일반 QA** | Qual è la capitale d'Italia? | `La capjetale d'Italjea est la capjetale de l'Amé` | ~332.2ms |
| **러시아어 일반 QA** | Какая столица России? | `Россия — это столица в конце 1970 года и` | ~355.1ms |
| **아랍어 일반 QA** | ما هي عاصمة مصر؟ | `عاصمة مصر هي عاصمة مصر هي عاصمة مصر هي عاصم` | ~335.1ms |
| **그리스어 일반 QA** | Ποια είναι η πρωτεύουσα της Ελλάδας; | `Η ελληνική πρωτεύουσα της Ελλάδας είναι μια` | ~344.7ms |
| **튀르키예어 일반 QA** | Türkiye'nin başkenti neresidir? | `Türkbenye'nin başkentben neresbendir. Başkentben ne` | ~350.9ms |
| **폴란드어 일반 QA** | Co jest stolicą Polski? | `Sdolicą Polski jest sdolicą polskiego w postaci` | ~339.4ms |
| **힌디어 일반 QA** | भारत की राजधानी क्या है? | `भारत की राजधानी क्या है, और इसका उपयोग किसी` | ~315.6ms |
| **태국어 일반 QA** | เมืองหลวงของประเทศไทยคืออะไร? | `เมืองหลวง ของ ประเทศ ไทย คือ เมือง ที่ มี ประชากร สูง ประเทศ ไทย` | ~336.1ms |
| **베트남어 일반 QA** | Thủ đô của Việt Nam là gì? | `Thủ đô cổ Vjeệt Nam là gì est le principal domaine de l'` | ~331.2ms |
| **일상어 번역 요청** | 안녕이 영어로 뭐야? | `안녕은 영어로 Hello 입니다.` | ~240.9ms |
| **일상어 번역 요청 2** | 사과가 프랑스어로 뭐야? | `사과는 프랑스어로 pomme 입니다.` | ~256.8ms |

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
- **기초 사전학습 모델**: 본 모델은 19M 규모의 베이스 사전학습 체크포인트입니다. 정교한 작업 수행, 사실 관계 검증 및 완성도 높은 대화 생성이 필요한 경우 도메인 파인튜닝(SFT) 또는 검색 증강 생성(RAG) 파이프라인 결합을 권장합니다.

---

## 💼 Opportunities & Contact (채용 제안 및 투자 문의)

This project demonstrates practical competency in designing custom micro-scale architectures, end-to-end multi-language pre-training, and ultra-low-latency deployment under extreme compute constraints.

I am actively seeking **AI Engineering / Research opportunities, recruitment offers, and technical partnerships**.

- **공식 웹사이트 (Official Website)**: [https://baar.uk/model/](https://baar.uk/model/)
- **기업 도입 및 라이선스 문의 (Commercial Adoption)**: [admin@099.kr](mailto:admin@099.kr)
- **채용 및 포지션 제안 (Recruitment & Hiring)**: [admin@099.kr](mailto:admin@099.kr)
- **투자 및 기술 협력 문의 (Investment & Partnerships)**: [admin@099.kr](mailto:admin@099.kr)

*극단적인 저사양 리소스 환경에서도 즉각 작동하는 고효율 다국어 모델 아키텍처를 설계하고, 데이터 정제부터 학습·서빙까지 전 과정을 직접 구현하는 AI 엔지니어입니다. 기술 도입, 채용 제안 및 협업에 관심 있는 기업과 팀의 문의를 환영합니다.*