---
type: "dataset"
id: "nlpai-lab/openassistant-guanaco-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/nlpai-lab/openassistant-guanaco-ko"
downloads: 105
summary: "Open Assistant 데이터셋의 한국어 번역본으로, 대화 모델 학습에 사용됨"
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
  - "[[질의응답]]"
  - "[[요약]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nlpai-lab/openassistant-guanaco-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/nlpai-lab/openassistant-guanaco-ko)

Open Assistant 데이터셋의 한국어 번역본으로, 대화 모델 학습에 사용됨

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **작업**: [[질의응답]] — metadata · task_categories = `question-answering` · 신뢰도 low
- **작업**: [[요약]] — metadata · task_categories = `summarization` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:question_answering, task:summarization = `Korean translation of Guanaco via the DeepL API` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:question_answering, task:summarization = `Korean translation of Guanaco via the DeepL API` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `999` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This dataset is a subset of the Open Assistant dataset` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `This dataset was used to train Guanaco with QLoRA.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 1498자 ≈ 999 토큰 (viewer statistics, default/test)
