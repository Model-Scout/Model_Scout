---
license: apache-2.0
dataset_info:
  features:
  - name: conversations
    list:
    - name: from
      dtype: string
    - name: value
      dtype: string
  - name: src
    dtype: string
  splits:
  - name: train
    num_bytes: 1087781139
    num_examples: 1122566
  download_size: 567833382
  dataset_size: 1087781139
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- text-generation
language:
- ko
---

# kollm Converations Dataset

This dataset is an integrated dataset created in conversations format for SFT learning using the Korean dataset currently available on huggingface and github.



Our the nox model was trained on the kollm dataset. For datasets that are private due to license restrictions, please download them directly from the URL below.



## Included datasets

| Source                        | 설명                                                         | 원본 URL                                                     |
| ----------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| KoAlpaca-v1.1                 | 네이버 지식인 질답을 ChatGPT를 이용해 재생성한 Alpaca 형식 데이터셋 | https://github.com/Beomi/KoAlpaca/blob/main/KoAlpaca_v1.1.jsonl |
| kollm_kmmlu                   | 한국어 벤치마크 KMMLU                                        | https://huggingface.co/datasets/HAERAE-HUB/KMMLU             |
| Ko-CommonGen                  | 개념 집합을 바탕으로 짧은 문장을 재구성하는 자연어 생성 데이터셋 | https://github.com/J-Seo/Korean-CommonGen/tree/main/dataset  |
| kobest_hellaswag              | 한국어 벤치마크 KoBEST                                       | https://huggingface.co/datasets/skt/kobest_v1                |
| namuwiki-alpaca-dataset       | 나무위키 덤프 파일의 Alpaca 형식 변환 데이터셋               | https://huggingface.co/datasets/psymon/namuwiki_alpaca_dataset |
| ko-alpaca-data                | 한글로 번역한 Alpaca 데이터셋 질문에 대한 ChatGPT 답변 생성 데이터셋 | https://huggingface.co/datasets/Bingsu/ko_alpaca_data        |
| OIG-small-chip2-ko            | LAION AI의 OIG-small-chip2 싱글턴 대화 한글 번역 데이터셋    | https://huggingface.co/datasets/heegyu/OIG-small-chip2-ko    |
| humane-right-corpus-v1        | 국가인권위원회 상담 문서 기반 ChatGPT 질답 생성 데이터셋     | https://github.com/human-rights-corpus/HRC                   |
| kobest_wic                    | 한국어 벤치마크 KoBEST                                       | https://huggingface.co/datasets/skt/kobest_v1                |
| koopus100                     | OPUS-100 데이터셋의 영어-한국어 subset                       | https://huggingface.co/datasets/Helsinki-NLP/opus-100/tree/main/en-ko |
| sentence-type                 | 문장 유형 분류 데이터셋                                      | https://dacon.io/competitions/official/236037/data           |
| koiwslt2017                   | IWSLT 2017 데이터셋의 영어-한국어 subset                     | https://huggingface.co/datasets/iwslt2017/viewer/iwslt2017-ko-en |
| korean-parallel-corpora       | 한영 번역 병렬 데이터셋                                      | https://huggingface.co/datasets/Moo/korean-parallel-corpora  |
| squad-kor-v1                  | 한국어 MRC 데이터셋 KorQuAD v1.0                             | https://huggingface.co/datasets/squad_kor_v1                 |
| kobest_boolq                  | 한국어 벤치마크 KoBEST                                       | https://huggingface.co/datasets/skt/kobest_v1                |
| kobest_sentineg               | 한국어 벤치마크 KoBEST                                       | https://huggingface.co/datasets/skt/kobest_v1                |
| kobest_copa                   | 한국어 벤치마크 KoBEST                                       | https://huggingface.co/datasets/skt/kobest_v1                |
| kollm_paws-x                  | PAWS-X 데이터셋의 영어-한국어 subset                         | https://huggingface.co/datasets/paws-x/viewer/ko             |
| total_kor_counsel_bot         | 한국어 심리 상담 싱글턴 대화 데이터셋                        | https://github.com/MrBananaHuman/CounselGPT/blob/main/total_kor_counsel_bot.jsonl |
| para_pat                      | ParaPat 데이터셋의 영어-한국어 subset                        | https://huggingface.co/datasets/para_pat/viewer/en-ko        |
| tydiqa-goldp                  | TyDi QA 데이터셋의 Gold Passage Task에 대한 한국어 subset    | https://huggingface.co/datasets/khalidalt/tydiqa-goldp/viewer/korean |
| tydiqa-xtreme                 | XTREME 벤치마크의 TyDiQA Task에 대한 한국어 subset           | https://huggingface.co/datasets/juletxara/tydiqa_xtreme/viewer/ko |
| korquad-chat-v1               | 한국어 MRC 데이터셋 KorQuAD v1.0의 답변을 ChatGPT를 이용해 재생성한 멀티턴 대화 데이터셋 | https://huggingface.co/datasets/heegyu/korquad-chat-v1       |
| answerable-tydiqa             | TyDi QA 데이터셋의 Gold Passage Task를 확장하여, 답변 불가능한 질문도 포함한 데이터셋 | https://huggingface.co/datasets/copenlu/answerable_tydiqa    |
| klue-mrc                      | 한국어 벤치마크 KLUE MRC 데이터셋                            | https://github.com/KLUE-benchmark/KLUE/tree/main/klue_benchmark/klue-mrc-v1.1 |
| klue-mrc-qa                   | 한국어 벤치마크 KLUE MRC 데이터셋의 답변을 ChatGPT를 이용해 재생성한 데이터셋 | https://github.com/KLUE-benchmark/KLUE/tree/main/klue_benchmark/klue-mrc-v1.1 |
| openassistant-guanaco-ko      | 다국어로 이루어진 Guanaco 데이터셋 전체를 한글로 번역한 데이터셋 | https://huggingface.co/datasets/nlpai-lab/openassistant-guanaco-ko?row=0 |
| KOpen-platypus                | 한글로 번역한 Open-Platypus 데이터셋                         | https://huggingface.co/datasets/kyujinpy/KOpen-platypus      |
| OpenOrca-ko-v3                | 한글로 번역한 OpenOrca 데이터셋                              | https://huggingface.co/datasets/kyujinpy/OpenOrca-ko-v3      |
| kowizard                      | Alpaca 형식 질답 데이터셋                                    |                                                              |
| KOR-OpenOrca-Platypus-v2      | 한글로 번역한 OpenOrca 데이터셋                              | https://huggingface.co/datasets/kyujinpy/KOR-OpenOrca-Platypus-v2 |
| kollm_belebele                | 다국어 MRC 벤치마크 Belebele의 한국어 subset                 | https://huggingface.co/datasets/facebook/belebele/blob/main/data/kor_Hang.jsonl |
| EverythingLM-data-V2-Ko       | 한글로 번역한 EverythingLM V2 데이터셋                       | https://huggingface.co/datasets/ziozzang/EverythingLM-data-V2-Ko |
| ko-Ultrafeedback-binarized    | 한글로 번역한 Ultrafeedback_binarized 데이터셋               | https://huggingface.co/datasets/maywell/ko_Ultrafeedback_binarized |
| KoInstruct-QA                 | Alpaca 형식 질답 데이터셋                                    | https://huggingface.co/datasets/HAERAE-HUB/KoInstruct-QA     |
| sharegpt-deepl-ko-translation | shareGPT 데이터셋을 질답 형식에서 한영 번역 형식으로 변환한 데이터셋 | https://huggingface.co/datasets/squarelike/sharegpt_deepl_ko_translation |
| ko-lima-vicuna                | LIMA 데이터셋을 ChatGPT를 이용해 한글로 재생성한 shareGPT 형식 데이터셋 | https://huggingface.co/datasets/changpt/ko-lima-vicuna       |
| KoInstruct-Base               | Alpaca 형식 질답 데이터셋                                    | https://huggingface.co/datasets/HAERAE-HUB/KoInstruct-Base   |
| kollm_csatqa                  | 한국어 대학수학능력시험 질답 데이터셋                        | https://huggingface.co/datasets/HAERAE-HUB/csatqa            |
| ShareGPT-74k-ko               | 한글로 번역한 shareGPT 데이터셋                              | https://huggingface.co/datasets/dbdu/ShareGPT-74k-ko         |
| sharegpt-deepl-ko             | 한글로 번역한 shareGPT 데이터셋                              | https://huggingface.co/datasets/junelee/sharegpt_deepl_ko    |


