---
license: cc-by-4.0
language:
  - ko
  - en
pretty_name: Korea PIPC Enforcement Datasets (datalaw.kr)
tags:
  - korea
  - privacy
  - personal-data-protection
  - legal
  - enforcement
  - regulation
  - pipc
  - data-breach
  - damages
size_categories:
  - n<1K
---

# 한국 개인정보 규제 자료 데이터셋 (datalaw.kr)

이 저장소는 이현섭 변호사(법무법인 세움)가 운영하는 사이트 datalaw.kr에 공개 중인 한국 개인정보 규제 자료 CSV 6종을 담은 것입니다. 이 저장소는 사이트에 공개된 최신 판을 주 1회 따라가는 **작업본**이며, 저장소 이름은 `08swap08/korea-pipc-enforcement`입니다. 논문·보고서에서 인용할 고정판은 Zenodo DOI `10.5281/zenodo.22722237`(concept DOI `10.5281/zenodo.22722236`)를 쓰십시오. 버전이 고정된 쪽만 나중에 같은 자료를 다시 재현할 수 있기 때문입니다.

An English summary follows the Korean sections below.

## 수록 파일

모든 파일은 UTF-8로 인코딩되어 있습니다. 첫 줄은 `#`으로 시작하는 고지 줄이고, 둘째 줄이 열 제목입니다. 파일을 읽을 때는 첫 줄을 건너뛰어야 합니다.

| 파일 | 내용 | 행 수 | 기준일 | 원본 |
|---|---|---|---|---|
| `pipc-sanctions.csv` | 개인정보보호위원회 제재 의결 | 1051행 | 2026-10-23 수집 | https://datalaw.kr/sanctions/ |
| `kmcc-sanctions.csv` | 방송통신위원회의 개인정보 사건 의결 | 348행 | 2026-10-23 기준 | https://datalaw.kr/sanctions/kmcc/ |
| `mediation-cases.csv` | 개인정보분쟁조정위원회 공개 조정 사례 | 771행 | 2026-10-23 수집 | https://datalaw.kr/mediation/ |
| `damages-judgments.csv` | 개인정보 유출 민사 손해배상 판결 | 37행 | 2026-10-24 작성 기준 | https://datalaw.kr/damages/ |
| `pipc-fine-mitigation.csv` | 과징금 산정 근거 | 124행 | 2026-10-23 기준 | https://datalaw.kr/decisions/ |
| `law-timeline.csv` | 개인정보·AI 관련 법령 시행일 | 23행 | 2026-10-23 수집 | https://datalaw.kr/timeline/ |
| `pipc-decision-labels.csv` | 제재 의결 심층 라벨(1행=1의결) | 833행 | 2026-10-12 기준 | https://datalaw.kr/decision-labels/ |
| `pipc-decision-articles.csv` | 위반으로 인정된 조문(1행=1조문) | 2633행 | 2026-10-12 기준 | https://datalaw.kr/decision-labels/ |
| `pipc-decision-mitigation.csv` | 가중·감경 사유(1행=1사유) | 2137행 | 2026-10-12 기준 | https://datalaw.kr/decision-labels/ |
| `pipc-decision-issues.csv` | 쟁점(1행=1쟁점) | 337행 | 2026-10-12 기준 | https://datalaw.kr/decision-labels/ |

최종 동기화: 2026-10-26

### 1. `pipc-sanctions.csv`
개인정보보호위원회의 제재 의결을 담은 파일입니다. 1051행이며 수집일은 2026-10-23입니다.
열: 의결일, 안건번호, 사건번호, 의결주체, 피심인, 위반조문, 처분, 과징금(원), 과태료(원), 행 주소, 원문 게시물, coverage_status

`coverage_status`(2026-10-19 추가)는 이 행의 안건번호가 `pipc-decision-labels.csv` 에도 있으면 `in_labels`, 없으면 `not_in_labels` 입니다. 두 표는 원천이 다르고(결정문 게시판 / 국가법령정보센터 법령 API) 하나의 모집단이 아니므로 비율로 읽지 마십시오. 세 표의 단위·겹침·결손은 https://datalaw.kr/data/coverage.json 에 있습니다.

