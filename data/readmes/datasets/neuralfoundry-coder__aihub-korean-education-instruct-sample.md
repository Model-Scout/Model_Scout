---
language:
- ko
license: cc-by-nc-sa-4.0
task_categories:
- text-generation
- question-answering
tags:
- education
- korean
- instruction-tuning
- sLLM
- aihub
pretty_name: Korean Education Instruction Dataset (Sample)
size_categories:
- 1K<n<10K
---

<!-- aegis-dataset-card -->

# aihub-korean-education-instruct-sample

> **용도 기록 없음** · Korean Education Instruction Dataset (Sample)  
> 파일 3개 · 16.2 MB · 행 6,000 · revision `a57a079497` · 카드 갱신 2026-10-20  
> 전체 모델 ↔ 데이터 매핑 · 서버 복원 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020)

## 개요
AI Hub의 한국어 교육 데이터셋 13종을 sLLM 지시학습(Instruction Tuning)용으로 변환한 데이터셋입니다.
초등학교부터 고등학교까지의 다양한 교육 콘텐츠를 포함합니다.

## 이 데이터로 학습한 모델
이 데이터로 학습했다는 기록(학습 설정 · 모델 카드)을 찾지 못했다. 카탈로그의 '확인 필요' 목록에 있다.

## 파일 구성
| 파일 | 크기 | 행 | 내용 |
|---|---|---|---|
| `README.md` | 2.0 KB | - |  |
| `data/train.jsonl` | 14.7 MB | 5,400 |  |
| `data/validation.jsonl` | 1.5 MB | 600 |  |

## 필드 · 범주 분포
**`data/train.jsonl`, `data/validation.jsonl`** (기준 `data/train.jsonl`)

| 필드 | 타입 | 채움 |
|---|---|---|
| `id` | str | 100% |
| `conversations` | list | 100% |
| `category` | str | 100% |
| `subcategory` | str | 100% |
| `source` | str | 100% |
| `metadata` | dict | 100% |

범주 분포(기준 파일):
- `category`: korean 927(17%) · writing 901(17%) · math 901(17%) · career 896(17%) · curriculum 888(16%) · tutor 887(16%)
- `subcategory`: reading_comprehension 927(17%) · problem_solving 901(17%) · emotion_feedback 887(16%) · qa 868(16%) · sentence_completion 662(12%) · 서술형_글쓰기 452(8%) · career_counseling 234(4%) · 주제별_글쓰기 228(4%) · 논술형_글쓰기 221(4%) · academic_paper 20(0%)
- `source`: 29_korean_reading 927(17%) · 241_emotion_tutor 887(16%) · 28_curriculum 868(16%) · 111_math_problem_gen 750(14%) · 108_career_sentence 662(12%) · 25_descriptive 452(8%) · 270_career_counseling 234(4%) · 27_topic_writing 228(4%) · 26_essay 221(4%) · 30_math_solution 151(3%) · 32_academic_paper 20(0%)

필드는 행 최상위 키, 채움은 그 키가 있는 행 비율이다. 범주 분포는 글 필드가 아니고 값이 짧고(≤48자) 종류가 적은(≤40) 필드만 셌다.

## 내려받기 · 복원
```bash
hf download neuralfoundry-coder/aihub-korean-education-instruct-sample --repo-type dataset --local-dir <폴더>
```
- 서버 파일 전체의 위치 · 재생성 방법: [`neuralfoundry-coder/workspace-data-catalog_261020`](https://huggingface.co/datasets/neuralfoundry-coder/workspace-data-catalog_261020) 의 `restore_map.json`

## 기존 설명 (2026-10-20 이전 카드)

### Korean Education Instruction Dataset (Sample)

> **Note**: 이 데이터셋은 전체 데이터셋의 샘플 버전입니다 (카테고리별 최대 1,000건).

#### 개요

AI Hub의 한국어 교육 데이터셋 13종을 sLLM 지시학습(Instruction Tuning)용으로 변환한 데이터셋입니다.
초등학교부터 고등학교까지의 다양한 교육 콘텐츠를 포함합니다.

#### 데이터셋 통계

| 카테고리 | 데이터 수 |
|----------|----------|
| math (수학) | 1000 |
| korean (국어) | 1000 |
| writing (글쓰기) | 1000 |
| career (진로) | 1000 |
| curriculum (교과) | 1000 |
| tutor (튜터링) | 1000 |
| **총계** | **6000** |

#### 사용 방법

```python
from datasets import load_dataset

### 데이터셋 로드
dataset = load_dataset("neuralfoundry-coder/aihub-korean-education-instruct-sample")

### 학습 데이터 접근
train_data = dataset['train']
print(train_data[0])
```

#### 데이터 포맷

```json
{
  "id": "math_111_a1b2c3d4",
  "conversations": [
    {"role": "system", "content": "당신은 수학 교사입니다..."},
    {"role": "user", "content": "문제를 풀어주세요..."},
    {"role": "assistant", "content": "풀이 과정..."}
  ],
  "category": "math",
  "subcategory": "problem_solving",
  "source": "111_math_problem_gen",
  "metadata": {"grade": "초등학교 3학년", "difficulty": "2"}
}
```

#### 데이터 출처

AI Hub (한국지능정보사회진흥원)에서 제공하는 교육 데이터셋 기반:
- 수학 자동 풀이/문제 생성
- 국어 독해 문제
- 글쓰기 평가 (서술형/논술형)
- 진로 상담
- 교과 단계별 데이터
- 감성 AI 튜터

#### 라이선스

- CC BY-NC-SA 4.0 (비상업적 목적)
- AI Hub 이용약관 준수 필요
