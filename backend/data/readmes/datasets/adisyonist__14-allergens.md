---
dataset_info:
  features:
    - name: text
      dtype: string
    - name: allergens
      sequence: string
  config_name: default
  task_categories:
    - text-classification
language:
  - en
  - bn
  - ca
  - hr
  - cs
  - da
  - nl
  - fi
  - fr
  - de
  - el
  - gu
  - he
  - hi
  - hu
  - id
  - it
  - ja
  - kn
  - ko
  - ms
  - ml
  - mr
  - nb
  - or
  - pl
  - pt
  - pa
  - ro
  - ru
  - sk
  - sl
  - es
  - sv
  - ta
  - te
  - th
  - tr
  - uk
  - ur
  - vi
language_bcp47:
  - zh-CN
  - zh-TW
---

# 14-Allergens Food and Menu Dataset

This release contains 131,825 JSONL records: the existing `14-allergens` data combined with the additional `sofra.jsonl` and `ek.jsonl` records.

## Türkçe

Bu veri kümesi, yiyecek ve menü metinleriyle bunlara bağlı alerjen etiketlerini içerir. Veriler; fikir vermek, prototip oluşturmayı ve veri/uygulama geliştirme görevlerini kolaylaştırmak amacıyla sunulmuştur.

Bu sürüm, mevcut `14-allergens` verisine `sofra.jsonl` ve `ek.jsonl` kayıtlarının eklenmesiyle oluşturulmuştur (toplam 131.825 kayıt).

Kayıt satırları konsept veya kaynak bloklarına göre sıralı değildir; karışık sırada sunulmuştur.

Verilerde hatalar, eksik bilgiler veya tarif/üretim yöntemine bağlı farklılıklar bulunabilir. Alerjen bilgileri tıbbi tavsiye değildir; gıda güvenliği, restoran servisi veya sağlık kararlarında tek başına kullanılmamalıdır. Gerçek kullanım öncesinde içerikler ve çapraz bulaşma bilgileri yetkin kişilerce doğrulanmalıdır.

Kayıt şeması:

```json
{"text":"Türk Yoğurtlu Türk Döneri - döner eti, yoğurt, domates, soğan, lavaş","allergens":["gluten","milk"]}
```

## English

This dataset contains food and menu text paired with corresponding allergen labels. It is provided for ideation, prototyping, and making data/application development tasks easier.

This release combines the existing `14-allergens` data with additional `sofra.jsonl` and `ek.jsonl` records (131,825 records total).

Record rows are intentionally shuffled rather than grouped by concept or source block.

The data may contain errors, omissions, or recipe and preparation-method differences. Allergen information is not medical advice and must not be used alone for food-safety, restaurant-service, or health decisions. Before real-world use, ingredients and cross-contact information should be verified by qualified professionals.

Record schema:

```json
{"text":"Turkish Yogurt Döner - döner meat, yogurt, tomatoes, onions, flatbread","allergens":["gluten","milk"]}
```

The allergen vocabulary follows the 14-allergen convention used in this release: celery, crustaceans, eggs, fish, gluten, lupin, milk, mollusks, mustard, nuts, peanuts, sesame, soy, and sulfites.
