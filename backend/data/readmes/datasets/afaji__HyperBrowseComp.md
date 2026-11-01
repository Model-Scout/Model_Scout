---
pretty_name: HyperBrowseComp
license: cc-by-sa-4.0
tags:
- benchmark
- encrypted
extra_gated_heading: HyperBrowseComp benchmark access
extra_gated_prompt: >-
  HyperBrowseComp is a held-out evaluation benchmark. To preserve the value of
  future evaluations, the authors ask users not to use its questions or answers
  for model training, fine-tuning, or distillation. This is a research practice
  request, not an additional restriction on the CC BY-SA 4.0 license.
extra_gated_fields:
  "I acknowledge the authors' request not to train, fine-tune, or distill models on HyperBrowseComp questions or answers": checkbox
language:
- ko
- de
- jv
- id
- es
- ru
- zh
- te
- arz
- uz
- th
- fil
- vi
configs:
- config_name: default
  data_files:
  - split: test
    path: data/hyperbrowsecomp_retained_423_encrypted.parquet
dataset_info:
  features:
  - name: id
    dtype: string
  - name: canary
    dtype: string
  - name: question
    dtype: string
  - name: answer
    dtype: string
  splits:
  - name: test
    num_bytes: 344660
    num_examples: 423
  download_size: 346991
  dataset_size: 344660
---

# HyperBrowseComp

HyperBrowseComp is a multilingual and multimodal stress test for web-browsing
agents. The paper's filtered benchmark contains 423 manually authored and
human-validated questions across 13 languages. Each question has a short,
publicly verifiable answer, but finding it can require following several clues
across obscure webpages, videos, scanned documents, images, or maps. The
benchmark tests whether agents can persistently find and connect evidence on
the open web.

[Project website](https://hyperbrowsecomp.github.io/) ·
[Paper](https://arxiv.org/abs/2610.03574) ·
[Code](https://github.com/HyperBrowseComp/HyperBrowseComp)

## Dataset

The `test` split is the paper's **423-question release**, stored in
[`data/hyperbrowsecomp_retained_423_encrypted.parquet`](https://huggingface.co/datasets/afaji/HyperBrowseComp/blob/main/data/hyperbrowsecomp_retained_423_encrypted.parquet).
Its columns are `id`, `canary`, `question`, and `answer`. The question and answer
fields are encrypted with AES-256-GCM; `canary` is used to derive each field's
nonce. IDs have the form `<LANG>_<question id>`, such as `KO_7388`.

## License and benchmark integrity

HyperBrowseComp is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
To help keep the benchmark useful for evaluation, the authors ask users not to
train, fine-tune, or distill models on its questions or answers. This request does
not alter the permissions granted by the license.

## Load and decrypt

Accept the dataset's access conditions and log in to Hugging Face before
downloading. The `test` split loads the paper's 423 questions. The decryption
key is included in the final line:

```python
import base64
import hashlib

from datasets import load_dataset
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


ds = load_dataset("afaji/HyperBrowseComp", split="test")


def _nonce(canary, field):
    return hashlib.sha256(f"{canary}:{field}".encode()).digest()[:12]


def _open(ciphertext_b64, key, canary, field):
    return AESGCM(key).decrypt(_nonce(canary, field), base64.b64decode(ciphertext_b64), None).decode()


def decrypt_row(row, master_key):
    key = bytes.fromhex(master_key)
    return {
        "id": row["id"],
        "question": _open(row["question"], key, row["canary"], "question"),
        "answer": _open(row["answer"], key, row["canary"], "answer"),
    }


decrypt_row(ds[0], "2a8633906fda29da5f696452a1e58f00fcb1edbb3b9c231783f3c1acf80021cb")
```
