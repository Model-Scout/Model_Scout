---
language:
- ko
license: cc-by-sa-4.0
pretty_name: "spider-ko: 한국어 Text-to-SQL 데이터셋"
tags:
- korean
- text-to-sql
- table-question-answering
- text2text-generation
task_categories:
- table-question-answering
- text2text-generation
annotations_creators:
- machine-generated
- expert-generated
source_datasets:
- extended-from-spider
size_categories:
- 1K<n<10K
---

# Dataset Card for spider-ko: 한국어 Text-to-SQL 데이터셋

### 데이터셋 요약
Spider-KO는 Yale University의 [Spider](https://yale-lily.github.io/spider) 데이터셋을 한국어로 번역한 **텍스트-SQL** 변환 데이터셋입니다. 원본 Spider 데이터셋의 자연어 질문을 한국어로 번역하여 구성하였습니다. 이 데이터셋은 다양한 도메인의 데이터베이스에 대한 질의와 해당 SQL 쿼리를 포함하고 있으며, 한국어 Text-to-SQL 모델 개발 및 평가에 활용될 수 있습니다.

### 지원 태스크 및 리더보드
-   `text-to-sql`: 한국어 자연어 질문을 SQL 쿼리로 변환하는 태스크에 사용됩니다. 

### 언어
데이터셋의 질문은 한국어(`ko`)로 번역되었으며, SQL 쿼리는 영어 기반으로 유지되었습니다. 원본 영어 질문도 함께 제공됩니다.

## 데이터셋 구조

### 데이터 필드
- `db_id` (string): 해당 질문과 관련된 데이터베이스 식별자
- `query` (string): 질문에 대응하는 SQL 쿼리
- `question` (string): 원본 영어 자연어 질문
- `query_toks` (list): SQL 쿼리를 토큰화한 리스트
- `query_toks_no_value` (list): 값을 제외한 SQL 쿼리 토큰 리스트
- `question_ko` (string): 한국어로 번역된 자연어 질문

### 데이터 분할
데이터셋은 원본 Spider 데이터셋의 분할 방식을 따라 다음과 같이 제공됩니다.
-   `train`: 7,000개
-   `validation` (dev): 1,034개

## 데이터셋 생성

### 큐레이션 근거
한국어 환경에서 자연어 질의를 SQL로 변환하는 모델을 개발하기 위해 구축되었습니다. 영어 중심의 Text-to-SQL 데이터셋 생태계를 한국어로 확장하여 한국어 사용자들을 위한 데이터베이스 질의 시스템 개발을 지원하고자 합니다.

### 번역 및 어노테이션

**번역 과정:** 
번역은 크게 다음과 같은 다단계 파이프라인으로 진행되었습니다.

1. LLM 기반 초기 번역 수행 (Claude 3.5 Sonnet)
2. LLM 활용 자동 검증 및 개선 프로세스 적용 (Gemini 2.0 Flash + Claude 3.5 Sonnet)
3. 인간 전문가에 의한 최종 검수

**주요 오류 유형 및 대응 방안:**
번역 과정에서 발견된 주요 오류 유형을 분석하고 이를 해결하기 위한 검증 프로세스를 구축했습니다.

- **시간/수 비교 표현 오류**: 
  영어와 한국어 간 시간 표현 방식과 수량 비교 표현의 차이로 인한 오류를 검출하고 수정

- **어색한 한국어 단어/문장 사용**: 
  직역으로 인한 부자연스러운 표현을 자연스러운 한국어 표현으로 대체하는 검증 단계 추가

- **서술어 호응 오류**:
  한국어 문장의 주어-서술어 호응 관계를 검증하여 문법적으로 올바른 문장 구성 확보

- **도메인 어휘 번역 오류**:
  데이터베이스 특화 용어(테이블명, 필드명 등)의 문맥에 맞는 번역을 위해 LLM에게 SQL 쿼리와 함께 참조하도록 지시

- **의미 누락 및 변형**:
  원문의 의미가 번역 과정에서 손실되거나 변형되지 않도록 의미 보존 검증 단계 추가

**LLM 활용 검증 프로세스:**
1. 각 번역 결과에 대해 주요 오류 유형별 체크리스트를 기반으로 한 자동 검증
2. 도메인 특화 용어의 일관된 번역을 위한 용어 데이터베이스 구축 및 참조
3. 문맥을 고려한 번역 적절성 평가 (SQL 쿼리와의 일관성 검증)
4. 자연스러운 한국어 표현으로의 변환 검증

**최종 검수 과정:**
- 데이터베이스 지식을 갖춘 한국어 전문가에 의한 최종 검수
- 주요 오류 유형별 검증을 통한 번역 품질 향상

이러한 다단계 검증 프로세스를 통해 한국어 Text-to-SQL 데이터의 품질을 효과적으로 개선하였습니다.

## 데이터 사용 시 고려사항

### 알려진 한계
-   **영어 테이블/컬럼명**: SQL 쿼리에서는 원본 영어 테이블명과 컬럼명을 사용하므로, 한국어 질문과 영어 SQL 간의 언어적 불일치가 존재합니다.
-   **문화적 맥락 차이**: 특정 고유명사나 문화적 참조가 한국어 맥락에서는 생소할 수 있습니다.
-   **한국어 특수성**: 한국어의 조사, 어순 등의 특성이 SQL 변환 과정에서 추가적인 복잡성을 야기할 수 있습니다.
-   **테이블 내 영문 데이터**: 실제 데이터베이스 값이 영어로 되어 있어, 한국어 질문에서 이를 참조할 때 불일치가 발생할 수 있습니다.

## 추가 정보

### 데이터셋 큐레이터
[@sim-so](https://huggingface.co/sim-so), [@choincnp](https://huggingface.co/choincnp), [@nuatmochoi](https://huggingface.co/nuatmochoi)

### 라이선스 정보
이 데이터셋은 원본 Spider 데이터셋과 동일하게 **CC BY-SA 4.0 (Creative Commons Attribution-ShareAlike 4.0 International)** 라이선스를 따릅니다.

### 인용 정보

이 데이터셋을 연구 등에 활용하실 경우, 다음 형식으로 인용해주시기 바랍니다.
```
@misc{spider_ko_2025,
  title={spider-ko},
  author={Sohyun Sim, Youngjun Cho, Seongwoo Choi},
  year={2025},
  publisher={Hugging Face KREW},
  howpublished={\url{https://huggingface.co/datasets/huggingface-KREW/spider-ko}}
}
```
또한, 원본 Spider 데이터셋도 함께 인용해 주세요.
```
@inproceedings{yu-etal-2018-spider,
    title = "{S}pider: A Large-Scale Human-Labeled Dataset for Complex and Cross-Domain Semantic Parsing and Text-to-{SQL} Task",
    author = "Yu, Tao  and
      Zhang, Rui  and
      Yang, Kai  and
      Yasunaga, Michihiro  and
      Wang, Dongxu  and
      Li, Zifan  and
      Ma, James  and
      Li, Irene  and
      Yao, Qingning  and
      Roman, Shanelle  and
      Zhang, Zilin  and
      Radev, Dragomir",
    editor = "Riloff, Ellen  and
      Chiang, David  and
      Hockenmaier, Julia  and
      Tsujii, Jun{'}ichi",
    booktitle = "Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing",
    month = oct # "-" # nov,
    year = "2018",
    address = "Brussels, Belgium",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D18-1425",
    doi = "10.18653/v1/D18-1425",
    pages = "3911--3921",
    archivePrefix={arXiv},
    eprint={1809.08887},
    primaryClass={cs.CL},
}
```

### 기여
번역 데이터셋 구축에 참여한 모든 팀원들과 가짜연구소, Hugging Face KREW에게 감사드립니다.