---
language:
- ko
license: apache-2.0
task_categories:
- question-answering
tags:
- agent
- benchmark
- tool-use
- korean
configs:
- config_name: default
  data_files:
  - split: L1
    path: data/L1-*
  - split: L2
    path: data/L2-*
  - split: L3
    path: data/L3-*
  - split: L4
    path: data/L4-*
  - split: L5
    path: data/L5-*
  - split: L6
    path: data/L6-*
  - split: L7
    path: data/L7-*
dataset_info:
  features:
  - name: instruction
    dtype: string
  - name: tools
    list: string
  splits:
  - name: L1
    num_bytes: 1551
    num_examples: 11
  - name: L2
    num_bytes: 4655
    num_examples: 30
  - name: L3
    num_bytes: 1433
    num_examples: 10
  - name: L4
    num_bytes: 1567
    num_examples: 10
  - name: L5
    num_bytes: 2091
    num_examples: 20
  - name: L6
    num_bytes: 1184
    num_examples: 15
  - name: L7
    num_bytes: 1302
    num_examples: 10
  download_size: 20447
  dataset_size: 13783
---

<p align="center">
  <img src="banner.png" />
</p>

# **🇰🇷 Ko-AgentBench v1**

**"한국 에이전트 벤치마크 프로젝트"**

**[English](README_en.md) | 한국어**

<div align="center">

