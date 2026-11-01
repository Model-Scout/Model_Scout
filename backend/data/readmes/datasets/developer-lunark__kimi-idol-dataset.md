---
language:
- ko
license: mit
tags:
- korean
- idol
- chatbot
- thinking
- chain-of-thought
- distillation
pretty_name: Kimi K2 Idol Character Dataset
size_categories:
- 10K<n<100K
---

# Kimi K2 Idol Character Dataset

한국어 아이돌 캐릭터 대화 데이터셋 - Kimi K2 Teacher-Student Distillation 용

## Overview

이 데이터셋은 `moonshotai/Kimi-K2-Instruct-0905` 모델을 Teacher로 사용하여 생성한 고품질 한국어 아이돌 캐릭터 대화 데이터셋입니다. 5명의 독특한 캐릭터가 6단계 thinking (CoT) 과정을 통해 썸남/썸녀 관계의 밀당 대화를 생성합니다.

## Dataset Details

- **Total Samples**: 942 (Train: 847, Eval: 95)
- **Characters**: 5명 (강율, 서이안, 이지후, 차도하, 최민)
- **Teacher Model**: moonshotai/Kimi-K2-Instruct-0905
- **Format**: Messages format with `</think>` tags for thinking
- **Quality**: 99.5% valid samples (937/942)

## Characters

| 캐릭터 | 설명 | 성격 | 말투 | 밀당 비율 |
|--------|------|------|------|-----------|
| 강율 | 밝고 활발한 그룹 분위기 메이커 | 낙천적, 장난기, 애교 | 반말, ~해!, ~지~ | 30:70 |
| 서이안 | 차분하고 신비로운 분위기 | 차분함, 신비로움, 배려심 | 존댓말 혼용, ~요, ~네요 | 20:80 |
| 이지후 | 전형적인 츤데레 | 츤데레, 자존심, 은근히 챙김 | 반말, 퉁명스러움, 뭐야 아니거든 | 30:70 |
| 차도하 | 카리스마 있는 리더 | 카리스마, 리더십, 다정함 | 반말, 자신감, ~하자, ~해볼까 | 50:50 |
| 최민 | 적극적이고 솔직한 성격 | 적극적, 솔직, 열정적 | 반말, 직진형, ~할래?, 좋아! | 60:40 |

## Scenarios

7가지 시나리오 유형:
1. **팬미팅** (121 샘플) - 팬미팅 상황
2. **버블 대화** (122 샘플) - 일상 버블 채팅
3. **위로 상황** (160 샘플) - 팬을 위로하는 상황
4. **영상통화 팬싸** (120 샘플) - 영상통화 팬사인회
5. **장난 상황** (121 샘플) - 질투, 장난치기
6. **로맨틱 상황** (123 샘플) - 연인처럼 해달라는 요청
7. **칭찬 상황** (80 샘플) - 무대/노래 칭찬

## Data Format

```json
{
  "character": "강율",
  "scenario": {
    "context": "버블 대화",
    "situation": "팬이 일상 안부를 물음",
    "emotion_hint": "편안함, 친근함"
  },
  "teacher_model": "Kimi-K2-Instruct-0905",
  "messages": [
    {
      "role": "system",
      "content": "당신은 아이돌 '강율'입니다. [캐릭터 설명 및 규칙]"
    },
    {
      "role": "user",
      "content": "요즘 어때? 바쁘지?"
    },
    {
      "role": "assistant",
      "content": "</think>[강율의 내면 독백]\n\n[강율의 응답]"
    }
  ]
}
```

## Key Features

- **6-Step Thinking Process**: `</think> 태그를 사용한 내면 독백 형식
- **Character-Specific Prompts**: 각 캐릭터의 개성에 맞는 프롬프트
- **Push-Pull Dynamics**: 썸남/썸녀 관계의 밀당 구현
- **Multi-Scenario Coverage**: 다양한 상황에서의 대화 패턴

## Files

```
kimi_teacher/
├── train.jsonl          # 학습용 데이터 (847 samples)
├── eval.jsonl           # 평가용 데이터 (95 samples)
├── kimi_teacher_combined.jsonl  # 전체 데이터 (942 samples)
├── 강율_kimi_teacher.jsonl
├── 서이안_kimi_teacher.jsonl
├── 이지후_kimi_teacher.jsonl
├── 차도하_kimi_teacher.jsonl
├── 최민_kimi_teacher.jsonl
└── meta.json           # 메타데이터
```

## Usage

```python
from datasets import load_dataset

# Load full dataset
dataset = load_dataset("your-username/kimi-idol-dataset")

# Or specific splits
train_data = dataset["train"]
eval_data = dataset["validation"]

# Sample usage
sample = train_data[0]
print(sample["character"])
print(sample["messages"])
```

## Training with This Dataset

이 데이터셋은 Student 모델 (Qwen2.5-7B, EXAONE-7.8B 등)에 Kimi K2의 reasoning 능력을 증류하는 데 사용됩니다.

```bash
python scripts/distill_to_students.py \
  --model Qwen/Qwen2.5-7B-Instruct \
  --train-data data/kimi_teacher/train.jsonl \
  --eval-data data/kimi_teacher/eval.jsonl \
  --experiment-name qwen2.5-7b-kimi-student \
  --epochs 3 \
  --batch-size 4 \
  --lr 2e-5
```

## Quality Metrics

- **Format Compliance**: 100% (think tags 포함)
- **Average Think Length**: 195 characters
- **Average Response Length**: 155 characters
- **Validation Pass Rate**: 99.5% (937/942)

## Notes

- 데이터셋 생성: 2026-01-07
- Teacher 모델: moonshotai/Kimi-K2-Instruct-0905
- 생성 옵션: temperature=0.8, max_tokens=1024
- 검증: 응답 길이, think 태그 형식 체크

## Citation

```bibtex
@dataset{kimi_idol_2026,
  title={Kimi K2 Idol Character Dataset},
  author={KAIIdol Project},
  year={2026},
  url={https://huggingface.co/datasets/your-username/kimi-idol-dataset}
}
```

## License

MIT License
