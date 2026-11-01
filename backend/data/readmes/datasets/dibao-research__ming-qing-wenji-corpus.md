---
language:
  - lzh
  - zh
  - ko
license: apache-2.0
task_categories:
  - text-generation
  - token-classification
  - text-classification
tags:
  - classical-chinese
  - historical-documents
  - Ming-dynasty
  - Qing-dynasty
  - literary-collections
  - Siku-Quanshu
  - digital-humanities
  - East-Asian-studies
  - NLP
  - corpus
  - wenji
pretty_name: "Ming-Qing Literary Collections Corpus / 明清別集語料庫 / 명청별집어료고"
size_categories:
  - 10K<n<100K
source_datasets:
  - astra77/huaxia-lib
---

# Ming-Qing Literary Collections Corpus / 明清別集語料庫 / 명청별집어료고

## Dataset Description / 數據集說明 / 데이터셋 설명

### Summary / 概要 / 요약

**English:** The Ming-Qing Literary Collections Corpus is a structured digital corpus of 472 literary collections (bieji 別集) from the Ming (明, 1368–1644) and Qing (清, 1644–1912) dynasties. The texts are sourced from the Siku Quanshu (四庫全書) tradition and include poetry, prose, memorials, essays, letters, and other literary genres by scholars, officials, and literati across three centuries of Chinese intellectual history.

