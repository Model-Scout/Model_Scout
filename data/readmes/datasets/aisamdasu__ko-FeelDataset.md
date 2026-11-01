---
language:
- ko
pretty_name: ko-FeelDataset
task_categories:
- text-classification
tags:
- emotion
- emotion-recognition
- korean
- conversational
- sentiment
size_categories:
- 10K<n<100K
---

# ko-FeelDataset

한국어 일상 발화 한두 문장에 담긴 **감정**을 라벨링한 **44,887개**의 데이터셋입니다. 한 발화에 대해 주 감정·부 감정과 강도·확신도를 함께 답니다.

## 무엇을 담았나

- 가족·연애·직장·이별·육아·건강·돈·학교·반려동물·명절 등 **아주 다양한 일상 장면**에서 나오는 감정.
- 발화는 "슬프다/불안하다" 같은 **감정 단어를 직접 쓰지 않고**, 상황·행동·디테일로 감정을 **보여주는** 방식으로 쓰여 있습니다.
- 라벨 분포는 인위적 균등이 아니라 **현실에 가까운 분포**이며, 사랑·감사·안도·그리움 같은 **따뜻한 관계적 감정**이 풍부합니다.

## 포맷

한 줄당 JSON 1개(JSONL), 챗 파인튜닝용 `messages` 포맷입니다.

```json
{"messages": [
  {"role": "user", "content": "퇴근하고 비밀번호 누르고 문 여는데 달려나오는 발톱 소리가 없어서, 신발도 못 벗고 현관에 한참 그냥 서 있었어."},
  {"role": "assistant", "content": "{\"primary_emotion\": \"grief\", \"secondary_emotion\": \"loneliness\", \"intensity\": 0.9, \"confidence\": 0.94}"}
]}
```

`assistant`의 content는 아래 4개 키를 가진 JSON 문자열입니다.

| 필드 | 설명 |
|---|---|
| `primary_emotion` | 지배적 감정 (아래 22개 중 하나) |
| `secondary_emotion` | 함께 묻어나는 부차 감정 (primary와 다름) |
| `intensity` | 감정 강도 0.00–1.00 |
| `confidence` | 라벨 확신도 0.50–1.00 |

## 감정 라벨 (22종)

```
joy, excitement, gratitude, pride, relief, love,
sadness, loneliness, grief, disappointment,
anger, frustration, disgust,
fear, anxiety, embarrassment, confusion, curiosity, surprise,
fatigue, stress, neutral
```

## 통계

- **44,887건** · 중복 없음 · 발화 길이 중앙값 48자
- `intensity` 평균 0.63 · `confidence` 평균 0.86
- 주 감정 상위: anxiety · relief · sadness · frustration · disappointment … (최다:최소 ≈ 3.8:1의 현실형 분포)

## 제작 철학

대량 자동 생성이 아니라, **한 건씩 품질을 확인해 통과시킨** 데이터입니다. 상투적이거나 부자연스러운 문장, 감정 단어가 노출된 문장, 중복·유사 문장을 걸러내고 **자연스럽고 구체적인 한국어**만 남겼습니다. "보여주기" 문체, 무중복, 다양성, 현실적이면서 따뜻한 감정 분포를 일관되게 유지하는 것을 목표로 했습니다.

## 사용 예

```python
from datasets import load_dataset
ds = load_dataset("aisamdasu/ko-FeelDataset")
```
