---
type: "dataset"
id: "dobstudio/kor-persona-survey-sample"
source: "huggingface"
url: "https://huggingface.co/datasets/dobstudio/kor-persona-survey-sample"
downloads: 11
summary: "한국인 가상 인물 프로필이 설문 문항에 인물 입장에서 답한 시연용 축소 샘플 데이터입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# dobstudio/kor-persona-survey-sample

> dataset · [Hugging Face](https://huggingface.co/datasets/dobstudio/kor-persona-survey-sample)

한국인 가상 인물 프로필이 설문 문항에 인물 입장에서 답한 시연용 축소 샘플 데이터입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Korean persona profiles answering survey / balance-game questions in character, labeled by a Qwen2.5-72B-Instruct teacher.` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:generation = `Korean persona profiles answering survey / balance-game questions in character` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Teacher label: `{choice, confidence, reason}`` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `245` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Korean persona profiles answering survey / balance-game questions in character` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `A deliberately reduced demonstration sample (800 triplets) of the synthetic training data behind dobstudio/kor-persona-survey-7b` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `persona_profile` 열 p90 368자 ≈ 245 토큰 (viewer statistics, default/train)
