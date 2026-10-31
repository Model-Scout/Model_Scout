---
task_categories:
- image-to-text
language:
- ko
tags:
- ocr
- waybill
- robotics
- indory
- synthetic
license: other
---

# indory_waybill_ocr_640x480

Indory waybill OCR benchmark dataset.

This dataset contains resized waybill images and destination labels used to
evaluate the `control-server-detection` `/v1/waybill/scan` API. The service's
internal Python package is still named `indory_ocr` for compatibility, but the
public repository name is `control-server-detection`. The benchmark target is
the delivery destination room/floor decision, not generic full-document OCR.

## Data Provenance and Privacy

All waybill images in this export are generated/synthetic benchmark images.
They do not contain real customer names, real phone numbers, real addresses,
real tracking numbers, service credentials, private network details, or robot
runtime logs. Any waybill-style identifiers visible in the images are synthetic
test text for OCR evaluation.

## Files

- `images/test/`: benchmark images
- `metadata.jsonl`: Hugging Face imagefolder metadata
- `manifest.json`: manifest consumed by `python3 benchmark/run.py`
- `dataset_summary.json`: export counts and source manifest metadata
- `checksums.sha256`: file integrity checksums

## Current Export

- Samples: 187
- Ground-truth samples: 187
- Split: `test`
- Image size: 640x480 resized synthetic benchmark snapshot

Review the dataset license before reusing or redistributing the images.
