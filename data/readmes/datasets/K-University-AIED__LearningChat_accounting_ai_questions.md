---
license: cc-by-nc-nd-4.0
configs:
- config_name: default
  data_files:
  - split: train
    path: metadata.csv
dataset_info:
  features:
  - name: record_id
    dtype: string
  - name: file_name
    dtype: string
  - name: section_id
    dtype: string
  - name: export_batch_ts
    dtype: string
  - name: student_uid
    dtype: string
  - name: student_image_index
    dtype: int64
  - name: file_ext
    dtype: string
  - name: file_size_bytes
    dtype: int64
  - name: filename_pattern_group
    dtype: string
  - name: sha256
    dtype: string
  splits:
  - name: train
    num_examples: 787
tags:
- education
- accounting
- ai-questions
language:
- ko
size_categories:
- n<1K
---

# 공개용 회계입문 AI질문 이미지 데이터셋

이 데이터셋은 회계입문 수업의 `AI질문 1회` 과제 제출 이미지들을 공개용으로 문서화하기 위해 정리한 메타데이터 패키지다. 현재 폴더에 존재하는 6개 수집 배치 전체를 통합했으며, 공개 버전에서는 학생 실명과 원본 파일명을 직접 노출하지 않도록 비식별 규칙을 적용했다.

본 문서와 함께 제공되는 `metadata.csv`는 이미지 파일 1개당 1행을 가지는 인벤토리다. 실제 공개 배포 시 이미지 파일은 `data/images/AIQ-XXXXXX.ext` 형식으로 익명 재배치하는 것을 전제로 한다.

## 1. 데이터셋 범위

- 대상 과목: 회계입문
- 대상 과제: `AI질문 1회`
- 포함 범위: 현재 작업 폴더에 있는 6개 수집 배치 전체
- 레코드 단위: 이미지 파일 1개 = `metadata.csv` 1행
- 공개 버전 기준: 완전 비식별 전제

### 분반별 구성

| section_id | 익명 제출자 수 | 이미지 수 |
| --- | ---: | ---: |
| 205201-02 | 38 | 313 |
| 205201-03 | 39 | 484 |
| 합계 | 77 | 797 |

### 배치 시각별 구성

| section_id | export_batch_ts | 이미지 수 |
| --- | --- | ---: |
| 205201-02 | 2026-02-03_11-49-51 | 155 |
| 205201-02 | 2026-02-03_11-53-38 | 158 |
| 205201-03 | 2026-02-03_11-54-31 | 121 |
| 205201-03 | 2026-02-03_11-54-50 | 125 |
| 205201-03 | 2026-02-03_11-54-59 | 134 |
| 205201-03 | 2026-02-03_11-56-04 | 104 |

## 2. 수집 배경과 원천

원본 데이터는 학생들이 과제 제출 과정에서 업로드한 이미지 파일들로 구성되어 있다. 현재 로컬 작업 폴더에서는 다음 구조로 정리되어 있었다.

```text
클라썸_과제물_회계입문 (분반)__과제_ AI질문 1회_배치시각/
└─ 검토 완료/
   └─ 학생명/
      └─ 이미지 파일
```

이미지의 실제 내용은 스크린샷, 모바일 캡처, 사진, 앱 내보내기 이미지 등이 혼합되어 있으며, 해상도와 비율, 파일명 규칙이 균질하지 않다. 원본에는 동일 분반 내 여러 수집 배치가 존재하므로, 본 메타데이터는 `section_id`와 `export_batch_ts`를 함께 보존한다.

## 3. 데이터 구성 요약

- 총 이미지 수: 797
- 총 익명 제출자 수: 77
- 총 용량: 257,782,276 bytes (약 245.84 MB)
- 파일 형식: `png` 485개, `jpg` 303개, `jpeg` 9개
- 중복 제거 여부: 수행하지 않음. 원본 수집 배치의 파일을 전수 유지함

### 원본 파일명 패턴 그룹 분포

`filename_pattern_group`은 원본 파일명을 직접 공개하지 않고 파일 생성 양식을 기술적으로 요약하기 위한 비식별 분류값이다.

