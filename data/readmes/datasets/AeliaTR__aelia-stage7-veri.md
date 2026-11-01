---
language: [tr, en, de, fr, es, it, pt, ru, ar, zh, ja, ko]
license: apache-2.0
task_categories: [text-generation]
tags: [aelia, turkish, multilingual, sft, dpo]
---

# AELIA · Stage 7 veri seti (12 dil)

**AELIA Soveria 1.0** için Stage 7 (12 dilli sohbet) eğitim verisi.

| Dosya | Satır | İçerik |
|---|---|---|
| `STAGE_7_LLM_MASTER.jsonl` | 4324 | SFT master: Stage 7 + 780 Stage 6 replay + 407 kimlik |
| `STAGE_7_DPO_PAIRS.jsonl` | 762 | DPO çiftleri (`prompt` / `chosen` / `rejected`) |
| `STAGE_7_LLM_MASTER.manifest.json` | — | sayımlar, oranlar, sha256 |

## Biçim (`STAGE_7_LLM_MASTER.jsonl`)

```json
{"id": "s7-it-000160", "dil": "it", "kategori": "gunluk", "konu": "...",
 "system": "You must respond ONLY in the language of the user's prompt...",
 "kaynak_tur": "sft|replay|kimlik", "kaynak": "aelia_asama7_12dil_sohbet.jsonl",
 "messages": [{"role": "user", "content": "..."},
              {"role": "assistant", "content": "..."}]}
```

- `kaynak_tur`: `sft` (Stage 7), `replay` (Stage 6 turundan %20 — unutma önleyici),
  `kimlik` (kanonik kimlik Q&A, Türkçe).
- Replay içeriği (Stage 6 dosyası saf kod değil): sohbet 465, hata 131, kod 110, sinir 74
- DPO kayıtları SFT'ye karıştırılmadı (aynı cevap iki kez eğitilmesin).
- Replay/Stage 7 oranı: 0.2001 (hedef 0,20).

## Colab'de kullanım

```python
import os
from google.colab import userdata
os.environ["HF_TOKEN"] = userdata.get("HF_TOKEN")     # Colab Secrets

from huggingface_hub import hf_hub_download
yol = hf_hub_download("AeliaTR/aelia-stage7-veri", "STAGE_7_LLM_MASTER.jsonl",
                      repo_type="dataset", token=os.environ["HF_TOKEN"])
```

Tam eğitim defteri: `colab_llm_stage7.ipynb` (Qwen3-4B · QLoRA r=32 · erken durdurma).
