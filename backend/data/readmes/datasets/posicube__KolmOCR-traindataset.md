---
license: odc-by
language:
- ko
tags:
- ocr
- document-understanding
- layout-analysis
- pdf-rendering
size_categories:
- 10K<n<100K
task_categories:
- image-to-text
- text-generation
---

# KolmOCR Training Dataset

## 데이터셋 개요

KolmOCR Training Dataset은 [allenai/olmOCR-mix-1025](https://huggingface.co/datasets/allenai/olmOCR-mix-1025) 데이터셋을 일부를 한국어로 번역하고, 다단계 파이프라인을 통해 PDF 및 PNG 렌더링을 활용하여 만들어진 markdown 생성 모델 학습용 데이터셋입니다.

이 데이터셋은 원본 문서의 레이아웃과 비슷한 고품질 PDF와 이미지를 생성하였으며, 각 샘플에는 구조화된 JSON 메타데이터와 bounding box 정보가 포함된 markdown 문서가 포함합니다.

## 처리 파이프라인

번역된 Markdown 텍스트는 다음 3단계 파이프라인을 통해 처리되었습니다:

### STAGE 1: BuildDraftHTML
- Markdown을 블록 단위로 파싱하여 HTML로 변환
- 이미지 및 figure 삽입 처리

### STAGE 2: BuildCSS with VLM
1. **ApplyBlockwiseCSS**: 각 div 블록에 기본 스타일 적용
2. **TuneCSS4ValidDoc**: A4 크기 문서에 최적화된 CSS 생성
3. **ApplyTheme2CSS**: 블록 유형별로 분류하고 테마가 적용된 CSS 스타일링

### STAGE 3: HTMLRendering
- HTML을 PDF 및 PNG 형식으로 렌더링
- Bounding box 검증을 포함한 품질 검증 수행

## 데이터셋 구조

### Subsets
다음은 pdf-md 쌍의 수입니다.
| Subset | Train | Eval | Total | 원본 출처 |
|--------|-------|------|-------|-----------|
| 00_documents | 11,622 | 211 | 11,833 | 일반 문서 |
| 01_books | 244 | 13 | 257 | 도서 콘텐츠 |
| **Total** | **11,866** | **224** | **12,090** | |

### 파일 구조

각 샘플은 고유 ID로 구분된 디렉토리에 저장되며, 다음 파일들을 포함합니다:

```
processed_{subset}_{split}/
├── {hash_prefix}/
│   └── {sample_id}/
│       ├── {sample_id}.json        # 구조화된 메타데이터 및 블록 정보
│       ├── {sample_id}.pdf         # 렌더링된 PDF 문서
│       ├── {sample_id}.md          # 렌더링된 PDF 문서를 markdown으로 나타낸 문서
│       └── {sample_id}.png         # 렌더링된 PNG 이미지
```

**예시:**
```
processed_00_documents_train/4788/553a1148cdf35b53c0454de97ff301b647fc-3/
├── 553a1148cdf35b53c0454de97ff301b647fc-3.json
├── 553a1148cdf35b53c0454de97ff301b647fc-3.pdf
├── 553a1148cdf35b53c0454de97ff301b647fc-3.md
└── 553a1148cdf35b53c0454de97ff301b647fc-3.png
```

### Markdown 파일
- 렌더링된 PDF 문서를 markdown으로 나타낸 문서로써, 각 markdown 문서상의 이미지들은 각 문서별 폴더의 images 아래 있습니다. 
- 각 markdown의 block의 위치는 하기의 [Bounding Box 형식](#Bounding-Box-형식)와 같이 markdown comment로 표현 되었습니다.

### JSON 메타데이터 형식

각 `.json` 파일은 문서를 구조화된 블록 배열로 표현합니다:

```json
[
  {
    "id": "front_matter",
    "type": "front_matter",
    "markdown": "primary_language: en\nis_rotation_valid: True\n...",
    "metadata": {
      "primary_language": "en",
      "is_rotation_valid": true,
      "rotation_correction": 0,
      "is_table": false,
      "is_diagram": false
    }
  },
  {
    "id": "b001_1",
    "type": "text",
    "content": "텍스트 내용...",
    "markdown": "마크다운 형식 텍스트...",
    "bbox": [x1, y1, x2, y2],
    "text": "텍스트 내용..."
  },
  {
    "id": "b002",
    "type": "text",
    "content": "\\[ 수식 내용 \\]",
    "display_mode": true,
    "bbox": [x1, y1, x2, y2],
    "page": 1
  },
  {
    "id": "b003_1",
    "type": "figure",
    "markdown": "",
    "src": "images/example.png",
    "alt": "이미지 설명",
    "bbox": [x1, y1, x2, y2],
    "text": "",
    "content": ""
  }
]
```

### 블록 타입

- `front_matter`: 문서 메타데이터 (언어(원 데이터의 언어), 회전, 테이블/다이어그램 포함 여부)
- `text`: 일반 텍스트 블록 (수식 포함 가능)
- `figure`: 이미지 또는 다이어그램
- 기타: 원본 데이터의 구조에 따라 추가 타입 존재 가능

### Bounding Box 형식

모든 bounding box는 1000x1000으로 정규화된 `[x1, y1, x2, y2]` 형식으로 표현됩니다:
- `(x1, y1)`: 좌상단 좌표
- `(x2, y2)`: 우하단 좌표
- 좌표는 픽셀 단위

## 데이터셋 다운로드

이 데이터셋은 JSON, PDF, PNG, Markdown 파일로 구성된 원본 파일들을 제공합니다. HuggingFace Hub 라이브러리를 사용하여 필요한 부분만 선택적으로 다운로드할 수 있습니다.

### 방법 1: 특정 subset만 다운로드 (권장)

```python
from huggingface_hub import snapshot_download

# Documents subset만 다운로드
documents_path = snapshot_download(
    repo_id="posicube/KolmOCR-traindataset",
    repo_type="dataset",
    allow_patterns=["processed_00_documents_*/**/*"]
)
print(f"Documents downloaded to: {documents_path}")

# Books subset만 다운로드
books_path = snapshot_download(
    repo_id="posicube/KolmOCR-traindataset",
    repo_type="dataset",
    allow_patterns=["processed_01_books_*/**/*"]
)
print(f"Books downloaded to: {books_path}")

# Train split만 다운로드
train_path = snapshot_download(
    repo_id="posicube/KolmOCR-traindataset",
    repo_type="dataset",
    allow_patterns=["*_train/**/*"]
)
```

### 방법 2: 전체 데이터셋 다운로드

```python
from huggingface_hub import snapshot_download

# 전체 데이터셋 다운로드 (약 12,000개 샘플)
dataset_path = snapshot_download(
    repo_id="posicube/KolmOCR-traindataset",
    repo_type="dataset"
)
print(f"Dataset downloaded to: {dataset_path}")
```

### 방법 3: 개별 파일 다운로드

소량의 샘플만 필요한 경우 개별 파일을 다운로드할 수 있습니다:

```python
from huggingface_hub import hf_hub_download

# 특정 샘플의 JSON 메타데이터 다운로드
json_path = hf_hub_download(
    repo_id="posicube/KolmOCR-traindataset",
    filename="processed_00_documents_train/4788/553a1148cdf35b53c0454de97ff301b647fc-3/553a1148cdf35b53c0454de97ff301b647fc-3.json",
    repo_type="dataset"
)

# 해당 샘플의 PDF 다운로드
pdf_path = hf_hub_download(
    repo_id="posicube/KolmOCR-traindataset",
    filename="processed_00_documents_train/4788/553a1148cdf35b53c0454de97ff301b647fc-3/553a1148cdf35b53c0454de97ff301b647fc-3.pdf",
    repo_type="dataset"
)
```

## 사용 예시

### Python으로 데이터 사용하기

다운로드한 데이터셋을 Python으로 로드하는 예시입니다:

```python
import json
from pathlib import Path
from PIL import Image

# 데이터셋 경로 (다운로드한 경로로 변경)
dataset_root = Path("KolmOCR-traindataset")  # 또는 snapshot_download()의 반환값

# 모든 샘플 순회
for subset_dir in dataset_root.glob("processed_*"):
    print(f"Processing {subset_dir.name}...")

    for hash_dir in subset_dir.iterdir():
        if not hash_dir.is_dir():
            continue

        for sample_dir in hash_dir.iterdir():
            if not sample_dir.is_dir():
                continue

            sample_id = sample_dir.name

            # JSON 메타데이터 읽기
            json_path = sample_dir / f"{sample_id}.json"
            if json_path.exists():
                with open(json_path, 'r', encoding='utf-8') as f:
                    blocks = json.load(f)

                # Markdown 읽기
                md_path = sample_dir / f"{sample_id}.md"
                if md_path.exists():
                    with open(md_path, 'r', encoding='utf-8') as f:
                        markdown_content = f.read()

                # 이미지 로드
                png_path = sample_dir / f"{sample_id}.png"
                if png_path.exists():
                    image = Image.open(png_path)

                # PDF 경로
                pdf_path = sample_dir / f"{sample_id}.pdf"

                # 텍스트 블록 추출
                for block in blocks:
                    if block.get('type') == 'text' and 'bbox' in block:
                        print(f"ID: {block['id']}")
                        print(f"Content: {block.get('content', '')[:50]}...")
                        print(f"BBox: {block['bbox']}")

                break  # 예시를 위해 첫 샘플만 처리
        break
    break
```

### 특정 subset만 로드하기

```python
from pathlib import Path
import json

def load_subset(dataset_root, subset_name, split="train"):
    """
    특정 subset의 데이터 로드

    Args:
        dataset_root: 데이터셋 루트 경로
        subset_name: "00_documents" 또는 "01_books"
        split: "train" 또는 "eval"

    Returns:
        샘플 리스트
    """
    subset_dir = Path(dataset_root) / f"processed_{subset_name}_{split}"
    samples = []

    for hash_dir in subset_dir.iterdir():
        if not hash_dir.is_dir():
            continue

        for sample_dir in hash_dir.iterdir():
            if not sample_dir.is_dir():
                continue

            sample_id = sample_dir.name
            json_path = sample_dir / f"{sample_id}.json"

            if json_path.exists():
                with open(json_path, 'r', encoding='utf-8') as f:
                    samples.append({
                        'id': sample_id,
                        'json_path': json_path,
                        'md_path': sample_dir / f"{sample_id}.md",
                        'pdf_path': sample_dir / f"{sample_id}.pdf",
                        'png_path': sample_dir / f"{sample_id}.png",
                        'metadata': json.load(f)
                    })

    return samples

# 사용 예시
dataset_root = "KolmOCR-traindataset"
documents_train = load_subset(dataset_root, "00_documents", "train")
books_train = load_subset(dataset_root, "01_books", "train")

print(f"Documents train samples: {len(documents_train)}")
print(f"Books train samples: {len(books_train)}")
```

## 원본 데이터셋 정보

이 데이터셋은 [allenai/olmOCR-mix-1025](https://huggingface.co/datasets/allenai/olmOCR-mix-1025)의 한국어 번역 버전을 기반으로 합니다.

원본 데이터셋 특징:
- **총 270,000개 PDF 페이지**를 GPT-4o로 OCR 처리
- 일관된 수식 형식 (`\[`, `\]` for display math, `\(`, `\)` for inline math)
- HTML 형식의 테이블
- 이미지에 대한 기본 alt 텍스트
- 손글씨 및 역사적 문서 포함

## 라이선스

이 데이터셋은 원본 데이터셋과 동일한 [ODC-BY (Open Data Commons Attribution)](https://opendatacommons.org/licenses/by/) 라이선스를 따릅니다.

## 인용

```bibtex
@misc{KolmOCR-traindataset,
  title={KolmOCR-traindataset},
  author={Posicube Inc.},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/posicube/KolmOCR-traindataset}}
}
```

이 데이터셋을 사용하는 경우, 아래의 원본 olmOCR-mix 데이터셋도 함께 인용해주세요:

```bibtex
@misc{olmocr-mix-1025,
  title={olmOCR-mix-1025},
  author={Allen Institute for AI},
  year={2025},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/datasets/allenai/olmOCR-mix-1025}}
}
```

## 관련 리소스

- 원본 데이터셋: [allenai/olmOCR-mix-1025](https://huggingface.co/datasets/allenai/olmOCR-mix-1025)
- olmOCR GitHub: [https://github.com/allenai/olmocr](https://github.com/allenai/olmocr)
- olmOCR Collection: [https://huggingface.co/collections/allenai/olmocr](https://huggingface.co/collections/allenai/olmocr)
- KolmOCR Github: [posicube-services/KolmOCR](https://github.com/posicube-services/KolmOCR)

## 연락처

데이터셋에 대한 문의사항이나 이슈가 있으시면 이슈를 등록해주세요.