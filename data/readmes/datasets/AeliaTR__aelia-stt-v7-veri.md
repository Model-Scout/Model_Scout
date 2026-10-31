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
license: cc-by-nc-4.0
task_categories:
- automatic-speech-recognition
tags:
- speech
- whisper
- lora
- turkish
- multilingual
- cumulative
pretty_name: Aelia STT v7 kumulatif Lingo + CV17 + FLEURS + Milyoner
size_categories:
- 10K<n<100K
---

# Aelia STT v7 - KUMULATIF egitim havuzu (12 dil)

**Kural: veri SILINMEZ, uzerine EKLENIR.** Bu depo v6 havuzunun TAMAMINI
(31368 satir) ve yeni **Kim Milyoner Olmak Is(ter)** (Who Wants to Be a
Millionaire) segmentlerini (2478 satir) birlikte tutar.

| alan | deger |
|---|---|
| toplam satir | **33846** |
| toplam ses | **70.18 saat** |
| v6 (Lingo+CV17+FLEURS) | 31368 |
| yeni (Milyoner) | 2478 |
| dil | 12 |

## Kaynak dagilimi

| `common_voice_17_0` | 7937 |
| `fleurs` | 15561 |
| `lingo` | 7870 |
| `milyoner` | 2478 |

## Dil dagilimi

| dil | satir |
|---|---|
| `ar` | 3059 |
| `de` | 2713 |
| `en` | 2733 |
| `es` | 2696 |
| `fr` | 2690 |
| `it` | 2637 |
| `ja` | 2661 |
| `ko` | 2876 |
| `pt` | 2778 |
| `ru` | 2726 |
| `tr` | 2717 |
| `zh` | 3560 |

## Dosya semasi

    ses/<dil>_pN.i16       v6 paketleri (16 kHz mono int16)
    ses/<dil>_mN.i16       Milyoner paketleri (ayni format)
    index.json             {"<dil>/<md5-12>": ["<paket>", <offset>, <ornek>]}
    veri/STT_MASTER_TEMIZ.jsonl          tum satirlar
    veri/STT_MASTER_TEMIZ_EGITIM.jsonl   egitim kopyasi (ayni birlesim)
    veri/STT_ALTIN_SET.jsonl             v6 altin set (WER icin DEGISMEDI)

Satir ornegi:

```json
{"ses_yolu": "tr/1f2e3d4c5b6a", "kaynak_ses": "v7m://<video>#12",
 "metin": "Hangisi ... degildir?", "dil": "tr", "kaynak": "milyoner",
 "bas": 84.6, "son": 103.4, "kaynak_vtt": "otomatik"}
```

## Kullanim

```python
import json, numpy as np
idx = json.load(open("index.json"))
paket, ofs, n = idx["tr/1f2e3d4c5b6a"]
pcm = np.fromfile("ses/%s" % paket, dtype="<i2", count=n, offset=ofs)
ses = pcm.astype("float32") / 32768.0      # 16 kHz mono
```

## Kaynaklar ve lisans

* **Lingo** (yerel derlem) - AeliaTR ic kullanim.
* **Common Voice 17.0** (`fixie-ai/common_voice_17_0`) - CC0-1.0.
* **FLEURS** (`google/fleurs`) - CC-BY-4.0.
* **Milyoner** - YouTube yayinlarindan yalnizca arastirma/egitim amaciyla
  alinan ses + otomatik altyazi; telif yayincilara aittir, ticari dagitim
  yapilmaz.

## Surum notu

* v6: 31.368 satir (12 dil, Lingo+CV17+FLEURS).
* **v7 (bu depo):** v6 + Milyoner = 33846 satir. Altin set **degismedi**,
  boylece v6/v7 WER olcumleri ayni kume uzerinde kiyaslanabilir.
