---
library_name: transformers
license: apache-2.0
base_model: google/gemma-2-27b-it
datasets:
- Saxo/ko_cn_translation_tech_social_science_linkbricks_single_dataset
- Saxo/ko_jp_translation_tech_social_science_linkbricks_single_dataset
- Saxo/en_ko_translation_tech_science_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/en_ko_translation_social_science_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_aspect_sentiment_sns_mall_sentiment_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_summarization_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/OpenOrca_cleaned_kor_linkbricks_single_dataset_with_prompt_text_huggingface
- Saxo/ko_government_qa_total_linkbricks_single_dataset_with_prompt_text_huggingface_sampled
- Saxo/ko-news-corpus-1
- Saxo/ko-news-corpus-2
- Saxo/ko-news-corpus-3
- Saxo/ko-news-corpus-4
- Saxo/ko-news-corpus-5
- Saxo/ko-news-corpus-6
- Saxo/ko-news-corpus-7
- Saxo/ko-news-corpus-8
- Saxo/ko-news-corpus-9
- maywell/ko_Ultrafeedback_binarized
- youjunhyeok/ko-orca-pair-and-ultrafeedback-dpo
- lilacai/glaive-function-calling-v2-sharegpt
- kuotient/gsm8k-ko
language:
- ko
- en
- jp
- cn
pipeline_tag: text-generation
---

# Model Card for Model ID

<div align="center">
<img src="http://www.linkbricks.com/wp-content/uploads/2024/11/fulllogo.png" />
</div>


AI 와 빅데이터 분석 전문 기업인 Linkbricks의 데이터사이언티스트인 지윤성(Saxo) 박사가 <br>
gemma-2-27b-it 베이스모델을 사용해서 H100-80G 8개를 통해 약 38%정도의 파라미터를 한국어 CPT(Continued-Pretraining)->SFT->DPO 한 한글 언어 모델<br>
9천만건의 한글 뉴스 코퍼스를 기준으로 다양한 테스크별 한국어-중국어-영어-일본어 교차 학습 데이터와 수학 및 논리판단 데이터를 통하여 한중일영 언어 교차 증강 처리와 복잡한 논리 문제 역시 대응 가능하도록 훈련한 모델이다.<br> 
-토크나이저는 단어 확장 없이 베이스 모델 그대로 사용<br>
-고객 리뷰나 소셜 포스팅 고차원 분석 및 코딩과 작문, 수학, 논리판단 등이 강화된 모델<br>
-128k-Context Window<br>
-Deepspeed Stage=3, rslora 및 BAdam Layer Mode 사용 <br>
"transformers_version": "4.46.1"
<br><br>

Finetuned by Mr. Yunsung Ji (Saxo), a data scientist at Linkbricks, a company specializing in AI and big data analytics <br>
about 38% of total parameters Korean CPT(Continued-Pretraining)->SFT->DPO training model based on gemma-2-27b-it through 8 H100-80Gs as a Korean language model <br>
It is a model that has been trained to handle Korean-Chinese-English-Japanese cross-training data and 90M korean news corpus and logic judgment data for various tasks to enable cross-fertilization processing and complex Korean logic & math problems. <br>
-Tokenizer uses the base model without word expansion<br>
-Models enhanced with high-dimensional analysis of customer reviews and social posts, as well as coding, writing, math and decision making<br>
-128k-Context Window<br>
-Deepspeed Stage=3, use rslora and BAdam Layer Mode<br>
<br><br>


<a href="www.linkbricks.com">www.linkbricks.com</a>, <a href="www.linkbricks.vc">www.linkbricks.vc</a>
