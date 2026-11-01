---
license: cc-by-4.0
language:
- ko
task_categories:
- text-generation
tags:
- accounting
- k-ifrs
- journal-entry
- finance
- chain-of-thought
- korean
- synthetic
size_categories:
- 1K<n<10K
pretty_name: K-IFRS Journal Entries (CoT, 3000)
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
---

# K-IFRS 분개 생성 데이터셋 (CoT, 3000건)

한국 회계기준(K-IFRS) 거래를 입력받아 **계산 과정(Chain-of-Thought) + 복식부기 분개(JSON)** 를 생성하도록 학습시키기 위한 한국어 합성 데이터셋입니다. 로컬 소형 언어모델(Qwen2.5-Coder-7B)의 LoRA 파인튜닝 연구에 사용되었습니다.

## 구성

| split | 건수 |
|-------|------|
| train | 2,700 |
| test  | 300 |
| **합계** | **3,000** |

## 포맷

Alpaca 스타일의 `instruction` / `input` / `output` 3개 필드.

- **instruction**: 분개 생성 지시 (한국어 계정과목, 차·대변 양수, 합계 일치 요구)
- **input**: 거래 조건 (액면·이자율·만기·취득원가 등 계산에 필요한 수치)
- **output**: `[계산]` 단계별 산식 + `[분개]` JSON (`{"차변": [...], "대변": [...]}`)

### 예시 (output)

```
[계산]
1) 감가상각대상금액 = 취득원가 63,800,000 − 잔존가치 0 = 63,800,000원
2) 연 감가상각비 = 63,800,000 ÷ 내용연수 5년 = 12,760,000원

[분개]
{"차변": [{"계정": "감가상각비", "금액": 12760000}], "대변": [{"계정": "감가상각누계액", "금액": 12760000}]}
```

## 거래 유형 (4종, 모두 계산 필요)

1. **사채 할인발행** — 유효이자율법 현재가치
2. **유형자산 감가상각** — 정액법
3. **금융자산 FVPL 평가** — 공정가치 변동
4. **리스 최초인식** — 리스료 연금현가

## 생성 방법

LLM이 계산을 틀리는 문제를 피하기 위해 **회계 공식을 파이썬 코드에 내장**하여 정답(label)을 결정론적으로 생성했습니다. 금액·이자율·만기를 무작위로 변형하되 계산은 파이썬이 수행하므로 label은 항상 정확하며, 전 건이 **차변 합 = 대변 합**을 만족하도록 자동 검증했습니다.

## 활용 및 한계

- 이 데이터로 LoRA 파인튜닝 시 **형식·계정과목 정확도는 0% → 100%** 로 학습되지만, **금액 계산 정확도는 52~55%에서 천장**에 부딪힙니다. 특히 현재가치 같은 다단계 계산은 모델이 산술 자체를 틀립니다.
- 따라서 정확한 회계 자동화에는 **결정론적 계산 모듈 + LLM 구조 생성의 하이브리드**가 필요하다는 점을 정량적으로 보여주는 연구용 데이터셋입니다.

## 인용 / 참고문헌

본 데이터셋은 다음 선행 연구를 한국어·계산 직면 설정으로 확장한 연구의 일부입니다.

> Zupan, M. (2025). *Developing an Accounting Virtual Assistant Through Supervised Fine-Tuning (SFT) of a Small Language Model (SLM).* Intelligent Systems in Accounting, Finance and Management.

## 라이선스

[CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/) — 출처를 표시하면 자유롭게 사용·재배포할 수 있습니다.
