---
license: cc-by-nc-nd-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: metadata.csv
dataset_info:
  features:
  - name: dataset_id
    dtype: string
  - name: course_name_ko
    dtype: string
  - name: semester
    dtype: string
  - name: assignment_type
    dtype: string
  - name: team_id
    dtype: string
  - name: work_title_ko
    dtype: string
  - name: file_name
    dtype: string
  - name: relative_path
    dtype: string
  - name: file_format
    dtype: string
  - name: duration_hhmmss
    dtype: string
  - name: frame_width
    dtype: int64
  - name: frame_height
    dtype: int64
  - name: fps
    dtype: float64
  - name: bitrate_kbps
    dtype: int64
  - name: file_size_mb
    dtype: float64
  - name: language
    dtype: string
  - name: summary_ko
    dtype: string
  - name: topic_keywords
    dtype: string
  - name: ai_tools_used
    dtype: string
  - name: editing_tools
    dtype: string
  - name: report_available
    dtype: string
  - name: rights_note
    dtype: string
  - name: notes
    dtype: string
  splits:
  - name: train
    num_examples: 20
tags:
- education
- ai-video
- creative-ai
language:
- ko
size_categories:
- n<1K
---

# Hallym AI Video Production Practice 2025-2 Public Dataset

## 1. 데이터셋 개요

- 데이터셋명: 한림대학교 `AI영상제작실습` 2025-2 공개용 데이터셋
- 교과목명: `AI영상제작실습`
- 학기: `2025-2`
- 생성 배경: 2025학년도 2학기 `AI영상제작실습` 수업에서 조별로 제작·제출한 AI 기반 영상 결과물을 공개용 데이터셋 형태로 정리한 것이다.
- 목적: 수업 기반 AI 영상 창작 결과물을 공개 아카이브 형태로 정리하고, 작품 단위 메타데이터를 함께 제공하기 위함이다.

## 2. 데이터셋 범위

- 총 작품 수: 20편
- 데이터 단위: 조별 제출 영상 1편 = `metadata.csv` 1행
- 포함 대상: `1조`부터 `20조`까지 각 팀 폴더의 원본 MP4 1개
- 제외 대상:
  - 보고서 파일(`.pdf`, `.docx`, `.hwp`)
  - 라이선스 동의서 파일
  - `AI제작콘텐츠 발표회 2025 출품작` 폴더에 따로 복사된 중복 MP4 5개

## 3. 폴더 구조

```text
AI영상제작실습 25-2 영상 모음/
  metadata.csv
  readme.md
  1조/
    *.mp4
  ...
  20조/
    *.mp4
  AI제작콘텐츠 발표회 2025 출품작/
    *.mp4
```

## 4. 메타데이터 설명

`metadata.csv`는 UTF-8 인코딩 CSV이며, 작품 20편에 대한 메타데이터를 제공한다.

| column_name | 설명 |
| --- | --- |
| `dataset_id` | 데이터셋 내부 고유 식별자 |
| `course_name_ko` | 교과목명 |
| `semester` | 학기 |
| `assignment_type` | 과제 유형(`중간과제`, `중간대체과제`) |
| `team_id` | 조 번호 |
| `work_title_ko` | 작품명 |
| `file_name` | 실제 MP4 파일명 |
| `relative_path` | 데이터셋 루트 기준 상대경로 |
| `file_format` | 파일 형식 |
| `duration_hhmmss` | 재생 시간 |
| `frame_width` | 영상 가로 해상도 |
| `frame_height` | 영상 세로 해상도 |
| `fps` | 프레임레이트 |
| `bitrate_kbps` | 비트레이트(kbps) |
| `file_size_mb` | 파일 크기(MB) |
| `language` | 작품의 주 사용 언어 |
| `summary_ko` | 작품 요약 |
| `topic_keywords` | 핵심 주제 키워드 |
| `ai_tools_used` | 생성형 AI 도구 |
| `editing_tools` | 후반 편집 도구 |
| `report_available` | 참고 보고서 확인 여부 |
| `rights_note` | 권리 관련 비고 |
| `notes` | 파일명 불일치, 보고서 형식 문제 등 특이사항 |

### 제목 정규화 기준

- 작품 제목은 보고서에 명시된 제목을 우선 사용했다.
- 영상 파일명이 조 번호, 학기, 과제명 등으로만 구성된 경우에는 파일명 또는 수업 내부 메모를 참고해 사람이 읽기 좋은 제목으로 정규화했다.
- 보고서 제목이 지나치게 일반적인 경우에는 실제 영상 파일명에 나타난 작품명을 우선했다.

### 수작업 보강 항목

- `summary_ko`
- `topic_keywords`
- `ai_tools_used`
- `editing_tools`
- `assignment_type`

위 항목은 조별 보고서를 우선 참고해 작성했으며, 보고서가 없거나 자동 추출이 어려운 경우에는 `not_available` 또는 `not_reported`로 표기했다.

## 5. 수집 및 정리 방법

1. 상위 폴더에서 `^[0-9]+조$` 패턴을 만족하는 조 폴더만 선별했다.
2. 각 조 폴더에서 원본 MP4 1개씩만 데이터셋 본체로 포함했다.
3. 기술 메타데이터는 Windows 파일 속성 기준으로 수집했다.
4. 설명 메타데이터는 조별 보고서(`pdf`, `docx`, `hwp`)를 참고해 수작업 정리했다.
5. `AI제작콘텐츠 발표회 2025 출품작` 폴더의 MP4는 중복본으로 판단하여 제외했다.

## 6. 개인정보 및 권리

- 학생 이름과 학번은 공개용 `metadata.csv`와 `readme.md`에 포함하지 않았다.
- 개별 라이선스 동의서는 내부 보관 자료로만 간주하고 공개 데이터셋에는 포함하지 않았다.
- 공개용 메타데이터는 팀 단위 익명화 기준으로 정리했다.
- `rights_note` 컬럼의 `creator consent documents retained internally`는 권리 확보 문서가 별도 보관 중임을 뜻한다.

## 7. 품질 및 한계

- 일부 작품은 원본 영상 파일명이 일반적이거나 오기되어 있어 제목을 정규화했다.
- `16조`의 원본 영상 파일명은 `AI영상_4조_25-2.mp4`로 저장되어 있어 `notes`에 예외를 기록했다.
- `2조`는 현재 폴더 기준으로 별도 보고서를 확인하지 못해 설명형 메타데이터 일부가 비어 있다.
- `8조`는 보고서가 HWP 형식으로만 존재해 현재 환경에서 자동 파싱하지 못했으며, 일부 설명 메타데이터를 `not_available` 또는 `not_reported`로 남겼다.
- 보고서 형식이 PDF, DOCX, HWP로 혼재되어 있어 조별 메타데이터의 상세도는 완전히 동일하지 않다.

## 8. 문의 및 관리 정보

- 임시 라이선스: `CC BY NC ND 4.0`
- 프로젝트: `글로컬대학 30`

