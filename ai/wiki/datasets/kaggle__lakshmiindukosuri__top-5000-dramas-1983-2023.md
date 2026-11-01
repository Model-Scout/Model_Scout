---
type: "dataset"
id: "kaggle/lakshmiindukosuri/top-5000-dramas-1983-2023"
source: "kaggle"
url: "https://www.kaggle.com/datasets/lakshmiindukosuri/top-5000-dramas-1983-2023"
downloads: 463
summary: "1983년부터 2023년까지 한국, 일본, 중국, 대만, 태국의 상위 5000 아시아 드라마 정보를 담은 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[문서 검색]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/lakshmiindukosuri/top-5000-dramas-1983-2023

> dataset · [Kaggle](https://www.kaggle.com/datasets/lakshmiindukosuri/top-5000-dramas-1983-2023)

1983년부터 2023년까지 한국, 일본, 중국, 대만, 태국의 상위 5000 아시아 드라마 정보를 담은 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `providing a rich source of information on a wide array of dramas from different cultures and time periods` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `Explore the world of Asian television with this comprehensive dataset featuring the top 5000 dramas` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `Columns : **Name**: The title of the drama. **Episodes**: The number of episodes in the drama series. **Released Year**: The year when the drama was originally ` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:retrieval = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `Columns : **Name**: The title of the drama. **Episodes**: The number of episodes in the drama series. **Released Year**: The year when the drama was originally ` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license = `Unknown` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `Explore the world of Asian television with this comprehensive dataset featuring the top 5000 dramas from five different languages - Korean, Japanese, Chinese, T` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset is a treasure trove for enthusiasts, researchers, and analysts interested in Asian television` · 신뢰도 low