## Not included datasets

### ETRI 데이터셋

| Source          | 설명                                   | 원본 URL                              |
| --------------- | -------------------------------------- | ------------------------------------- |
| etri-short-qa   | 위키피디아 단문질문 QA Datasets        | https://aiopen.etri.re.kr/corpusModel |
| etri-mrc        | MRC 한국어 QA Dataset                  | https://aiopen.etri.re.kr/corpusModel |
| etri-explain-qa | 엑소브레인 근거 설명 QA Dataset        | https://aiopen.etri.re.kr/corpusModel |
| etri-law-qa     | 엑소브레인 법령QA Dataset (국회도서관) | https://aiopen.etri.re.kr/corpusModel |
| etri-squad      | SQuAD 한국어 QA Dataset                | https://aiopen.etri.re.kr/corpusModel |

### AIHub 데이터셋


| Source                                     | 설명                                                 | 원본 URL                                                     |
| ------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------------------ |
| aihub-knowledge-chat                       | 전문지식 답변을 포함하는 멀티턴 대화 데이터셋        | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71304 |
| aihub-expertise                            | 의료, 금융, 스포츠 등 전문분야 한영 번역 데이터셋    | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=111 |
| aihub-socialsci                            | 법률, 교육, 경제 등 사회과학 분야 한영 번역 데이터셋 | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=125 |
| aihub-MT-new-corpus                        | 기계 번역 앱 구축용 한영 번역 데이터셋               | https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71593 |
| aihub-techsci                              | ICT, 전기/전자 등 기술과학 분야 한영 번역 데이터셋   | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=124 |
| aihub-food                                 | 식품 분야 영한 번역 데이터셋                         | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71262 |
| aihub-techsci2                             | ICT, 전기/전자 등 기술과학 분야 한영 번역 데이터셋   | https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71266 |
| aihub-speechtype-based-machine-translation | 발화 유형별 영한 번역 데이터셋                       | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71411 |
| aihub-parallel-translation                 | 발화 유형 및 분야별 한영 번역 데이터셋               | https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=126 |
| aihub-ko-wiki-squad                        | 한국어 위키백과 MRC 데이터셋                         | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=106 |
| aihub-basicsci                             | 수학, 물리학 등 기초과학 분야 한영 번역 데이터셋     | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71496 |
| aihub-MTPE                                 | 기계번역 품질 사후검증 데이터셋                      | https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71475 |
| aihub-broadcast-content                    | 방송 콘텐츠 분야 한영 번역 데이터셋                  | https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71382 |
| aihub-colloquial                           | 신조어, 약어 등을 포함하는 구어체 한영 번역 데이터셋 | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71265 |
| aihub-humanities                           | 인문학 분야 한영 번역 데이터셋                       | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71498 |
| aihub-news-mrc                             | 뉴스 본문 기반 MRC 데이터셋                          | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=89 |
| aihub-ko-multi-session-chat                | 한국어 멀티세션 대화 데이터셋                        | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71630 |
| aihub-patent                               | 특허명세서 영한 번역 데이터셋                        | https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=563 |



Please refer to the url below for information on aihub licensing.

https://aihub.or.kr/partcptnmlrd/inqry/view.do?currMenu=144&topMenu=104