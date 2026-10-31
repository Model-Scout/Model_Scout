---
task_categories:
- translation
language:
- en
- ko
---

## Preprocessing En-Ko subset of [Parallel Sentences Datasets](https://huggingface.co/collections/sentence-transformers/parallel-sentences-datasets-6644d644123d31ba5b1c8785)

* 해외에서 제작된 많은 대규모 번역 쌍 데이터들이 영어 텍스트와 한국어 텍스트를 문장 단위로 분리한 후 기계적으로 매핑시키고 있습니다.
* 이로 인해 전혀 엉뚱한 문장이 번역 쌍으로 매칭되어 있는 문제가 발생합니다.
* 임베딩 유사도 기반 전처리를 통해 이 문제를 해결할 수 있을 것 같아서 이 데이터 셋을 제작했습니다.
* 일부 데이터는 상업적 사용이 어려운 라이선스가 적용된 경우가 있습니다.

### 데이터 목록
* [parallel-sentences-global-voices](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-global-voices)
* [parallel-sentences-muse](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-muse)
* [parallel-sentences-jw300](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-jw300)
* [parallel-sentences-tatoeba](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-tatoeba)
* [parallel-sentences-wikititles](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-wikititles)

### 유사도 측정
* [BAAI/BGE-m3](https://huggingface.co/BAAI/bge-m3)로 임베딩
* 영어 문장과 한국어 문장의 유사도 계산

### 활용 예시
* 유사도가 0.65~0.7 이상인 데이터만 활용하는 것이 좋습니다.
* 일부 사례에서는 추가적인 전처리를 통해 정확한 번역 쌍을 되찾거나, 문서 단위로 번역 데이터를 구축하는 것이 가능할 것 같습니다(Global-Voice처럼).

### 데이터 상세 및 전처리 내역
* **parallel-sentences-europarl**
  * 수집하지 않음(한국어 데이터 없음)
* **parallel-sentences-global-voices**
  * 특징
    * Global voice에서 수집된 글로벌 뉴스 기사(문장 단위 매칭) 데이터
    * 문장 단위 매칭이 적절하지 않은 경우가 있음(밀려서 매칭되는 현상)
    * 기사 내용이 완전히 일치하지 않는 경우 소수 존재
    * 상세: J. Tiedemann, 2012, Parallel Data, Tools and Interfaces in OPUS. In Proceedings of the 8th International Conference on Language Resources and Evaluation (LREC 2012)
  * 전처리
    * 기사 단위로 병합
    * 영어 데이터에만 있는 "· Global Voice" 제거
* **parallel-sentences-muse**
  * 특징
    * 단어 번역 데이터
  * 전처리
    * 유사도 측정이 무의미하므로, 전부 1.0 입력
* **parallel-sentences-jw300**
  * 특징
    * 문장 단위 매칭 데이터
    * 문장 단위 매칭이 적절하지 않은 경우가 있음(밀려서 매칭되는 현상)
    * 한국어 띄어쓰기 이상함
    * 기사 단위 분리 어려움
  * 전처리
    * "\\u200b" 제거
    * [quickspacer](https://github.com/cosmoquester/quickspacer)를 이용해 띄어쓰기 교정
* **parallel-sentences-news-commentary**
  * 수집하지 않음(한국어 데이터 없음)
* **parallel-sentences-opensubtitles**
  * 수집하지 않음(번역 쌍 매칭이 안됨)
* **parallel-sentences-talks**
  * 제공하지 않음
    * [TED Talks Usage Policy](https://www.ted.com/about/our-organization/our-policies-terms/ted-talks-usage-policy)에 따라, similarity를 추가하거나, 큐레이션하는 것은 원본 데이터를 변형시키는 행위라고 생각되어 공유하지 않습니다. 
    * 혹시 제가 라이선스와 관련해서 잘못 알고 있다면 알려주세요.
  * 특징
    * TED 강연에 대한 영어 자막 + 한국어 자막
    * 상당히 좋은 전문 분야+구어체 데이터 셋입니다. 번역 쌍 매칭 정확도도 평균적으로 높긴 한데, 그래도 임베딩 유사도 기반 전처리를 하고 사용하시는 것을 추천드립니다.
    * [sentence-transformers/parallel-sentences-talks](https://huggingface.co/datasets/sentence-transformers/parallel-sentences-talks)
* **parallel-sentences-tatoeba**
  * 특징
    * 주로 구어체로 이루어진, 사람이 번역한 문장 번역 쌍
    * 동일한 문장에 대한 2가지 이상의 번역이 존재하는 경우도 있음(모두 옳은 번역)
  * 별도의 전처리 하지 않음
* **parallel-sentences-wikimatrix**
  * 수집하지 않음(저퀄리티)
* **parallel-sentences-wikititles**
  * 특징
    * 단어 번역 데이터(위키피디아 제목)
  * 전처리
    * "(동음이의)", "(disambiguation)" 제거
    * 유사도 측정이 무의미하므로, 전부 1.0 입력
* **parallel-sentences-ccmatrix**
  * 수집하지 않음(대용량)
  * 평균 퀄리티는 낮지만, 데이터의 양(19.4M 번역 쌍)이 많아 좋은 번역 쌍도 많이 존재합니다. 추후 전처리 시도해보겠습니다.