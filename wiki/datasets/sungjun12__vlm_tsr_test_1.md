---
type: "dataset"
id: "sungjun12/vlm_tsr_test_1"
source: "huggingface"
url: "https://huggingface.co/datasets/sungjun12/vlm_tsr_test_1"
downloads: 37
summary: "테이블 이미지와 정답 HTML로 구성된 구조 유사도 평가용 테스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[리랭킹]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[조건부 이용]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sungjun12/vlm_tsr_test_1

> dataset · [Hugging Face](https://huggingface.co/datasets/sungjun12/vlm_tsr_test_1)

테이블 이미지와 정답 HTML로 구성된 구조 유사도 평가용 테스트 데이터셋입니다.

## 분류

- **작업**: [[리랭킹]] — ner · readme = `TEDS
Tree-Edit Distance 기반 구조 유사도 (0~1)` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `test/source/T01_C01/{id}.jpg    # 테이블 이미지` · 신뢰도 high
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:reranking, task:visual_qa = `test/source/T01_C01/{id}.json   # 정답 HTML + 메타데이터` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:visual_qa = `test/label/T01_C01/{id}.html    # 렌더링용 GT HTML` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `18` · 신뢰도 medium
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `vlm_tsr_test의 1/4 파트` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high

샘플 길이: `file_name` 열 p90 27자 ≈ 18 토큰 (viewer statistics, default/test)
