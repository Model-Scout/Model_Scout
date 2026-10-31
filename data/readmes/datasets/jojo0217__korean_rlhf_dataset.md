---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
---

성균관대학교 산학협력프로젝트 과정에서 한국어 llm 모델 SFT 학습을 위해 구축한 데이터셋 입니다.   
2023-09-25   
오픈 어시스턴트 data에서 오픈 어시스턴트를 포함하는 데이터 삭제   
-> 답변에 오픈 어시스턴트라고 하는 경우가 나오기 때문   
또한 스탠포드 대학 번역 데이터에서 번역 과정 오류로 input에 입력없음 과 같이 추가된 부분 삭제   
그리고 \<unk\> 등으로 gpt 상에서 번역 오류가 난 것들을 삭제   
***
자연스러움을 위해 stanford alpaca data, oig_chip2를 ChatGPT3.5 turbo 16k를 이용하여 새롭게 전처리 과정을 거쳤습니다.   
https://github.com/JoJo0217/rlhf_korean_dataset/tree/main   
여기에서 자세한 설명을 볼 수 있으며   
데이터의 구성은 다음과 같습니다.   
***
데이터 구성   
|데이터 종류|개수|url|
|:---|---:|---:|
|koalpaca v1.1|21155|https://github.com/Beomi/KoAlpaca|
|stanford alpaca|51374|https://huggingface.co/datasets/tatsu-lab/alpaca|
|dolly|15009|https://huggingface.co/datasets/nlpai-lab/databricks-dolly-15k-ko|
|openassistant|9651|https://huggingface.co/datasets/nlpai-lab/openassistant-guanaco-ko|
|oig_chip2|10000|https://huggingface.co/datasets/0-hero/OIG-small-chip2|
|총합|107189||
