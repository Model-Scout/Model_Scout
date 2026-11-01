---
license: other
language:
- ko
task_categories:
- image-to-text
tags:
- ocr
- document-parsing
- korean
- benchmark
pretty_name: KoOCR-Bench
size_categories:
- n<1K
---

# KoOCR-Bench v1.2

한국어 문서 OCR·문서 파싱 벤치마크입니다. 실제 한국 문서 623쪽(7개 영역)으로 글자, 표, 제목, 읽기 순서, 좌표를 함께 평가합니다. **평가 전용**입니다. 학습에 쓰지 마세요.

A Korean document OCR / parsing benchmark: 623 real Korean pages in 7 slices, scoring text, HTML tables, headings, reading order and block boxes. Evaluation only.

## 구성

| 영역 (slice) | 쪽 | 정답 | 출처 |
|---|---|---|---|
| tables | 100 | HWPX 원본 표 격자 | korea.kr 정책브리핑 첨부 (공공누리 제1유형) |
| kostat_wide | 100 | 원본 통계표 격자 | 통계청 공개 통계표 |
| gwanbo_table | 100 | PDF 텍스트층 | 대한민국 관보 |
| kdi_headings | 100 | 저자 북마크 제목 + PDF 텍스트층 | KDI 보고서 |
| suneung2026 | 104 | PDF 텍스트층 | 2026학년도 대학수학능력시험 |
| user_real | 100 | PDF 텍스트층 | 실사용자 업로드 문서 |
| handwritten | 19 | 사람이 읽어 전사 | 웹에 공유된 손글씨 학습 노트 |

영역별 출처와 라이선스는 `manifest.jsonl`의 `source`, `license` 필드에 있습니다.

## 채점 (`code/koocr_score.py`, `code/koocr_total.py`)

- **글자 영역**: 1 − CER. 비교 전에 마크업, 공백, 줄바꿈을 지우고 NFKC 정규화한 뒤 글자와 숫자만 남깁니다. 띄어쓰기, 줄바꿈, 문장부호 표기 차이는 감점하지 않습니다.
- **외국 문자 패널티**: 한국어 벤치이므로, 정답에 없는 외국 문자(한자, 가나, 키릴 등)는 일반 오류 1개 + 추가 2개로 셉니다. 정답에 실제로 있는 한자(관보, 수능)는 감점하지 않습니다.
- **반복 폭주**: 페이지 CER은 1에서 자릅니다.
- **표**: HTML `<table>`만 채점합니다(TEDS). `<th>`/`<td>` 차이와 rowspan/colspan 외 속성은 무시합니다. Markdown 표는 0점입니다.
- **bbox**: 블록 중 좌표가 붙은 블록의 비율입니다.
- **읽기 순서**: 정답 줄이 출력에서 나오는 순서의 최장 증가 부분열 비율입니다.
- **제목**: KDI 저자 북마크 제목 재현율입니다.

### 배점

| gwanbo | kostat | kdi | tables | handwriting | user | bbox | order | suneung | heading | grid |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.15 | 0.18 | 0.12 | 0.12 | 0.10 | 0.10 | 0.08 | 0.05 | 0.05 | 0.04 | 0.02 |

총점은 측정한 항목의 가중치 합으로 나눠 정규화합니다. v1.1(2026-10-05)에서 통계표와 표 비중을 올리고, 읽기 순서(줄 단위 거친 지표)와 표 정확일치(엔진 간 변별력 낮음) 비중을 낮췄습니다.

## 결과 (2026-10-05, 604쪽, 필기 제외)