### 2. `mediation-cases.csv`
개인정보분쟁조정위원회가 공개한 조정 사례를 담은 파일입니다. 771행이며 수집일은 2026-10-23입니다.
열: 연번, 연도, 구분, 침해유형, 제목, 손해배상 금액, 결론, 판단 이유, 인용 조문, 원문, 행 주소

### 3. `damages-judgments.csv`
개인정보 유출에 관한 민사 손해배상 판결을 담은 파일입니다. 37행이며 작성 기준일은 2026-10-24입니다. 다른 파일과 달리 사람이 직접 정리한 자료입니다.
열: 사고, 사고 유형, 피고, 피고 표기 근거, 침해내용, 결과, 확정 상태, 1인당 인정액, 인정액 경위, 심급 경과, 판단을 가른 것, 행 주소

### 4. `pipc-fine-mitigation.csv`
개인정보보호위원회 결정문의 「이유」 절에서 추출한 과징금 산정 근거를 담은 파일입니다. 124행이며 기준일은 2026-10-23입니다.
열에는 의결일, 안건번호, 피심인, 과징금, 산정 기준, 조문, 중대성, 1차 가중, 2차 가중, 감경 비율과 감경 사유가 있습니다.

### 5. `law-timeline.csv`
개인정보·AI 관련 법령의 시행일을 담은 파일입니다. 23행이며 수집일은 2026-10-23입니다. 국가법령정보센터의 시행예정법령을 기준으로 정리한 자료입니다.
열: 시행일, 법령명, 구분, 제개정, 공포번호, 공포일, 같은 개정의 다른 시행일, 비고 요지, 비고, 해설, 행 주소

### 6. `kmcc-sanctions.csv`
방송통신위원회가 개인정보 사건에 내린 의결을 담은 파일입니다. 348행이며 기준일은 2026-10-23입니다. 방송통신위원회는 폐지된 기관이고, 의결서가 스캔 PDF로만 남아 있어 기계가 본문을 읽지 못합니다. 이 파일은 그 스캔본을 이미지로 구워 OCR을 걸고, 뽑힌 텍스트를 파싱해 표로 구조화한 것입니다. 기계가 읽을 수 있는 형태의 같은 자료는 다른 곳에 없습니다. 원문은 https://datalaw.kr/sanctions/kmcc/ 에 있습니다.
열: 의결일, 안건번호, 피심인(의결 당시 상호), 업종, 위반조문, 처분, 과징금(원), 과태료(원), 행 주소, 의결서 PDF

### 7. `pipc-decision-labels.csv` · 8. `pipc-decision-articles.csv` · 9. `pipc-decision-mitigation.csv` · 10. `pipc-decision-issues.csv`

제재 의결 833건의 결정문 본문을 읽어 구조화한 네 파일입니다. 앞의 여섯 파일과 달리 **대규모언어모델(claude-opus-5)이 본문에서 추출한 값**이며, 원천은 datalaw.kr 수집물이 아니라 국가법령정보센터 법령 API(target=ppc)입니다. 수록 기간은 2012-11-12부터 2026-09-09까지입니다.