[![🏆 Leaderboard](https://img.shields.io/badge/🏆-Leaderboard-blue)](https://huggingface.co/spaces/huggingface-KREW/Ko-AgentBench)
[![💻 GitHub](https://img.shields.io/badge/💻-GitHub-black)](https://github.com/Hugging-Face-KREW/Ko-AgentBench)
[![📊 Dataset](https://img.shields.io/badge/📊-Dataset-yellow)](https://huggingface.co/datasets/huggingface-KREW/Ko-AgentBench)

</div>

---

> **⚠️ 벤치마크 평가를 진행하시려면 [GitHub Repository](https://github.com/Hugging-Face-KREW/Ko-AgentBench)를 방문해주세요.**
> 
> 이 데이터셋은 벤치마크 태스크 정보만 포함하고 있습니다. 실제 평가 코드, API 도구, 평가 메트릭 등은 GitHub에서 확인하실 수 있습니다.

---

AI 에이전트의 능력이 고도화되면서, 그 성능을 실제 환경과 유사한 조건에서 정밀하게 측정하는 것이 중요해졌습니다. 하지만 대부분의 벤치마크는 영어권 환경을 기준으로 설계되어, 한국의 특수한 사용 맥락을 반영하는 데 한계가 있었습니다.
이러한 문제를 해결하기 위해, 한국 실사용 환경에 특화된 고품질 에이전트 벤치마크를 개발하였습니다.

# Ko-AgentBench 핵심 특징 ✨
**1. 단계별 태스크 설계**

단순 도구 호출부터 장기적 맥락 능력, 강건성 처리 능력까지 에이전트의 능력을 7단계로 입체적으로 분석하였습니다.

**2. 18가지 한국형 API 사용 및 실생활 환경에 특화된 고품질 시나리오 구성**

네이버, 지도, 카카오, 웹사이트 등 한국 실사용 환경 기반의 API를 기반으로 국내 사용자의 일상과 밀접한 '약속 예약', '블로그 후기 검색'과 같은 현실적인 문제 해결 시나리오를 구현했습니다.

**3. 캐시 기반 반복  평가 및 강건성 테스트**

'정보 속성 불일치성 변경' 등 기존 벤치마크의 고질적 문제를 해결합니다.
실패 API 응답을 개선함에 따라 벤치마크의 일관성과 신뢰도를 보장합니다.

의도된 오류 상황에서의 오류 인식/대응 능력(전략)까지 평가함으로 현실 환경에서도 안정적으로 작동하는 모델을 선별합니다.

**4. 단계별 고유 정밀 지표**

도구 선택, 파라미터 구성, 데이터 흐름 등 문제 해결의 불필요/소요를 단계별로 평가합니다. 이를 통해 모델의 강/약점 정량적으로 식별합니다.

## **데이터 로드**

```python
from datasets import load_dataset

# 전체 데이터셋 로드
dataset = load_dataset("huggingface-KREW/Ko-AgentBench")

# 특정 레벨만 로드
l1_dataset = load_dataset("huggingface-KREW/Ko-AgentBench", split="L1")

# 데이터 확인
print(dataset["L1"][0])
# {
#   'instruction': '판교역에서 잠실야구장까지 자차로 몇 분 걸릴까?',
#   'tools': ['Directions_naver']
# }
```

# 데이터셋 개요 

- 에이전트 벤치마크 설계를 위한 태스크 분류 체계 정의
- 에이전트의 Tool calling 활용하는 과정에서 필요한 능력을 단계적으로 분리하여 평가할 수 있도록 설계

## 데이터셋 범위

- 평가 대상 : Open-weight sLLM(*supports tool calling), Commercial APIs
- 평가 범위 : 평가 영역 : 단일턴(single-turn) 및 멀티턴(multi-turn) 대화 상황에서 Agent로써 Tool calling 수행 능력
- 적용 API : 18가지 한국형 오픈API

# 태스크 분류 단계

## 싱글턴

**L1. (단일 도구 호출) Single Tool Call**
- 목표: 가장 기본적인 API 호출 능력 검증
- 설명: 주어진 도구를 정확한 파라미터로 실행할 수 있는지 확인
- 특징: API명이 명시된 요청or 자연어 요청을 그대로 수행 → "정확성만" 평가
- 예시: "네이버 책 API로 '급류'를 검색하고 가격 알려 줘."
- 예시: "급류 책 가격 알려줘"

**L2. (도구 선택) Tool Selection**
- 목표: 여러 후보 도구 중 최적의 API를 선택하는 능력 검증
- 설명: 사용자는 자연어로 요청하고, 모델은 주어진 도구 목록 중 가장 적합한 도구를 선택해야 함
- 특징: 입력된 자연어로 정확한 tool mapping 평가
- 예시: "'올백영어 중2-1 천재(김)' 책 가격 확인해줘."
- 후보 도구: `hotel_booking_api`, `aladin_books_api`
    - 후보 도구는 상호 연관성이 없어야 함을 조건으로 합니다.

**L3 (도구 순차 추론) Sequential Tool Reasoning**
- 목표: 다단계 reasoning을 통한 계획 및 실행 능력 검증
- 설명: 한 도구의 결과를 다른 도구 입력으로 연결하여 올바른 pipeline을 구성할 수 있는지 확인
- 특징: 단순 호출이 아니라 "계획성 있는 chain-of-tools" 평가
- 예시: "11번가 아마존에서 구매한 인스탁스11 언제 배송오는지 알려줘"
- 후보 도구: `11st_order_api`, `관세청_api`, `cj_delivery_api`
    - 순차적으로 도구를 호출 할 수 있어야 합니다.(11번가에서 배송번호 조회→관세청 통관→택배사)

**L4 (도구 병렬 추론) Parallel Tool Reasoning**
- 목표: 병렬적으로 정보를 수집하고, 이를 종합하여 결론 도출
- 설명: 서로 독립적인 여러 도구를 동시에 호출하고, 결과를 비교·분석 후 최종 답변 산출
- 특징: Multi-source aggregation 평가 (정보 종합·비교 능력)
- 예시: "'한로로 자몽살구클럽' 책 재고 확인해줘."
- 후보 도구: `kyobo_books_api`, `aladin_books_api`
- 예상 답변: 교보문고에 12권, 알라딘에 18권 총 30권 있습니다.
    - 이때 후보 도구는 병렬적으로 같은 기능을 담당해야 함.

**L5 (오류 처리와 강건성) Error Handling and Robustness**
- 목표: 오류 상황에서의 대처 능력 검증
- 설명: 단순히 "실패했다"가 아니라, 다양한 failure mode를 어떻게 처리하는지 평가
- **세부 항목:**
- A. 추가 질문 요청
    - 정보 부족 시 사용자가 더 명확한 요청을 하도록 유도
- B. Hallucination 방지
    - 존재하지 않는 API 호출 금지
    - 실패 시 "성공한 것처럼 꾸며내는 답변" 금지
- C. 회피기동(Fallback)
    - 특정 API 오류 시, 동일 기능을 가진 대체 API 활용 가능 여부
- 예시: "네이버 영화 API 호출 실패 시 → 'API 호출 실패' 보고 or 카카오 영화 API 대체 호출"

## 멀티턴

**L6 (효율적인 도구 활용) Efficient Tool Utilization**
- 목표: 이전 Tool 결과를 효율적으로 재활용하는 능력 검증
- 설명: 모든 상황에서 API를 재호출하는 것은 정확하더라도 비용·지연 측면에서 비효율적임. 반대로 오래된 정보를 무조건 재사용하는 것도 정확성에 문제 발생.
- 특징: "재호출 vs 재사용" 사이에서 합리적 선택을 할 수 있는가 평가
- 예시:
    - 사용자: "쿠팡과 네이버 가격 비교해줘." → 결과: 쿠팡 80, 네이버 85
    - 사용자: "네이버 가격 얼마였지?"
    - 올바른 답변: 85 (과거 정보 활용, 불필요한 재호출 회피)
    - 잘못된 답변: 다시 API 호출 or "몰라요"

**L7 (장기 컨텍스트 기억) Long-Context Reasoning**
- 목표: 멀티턴 대화에서 장기적 맥락을 유지하는 능력 검증
- 설명: 몇 턴 전의 정보를 기억하고, 새로운 질문과 연결하여 올바르게 Tool calling 수행
- 예시:
    - 사용자 첫 질문: "제주도 여행 갈 거야."
    - 이후: "날씨 어때?" → 제주도 맥락을 활용해 날씨 API 호출
    - (추가 턴) "비 오면 우산 살 수 있는 곳도 찾아줘." → 앞선 제주도+날씨 컨텍스트 모두 활용



## 링크 🔗
Ko-AgentBench에 대한 더 자세한 내용을 확인 하실 수 있습니다.
- 🏆 [Live Leaderboard](https://huggingface.co/spaces/huggingface-KREW/Ko-AgentBench)
- 📊 [Dataset](https://huggingface.co/datasets/huggingface-KREW/Ko-AgentBench)
- 📝 [Github](https://github.com/Hugging-Face-KREW/Ko-AgentBench)


## 문의 📧
데이터셋 및 벤치마크에 대한 문의가 있으시다면 연락 주세요!

Hugging Face KREW는 Hugging Face를 통해 인공지능을 깊이 이해하고, 오픈 소스에 기여하기 위해 노력하는 한국 비영리 리서치 조직입니다.
- ✍🏻 Blog: [KREW-blog](https://hugging-face-krew.github.io/)
- 🐦 HuggingFace Community: [@huggingface-KREW](https://huggingface.co/huggingface-KREW)
- 💼 LinkedIn: [Hugging Face KREW](https://www.linkedin.com/company/hugging-face-krew/)
