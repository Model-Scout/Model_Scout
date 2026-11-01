---
type: "dataset"
id: "joonhok-exo-ai/korean_law_case_codes"
source: "huggingface"
url: "https://huggingface.co/datasets/joonhok-exo-ai/korean_law_case_codes"
downloads: 17
summary: "사건별 부호문자 규정에 따른 전체 사건부호 데이터셋으로 법률 AI 서비스에 활용됨."
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
  - "[[조건부 이용]]"
domain:
  - "[[법률]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[CSV]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# joonhok-exo-ai/korean_law_case_codes

> dataset · [Hugging Face](https://huggingface.co/datasets/joonhok-exo-ai/korean_law_case_codes)

사건별 부호문자 규정에 따른 전체 사건부호 데이터셋으로 법률 AI 서비스에 활용됨.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `이 데이터셋은 인공지능 법률 서비스를 만들고 있는 제가 직접 필요해서 만들게 되었습니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `사건별 부호문자의 부여에 관한 예규(재일 2003-1, 재판예규 제1769호)에서 규정한 전체 사건부호 데이터셋입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `사건별 부호문자의 부여에 관한 예규(재일 2003-1, 재판예규 제1769호)에서 규정한 전체 사건부호 데이터셋입니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `10` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `openrail` · 신뢰도 high
- **도메인**: [[법률]] — tag_match · readme, tags = `legal` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `이 데이터셋은 인공지능 법률 서비스를 만들고 있는 제가 직접 필요해서 만들게 되었습니다.` · 신뢰도 low
- **데이터 형식**: [[CSV]] — metadata · format = `csv` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `사건종류` 열 p90 15자 ≈ 10 토큰 (viewer statistics, default/train)