- `pipc-decision-labels.csv` 열: 의결일, 안건번호, 사건번호, 피심인, 결정문일련번호, 안건명, 사실관계유형, 한 패스만 고른 유형, 사실관계요지, 업종, 사업자유형, 적용법버전, 적용법 판, 정보주체수(명), 유출건수(건), 수치 근거, 유출항목, 공중노출, 중대성등급, 과징금(원), 과태료(원), 쟁점수, 불명확항목, 2회추출 불일치 항목, 원문(법령API), coverage_status — `in_sanctions`(같은 안건번호가 pipc-sanctions.csv 에 있음)·`before_sanctions_scope`(제재 DB 범위 2020-11-25 전 의결)·`policy_recommendation`(정책 부처에 한 권고 — 제재 범위 밖)·`in_unpublished_layer`(결정문이 게시판에서 내려가 미공개 제재 표에 있음)·`not_in_sanctions`(이유 미상)·`no_agenda_no`(안건번호가 비어 대조하지 않음), 2026-10-19 추가
- `pipc-decision-articles.csv` 열: 의결일, 안건번호, 사건번호, 피심인, 결정문일련번호, 법령, 조문, 층위, 2회추출 확인, 내용요지, 원문표기(법령), 원문표기(조문), 원문(법령API)
- `pipc-decision-mitigation.csv` 열: 의결일, 안건번호, 사건번호, 피심인, 결정문일련번호, 구분, 사유, 원문표현, 원문(법령API)
- `pipc-decision-issues.csv` 열: 의결일, 안건번호, 사건번호, 피심인, 결정문일련번호, 피심인 주장, 위원회 판단, 원문(법령API)

**품질 측정.** 같은 결정문을 두 번 독립 추출해 값이 일치하는 비율을 실측했습니다. 중대성등급 99.7%, 안건번호 98.8%, 정보주체수 96.8%, 사업자유형 95.0%이고, 위반조문은 법령명·조문 표기를 정규화한 뒤 90.0%(자카드 평균 94.4%)입니다. 행마다 「2회추출 불일치 항목」 칸에 **어느 항목이 갈렸는지** 적었습니다(833행 중 493행은 전부 일치). 비교 대상은 구조화 항목(중대성등급·사업자유형·사실관계유형·위반조문)뿐입니다 — 업종·적용법버전·사실관계요지는 자유서술이라 두 패스가 같은 뜻을 다르게 적는 일이 많아(「대리점 판매」/「대리점을 통한 판매」) 문자열 일치로 재면 멀쩡한 값을 불량으로 표시하게 됩니다. 적용법버전은 그 대신 규칙으로 판(版)만 뽑아 `적용법 판` 열에 넣었습니다(데이터3법 개정 전 2행 / 개정 후~전부개정 전 477행 / 2023년 전부개정 후 346행 / 판정 불가 8행).

**금액은 모델 값이 아닙니다.** 검증에서 모델이 과태료를 과징금 항목에 넣는 오류가 10%대로 확인되었고, 두 추출이 같이 틀리는 경우는 일치율 검사로 걸러지지 않았습니다. 따라서 과징금·과태료는 결정문 주문의 문언을 규칙으로 파싱한 값을 실었으며, `pipc-sanctions.csv` 와 겹치는 696건에서 과징금 97.5%·과태료 99.1%가 일치했습니다. 2026-10-11 에 제공 요청·침해요인 심의 등 제재가 아닌 의결 41건을 걸러냈습니다(874→833행).

**위반조문도 합집합입니다.** 두 패스가 갈리는 지점은 법률이 아니라 그 아래 시행령·고시를 함께 적을지였습니다(한쪽에만 있는 조문의 77%가 시행령·고시). 층위(법률·시행령·고시·시행규칙)와 `2회추출 확인`(양쪽/한쪽)을 열로 두었으니 필요에 맞게 거르십시오. 법률 1,229행 중 1,178행(96%)은 두 번 다 잡혔습니다.

**사실관계유형은 합집합입니다.** 두 번 추출한 결과를 합쳐 실었습니다 — 선례 검색에서는 놓치는 것이 잘못 걸리는 것보다 해롭기 때문입니다. 한 번만 잡힌 유형은 `한 패스만 고른 유형` 열에 따로 적었으니, 정밀도를 우선하시려면 그 열의 유형을 빼고 쓰십시오(833행 중 201행에 해당). 포괄 항목 「기타」는 정보가 없고 변동만 만들어 뺐습니다 — 유형 칸이 빈 32행이 그에 해당합니다.

**유출 규모의 단위.** 결정문은 규모를 「명」으로도 「건」으로도 적는다(「개인정보 약 844건」). 한 사람이 여러 건일 수 있어 둘은 같은 값이 아니므로 열을 나누었다 — 원문 표기를 대조해 「명」이면 `정보주체수(명)`(270행), 「건」이면 `유출건수(건)`(79행)에 넣고, 판정 근거를 `수치 근거` 열에 적었다. 본문에서 그 수를 찾지 못한 19행은 「본문에서 수치 확인 못 함」으로 표시했다.

