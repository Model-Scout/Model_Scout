---
dataset_info:
  features:
  - name: query_id
    dtype: int64
  - name: source_type
    dtype: string
  - name: query_type
    dtype: string
  - name: query_format
    dtype: string
  - name: query
    dtype: string
  - name: doc_id
    dtype: string
  - name: image_id
    dtype: int64
  - name: image
    dtype: image
  - name: markdown
    dtype: string
  - name: elements
    dtype: string
  - name: page_number_in_doc
    dtype: int64
  splits:
  - name: train
    num_bytes: 270527680486.72
    num_examples: 310226
  download_size: 251526672926
  dataset_size: 270527680486.72
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
task_categories:
- document-question-answering
- visual-document-retrieval
language:
- ko
tags:
- Visual Retrieving
- Industrial RAG
- datadesigner
size_categories:
- 100K<n<1M
license: cc-by-4.0
---

<h1 align="center"> 🔎 Ko-VDR Train Public v2 </h1>

<p align="center">
  <img width="800" alt="Korean VDR Train" src="https://cdn-uploads.huggingface.co/production/uploads/655eeb5532537bcc8d7460ab/Em_W5suEXUrDiSHNoDREs.png" />
</p>

> [!NOTE]
> **Changes from v1**
> - Collected more diverse documents to increase the number of queries.
> - Partially revised prompts to improve generation quality.
> - Applied relevance mapping in both the generation and filtering stages, retaining only queries where relevance mapping was consistently performed in both stages.
> - Applied rule-based filtering to remove low-quality queries.

