---
type: "model"
id: "Saxo/Linkbricks-Horizon-AI-Korean-llama3.1-sft-dpo-70B"
source: "huggingface"
url: "https://huggingface.co/Saxo/Linkbricks-Horizon-AI-Korean-llama3.1-sft-dpo-70B"
downloads: 121
context_length: 131072
parameters_b: 70.554
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
  - "[[중국어]]"
input_length:
  - "[[초장문]]"
commercial_use:
  - "[[상업 이용 가능]]"
model_size:
  - "[[대형 모델]]"
---
# Saxo/Linkbricks-Horizon-AI-Korean-llama3.1-sft-dpo-70B

> model · [Hugging Face](https://huggingface.co/Saxo/Linkbricks-Horizon-AI-Korean-llama3.1-sft-dpo-70B)

## 분류

- **작업**: [[텍스트 생성]] — metadata · task.matched = `text-generation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:generation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[일본어]] — metadata · language_codes = `jp` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · language_codes = `4 languages` · 신뢰도 high
- **언어**: [[중국어]] — metadata · language_codes = `cn` · 신뢰도 high
- **입력 길이**: [[초장문]] — metadata · context_length = `131072` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **모델 크기**: [[대형 모델]] — metadata · parameter_count_billion = `70.554` · 신뢰도 high

처리 가능한 데이터 길이: [[단문]] · [[중문]] · [[장문]] · [[초장문]]

## 학습 데이터

- [[Saxo__OpenOrca_cleaned_kor_linkbricks_single_dataset_with_prompt_text_huggingface|Saxo/OpenOrca_cleaned_kor_linkbricks_single_dataset_with_prompt_text_huggingface]]
- [[Saxo__en_ko_translation_social_science_linkbricks_single_dataset_with_prompt_text_huggingface|Saxo/en_ko_translation_social_science_linkbricks_single_dataset_with_prompt_text_huggingface]]
- [[Saxo__en_ko_translation_tech_science_linkbricks_single_dataset_with_prompt_text_huggingface|Saxo/en_ko_translation_tech_science_linkbricks_single_dataset_with_prompt_text_huggingface]]
- [[Saxo__ko_aspect_sentiment_sns_mall_sentiment_linkbricks_single_dataset_with_prompt_text_huggingface|Saxo/ko_aspect_sentiment_sns_mall_sentiment_linkbricks_single_dataset_with_prompt_text_huggingface]]
- [[Saxo__ko_cn_translation_tech_social_science_linkbricks_single_dataset|Saxo/ko_cn_translation_tech_social_science_linkbricks_single_dataset]]
- [[Saxo__ko_government_qa_total_linkbricks_single_dataset_with_prompt_text_huggingface_sampled|Saxo/ko_government_qa_total_linkbricks_single_dataset_with_prompt_text_huggingface_sampled]]
- [[Saxo__ko_jp_translation_tech_social_science_linkbricks_single_dataset|Saxo/ko_jp_translation_tech_social_science_linkbricks_single_dataset]]
- [[Saxo__ko_summarization_linkbricks_single_dataset_with_prompt_text_huggingface|Saxo/ko_summarization_linkbricks_single_dataset_with_prompt_text_huggingface]]
- [[maywell__ko_Ultrafeedback_binarized|maywell/ko_Ultrafeedback_binarized]]
