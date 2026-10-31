---
language:
  - ko
task_categories:
  - text-generation
  - question-answering
  - summarization
  - text-retrieval
tags:
  - namuwiki
  - arknights
  - game
license: cc-by-nc-sa-2.0
---

# ⚠️ 이 데이터셋은 테스트 버전으로, 데이터 일관성이 보장되지 않습니다.

---

# Namuwiki Arknights Text Dataset (preview)

이 데이터셋은 [명일방주 - 나무위키](https://namu.wiki/w/명일방주) 관련 문서에서 추출한 한국어 텍스트 데이터셋입니다.

- version: [v1.0](https://huggingface.co/datasets/alchemine/namuwiki-arknights-text-preview/tree/v1.0)

## 📅 데이터 생성일

2025/09/12

## 📊 데이터셋 통계

- **전체 데이터 수**: 1,463
- **전체 문서 수**: 47
- **평균 품질 점수**: 2.06

## 📝 데이터 구조

각 샘플은 다음과 같은 필드를 포함합니다:

- `id`(`str`): 고유 식별자
- `doc_id`(`str`): 문서 ID
- `doc_title`(`str`): 문서 제목
- `section_id`(`str`): 섹션 ID
- `section_depth`(`int`): 섹션 깊이
- `section_number`(`str`): 섹션 번호
- `section_url`(`str`): 섹션 URL
- `parent_id`(`str`): 부모 섹션 ID
- `parent_headings`(`str`): 부모 섹션 제목들 (줄바꿈으로 연결)
- `heading`(`str`): 섹션 제목
- `content`(`str`): 섹션 내용
- `created_at`(`str`): 생성 시간 (ISO 8601 형식)
- `is_valid`(`bool`): 유효성 여부
- `quality`(`float`): 품질 점수

## 🔍 품질 기준

- **유효 데이터**: 실제 내용이 있고 리다이렉션이 아닌 섹션
- **품질 점수**: 텍스트 품질을 줄바꿈 개수 대비 문장의 개수로 평가
- **필터링**: 내용이 없거나, 품질 점수 0.5 미만인 섹션은 무효로 분류

## 💡 사용 예시

```python
from datasets import load_dataset

# 데이터셋 로드
dataset = load_dataset("alchemine/namuwiki-arknights-text-preview", split="train")

# 문서명 확인
for title, url in set(zip(dataset["doc_title"], dataset["section_url"])):
    print(f"title: {title}, url: {url.split('#')[0]}")

# 섹션명 확인
for d in dataset:
    print(
        f"title: {d['doc_title']}, section: '{d['heading']}', url: {d['section_url']}"
    )

# 유효한 데이터만 필터링
valid_data = dataset.filter(lambda x: x["is_valid"])

# 고품질 데이터만 필터링
high_quality_data = valid_data.filter(lambda x: x["quality"] >= 1.0)
```

## 📄 라이선스

이 데이터셋은 [CC BY-NC-SA 2.0 KR](https://creativecommons.org/licenses/by-nc-sa/2.0/kr/legalcode) 라이선스 하에 배포됩니다.