| rank | engine | total | gwanbo | kostat | kdi | tables | user | bbox | order | suneung | heading | grid |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | mistral-ocr | 0.7734 | 0.920 | 0.767 | 0.904 | 0.637 | 0.520 | 0.917 | 0.871 | 0.734 | 0.861 | 0.130 |
| 2 | schift-ocr (ours) | 0.7551 | 0.903 | 0.727 | 0.902 | 0.657 | 0.453 | 0.944 | 0.873 | 0.688 | 0.819 | 0.105 |
| 3 | mineru-4 (advanced) | 0.7523 | 0.897 | 0.704 | 0.937 | 0.640 | 0.413 | 0.941 | 0.934 | 0.722 | 0.792 | 0.150 |
| 4 | paddleocr-vl-1.6 | 0.7483 | 0.882 | 0.740 | 0.864 | 0.623 | 0.480 | 0.858 | 0.922 | 0.722 | 0.881 | 0.145 |
| 5 | unlimited-ocr (base) | 0.7454 | 0.853 | 0.741 | 0.901 | 0.625 | 0.470 | 0.963 | 0.868 | 0.702 | 0.743 | 0.080 |
| 6 | gemini-3.1-flash-lite | 0.7363 | 0.891 | 0.756 | 0.897 | 0.585 | 0.528 | 0.852 | 0.860 | 0.448 | 0.852 | 0.105 |
| 7 | ovisocr2 | 0.6625 | 0.904 | 0.751 | 0.857 | 0.632 | 0.464 | 0.000 | 0.874 | 0.676 | 0.663 | 0.155 |
| 8 | clova-ocr | 0.6600 | 0.834 | 0.721 | 0.905 | 0.643 | 0.359 | 1.000 | 0.694 | 0.154 | 0.000 | 0.080 |
| 9 | deepseek-ocr | 0.6119 | 0.657 | 0.651 | 0.827 | 0.553 | 0.472 | 0.466 | 0.874 | 0.582 | 0.421 | 0.070 |
| 10 | gemini-3.5-flash-lite | 0.5910 | 0.594 | 0.559 | 0.787 | 0.501 | 0.376 | 0.841 | 0.811 | 0.340 | 0.743 | 0.070 |
| 11 | google-vision | 0.4147 | 0.670 | 0.000 | 0.906 | 0.000 | 0.406 | 0.765 | 0.809 | 0.520 | 0.000 | 0.000 |

- 모든 엔진은 temperature 0, repetition_penalty 1.0, 디코딩 트릭 없이 한 번 실행했습니다. schift-ocr은 같은 조건 2회 평균입니다.
- 출력 형식과 공식 프롬프트는 [`FORMAT.md`](FORMAT.md)에 있습니다. 범용 VLM(Gemini)은 공식 프롬프트를 그대로 보냈고, OCR API(Mistral, CLOVA, Google Vision)는 API가 돌려주는 블록 좌표를 공개 어댑터(`code/engines/api_koocr_v12.py`)로 같은 형식에 맞췄습니다.
- v1.2(2026-10-05): v1.1까지는 Gemini·Mistral·CLOVA에 좌표를 요청하지 않아(또는 받은 좌표를 버려) 이 세 엔진의 bbox가 0이었습니다. 세 API를 좌표를 받는 방식으로 다시 돌려 고쳤고, gemini-3.5-flash-lite를 추가했습니다.
- Gemini 3.5는 thinkingBudget 0을 받지 않아 가장 낮은 thinkingLevel(`minimal`)로 실행했습니다.
- PaddleOCR-VL은 별도 layout box 목록, MinerU는 middle_json 블록 좌표로 bbox를 계산했습니다(`results/bbox_override_v2.json`). OvisOCR2는 모델에 좌표 출력 기능이 없어 bbox 0입니다.
- 필기 영역은 정답 전사 검수를 마친 뒤 v2에서 총점에 넣습니다. 데이터는 지금도 공개되어 있습니다.
- 상용 API(Gemini, CLOVA, Mistral, Google Vision)는 점수만 공개합니다. 오픈 모델 예측은 `predictions/`에 있습니다.

## 재현

```
python code/koocr_score.py manifest.jsonl myengine=pred.jsonl --tier full > scores.txt
python code/koocr_total.py --bbox-override results/bbox_override_v2.json --no-handwriting scores.txt
```

예측 파일은 한 줄에 `{"id": <manifest id>, "text": <engine output>}`입니다. TEDS는 opendataloader-bench의 `evaluator_table`을 씁니다(`ODLB_SRC` 환경변수). 엔진 실행 스크립트는 `code/engines/`, 출력 형식과 공식 프롬프트는 `FORMAT.md`에 있습니다.
