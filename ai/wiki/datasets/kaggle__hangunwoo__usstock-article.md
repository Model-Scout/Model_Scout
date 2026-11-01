---
type: "dataset"
id: "kaggle/hangunwoo/usstock-article"
source: "kaggle"
url: "https://www.kaggle.com/datasets/hangunwoo/usstock-article"
downloads: 40
summary: "dcinside '미국 주식 갤러리'의 한국어 주식 관련 기사 데이터셋으로 감성 분석 포함"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
  - "[[정보 추출]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# kaggle/hangunwoo/usstock-article

> dataset · [Kaggle](https://www.kaggle.com/datasets/hangunwoo/usstock-article)

dcinside '미국 주식 갤러리'의 한국어 주식 관련 기사 데이터셋으로 감성 분석 포함

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `sentiment analysis by positive / negative / neutral was also performed` · 신뢰도 medium
- **작업**: [[정보 추출]] — ner · readme = `each article has been evaluated by Gemini 2.5 flash for relevance to US stocks` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:information_extraction = `This is a korean article dataset` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `sentiment analysis by positive / negative / neutral was also performed` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `MIT` · 신뢰도 high
- **도메인**: [[금융·경제]] — ner · readme = `relevance to US stocks` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `There is over 60k+ article data` · 신뢰도 low
