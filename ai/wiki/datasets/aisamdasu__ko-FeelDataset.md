---
type: "dataset"
id: "aisamdasu/ko-FeelDataset"
source: "huggingface"
url: "https://huggingface.co/datasets/aisamdasu/ko-FeelDataset"
downloads: 14
summary: "한국어 일상 발화에 담긴 감정을 라벨링한 44,887개 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[일반]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# aisamdasu/ko-FeelDataset

> dataset · [Hugging Face](https://huggingface.co/datasets/aisamdasu/ko-FeelDataset)

한국어 일상 발화에 담긴 감정을 라벨링한 44,887개 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — metadata · readme, task_categories = `text-classification` · 신뢰도 medium
- **작업**: [[텍스트 생성]] — tag_match · tags = `conversational` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:generation = `한국어 일상 발화 한두 문장에 담긴 감정을 라벨링한 44,887개의 데이터셋입니다.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = ``assistant`의 content는 아래 4개 키를 가진 JSON 문자열입니다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `가족·연애·직장·이별·육아·건강·돈·학교·반려동물·명절 등 아주 다양한 일상 장면에서 나오는 감정.` · 신뢰도 low
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
