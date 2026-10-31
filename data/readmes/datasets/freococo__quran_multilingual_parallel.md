---
license: mit
language:
- ar
- sq
- am
- az
- bn
- bs
- bg
- my
- zh
- da
- nl
- en
- tl
- fr
- ff
- fa
- de
- gu
- ha
- hi
- id
- it
- ja
- jv
- kk
- km
- ko
- ku
- ky
- ms
- ml
- ps
- pl
- pt
- pa
- ru
- sd
- si
- so
- es
- sw
- sv
- tg
- ta
- tt
- te
- th
- tr
- ur
- ug
- uz
- yo
- 'no'
- vi
task_categories:
- translation
---

# 📘 Qur’an Multilingual Parallel Dataset (`quran_multilingual_parallel`)

This dataset presents a clean, structurally-aligned multilingual parallel corpus of the Qur’anic text. It is intended for linguistic, computational, and cross-lingual AI applications — not only for religious interpretation.

It contains over **6,200 verse-level alignments** in **54 human languages**, formatted in a machine-friendly `.csv` structure with language-specific translation fields.

---

## 🧠 Dataset Highlights

- 📖 6,236 ayahs (verses)
- 📚 114 surahs (chapters)
- 🌍 Translations in 53 languages
- 🕌 Arabic source text included
- 🔢 Fully aligned, row-per-verse CSV
- ⚠️ Missing translations are transparently documented

---

## 📁 Files Included

| File                             | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| `quran_multilingual_parallel.csv`| Complete parallel corpus: 6,236 rows × 57 columns                          |
| `README.md`                      | This documentation                                                         |

---

## 🧾 Column Format

Each row corresponds to a verse (ayah). Columns include:

| Column           | Description                                      |
|------------------|--------------------------------------------------|
| `surah_number`   | Integer: Surah (chapter) number (1–114)          |
| `surah`          | Slugified Surah name (e.g., `al-baqarah`)        |
| `ayah`           | Integer: Ayah (verse) number                     |
| `arabic`         | Original Arabic text of the verse                |
| `{language}`     | One column per language, each containing the translation for that ayah |

---

## 🌍 Languages Included

This dataset includes translations in the following 54 languages:

    1.	Arabic         (original)
	2.	Albanian
	3.	Amharic
	4.	Azerbaijani
	5.	Bengali
	6.	Bosnian
	7.	Bulgarian
	8.	Burmese
	9.	Chinese
	10.	Danish
	11.	Dutch
	12.	English
	13.	Filipino
	14.	French
	15.	Fulah
	16.	Persian
	17.	German
	18.	Gujarati
	19.	Hausa
	20.	Hindi
	21.	Indonesian
	22.	Italian
	23.	Japanese
	24.	Javanese
	25.	Kazakh
	26.	Khmer
	27.	Korean
	28.	Kurdish
	29.	Kyrgyz
	30.	Malay
	31.	Malayalam
	32.	Norwegian
	33.	Pashto
	34.	Polish
	35.	Portuguese
	36.	Punjabi
	37.	Russian
	38.	Sindhi
	39.	Sinhalese
	40.	Somali
	41.	Spanish
	42.	Swahili
	43.	Swedish
	44.	Tajik
	45.	Tamil
	46.	Tatar
	47.	Telugu
	48.	Thai
	49.	Turkish
	50.	Urdu
	51.	Uyghur
	52.	Uzbek
	53.	Vietnamese
	54.	Yoruba
---

## ⚠️ Missing Translation Entries