**빈 칸의 뜻.** 결정문이 금액·인원·상호를 비실명으로 가렸거나 표·이미지로만 표시해 본문에서 읽을 수 없는 경우입니다. 추정값을 넣지 않았고 사유는 `불명확항목` 열에 적었습니다. 피심인 상호를 확인할 수 있는 의결은 833건 중 383건입니다. 법령 API가 본문을 중간에서 끊어 돌려주는 제재 의결 73건은 수록하지 않았습니다.

## 용도

이 자료는 다음과 같은 용도로 쓸 수 있습니다.

- 한국 개인정보 규제 연구
- 제재 경향 분석
- 법률 정보 검색·질의응답 시스템의 근거 자료

이 자료는 개별 사건의 법률 판단을 대체하지 않습니다.

## 한계와 주의사항

이용자는 자료를 쓰기 전에 아래 사항을 확인해야 합니다.

1. 정확성. `damages-judgments.csv`를 제외한 파일은 기계 추출 요약이며, 배포자는 정확성을 보증하지 않습니다. 이용자는 자료를 근거로 쓰기 전에 결정문과 판결문 원문을 확인해야 합니다.
2. 비실명 처리. 개인정보보호위원회가 비실명 처리한 피심인은 이 자료에서도 그대로 비실명입니다. 가려진 이름을 다른 자료로 특정하지 않는 것이 이 자료의 원칙입니다. 이용자도 가려진 이름을 다른 자료로 특정하지 않아야 합니다.
3. 수집 범위. 이 자료는 결정문 본문이 공개된 의결만 담습니다. 따라서 이 자료의 건수는 전수가 아니라 하한입니다.
4. 갱신. 자료는 계속 갱신됩니다. 이용자는 자료를 인용할 때 수집일을 함께 적어야 합니다.
5. 정정 요청. 오류를 발견한 이용자는 hyunsub.lee@seumlaw.com 으로 정정을 요청할 수 있습니다.

## 라이선스