> [!NOTE]
> For a high-level overview of how the dataset was generated, see [PIPELINE.md](https://huggingface.co/datasets/NomaDamas/ko-vdr-train-public-v2.0/blob/main/PIPELINE.md).

This dataset is a training dataset for Korean Visual Document Retrieval. It includes 310,226 query-page pairs (146,752 unique queries) generated from 49 Korean government and public institution PDF documents using LLM-based (Solar Pro 3) synthetic query generation. Queries are generated from two sources: page-level summaries (87%) and direct page context (13%), covering 7 query types (compare-contrast, open-ended, enumerative, multi-hop, extractive, numerical, boolean) in instruction, question, and keyword formats.

## Links

* **Github:** [https://github.com/whybe-choi/kovidore-data-generator](https://github.com/whybe-choi/kovidore-data-generator)

### Dataset Summary

- Description: Training data for Korean Visual Document Retrieval, generated from Korean government and public institution reports
- Language: ko
- Document Types: Government reports, guidelines, manuals, survey reports

### Dataset Statistics

- Total Documents : 49
- Total Pages : 7,548
- Total Queries : 146,752
- Average number of pages per query : 2.0

### Number of Relevant Pages per Query

| # Relevant Pages | # Queries |
|:-:|:-:|
| 1 | 44,244 |
| 2 | 69,339 |
| 3 | 24,138 |
| 4 | 6,319 |
| 5 | 1,814 |
| 6 | 552 |
| 7 | 204 |
| 8 | 101 |
| 9 | 41 |

### Queries per Document

| Doc ID | Context | Summary | Count |
|--------|---------|---------|-------|
| 기후에너지환경부_에너지총조사_20241130 | 2,987 | 2,630 | 5,617 |
| 25년_주요업무계획(게시용) | 2,603 | 2,665 | 5,268 |
| 2025년_지방공무원_인사실무 | 2,048 | 2,720 | 4,768 |
| (최종보고서)_국제_OTT_산업_실태조사_및_국내_OTT_글로벌_진출_방안_연구 | 1,694 | 2,706 | 4,400 |
| 2023-2024_항만업무편람 | 631 | 3,177 | 3,808 |
| 내지-KOSI_중소기업동향_2026년_2월호 | 96 | 3,382 | 3,478 |
| 해양수산부_무인도서_100선_20221231 | 183 | 3,273 | 3,456 |
| 국토교통부_해외건설_세무업무_매뉴얼_20220404 | 750 | 2,657 | 3,407 |
| 2019년_제6차_작업환경실태조사_최종보고서(지사_제외) | 374 | 2,896 | 3,270 |
| 2024_회계연도_기업체노동비용조사_보고서 | 506 | 2,727 | 3,233 |
| 국토교통부_해외건설_법률컨설팅_사례_20240628 | 486 | 2,729 | 3,215 |
| 2022년도국가연구개발사업상위평가보고서(중간평가)_최종 | 503 | 2,691 | 3,194 |
| 경상북도_(PDF)인삼재배전서_20210825 | 147 | 3,025 | 3,172 |
| 2025_산업보고서(방위산업)_라틴아메리카_협력센터 | 41 | 3,119 | 3,160 |
| 1.조사요약(2024부산방문관광객실태조사) | 222 | 2,912 | 3,134 |
| 국토안전관리원_스마트_안전유지관리_시설물_확대방안_마련_용역_보고서_2024 | 680 | 2,414 | 3,094 |
| 2026년_공무원_인재개발_종합계획 | 285 | 2,774 | 3,059 |
| 생체정보_보호_안내서(2024.12) | 285 | 2,740 | 3,025 |
| 2025년_교육운영계획 | 103 | 2,919 | 3,022 |
| 그랜드코리아레저(주)_카지노_비즈니스와_제도_20140219 | 64 | 2,923 | 2,987 |
| 제3차_해양수산발전기본계획(2021-2030) | 701 | 2,272 | 2,973 |
| 2025_산업보고서(제약바이오)_라틴아메리카_협력센터 | 44 | 2,893 | 2,937 |
| 한국인터넷진흥원_개인정보_유출_신고_동향_및_예방_방법_20241231 | 132 | 2,754 | 2,886 |
| (최종)UN개황(2019)-내지-최종(웹용) | 650 | 2,220 | 2,870 |
| 한국원자력환경공단_처분시설_부지주변_방사선환경조사_보고서_20250831 | 255 | 2,585 | 2,840 |
| (최종보고서)_디지털미디어_허브_조성을_위한_빛마루_중장기_전략_연구 | 170 | 2,599 | 2,769 |
| 합성데이터_생성활용_안내서(2024.12) | 388 | 2,372 | 2,760 |
| 개인정보_유출_등_사고_대응_매뉴얼(2024.3) | 177 | 2,572 | 2,749 |
| 2024년도하반기국가연구개발사업특정평가보고서(다부처공동추진사업군) | 393 | 2,351 | 2,744 |
| 제1차_대한민국_공공외교_기본계획(2017-2021)_(최종본) | 50 | 2,673 | 2,723 |
| 한국노인인력개발원_노인_일자리_및_사회활동_지원사업_시행_20년의_성과 | 30 | 2,682 | 2,712 |
| 수도권매립지관리공사_관리형매립지_조사결과보고서_20230102 | 245 | 2,467 | 2,712 |
| 과학기술정보통신부_국립전파연구원_ICT_융복합_시설의_안전한_전자파_환경_기반_조성_연구_20241231 | 221 | 2,461 | 2,682 |
| (최종보고서)_국내외_온라인_동영상_미디어콘텐츠_시장_전망_및_정책_추진방향_연구 | 113 | 2,503 | 2,616 |
| 제3차_환경관리해역_기본계획 | 419 | 2,191 | 2,610 |
| 데이터에_담긴_서울교통_2023 | 47 | 2,562 | 2,609 |
| 지점별_인입가능량_최종_분석_결과 | 8 | 2,591 | 2,599 |
| 한국수력원자력(주)_i_SMR_및_SSNC_설명자료_20250829 | 111 | 2,413 | 2,524 |
| 한국언론진흥재단_미디어이슈_광고요금제_도입을_앞둔_넷플릭스에_대한_인식_및_이용_조사_20220928 | 15 | 2,502 | 2,517 |
| (최종보고서)_디지털미디어_신산업_진흥_방안_및_인력수급_기초조사에_관한_연구 | 134 | 2,364 | 2,498 |
| 행정안전부_모바일_전자정부서비스_앱_소스코드_검증_가이드라인_20211029 | 169 | 2,278 | 2,447 |
| 제2차_환경관리해역_기본계획 | 79 | 2,367 | 2,446 |
| 한국언론진흥재단_미디어이슈_이대남_현상에_대한_인식_20220323 | 14 | 2,423 | 2,437 |
| 한국언론진흥재단_미디어이슈_코로나19_관련_정보_이용_및_인식_현황_20200326 | 19 | 2,360 | 2,379 |
| 한국무역보험공사_해외시장_신용위험_보고서_20240510 | 17 | 2,361 | 2,378 |
| 과학기술정보통신부_국립전파연구원_전자파_흡수전력밀도_등_전자파_인체노출량_평가기술_연구_20241231 | 251 | 2,066 | 2,317 |
| 2025년_4분기_위성정보_서비스_현황 | 19 | 2,218 | 2,237 |
| 농지개량행위신고업무지침 | 24 | 2,175 | 2,199 |
| 그랜드코리아레저(주)_블랙잭_게임의_이해_20250617 | 38 | 1,777 | 1,815 |
| **Total** | **19,621** | **127,131** | **146,752** |

### Query Type

| Query Type | Count |
|------------|-------|
| Compare-Contrast | 22,211 |
| Numerical | 21,774 |
| Extractive | 21,243 |
| Multi-Hop | 20,726 |
| Enumerative | 20,382 |
| Open-Ended | 20,317 |
| Boolean | 20,099 |

### Query Format

| Query Format | Count |
|--------------|-------|
| Instruction | 62,264 |
| Question | 60,145 |
| Keyword | 24,343 |
| **Total** | **146,752** |

## Dataset Structure

Each row represents a query-page pair with the following fields:

```json
{
  "query_id": <int>,
  "source_type": <str>,
  "query_type": <str>,
  "query_format": <str>,
  "query": <str>,
  "doc_id": <str>,
  "image_id": <int>,
  "image": <PIL.Image>,
  "markdown": <str>,
  "elements": <str>,
  "page_number_in_doc": <int>
}
```

- **query_id** \<int\> : A unique numerical identifier for the query.
- **source_type** \<str\> : `"summary"` or `"context"`, metadata about the type of information used by the annotation pipeline to create the query.
- **query_type** \<str\> : The type of query (e.g., `"compare-contrast"`, `"open-ended"`, `"enumerative"`, `"multi-hop"`, `"extractive"`, `"numerical"`, `"boolean"`).
- **query_format** \<str\> : The syntactic format of the query (`"instruction"`, `"question"`, or `"keyword"`).
- **query** \<str\> : The actual text of the search question or instruction used for retrieval.
- **doc_id** \<str\> : Name of the source document.
- **image_id** \<int\> : A unique numerical identifier for the matched page.
- **image** \<PIL.Image\> : The matched page image.
- **markdown** \<str\> : Extracted text from the page using an OCR pipeline.
- **elements** \<str\> : JSON-serialized list of extracted layout elements with bounding boxes and text from the page using an OCR pipeline.
- **page_number_in_doc** \<int\> : Original page number inside the document.

## License Information

All annotations, query-document relevance judgments (qrels), and related metadata generated for this corpus are distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

The licensing status of the original source documents (the corpus) and any parsed text (`markdown` column in the corpus) are inherited from their respective publishers. For detailed metadata of each source document (title, doc_id, page count, URL, and license), refer to [`document_metadata.csv`](./document_metadata.csv).

For documents subject to the [Korea Open Government License (KOGL)](https://www.kogl.or.kr/info/license.do) Type 1, the sources are attributed as follows:

| Title | Doc ID | Type | Attribution Text |
| :--- | :--- | :--- | :--- |
| 개인정보 유출 등 사고 대응 매뉴얼 | 개인정보_유출_등_사고_대응_매뉴얼(2024.3) | Type 1 | 본 저작물은 개인정보보호위원회에서 2024년 작성하여 공공누리 제 1유형으로 개방한 '개인정보 유출 등 사고 대응 매뉴얼'을 이용하였으며, 해당 저작물은 [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10123)에서 무료로 다운받으실 수 있습니다. |
| 생체정보 보호 안내서 | 생체정보_보호_안내서(2024.12) | Type 1 | 본 저작물은 개인정보보호위원회에서 2024년 작성하여 공공누리 제 1유형으로 개방한 '생체정보 보호 안내서'를 이용하였으며, 해당 저작물은 [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10900)에서 무료로 다운받으실 수 있습니다. |
| 합성데이터 생성활용 안내서 | 합성데이터_생성활용_안내서(2024.12) | Type 1 | 본 저작물은 개인정보보호위원회에서 2025년 작성하여 공공누리 제 1유형으로 개방한 '합성데이터 생성·활용 안내서'를 이용하였으며, 해당 저작물은 [개인정보보호위원회 발간자료](https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10915)에서 무료로 다운받으실 수 있습니다. |
| 해양수산부 무인도서 100선 | 해양수산부_무인도서_100선_20221231 | Type 1 | 본 저작물은 해양수산부에서 2021년 작성하여 공공누리 제 1유형으로 개방한 '무인도서 백서'를 이용하였으며, 해당 저작물은 [해양수산부 무인도서종합정보시스템](http://uii.mof.go.kr)"에서 무료로 다운받으실 수 있습니다. |
| 위성정보 서비스 현황 | 2025년_4분기_위성정보_서비스_현황 | Type 1 | 본 저작물은 과학기술정보통신부 중앙전파관리소에서 2026년 작성하여 공공누리 제 1유형으로 개방한 '2025년 4분기 위성전파 감시동향'을 이용하였으며, 해당 저작물은 [중앙전파관리소 위성전파김시센터 위성전파감시정보](https://www.srmc.go.kr/obser/obserInfoBBSList.do)'에서 무료로 다운받으실 수 있습니다. |
| 한국원자력환경공단 처분시설 부지주변 방사선환경조사 보고서 | 한국원자력환경공단_처분시설_부지주변_방사선환경조사_보고서_20250831 | Type 1 | 본 저작물은 한국원자력환경공단에서 2025년 작성하여 공공누리 제 1유형으로 개방한 '방사성폐기물 처분시설 부지주변 방사선환경보고서'를 이용하였으며, 해당 저작물은 [공공데이터포털](https://www.data.go.kr/data/15156699/fileData.do)에서 무료로 다운받으실 수 있습니다. |
| 한국언론진흥재단 미디어이슈 이대남 현상에 대한 인식 | 한국언론진흥재단_미디어이슈_이대남_현상에_대한_인식_20220323 | Type 1 | 본 저작물은 한국언론진흥재단에서 2022년 작성하여 공공누리 제 1유형으로 개방한 '이대남 현상에 대한 인식'을 이용하였으며, 해당 저작물은 [공공데이터포털](https://www.data.go.kr/data/15112343/fileData.do)에서 무료로 다운받으실 수 있습니다. |
| 한국언론진흥재단 미디어이슈 코로나19 관련 정보 이용 및 인식 현황 | 한국언론진흥재단_미디어이슈_코로나19_관련_정보_이용_및_인식_현황_20200326 | Type 1 | 본 저작물은 한국언론진흥재단에서 2020년 작성하여 공공누리 제 1유형으로 개방한 '코로나19(COVID-19) 관련 정보 이용 및 인식 현황'을 이용하였으며, 해당 저작물은 [공공데이터포털](https://www.data.go.kr/data/15086396/fileData.do)에서 무료로 다운받으실 수 있습니다. |
| 한국언론진흥재단 미디어이슈 광고요금제 도입을 앞둔 넷플릭스에 대한 인식 및 이용 조사 | 한국언론진흥재단_미디어이슈_광고요금제_도입을_앞둔_넷플릭스에_대한_인식_및_이용_조사_20220928 | Type 1 | 본 저작물은 한국언론진흥재단에서 2022년 작성하여 공공누리 제 1유형으로 개방한 '광고요금제 도입을 앞둔 넷플릭스에 대한 인식 및 이용 조사'를 이용하였으며, 해당 저작물은 [공공데이터포털](https://www.data.go.kr/data/15112345/fileData.do)에서 무료로 다운받으실 수 있습니다. |
| 과학기술정보통신부 국립전파연구원 전자파 흡수전력밀도 등 전자파 인체노출량 평가기술 연구 | 과학기술정보통신부_국립전파연구원_전자파_흡수전력밀도_등_전자파_인체노출량_평가기술_연구_20241231 | Type 1 | 본 저작물은 과학기술정보통신부 국립전파연구원에서 2024년 작성하여 공공누리 제 1유형으로 개방한 '전자파 흡수전력 밀도 등 전자파 인체노출량 평가기술 연구'를 이용하였으며, 해당 저작물은 [공공데이터포털](https://www.data.go.kr/data/15112345/fileData.do)에서 무료로 다운받으실 수 있습니다. |
| 과학기술정보통신부 국립전파연구원 ICT 융복합 시설의 안전한 전자파 환경 기반 조성 연구 | 과학기술정보통신부_국립전파연구원_ICT_융복합_시설의_안전한_전자파_환경_기반_조성_연구_20241231 | Type 1 | 본 저작물은 과학기술정보통신부 국립전파연구원에서 2024년 작성하여 공공누리 제 1유형으로 개방한 'ICT 융・복합 시설의 안전한 전자파 환경 기반 조성 연구'를 이용하였으며, 해당 저작물은 [공공데이터포털](https://www.data.go.kr/data/15145080/fileData.do)에서 무료로 다운받으실 수 있습니다. |

## Acknowledgements

This dataset was generated using the [kovidore-data-generator](https://github.com/whybe-choi/kovidore-data-generator) pipeline.
We acknowledge the datasets provided by the [Public Data Portal(공공데이터포털)](https://www.data.go.kr/index.do), which were utilized to construct this training dataset.

## Citation

If you use Ko-VDR Train Public in your research, please cite as follows:
```bibtex
@inproceedings{choi-etal-2026-kovidore,
    title = "{KoViDoRe: A Benchmark for {K}orean Visual Document Retrieval",
    author = "Choi, Yongbin and Song, Yongwoo and Sung, Mujeen",
    booktitle = "Proceedings of the 2nd Workshop on Multimodal Augmented Generation via Multimodal Retrieval (MAGMaR 2026)",
    year = "2026",
    doi = "10.18653/v1/2026.magmar-main.11",
    url = "https://aclanthology.org/2026.magmar-main.11/"
}
```