While all 6,236 verses are structurally included, **79 translations** were unavailable from the source site ([al-quran.cc](https://www.al-quran.cc/quran-translation/)) at the time of scraping.

These translations are missing in the following `(language, surah, ayah)` combinations:

<details>
<summary>📋 Click to expand full list of missing translations (79)</summary>

01. azerbaijani — al-asr:1
02. azerbaijani — al-asr:2
03. azerbaijani — al-asr:3
04. filipino — al-haaqqa:52
05. german — al-baqara:220
06. german — al-isra:65
07. german — an-naba:3
08. german — ar-rum:5
09. german — az-zamar:40
10. jawa — al-furqan:37
11. kyrgyz — al-mulk:16
12. portuguese — aal-e-imran:50
13. portuguese — aal-e-imran:51
14. portuguese — an-naml:31
15. portuguese — an-naziat:19
16. portuguese — as-saaffat:53
17. portuguese — ash-shuara:17
18. portuguese — nooh:11
19. portuguese — nooh:12
20. portuguese — nooh:13
21. portuguese — nooh:14
22. portuguese — nooh:15
23. portuguese — nooh:16
24. portuguese — nooh:17
25. portuguese — nooh:18
26. portuguese — nooh:19
27. portuguese — nooh:20
28. sindhi — ibrahim:1
29. sindhi — ibrahim:2
30. sindhi — ibrahim:3
31. sindhi — ibrahim:4
32. sindhi — ibrahim:5
33. sindhi — ibrahim:6
34. sindhi — ibrahim:7
35. sindhi — ibrahim:8
36. sindhi — ibrahim:9
37. sindhi — ibrahim:10
38. sindhi — ibrahim:11
39. sindhi — ibrahim:12
40. sindhi — ibrahim:13
41. sindhi — ibrahim:14
42. sindhi — ibrahim:15
43. sindhi — ibrahim:16
44. sindhi — ibrahim:17
45. sindhi — ibrahim:18
46. sindhi — ibrahim:19
47. sindhi — ibrahim:20
48. sindhi — ibrahim:21
49. sindhi — ibrahim:22
50. sindhi — ibrahim:23
51. sindhi — ibrahim:24
52. sindhi — ibrahim:25
53. sindhi — ibrahim:26
54. sindhi — ibrahim:27
55. sindhi — ibrahim:28
56. sindhi — ibrahim:29
57. sindhi — ibrahim:30
58. sindhi — ibrahim:31
59. sindhi — ibrahim:32
60. sindhi — ibrahim:33
61. sindhi — ibrahim:34
62. sindhi — ibrahim:35
63. sindhi — ibrahim:36
64. sindhi — ibrahim:37
65. sindhi — ibrahim:38
66. sindhi — ibrahim:39
67. sindhi — ibrahim:40
68. sindhi — ibrahim:41
69. sindhi — ibrahim:42
70. sindhi — ibrahim:43
71. sindhi — ibrahim:44
72. sindhi — ibrahim:45
73. sindhi — ibrahim:46
74. sindhi — ibrahim:47
75. sindhi — ibrahim:48
76. sindhi — ibrahim:49
77. sindhi — ibrahim:50
78. sindhi — ibrahim:51
79. sindhi — ibrahim:52

</details>

These empty fields are left intentionally blank in the dataset. All ayahs are present in Arabic, and structural alignment is maintained.

---

## 🔍 Data Source and Extraction

- Source: [https://www.al-quran.cc/quran-translation/](https://www.al-quran.cc/quran-translation/)
- Extraction: Python-based HTML parsing with dynamic AJAX handling
- Structural validation: 114 surahs × 6,236 ayahs cross-checked
- Missing translations logged during post-validation

---


## 📜 Linguistic and Literary Significance of the Qur’an

### 🧬 A Living Corpus Preserved in Speech

The Qur’an is the only major historical text that has been **memorized word-for-word by millions of people** across generations, regions, and languages — regardless of whether they spoke Arabic natively.

- Over **1,400 years old**, the Arabic text of the Qur’an remains **unchanged**, **recited daily**, and **actively memorized**, verse by verse.
- It is preserved not only in manuscripts but in **oral transmission**, making it one of the most reliably reconstructed texts in human linguistic history.

### 🌍 Translated into Languages That Weren’t Yet Standardized

Several languages in this dataset — such as **today’s form of Burmese (Myanmar)**, **Swahili**, **Standard Indonesian**, and even **Modern English** — had not yet developed or reached their current standardized written form at the time the Qur’an was first revealed over 1,400 years ago.

Yet today, these communities:
- Study and translate the Qur’an with deep linguistic care
- Retain the **verse structure** in all translations
- Participate in a **global multilingual alignment** with the same source text

This makes the Qur’an a **linguistic anchor** across centuries, preserved in meaning and form across **dozens of linguistic systems**.

### ✍️ Neither Prose Nor Poetry — A Unique Register

From a literary standpoint, the Qur’an’s structure is:
- Not classical prose
- Not traditional poetry
- But a **distinct rhythmic and rhetorical form** known for:
  - Internal rhyme and parallelism
  - Recurring motifs
  - High semantic density and emotional resonance

This genre continues to challenge both literary analysis and computational modeling.

### 🤖 Relevance to AI and Linguistics

The Qur’an is an ideal corpus for AI-based multilingual NLP:

- 🔁 Fully aligned across 53 languages
- 🧩 Rigid source structure (verse-level)
- 🧠 Oral memory transmission modeling
- 🌐 Cross-lingual semantic drift analysis
- 🛠️ Faithful translation alignment tasks

It provides a **fixed point of semantic comparison** for understanding how languages represent meaning — historically and today.

---


## 🪪 License

- Text: Public Domain where applicable (verify by language)
- Code/scripts: MIT License

---

## 📌 Citation

```bibtex
@misc{quran_multilingual_parallel_2025,
  title  = {Qur’an Multilingual Parallel Dataset},
  author = {freococo},
  year   = {2025},
  url    = {https://huggingface.co/datasets/freococo/quran_multilingual_parallel}
}