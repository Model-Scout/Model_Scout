---
type: "dataset"
id: "kaggle/kimjihoo/coronavirusdataset"
source: "kaggle"
url: "https://www.kaggle.com/datasets/kimjihoo/coronavirusdataset"
downloads: 145701
summary: "한국 코로나19 확진자 관련 KCDC 자료 기반 구조화 데이터셋으로 분석 및 시각화에 활용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[임베딩]]"
  - "[[정보 추출]]"
  - "[[이미지 이해]]"
input_modality:
  - "[[이미지 (입력 형식)|이미지]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[비상업 전용]]"
domain:
  - "[[의료·보건]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/kimjihoo/coronavirusdataset

> dataset · [Kaggle](https://www.kaggle.com/datasets/kimjihoo/coronavirusdataset)

한국 코로나19 확진자 관련 KCDC 자료 기반 구조화 데이터셋으로 분석 및 시각화에 활용됨

## 분류

- **작업**: [[임베딩]] — ner · readme = `We make a structured dataset based on the report materials of KCDC and local governments.` · 신뢰도 low
- **작업**: [[정보 추출]] — ner · readme = `We make a structured dataset based on the report materials of KCDC and local governments.` · 신뢰도 low
- **작업**: [[이미지 이해]] — ner · readme = `we analyze and visualize the data using various data mining or visualization techniques.` · 신뢰도 low
- **입력 형식**: [[이미지 (입력 형식)|이미지]] — task_rule · task:visual_qa = `image` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — ner · readme = `We make a structured dataset based on the report materials of KCDC and local governments.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:embedding, task:information_extraction, task:visual_qa = `text` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `We make a structured dataset based on the report materials of KCDC and local governments.` · 신뢰도 low
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:visual_qa = `text` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[비상업 전용]] — metadata · license = `CC BY-NC-SA 4.0` · 신뢰도 high
- **도메인**: [[의료·보건]] — ner · readme = `COVID-19 has infected more than 10,000 people in South Korea.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `We make a structured dataset based on the report materials of KCDC and local governments.` · 신뢰도 low
