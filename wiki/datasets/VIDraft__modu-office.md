---
type: "dataset"
id: "VIDraft/modu-office"
source: "huggingface"
url: "https://huggingface.co/datasets/VIDraft/modu-office"
downloads: 28
summary: "광고 없는 한국형 오피스 앱 모두의 오피스(Modu Office)로 HWP, PDF 등 문서 뷰어 제공"
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[도구 호출]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
output_modality:
  - "[[문서 파일 (출력 형식)|문서 파일]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
---
# VIDraft/modu-office

> dataset · [Hugging Face](https://huggingface.co/datasets/VIDraft/modu-office)

광고 없는 한국형 오피스 앱 모두의 오피스(Modu Office)로 HWP, PDF 등 문서 뷰어 제공

## 분류

- **작업**: [[도구 호출]] — ner · readme = `광고 없는 한국형 오피스 — HWP · HWPX · PDF · DOCX 무료 뷰어` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `HWP/HWPX/PDF 파일을 열 때 "모두의 오피스"로 열 수 있습니다.` · 신뢰도 medium
- **출력 형식**: [[문서 파일 (출력 형식)|문서 파일]] — ner · readme = `광고가 전혀 없습니다. 문서는 폰에서 바로 열립니다(오프라인 뷰).` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `광고 없는 한국형 오피스 — HWP · HWPX · PDF · DOCX 무료 뷰어` · 신뢰도 low