| filename_pattern_group | 의미 | 건수 |
| --- | --- | ---: |
| `uuid_like` | UUID 유사 자동 생성 파일명 | 418 |
| `rn_image_picker` | React Native image picker 임시 파일명 | 103 |
| `screenshot` | 스크린샷 계열 파일명 | 67 |
| `numeric` | 숫자 위주 파일명 | 43 |
| `img_prefix` | `IMG_` 접두 파일명 | 33 |
| `kakaotalk` | 카카오톡 저장 파일명 | 33 |
| `other` | 그 외 비정형 파일명 | 100 |

## 4. 비식별화 및 파일명 정책

- 학생 실명은 공개 메타데이터에 포함하지 않는다.
- 원본 학생 폴더 경로와 원본 파일명은 공개 메타데이터에 포함하지 않는다.
- 학번, 학과명, 기기명 등 식별 가능 문자열은 공개 메타데이터에서 제거한다.
- 각 제출자는 분반별 익명 ID인 `student_uid`로만 표현한다.
- 각 이미지에는 전역 고유 식별자인 `record_id`를 부여한다.
- 공개용 `file_name`은 `data/images/AIQ-XXXXXX.ext` 형식의 익명 파일명으로 정의한다.

익명 ID 예시는 다음과 같다.

- `205201-02_STU_001`
- `205201-03_STU_014`

`student_uid`는 같은 분반 안에서 정렬된 제출자 목록 기준으로 부여한 안정적인 익명 식별자다. `student_image_index`는 같은 수집 배치 내 동일 제출자 폴더에서 자연 정렬한 순번이다.

## 5. metadata.csv 컬럼 설명

| column | type | 설명 |
| --- | --- | --- |
| `record_id` | string | 전역 순번 기반 공개 식별자. 형식: `AIQ-000001` |
| `file_name` | string | 공개 패키지에서 사용할 익명 파일 경로. 형식: `data/images/AIQ-000001.png` |
| `section_id` | string | 원본 최상위 폴더에서 추출한 분반 ID |
| `export_batch_ts` | string | 원본 최상위 폴더 끝의 배치 시각 |
| `student_uid` | string | 분반별 익명 제출자 ID |
| `student_image_index` | int | 같은 배치의 같은 제출자 폴더 안에서의 자연 정렬 순번 |
| `file_ext` | string | 파일 확장자 (`png`, `jpg`, `jpeg`) |
| `file_size_bytes` | int | 파일 크기 바이트 단위 값 |
| `filename_pattern_group` | string | 원본 파일명 규칙을 비식별적으로 분류한 값 |
| `sha256` | string | 무결성 검증용 SHA-256 해시 |

## 6. 활용 제한 및 한계

- 이 데이터셋에는 정답 라벨, 평가 점수, 과제 채점 결과가 포함되어 있지 않다.
- 현재 메타데이터는 기술적 인벤토리 중심이며, 의미 기반 주석은 포함하지 않는다.
- 이미지 내용은 학생이 직접 업로드한 화면 캡처 또는 사진이므로, 텍스트 노출 방식과 화질이 매우 불균질하다.
- 원본 이미지 내부에는 이름, 계정 정보, 대화 내용, 기기 정보 등 개인정보가 남아 있을 수 있다.
- 따라서 외부 공개 전에는 이미지 픽셀 단위의 2차 비식별 검수와 필요 시 마스킹 작업이 별도로 필요하다.

## 7. 검증 요약

현재 `metadata.csv` 기준으로 다음 조건을 만족하도록 생성했다.

- 총 행 수 797
- `record_id` 유일성 확보
- `file_name` 유일성 확보
- `section_id`별 건수 일치: `205201-02=313`, `205201-03=484`
- `student_uid` 고유 개수 일치: `205201-02=38`, `205201-03=39`
- `file_ext` 값은 `png`, `jpg`, `jpeg`로 제한
- `filename_pattern_group` 값은 정의된 7개 범주로 제한

## 8. 라이선스 및 문의처

- 임시 라이선스: `CC BY NC ND 4.0`
- 프로젝트: `글로컬대학 30`

