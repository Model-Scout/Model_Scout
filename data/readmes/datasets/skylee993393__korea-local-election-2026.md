---
language:
- ko
license: other
license_name: kogl-type-1
license_link: https://www.kogl.or.kr/info/license.do#01-tab
tags:
- elections
- korea
- politics
- nec
- mcp
size_categories:
- 1K<n<10K
---

# 9회 전국동시지방선거 (2026.6.3) 후보자 데이터셋

대한민국 제9회 전국동시지방선거 후보자 정보를 중앙선거관리위원회 공식 데이터에서
수집·정제한 데이터셋. AI 자연어 인터페이스(MCP) 와 결합되어 유권자가 자기 지역구
후보 정보를 손쉽게 조회·비교할 수 있도록 제공된다.

## 관련 프로젝트

| 항목 | 링크 |
|---|---|
| GitHub 저장소 (코드) | https://github.com/skymoonlee/electionmcp |
| MCP 서버 (라이브) | https://mcp.electionmcp.kr/mcp |
| 헬스체크 | https://mcp.electionmcp.kr/health |

본 데이터셋만으로도 분석·연구에 사용 가능하지만, MCP 서버를 통한
Claude·Cursor·Cline 등 AI 클라이언트 연동이 권장된다. 자세한 사용법은
GitHub 저장소의 README 참조.

## 출처
- 중앙선거관리위원회 공공데이터포털 OpenAPI (공공누리 1유형)
  - 후보자 정보, 선거공약 정보, 코드 정보
- 중앙선거관리위원회 정보공개자료 (info.nec.go.kr)
  - 전과기록, 재산신고, 병역, 학력, 납세

## 라이선스
공공누리 제1유형 (출처표시) — 출처: **중앙선거관리위원회**

## 사용 목적
공직선거법 제49조에 따른 **국민의 알권리 및 선거권 행사 보장** 목적의 정보 제공.

## 스키마
- `hubo_id`: 후보자 ID
- `sg_type` / `sg_type_name`: 선거 종류 코드 / 명칭
- `sido`, `sgg`, `district`: 광역시도, 시군구, 선거구
- `name`, `party`, `ballot_number`: 이름, 정당, 기호
- `stage`: preliminary | official
- `pledges`: 공약 리스트
- `criminal`, `assets`, `military`, `education`, `tax`: 정보공개자료 텍스트
- `extraction_methods`: PDF 추출 방법 (pdfplumber/ocr/failed)
- `source_urls`: 원본 URL

## 주의사항
선거 결과의 평가나 후보 추천에 이 데이터를 사용하지 마십시오.
사실 정보 조회 및 비교 목적으로만 사용하십시오.
