---
license: cc-by-nc-4.0
language:
- en
- ko
---

---
## Developed by : 
* K2S3

## Model Number:
* K2S3-Mistral-7b-v1.1

## Base Model : 
* mistralai/Mistral-7B-v0.1

### Training Data
* The training data for this model includes alpaca-gpt4-data, and samples from The OpenOrca Dataset.
* 이 모델의 훈련 데이터에는 alpaca-gpt4-data, 그리고 OpenOrca Dataset에서 제공한 샘플들이 포함됩니다.

### Training Method
* This model was fine-tuned on the "mistralai/Mistral-7B-v0.1" base model using a full parameter tuning method with SFT (Supervised Fine-Tuning).
* 이 모델은 "mistralai/Mistral-7B-v0.1" 기반 모델을 SFT를 사용하여 전체 파라미터 조정 방법으로 미세조정되었습니다.

### Hardware
* Hardware: Utilized two A100 (80G*2EA) GPUs for training.
* Training Factors: This model was fine-tuned with SFT, using the HuggingFace SFTtrainer and applied fsdp. 
* 이 모델은 SFT를 사용하여 HuggingFace SFTtrainer와 fsdp를 적용하여 미세조정되었습니다.