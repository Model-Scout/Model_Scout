---
license: cc-by-nc-4.0
task_categories:
- reinforcement-learning
- text-generation
language:
- ko
tags:
- RLHF
- SFT
- RM
- instruction-tuning
- reward-model
- PPO
---

## KULLM을 baseline으로 RLHF 강화학습을 하는데 사용한 데이터셋입니다.
- **Step1: step1_SFT_train.jsonl** (KULLM 12.8B 모델을 Supervised Fine-Tuning 하는데 사용하였습니다.)
- **Step2: step2_RM_train.json** (polyglot-ko 1.3B 모델을 Reward Model로 학습하는데 사용하였습니다.)
- **Step3: step3_PPO_train.json** (SFT 모델과 RM 모델을 사용하여 RLHF 학습을 하는데 사용하였습니다.)
자세한 정보는 다음을 참고해주세요: https://huggingface.co/Trofish/KULLM-RLHF

## 강화학습 단계별 데이터셋 구축
![image](https://github.com/VAIV-2023/VAIV2023/assets/79634774/a4988abd-c6fd-4fc2-8e53-9a02240e2275)
![image](https://github.com/VAIV-2023/VAIV2023/assets/79634774/dae49a1e-a834-463c-9f95-34cf254fdaeb)

## 데이터셋 선정 시 고려 사항
- **일상 대화와 혐오 표현 대처 능력을 올리기 위한 데이터셋과, 학습 시 챗봇 모델의 general한 task에 대한 성능이 하락하는 것을 막기 위해서 general task 데이터셋을 구성**
  
- **국립국어원 일상 대화 데이터셋:** 일상적인 대화에 대한 자연스러운 응답이 있으면서도, 맞춤법이 잘 지켜지고 은어, 비문, 초성 등이 없으며 주제별로 다양한 대화가 있음
  
- **AI Hub 혐오 표현 데이터셋:** 혐오, 차별, 성적인 내용, 폭력, 범죄 등 카테고리별로 다양한 혐오 표현이 있음
  
- **General task 데이터셋**
    - Evol-Instruct 데이터셋: 다양한 분야에 대한 복잡하고 논리적인 prompt와 답변이 있음
    - Self-Instruct 데이터셋: 사람이 직접 생성한 양질의 Seed data를 기반으로 데이터 증강
    - RLHF 한국어 번역 데이터셋: DeepSpeedChat에서 공개한 데이터셋을 한국어로 번역
      
# Step1. SFT 모델 Fine-tuning
## Baseline Model
[- 고려대학교 NLP & AI 연구실과 HIAI 연구소가 개발한 한국어 LLM **"KULLM"** 사용](https://github.com/nlpai-lab/KULLM)

## Datasets
![image](https://github.com/VAIV-2023/VAIV2023/assets/79634774/085610db-3714-43c3-855b-58baad2f4e8b)

# Step2. Reward Model ver1 구현
## Baseline Model
- EleutherAI에서 개발한 초거대 한국어 언어 모델 **Polyglot-Ko** 사용
- 1.3b 모델과 5.8b 모델을 각각 실험
## Datasets
![image](https://github.com/VAIV-2023/RLHF-Korean-Friendly-LLM/assets/79634774/0082da9b-b0b8-4089-8647-cffa5ce724fb)
- InstructGPT의 데이터셋 구축 방법
    - Reward 모델 학습 데이터셋으로 SFT 학습에 사용한 prompt(1,500개 - 일상대화:혐오표현=2:1)와 새로운 prompt(1,000개 - DeepSpeedChat 번역 데이터셋) 사용 
    - SFT 모델에서 한개의 prompt당 K개의 Response를 생성하고, 순위를 Labeling
- 데이터셋 라벨링
    - Instruct GPT의 경우 사람이 직접 Labeling을 하엿지만, 일관된 평가와 시간 단축을 위해 GPt-4와 G-Eval을 이용
    - SFT에서 생성한 두 Response 중 G-Eval 평가 점수 합이 높은 것을 Chosen response로 결정
    - 데이터셋 유형별로 G-Eval 평가 Prompt에 차이를 두었음
    -   ![image](https://github.com/VAIV-2023/RLHF-Korean-Friendly-LLM/assets/79634774/7d7117d0-02e9-42dd-8ce3-5244cf726bf8)

## RLFH Model Evaluation
![image](https://github.com/VAIV-2023/VAIV2023/assets/79634774/2b58ed3a-7ed5-4e60-ba4b-c9b291b1fdff)
![image](https://github.com/VAIV-2023/VAIV2023/assets/79634774/75b2a1ee-d7c0-4ba9-ab2f-727abab644e9)

## Final RLHF Model
- https://huggingface.co/Trofish/KULLM-RLHF
