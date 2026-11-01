---
license: cc-by-4.0
task_categories:
  - document-question-answering
  - visual-question-answering
language:
  - ko
tags:
  - ocr
  - document-understanding
  - embeddings
  - korean
size_categories:
  - 10K<n<100K
---

# SDS-KoPub OCR Results & Embeddings

OCR layout parsing results and VL embeddings for the
[SDS-KoPub-VDR-Benchmark](https://huggingface.co/datasets/SamsungSDS-Research/SDS-KoPub-VDR-Benchmark)
corpus (64 Korean public document pages).

## Contents

| File | Description | Size |
|------|-------------|------|
| `ocr_results.jsonl` | GLM-OCR structured layout results (regions, markdown, bbox, labels) | 64 records |
| `parsed_texts.jsonl` | Extracted text per page (embedding input) | 64 records |
| `embeddings/corpus_images.npy` | Page image embeddings | (64, 2048) |
| `embeddings/corpus_ocr_text.npy` | OCR text embeddings | (64, 2048) |
| `embeddings/queries.npy` | Query embeddings | (600, 2048) |
| `crops.tar.gz` | Image/chart region crops | 18 images |

## Models Used

- **OCR**: [GLM-OCR](https://huggingface.co/zai-org/GLM-OCR) (0.9B, layout via PP-DocLayoutV3)
- **Embeddings**: [Qwen3-VL-Embedding-2B-FP8](https://huggingface.co/Qwen/Qwen3-VL-Embedding-2B-FP8) (2048-dim)

## OCR Result Format

Each line in `ocr_results.jsonl`:
```json
{
  "page_id": "doc_123_page_0",
  "page_idx": 0,
  "regions": [
    {"index": 0, "label": "doc_title", "bbox_2d": [x1, y1, x2, y2], "content": "..."},
    {"index": 1, "label": "table", "bbox_2d": [...], "content": "<table>...</table>"},
    {"index": 2, "label": "image", "bbox_2d": [...], "content": null}
  ],
  "markdown": "# Title\n\n| col1 | col2 |\n...",
  "image_crops": [{"path": "crops/doc_123_page_0_crop_2.jpg", "bbox": [...], "label": "image"}]
}
```

## Usage

```python
import json
import numpy as np
from huggingface_hub import hf_hub_download

# Load OCR results
path = hf_hub_download("Forturne/sds-kopub-ocr-test", "ocr_results.jsonl", repo_type="dataset")
with open(path) as f:
    records = [json.loads(line) for line in f]

# Load embeddings
img_emb = np.load(hf_hub_download("Forturne/sds-kopub-ocr-test", "embeddings/corpus_images.npy", repo_type="dataset"))
txt_emb = np.load(hf_hub_download("Forturne/sds-kopub-ocr-test", "embeddings/corpus_ocr_text.npy", repo_type="dataset"))
q_emb = np.load(hf_hub_download("Forturne/sds-kopub-ocr-test", "embeddings/queries.npy", repo_type="dataset"))

# Retrieval: cosine similarity (embeddings are L2-normalized)
scores = q_emb @ img_emb.T  # (num_queries, num_pages)
```

## Pipeline

Generated with `run_b200_pipeline.py` on NVIDIA B200 (192GB).
