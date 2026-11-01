---
type: "dataset"
id: "naplab/AVMeme-Exam"
source: "huggingface"
url: "https://huggingface.co/datasets/naplab/AVMeme-Exam"
downloads: 118
summary: "AVMeme-Exam은 멀티모달 대형언어모델의 오디오-비주얼 밈 이해 능력을 평가하는 벤치마크입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 분류]]"
  - "[[질의응답]]"
input_modality:
  - "[[음성 (입력 형식)|음성]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
  - "[[영상 (입력 형식)|영상]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[hi]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[중국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[평가용]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# naplab/AVMeme-Exam

> dataset · [Hugging Face](https://huggingface.co/datasets/naplab/AVMeme-Exam)

AVMeme-Exam은 멀티모달 대형언어모델의 오디오-비주얼 밈 이해 능력을 평가하는 벤치마크입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `Multiple-choice question designed to test meme understanding` · 신뢰도 low
- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[음성 (입력 형식)|음성]] — ner · modality, readme = `Audio, video, and text` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification, task:question_answering = `Audio, video, and text` · 신뢰도 medium
- **입력 형식**: [[영상 (입력 형식)|영상]] — ner · modality, readme = `Audio, video, and text` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `Multiple-choice question designed to test meme understanding` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[hi]] — metadata · languages = `hi` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `multimodal benchmark for testing whether multimodal large language models (MLLMs) can really understand audio-visual memes` · 신뢰도 low
- **데이터 용도**: [[평가용]] — name_rule · dataset_id/tags = `evaluation` · 신뢰도 medium
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `9999.0` · 신뢰도 high
