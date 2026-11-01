---
type: "dataset"
id: "heegyu/korean-petitions"
source: "huggingface"
url: "https://huggingface.co/datasets/heegyu/korean-petitions"
downloads: 338
summary: "청와대 국민청원 데이터를 모은 것으로, 청원 내용 분석에 활용 가능하다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "not_ko"
task:
  - "[[텍스트 분류]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[행정·민원]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# heegyu/korean-petitions

> dataset · [Hugging Face](https://huggingface.co/datasets/heegyu/korean-petitions)

청와대 국민청원 데이터를 모은 것으로, 청원 내용 분석에 활용 가능하다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `"category": "반려동물"` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `청와대 국민청원` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification, task:retrieval = `"content": "길고양이들 밥주고있는 사람입니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `"category": "반려동물"` · 신뢰도 low
- **입력 길이**: [[초장문]] — viewer_stats · viewer_statistics = `37253` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `mit` · 신뢰도 high
- **도메인**: [[행정·민원]] — ner · readme = `청와대 국민청원` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `데이터 출처: https://github.com/lovit/petitions_archive` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `content` 열 p90 149013자 ≈ 37253 토큰 (viewer statistics, default/train)

## 이 데이터로 학습한 모델

- [[heegyu__ajoublue-gpt2-base-24L|heegyu/ajoublue-gpt2-base-24L]]
- [[heegyu__kogpt-j-350m|heegyu/kogpt-j-350m]]
- [[heegyu__kogpt-j-base|heegyu/kogpt-j-base]]
- [[heegyu__kogpt-j-base-24L|heegyu/kogpt-j-base-24L]]
