---
configs:
- config_name: example-mcqa
  data_files: example-mcqa.csv
- config_name: account_calc
  data_files: account_calc.csv
- config_name: financial_market_augmented
  data_files: financial_market_augmented.csv
- config_name: financial_mmlu_augmented
  data_files: financial_mmlu_augmented.csv
- config_name: krx-textbook
  data_files: krx-textbook.csv
- config_name: mmmlu_revised_augmented_cot-2mask
  data_files: mmmlu_revised_augmented_cot-2mask.csv
- config_name: mmmlu_revised_augmented_cot-poe
  data_files: mmmlu_revised_augmented_cot-poe.csv
- config_name: mmmlu_revised_augmented_cot
  data_files: mmmlu_revised_augmented_cot.csv
language:
- ko
license:
- cc-by-nc-nd-4.0
tags:
- krx
---

# 제3회 KRX 금융 언어 모델 경진대회 MCQA 데이터셋

- 팀명 : overfit-brothers

### 데이터셋 구성

- example-mcqa
  * KRX-Bench 예시 데이터
  * 출처: KRX-Bench 예시 데이터
- account_calc
  * 회계원리 수준 MCQA 계산문제 seed 데이터 37건을 직접 제작한 후 gpt-4o API를 통해 증강
  * 데이터 개수: 222
  * 출처: 자체 제작
- KRX 법규 데이터(financial_market_augmented)
  * 금융 도메인의 다중 선택(Multiple Choice) 데이터셋 allganize/financial-mmlu-ko에 대해서 정답을 제공하지 않고 gpt-4o로 CoT 형식의 해설을 만들어 제작
  * 데이터 개수 : 1063
  * 라이센스: Wikipedia: CC BY-SA 4.0, 한국은행 저작권 보호방침: 공공데이터법

- financial_mmlu_augmented
  * 금융 도메인의 다중 선택(Multiple Choice) 데이터셋 allganize/financial-mmlu-ko에 대해서 정답을 제공하지 않고 gpt-4o로 CoT 형식의 해설을 만들어 제작
  * 데이터 개수: 1063
  * [출처]( https://huggingface.co/datasets/allganize/financial-mmlu-ko)
  * 라이센스: Wikipedia: CC BY-SA 4.0, 한국은행 저작권 보호방침: 공공데이터법
    
- 한국거래소 교육자료 데이터(krx-textbook)
  * 한국거래소에서 발간한 e-book ‘초보투자자를 위한 증권과 투자 따락잡기’ pdf에서 문제 생성
  * 데이터 개수: 212
  * 출처 : [KRX Academy](https://main.krxverse.co.kr/ )

- mmmlu_revised_augmented_cot,2mask,poe)
  * 전문 번역가가 14개국어로 번역한 데이터셋인 openai/MMMLU에서 한국어 부분을 추출한 뒤 econometrics, high_school_macroeconomics. high_school_microenocomics, management,  marketing, business_ethics 스플릿을 추출하여 형식에 맞게 재구성, gpt-4o API 를 통해 CoT, POE, 2mask 형식 답변 생성
  * 데이터 개수: 6986
  * 출처:  https://huggingface.co/datasets/openai/MMMLU
  * 라이센스:  MIT