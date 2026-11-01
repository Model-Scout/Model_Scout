---
type: "dataset"
id: "EinicherAI/nemotron-multilingual-math-verified"
source: "huggingface"
url: "https://huggingface.co/datasets/EinicherAI/nemotron-multilingual-math-verified"
downloads: 15
summary: "일본어, 한국어, 브라질 포르투갈어 수학 문제의 정답 박스 처리 검증 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[de]]"
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[pt]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# EinicherAI/nemotron-multilingual-math-verified

> dataset · [Hugging Face](https://huggingface.co/datasets/EinicherAI/nemotron-multilingual-math-verified)

일본어, 한국어, 브라질 포르투갈어 수학 문제의 정답 박스 처리 검증 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Rows are useful for small-model SFT in Japanese, Korean, and Brazilian Portuguese mathematical reasoning where an answer must be boxed.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:generation = `math splits (math_ja, math_ko, math_pt)` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `where an answer must be boxed` · 신뢰도 medium
- **언어**: [[de]] — metadata · languages = `de` · 신뢰도 high
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[pt]] — metadata · languages = `pt` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a verified subset of nvidia/Nemotron-SFT-Multilingual-v2's math splits (math_ja, math_ko, math_pt)` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Rows are useful for small-model SFT in Japanese, Korean, and Brazilian Portuguese mathematical reasoning` · 신뢰도 medium
