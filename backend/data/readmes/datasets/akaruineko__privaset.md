---
license: mit
language:
- zh
- ar
- hi
- en
- es
- bn
- pt
- ru
- ja
- de
- ko
- fr
- jv
- te
- mr
- vi
- ta
- it
- tr
- ur
- pa
- uk
- gu
- th
- pl
tags:
- pii
- private
- pii-detection
- privacy
pretty_name: PRIVAset
size_categories:
- 1M<n<10M
---

# PRIVAset: A Multilingual Synthetic PII Detection Dataset

PRIVAset is a large-scale, privacy-safe, synthetic dataset for training and evaluating **Personally Identifiable Information (PII) filtering systems**. It supports **25 languages**, includes **16 PII types**, and is designed for tasks such as classification, named-entity recognition (NER), and redaction.

All data is generated using `Faker` (locale-aware) and custom synthetic logic. **No real PII is used**, making it safe for public release, model fine-tuning, and benchmarking.

---

## Dataset Highlights

- **16 PII types** – including `PERSON_NAME`, `EMAIL`, `PHONE`, `SSN`, `CREDIT_CARD`, `IPV4/6`, `STREET_ADDRESS`, `DATE_OF_BIRTH`, `PASSPORT`, `DRIVERS_LICENSE`, `IBAN`, `TAX_ID`, `API_KEY`, `MEDICAL_RECORD`, and `BANK_ACCOUNT`.
- **25 languages** – with native-script templates and locale-aware Faker support. Languages range from high-resource (English, Chinese, Arabic) to lower-resource (Javanese, Gujarati, Punjabi).
- **10 real-world contexts** – including chat, email, support tickets, medical notes, legal documents, code snippets, social posts, resumes, ecommerce, and finance.
- **Balanced positives and negatives** – with hard negatives that look like PII but are not.
- **Token‑level annotations** – each record includes character-level spans (`start`, `end`, `type`, `value`), document‑level label (`has_pii`), and risk score (`high`/`medium`/`low`).
- **Multi‑PII examples** – ~30% of records contain 2–4 PII entities.
- **Robustness augmentations** – including email obfuscation (`[at]`/`(dot)`), phone format variance, and case flipping.
- **Flexible exports** – available in `JSONL`, `CSV`, Hugging Face `datasets`, and instruction‑tuning formats (`prompt`/`completion`).

---

## Supported Languages

| Language | Code | Faker Locale | Native Script |
|----------|------|--------------|---------------|
| Chinese | `zh` | `zh_CN` | 中文 |
| Arabic | `ar` | `ar_SA` | العربية |
| Hindi | `hi` | `hi_IN` | हिन्दी |
| English | `en` | `en_US` | English |
| Spanish | `es` | `es_ES` | Español |
| Bengali | `bn` | `bn_BD` | বাংলা |
| Portuguese | `pt` | `pt_PT` | Português |
| Russian | `ru` | `ru_RU` | Русский |
| Japanese | `ja` | `ja_JP` | 日本語 |
| German | `de` | `de_DE` | Deutsch |
| Korean | `ko` | `ko_KR` | 한국어 |
| French | `fr` | `fr_FR` | Français |
| Javanese | `jv` | `id_ID` | Basa Jawa |
| Telugu | `te` | `en_IN` | తెలుగు |
| Marathi | `mr` | `mr_IN` | मराठी |
| Vietnamese | `vi` | `vi_VN` | Tiếng Việt |
| Tamil | `ta` | `ta_IN` | தமிழ் |
| Italian | `it` | `it_IT` | Italiano |
| Turkish | `tr` | `tr_TR` | Türkçe |
| Urdu | `ur` | `en_PK` | اردو |
| Punjabi | `pa` | `en_IN` | ਪੰਜਾਬੀ |
| Ukrainian | `uk` | `uk_UA` | Українська |
| Gujarati | `gu` | `gu_IN` | ગુજરાતી |
| Thai | `th` | `th_TH` | ภาษาไทย |
| Polish | `pl` | `pl_PL` | Polski |

---

## Use Cases

- **Multilingual PII classification** – use `has_pii` + `language` for per‑language calibration.
- **NER / Token classification** – use `pii` spans to generate BIO tags; spans are character‑accurate for CJK and Arabic scripts.
- **Redaction systems** – replace spans with `[REDACTED_{TYPE}]`.
- **Risk‑aware filtering** – block `high`‑risk entities (SSN, credit card, IBAN, API key) and warn on `medium` risk.

---

## License

This dataset is released under the **MIT License**.