정리물의 라이선스는 CC BY 4.0(https://creativecommons.org/licenses/by/4.0/)입니다. 원문 결정·판결 자체는 한국 저작권법 제7조에 따라 저작권 보호 대상이 아닙니다.

## 출처 표기

권장 출처 표기는 다음과 같습니다. 수집일은 실제로 사용한 파일의 수집일로 바꿔 적습니다.

> 이현섭 변호사(법무법인 세움), 「개인정보위 제재 추적기」, https://datalaw.kr/sanctions/ (YYYY-MM-DD 수집분)

학술 인용에는 DOI를 씁니다.

- 판이 고정된 버전: https://doi.org/10.5281/zenodo.22722237
- 항상 최신판: https://doi.org/10.5281/zenodo.22722236

## English Summary

### Overview

This repository contains six CSV files of Korean personal data protection enforcement and regulatory records, published by Hyunsub Lee, attorney at SEUM Law, on https://datalaw.kr. It is a **working copy** that follows the latest CSV files published on that site with a weekly sync. For citation in papers and reports, use the fixed version on Zenodo: DOI `10.5281/zenodo.22722237` (concept DOI `10.5281/zenodo.22722236`). Reproducibility lives with the version-pinned copy, not with a moving one.

All files are UTF-8 encoded. The first line of each file is a notice line beginning with `#`; the second line is the column header. Skip the first line when parsing.

### Files

| File | Content | Rows | Reference date | Source page |
|---|---|---|---|---|
| `pipc-sanctions.csv` | Enforcement decisions of the Personal Information Protection Commission (PIPC) | 1051 | Collected 2026-10-23 | https://datalaw.kr/sanctions/ |
| `kmcc-sanctions.csv` | Decisions of the Korea Communications Commission (KCC) in personal data cases, structured from scanned decision PDFs via OCR | 348 | As of 2026-10-23 | https://datalaw.kr/sanctions/kmcc/ |
| `mediation-cases.csv` | Published mediation cases of the Personal Information Dispute Mediation Committee | 771 | Collected 2026-10-23 | https://datalaw.kr/mediation/ |
| `damages-judgments.csv` | Civil damages judgments on personal data breaches (manually compiled) | 37 | As of 2026-10-24 | https://datalaw.kr/damages/ |
| `pipc-fine-mitigation.csv` | Administrative fine calculation grounds extracted from the reasoning section of PIPC decisions | 124 | As of 2026-10-23 | https://datalaw.kr/decisions/ |
| `law-timeline.csv` | Effective dates of Korean personal data and AI related statutes, based on the National Law Information Center | 23 | Collected 2026-10-23 | https://datalaw.kr/timeline/ |
| `pipc-decision-labels.csv` | Deep labels of PIPC enforcement decisions, one row per decision | 833 | As of 2026-10-12 | https://datalaw.kr/decision-labels/ |
| `pipc-decision-articles.csv` | Provisions found violated, one row per provision | 2633 | As of 2026-10-12 | https://datalaw.kr/decision-labels/ |
| `pipc-decision-mitigation.csv` | Aggravating and mitigating grounds, one row per ground | 2137 | As of 2026-10-12 | https://datalaw.kr/decision-labels/ |
| `pipc-decision-issues.csv` | Contested issues, one row per issue | 337 | As of 2026-10-12 | https://datalaw.kr/decision-labels/ |

Last synced: 2026-10-26

Column headers are in Korean. The Korean sections above list the columns of each file.

About `kmcc-sanctions.csv`: before the PIPC became the single supervisory authority, the Korea Communications Commission (KCC) — an agency that has since been abolished — decided personal data cases under the Network Act. Its decisions survive only as scanned PDFs that machines cannot read. Standard PDF text extraction returns nothing for most of them (only 3 of a 40-document sample carry a text layer), so this table was built by rasterising the scans, running OCR and parsing the result into 348 structured decisions (as of 2026-08-21). The same data is not available anywhere else in machine-readable form. Source: https://datalaw.kr/sanctions/kmcc/. Columns: 의결일 (decision date), 안건번호 (agenda number), 피심인(의결 당시 상호) (respondent, trade name at the time of decision), 업종 (industry), 위반조문 (provisions violated), 처분 (disposition), 과징금(원) (administrative fine, KRW), 과태료(원) (negligence fine, KRW), 행 주소 (row anchor URL), 의결서 PDF (decision PDF).

### Intended uses

- Research on Korean personal data protection regulation
- Analysis of enforcement trends
- Grounding material for legal information retrieval and question answering systems

This dataset does not replace legal judgment on any individual case.

### Limitations

1. Accuracy. Except for `damages-judgments.csv`, the records are machine-extracted summaries. The publisher does not guarantee accuracy. Verify against the original decisions and judgments before relying on any record.
2. Pseudonymized parties. Where the PIPC has pseudonymized a respondent, the respondent remains pseudonymized in this dataset. This dataset does not identify masked parties from other sources, and users are asked to follow the same principle.
3. Coverage. Only decisions whose full text has been published are included. The counts are therefore a lower bound, not a complete census.
4. Updates. The data is updated over time. Cite the collection date together with the file.
5. Corrections. Send correction requests to hyunsub.lee@seumlaw.com.

### License and citation

The compilation is licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The underlying decisions and judgments are not subject to copyright protection under Article 7 of the Korean Copyright Act.

Suggested citation:

> Hyunsub Lee (SEUM Law), "Korea PIPC Enforcement Tracker", https://datalaw.kr/sanctions/ (collected YYYY-MM-DD)

For academic citation, use the DOI:

- Version DOI (fixed): https://doi.org/10.5281/zenodo.22722237
- Concept DOI (always latest): https://doi.org/10.5281/zenodo.22722236

### Disclaimer

This is not legal advice. The dataset is provided for informational and research purposes only and does not replace legal judgment on any individual case.
