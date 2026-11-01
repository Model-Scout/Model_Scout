---
type: "dataset"
id: "NAMJOON/multichallenge-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/NAMJOON/multichallenge-ko"
downloads: 47
summary: "MultiChallenge 영어 벤치마크를 한국어로 기계 번역한 대화형 평가 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# NAMJOON/multichallenge-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/NAMJOON/multichallenge-ko)

MultiChallenge 영어 벤치마크를 한국어로 기계 번역한 대화형 평가 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `273 대화, 4개 축. 원본 구조를 유지합니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `평가 대상은 모델이 생성할 다음 응답입니다` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `72` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `MultiChallenge (Sirdeshmukh et al., Findings of ACL 2025) 를 한국어로 기계 번역한 자료입니다.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `번역 벤치마크와 한국어로 직접 작성한 벤치마크를 비교하는 연구를 위해 만들었습니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `TARGET_QUESTION` 열 p90 109자 ≈ 72 토큰 (viewer statistics, korean_only/train)
