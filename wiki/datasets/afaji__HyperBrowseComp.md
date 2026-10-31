---
type: "dataset"
id: "afaji/HyperBrowseComp"
source: "huggingface"
url: "https://huggingface.co/datasets/afaji/HyperBrowseComp"
downloads: 101
summary: "HyperBrowseComp는 13개 언어로 된 웹 브라우징 에이전트 평가용 다국어·다중모달 스트레스 테스트 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[질의응답]]"
input_modality:
  - "[[문서 파일 (입력 형식)|문서 파일]]"
  - "[[위치·좌표 (입력 형식)|위치·좌표]]"
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# afaji/HyperBrowseComp

> dataset · [Hugging Face](https://huggingface.co/datasets/afaji/HyperBrowseComp)

HyperBrowseComp는 13개 언어로 된 웹 브라우징 에이전트 평가용 다국어·다중모달 스트레스 테스트 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — ner · readme = `The paper's filtered benchmark contains 423 manually authored and human-validated questions across 13 languages.` · 신뢰도 low
- **입력 형식**: [[문서 파일 (입력 형식)|문서 파일]] — ner · readme = `following several clues across obscure webpages, videos, scanned documents, images, or maps.` · 신뢰도 medium
- **입력 형식**: [[위치·좌표 (입력 형식)|위치·좌표]] — ner · readme = `following several clues across obscure webpages, videos, scanned documents, images, or maps.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — ner · readme = `following several clues across obscure webpages, videos, scanned documents, images, or maps.` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `questions across 13 languages` · 신뢰도 high
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · readme = `following several clues across obscure webpages, videos, scanned documents, images, or maps.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Each question has a short, publicly verifiable answer` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `13 languages` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-sa-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `The benchmark tests whether agents can persistently find and connect evidence on the open web.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `The `test` split is the paper's **423-question release**` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `parquet` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high
