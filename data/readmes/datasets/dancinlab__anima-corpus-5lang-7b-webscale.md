---
license: odc-by
language:
- en
- fr
- de
- es
- ko
pretty_name: anima 5-lang 7B web-scale corpus (R2-staged pointer index)
tags:
- byte-level
- web-scale
- fineweb
- multilingual
- r2-staged
size_categories:
- 100B<n<1T
---

# anima-corpus-5lang-7b-webscale

> **⚠️ R2-STAGED, NOT HF-HOSTED.** The **143.60 GiB** of raw byte-corpus lives **only in
> Cloudflare R2** (bucket `phanes`, prefix `anima-7b/web/`) — an egress-free durable staging
> store. **This HF dataset holds the manifest + card + 200 KB per-language sample heads, NOT
> the 143 GB.** The full corpus is **fetched from R2** for training; it is not HF-mirrored and
> not held locally.

The **web-scale 7B-Chinchilla-optimal** extension of the anima default-lane corpus. Byte-level
(V = 256), 5-language balanced (en / fr / de / es / ko), web-derived under **ODC-BY**.

| metric | value |
|---|---|
| total byte-corpus | **143.60 GiB** (154.19 GB decimal) |
| tokens / param (7B) | **22.0 tok/param** (Chinchilla-optimal 20 → **EXCEEDS**) |
| fraction of 7B-optimal | **110.1%** of the 140B-token budget |
| byte vocabulary | **V = 256** |
| shards | 20 |
| license | **ODC-BY** (web-derived) |

## Per-language / per-source

| lang | GB (decimal) | source (ODC-BY) |
|---|---:|---|
| en | 25.83 | `HuggingFaceFW/fineweb` sample/10BT |
| fr | 32.79 | `HuggingFaceFW/fineweb-2` fra_Latn |
| de | 31.00 | `HuggingFaceFW/fineweb-2` deu_Latn |
| es | 32.94 | `HuggingFaceFW/fineweb-2` spa_Latn |
| ko | 31.64 | `HuggingFaceFW/fineweb-2` kor_Hang |
| **total** | **154.19** | — |

**Korean web bulk is INCLUDED** (≈ 31.64 GB) — this fixes the prior clean-license build's
Korean gap (Project Gutenberg has no Korean, so the earlier `gb-balanced` corpus had ko art /
consciousness = 0 and leaned wiki-only).

## License & hygiene

- **ODC-BY**, Common-Crawl-derived FineWeb / FineWeb-2. Attribution per ODC-BY.
- **PII-scrubbed**: `email → [EMAIL]`, `phone → [PHONE]` (these tokens are the scrub markers
  and are expected in the text). **Control bytes 0xFE / 0xFF stripped** (V = 256).
- **No persona / role injection.** anima's persona + identity voice stay **authored**
  elsewhere; this is the web factual/linguistic base only.

## How to fetch from R2

`MANIFEST.json` carries the per-shard R2 keys + bytes + sha256. Stream each shard from R2
(`https://<account>.r2.cloudflarestorage.com`, region `auto`, bucket `phanes`) with boto3 and
verify against the per-shard sha256. See `CORPUS_CARD.md` for the full code snippet.

## Scope (honest)

This is the **CORPUS** — an R2-staged pointer index. The actual **7B train is a separate
follow-on GPU fire**; **no 7B-trained-model is claimed** here. Numbers (143.60 GiB / 22.0
tok/param / 110.1% / per-lang) are the achieved corpus values verified against the R2 manifest
byte counts.

See `CORPUS_CARD.md` for the full card.
