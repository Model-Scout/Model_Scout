---
license: other
license_name: common-crawl
license_link: https://commoncrawl.org/terms-of-use/
language:
- ko
tags:
- korean
- web
- commoncrawl
- text
size_categories:
- 1M<n<10M
---

# CC-korean

한국어 웹 텍스트 코퍼스. CommonCrawl WET 파일에서 추출한 한국어 문서 데이터셋입니다.

## 데이터 수집 방법

- **소스**: [CommonCrawl](https://commoncrawl.org/) WET 파일 (HTML 제거된 텍스트 포맷)
- **수집 스냅샷**: CC-MAIN-2025-05 ~ CC-MAIN-2026-12 (총 15개 스냅샷, 2025~2026년)
- **언어 필터**: fasttext `lid.176.bin` 모델로 한국어(`ko`) 감지, 신뢰도 0.5 이상만 수집
- **1차 품질 필터**: 수집 단계에서 휴리스틱 줄 단위 노이즈 제거 + KenLM perplexity 필터 적용

## 필터링

수집 후 추가로 2단계 필터링 적용.

**줄 단위 인라인 제거**:
- URL, 이모티콘, 대괄호 태그, 기자 바이라인, 출처 표기 등

**줄 단위 제거 항목**:
- 한국어 없는 줄 (영문·중문·일문 등)
- UI/네비게이션 잔재 (로그인, 더보기, 공유 버튼, 파이프 구분자 등)
- 날짜·메타 태그, 주소, 사업자 정보, 저작권 문구
- 광고·도박·성인 키워드, 게시판 헤더, 페이지네이션 등
- 총 약 4,300만 줄 제거

**문서 단위 필터링**: 총 3,695,378개 입력 → 3,570,675개 통과 (96.6%)

## 데이터 규모

| 항목 | 값 |
|---|---|
| 스냅샷 수 | 15 |
| 총 문서 수 | 3,570,675 |
| 총 용량 | 약 36 GB |

## 칼럼 설명

| 칼럼 | 타입 | 설명 |
|---|---|---|
| `url` | string | 원본 문서 URL |
| `date` | string | WET 파일 수집 날짜 |
| `text` | string | 필터링 후 본문 텍스트 |
| `char_count` | int | 문자 수 |
| `line_count` | int | 줄 수 |
| `lang_conf` | float | 언어 감지 신뢰도 |
| `license` | string | Common Crawl Terms of Use |

## 라이선스

본 데이터셋은 CommonCrawl이 수집한 공개 웹 페이지에서 추출되었습니다.
원본 콘텐츠의 저작권은 각 웹사이트 및 저작권자에게 있습니다.
본 데이터셋은 연구 목적으로 제공되며, 상업적 이용 시 원본 저작권자의 허락이 필요합니다.
수집 조건: [Common Crawl Terms of Use](https://commoncrawl.org/terms-of-use/)
