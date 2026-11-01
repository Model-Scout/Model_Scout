---
license: cc-by-4.0
language:
- ko
- ja
task_categories:
- image-to-text
tags:
- ocr
- document-parsing
- korean
- newspaper
- mdpbench
pretty_name: MDPBench Doc OCR SFT (KO/JP)
configs:
- config_name: ko
  data_files:
  - split: train
    path: ko/train-*.parquet
size_categories:
- 1K<n<10K
---

# mdpbench-doc-ocr-sft

Qwen 4B (Qwen3-VL) **MDPBench 한국어/일본어 문서 OCR/파싱** SFT 학습 데이터(공개 가능분).
재현 코드: https://github.com/sionic-ai/qwen-mdpbench-ocr

## Configs
| config | rows | 내용 | 상태 |
|---|---|---|---|
| `ko` | 2,407 | 한국 지자체 소식지(신문형) 이미지 + Markdown GT | 공개 |
| `jp` | — | 일본어 (추후) | 예정 |

## 스키마
- `image` (Image, bytes 임베드) — 문서 페이지
- `markdown` (string) — GT 전사(Markdown, 표/읽기순서 보존)
- `source` (string) — `snvision` / `seocho` / `gongju`
- `lang` (string) — `ko`
- `doc_type` (string) — `newspaper`

## 출처 & 라이선스
- 한국 지자체 소식지(성남 비전성남 / 서초구 / 공주시) — **공공저작물**(저작권법 24조의2), 비상업·연구 활용. PDF → 250DPI 렌더.
- GT 라벨 = 2-teacher 합의(PaddleOCR-VL-1.6 + Qwen3.5-9B 구조/순서) + 원본 PDF 텍스트레이어 내용검증 + bigram 게이트.
- **포함 안 함**: KICE 기출(저작권), MDPBench 테스트셋(공식 저자 배포본), 출처 미확인 PDF, 합성 데이터(코드로 재생성 가능).

## 무오염
MDPBench 테스트셋과 0 교집합 검증된 학습 데이터.

## 사용 예
```python
from datasets import load_dataset
ds = load_dataset("sionic-ai/mdpbench-doc-ocr-sft", "ko", split="train")
print(ds[0]["markdown"][:200]); ds[0]["image"]
```
