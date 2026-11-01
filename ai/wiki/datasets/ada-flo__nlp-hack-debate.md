---
type: "dataset"
id: "ada-flo/nlp-hack-debate"
source: "huggingface"
url: "https://huggingface.co/datasets/ada-flo/nlp-hack-debate"
downloads: 7
summary: "영어와 한국어로 된 토론 주제 대화 생성 데이터로, seq2seq 토론 챗봇 학습용입니다."
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
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[Parquet]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# ada-flo/nlp-hack-debate

> dataset · [Hugging Face](https://huggingface.co/datasets/ada-flo/nlp-hack-debate)

영어와 한국어로 된 토론 주제 대화 생성 데이터로, seq2seq 토론 챗봇 학습용입니다.

## 분류

- **작업**: [[텍스트 생성]] — ner · readme = `Bilingual (English + Korean) training data for an LSTM-based seq2seq debate chatbot.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Each record is a (topic, input_context, target_output) triple plus precomputed encoder_input / decoder_input / decoder_target ready for seq2seq training.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Each record is a (topic, input_context, target_output) triple plus precomputed encoder_input / decoder_input / decoder_target ready for seq2seq training.` · 신뢰도 medium
- **언어**: [[영어]] — metadata · languages = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `170` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `cc-by-4.0` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `Bilingual (English + Korean) training data for an LSTM-based seq2seq debate chatbot.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `Bilingual (English + Korean) training data for an LSTM-based seq2seq debate chatbot.` · 신뢰도 medium
- **데이터 형식**: [[Parquet]] — metadata · format = `optimized-parquet` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high

샘플 길이: `encoder_input` 열 p90 254자 ≈ 170 토큰 (viewer statistics, default/validation)
