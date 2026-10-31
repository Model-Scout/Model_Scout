---
license: cc-by-nc-nd-4.0
task_categories:
- question-answering
- text-generation
language:
- ko
tags:
- education
- deep-learning
- qa-dataset
- ai-tutor
- multimodal
size_categories:
- 1K<n<10K
---

# Construction of LLM-based Level-Aware QA Dataset for AI Tutor Development

This dataset is a resource-based QA dataset of approximately 5,000 items generated using GPT-4o based on deep learning major lecture materials and foundational papers. It is a multi-modal dataset containing not only text but also visual information such as formulas and charts. The questions and answers are systematically organized according to the learner's comprehension level (High/Mid/Low). In particular, high reliability was secured by passing through LLM mutual cross-validation and expert human verification. (The dataset is distributed under the CC BY-NC-ND 4.0 license and can be used by clinicians or researchers for public interest purposes.)

## Dataset Overview
- Total Data Volume: 5,000 QA pairs
- Number of Source Materials: 49

## Dataset Composition
It is constructed by integrally analyzing text and visual information (formulas, charts, images) from deep learning lecture materials and foundational papers. Each data entry is categorized according to the learner's level. The question types are diverse, ranging from conceptual understanding to data analysis, enabling comprehensive learning and evaluation of major-specific knowledge.

## Dataset Fields
- `title`: Document Title
- `section`: Section Title
- `question`: Question
- `level`: Question level (High/Mid/Low)
- `answer`: Answer
- `category`: Question Category (Conceptual, Figure Analysis, Quote_Interpretation)
- `context_page`: Reference Page

## License
This dataset follows the CC BY-NC-ND 4.0 license. This license allows the material to be used in unadapted form for non-commercial purposes, provided that attribution is given. Also, before using the dataset, you must inform the author of the intent and scope of use.

This dataset is provided for the purpose of facilitating the distribution of the original dataset.

This dataset is a research result of 'Glocal University 30' supported by the Ministry of Education and the National Research Foundation of Korea. (GLOCAL-202407990001)

Contact: 010-4194-4693 (dlekgo79@hallym.ac.kr)

---

# AI 튜터 개발을 위한 LLM 기반 학생 수준별 QA 학습 데이터 구축

본 데이터셋은 딥러닝 전공 강의 자료와 기초 논문을 토대로 GPT-4o를 활용해 생성된 약 5,000건의 자료 기반 QA 데이터입니다. 텍스트뿐만 아니라 수식, 도표 등 시각 정보를 포함한 멀티모달 데이터로, 학습자의 이해도(상/중/하)에 맞춰 질문과 답변을 체계적으로 구성하였습니다. 특히 LLM 상호 교차 검증과 전공자 인간 검수를 통과하여 높은 신뢰성을 확보했습니다. (데이터 셋은 CC BY NC ND 4.0 라이선스 하에 배포되며 공익적인 목적을 위해 임상가 혹은 연구자들이 사용 가능합니다)

## 데이터셋 개요
- 총 데이터량: 약 5000개의 QA 쌍
- 자료 수: 49개

## 데이터 구성
딥러닝 강의 자료와 기초 논문의 텍스트 및 시각 정보(수식, 도표, 그림)를 통합적으로 분석하여 구성되었습니다. 각 데이터는 학습자의 수준에 따라 구분되어 있으며 질문 유형도 개념 이해, 자료 분석 등으로 다양하게 구성되어 있어 종합적인 전공 지식 학습과 평가가 가능한 데이터를 포함합니다.

## 컬럼 정보
- `title`: 자료 제목
- `section`: 단락 제목
- `question`: 질문
- `level`: 질문의 난이도 (상/중/하)
- `answer`: 정답
- `category`: 질문 유형 (Conceptual, Figure Analysis, Quote_Interpretation)
- `context_page`: 참고 페이지

## 라이선스
이 데이터셋은 CC BY NC ND 4.0 라이선스를 따릅니다. 이 라이선스는 비영리적인 용도로 출처를 명시하는 경우 자료를 변형하지 않은 형태로 사용할 수 있습니다. 또한 데이터셋을 사용하기 전 사용 의도와 범위를 저작자에게 미리 알려야 합니다.

이 데이터셋은 원본 데이터셋의 배포를 돕기 위한 목적으로 제공됩니다.

본 데이터셋은 본 과제(결과물)는 교육부와 한국연구재단의 재원으로 지원을 받아 수행된 '글로컬대학 30'의 연구결과입니다. (GLOCAL-202407990001)

연락처: 010-4194-4693 (dlekgo79@hallym.ac.kr)
