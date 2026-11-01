---
type: "dataset"
id: "dancinlab/anima-chat-corpus-mix-70wiki-30dialogue"
source: "huggingface"
url: "https://huggingface.co/datasets/dancinlab/anima-chat-corpus-mix-70wiki-30dialogue"
downloads: 33
summary: "70% 위키피디아와 30% 실제 대화로 구성된 바이트 수준 챗봇 학습용 코퍼스입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_with_others"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[일본어]]"
  - "[[한국어]]"
  - "[[다국어]]"
  - "[[ru]]"
  - "[[중국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
data_format:
  - "[[텍스트 파일]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# dancinlab/anima-chat-corpus-mix-70wiki-30dialogue

> dataset · [Hugging Face](https://huggingface.co/datasets/dancinlab/anima-chat-corpus-mix-70wiki-30dialogue)

70% 위키피디아와 30% 실제 대화로 구성된 바이트 수준 챗봇 학습용 코퍼스입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `chat-capable LADDER rung-0 (≈18M byte transformer)` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `byte-level (vocab 256) corpus` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `byte-level continuation format `사용자: | 도우미: `` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · languages = `ja` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `5 languages` · 신뢰도 high
- **언어**: [[ru]] — metadata · languages = `ru` · 신뢰도 high
- **언어**: [[중국어]] — metadata · languages = `zh` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `53` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `5-language aphorisms (en·zh·ru·ja·ko), the backbone the d768 production model trained on.` · 신뢰도 low
- **데이터 형식**: [[텍스트 파일]] — metadata · format = `text` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 213자 ≈ 53 토큰 (viewer statistics, default/train)
