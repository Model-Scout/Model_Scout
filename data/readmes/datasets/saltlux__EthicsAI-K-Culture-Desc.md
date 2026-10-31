---
license: apache-2.0
task_categories:
  - question-answering
  - multiple-choice
language:
  - ko
size_categories:
  - n<1K
tags:
  - korean-culture
  - cultural-understanding
  - mcqa
pretty_name: K-Culture Contextual Understanding Benchmark
---

# 한국 문화 맥락 이해 벤치마크 (K-Culture Contextual Understanding Benchmark)

한국 문화에 대한 모델의 맥락적 이해도를 평가하기 위해 설계된 530개의 시나리오 기반 객관식 질문을 포함하는 한국 문화 이해 벤치마크 데이터셋입니다.

## 데이터셋 설명

**한국 문화 맥락 이해 벤치마크**는 실생활 시나리오와 대화를 통해 거대언어모델(LLM)의 한국 문화 맥락 이해 능력을 평가하기 위해 설계된 데이터셋입니다. 각 항목은 문화적 설명, 실제 상황을 묘사한 시나리오, 그리고 상세한 해설이 포함된 객관식 질문으로 구성되어 있습니다.

* **언어:** 한국어 (ko)
* **크기:** 530개 항목
* **작업:** 객관식 질의응답 (MCQA)
* **버전:** v1.0

## 데이터 구조

### 데이터 필드

| 필드명 | 타입 | 설명 |
| --- | --- | --- |
| `DescriptionID` | int | 각 항목의 고유 식별자 |
| `Description` | string | 한국 문화 현상에 대한 간결한 설명 |
| `ScenarioBody` | string | 문화적 맥락을 보여주는 사실적인 시나리오 |
| `MCQA` | object | 객관식 질문 및 정답 정보 |
| `MCQA.Question` | string | 시나리오를 바탕으로 한 질문 |
| `MCQA.Choices` | string | 4개의 선택지 (A, B, C, D) |
| `MCQA.Answer` | string | 정답 (A, B, C 또는 D) |
| `MCQA.Explanation` | string | 정답의 이유 및 오답에 대한 상세 설명 |
| `Type` | string | 질문 유형 카테고리 (1, 2 또는 3) |
| `Category` | string | 문화 영역 카테고리 |

### 데이터 예시

```json
{
  "DescriptionID": 1,
  "Description": "한국의 야구장에서는 관중들이 다함께 응원가를 부르고, 춤을 춘다.",
  "ScenarioBody": "지윤은 미국에서 온 교환학생 에밀리와 함께...",
  "MCQA": {
    "Question": "에밀리의 SNS 글과 그에 대한 대화에서, 에밀리가 인상적으로 느낀 점에 가장 부합하는 것은?",
    "Choices": "A. 팬들이 경기 내내 적극적으로 노래와 율동에 참여하는 분위기\nB. 응원단과 치어리더가 경기 중간마다 공연을 펼치는 점\nC. 다양한 간식과 음료를 즐기며 경기를 관람하는 문화\nD. 관중들이 특정 시간에만 단체로 노래를 부르는 모습",
    "Answer": "A",
    "Explanation": "- 정답이 되는 이유: 에밀리는 SNS에 \"콘서트에 다녀온 것 같다\"라고 표현하고..."
  },
  "Type": "1",
  "Category": "Music, Sports and Arts"
}

```

## 질문 유형

| 유형 | 설명 | 개수 |
| --- | --- | --- |
| 유형 1 | 한국 문화와 유사한 외국 문화 사이의 유사점과 차이점을 정확히 비교할 수 있는가? | 290 |
| 유형 2 | 한국 문화 내의 유사한 개념들 사이의 차이점을 이해하고 있는가? | 101 |
| 유형 3 | 한국 내 특정 집단에서만 공유되는 맥락을 이해하고 있는가? | 139 |

## 카테고리

본 데이터셋은 15개의 문화 영역을 다룹니다:

| 카테고리 | 개수 |
| --- | --- |
| 식음료 (Food and Drinks) | 127 |
| 전통 및 의례 (Traditions and Rituals) | 68 |
| 지식 및 이야기 (Knowledge and Stories) | 58 |
| 도구 및 사물 (Tools and Objects) | 50 |
| 음악, 스포츠 및 예술 (Music, Sports and Arts) | 45 |
| 언어 (Language) | 34 |
| 건축 (Architecture) | 29 |
| 경제 및 노동 (Economy and Work) | 25 |
| 정치 및 정부 (Politics and Government) | 19 |
| 환경 및 지리 (Environment and Geography) | 18 |
| 지역 사회 (Greater Community) | 18 |
| 가치관 (Values) | 18 |
| 기술 및 숙련 (Techniques and Skills) | 10 |
| 교육 (Education) | 7 |
| 엔터테인먼트 (Entertainment) | 4 |

## 사용 방법

### 데이터셋 불러오기

```python
from datasets import load_dataset

dataset = load_dataset("SOGANG-ISDS/K-Culture-Desc")

```

### 예시 코드

```python
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("SOGANG-ISDS/K-Culture-Desc")

# 샘플 데이터 확인
sample = dataset['test'][0]
print(f"설명: {sample['Description']}")
print(f"질문: {sample['MCQA']['Question']}")
print(f"선택지: {sample['MCQA']['Choices']}")
print(f"정답: {sample['MCQA']['Answer']}")

```

### 평가 예시

```python
def evaluate_model_response(model_answer: str, correct_answer: str) -> bool:
    """모델의 답변이 정답과 일치하는지 확인합니다."""
    return model_answer.strip().upper() == correct_answer.strip().upper()

# 평가 실행 예시
correct = evaluate_model_response("A", sample['MCQA']['Answer'])
print(f"정답 여부: {correct}")

```

## 사의 표명

본 연구는 대한민국 정부(과학기술정보통신부)의 재원으로 정보통신기획평가원(IITP)의 지원을 받아 수행되었습니다 (No.RS-2024-00343989, 사회적·윤리적 학습을 위한 데이터 특성 및 생성 AI 모델의 윤리성 강화 기술 개발).

## 인용 (Citation)

```bibtex
@dataset{k_culture_2025,
  title={A Korean Cultural Understanding Benchmark Dataset with Detailed Scenario},
  year={2025},
  url={https://huggingface.co/datasets/SOGANG-ISDS/K-Culture-Desc}
}

```

## 라이선스

이 데이터셋은 [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)에 따라 이용 가능합니다.