This corpus was derived from [astra77/huaxia-lib](https://huggingface.co/datasets/astra77/huaxia-lib) (Apache 2.0), with dynasty classification, metadata extraction, and structural reorganization applied for research purposes.

**中文：** 明清別集語料庫收錄明（1368–1644）、清（1644–1912）兩代別集472種，涵蓋詩、文、奏疏、書信等文體。文本源自四庫全書系統，經結構化處理後附加朝代分類與元數據。

本語料庫基於 [astra77/huaxia-lib](https://huggingface.co/datasets/astra77/huaxia-lib)（Apache 2.0 授權）加工而成。

**한국어:** 명청별집어료고(明清別集語料庫)는 명(明, 1368–1644)·청(清, 1644–1912) 양대의 별집(別集) 472종을 구조화한 디지털 코퍼스다. 시(詩)·문(文)·주소(奏疏)·서신(書信) 등 다양한 문체를 포함하며, 사고전서(四庫全書) 계통의 텍스트를 원본으로 한다. 학자·관료·문인 등 3세기에 걸친 중국 지성사의 저작을 수록하고 있다.

본 코퍼스는 [astra77/huaxia-lib](https://huggingface.co/datasets/astra77/huaxia-lib)(Apache 2.0)를 원본으로 하여, 조대(朝代) 분류·메타데이터 추출·구조 재편을 거쳐 연구 목적으로 가공한 파생 데이터셋이다.

### Research Significance / 研究價值 / 연구 가치

This corpus is particularly valuable for studies in:

* **Ming-Qing political communication / 明清政治傳播 / 명청 정치 커뮤니케이션:** 451 files across 122 collections contain references to the dibao (邸報) system — the official gazette network of imperial China. / 122종 별집의 451건 파일에서 제국 관보 체계인 저보(邸報) 관련 언급이 확인된다.
* **Literary history / 文學史 / 문학사:** Covers major literary figures including Wang Shizhen (王世貞), Qian Qianyi (錢謙益), Gu Yanwu (顧炎武), Gong Zizhen (龔自珍) and hundreds more. / 왕세정(王世貞)·전겸익(錢謙益)·고염무(顧炎武)·공자진(龔自珍) 등 주요 문인 수백 명의 문집을 포괄한다.
* **NER training / 命名實體識別 / 개체명인식(NER) 훈련:** Rich in named entities (persons, offices, places, institutions) for training Classical Chinese NER models. / 인명·관직명·지명·기관명이 풍부하여 고전 한문 NER 모델 훈련 데이터로 적합하다.
* **Cross-referencing / 交叉對照 / 교차 대조:** Can be linked with the [Wanli Dibao Corpus](https://huggingface.co/datasets/dibao-research/wanli-dibao-corpus) for sender-receiver analysis of Ming political communication. / [만력저보코퍼스](https://huggingface.co/datasets/dibao-research/wanli-dibao-corpus)와 연동하여 명대 정치 커뮤니케이션의 발신자-수신자 분석이 가능하다.

### Languages / 語言 / 언어

* Classical Chinese (文言文 / Literary Chinese, ISO 639-3: `lzh`) / 고전 한문(문언문)
* Some annotations in Modern Chinese (`zh`) / 일부 주석은 현대 중국어(`zh`)
* Dataset card available in Korean (`ko`) / 데이터셋 카드 한국어 병기

## Dataset Structure / 數據結構 / 데이터 구조

### Data Fields / 數據字段 / 데이터 필드

| Field | Type | Description (EN) | 說明 (中文) | 설명 (한국어) |
|-------|------|------------------|-------------|---------------|
| `id` | string | Unique record identifier (dynasty_collection_page) | 記錄唯一識別碼 | 레코드 고유 식별자 (조대_별집_페이지) |
| `dynasty` | string | Dynasty: 明 (Ming) or 清 (Qing) | 朝代 | 조대: 明(명) 또는 清(청) |
| `collection` | string | Name of the literary collection (別集名) | 別集名稱 | 별집명 |
| `page` | integer | Page/section number within the collection | 頁碼/分段序號 | 해당 별집 내 페이지/구간 번호 |
| `juans` | list[string] | Volume numbers (卷) mentioned in the text | 涉及卷數 | 텍스트에 언급된 권(卷) 번호 목록 |
| `siku_category` | string | Siku Quanshu classification (if detected) | 四庫全書分類 | 사고전서 분류 (탐지된 경우) |
| `author` | string | Author name (if detected from text) | 作者（自動提取） | 저자명 (텍스트에서 자동 추출) |
| `char_count` | integer | Character count of the text | 文本字數 | 텍스트 글자 수 |
| `text` | string | Full text content | 全文內容 | 전문(全文) |

### Statistics / 統計 / 통계

| Category | Collections | Records | Characters |
|----------|-------------|---------|------------|
| 明 (Ming / 명) | 329 | 14,138 | 52,154,543 |
| 清 (Qing / 청) | 143 | 6,730 | 25,391,129 |
| **Total / 합계** | **472** | **20,868** | **77,545,672** |

### Data Splits / 數據分割 / 데이터 분할

| Split | Records | Description |
|-------|---------|-------------|
| `train` | 20,868 | Complete corpus (all collections) / 전체 코퍼스 (전 별집 포함) |

## Source and License / 出處及授權 / 출처 및 라이선스

### Original Data / 原始數據 / 원본 데이터

* **Source / 출처:** [astra77/huaxia-lib](https://huggingface.co/datasets/astra77/huaxia-lib)
* **Original License / 원본 라이선스:** Apache-2.0
* **Original Description / 원본 설명:** 四庫別集 1,095 collections from the Siku Quanshu tradition / 사고전서 계통 사고별집 1,095종

### Modifications / 修改說明 / 가공 내역

The following modifications were made to the original data: / 원본 데이터에 대해 다음과 같은 가공을 수행했다:

1. **Extraction / 추출:** Selected 472 collections (329 Ming + 143 Qing) from the full 1,095-collection dataset. / 전체 1,095종에서 472종(명 329 + 청 143)을 선별 추출했다.
2. **Dynasty classification / 조대 분류:** Added `dynasty` field (明/清) based on pre-compiled mapping. / 사전 편성된 매핑 테이블에 기반하여 `dynasty` 필드(明/清)를 부여했다.
3. **Metadata extraction / 메타데이터 추출:** Automatically extracted `author`, `juans`, `siku_category` from text content. / 텍스트 본문에서 `author`·`juans`·`siku_category`를 자동 추출했다.
4. **Structural reorganization / 구조 재편:** Converted from .md page files to JSONL records with structured metadata. / .md 페이지 파일을 구조화된 메타데이터가 포함된 JSONL 레코드로 변환했다.
5. **TOC removal / 목차 제거:** Filtered out table-of-contents pages (p0.md files) that contained only navigation links. / 내비게이션 링크만 포함된 목차 페이지(p0.md)를 제거했다.

### License / 授權 / 라이선스

* **Original texts / 고적 원문:** Public domain (古籍原文, authors deceased 100+ years) / 퍼블릭 도메인 (저자 사후 100년 이상 경과)
* **Dataset compilation and editing / 데이터셋 편집:** Original compilation by astra77, Apache-2.0 / astra77 원 편집, Apache-2.0
* **This derivative dataset / 본 파생 데이터셋:** Apache-2.0 (in compliance with original license terms) / Apache-2.0 (원본 라이선스 조건 준수)
* **Curator / 큐레이터:** dibao-research (Kwanyong Kim / 김관용)

Per Apache 2.0 requirements, this dataset retains attribution to the original author (astra77) and documents all modifications made. / Apache 2.0 요건에 따라 원 저작자(astra77)에 대한 귀속 표시를 유지하고, 모든 가공 내역을 명기했다.

## Considerations for Using the Data / 使用注意事項 / 이용 시 유의사항

### Known Limitations / 已知限制 / 알려진 한계

1. The `author` field is automatically extracted and may be incomplete for some collections. / `author` 필드는 자동 추출이므로 일부 별집에서 누락될 수 있다.
2. The `juans` field captures volume numbers mentioned on each page, not a definitive table of contents. / `juans` 필드는 각 페이지에 언급된 권(卷) 번호일 뿐, 완전한 목차가 아니다.
3. Some collections may contain OCR artifacts from the digitization process. / 디지털화 과정에서 발생한 OCR 오류가 잔존할 수 있다.
4. The `siku_category` is only detected when the text explicitly contains "欽定四庫全書" markers. / `siku_category`는 텍스트에 "欽定四庫全書" 표지가 명시된 경우에만 탐지된다.

### Bias / 偏見 / 편향

The Siku Quanshu represents an imperially-sponsored editorial project of the Qianlong era (18th century). Its selection criteria reflect the political and cultural biases of the Qing court. Works deemed heterodox or politically sensitive were excluded or censored.

사고전서는 건륭(乾隆) 연간(18세기)의 칙편(勅編) 사업이다. 그 선록(選錄) 기준은 청 조정의 정치적·문화적 편향을 반영한다. 이단으로 간주되거나 정치적으로 민감한 저작은 배제되거나 삭개(刪改)되었다.

## Citation / 引用 / 인용

If you use this dataset, please cite both this derivative and the original: / 본 데이터셋을 사용할 경우, 파생 데이터셋과 원본 데이터셋을 모두 인용해 주십시오:

```bibtex
@dataset{ming_qing_wenji_2026,
  title={Ming-Qing Literary Collections Corpus: A Structured Edition from the Siku Quanshu Tradition},
  author={Kim, Kwanyong},
  year={2026},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/dibao-research/ming-qing-wenji-corpus},
  note={Derived from astra77/huaxia-lib (Apache 2.0)}
}

@dataset{astra77_huaxia_lib,
  title={huaxia-lib: 四庫別集 Digital Library},
  author={astra77},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/astra77/huaxia-lib},
  license={Apache-2.0}
}
```

## Related Resources / 相關資源 / 관련 자료

| Resource | Description | Link |
|----------|-------------|------|
| Wanli Dibao Corpus / 만력저보코퍼스 | Ming dynasty official gazette corpus / 명대 관보 코퍼스 | [dibao-research/wanli-dibao-corpus](https://huggingface.co/datasets/dibao-research/wanli-dibao-corpus) |
| huaxia-lib (Original) / 원본 | Full Siku Quanshu literary collections / 사고전서 별집 전체 | [astra77/huaxia-lib](https://huggingface.co/datasets/astra77/huaxia-lib) |
| Ming Shilu (明實錄) / 명실록 | Veritable Records of the Ming Dynasty / 명대 실록 | [Academia Sinica](https://hanchi.ihp.sinica.edu.tw/) |
| CTEXT | Chinese Text Project / 중국철학서전자화계획 | [ctext.org](https://ctext.org) |

## Contact / 聯繫 / 연락처

For questions, corrections, or collaboration inquiries, please use the Discussions tab on this repository or contact via email.

문의·정오(訂誤)·공동연구 제안은 본 리포지토리의 Discussions 탭 또는 이메일로 연락 바랍니다.

* **Email:** humanet2@gmail.com
* **Organization:** [dibao-research](https://huggingface.co/dibao-research)
