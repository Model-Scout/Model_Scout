---
type: "dataset"
id: "endomorphosis/ipfs_korea_laws"
source: "huggingface"
url: "https://huggingface.co/datasets/endomorphosis/ipfs_korea_laws"
downloads: 64
summary: "국가법령정보센터 법제처의 대한민국 현행법령 스냅샷 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# endomorphosis/ipfs_korea_laws

> dataset · [Hugging Face](https://huggingface.co/datasets/endomorphosis/ipfs_korea_laws)

국가법령정보센터 법제처의 대한민국 현행법령 스냅샷 데이터셋입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `article/조문 rows for the same snapshot` · 신뢰도 low
- **작업**: [[문서 검색]] — metadata · readme, task_categories = `text-retrieval` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:information_extraction, task:retrieval = `published via law.go.kr public HTML` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `article/조문 rows for the same snapshot` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `51488` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `Research snapshot of in-force national 법령 of the Republic of Korea` · 신뢰도 low
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 77232자 ≈ 51488 토큰 (viewer statistics, laws/train)
