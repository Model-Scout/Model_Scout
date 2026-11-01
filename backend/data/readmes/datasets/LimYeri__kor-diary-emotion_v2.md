---
dataset_info:
  features:
  - name: text
    dtype: string
  - name: main_emotion
    dtype: string
  - name: fine_emotions
    dtype: string
  - name: situation_category
    dtype: string
  - name: situation_detail
    dtype: string
  splits:
  - name: train
    num_bytes: 16144221
    num_examples: 37376
  download_size: 6808308
  dataset_size: 16144221
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: mit
task_categories:
- text-classification
language:
- ko
---


# Korean Daily-Emotion & Situation Dataset  

## 📌 Dataset Overview

이 데이터셋은 한국어 감정 분류를 위해 제작된 텍스트 데이터셋으로,  
OpenAI API를 활용해 생성된 **일기(Diary) 형식의 자연스럽고 일상적인 문장들**로 구성되어 있습니다.  
총 **29,968개**의 문장을 포함하며, 각 샘플은 사용자의 일상 경험·상황·감정 흐름을 반영하도록 설계되었습니다.  

This is a large-scale **Korean diary-style emotion classification dataset** generated using OpenAI's GPT-4o-mini model.  
It contains **29,968 samples**, each written in a natural diary format,  
capturing everyday situations and emotional nuances across **8 main emotions** with fine-grained emotional labels.

---
## 📌 Dataset Structure

데이터셋의 각 샘플은 다음 5개 필드로 구성됩니다.
| Column | Description |
|--------|-------------|
| `text` | 1~4문장 내외의 자연스러운 한국어 일기 |
| `main_emotion` | 8가지 대표 감정 중 하나 |
| `fine_emotions` | 대표 감정의 세부 감정 리스트(1-3개) |
| `situation_category` | 감정이 나타난 상황의 카테고리 |
| `situation_detail` | 상황을 구체적으로 설명 |

---
## 🎭 Emotion Labels (`main_emotion`)

총 8개의 대표 감정으로 구성됩니다.
| Emotion (감정) | Count (개수) |
|----------------|--------------|
| 기쁨           | 6,235행        |
| 설렘           | 6,227행        |
| 평범함         | 6,229행        |
| 놀라움         | 6,243행        |
| 불쾌함         | 4,800행        |
| 두려움         | 1,000행        |
| 슬픔           | 1,000행        |
| 분노           | 5,642행        |

### 감정별 대표 세부 감정 (fine_emotions 기반)

```python
emotion_keyword_map = {
    "기쁨": ["기분좋은", "즐거운", "고마운", "홀가분한", "사랑스러운", "재밌는", "기쁜", "뿌듯한", "속시원한", "만족스러운", "신나는", "행복한", "감동받은", "날아갈 것 같은"],
    "설렘": ["몽글몽글한", "두근거리는", "간질간질한", "설레는", "흥미로운", "신나는", "기대되는", "궁금한", "긴장되는", "안달나는", "텐션 높은", "간절한 마음의"],
    "평범함": ["잔잔한", "별 일 없는", "나쁘지 않은", "그저 그런", "만족스러운", "무난한", "피곤한", "괜찮은", "싱숭생숭한", "소소한", "평범한", "안정감이 드는", "편안한"],
    "놀라움": ["당황스러운", "어이 없는", "부끄러운", "심쿵한", "깜짝 놀란", "어안이 벙벙한", "멘탈 무너지는", "만감이 교차하는", "기가 막히는", "소름끼치는", "상상을 초월하는", "골때리는", "폭풍같은"],
    "불쾌함": ["피곤한", "지치는", "귀찮은", "재미없는", "지루한", "불편한", "불쾌한", "찝찝한", "소외감 느끼는", "우울한", "지긋지긋한", "토나오는", "기분 더러운"],
    "두려움": ["망설여지는", "걱정되는", "불안한", "심란한", "긴장되는", "막막한", "두려운", "큰일 난 것 같은", "겁나는", "무서운", "초조한", "쫄리는", "숨막히는", "도망치고 싶은", "끝이 보이지 않는"],
    "슬픔": ["무기력한", "실망스러운", "속상한", "외로운", "마음아픈", "후회되는", "힘든", "서러운", "슬픈", "허탈한", "막막한", "우울한", "혼자인 것 같은", "울고싶은",  "절망적인", "그리운", "공허한", "세상이 무너진 것 같은"],
    "분노": ["답답한", "짜증나는", "신경질나는", "어이없는", "이해할 수 없는", "화나는", "한심한", "킹받는", "억울한", "기분 더러운", "질투나는", "분한", "빡치는", "소리지르고 싶은"]
}
```

---
## ✔️ Model & Data Generation Info

- 본 데이터셋은 OpenAI **gpt-4o-mini** 모델을 사용해 생성되었습니다.  
- 모든 문장은 **모델이 창작한 내용이며**, 실제 개인 정보·실존 인물·저작물 등의 내용은 포함하지 않습니다.
- 감정 및 상황 설정은 프롬프트 기반 규칙에 따라 자동 생성되었으며, **데이터 품질 편향이나 오류는 모델의 특성에서 기인할 수 있습니다.**  

**데이터 내용에 대한 책임은 LLM 생성 과정의 특성에 있으며**, 데이터 생성자는 이를 조작하거나 개입하지 않았습니다.