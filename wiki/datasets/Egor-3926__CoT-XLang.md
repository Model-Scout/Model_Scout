---
type: "dataset"
id: "Egor-3926/CoT-XLang"
source: "huggingface"
url: "https://huggingface.co/datasets/Egor-3926/CoT-XLang"
downloads: 235
summary: "CoT-XLang은 영어, 러시아어, 일본어 등 여러 언어의 단계별 추론 텍스트 예제로 구성된 다국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[es]]"
  - "[[id]]"
  - "[[it]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[th]]"
  - "[[vi]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[대규모 데이터]]"
---
# Egor-3926/CoT-XLang

> dataset · [Hugging Face](https://huggingface.co/datasets/Egor-3926/CoT-XLang)

CoT-XLang은 영어, 러시아어, 일본어 등 여러 언어의 단계별 추론 텍스트 예제로 구성된 다국어 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering = `многоязычный датасет, состоящий из текстовых примеров с пошаговыми рассуждениями` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering = `модели, способные генерировать пошаговые рассуждения` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[es]] — metadata · languages = `es` · 신뢰도 high
- **언어**: [[id]] — metadata · languages = `id` · 신뢰도 high
- **언어**: [[it]] — metadata · languages = `it` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `10 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[th]] — metadata · languages = `th` · 신뢰도 high
- **언어**: [[vi]] — metadata · languages = `vi` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `492` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `CoT-XLang — это многоязычный датасет, состоящий из текстовых примеров с пошаговыми рассуждениями (Chain-of-Thought, CoT) на различных языках` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Используйте датасет для обучения моделей, обеспечивая многоязычную поддержку и акцент на пошаговые объяснения` · 신뢰도 low
- **데이터 규모**: [[대규모 데이터]] — metadata · size_categories = `9999999.0` · 신뢰도 high

샘플 길이: `response` 열 p90 1968자 ≈ 492 토큰 (viewer statistics, Korean/train)
