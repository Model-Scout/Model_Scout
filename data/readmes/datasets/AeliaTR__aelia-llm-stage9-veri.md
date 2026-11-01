---
language:
- tr
- en
- de
- fr
- es
- it
- ru
- ar
- zh
- ja
- ko
- pt
license: apache-2.0
task_categories:
- text-generation
- question-answering
tags:
- llm
- agent
- tool-calling
- chain-of-thought
- cumulative
pretty_name: Aelia LLM Stage 9 kumulatif Stage 8 + Milyoner
---

# Aelia LLM Stage 9 - KUMULATIF egitim havuzu

**Kural: veri SILINMEZ, uzerine EKLENIR.** Stage 8 ajan havuzunun TAMAMI
(15000 satir) korunur; uzerine Milyoner transkriptlerinden cikarilan
**soru-cevap + <think>** satirlari (2736: 0 QA/belirsizlik +
2121 diyalog) eklenir.

| alan | deger |
|---|---|
| toplam satir | **17736** |
| Stage 8 (korunan) | 15000 |
| yeni Milyoner QA | 0 |
| yeni Milyoner sohbet | 2121 |
| yeni Milyoner ozet (<think>) | 615 |
| GRPO (korunan) | 2000 |
| dil | 12 |

## Kategori dagilimi

| kategori | satir |
|---|---|
| `tool` | 9000 |
| `sohbet` | 3621 |
| `rag` | 2250 |
| `kimlik` | 1500 |
| `replay` | 750 |
| `ozet` | 615 |

## Dil dagilimi (yeni QA)

| dil | satir |
|---|---|
| `tr` | 0 |
| `en` | 0 |
| `de` | 0 |
| `fr` | 0 |
| `es` | 0 |
| `it` | 0 |
| `ru` | 0 |
| `ar` | 0 |
| `zh` | 0 |
| `ja` | 0 |
| `ko` | 0 |
| `pt` | 0 |

## Dosyalar

* `STAGE_9_LLM_MASTER.jsonl` - Stage 8 (15.000) + Milyoner sohbet + ozet (yeni)
* `STAGE_9_GRPO_VERI.jsonl` - Stage 8 GRPO (aynen)
* `STAGE_9_MILYONER_SOHBET.jsonl` - yalnizca yeni diyalog satirlari
* `STAGE_9_MILYONER_OZET.jsonl` - yalnizca yeni ozet + `<think>` satirlari

> **QA notu (olculdu):** Milyoner altyazilarinda soru metinleri var (337 satir)
> ama **secenekler ve aciklanan cevaplar ekranda** oldugu icin transkriptte
> gorunmuyor; dogrulanabilir QA cikarilamadi (0 satir). Uydurma soru-cevap
> yazmak yerine havuz, gercek diyalog + cikarimsal ozet ile genisletildi.

## Yeni satir semasi

```json
{"id": "s9-mily-tr-0001", "dil": "tr", "kategori": "mantik",
 "kaynak": "milyoner", "kaynak_tur": "qa", "kaynak_video": "<youtube-id>",
 "system": "...", "tools": [],
 "messages": [{"role": "user", "content": "Soru: ...\nA) ...\nB) ..."},
              {"role": "assistant", "content": "<think>...</think>\n\nCevap: B) ..."}],
 "cevap": "B", "secenek": {"A": "...", "B": "..."},
 "sentetik_mantik": true, "cok_adimli": false, "arac": null}
```

### Durustluk notu

* Cevap **yalnizca programda aciklanan** cevaptan alinir (transkriptte
  "dogru cevap / final answer / richtige Antwort / الإجابة الصحيحة / 正解 ..."
  isareti + harf). Cevabi aciklanmayan soru havuza GIRMEZ.
* `<think>` blogu, secenek listesi ve aciklanan harften **deterministik**
  uretilir (`sentetik_mantik: true`): amac format/akil yurutme iskeletini
  ogrenmek; metin kaynaktan alinmaz, uydurma bilgi eklenmez.

## Kaynaklar ve lisans

* Stage 8 ajan havuzu - AeliaTR (Apache-2.0).
* Milyoner transkriptleri - YouTube otomatik altyazilar; telif yayincilara
  aittir, yalnizca arastirma/egitim amaciyla kullanilir.
