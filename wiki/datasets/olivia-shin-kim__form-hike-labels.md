---
type: "dataset"
id: "olivia-shin-kim/form-hike-labels"
source: "huggingface"
url: "https://huggingface.co/datasets/olivia-shin-kim/form-hike-labels"
downloads: 46
summary: "HiKE 코드스위칭 벤치마크의 한국어 차용어 인식 및 형태 평가용 라벨 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[음성 인식]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# olivia-shin-kim/form-hike-labels

> dataset · [Hugging Face](https://huggingface.co/datasets/olivia-shin-kim/form-hike-labels)

HiKE 코드스위칭 벤치마크의 한국어 차용어 인식 및 형태 평가용 라벨 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Labels for scoring Korean loanwords in the HiKE code-switching benchmark by recognition in any accepted written form and by the form produced` · 신뢰도 low
- **작업**: [[음성 인식]] — metadata · task_categories = `automatic-speech-recognition` · 신뢰도 low
- **입력 형식**: [[음성 (입력 형식)|음성]] — task_rule · task:speech_recognition = `audio` · 신뢰도 medium
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:classification = `offsets refer to HiKE's `text` field and `utt_id` to its `sample_id`` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:speech_recognition = `These labels let a transcript be scored for whether the item was recognized at all and, separately, which form it was written in.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `11` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `HiKE code-switching benchmark` · 신뢰도 low
- **데이터 용도**: [[평가용]] — ner · dataset_id/tags, readme = `All configurations have one split, `test`.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `type_key` 열 p90 16자 ≈ 11 토큰 (viewer statistics, accept_sets/test)
