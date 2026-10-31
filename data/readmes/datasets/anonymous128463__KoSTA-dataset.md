---
license: cc-by-nc-4.0
language:
- ko
task_categories:
- image-to-image
tags:
- scene-text-editing
- korean
- pii
- ocr
- benchmark
size_categories:
- n<1K
---

# KoSTA-bench

한국어 PII(개인정보) 장면 텍스트 편집(Scene Text Editing) 벤치마크. 원본·타깃 텍스트를 모두 가상 PII 키워드로 구성한 611개 (원본, 타깃) 이미지 쌍으로 이루어진다.

## 구성

- `source/{name}` — 원본 텍스트(`text_s`)가 담긴 원본 이미지 crop
- `target/{name}` — 타깃 텍스트(`text_t`)로 편집된 타깃 이미지 crop
- `manifest.jsonl` — 샘플별 메타데이터 (한 줄당 한 샘플)

### manifest 필드

| 필드 | 설명 |
| --- | --- |
| name | 샘플 파일명 (`source/`, `target/` 공통) |
| text_s | 원본 텍스트 |
| text_t | 타깃 텍스트 |
| label | PII 유형 라벨 |

예시:

```json
{"name": "000000.png", "text_s": "원수", "text_t": "과장", "label": "cv_position"}
```

## 통계

10개 카테고리 21종 유형, 611쌍(원본·타깃 합 1,222장). 모든 샘플은 PaddleOCR PP-OCRv5 완전일치(strict-pass) 검증과 전문가 3인 중 2인 이상의 인간 검수를 통과했다.

## 로딩 예시

```python
import json
from huggingface_hub import snapshot_download

root = snapshot_download("<your-username>/KoSTA-bench", repo_type="dataset")
rows = [json.loads(l) for l in open(f"{root}/manifest.jsonl")]

r = rows[0]
src_path = f"{root}/source/{r['name']}"   # 원본 이미지
tgt_path = f"{root}/target/{r['name']}"   # 타깃 이미지
```

## 라이선스 및 개인정보

원본·타깃 텍스트는 모두 가상 PII 키워드이며 실제 개인정보를 포함하지 않는다. `license` 필드는 실제 배포 근거에 맞게 수정하여 사용한다.
