---
type: "dataset"
id: "sungjun12/vlm_tsr_test_4"
source: "huggingface"
url: "https://huggingface.co/datasets/sungjun12/vlm_tsr_test_4"
downloads: 223
summary: "테이블 이미지와 HTML 정답으로 구성된 VLM TSR 테스트 데이터셋 4/4 파트입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[정보 추출]]"
  - "[[리랭킹]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[문서 파일 (출력 형식)|문서 파일]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[미디어 파일]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# sungjun12/vlm_tsr_test_4

> dataset · [Hugging Face](https://huggingface.co/datasets/sungjun12/vlm_tsr_test_4)

테이블 이미지와 HTML 정답으로 구성된 VLM TSR 테스트 데이터셋 4/4 파트입니다.

## 분류

- **작업**: [[정보 추출]] — ner · readme = `test/source/T01_C01/{id}.json   # 정답 HTML + 메타데이터` · 신뢰도 low
- **작업**: [[리랭킹]] — ner · readme = `TEDS
Tree-Edit Distance 기반 구조 유사도 (0~1)` · 신뢰도 low
- **작업**: [[이미지 이해]] — metadata · task_categories = `image-to-text` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · modality, readme, task:visual_qa = `test/source/T01_C01/{id}.jpg    # 테이블 이미지` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:information_extraction, task:reranking, task:visual_qa = `test/source/T01_C01/{id}.json   # 정답 HTML + 메타데이터` · 신뢰도 medium
- **출력 형식**: [[문서 파일 (출력 형식)|문서 파일]] — ner · readme = `test/label/T01_C01/{id}.html    # 렌더링용 GT HTML` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `vlm_tsr_test의 4/4 파트. scene 그룹 57xxx~63xxx 포함.` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `전체 테스트셋은 4개 레포로 나뉘어 있습니다` · 신뢰도 medium
- **데이터 형식**: [[미디어 파일]] — metadata · format = `imagefolder` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
