---
type: "dataset"
id: "tellarin-ai/ntx_llm_inst_korean"
source: "huggingface"
url: "https://huggingface.co/datasets/tellarin-ai/ntx_llm_inst_korean"
downloads: 19
summary: "원본 NTX 데이터의 한국어 부분을 Aya 명령어 형식으로 변환한 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[정보 추출]]"
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
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# tellarin-ai/ntx_llm_inst_korean

> dataset · [Hugging Face](https://huggingface.co/datasets/tellarin-ai/ntx_llm_inst_korean)

원본 NTX 데이터의 한국어 부분을 Aya 명령어 형식으로 변환한 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Aya instruction format` · 신뢰도 low
- **작업**: [[정보 추출]] — metadata · task_categories = `token-classification` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:information_extraction = `Korean data from the original NTX` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Aya instruction format` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `442` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a format conversion for the Korean data from the original NTX into the Aya instruction format` · 신뢰도 low
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `inputs` 열 p90 663자 ≈ 442 토큰 (viewer statistics, default/train)
