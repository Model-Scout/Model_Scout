---
license: cc-by-sa-4.0
language:
- ko
tags:
- 질의응답,
- 시간민감형질의응답,
- 검색증강생성,
- RAG,
- QA,
pretty_name: 한국어 시간민감형 질의응답(KoTSQA)
size_categories:
- 1K<n<10K
---


# Dataset Card for Dataset Name
한국어 시간민감형 질의응답 데이터 (Korean Time-Sensitive Q&A Dataset: KoTSQA)
- Copyright (C) 2025~ ETRI LIRS.
- koTSQA 데이터셋의 Split Version. train/validation 등의 용도로 사용하게 하고, test 6,750개, train 750 (강화학습에 활용)임

## Dataset Details
![유형정보](https://cdn-uploads.huggingface.co/production/uploads/63c897bd15c7abaf680c1572/CBB8WJN-k5_OXtE3z_rVT.png)

Train Part
- Stats - Unchanged: 243(0.3240), changed: 264(0.3520), new: 243(0.3240),
- Stats w/o false-premise - Unchanged: 181(0.3285), changed: 194(0.3521), new: 176(0.3194),
- Stats of false-premise - Unchanged: 62(0.3116), changed: 70(0.3518), new: 67(0.3367),  
   
Test Part
- Stats - Unchanged: 2007(0.2973), changed: 2736(0.4053), new: 2007(0.2973),
- Stats w/o false-premise: Unchanged - 1489(0.3010), changed: 2016(0.4075), new: 1442(0.2915),
- Stats of false-premise: Unchanged - 518(0.2873), changed: 720(0.3993), new: 565(0.3134) 

### Dataset Description
LLM의 데이터 오염에 자유롭고, LLM의 내재지식과 외부지식의 지식충돌 문제를 평가할 수 있는 KoTSQA(Korean Time-Sensitive Q&A) 벤치마크

- **Curated by:** [한국전자통신연구원 언어지능연구실, 마인즈 솔루션]
- **Funded by [optional]:** [2024년도 정부(과학기술정보통신부)의 재원으로 정보통신기획평가원의 지원(No. RS-2024-00338140, 생성형 언어모델의 지속 가능성과 시간의 흐름에 따른 최신성 반영을 위한 학습 및 활용 기술 개발)을 받아 수행된 연구]
- **Language(s) (NLP):** [한국어]
- **License:** [CC BY-SA 4.0]

### Dataset Sources [optional]
- **Paper [optional]:** [KoTSQA: LLM에 자유로운 시간 민감형 질의응답 벤치마크(KCC 2025), 최신지식에 대한 응답성능 개선을 위한 Recursive RAG(KCC 2026)]

## Dataset Structure
- id: 질의응답 데이터셋의 ID
- question: 질문
- ansewrs: 정답목록
- passages: 정답근거 단락들(4개의 단락에서 질문을 생성함)
- fact_type: 지식의 유형(unchanged, changed, new)
- q_type: 질문의 유형(single-hop, multi-hop, false-premise)

ID의 구성체계
- 숫자_f - wikipedia에 기반한 factoid QA로 single-hop 질문,
- 숫자_c - wikipedia에 기반한 factoid QA로 multi-hop, false-premise 질문,
- 숫자_h - wikipedia와 가상의 단락에 기반한 질문(single-hop의 경우, 가상의 단락에 정답이 있음.)

![통계정보](https://cdn-uploads.huggingface.co/production/uploads/63c897bd15c7abaf680c1572/iyiR7bimHHBikMhnUF8Oj.png)
  
## Dataset Creation

### Curation Rationale
초거대언어모델(large language model)은 학습에 사용된 말뭉치(corpus)로부터 많은 지식(knowledge)을 파라미터(parameter)에 저장하고, 
이에 기반하여 지식기반 태스크(knowledge-sensitive tasks)에서 훌륭한 추론능력(inference ability)을 보여왔다. 
그러나, LLM이 학습된 이후(cutoff dates 이후)의 지식은 파라미터에 저장할 수가 없다. 이와 같은 문제를 해결하기 위해, 검색증강생성(retrieval-augmented generation), 지식편집(knowledge editing), 연속학습(continual learning) 등의 기술들이 소개되었고, 
특히 검색증강생성 기술이 가장 각광받는 기술로 발전하고 있다. 그러나, 검색증강생성에서 파라미터에 내재된 지식(parametric knowledge)과 검색된 외부지식(nonparmetric knowledge, external knowledge)간의 지식충돌에 대해서 객관적으로 평가가 가능한 벤치마크가 부재하다.
최근에 많이 공개되고 있는 시간 민감형 질의응답(time-sensitive Q&A) 벤치마크의 경우에도 대부분 영어이고, LLM의 데이터 오염(data-contamination)에 자유롭지 않다. 
그래서 LLM의 데이터 오염에 자유롭고, LLM의 내재지식과 외부지식의 지식충돌 문제를 평가할 수 있는 KoTSQA(Korean Time-Sensitive Q&A) 벤치마크를 구축하였다.

### Source Data
한국어 위키피디아 사전에 기반하여 벤치마크를 구성함.

#### Data Collection and Processing
![구축방법](https://cdn-uploads.huggingface.co/production/uploads/63c897bd15c7abaf680c1572/weGvqe3P3ih5pcB6k457s.png)

## Citation [optional]
- KoTSQA: LLM에 자유로운 시간 민감형 질의응답 벤치마크(KCC 2025) [논문보기](KCC2025.pdf)
- 최신지식에 대한 응답성능 개선을 위한 Recursive RAG(KCC 2026) [논문보기](KCC2026.pdf) [발표자료보기](KCC2026_Poster.pdf)

## Dataset Card Contact

한국전자통신연구원 언어지능연구실 허정(jeonghur@etri.re.kr)