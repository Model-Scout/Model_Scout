---
configs:
- config_name: example-it
  data_files: example-it.csv
- config_name: finqa-50k-merged-quality_filtered
  data_files: finqa-50k-merged-quality_filtered.csv
- config_name: financial-market-law-it
  data_files: financial-market-law-it.csv
- config_name: financial_judgement_instructions
  data_files: financial_judgement_instructions.csv
- config_name: evil-jailbreak-kor-train
  data_files: evil-jailbreak-kor-train.csv
- config_name: evil-jailbreak-kor-test
  data_files: evil-jailbreak-kor-test.csv
- config_name: Finace-Jailbreak-prompt
  data_files: Finace-Jailbreak-prompt.csv
language:
- ko
license:
- cc-by-nc-nd-4.0
tags:
- krx
---
# 제3회 KRX 금융 언어 모델 경진대회 Instruction 데이터셋

- 팀명 : overfit-brothers

### 데이터셋 구성

- example-it
  * KRX-Bench 예시 데이터
  * 출처: KRX-Bench 예시 데이터
- finqa-50k-merged-quality_filtered
  * ConvFinQA-ko
    - fingpt-convfinqa 데이터셋을 샘플링하여 번역한 mncai/finance-tasks-ConvFinQA-ko 의 질문 문장을 gpt-4o API에게 제공하고 CoT 형식의 풀이 데이터 생성
    - 데이터 개수: 26,450
    - [출처]( https://huggingface.co/datasets/mncai/finance-tasks-ConvFinQA-ko?row=0)
    - 라이센스: ConvFinQA-MIT License
  * 튜토리얼Instruction 데이터
    - 경진대회 튜토리얼에서 제공하는 도메인 합성 데이터(with raw text/web text) 2종에 대해 gpt-4o API를 사용하여 퀄리티 1~5점 스케일로 필터링 후 5점을 획득한 샘플로 재구성
    - [출처1](https://huggingface.co/datasets/Cartinoe5930/raw_text_synthetic_dataset_50k) , [출처2](https://huggingface.co/datasets/Cartinoe5930/web_text_synthetic_dataset_50k)
- 금융 판례 기반 instruction 데이터(financial_judgement_instructions)
  * 판결문 sLLM 학습을 위한 데이터(Suchae/korean-judgment-easyread-transform)를 instruction 데이터로 변환
  * 데이터 개수: 5611
  * [출처](https://huggingface.co/datasets/Suchae/korean-judgment-easyread-transform)
  * 라이센스: apache-2.0
- KRX 법규 데이터(financial-market-law-it)
  * KRX 법규서비스 홈페이지에서 공통규정, 유가증권시장규정, 코스닥시장규정, 코넥스시장규정 업무규정에서 규정 데이터 81건 수집 후 gpt-4o API를 활용해 Instruction형식으로 변환
  * 데이터 개수: 81
  * [출처](https://law.krx.co.kr/las/TopFrame.jsp)
- evil-jailbreak-kor
  * Many-shot Jailbreaking, prompt injection을 통해 총 100건의 유해 질문을 생성
  * 기존 유해 질문 데이터셋 번역: Granther/evil-jailbreak, rubend18/ChatGPT-Jailbreak-Prompts
- Finace-Jailbreak-prompt
  * 금융 관련 유해질문에 대한 방어 생성 성능 측정용 데이터셋
  * 출처: 직접 제작