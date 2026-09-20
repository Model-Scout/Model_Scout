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
- maywell/ko_Ultrafeedback_binarized
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
<br>
<a href="https://huggingface.co/spaces/upstage/open-ko-llm-leaderboard">Open Ko LLM Leaderboard Season 2</a> 🏆 Rank-1 2024/11/01~2024/12/28
<br>
<br>
<br>
AI 와 빅데이터 분석 전문 기업인 Linkbricks Horizon-AI의 데이터사이언티스트인 지윤성(Saxo) 대표가 gemma-2-27b-it 베이스모델을 H100-80G 8개를 통해 SFT->DPO 파인 튜닝을 한
한글 언어 모델로 한국어-중국어-영어-일본어 교차 학습 데이터와 로지컬 데이터를 통하여 한중일영 언어 교차 증강 처리와 복잡한 한글 논리 문제 역시 대응 가능하도록 훈련한 모델이며 토크나이저는 단어 확장 없이 베이스 모델 그대로 사용. 
특히 고객 리뷰나 소셜 포스팅 고차원 분석 및 코딩과 욕설, 비방, 음란물, 성적으로 노골적인 콘텐츠, 인종차별 또는 기타 유해 콘텐츠 탐지
개인정보 및 민감정보 패턴 탐지, 차단 또는 사용자 경고가 필요할 수 있는 기타 고위험 요청 탐지 강화된 모델<br>
-Deepspeed Stage=3, rslora 및 BAdam Layer Mode 사용<br>
Linkbricks Horizon-AI CEO and data scientist Yunsung Ji (Saxo) developed a Korean-specialized large language model based on Gemma-2-27B-IT, fine-tuned through a two-stage SFT → DPO pipeline using eight NVIDIA H100 80GB GPUs.
The model was trained on cross-lingual datasets spanning Korean, Chinese, English, and Japanese, together with logical reasoning datasets. This enables cross-lingual knowledge augmentation and reasoning across all four languages, while significantly improving its ability to handle complex Korean-language logical reasoning tasks.
The model retains the original Gemma-2-27B-IT tokenizer without additional vocabulary expansion, preserving compatibility with the base model architecture.
It is particularly optimized for high-dimensional analysis of customer reviews and social media posts, as well as coding and content-safety applications. Its safety capabilities have been strengthened to detect potentially harmful content, including profanity, harassment and defamation, sexually explicit or obscene material, racist or discriminatory content, and other forms of harmful content.
The model also provides enhanced detection of personally identifiable information (PII) and sensitive-information patterns, along with improved identification of high-risk requests that may require blocking, additional safeguards, or user warnings.
-ollama run benedict/linkbricks-gemma2-korean:27b
<br>
Benchmark (Open Ko LLM Leader  Board Season 2 : No. 1)<br>
Model : Saxo/Linkbricks-Horizon-AI-Korean-Gemma-2-sft-dpo-27B<br>
Average  : 51.37<br>
Ko-GPQA : 25.25<br>
Ko-Winogrande : 68.27<br>
Ko-GSM8k : 70.96<br>
Ko-EQ Bench : 50.25<br>
Ko-IFEval : 49.84<br>
KorNAT-CKA : 34.59<br>
KorNAT-SVA : 48.42<br>
Ko-Harmlessness : 65.66<br>
Ko-Helpfulness : 49.12<br>
<div align="center">
<img src="http://www.linkbricks.com/wp-content/uploads/2024/12/스크린샷-2024-12-16-오전-10.43.06.png" />
</div>

<br>


<br><br>

CEO Yunsung Ji (Saxo), a data scientist at Linkbricks Horizon-AI, a company specializing in AI and big data analytics, fine-tuned the gemma-2-27b-it base model with SFT->DPO using four H100-80Gs.
It is a Korean language model trained to handle complex Korean logic problems through Korean-Chinese-English-Japanese cross-training data and logical data, and Tokenizer uses the base model without word expansion. 


<a href="www.horizonai.ai">www.horizonai.ai</a>, <a href="www.linkbricks.com">www.linkbricks.com</a>, <a href="www.linkbricks.vc">www.linkbricks.vc</a>
