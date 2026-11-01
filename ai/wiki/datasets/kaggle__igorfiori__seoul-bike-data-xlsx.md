---
type: "dataset"
id: "kaggle/igorfiori/seoul-bike-data-xlsx"
source: "kaggle"
url: "https://www.kaggle.com/datasets/igorfiori/seoul-bike-data-xlsx"
downloads: 33
summary: "서울시 공공자전거 대여 시간별 이용량과 기상 정보를 담은 데이터셋으로 수요 예측에 활용 가능"
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[시계열 예측]]"
input_modality:
  - "[[시계열 (입력 형식)|시계열]]"
output_modality:
  - "[[표 (출력 형식)|표]]"
  - "[[시계열 (출력 형식)|시계열]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[교통·모빌리티]]"
---
# kaggle/igorfiori/seoul-bike-data-xlsx

> dataset · [Kaggle](https://www.kaggle.com/datasets/igorfiori/seoul-bike-data-xlsx)

서울시 공공자전거 대여 시간별 이용량과 기상 정보를 담은 데이터셋으로 수요 예측에 활용 가능

## 분류

- **작업**: [[시계열 예측]] — ner · readme = `Este dataset permite explorar essas relações e construir modelos preditivos para antecipar a demanda.` · 신뢰도 low
- **입력 형식**: [[시계열 (입력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **출력 형식**: [[표 (출력 형식)|표]] — ner · readme = `A variável alvo. É a contagem total de bicicletas alugadas naquela hora.` · 신뢰도 low
- **출력 형식**: [[시계열 (출력 형식)|시계열]] — task_rule · task:forecasting = `time_series` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `CC BY-SA 4.0` · 신뢰도 high
- **도메인**: [[교통·모빌리티]] — ner · readme = `O uso de sistemas de compartilhamento de bicicletas públicas explodiu em todo o mundo, tornando-se uma peça chave da mobilidade urbana sustentável.` · 신뢰도 low
