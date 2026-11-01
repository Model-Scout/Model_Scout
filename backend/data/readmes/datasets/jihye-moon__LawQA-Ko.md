---
task_categories:
- text-generation
- question-answering
language:
- ko
tags:
- legal
size_categories:
- 10K<n<100K
---

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->

법률에 대한 질문과 답변으로 구성된 데이터셋 입니다. 

아래의 데이터셋에서 질문과 답변을 병합하여 Datasets를 만들었습니다. 


| 정보 출처 | Dataset Page | Rows |
|---|---|---|
|[찾기쉬운생활법령정보 백문백답](https://www.easylaw.go.kr/CSP/OnhunqueansLstRetrieve.laf?search_put=)| [jiwoochris/easylaw_kr](https://huggingface.co/datasets/jiwoochris/easylaw_kr) | 2,195 rows |
|[대한법률구조공단 법률상담사례](https://www.klac.or.kr/legalinfo/counsel.do)| [jihye-moon/klac_legal_aid_counseling](https://huggingface.co/datasets/jihye-moon/klac_legal_aid_counseling) | 10,037 rows |
|[대한법률구조공단 사이버상담](https://www.klac.or.kr/legalstruct/cyberConsultation.do)| [jihye-moon/klac_cyber_counseling](https://huggingface.co/datasets/jihye-moon/klac_cyber_counseling) | 2,587 rows |

※ 위의 데이터는 모두 웹 페이지를 크롤링 하여 구축된 데이터 입니다. 

※ 대한법률구조공단 데이터는 크롤링 후, 전처리(공단 안내문구 삭제, 쿠션어 삭제 등)를 하였습니다. 