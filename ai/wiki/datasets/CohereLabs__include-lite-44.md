---
type: "dataset"
id: "CohereLabs/include-lite-44"
source: "huggingface"
url: "https://huggingface.co/datasets/CohereLabs/include-lite-44"
downloads: 1134
summary: "44개 언어의 학술 및 전문 시험 문제로 구성된 다국어 LLM 평가용 지식 및 추론 벤치마크 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교육]]"
  - "[[환경·기상]]"
  - "[[금융·경제]]"
  - "[[의료·보건]]"
  - "[[법률]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# CohereLabs/include-lite-44

> dataset · [Hugging Face](https://huggingface.co/datasets/CohereLabs/include-lite-44)

44개 언어의 학술 및 전문 시험 문제로 구성된 다국어 LLM 평가용 지식 및 추론 벤치마크 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `4-option multiple-choice-questions (MCQ)` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `4-option multiple-choice-questions (MCQ)` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `44 languages` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `33` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[교육]] — ner · readme = `extracted from academic and professional exams, covering 57 topics` · 신뢰도 low
- **도메인**: [[환경·기상]] — tag_match · tags = `climate` · 신뢰도 medium
- **도메인**: [[금융·경제]] — tag_match · tags = `finance` · 신뢰도 medium
- **도메인**: [[의료·보건]] — tag_match · tags = `medical` · 신뢰도 medium
- **도메인**: [[법률]] — tag_match · tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `evaluates multilingual LLMs for performance in the actual language environments` · 신뢰도 medium
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `question` 열 p90 133자 ≈ 33 토큰 (viewer statistics, Korean/test)
