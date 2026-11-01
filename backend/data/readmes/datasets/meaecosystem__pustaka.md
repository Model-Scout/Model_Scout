---
license: other
license_name: mea-ecosystem-open-license-v1.0
license_link: https://huggingface.co/datasets/meaecosystem/pustaka/blob/main/LICENSE.md
language:
  - id
  - en
  - ja
  - zh
  - ko
tags:
  - indonesian
  - text-corpus
  - pretraining
  - language-modeling
  - multilingual
  - web-crawl
  - wikipedia
  - open-corpus
task_categories:
  - text-generation
pretty_name: Pustaka
size_categories:
  - 10M<n<100M
---

<div align="center">

<img src="assets/pustaka_banner.svg" alt="Pustaka banner" width="100%">

<br>

**[ 🇮🇩 Bahasa Indonesia ](#bahasa-indonesia) · [ 🇬🇧 English ](#english) · [ 🇯🇵 日本語 ](#日本語) · [ 🇨🇳 中文 ](#中文) · [ 🇰🇷 한국어 ](#한국어)**

</div>

---

## Bahasa Indonesia

**Pustaka** adalah korpus teks terbuka berskala besar yang dikembangkan oleh **MEA Ecosystem**, dimulai dengan fokus penuh pada Bahasa Indonesia. Corpus ini disusun dari beberapa sumber publik berkualitas — web crawl yang telah difilter, ensiklopedia, berita, forum, hingga lexicon bahasa gaul — lalu diproses ulang melalui pipeline pembersihan (deteksi bahasa, filter panjang dokumen, deteksi boilerplate/spam, dan deduplikasi) sebelum dirilis.

Pustaka dibangun untuk **digunakan siapa saja** — baik untuk pretraining model bahasa, penelitian NLP, maupun eksperimen pribadi — dan dirilis secara terbuka di bawah Hugging Face.

### Statistik

| Sumber | Dokumen | Karakter (approx) | Status |
|---|---:|---:|---|
| CulturaX (id) | 22.353.087 | ~58,73 Miliar | ✅ Selesai |
| Indo4B | 17.889.547 | ~4,95 Miliar | ✅ Selesai |
| CC-News ID | 2.622.291 | ~5,54 Miliar | ✅ Selesai |
| Wikipedia ID | 520.330 | ~0,95 Miliar | ✅ Selesai |
| Kaskus WebText | 31.737 | ~0,11 Miliar | ✅ Selesai |
| Kamus Alay (slang) | 15.006 pasangan kata | — | ✅ Selesai |
| OSCAR-2301 (id) | — | — | ⏸️ Belum termasuk (menunggu approval akses) |
| **Total** | **~43,4 Juta dokumen** | **~70,3 Miliar karakter** | *(di luar OSCAR & Kamus Alay)* |
*Tabel di atas mencakup `corpus-bahasa-indonesia/` saja. Untuk corpus lain (kode, matematika, instruksi, Wikipedia multi-bahasa, hukum, dan corpus native Bahasa Indonesia yang sedang berjalan), lihat bagian masing-masing di bawah.*

### Sumber & Lisensi

| Sumber | Deskripsi | Lisensi |
|---|---|---|
| [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX) (subset `id`) | Web crawl gabungan mC4 + OSCAR, telah dibersihkan & dedup MinHash | Mengikuti lisensi asal (mC4 + OSCAR), non-komersial kecuali dinyatakan lain — lihat halaman dataset |
| [OSCAR-2301](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301) (subset `id`) | Web crawl tambahan, snapshot berbeda dari CulturaX | CC0, dengan syarat penggunaan tambahan dari OSCAR — lihat halaman dataset |
| [SEACrowd/Indo4B](https://huggingface.co/datasets/SEACrowd/indo4b) (via repost parquet) | Campuran teks formal & percakapan dari 12 sumber | CC0 |
| [Wikipedia ID](https://huggingface.co/datasets/wikimedia/wikipedia) | Ensiklopedia bahasa Indonesia | CC BY-SA 3.0 / GFDL |
| CC-News ID (Wikidepia) | Berita CommonCrawl 2016-2021, difilter bahasa Indonesia | Mengikuti lisensi CommonCrawl |
| Kaskus WebText (Wikidepia) | Teks forum Kaskus, difilter minimal 3 cendol (karma) | Untuk riset, cek ketentuan penggunaan sumber asal |
| [Kamus Alay](https://github.com/nasalsabila/kamus-alay) | Lexicon slang-formal Bahasa Indonesia | MIT |

**Catatan penting**: setiap subset mengikuti lisensi sumber aslinya masing-masing. Sebelum menggunakan Pustaka untuk keperluan komersial, periksa lisensi tiap subset yang relevan dengan kebutuhan Anda.

### Corpus Code

Selain corpus Bahasa Indonesia, Pustaka juga menyediakan **corpus kode sumber multi-bahasa** (total **7,66 GB**) yang dikurasi dari [codeparrot/github-code](https://huggingface.co/datasets/codeparrot/github-code) — mencakup 10 bahasa pemrograman modern:

`Python`, `JavaScript`, `TypeScript`, `HTML`, `CSS`, `Java`, `Go`, `C++`, `Rust`, `SQL`

**Filter kualitas untuk corpus kode:**
- Hanya file dengan **lisensi permissive** (MIT, Apache-2.0, BSD, ISC, dll) — lisensi copyleft (GPL/AGPL) dikecualikan
- **Wajib mengandung dokumentasi** (docstring/comment block) — file tanpa indikasi dokumentasi dibuang
- Filter panjang file dan deteksi file generated/minified/binary blob
- Deduplikasi exact-hash lintas sumber

Lihat bagian [Struktur Data](#struktur-data) untuk detail folder `corpus-code/`.

### Corpus Math & Reasoning

Pustaka juga menyediakan **corpus soal matematika dengan penalaran (reasoning)** dalam Bahasa Inggris, terdiri dari:

| Sumber | Deskripsi | Jumlah Soal |
|---|---|---:|
| [GSM8K](https://huggingface.co/datasets/openai/gsm8k) | Soal matematika grade-school, 2-8 langkah penyelesaian | 7.473 |
| [NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | Soal kompetisi (SMA s.d. olimpiade), format Chain-of-Thought lengkap | 852.853 |
| **Total** | | **~860.326** |

**Catatan bahasa**: kedua sumber ini murni Bahasa Inggris. NuminaMath aslinya dikumpulkan dari soal ujian berbahasa non-Inggris (OCR dari PDF), namun teks asli sebelum diterjemahkan tidak dirilis publik oleh pembuatnya — hanya versi hasil terjemahan Inggris yang tersedia.

**Format berbeda dari corpus lain**: data ini disimpan sebagai **JSONL** (bukan `.txt` polos), karena berstruktur `{question, solution, answer}` — mempertahankan struktur penting untuk instruction-tuning/reasoning, berbeda dari corpus teks bebas lainnya.

### Corpus Instruction & Dialog

Pustaka juga menyediakan **corpus instruksi/dialog** dwibahasa (ID + EN), untuk instruction-tuning:

| Sumber | Bahasa | Deskripsi | Jumlah |
|---|---|---|---:|
| [Dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | EN | Instruksi human-written kualitas tinggi dari Databricks | ~15K |
| [Alpaca-cleaned-Indonesian](https://huggingface.co/datasets/ilhamfadheel/alpaca-cleaned-indonesian) | ID | Alpaca-cleaned diterjemahkan ke Bahasa Indonesia | ~52K |
| [OIG](https://huggingface.co/datasets/laion/OIG) | EN | Open Instruction Generalist, diambil 500K dari total 44M+ (kualitas medium menurut pembuatnya, dibatasi agar tidak mendominasi corpus) | 500K |
| **Total** | | | **~567K instruksi** |

**Format**: JSONL dengan struktur `{source, instruction, input, output}`, konsisten dengan corpus-math.

Lihat bagian [Struktur Data](#struktur-data) untuk detail folder `corpus-instruct/`.

### Corpus Wikipedia Multi-bahasa

Selain Wikipedia Bahasa Indonesia (bagian dari `corpus-bahasa-indonesia/`), Pustaka menyediakan **corpus Wikipedia multi-bahasa** terpisah yang mencakup bahasa-bahasa besar lainnya, bersumber dari snapshot `wikimedia/wikipedia` (20231101):

| Bahasa | Ukuran | Status |
|---|---:|---|
| Jepang (ja) | — | ✅ Selesai |
| Korea (ko) | — | ✅ Selesai |
| Mandarin (zh) | — | ✅ Selesai |
| **Total (ja+ko+zh)** | **2,81 GB** | ✅ Selesai |

Wikipedia Bahasa Indonesia tetap berada di `corpus-bahasa-indonesia/wikipedia/` (sudah selesai lewat pipeline terpisah), tidak diduplikasi ke sini. Metodologi pembersihan mengikuti pipeline yang sama dengan corpus Pustaka lainnya (deteksi bahasa, filter panjang, heuristik boilerplate/spam, deduplikasi xxhash64), dengan target bahasa dicek per-sumber, bukan hardcoded.

Lihat bagian [Struktur Data](#struktur-data) untuk detail folder `wikipedia/`.

### Corpus Hukum & Perundang-undangan

Pustaka juga menyediakan **corpus teks hukum/perundang-undangan**, mencakup teks legislasi utama dari negara-negara besar:

| Sumber | Negara | Deskripsi | Lisensi | Status |
|---|---|---|---|---|
| [y2lan/japan-law](https://huggingface.co/datasets/y2lan/japan-law) | Jepang | 8.746 undang-undang dari situs resmi e-Gov Jepang | MIT | ✅ Selesai (8.740 dokumen) |
| [macadeliccc/US-FederalLaws](https://huggingface.co/datasets/macadeliccc/US-FederalLaws) | Amerika Serikat | US Code + undang-undang publik kongres + executive orders | Apache-2.0 (teks hukum federal AS sendiri juga berstatus public domain berdasarkan *Georgia v. Public.Resource.Org*, 2020) | ✅ Selesai (34.187 dokumen) |
| — | Tiongkok (zh) | Belum ada sumber berlisensi permisif yang bersih (alternatif yang ada berbayar/komersial atau web-crawl campuran) | — | ⏸️ Dilewati sementara; direncanakan lewat crawler generik yang lebih luas nanti |

**Catatan format**: sumber Jepang memakai skema tetap yang bersih (`num`, `title`, `id`, `date`, `body`); sumber AS berasal dari 4 file terpisah dengan skema berbeda-beda, sehingga ekstraksi field dilakukan secara dinamis.

Lihat bagian [Struktur Data](#struktur-data) untuk detail folder `corpus-hukum/`.

### Corpus Bahasa Indonesia Native (Common Crawl, bebas lisensi restriktif)

Pustaka sedang membangun **corpus web Bahasa Indonesia baru yang independen**, bersumber langsung dari file WET mentah Common Crawl (ekstraksi plaintext yang disediakan Common Crawl sendiri), bukan lewat rilis ulang pihak ketiga seperti CulturaX atau OSCAR.

**Alasan dibangun**: CulturaX dan OSCAR melakukan crawl Common Crawl sendiri lalu merilis ulang hasilnya di bawah lisensi non-komersial yang lebih restriktif. Karena MEA Ecosystem memproses data mentah Common Crawl secara langsung (CC0 / tanpa batasan dari Common Crawl Foundation) alih-alih menggunakan turunan pihak ketiga yang sudah berlisensi, tidak ada pembatasan non-komersial yang terwarisi. Corpus ini ditujukan untuk pada akhirnya **menggantikan** CulturaX/OSCAR/Indo4B dalam training produksi SIESTA, bukan sekadar melengkapi.

- **Sumber**: file WET Common Crawl, snapshot `CC-MAIN-2026-34` (tetap; snapshot lebih baru bisa dipakai manual lewat `--snapshot` bila diinginkan)
- **Filtering**: pipeline identik dengan `corpus-bahasa-indonesia/` lainnya — fastText `lid.176` (ambang kepercayaan 0,65 untuk label `id`), filter panjang (200–300.000 karakter), heuristik boilerplate/spam, deduplikasi xxhash64
- **Independensi**: folder ini **tidak** melakukan cross-dedup terhadap hash progress `corpus-bahasa-indonesia/` yang sudah ada — sengaja dibuat dari nol sebagai pengganti berlisensi bersih, bukan pelengkap
- **Status**: 🔄 Sedang berjalan — pipeline latar belakang jangka panjang (estimasi 30+ hari dengan kecepatan saat ini dari total 95.342 file WET di snapshot). Saat ini terkumpul **1,16 GB** (per 14 Sept 2026), dengan satu shard selesai dan satu shard lagi sedang berjalan.

Corpus ini berjalan independen dan tidak menghambat penggunaan corpus Bahasa Indonesia berbasis CulturaX/Indo4B yang sudah ada untuk pengembangan sehari-hari — ini proyek jangka panjang untuk rilis produksi dengan lisensi yang sepenuhnya bersih.

Lihat bagian [Struktur Data](#struktur-data) untuk detail folder `corpus-bahasa-indonesia-native/`.

### Struktur Data

```
meaecosystem/pustaka/
├── corpus-bahasa-indonesia/
│   ├── culturax/
│   │   └── culturax_shard_XXXXX.txt.gz
│   ├── oscar/
│   ├── indo4b/
│   ├── wikipedia/            (hanya id, lihat wikipedia/ terpisah di bawah untuk ja/ko/zh)
│   ├── ccnews/
│   ├── kaskus/
│   └── kamus_alay/
│       └── kamus_alay.txt.gz   (format: slang<TAB>formal, satu pasangan per baris)
├── corpus-code/                  (7,66 GB total)
│   ├── python/
│   ├── javascript/
│   ├── typescript/
│   ├── html/
│   ├── css/
│   ├── java/
│   ├── go/
│   ├── cpp/
│   ├── rust/
│   └── sql/
│       └── code_{bahasa}_shard_XXXXX.txt.gz   (satu file kode per baris, newline internal di-escape sebagai \n)
├── corpus-math/                  (~860K soal, format JSONL)
│   ├── gsm8k/
│   └── numinamath/
│       └── math_{sumber}_shard_XXXXX.jsonl.gz   (format: {"source", "question", "solution", "answer"} per baris)
├── corpus-instruct/               (~567K instruksi, format JSONL)
│   ├── dolly/
│   ├── alpaca_id/
│   └── oig/
│       └── instruct_{sumber}_shard_XXXXX.jsonl.gz   (format: {"source", "instruction", "input", "output"} per baris)
├── wikipedia/                    (2,81 GB, multi-bahasa, terpisah dari corpus-bahasa-indonesia)
│   ├── ja/
│   ├── ko/
│   └── zh/
│       └── wikipedia_{bahasa}_shard_XXXXX.txt.gz
├── corpus-hukum/                 (teks perundang-undangan)
│   ├── japan/
│   └── us/
│       └── hukum_{negara}_shard_XXXXX.jsonl.gz
├── corpus-bahasa-indonesia-native/   (🔄 sedang berjalan, ~1,16 GB terkumpul — pengganti CulturaX/OSCAR/Indo4B berlisensi bersih)
│   └── native_id_shard_XXXXX.txt.gz
├── tokenizer/
│   └── tokenizer.json          (Byte-Level BPE, vocab 131.072 — lihat bagian Tokenizer)
└── _progress/                   (metadata internal untuk resume pipeline)
```

Setiap file `.txt.gz` berisi satu dokumen per baris (kecuali `kamus_alay`, yang berformat TSV).

### Cara Menggunakan

```python
from datasets import load_dataset

# Load satu subset (streaming, direkomendasikan untuk corpus besar)
ds = load_dataset(
    "meaecosystem/pustaka",
    data_files="corpus-bahasa-indonesia/wikipedia/*.txt.gz",
    split="train",
    streaming=True,
)

for row in ds:
    print(row["text"][:200])
    break
```

Atau dengan `pandas` untuk file kecil seperti `kamus_alay`:

```python
import pandas as pd
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="meaecosystem/pustaka",
    repo_type="dataset",
    filename="corpus-bahasa-indonesia/kamus_alay/kamus_alay.txt.gz",
)
df = pd.read_csv(path, sep="\t", names=["slang", "formal"], compression="gzip")
```

### Tokenizer

Pustaka menyertakan tokenizer **Byte-Level BPE** (vocab **131.072**) yang dilatih khusus dari sampel corpus ini — mencakup seluruh cakupan bahasa Pustaka (Indonesia, Inggris, Jepang, Korea, Mandarin) plus kode program. Karena berbasis byte-level, tokenizer ini **tidak pernah menghasilkan token `<unk>`** — karakter apa pun yang tidak tercakup oleh merge yang dipelajari akan otomatis jatuh ke representasi byte UTF-8 mentah, sehingga seluruh corpus (termasuk yang akan bertambah di masa depan) tetap bisa dihitung tokennya secara konsisten.

Tokenizer ini **bukan** dimaksudkan untuk model produksi manapun (termasuk SIESTA) — melainkan sebagai alat ukur standar untuk menghitung jumlah token di seluruh corpus Pustaka, dan disertakan agar hasil penghitungan token dapat direproduksi oleh siapa saja. Special token: `<pad>`, `<bos>`, `<eos>`, `<unk>` (yang terakhir nyaris tidak pernah muncul karena sifat byte-level di atas).

File tokenizer tersedia di `tokenizer/tokenizer.json`.

**Hasil pengukuran token (estimasi, per 15 Sept 2026)**:

| Sumber | Dokumen | Token (estimasi) |
|---|---:|---:|
| corpus-bahasa-indonesia | ~24,5 Juta | ~6,40 Miliar |
| corpus-bahasa-indonesia-native | ~610 Ribu | ~0,98 Miliar |
| corpus-code | ~4,76 Juta | ~11,64 Miliar |
| corpus-math | ~815 Ribu | ~0,39 Miliar |
| corpus-instruct | ~389 Ribu | ~0,16 Miliar |
| corpus-hukum | ~55,7 Ribu | ~0,10 Miliar |
| wikipedia (ja/ko/zh) | ~941 Ribu | ~1,47 Miliar |
| **Total** | **~31,5 Juta** | **~20,15 Miliar** |

*Angka di atas adalah estimasi (sampling per-shard + ekstrapolasi berdasarkan rasio ukuran file terkompresi), bukan hitungan eksak per dokumen — cukup akurat untuk keperluan pelaporan skala corpus.*

### Metodologi Pembersihan

1. **Deteksi bahasa** — fastText `lid.176`, ambang kepercayaan minimum 0,65 untuk label `id`
2. **Filter panjang** — dokumen di bawah 200 karakter atau di atas 300.000 karakter dibuang
3. **Filter boilerplate/spam** — heuristik rasio simbol-huruf, rasio huruf kapital, dan deteksi baris berulang (menu navigasi, cookie notice, dsb.)
4. **Deduplikasi** — exact-dedup menggunakan hash xxhash64 di seluruh corpus (lintas sumber)

### Kontak & Kontribusi

Dikembangkan oleh **Evan (M. Evan Almunawar)** sebagai bagian dari **MEA Ecosystem**. Pertanyaan, laporan masalah, atau saran dapat disampaikan melalui halaman diskusi dataset ini di Hugging Face.

---

## English

**Pustaka** is a large-scale open text corpus developed by **MEA Ecosystem**, starting with a full focus on Indonesian. The corpus is assembled from several high-quality public sources — filtered web crawls, encyclopedic text, news, forums, and a colloquial-slang lexicon — then reprocessed through a cleaning pipeline (language detection, document-length filtering, boilerplate/spam detection, and deduplication) before release.

Pustaka is built to be **freely usable by anyone** — for language model pretraining, NLP research, or personal experimentation — and is released openly on Hugging Face.

### Statistics

| Source | Documents | Characters (approx) | Status |
|---|---:|---:|---|
| CulturaX (id) | 22,353,087 | ~58.73B | ✅ Done |
| Indo4B | 17,889,547 | ~4.95B | ✅ Done |
| CC-News ID | 2,622,291 | ~5.54B | ✅ Done |
| Wikipedia ID | 520,330 | ~0.95B | ✅ Done |
| Kaskus WebText | 31,737 | ~0.11B | ✅ Done |
| Kamus Alay (slang) | 15,006 word pairs | — | ✅ Done |
| OSCAR-2301 (id) | — | — | ⏸️ Not yet included (awaiting access approval) |
| **Total** | **~43.4M documents** | **~70.3B characters** | *(excluding OSCAR & Kamus Alay)* |
*The table above covers `corpus-bahasa-indonesia/` only. For the other corpora (code, math, instruction, multilingual Wikipedia, legislation, and the in-progress native Indonesian corpus), see their respective sections below.*

### Sources & Licensing

| Source | Description | License |
|---|---|---|
| [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX) (`id` subset) | Combined mC4 + OSCAR web crawl, cleaned & MinHash-deduplicated | Follows upstream licenses (mC4 + OSCAR); non-commercial unless stated otherwise — see dataset page |
| [OSCAR-2301](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301) (`id` subset) | Additional web crawl, different snapshot from CulturaX | CC0, with OSCAR's additional terms of use — see dataset page |
| [SEACrowd/Indo4B](https://huggingface.co/datasets/SEACrowd/indo4b) (via parquet repost) | Formal + colloquial text mix from 12 sources | CC0 |
| [Wikipedia ID](https://huggingface.co/datasets/wikimedia/wikipedia) | Indonesian-language encyclopedia | CC BY-SA 3.0 / GFDL |
| CC-News ID (Wikidepia) | CommonCrawl news 2016-2021, filtered to Indonesian | Follows CommonCrawl's terms |
| Kaskus WebText (Wikidepia) | Kaskus forum text, filtered to 3+ cendol (karma) | For research use; check upstream terms |
| [Kamus Alay](https://github.com/nasalsabila/kamus-alay) | Indonesian slang-to-formal lexicon | MIT |

**Important**: each subset follows its own upstream license. Before any commercial use, check the license of every subset relevant to your use case.

### Code Corpus

Beyond the Indonesian corpus, Pustaka also provides a **multi-language source code corpus** (**7.66 GB** total) curated from [codeparrot/github-code](https://huggingface.co/datasets/codeparrot/github-code) — covering 10 modern programming languages:

`Python`, `JavaScript`, `TypeScript`, `HTML`, `CSS`, `Java`, `Go`, `C++`, `Rust`, `SQL`

**Quality filters for the code corpus:**
- **Permissive licenses only** (MIT, Apache-2.0, BSD, ISC, etc.) — copyleft licenses (GPL/AGPL) are excluded
- **Must contain documentation** (docstring/comment block) — files with no documentation indicators are dropped
- Length filtering and detection of generated/minified/binary blob files
- Exact-hash deduplication across sources

See the [Data Structure](#data-structure) section for `corpus-code/` folder details.

### Math & Reasoning Corpus

Pustaka also provides a **math reasoning corpus** in English, consisting of:

| Source | Description | Problem Count |
|---|---|---:|
| [GSM8K](https://huggingface.co/datasets/openai/gsm8k) | Grade-school math problems, 2-8 step solutions | 7,473 |
| [NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | Competition problems (high school to olympiad), full Chain-of-Thought format | 852,853 |
| **Total** | | **~860,326** |

**Language note**: both sources are purely in English. NuminaMath was originally sourced from non-English exam materials (OCR'd from PDFs), but the pre-translation original text was never released publicly by its creators — only the translated English version is available.

**Different format from other corpora**: this data is stored as **JSONL** (not plain `.txt`), since it's structured as `{question, solution, answer}` — preserving structure that matters for instruction-tuning/reasoning use, unlike the free-text corpora elsewhere in Pustaka.

### Instruction & Dialog Corpus

Pustaka also provides a bilingual (ID + EN) **instruction/dialog corpus** for instruction-tuning:

| Source | Language | Description | Count |
|---|---|---|---:|
| [Dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | EN | High-quality human-written instructions from Databricks | ~15K |
| [Alpaca-cleaned-Indonesian](https://huggingface.co/datasets/ilhamfadheel/alpaca-cleaned-indonesian) | ID | Alpaca-cleaned translated to Indonesian | ~52K |
| [OIG](https://huggingface.co/datasets/laion/OIG) | EN | Open Instruction Generalist, 500K sampled from 44M+ total (medium quality per its creators, capped to avoid dominating the corpus) | 500K |
| **Total** | | | **~567K instructions** |

**Format**: JSONL with structure `{source, instruction, input, output}`, consistent with corpus-math.

See the [Data Structure](#data-structure) section for `corpus-instruct/` folder details.

### Wikipedia Multilingual Corpus

Beyond Indonesian Wikipedia (part of `corpus-bahasa-indonesia/`), Pustaka provides a separate **multilingual Wikipedia corpus** covering additional major languages, sourced from the `wikimedia/wikipedia` snapshot (20231101):

| Language | Size | Status |
|---|---:|---|
| Japanese (ja) | — | ✅ Done |
| Korean (ko) | — | ✅ Done |
| Chinese (zh) | — | ✅ Done |
| **Total (ja+ko+zh)** | **2.81 GB** | ✅ Done |

Indonesian Wikipedia remains in `corpus-bahasa-indonesia/wikipedia/` (already complete via a separate pipeline) rather than being duplicated here. Cleaning follows the same pipeline as the rest of Pustaka (language detection, length filtering, boilerplate/spam heuristics, xxhash64 deduplication), with the target language checked per-source instead of hardcoded.

See the [Data Structure](#data-structure) section for `wikipedia/` folder details.

### Legislation Corpus

Pustaka also provides a **legislation/law text corpus**, covering the primary legal text of major countries:

| Source | Country | Description | License | Status |
|---|---|---|---|---|
| [y2lan/japan-law](https://huggingface.co/datasets/y2lan/japan-law) | Japan | 8,746 laws from Japan's official e-Gov site | MIT | ✅ Done (8,740 kept) |
| [macadeliccc/US-FederalLaws](https://huggingface.co/datasets/macadeliccc/US-FederalLaws) | United States | US Code + congressional public laws + executive orders | Apache-2.0 (US federal law text itself is also public domain per *Georgia v. Public.Resource.Org*, 2020) | ✅ Done (34,187 kept) |
| — | China (zh) | No clean permissive source currently available (commercial-only or mixed web-crawl alternatives) | — | ⏸️ Skipped for now; planned via a broader generic crawler later |

**Format note**: Japan uses a clean fixed schema (`num`, `title`, `id`, `date`, `body`); the US source draws from 4 separate files with differing schemas, so field extraction is handled dynamically.

See the [Data Structure](#data-structure) section for `corpus-hukum/` folder details.

### Native Indonesian Web Corpus (Common Crawl, license-clean)

Pustaka is building a **new, independent Indonesian web corpus** sourced directly from raw Common Crawl WET files (plaintext extraction provided by Common Crawl itself), rather than via third-party re-releases like CulturaX or OSCAR.

**Why this exists**: CulturaX and OSCAR crawl Common Crawl themselves and then re-release their derivatives under their own, more restrictive non-commercial terms. Because MEA Ecosystem processes the raw Common Crawl data directly (CC0 / unrestricted from the Common Crawl Foundation) rather than consuming a third party's already-licensed derivative, no inherited non-commercial restriction applies. This corpus is intended to eventually **replace** CulturaX/OSCAR/Indo4B in SIESTA's production training, not just supplement them.

- **Source**: Common Crawl WET files, snapshot `CC-MAIN-2026-34` (fixed; a newer snapshot can be passed manually via `--snapshot` when desired)
- **Filtering**: identical pipeline to the rest of `corpus-bahasa-indonesia/` — fastText `lid.176` (0.65 confidence threshold for `id`), length filter (200–300,000 characters), boilerplate/spam heuristics, xxhash64 deduplication
- **Independence**: this folder does **not** cross-deduplicate against the existing `corpus-bahasa-indonesia/` hash progress — it's intentionally a from-scratch, independently-licensed replacement, not a supplement
- **Status**: 🔄 In progress — long-running background pipeline (estimated 30+ days at current pace across 95,342 total WET files in the snapshot). Currently **1.16 GB** collected so far (as of Sept 14, 2026), with one finalized shard and a second shard in progress.

This corpus runs independently of, and does not block, Pustaka's current CulturaX/Indo4B-based Indonesian text for day-to-day development use — it is a long-term project for a fully clean-license production release.

See the [Data Structure](#data-structure) section for `corpus-bahasa-indonesia-native/` folder details.

### Data Structure

```
meaecosystem/pustaka/
├── corpus-bahasa-indonesia/
│   ├── culturax/
│   │   └── culturax_shard_XXXXX.txt.gz
│   ├── oscar/
│   ├── indo4b/
│   ├── wikipedia/            (id only — see separate wikipedia/ below for ja/ko/zh)
│   ├── ccnews/
│   ├── kaskus/
│   └── kamus_alay/
│       └── kamus_alay.txt.gz   (format: slang<TAB>formal, one pair per line)
├── corpus-code/                  (7.66 GB total)
│   ├── python/
│   ├── javascript/
│   ├── typescript/
│   ├── html/
│   ├── css/
│   ├── java/
│   ├── go/
│   ├── cpp/
│   ├── rust/
│   └── sql/
│       └── code_{language}_shard_XXXXX.txt.gz   (one code file per line, internal newlines escaped as \n)
├── corpus-math/                  (~860K problems, JSONL format)
│   ├── gsm8k/
│   └── numinamath/
│       └── math_{source}_shard_XXXXX.jsonl.gz   (format: {"source", "question", "solution", "answer"} per line)
├── corpus-instruct/               (~567K instructions, JSONL format)
│   ├── dolly/
│   ├── alpaca_id/
│   └── oig/
│       └── instruct_{source}_shard_XXXXX.jsonl.gz   (format: {"source", "instruction", "input", "output"} per line)
├── wikipedia/                    (2.81 GB, multilingual, separate from corpus-bahasa-indonesia)
│   ├── ja/
│   ├── ko/
│   └── zh/
│       └── wikipedia_{language}_shard_XXXXX.txt.gz
├── corpus-hukum/                 (legislation text)
│   ├── japan/
│   └── us/
│       └── hukum_{country}_shard_XXXXX.jsonl.gz
├── corpus-bahasa-indonesia-native/   (🔄 in progress, ~1.16 GB collected so far — license-clean replacement for CulturaX/OSCAR/Indo4B)
│   └── native_id_shard_XXXXX.txt.gz
├── tokenizer/
│   └── tokenizer.json          (Byte-Level BPE, 131,072 vocab — see Tokenizer section)
└── _progress/                   (internal pipeline metadata for resuming)
```

Each `.txt.gz` file contains one document per line (except `kamus_alay`, which is TSV-formatted).

### Usage

```python
from datasets import load_dataset

# Load a single subset (streaming recommended for large corpora)
ds = load_dataset(
    "meaecosystem/pustaka",
    data_files="corpus-bahasa-indonesia/wikipedia/*.txt.gz",
    split="train",
    streaming=True,
)

for row in ds:
    print(row["text"][:200])
    break
```

Or with `pandas` for small files like `kamus_alay`:

```python
import pandas as pd
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="meaecosystem/pustaka",
    repo_type="dataset",
    filename="corpus-bahasa-indonesia/kamus_alay/kamus_alay.txt.gz",
)
df = pd.read_csv(path, sep="\t", names=["slang", "formal"], compression="gzip")
```

### Tokenizer

Pustaka includes a **Byte-Level BPE** tokenizer (**131,072** vocab) trained specifically on a sample of this corpus — covering Pustaka's full language scope (Indonesian, English, Japanese, Korean, Chinese) plus source code. Because it's byte-level, this tokenizer **never produces an `<unk>` token** — any character not covered by a learned merge automatically falls back to raw UTF-8 byte representation, so the entire corpus (including future growth) can always be counted consistently.

This tokenizer is **not** intended for any production model (including SIESTA) — it exists as a standardized measurement tool to count tokens across the Pustaka corpus, and is included so that token counts can be reproduced by anyone. Special tokens: `<pad>`, `<bos>`, `<eos>`, `<unk>` (the last of which should almost never fire, given the byte-level fallback above).

The tokenizer file is available at `tokenizer/tokenizer.json`.

**Token count results (estimated, as of Sept 15, 2026)**:

| Source | Documents | Tokens (estimated) |
|---|---:|---:|
| corpus-bahasa-indonesia | ~24.5M | ~6.40B |
| corpus-bahasa-indonesia-native | ~610K | ~0.98B |
| corpus-code | ~4.76M | ~11.64B |
| corpus-math | ~815K | ~0.39B |
| corpus-instruct | ~389K | ~0.16B |
| corpus-hukum | ~55.7K | ~0.10B |
| wikipedia (ja/ko/zh) | ~941K | ~1.47B |
| **Total** | **~31.5M** | **~20.15B** |

*The figures above are estimates (per-shard sampling extrapolated from compressed-file-size ratios), not exact per-document counts — accurate enough for reporting corpus scale.*

### Cleaning Methodology

1. **Language detection** — fastText `lid.176`, minimum confidence threshold of 0.65 for the `id` label
2. **Length filtering** — documents under 200 characters or over 300,000 characters are dropped
3. **Boilerplate/spam filtering** — heuristics on symbol-to-letter ratio, uppercase ratio, and repeated-line detection (nav menus, cookie notices, etc.)
4. **Deduplication** — exact deduplication using xxhash64 across the entire corpus (cross-source)

### Contact & Contributions

Developed by **Evan (M. Evan Almunawar)** as part of **MEA Ecosystem**. Questions, issue reports, or suggestions can be raised via this dataset's discussion page on Hugging Face.

---

## 日本語

**Pustaka**（プスタカ）は、**MEA Ecosystem** が開発した大規模なオープンテキストコーパスです。まずはインドネシア語に完全に焦点を当てて構築されています。このコーパスは、フィルタリング済みのウェブクロール、百科事典、ニュース、フォーラム、俗語辞書など、複数の高品質な公開ソースから構成され、公開前に言語検出・文書長フィルタリング・定型文/スパム検出・重複除去のクリーニングパイプラインを経て再処理されています。

Pustaka は、言語モデルの事前学習、NLP研究、個人的な実験など、**誰でも自由に利用できる**ことを目的として、Hugging Face 上でオープンに公開されています。

### 統計

| ソース | ドキュメント数 | 文字数（概算） | 状態 |
|---|---:|---:|---|
| CulturaX (id) | 22,353,087 | 約58.73億 | ✅ 完了 |
| Indo4B | 17,889,547 | 約4.95億 | ✅ 完了 |
| CC-News ID | 2,622,291 | 約5.54億 | ✅ 完了 |
| Wikipedia ID | 520,330 | 約0.95億 | ✅ 完了 |
| Kaskus WebText | 31,737 | 約0.11億 | ✅ 完了 |
| Kamus Alay（俗語） | 15,006語ペア | — | ✅ 完了 |
| OSCAR-2301 (id) | — | — | ⏸️ 未収録（アクセス承認待ち） |
| **合計** | **約4,340万件** | **約703億文字** | *（OSCAR・Kamus Alayを除く）* |
*上記の表は`corpus-bahasa-indonesia/`のみを対象としています。その他のコーパス（コード、数学、指示、多言語Wikipedia、法令、進行中のインドネシア語ネイティブコーパス）については、以下の各セクションを参照してください。*

### ソースとライセンス

| ソース | 説明 | ライセンス |
|---|---|---|
| [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)（`id` サブセット） | mC4 と OSCAR を統合したウェブクロール、クリーニング済み・MinHash重複除去済み | 元のライセンスに準拠（mC4 + OSCAR）。特記なき限り非商用 — データセットページを参照 |
| [OSCAR-2301](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301)（`id` サブセット） | CulturaX とは異なるスナップショットの追加ウェブクロール | CC0、OSCAR の追加利用規約あり — データセットページを参照 |
| [SEACrowd/Indo4B](https://huggingface.co/datasets/SEACrowd/indo4b)（parquet 再公開版経由） | 12のソースからのフォーマル/口語混合テキスト | CC0 |
| [Wikipedia ID](https://huggingface.co/datasets/wikimedia/wikipedia) | インドネシア語版百科事典 | CC BY-SA 3.0 / GFDL |
| CC-News ID (Wikidepia) | CommonCrawl 由来のニュース（2016〜2021年）、インドネシア語にフィルタリング済み | CommonCrawl の利用規約に準拠 |
| Kaskus WebText (Wikidepia) | Kaskus フォーラムのテキスト、cendol（カルマ）3以上でフィルタリング | 研究目的での利用向け、元ソースの利用規約を確認してください |
| [Kamus Alay](https://github.com/nasalsabila/kamus-alay) | インドネシア語の俗語⇔標準語辞書 | MIT |

**重要**: 各サブセットはそれぞれの元のライセンスに従います。商用利用の前には、関連するすべてのサブセットのライセンスを確認してください。

### コードコーパス

Pustaka はインドネシア語コーパスに加え、[codeparrot/github-code](https://huggingface.co/datasets/codeparrot/github-code) から厳選した**多言語ソースコードコーパス**（合計 **7.66 GB**）も提供しています — 10の現代的なプログラミング言語をカバー:

`Python`、`JavaScript`、`TypeScript`、`HTML`、`CSS`、`Java`、`Go`、`C++`、`Rust`、`SQL`

**コードコーパスの品質フィルター:**
- **寛容なライセンスのみ**（MIT、Apache-2.0、BSD、ISC など）— コピーレフトライセンス（GPL/AGPL）は除外
- **ドキュメントを含むことが必須**（docstring/コメントブロック）— ドキュメントの兆候がないファイルは除外
- 長さフィルタリングと、生成/難読化/バイナリブロブファイルの検出
- ソース全体にわたる完全一致ハッシュによる重複除去

フォルダ `corpus-code/` の詳細は[データ構造](#データ構造)セクションを参照してください。

### 数学・推論コーパス

Pustaka は英語の**数学推論コーパス**も提供しています。以下で構成されます:

| ソース | 説明 | 問題数 |
|---|---|---:|
| [GSM8K](https://huggingface.co/datasets/openai/gsm8k) | 小学校レベルの数学問題、2〜8ステップの解法 | 7,473 |
| [NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | 競技問題（高校〜オリンピックレベル）、完全な思考の連鎖（CoT）形式 | 852,853 |
| **合計** | | **約860,326** |

**言語に関する注記**: 両ソースとも純粋に英語です。NuminaMath はもともと非英語の試験資料（PDFからOCR）を元にしていますが、翻訳前の原文は作成者によって公開されておらず、翻訳済みの英語版のみが利用可能です。

**他のコーパスと異なる形式**: このデータは `{question, solution, answer}` という構造を持つため、プレーンな `.txt` ではなく **JSONL** 形式で保存されています — Pustaka の他の自由テキストコーパスとは異なり、instruction-tuning/推論用途に重要な構造を保持しています。

### 指示・対話コーパス

Pustaka はインストラクションチューニング用に、バイリンガル（インドネシア語＋英語）の**指示・対話コーパス**も提供しています:

| ソース | 言語 | 説明 | 件数 |
|---|---|---|---:|
| [Dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | 英語 | Databricks による高品質な人間作成の指示データ | 約15K |
| [Alpaca-cleaned-Indonesian](https://huggingface.co/datasets/ilhamfadheel/alpaca-cleaned-indonesian) | インドネシア語 | Alpaca-cleaned をインドネシア語に翻訳 | 約52K |
| [OIG](https://huggingface.co/datasets/laion/OIG) | 英語 | Open Instruction Generalist、全4,400万件以上から50万件をサンプリング（作成者によれば品質は「中程度」、コーパスを支配しないよう上限を設定） | 50万 |
| **合計** | | | **約56.7万件** |

**形式**: `{source, instruction, input, output}` 構造の JSONL、corpus-math と統一。

フォルダ `corpus-instruct/` の詳細は[データ構造](#データ構造)セクションを参照してください。

### 多言語Wikipediaコーパス

インドネシア語版Wikipedia（`corpus-bahasa-indonesia/`の一部）に加えて、Pustakaは`wikimedia/wikipedia`スナップショット（20231101）を元にした、他の主要言語をカバーする独立した**多言語Wikipediaコーパス**を提供しています：

| 言語 | サイズ | 状態 |
|---|---:|---|
| 日本語 (ja) | — | ✅ 完了 |
| 韓国語 (ko) | — | ✅ 完了 |
| 中国語 (zh) | — | ✅ 完了 |
| **合計 (ja+ko+zh)** | **2.81 GB** | ✅ 完了 |

インドネシア語版Wikipediaは別パイプラインで既に完了しているため、重複を避けて`corpus-bahasa-indonesia/wikipedia/`にそのまま残しています。クリーニング手法はPustakaの他のコーパスと同様です（言語検出、長さフィルタリング、定型文/スパムのヒューリスティック、xxhash64による重複除去）。対象言語はハードコードではなく、ソースごとに動的にチェックされます。

`wikipedia/`フォルダの詳細は[データ構造](#データ構造)セクションを参照してください。

### 法令コーパス

Pustakaは主要国の一次法令テキストをカバーする**法令コーパス**も提供しています：

| ソース | 国 | 説明 | ライセンス | 状態 |
|---|---|---|---|---|
| [y2lan/japan-law](https://huggingface.co/datasets/y2lan/japan-law) | 日本 | 日本の公式e-Govサイトから8,746件の法令 | MIT | ✅ 完了（8,740件収録） |
| [macadeliccc/US-FederalLaws](https://huggingface.co/datasets/macadeliccc/US-FederalLaws) | アメリカ | 米国法典＋連邦議会の公法＋大統領令 | Apache-2.0（米国連邦法のテキスト自体も*Georgia v. Public.Resource.Org*（2020年）判決によりパブリックドメイン） | ✅ 完了（34,187件収録） |
| — | 中国 (zh) | 現時点で利用可能な許容的ライセンスのクリーンなソースなし（代替は商用限定または混在ウェブクロール） | — | ⏸️ 現時点でスキップ。より広範な汎用クローラーで将来対応予定 |

**フォーマットに関する注記**：日本のソースは固定の明確なスキーマ（`num`、`title`、`id`、`date`、`body`）を使用。米国のソースはスキーマが異なる4つの別ファイルから構成されるため、フィールド抽出は動的に処理されます。

`corpus-hukum/`フォルダの詳細は[データ構造](#データ構造)セクションを参照してください。

### インドネシア語ネイティブWebコーパス（Common Crawl、ライセンスクリーン）

Pustakaは、CulturaXやOSCARのようなサードパーティの再公開版を経由せず、Common Crawlの生のWETファイル（Common Crawl自身によるプレーンテキスト抽出）から直接ソースした、**新しい独立のインドネシア語Webコーパス**を構築中です。

**構築理由**：CulturaXとOSCARはCommon Crawl自体をクロールした上で、より制限の厳しい独自の非商用ライセンスで再公開しています。MEA EcosystemはCommon Crawlの生データを直接処理するため（Common Crawl Foundation自体によるCC0／無制限ライセンス）、サードパーティの既にライセンス付与された派生物を利用する場合とは異なり、非商用制限は継承されません。このコーパスは最終的にSIESTAの本番トレーニングにおいてCulturaX/OSCAR/Indo4Bを**置き換える**ことを意図しており、単なる補完ではありません。

- **ソース**：Common CrawlのWETファイル、スナップショット`CC-MAIN-2026-34`（固定。新しいスナップショットを使う場合は`--snapshot`で手動指定可能）
- **フィルタリング**：`corpus-bahasa-indonesia/`の他コーパスと同一のパイプライン — fastText `lid.176`（`id`ラベルの信頼度閾値0.65）、長さフィルタ（200〜300,000文字）、定型文/スパムのヒューリスティック、xxhash64による重複除去
- **独立性**：このフォルダは既存の`corpus-bahasa-indonesia/`のハッシュ進捗とは**クロス重複除去を行いません** — 補完ではなく、ライセンスがクリーンな置き換えとして意図的にゼロから構築されています
- **状態**：🔄 進行中 — 長期のバックグラウンドパイプライン（スナップショット内の全95,342件のWETファイルに対し、現在のペースで30日以上を見込む）。現時点（2026年9月14日時点）で**1.16 GB**を収集済み。完了したシャード1つと、進行中のシャード1つ。

このコーパスは、日常的な開発用途で使われている既存のCulturaX/Indo4Bベースのインドネシア語テキストとは独立して稼働しており、それらをブロックすることはありません — 完全にライセンスがクリーンな本番リリースを目指す長期プロジェクトです。

`corpus-bahasa-indonesia-native/`フォルダの詳細は[データ構造](#データ構造)セクションを参照してください。

### データ構造

```
meaecosystem/pustaka/
├── corpus-bahasa-indonesia/
│   ├── culturax/
│   │   └── culturax_shard_XXXXX.txt.gz
│   ├── oscar/
│   ├── indo4b/
│   ├── wikipedia/            (idのみ — ja/ko/zhは下記の別のwikipedia/を参照)
│   ├── ccnews/
│   ├── kaskus/
│   └── kamus_alay/
│       └── kamus_alay.txt.gz   （形式: slang<TAB>formal、1行に1ペア）
├── corpus-code/                  （合計 7.66 GB）
│   ├── python/
│   ├── javascript/
│   ├── typescript/
│   ├── html/
│   ├── css/
│   ├── java/
│   ├── go/
│   ├── cpp/
│   ├── rust/
│   └── sql/
│       └── code_{言語}_shard_XXXXX.txt.gz   （1行につき1コードファイル、内部改行は \n としてエスケープ）
├── corpus-math/                  （約86万問、JSONL形式）
│   ├── gsm8k/
│   └── numinamath/
│       └── math_{ソース}_shard_XXXXX.jsonl.gz   （形式: 1行ごとに {"source", "question", "solution", "answer"}）
├── corpus-instruct/               （約56.7万件、JSONL形式）
│   ├── dolly/
│   ├── alpaca_id/
│   └── oig/
│       └── instruct_{ソース}_shard_XXXXX.jsonl.gz   （形式: 1行ごとに {"source", "instruction", "input", "output"}）
├── wikipedia/                    (2.81 GB、多言語、corpus-bahasa-indonesiaとは別)
│   ├── ja/
│   ├── ko/
│   └── zh/
│       └── wikipedia_{言語}_shard_XXXXX.txt.gz
├── corpus-hukum/                 (法令テキスト)
│   ├── japan/
│   └── us/
│       └── hukum_{国}_shard_XXXXX.jsonl.gz
├── corpus-bahasa-indonesia-native/   (🔄 進行中、約1.16 GB収集済み — CulturaX/OSCAR/Indo4Bのライセンスクリーンな置き換え)
│   └── native_id_shard_XXXXX.txt.gz
├── tokenizer/
│   └── tokenizer.json          （Byte-Level BPE、語彙数131,072 — トークナイザーの項を参照）
└── _progress/                   （パイプライン再開用の内部メタデータ）
```

各 `.txt.gz` ファイルには1行につき1文書が含まれます（`kamus_alay` のみ TSV 形式）。

### 使い方

```python
from datasets import load_dataset

# 単一サブセットの読み込み（大規模コーパスにはストリーミングを推奨）
ds = load_dataset(
    "meaecosystem/pustaka",
    data_files="corpus-bahasa-indonesia/wikipedia/*.txt.gz",
    split="train",
    streaming=True,
)

for row in ds:
    print(row["text"][:200])
    break
```

`kamus_alay` のような小さいファイルには `pandas` を使用:

```python
import pandas as pd
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="meaecosystem/pustaka",
    repo_type="dataset",
    filename="corpus-bahasa-indonesia/kamus_alay/kamus_alay.txt.gz",
)
df = pd.read_csv(path, sep="\t", names=["slang", "formal"], compression="gzip")
```

### トークナイザー

Pustaka には、このコーパスのサンプルから専用に学習された **Byte-Level BPE トークナイザー**（語彙数 **131,072**）が含まれています — Pustaka の全言語（インドネシア語・英語・日本語・韓国語・中国語）とソースコードをカバーしています。バイトレベルであるため、このトークナイザーは**`<unk>` トークンを一切生成しません** — 学習済みマージでカバーされていない文字は自動的に生の UTF-8 バイト表現にフォールバックするため、今後増加するコーパスも含めて常に一貫してトークン数を計測できます。

このトークナイザーは、いかなる本番モデル（SIESTA を含む）向けのものでも**ありません**。Pustaka コーパス全体のトークン数を計測するための標準ツールとして存在し、誰でもトークン数を再現できるように同梱されています。特殊トークン: `<pad>`、`<bos>`、`<eos>`、`<unk>`（上記の理由でほとんど発生しません）。

トークナイザーファイルは `tokenizer/tokenizer.json` にあります。

**トークン数の計測結果（推定値、2026年9月15日時点）**:

| ソース | ドキュメント数 | トークン数（推定） |
|---|---:|---:|
| corpus-bahasa-indonesia | 約2,450万 | 約64.0億 |
| corpus-bahasa-indonesia-native | 約61万 | 約9.8億 |
| corpus-code | 約476万 | 約116.4億 |
| corpus-math | 約81.5万 | 約3.9億 |
| corpus-instruct | 約38.9万 | 約1.6億 |
| corpus-hukum | 約5.57万 | 約1.0億 |
| wikipedia (ja/ko/zh) | 約94.1万 | 約14.7億 |
| **合計** | **約3,150万** | **約201.5億** |

*上記の数値は推定値です（シャードごとのサンプリングを圧縮ファイルサイズ比率で外挿したもの）。厳密なドキュメント単位のカウントではありませんが、コーパス規模の報告には十分な精度です。*

### クリーニング手法

1. **言語検出** — fastText `lid.176`、`id` ラベルの最小信頼度しきい値は0.65
2. **長さフィルタリング** — 200文字未満または300,000文字を超える文書は除外
3. **定型文/スパムフィルタリング** — 記号対文字比率、大文字比率、繰り返し行検出（ナビメニュー、Cookie通知など）に基づくヒューリスティック
4. **重複除去** — コーパス全体（ソース横断）で xxhash64 による完全一致重複除去

### お問い合わせ・貢献

**MEA Ecosystem** の一環として **Evan（M. Evan Almunawar）** により開発されています。質問、問題報告、ご提案は Hugging Face 上の本データセットのディスカッションページからお寄せください。

---

## 中文

**Pustaka**（普斯塔卡）是由 **MEA Ecosystem** 开发的大规模开放文本语料库，首先完全聚焦于印度尼西亚语。该语料库整合了多个高质量公开来源——经过过滤的网络爬取数据、百科全书、新闻、论坛，以及俚语词典——并在发布前经过清洗流程（语言检测、文档长度过滤、样板/垃圾内容检测、去重）重新处理。

Pustaka 旨在**供任何人自由使用**——无论是用于语言模型预训练、NLP研究，还是个人实验——并在 Hugging Face 上公开发布。

### 统计数据

| 来源 | 文档数 | 字符数（约） | 状态 |
|---|---:|---:|---|
| CulturaX (id) | 22,353,087 | 约587.3亿 | ✅ 已完成 |
| Indo4B | 17,889,547 | 约49.5亿 | ✅ 已完成 |
| CC-News ID | 2,622,291 | 约55.4亿 | ✅ 已完成 |
| Wikipedia ID | 520,330 | 约9.5亿 | ✅ 已完成 |
| Kaskus WebText | 31,737 | 约1.1亿 | ✅ 已完成 |
| Kamus Alay（俚语） | 15,006 组词对 | — | ✅ 已完成 |
| OSCAR-2301 (id) | — | — | ⏸️ 尚未收录（等待访问批准） |
| **总计** | **约4,340万篇文档** | **约703亿字符** | *（不含 OSCAR 与 Kamus Alay）* |
*上表仅涵盖`corpus-bahasa-indonesia/`。其他语料库（代码、数学、指令、多语言维基百科、法律法规，以及正在进行中的印尼语原生语料库）请参见下方各自的部分。*

### 来源与许可证

| 来源 | 描述 | 许可证 |
|---|---|---|
| [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)（`id` 子集） | mC4 与 OSCAR 合并的网络爬取数据，已清洗并通过 MinHash 去重 | 遵循上游许可证（mC4 + OSCAR）；除非另有说明，否则为非商业用途 — 详见数据集页面 |
| [OSCAR-2301](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301)（`id` 子集） | 与 CulturaX 不同快照的额外网络爬取数据 | CC0，附带 OSCAR 的额外使用条款 — 详见数据集页面 |
| [SEACrowd/Indo4B](https://huggingface.co/datasets/SEACrowd/indo4b)（通过 parquet 转存版本） | 来自12个来源的正式与口语混合文本 | CC0 |
| [Wikipedia ID](https://huggingface.co/datasets/wikimedia/wikipedia) | 印度尼西亚语百科全书 | CC BY-SA 3.0 / GFDL |
| CC-News ID (Wikidepia) | 2016-2021年 CommonCrawl 新闻，已过滤为印度尼西亚语 | 遵循 CommonCrawl 条款 |
| Kaskus WebText (Wikidepia) | Kaskus 论坛文本，过滤至 cendol（威望值）3 以上 | 供研究使用，请查阅原始来源条款 |
| [Kamus Alay](https://github.com/nasalsabila/kamus-alay) | 印度尼西亚俚语与标准语对照词典 | MIT |

**重要提示**：每个子集均遵循各自的上游许可证。在进行任何商业用途之前，请查阅与您用途相关的每个子集的许可证。

### 代码语料库

除印尼语语料库外，Pustaka 还提供了从 [codeparrot/github-code](https://huggingface.co/datasets/codeparrot/github-code) 精心筛选的**多语言源代码语料库**（总计 **7.66 GB**）——涵盖10种现代编程语言：

`Python`、`JavaScript`、`TypeScript`、`HTML`、`CSS`、`Java`、`Go`、`C++`、`Rust`、`SQL`

**代码语料库的质量过滤条件：**
- **仅限宽松许可证**（MIT、Apache-2.0、BSD、ISC 等）——著佐权（copyleft）许可证（GPL/AGPL）被排除
- **必须包含文档**（文档字符串/注释块）——不含文档迹象的文件将被剔除
- 长度过滤，并检测生成/压缩混淆/二进制块文件
- 跨来源的精确哈希去重

有关 `corpus-code/` 文件夹的详细信息，请参阅[数据结构](#数据结构)部分。

### 数学与推理语料库

Pustaka 还提供英文的**数学推理语料库**，包括：

| 来源 | 描述 | 题目数量 |
|---|---|---:|
| [GSM8K](https://huggingface.co/datasets/openai/gsm8k) | 小学数学题，2-8 步解题过程 | 7,473 |
| [NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | 竞赛题目（高中至奥赛水平），完整思维链（CoT）格式 | 852,853 |
| **总计** | | **约860,326** |

**语言说明**：两个来源均为纯英文。NuminaMath 最初来源于非英文考试材料（从PDF进行OCR），但翻译前的原文从未由其创建者公开发布——仅提供翻译后的英文版本。

**与其他语料库不同的格式**：由于该数据具有 `{question, solution, answer}` 结构，因此以 **JSONL** 格式存储（而非纯文本 `.txt`）——这保留了对指令微调/推理用途至关重要的结构，有别于 Pustaka 中其他的自由文本语料库。

### 指令与对话语料库

Pustaka 还提供双语（印尼语+英语）的**指令/对话语料库**，用于指令微调：

| 来源 | 语言 | 描述 | 数量 |
|---|---|---|---:|
| [Dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | 英语 | Databricks 提供的高质量人工撰写指令 | 约1.5万 |
| [Alpaca-cleaned-Indonesian](https://huggingface.co/datasets/ilhamfadheel/alpaca-cleaned-indonesian) | 印尼语 | Alpaca-cleaned 翻译为印尼语版本 | 约5.2万 |
| [OIG](https://huggingface.co/datasets/laion/OIG) | 英语 | Open Instruction Generalist，从4400万+条中抽取50万条（据创建者称质量为"中等"，设置上限以避免主导整个语料库） | 50万 |
| **总计** | | | **约56.7万条指令** |

**格式**：JSONL，结构为 `{source, instruction, input, output}`，与 corpus-math 保持一致。

有关 `corpus-instruct/` 文件夹的详细信息，请参阅[数据结构](#数据结构)部分。

### 多语言维基百科语料库

除了印尼语维基百科（属于`corpus-bahasa-indonesia/`的一部分）之外，Pustaka 还提供一个独立的**多语言维基百科语料库**，涵盖其他主要语言，数据来源于`wikimedia/wikipedia`快照（20231101）：

| 语言 | 大小 | 状态 |
|---|---:|---|
| 日语 (ja) | — | ✅ 完成 |
| 韩语 (ko) | — | ✅ 完成 |
| 中文 (zh) | — | ✅ 完成 |
| **总计 (ja+ko+zh)** | **2.81 GB** | ✅ 完成 |

印尼语维基百科通过独立流程已经完成，因此仍保留在`corpus-bahasa-indonesia/wikipedia/`中，未在此处重复收录。清洗方法与 Pustaka 其他语料库一致（语言检测、长度过滤、样板/垃圾内容启发式规则、xxhash64 去重），目标语言按来源动态检测，而非硬编码。

`wikipedia/`文件夹的详细信息请参见[数据结构](#数据结构)部分。

### 法律法规语料库

Pustaka 还提供**法律法规文本语料库**，涵盖主要国家的核心法律文本：

| 来源 | 国家 | 描述 | 许可证 | 状态 |
|---|---|---|---|---|
| [y2lan/japan-law](https://huggingface.co/datasets/y2lan/japan-law) | 日本 | 来自日本官方 e-Gov 网站的 8,746 部法律 | MIT | ✅ 完成（收录 8,740 条） |
| [macadeliccc/US-FederalLaws](https://huggingface.co/datasets/macadeliccc/US-FederalLaws) | 美国 | 美国法典 + 国会公法 + 行政命令 | Apache-2.0（根据 2020 年*Georgia v. Public.Resource.Org*判决，美国联邦法律文本本身也属于公有领域） | ✅ 完成（收录 34,187 条） |
| — | 中国 (zh) | 目前没有干净的宽松许可来源（现有替代方案为商业付费或混合网络爬取内容） | — | ⏸️ 暂时跳过，计划后续通过更通用的爬虫处理 |

**格式说明**：日本来源采用固定的清晰结构（`num`、`title`、`id`、`date`、`body`）；美国来源分布在 4 个结构不一致的独立文件中，因此字段提取采用动态方式处理。

`corpus-hukum/`文件夹的详细信息请参见[数据结构](#数据结构)部分。

### 印尼语原生网络语料库（Common Crawl，许可证纯净）

Pustaka 正在构建一个**全新的独立印尼语网络语料库**，直接来源于 Common Crawl 的原始 WET 文件（由 Common Crawl 自身提供的纯文本提取），而非通过 CulturaX 或 OSCAR 等第三方转发版本。

**构建原因**：CulturaX 和 OSCAR 自行抓取 Common Crawl 数据后，以各自更严格的非商业条款重新发布衍生版本。由于 MEA Ecosystem 直接处理 Common Crawl 的原始数据（来自 Common Crawl Foundation 本身的 CC0／无限制许可），而非使用第三方已授权的衍生版本，因此不会继承任何非商业限制。该语料库的目标是最终在 SIESTA 的生产训练中**取代** CulturaX/OSCAR/Indo4B，而不仅仅是补充。

- **来源**：Common Crawl 的 WET 文件，快照版本`CC-MAIN-2026-34`（固定；如需使用更新的快照，可通过`--snapshot`手动指定）
- **过滤方式**：与`corpus-bahasa-indonesia/`其余部分完全相同的流程 — fastText `lid.176`（`id`标签置信度阈值 0.65）、长度过滤（200–300,000 字符）、样板/垃圾内容启发式规则、xxhash64 去重
- **独立性**：此文件夹**不会**与现有`corpus-bahasa-indonesia/`的哈希进度进行交叉去重 — 这是刻意从零构建的、许可证纯净的替代方案，而非补充内容
- **状态**：🔄 进行中 — 长期后台流程（按当前速度，快照中共 95,342 个 WET 文件，预计需 30 天以上）。截至 2026 年 9 月 14 日，已收集**1.16 GB**，其中一个分片已完成，另一个分片正在进行中。

该语料库独立运行，不会阻碍目前基于 CulturaX/Indo4B 的印尼语文本在日常开发中的使用 — 这是一个旨在实现完全许可证纯净的生产版本的长期项目。

`corpus-bahasa-indonesia-native/`文件夹的详细信息请参见[数据结构](#数据结构)部分。

### 数据结构

```
meaecosystem/pustaka/
├── corpus-bahasa-indonesia/
│   ├── culturax/
│   │   └── culturax_shard_XXXXX.txt.gz
│   ├── oscar/
│   ├── indo4b/
│   ├── wikipedia/            (仅id — ja/ko/zh请见下方独立的wikipedia/)
│   ├── ccnews/
│   ├── kaskus/
│   └── kamus_alay/
│       └── kamus_alay.txt.gz   （格式：slang<TAB>formal，每行一对）
├── corpus-code/                  （总计 7.66 GB）
│   ├── python/
│   ├── javascript/
│   ├── typescript/
│   ├── html/
│   ├── css/
│   ├── java/
│   ├── go/
│   ├── cpp/
│   ├── rust/
│   └── sql/
│       └── code_{语言}_shard_XXXXX.txt.gz   （每行一个代码文件，内部换行符转义为 \n）
├── corpus-math/                  （约86万题，JSONL 格式）
│   ├── gsm8k/
│   └── numinamath/
│       └── math_{来源}_shard_XXXXX.jsonl.gz   （格式：每行 {"source", "question", "solution", "answer"}）
├── corpus-instruct/               （约56.7万条，JSONL 格式）
│   ├── dolly/
│   ├── alpaca_id/
│   └── oig/
│       └── instruct_{来源}_shard_XXXXX.jsonl.gz   （格式：每行 {"source", "instruction", "input", "output"}）
├── wikipedia/                    (2.81 GB，多语言，独立于corpus-bahasa-indonesia)
│   ├── ja/
│   ├── ko/
│   └── zh/
│       └── wikipedia_{语言}_shard_XXXXX.txt.gz
├── corpus-hukum/                 (法律法规文本)
│   ├── japan/
│   └── us/
│       └── hukum_{国家}_shard_XXXXX.jsonl.gz
├── corpus-bahasa-indonesia-native/   (🔄 进行中，已收集约1.16 GB — CulturaX/OSCAR/Indo4B的许可证纯净替代方案)
│   └── native_id_shard_XXXXX.txt.gz
├── tokenizer/
│   └── tokenizer.json          （Byte-Level BPE，词汇量131,072 — 详见分词器部分）
└── _progress/                   （用于恢复处理流程的内部元数据）
```

每个 `.txt.gz` 文件每行包含一个文档（`kamus_alay` 除外，其格式为 TSV）。

### 使用方法

```python
from datasets import load_dataset

# 加载单个子集（大型语料库建议使用流式加载）
ds = load_dataset(
    "meaecosystem/pustaka",
    data_files="corpus-bahasa-indonesia/wikipedia/*.txt.gz",
    split="train",
    streaming=True,
)

for row in ds:
    print(row["text"][:200])
    break
```

对于像 `kamus_alay` 这样的小文件，可使用 `pandas`：

```python
import pandas as pd
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="meaecosystem/pustaka",
    repo_type="dataset",
    filename="corpus-bahasa-indonesia/kamus_alay/kamus_alay.txt.gz",
)
df = pd.read_csv(path, sep="\t", names=["slang", "formal"], compression="gzip")
```

### 分词器

Pustaka 包含一个专门基于本语料库样本训练的 **Byte-Level BPE 分词器**（词汇量 **131,072**）——涵盖 Pustaka 的全部语言范围（印尼语、英语、日语、韩语、中文）以及源代码。由于采用字节级别（byte-level）设计，该分词器**绝不会产生 `<unk>` 标记**——任何未被已学习合并规则覆盖的字符都会自动回退为原始 UTF-8 字节表示，因此整个语料库（包括未来新增的部分）始终可以保持一致的词元统计。

该分词器**并非**用于任何生产模型（包括 SIESTA），而是作为标准化测量工具，用于统计整个 Pustaka 语料库的词元数量，并随附以便任何人都能复现词元统计结果。特殊标记：`<pad>`、`<bos>`、`<eos>`、`<unk>`（由于上述字节级回退机制，最后一个几乎不会出现）。

分词器文件位于 `tokenizer/tokenizer.json`。

**词元统计结果（估算值，截至2026年9月15日）**：

| 来源 | 文档数 | 词元数（估算） |
|---|---:|---:|
| corpus-bahasa-indonesia | 约2,450万 | 约64.0亿 |
| corpus-bahasa-indonesia-native | 约61万 | 约9.8亿 |
| corpus-code | 约476万 | 约116.4亿 |
| corpus-math | 约81.5万 | 约3.9亿 |
| corpus-instruct | 约38.9万 | 约1.6亿 |
| corpus-hukum | 约5.57万 | 约1.0亿 |
| wikipedia (ja/ko/zh) | 约94.1万 | 约14.7亿 |
| **总计** | **约3,150万** | **约201.5亿** |

*以上数字为估算值（基于每个分片抽样、按压缩文件大小比例外推得出），并非精确的逐文档统计，但对于报告语料库规模而言已足够准确。*

### 清洗方法

1. **语言检测** — fastText `lid.176`，`id` 标签的最低置信度阈值为0.65
2. **长度过滤** — 剔除少于200字符或超过300,000字符的文档
3. **样板/垃圾内容过滤** — 基于符号与字母比例、大写字母比例，以及重复行检测（导航菜单、Cookie 通知等）的启发式规则
4. **去重** — 在整个语料库范围内（跨来源）使用 xxhash64 进行精确去重

### 联系与贡献

由 **Evan（M. Evan Almunawar）** 作为 **MEA Ecosystem** 的一部分开发。如有疑问、问题报告或建议，请通过本数据集在 Hugging Face 上的讨论页面提出。

---

## 한국어

**Pustaka**(푸스타카)는 **MEA Ecosystem**이 개발한 대규모 오픈 텍스트 코퍼스로, 인도네시아어에 전적으로 초점을 맞추어 시작되었습니다. 이 코퍼스는 필터링된 웹 크롤링 데이터, 백과사전, 뉴스, 포럼, 그리고 속어 사전 등 여러 고품질 공개 소스로 구성되며, 공개 전에 언어 감지, 문서 길이 필터링, 상용구/스팸 감지, 중복 제거를 포함한 정제 파이프라인을 거쳐 재처리됩니다.

Pustaka는 언어 모델 사전 학습, NLP 연구, 개인 실험 등 **누구나 자유롭게 사용할 수 있도록** 구축되었으며, Hugging Face에서 공개적으로 배포됩니다.

### 통계

| 소스 | 문서 수 | 문자 수 (약) | 상태 |
|---|---:|---:|---|
| CulturaX (id) | 22,353,087 | 약 587.3억 | ✅ 완료 |
| Indo4B | 17,889,547 | 약 49.5억 | ✅ 완료 |
| CC-News ID | 2,622,291 | 약 55.4억 | ✅ 완료 |
| Wikipedia ID | 520,330 | 약 9.5억 | ✅ 완료 |
| Kaskus WebText | 31,737 | 약 1.1억 | ✅ 완료 |
| Kamus Alay (속어) | 15,006 단어 쌍 | — | ✅ 완료 |
| OSCAR-2301 (id) | — | — | ⏸️ 미포함 (접근 승인 대기 중) |
| **합계** | **약 4,340만 건** | **약 703억 자** | *(OSCAR 및 Kamus Alay 제외)* |
*위 표는 `corpus-bahasa-indonesia/`만 포함합니다. 다른 코퍼스(코드, 수학, 지시문, 다국어 위키백과, 법령, 그리고 진행 중인 인도네시아어 네이티브 코퍼스)는 아래 각 섹션을 참조하세요.*

### 출처 및 라이선스

| 출처 | 설명 | 라이선스 |
|---|---|---|
| [CulturaX](https://huggingface.co/datasets/uonlp/CulturaX) (`id` 서브셋) | mC4와 OSCAR를 결합한 웹 크롤링, 정제 및 MinHash 중복 제거 완료 | 원본 라이선스를 따름(mC4 + OSCAR); 별도 명시가 없는 한 비상업적 용도 — 데이터셋 페이지 참조 |
| [OSCAR-2301](https://huggingface.co/datasets/oscar-corpus/OSCAR-2301) (`id` 서브셋) | CulturaX와 다른 스냅샷의 추가 웹 크롤링 | CC0, OSCAR의 추가 이용 약관 있음 — 데이터셋 페이지 참조 |
| [SEACrowd/Indo4B](https://huggingface.co/datasets/SEACrowd/indo4b) (parquet 재게시 버전) | 12개 출처의 격식체 및 구어체 혼합 텍스트 | CC0 |
| [Wikipedia ID](https://huggingface.co/datasets/wikimedia/wikipedia) | 인도네시아어 백과사전 | CC BY-SA 3.0 / GFDL |
| CC-News ID (Wikidepia) | 2016-2021년 CommonCrawl 뉴스, 인도네시아어로 필터링됨 | CommonCrawl 약관을 따름 |
| Kaskus WebText (Wikidepia) | Kaskus 포럼 텍스트, cendol(카르마) 3 이상으로 필터링됨 | 연구 목적 사용; 원본 출처 약관 확인 필요 |
| [Kamus Alay](https://github.com/nasalsabila/kamus-alay) | 인도네시아어 속어-표준어 사전 | MIT |

**중요**: 각 서브셋은 각자의 원본 라이선스를 따릅니다. 상업적 용도로 사용하기 전에 관련된 모든 서브셋의 라이선스를 확인하시기 바랍니다.

### 코드 코퍼스

인도네시아어 코퍼스 외에도, Pustaka는 [codeparrot/github-code](https://huggingface.co/datasets/codeparrot/github-code)에서 엄선한 **다국어 소스 코드 코퍼스**(총 **7.66 GB**)도 제공합니다 — 10개의 현대 프로그래밍 언어를 포함합니다:

`Python`, `JavaScript`, `TypeScript`, `HTML`, `CSS`, `Java`, `Go`, `C++`, `Rust`, `SQL`

**코드 코퍼스의 품질 필터:**
- **관대한 라이선스만 허용**(MIT, Apache-2.0, BSD, ISC 등) — 카피레프트 라이선스(GPL/AGPL)는 제외
- **문서화 필수**(docstring/주석 블록) — 문서화 흔적이 없는 파일은 제외
- 길이 필터링 및 생성됨/난독화됨/바이너리 블롭 파일 감지
- 소스 전체에 걸친 정확한 해시 기반 중복 제거

`corpus-code/` 폴더에 대한 자세한 내용은 [데이터 구조](#데이터-구조) 섹션을 참조하세요.

### 수학 및 추론 코퍼스

Pustaka는 영어로 된 **수학 추론 코퍼스**도 제공합니다:

| 소스 | 설명 | 문제 수 |
|---|---|---:|
| [GSM8K](https://huggingface.co/datasets/openai/gsm8k) | 초등학교 수준 수학 문제, 2-8단계 풀이 과정 | 7,473 |
| [NuminaMath-CoT](https://huggingface.co/datasets/AI-MO/NuminaMath-CoT) | 경시대회 문제(고교~올림피아드 수준), 완전한 사고의 연쇄(CoT) 형식 | 852,853 |
| **합계** | | **약 860,326** |

**언어 참고사항**: 두 소스 모두 순수 영어입니다. NuminaMath는 원래 비영어 시험 자료(PDF에서 OCR)를 기반으로 하지만, 번역 전 원문은 제작자에 의해 공개된 적이 없으며 — 번역된 영어 버전만 제공됩니다.

**다른 코퍼스와 다른 형식**: 이 데이터는 `{question, solution, answer}` 구조를 가지므로 일반 `.txt`가 아닌 **JSONL** 형식으로 저장됩니다 — Pustaka의 다른 자유 텍스트 코퍼스와 달리, instruction-tuning/추론 용도에 중요한 구조를 보존합니다.

### 지시문 및 대화 코퍼스

Pustaka는 instruction-tuning을 위한 이중 언어(인도네시아어+영어) **지시문/대화 코퍼스**도 제공합니다:

| 소스 | 언어 | 설명 | 개수 |
|---|---|---|---:|
| [Dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k) | 영어 | Databricks의 고품질 사람이 작성한 지시문 | 약 1.5만 |
| [Alpaca-cleaned-Indonesian](https://huggingface.co/datasets/ilhamfadheel/alpaca-cleaned-indonesian) | 인도네시아어 | Alpaca-cleaned를 인도네시아어로 번역 | 약 5.2만 |
| [OIG](https://huggingface.co/datasets/laion/OIG) | 영어 | Open Instruction Generalist, 전체 4,400만+ 건 중 50만 건 샘플링(제작자에 따르면 품질은 "중간" 수준, 코퍼스를 지배하지 않도록 상한 설정) | 50만 |
| **합계** | | | **약 56.7만 건** |

**형식**: `{source, instruction, input, output}` 구조의 JSONL, corpus-math와 통일됨.

`corpus-instruct/` 폴더에 대한 자세한 내용은 [데이터 구조](#데이터-구조) 섹션을 참조하세요.

### 다국어 위키백과 코퍼스

인도네시아어 위키백과(`corpus-bahasa-indonesia/`의 일부) 외에도, Pustaka는 `wikimedia/wikipedia` 스냅샷(20231101)을 기반으로 다른 주요 언어를 다루는 별도의 **다국어 위키백과 코퍼스**를 제공합니다:

| 언어 | 크기 | 상태 |
|---|---:|---|
| 일본어 (ja) | — | ✅ 완료 |
| 한국어 (ko) | — | ✅ 완료 |
| 중국어 (zh) | — | ✅ 완료 |
| **합계 (ja+ko+zh)** | **2.81 GB** | ✅ 완료 |

인도네시아어 위키백과는 별도의 파이프라인을 통해 이미 완료되었으므로 중복 수록하지 않고 `corpus-bahasa-indonesia/wikipedia/`에 그대로 유지됩니다. 정제 방식은 Pustaka의 다른 코퍼스와 동일합니다(언어 감지, 길이 필터링, 상용구/스팸 휴리스틱, xxhash64 중복 제거). 대상 언어는 하드코딩이 아닌 소스별 동적 검사를 통해 결정됩니다.

`wikipedia/` 폴더에 대한 자세한 내용은 [데이터 구조](#데이터-구조) 섹션을 참조하세요.

### 법령 코퍼스

Pustaka는 주요 국가의 핵심 법령 텍스트를 다루는 **법령 코퍼스**도 제공합니다:

| 소스 | 국가 | 설명 | 라이선스 | 상태 |
|---|---|---|---|---|
| [y2lan/japan-law](https://huggingface.co/datasets/y2lan/japan-law) | 일본 | 일본 공식 e-Gov 사이트의 법령 8,746건 | MIT | ✅ 완료 (8,740건 수록) |
| [macadeliccc/US-FederalLaws](https://huggingface.co/datasets/macadeliccc/US-FederalLaws) | 미국 | 미국 법전 + 연방 의회 공법 + 행정명령 | Apache-2.0 (미국 연방법 텍스트 자체도 2020년 *Georgia v. Public.Resource.Org* 판례에 따라 퍼블릭 도메인) | ✅ 완료 (34,187건 수록) |
| — | 중국 (zh) | 현재 깔끔한 허용적 라이선스 소스가 없음(대안은 상업용 유료이거나 혼합 웹크롤 데이터) | — | ⏸️ 현재는 제외; 추후 더 범용적인 크롤러로 별도 처리 예정 |

**형식 참고**: 일본 소스는 고정된 깔끔한 스키마(`num`, `title`, `id`, `date`, `body`)를 사용합니다. 미국 소스는 스키마가 서로 다른 4개의 개별 파일로 구성되어 있어 필드 추출을 동적으로 처리합니다.

`corpus-hukum/` 폴더에 대한 자세한 내용은 [데이터 구조](#데이터-구조) 섹션을 참조하세요.

### 인도네시아어 네이티브 웹 코퍼스 (Common Crawl, 라이선스 클린)

Pustaka는 CulturaX나 OSCAR 같은 제3자 재배포 버전을 거치지 않고, Common Crawl의 원본 WET 파일(Common Crawl 자체에서 제공하는 순수 텍스트 추출본)에서 직접 수집한 **새롭고 독립적인 인도네시아어 웹 코퍼스**를 구축하고 있습니다.

**구축 이유**: CulturaX와 OSCAR는 Common Crawl을 자체적으로 크롤링한 뒤, 더 제한적인 자체 비상업적 조건으로 재배포합니다. MEA Ecosystem은 Common Crawl의 원본 데이터를 직접 처리하므로(Common Crawl Foundation 자체의 CC0/무제한 라이선스), 이미 라이선스가 부여된 제3자의 파생물을 사용하는 경우와 달리 비상업적 제한이 상속되지 않습니다. 이 코퍼스는 궁극적으로 SIESTA의 프로덕션 학습에서 CulturaX/OSCAR/Indo4B를 **대체**하는 것을 목표로 하며, 단순한 보완이 아닙니다.

- **소스**: Common Crawl WET 파일, 스냅샷 `CC-MAIN-2026-34` (고정; 필요 시 `--snapshot`으로 최신 스냅샷을 수동 지정 가능)
- **필터링**: `corpus-bahasa-indonesia/`의 다른 부분과 동일한 파이프라인 — fastText `lid.176` (`id` 레이블 신뢰도 임계값 0.65), 길이 필터(200~300,000자), 상용구/스팸 휴리스틱, xxhash64 중복 제거
- **독립성**: 이 폴더는 기존 `corpus-bahasa-indonesia/`의 해시 진행 상황과 **교차 중복 제거를 수행하지 않습니다** — 보완이 아닌, 라이선스가 깨끗한 대체본으로서 의도적으로 처음부터 새로 구축됩니다
- **상태**: 🔄 진행 중 — 장기 백그라운드 파이프라인(스냅샷 내 전체 95,342개 WET 파일 기준, 현재 속도로 30일 이상 소요 예상). 2026년 9월 14일 기준 **1.16GB** 수집 완료, 완료된 샤드 1개와 진행 중인 샤드 1개.

이 코퍼스는 현재 일상적인 개발에 사용되는 기존 CulturaX/Indo4B 기반 인도네시아어 텍스트와 독립적으로 운영되며 이를 막지 않습니다 — 완전히 라이선스가 깨끗한 프로덕션 릴리스를 위한 장기 프로젝트입니다.

`corpus-bahasa-indonesia-native/` 폴더에 대한 자세한 내용은 [데이터 구조](#데이터-구조) 섹션을 참조하세요.

### 데이터 구조

```
meaecosystem/pustaka/
├── corpus-bahasa-indonesia/
│   ├── culturax/
│   │   └── culturax_shard_XXXXX.txt.gz
│   ├── oscar/
│   ├── indo4b/
│   ├── wikipedia/            (id 전용 — ja/ko/zh는 아래 별도의 wikipedia/ 참조)
│   ├── ccnews/
│   ├── kaskus/
│   └── kamus_alay/
│       └── kamus_alay.txt.gz   (형식: slang<TAB>formal, 줄당 한 쌍)
├── corpus-code/                  (총 7.66 GB)
│   ├── python/
│   ├── javascript/
│   ├── typescript/
│   ├── html/
│   ├── css/
│   ├── java/
│   ├── go/
│   ├── cpp/
│   ├── rust/
│   └── sql/
│       └── code_{언어}_shard_XXXXX.txt.gz   (한 줄에 하나의 코드 파일, 내부 줄바꿈은 \n으로 이스케이프)
├── corpus-math/                  (약 86만 문제, JSONL 형식)
│   ├── gsm8k/
│   └── numinamath/
│       └── math_{소스}_shard_XXXXX.jsonl.gz   (형식: 줄당 {"source", "question", "solution", "answer"})
├── corpus-instruct/               (약 56.7만 건, JSONL 형식)
│   ├── dolly/
│   ├── alpaca_id/
│   └── oig/
│       └── instruct_{소스}_shard_XXXXX.jsonl.gz   (형식: 줄당 {"source", "instruction", "input", "output"})
├── wikipedia/                    (2.81 GB, 다국어, corpus-bahasa-indonesia와 별도)
│   ├── ja/
│   ├── ko/
│   └── zh/
│       └── wikipedia_{언어}_shard_XXXXX.txt.gz
├── corpus-hukum/                 (법령 텍스트)
│   ├── japan/
│   └── us/
│       └── hukum_{국가}_shard_XXXXX.jsonl.gz
├── corpus-bahasa-indonesia-native/   (🔄 진행 중, 약 1.16GB 수집됨 — CulturaX/OSCAR/Indo4B의 라이선스 클린 대체본)
│   └── native_id_shard_XXXXX.txt.gz
├── tokenizer/
│   └── tokenizer.json          (Byte-Level BPE, 어휘 131,072개 — 토크나이저 섹션 참조)
└── _progress/                   (파이프라인 재개를 위한 내부 메타데이터)
```

각 `.txt.gz` 파일은 한 줄에 하나의 문서를 포함합니다(`kamus_alay` 제외, TSV 형식).

### 사용 방법

```python
from datasets import load_dataset

# 단일 서브셋 로드 (대용량 코퍼스는 스트리밍 권장)
ds = load_dataset(
    "meaecosystem/pustaka",
    data_files="corpus-bahasa-indonesia/wikipedia/*.txt.gz",
    split="train",
    streaming=True,
)

for row in ds:
    print(row["text"][:200])
    break
```

`kamus_alay`와 같은 작은 파일은 `pandas`를 사용할 수 있습니다:

```python
import pandas as pd
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="meaecosystem/pustaka",
    repo_type="dataset",
    filename="corpus-bahasa-indonesia/kamus_alay/kamus_alay.txt.gz",
)
df = pd.read_csv(path, sep="\t", names=["slang", "formal"], compression="gzip")
```

### 토크나이저

Pustaka에는 이 코퍼스의 샘플로부터 전용으로 학습된 **Byte-Level BPE 토크나이저**(어휘 **131,072**개)가 포함되어 있습니다 — Pustaka의 전체 언어 범위(인도네시아어, 영어, 일본어, 한국어, 중국어)와 소스 코드를 모두 다룹니다. 바이트 레벨 방식이기 때문에 이 토크나이저는 **`<unk>` 토큰을 전혀 생성하지 않습니다** — 학습된 병합 규칙으로 커버되지 않는 문자는 자동으로 원시 UTF-8 바이트 표현으로 대체되므로, 앞으로 늘어날 코퍼스를 포함해 항상 일관되게 토큰 수를 계산할 수 있습니다.

이 토크나이저는 어떠한 프로덕션 모델(SIESTA 포함)을 위한 것도 **아니며**, Pustaka 코퍼스 전체의 토큰 수를 측정하기 위한 표준화된 도구로서 존재하며, 누구나 토큰 수를 재현할 수 있도록 함께 제공됩니다. 특수 토큰: `<pad>`, `<bos>`, `<eos>`, `<unk>`(위의 이유로 거의 발생하지 않음).

토크나이저 파일은 `tokenizer/tokenizer.json`에 있습니다.

**토큰 수 측정 결과 (추정치, 2026년 9월 15일 기준)**:

| 소스 | 문서 수 | 토큰 수 (추정) |
|---|---:|---:|
| corpus-bahasa-indonesia | 약 2,450만 | 약 64.0억 |
| corpus-bahasa-indonesia-native | 약 61만 | 약 9.8억 |
| corpus-code | 약 476만 | 약 116.4억 |
| corpus-math | 약 81.5만 | 약 3.9억 |
| corpus-instruct | 약 38.9만 | 약 1.6억 |
| corpus-hukum | 약 5.57만 | 약 1.0억 |
| wikipedia (ja/ko/zh) | 약 94.1만 | 약 14.7억 |
| **합계** | **약 3,150만** | **약 201.5억** |

*위 수치는 추정치입니다(샤드별 샘플링을 압축 파일 크기 비율로 외삽한 값). 정확한 문서 단위 카운트는 아니지만, 코퍼스 규모를 보고하기에는 충분히 정확합니다.*

### 정제 방법론

1. **언어 감지** — fastText `lid.176`, `id` 레이블에 대한 최소 신뢰도 임계값 0.65
2. **길이 필터링** — 200자 미만 또는 300,000자를 초과하는 문서는 제외
3. **상용구/스팸 필터링** — 기호 대 문자 비율, 대문자 비율, 반복 줄 감지(네비게이션 메뉴, 쿠키 알림 등)에 기반한 휴리스틱
4. **중복 제거** — 전체 코퍼스(출처 간)에 걸쳐 xxhash64를 사용한 정확 중복 제거

### 문의 및 기여

**MEA Ecosystem**의 일환으로 **Evan(M. Evan Almunawar)**이 개발했습니다. 질문, 문제 보고, 제안 사항은 Hugging Face의 이 데이터셋 토론 페이지를 통해 제출해 주시기 바랍니다.