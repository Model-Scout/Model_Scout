---
datasets:
- Saxo/ko_cn_translation_tech_social_science_linkbricks_single_dataset
- Saxo/ko_jp_translation_tech_social_science_linkbricks_single_dataset
- Saxo/en_ko_translation_tech_science_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/en_ko_translation_social_science_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_aspect_sentiment_sns_mall_sentiment_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_summarization_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/OpenOrca_cleaned_kor_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_government_qa_total_linkbricks_single_dataset_with_prompt_text_huggingface_sampled
- maywell/ko_Ultrafeedback_binarized
language:
- ko
- en
- jp
- cn
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
base_model: NousResearch/Meta-Llama-3.1-8B-Instruct
---

# Model Card for Model ID

<div align="center">
<img src="http://www.linkbricks.com/wp-content/uploads/2024/11/fulllogo.png" />
</div>


AI 전문 기업인 Linkbricks Horizon-AI 의 데이터사이언티스트인 지윤성(Saxo) 대표가 NousResearch/Meta-Llama-3.1-8B-Instruct 베이스모델을 KT-CLOUD상의 H100-80G 4개를 통해 SFT->RLHF->DPO 파인 튜닝을 한
한글 언어 모델로 한국어-중국어-영어-일본어 교차 학습 데이터와 로지컬 데이터를 통하여 한중일영 언어 교차 증강 처리와 복잡한 한글 논리 문제 역시 대응 가능하도록 훈련한 모델이며 토크나이저는 단어 확장 없이 베이스 모델 그대로 사용. 
특히 고객 리뷰나 소셜 포스팅 고차원 분석 및 코딩등이 강화된 모델, 128k-Context Window, Tool Calling 지원 
Deepspeed Stage=3, rslora, flash attention 2 를 사용

CEO Yunsung Ji (Saxo), a data scientist at Linkbricks Horizon-AI, a company specializing in AI and big data analytics, fine-tuned the NousResearch/Meta-Llama-3.1-8B-Instruct base model with SFT->RLHF->DPO using four H100-80Gs on KT-CLOUD.
It is a Korean language model trained to handle complex Korean logic problems through Korean-Chinese-English-Japanese cross-training data and logical data, and Tokenizer uses the base model without word expansion. 


www.linkbricks.com, www.linkbricks.vc
