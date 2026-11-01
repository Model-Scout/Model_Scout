---
license: apache-2.0
language: [ko, en]
tags: [llm0to1, reproducibility, manifest, pretraining]
pretty_name: "LLM0to1 Reproducibility Manifest"
---

# LLM0to1 재현 매니페스트

**LLM0to1-10b** — 10B 규모 한/영 이중언어 LLM 을 바닥부터(from scratch) 학습한 프로젝트의
**데이터 계보 전체**를 담은 메타데이터. 이 파일 하나로 어떤 코퍼스가 어디서 왔고 얼마나 쓰였는지,
그리고 무엇이 어느 저장소에 공개되어 있는지 추적할 수 있다.

## 이 저장소가 필요한 이유

사전학습 데이터는 **116개 코퍼스 / 419B 토큰**이다. 전부를 그대로 재배포하는 것은 (a) 용량,
(b) 원본 라이선스(AI-Hub 약관·국립국어원·상업 도서) 때문에 불가능하다.
그래서 **"무엇을 어디서 얼마나 가져와 어떻게 정제했는지"** 를 기록으로 남기고,
재배포가 가능한 것은 실제 데이터까지 공개하는 방식을 택했다.

## 수록 내용 (`manifest.json`)

```
pretrain
  ├ model / tokenizer / corpora_count / total_tokens_B
  ├ data_stages[]        학습 커리큘럼(단계별 시작 스텝)
  └ corpora{}            코퍼스 116종. 각 항목:
       tokens_B          토큰 수(10억 단위)
       source            공개 원본 데이터셋 ID 또는 출처
       prep_script       전처리에 쓴 스크립트 파일명
       hf_repo           공개된 우리 파생본 경로(있으면)
       note              라이선스·주의사항
posttrain
  └ base_model / sft_mix / framework
```

## 코퍼스 요약

전체 **116종 / 418.6B 토큰**.
그중 **66종 / 214.9B** 는 정제 텍스트가 이미 공개되어 있고,
나머지 **50종 / 203.7B** 는 토큰화본으로 공개했다(아래).

| 분류 | 코퍼스 수 | 토큰 | 텍스트 공개 |
|---|---|---|---|
| 영어 | 32 | 261.8B | 2/32 |
| 코드 | 27 | 59.1B | 9/27 |
| 한국어 | 6 | 48.7B | 6/6 |
| 수학 | 3 | 30.5B | 1/3 |
| AI-Hub | 48 | 18.4B | 48/48 |

## 관련 저장소

| 저장소 | 내용 |
|---|---|
| `izlley2/llm0to1-tokenizer` | 토크나이저(byte-level BPE, vocab 160k) — `.ds` 복호화에 필요 |
| `izlley2/llm0to1-pt-tokenized-code` | 코드 코퍼스 토큰화본 |
| `izlley2/llm0to1-pt-tokenized-math` | 수학 코퍼스 토큰화본 |
| `izlley2/llm0to1-pt-tokenized-en-edu-2025` | 영어 교육 코퍼스(2025 덤프) 토큰화본 |
| `izlley2/llm0to1-pt-tokenized-en-misc` | 영어 기타 토큰화본 |
| `izlley2/LLM0to1-10b-step20000` / `-step83000` | 사전학습 체크포인트(HF 포맷) |
| `izlley2/LLM0to1-10b-step20000-nanotron` / `-step83000-nanotron` | 같은 체크포인트(nanotron 포맷, 학습 재개용) |

## 사후학습(post-training)

사전학습 모델과 별개로, 공개 base 모델(`Qwen/Qwen3.5-9B-Base`)을 이용한 한국어 채팅 모델 실험도
같은 프로젝트에서 진행했다. SFT 혼합 데이터의 구성·필터·오염감사 결과는 해당 데이터셋 카드에 있다.

## 라이선스 주의

`corpora[].note` 를 반드시 확인할 것. 특히:
- **국립국어원 모두의 말뭉치** 계열: 재배포 불가(학습 사용만 허용)
- **AI-Hub** 계열: AI-Hub 이용약관 적용, 재배포 제한
- **상업 전자책** 파생: 공개 부적절

이 매니페스트 자체(메타데이터)는 apache-2.0 이다.
