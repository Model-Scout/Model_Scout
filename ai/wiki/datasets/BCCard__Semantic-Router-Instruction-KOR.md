---
type: "dataset"
id: "BCCard/Semantic-Router-Instruction-KOR"
source: "huggingface"
url: "https://huggingface.co/datasets/BCCard/Semantic-Router-Instruction-KOR"
downloads: 65
summary: "한국어 semantic-turn router 학습용 14축 분류 지시문 데이터셋, 60만 행 규모"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
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
  - "[[평가용]]"
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# BCCard/Semantic-Router-Instruction-KOR

> dataset · [Hugging Face](https://huggingface.co/datasets/BCCard/Semantic-Router-Instruction-KOR)

한국어 semantic-turn router 학습용 14축 분류 지시문 데이터셋, 60만 행 규모

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `한 문장을 14개 축으로 동시에 분류하는 모델의 학습 데이터로 쓰기 위해 만들었고` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = ``instruction`은 해당 축·값을 판별할 수 있는 내용 단서를 실제로 포함한다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `한 `instruction`은 정확히 하나의 (category, value) 쌍으로 라벨링된다` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `129` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `semantic-turn router 학습·평가용 한국어 instruction 데이터셋` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · readme = `semantic-turn router 학습·평가용 한국어 instruction 데이터셋` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `한 문장을 14개 축으로 동시에 분류하는 모델의 학습 데이터로 쓰기 위해 만들었고` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `instruction` 열 p90 193자 ≈ 129 토큰 (viewer statistics, default/train)
