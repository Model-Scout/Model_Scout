---
license: cc0-1.0
task_categories:
- image-to-text
language:
- ko
tags:
- ocr
- korean
- gwanbo
- gazette
- digital-typesetting
- myeongjo
pretty_name: Gwanbo Digital Re-render (1994-2000 PETY)
---

# Gwanbo Digital Re-render (관보 디지털 재렌더)

대한민국 관보(官報) 1994–2000 PETY 스캔본을 **인식+재렌더(recognition + re-render)**
파이프라인으로 디지털 본 품질로 재조판한 데이터셋.

## 생성 방식

```
스캔 PDF(250dpi) → Chandra OCR-2 → Qwen3.6-27B 후처리(마크다운)
  → fontsr.render_digital:
       · gwanbo_ocr_error_patterns.json 오류패턴 교정(애급→예금, 소재→소계, 조홍→조흥 …)
       · 내용 기반 컬럼폭 표 레이아웃
       · UnBatang(은바탕 = 한양 신명조 계보, HWP 3.0~2000 기본 본문 글꼴) 렌더
```

스캔 글리프를 *복원*하는 SR과 달리, 인식된 텍스트를 **깨끗한 명조 폰트로 재조판**해
'디지털 본에 준하는' 완벽한 글리프를 생성한다. OCR 혼동 오류까지 교정된 버전이다.

## 구성

- `<doc_id>/page_XXXX_digital.png` — 페이지별 디지털 재렌더(그레이스케일 PNG)
- confidence ≥ 0.85 (오류패턴 기반 신뢰도 필터) 페이지만 포함

## 한계

- full-page OCR엔 좌표가 없어 **원본의 정확한 레이아웃/병합셀은 근사**(마크다운 표 → 균등/내용기반 그리드).
- 품질은 상위 OCR(Chandra/Qwen) 정확도에 의존. 원본 진본성이 필요하면 스캔 원본/SR본을 사용.

## 출처

- 원자료: 전자관보(공공) — 관보는 공개 자료.
- 코드: `fontsr/` (yakdoli/nemotron-ocr-v2), `gwanbo_ocr_error_patterns.json`.
