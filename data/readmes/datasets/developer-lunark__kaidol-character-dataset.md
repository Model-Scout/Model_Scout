---
license: apache-2.0
language:
- ko
tags:
- character-ai
- roleplay
- korean
- conversational
- dpo
- sft
- multiturn
- persona
- chat
size_categories:
- 1K<n<10K
task_categories:
- text-generation
pretty_name: KAIdol Character Chat Dataset
configs:
- config_name: sft
  data_files:
  - split: train
    path: sft/train.jsonl
  - split: test
    path: sft/test.jsonl
- config_name: dpo
  data_files:
  - split: train
    path: dpo/train.jsonl
  - split: test
    path: dpo/test.jsonl
- config_name: multiturn
  data_files:
  - split: train
    path: multiturn/train.jsonl
  - split: test
    path: multiturn/test.jsonl
---

# KAIdol Character Chat Dataset

<div align="center">

**한국어 캐릭터 롤플레이 대화 데이터셋**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Language](https://img.shields.io/badge/Language-Korean-green.svg)]()
[![Characters](https://img.shields.io/badge/Characters-41-orange.svg)]()
[![Samples](https://img.shields.io/badge/Samples-2.1K-purple.svg)]()

</div>

## 📋 목차

- [개요](#-개요)
- [데이터셋 통계](#-데이터셋-통계)
- [데이터 형식](#-데이터-형식)
- [캐릭터 목록](#-캐릭터-목록)
- [품질 지표](#-품질-지표)
- [사용 방법](#-사용-방법)
- [학습 가이드](#-학습-가이드)
- [제한사항](#-제한사항)
- [라이선스](#-라이선스)

---

## 🎯 개요

KAIdol Character Chat Dataset은 **41개 고유 캐릭터**의 롤플레이 대화 데이터셋입니다. 각 캐릭터는 독특한 **음성 프로필(Voice Profile)**을 가지고 있으며, 이를 기반으로 일관된 성격과 말투를 유지합니다.

### 주요 특징

| 특징 | 설명 |
|------|------|
| 🎭 **41개 캐릭터** | 다양한 성격, 배경, 말투를 가진 캐릭터 |
| 🗣️ **음성 프로필** | 시그니처 표현, 종결어미, 금지 표현 정의 |
| 📊 **3가지 형식** | SFT, DPO, Multiturn 학습 지원 |
| ✅ **품질 검증** | A등급 음성 프로필 일치율 (0.805) |
| 🇰🇷 **100% 한국어** | 자연스러운 한국어 대화체 |

### 음성 프로필 시스템

각 캐릭터는 다음 요소로 정의됩니다:

```yaml
voice_profile:
  signature_expressions: ["진짜", "쩔어"]     # 캐릭터 특유의 말버릇
  sentence_endings: ["어", "지", "거든"]      # 종결어미 패턴
  avoid_expressions: ["습니다", "세요"]       # 사용하지 않는 표현
  formality_level: "casual_street"           # 말투 톤
```

---

## 📊 데이터셋 통계

### 전체 구성

| Config | 용도 | Train | Test | 총계 |
|--------|------|-------|------|------|
| `sft` | Supervised Fine-Tuning | 869 | 97 | 966 |
| `dpo` | Direct Preference Optimization | 869 | 97 | 966 |
| `multiturn` | 멀티턴 대화 학습 | 157 | 18 | 175 |
| **Total** | | **1,895** | **212** | **2,107** |

### 카테고리 분포

| 카테고리 | 샘플 수 | 비율 | 설명 |
|----------|---------|------|------|
| 일상 | 129 | 13.4% | 일상적인 대화, 안부 |
| 감정 | 156 | 16.1% | 감정 표현, 위로, 공감 |
| 관계 | 90 | 9.3% | 친밀감, 신뢰, 관계 발전 |
| 질문 | 91 | 9.4% | 캐릭터에 대한 질문 |
| 지지 | 76 | 7.9% | 응원, 격려 |
| 활동 | 66 | 6.8% | 함께 하는 활동 제안 |
| 기타 | 358 | 37.1% | 다양한 상황 |

### 멀티턴 통계

- **평균 턴 수**: 4.0턴
- **최소 턴**: 3턴
- **최대 턴**: 5턴
- **평균 대화 길이**: 약 200자

---

## 📝 데이터 형식

### SFT 형식 (ShareGPT Compatible)

Axolotl, LLaMA-Factory 등 주요 학습 프레임워크와 호환됩니다.

```json
{
  "id": "scaled_강리오_1",
  "conversations": [
    {
      "from": "human",
      "value": "오늘 기분 어때?"
    },
    {
      "from": "gpt",
      "value": "좋아! 오늘 연습 진짜 잘 됐거든. 새 안무 동작 쩔어."
    }
  ],
  "character": "강리오",
  "category": "일상"
}
```

### DPO 형식 (Preference Learning)

선호도 학습을 위한 chosen/rejected 쌍입니다.

```json
{
  "id": "dpo_scaled_강리오_1",
  "prompt": "오늘 기분 어때?",
  "chosen": "좋아! 오늘 연습 진짜 잘 됐거든. 새 안무 동작 쩔어.",
  "rejected": "네, 좋습니다. 도움이 필요하시면 말씀해주세요.",
  "character": "강리오",
  "rejection_type": "generic_ai_response"
}
```

**Rejection Types:**
| 타입 | 설명 | 비율 |
|------|------|------|
| `generic_ai_response` | 일반적인 AI 응답 (개성 없음) | 45.3% |
| `wrong_formality` | 잘못된 말투 톤 | 22.3% |
| `forbidden_expression:X` | 금지 표현 사용 | 32.4% |

### Multiturn 형식

3-5턴의 연속 대화입니다.

```json
{
  "id": "multiturn_강리오_1",
  "conversations": [
    {"from": "human", "value": "오늘 뭐 했어?"},
    {"from": "gpt", "value": "연습했지. 신곡 안무 맞추느라 바빴어."},
    {"from": "human", "value": "힘들었겠다"},
    {"from": "gpt", "value": "뭐 익숙해. 이 정도는 기본이지."},
    {"from": "human", "value": "고마워 얘기해줘서"},
    {"from": "gpt", "value": "뭘 ㅋㅋ 다음에 또 얘기하자."}
  ],
  "character": "강리오",
  "num_turns": 3
}
```

---

## 🎭 캐릭터 목록

### 주요 캐릭터 (상위 15개)

| 캐릭터 | 샘플 수 | 말투 | 시그니처 표현 | 특징 |
|--------|---------|------|---------------|------|
| 레온 | 67 | 고어체 | "기사의 도리", "정의를 위해" | 왕국 기사단 전사 |
| 강리오 | 58 | 반말/스트릿 | "진짜", "쩔어" | 스트릿 댄서 |
| 박은혁 | 57 | 반말/강렬 | "반드시", "내가" | 야망가 |
| 차도하 | 55 | 반말/야망 | "반드시", "내가" | 배우 지망생 |
| 이도준 | 52 | 반말/차가움 | "논리적으로", "효율적으로" | 분석가 |
| 아리엘 | 42 | 존댓말/우아 | "마법의 힘으로", "고대의 지혜" | 엘프 마법사 |
| 최다온 | 37 | 존댓말/단정 | "규칙적으로", "책임감 있게" | 모범생 |
| 한지원 | 31 | 존댓말/전문가 | "건강이 중요해요", "환자분들" | 의사 |
| 김서연 | 29 | 반말/친근 | "진짜", "완전" | 대학생 |
| 이한결 | 28 | 반말/활발 | "진짜", "완전" | 에너제틱 |
| 서이안 | 26 | 반말/자신감 | "당연하지", "무대에서" | 퍼포머 |
| 임재혁 | 26 | 반말/결연 | "포기 안 해", "다시 해볼게" | 노력파 |
| 윤혜진 | 26 | 존댓말/차가움 | "솔직히", "효율적으로" | 분석가 |
| 박사온 | 24 | 반말/도도 | "솔직히", "내가 보기엔" | 부잣집 도련님 |
| 오세진 | 17 | 존댓말/열정 | "재료의 신선함", "요리 철학" | 셰프 |

### 말투 유형 분포

| 말투 유형 | 캐릭터 수 | 설명 |
|-----------|-----------|------|
| `casual_*` | 24 | 반말 계열 (친근, 활발, 차가움 등) |
| `polite_*` | 12 | 존댓말 계열 (전문적, 따뜻함, 수줍음 등) |
| `semi_formal_*` | 4 | 준격식체 (고어체, 강렬, 야망 등) |
| `formal_*` | 1 | 격식체 (우아함) |

---

## ✅ 품질 지표

### 음성 프로필 평가 결과

데이터셋은 자체 개발한 음성 프로필 평가 시스템으로 검증되었습니다.

| 지표 | 점수 | 설명 |
|------|------|------|
| **전체 등급** | **A (0.805)** | 종합 품질 점수 |
| 시그니처 일치율 | 93.8% | 캐릭터 특유 표현 포함 비율 |
| 종결어미 일치율 | 55.7% | 지정된 종결어미 사용 비율 |
| 금지 표현 위반율 | 6.0% | 금지 표현 사용 비율 (낮을수록 좋음) |
| 말투 톤 일치율 | 74.9% | 지정된 말투 톤 유지 비율 |

### 캐릭터별 등급 분포

| 등급 | 캐릭터 수 | 점수 범위 |
|------|-----------|-----------|
| S | 1 | 0.90+ |
| A | 8 | 0.80-0.89 |
| B | 17 | 0.70-0.79 |
| C | 12 | 0.60-0.69 |
| D | 3 | 0.50-0.59 |

---

## 💻 사용 방법

### 기본 로드

```python
from datasets import load_dataset

# SFT 데이터 로드
sft_dataset = load_dataset(
    "developer-lunark/kaidol-character-dataset",
    "sft"
)

# DPO 데이터 로드
dpo_dataset = load_dataset(
    "developer-lunark/kaidol-character-dataset",
    "dpo"
)

# 멀티턴 데이터 로드
multiturn_dataset = load_dataset(
    "developer-lunark/kaidol-character-dataset",
    "multiturn"
)
```

### 특정 캐릭터 필터링

```python
# 특정 캐릭터만 필터링
character_name = "강리오"
filtered = sft_dataset["train"].filter(
    lambda x: x["character"] == character_name
)
print(f"{character_name} 샘플 수: {len(filtered)}")
```

### 데이터 탐색

```python
# 샘플 확인
sample = sft_dataset["train"][0]
print(f"캐릭터: {sample['character']}")
print(f"카테고리: {sample['category']}")
for conv in sample["conversations"]:
    print(f"{conv['from']}: {conv['value']}")
```

---

## 🎓 학습 가이드

### Axolotl (SFT)

```yaml
# axolotl_config.yaml
base_model: beomi/gemma-ko-2b
datasets:
  - path: developer-lunark/kaidol-character-dataset
    name: sft
    type: sharegpt
    conversation: chatml

sequence_len: 2048
micro_batch_size: 4
gradient_accumulation_steps: 4
num_epochs: 3
learning_rate: 2e-5

chat_template: chatml
```

### Axolotl (DPO)

```yaml
# axolotl_dpo_config.yaml
base_model: your-sft-model
rl: dpo

datasets:
  - path: developer-lunark/kaidol-character-dataset
    name: dpo
    type: chatml.intel

dpo_beta: 0.1
learning_rate: 5e-7
num_epochs: 1
```

### LLaMA-Factory

```json
// dataset_info.json
{
  "kaidol_sft": {
    "hf_hub_url": "developer-lunark/kaidol-character-dataset",
    "subset": "sft",
    "formatting": "sharegpt",
    "columns": {
      "messages": "conversations"
    }
  },
  "kaidol_dpo": {
    "hf_hub_url": "developer-lunark/kaidol-character-dataset",
    "subset": "dpo",
    "ranking": true,
    "columns": {
      "prompt": "prompt",
      "chosen": "chosen",
      "rejected": "rejected"
    }
  }
}
```

### Transformers (직접 학습)

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
from datasets import load_dataset

# 데이터 로드
dataset = load_dataset(
    "developer-lunark/kaidol-character-dataset",
    "sft"
)

# 토크나이저
tokenizer = AutoTokenizer.from_pretrained("beomi/gemma-ko-2b")

def format_conversation(example):
    text = ""
    for conv in example["conversations"]:
        role = "user" if conv["from"] == "human" else "assistant"
        text += f"<|{role}|>\n{conv['value']}\n"
    return {"text": text}

formatted = dataset.map(format_conversation)
```

---

## ⚠️ 제한사항

### 데이터 제한

1. **한국어 전용**: 영어 또는 다른 언어는 포함되지 않음
2. **캐릭터 편향**: 일부 캐릭터는 샘플 수가 적음 (최소 3개 ~ 최대 67개)
3. **도메인 제한**: 롤플레이/캐릭터 대화에 특화됨

### 모델 학습 시 주의사항

1. **음성 프로필 일관성**: 모델이 캐릭터별 말투를 정확히 구분하도록 충분한 학습 필요
2. **System Prompt 권장**: 학습/추론 시 캐릭터 정보를 System Prompt로 제공 권장
3. **DPO 학습**: SFT 이후 DPO 학습 권장 (직접 DPO는 비권장)

### 윤리적 고려사항

- 이 데이터셋은 가상의 캐릭터 롤플레이용입니다
- 실제 인물을 모사하거나 사칭하는 용도로 사용하지 마세요
- 생성된 모델의 출력은 캐릭터의 가상 발언이며, 사실이 아닐 수 있습니다

---

## 📜 라이선스

이 데이터셋은 **Apache License 2.0** 하에 배포됩니다.

### 허용되는 사용
- ✅ 상업적 사용
- ✅ 수정 및 배포
- ✅ 특허 사용
- ✅ 개인 사용

### 조건
- 저작권 표시 유지
- 라이선스 사본 포함
- 변경 사항 명시

---

## 📚 인용

```bibtex
@dataset{kaidol_character_dataset_2025,
  title={KAIdol Character Chat Dataset: Korean Character Roleplay Conversation Dataset},
  author={Lunark},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/developer-lunark/kaidol-character-dataset},
  note={41 characters, 2.1K samples, Voice Profile based quality control}
}
```

---

## 🙏 감사의 말

- **데이터 생성**: Qwen3-235B-A22B (vLLM inference)
- **품질 평가**: Constitution-based Charm Evaluation System
- **영감**: Character.AI, Pygmalion, CAI-Tools

---

## 📬 문의

- **Issues**: [GitHub Issues](https://github.com/developer-lunark/kaidol-llm-dataset-pipeline/issues)
- **Email**: developer@lunark.dev

---

<div align="center">

**Made with ❤️ for Korean Character AI**

</div>
