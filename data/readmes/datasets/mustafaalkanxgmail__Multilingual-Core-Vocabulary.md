---
language:
- en
- ar
- ru
- es
- fr
- de
- it
- pt
- ko
- zh
- ja
- hi
- bn
- tr
- id
- sv
- nl
- pl
- vi
license: cc-by-4.0
task_categories:
- translation
- text-classification
tags:
- frequency
- dictionary
- transliteration
- romanization
- pos-tagging
---

# Multilingual Core Vocabulary 🌍

This dataset contains millions of frequency-sorted, highly accurate words across 19 languages. It is designed to be the ultimate resource for building cross-lingual applications, AI similarity agents, and translation models.

## Dataset Structure
This repository contains two variations of the dataset:
* **Massive_Dataset**: Contains over 6 million words. The words were extracted and frequency-sorted from FastText, cleaned from internet noise using official Hunspell dictionaries, translated using Meta's NLLB-600M AI, and Romanized using specialized linguistic libraries.
* **Balanced_Dataset**: Contains highly accurate core vocabulary cross-referenced against Facebook MUSE bilingual dictionaries for perfect 1-to-1 translations.

## Features (Columns)
- `Word`: The original word in its native script.
- `Pronunciation`: Romanized English representation of the phonetic pronunciation (e.g., Pinyin for Chinese, Romaji for Japanese).
- `POS_Tag`: The Universal Part-of-Speech tag (e.g., NOUN, VERB, ADJ) generated using the spaCy English NLP model.
- `Translation`: English meaning of the word.

## Languages Included
Arabic, Russian, Spanish, French, German, Italian, Portuguese, Korean, Chinese, Japanese, Hindi, Bengali, Turkish, Indonesian, Swedish, Dutch, Polish, Vietnamese, and English.

## Pipeline Overview
1. **Extraction**: Top words scraped from Common Crawl / Wikipedia via FastText.
2. **Filtration**: Strict dictionary validation using Linux `Hunspell` (removed 15+ million invalid tokens/emojis).
3. **Translation**: GPU-accelerated translation via Meta's `NLLB-200-distilled-600M`.
4. **Romanization**: Custom phonetic transliteration using `pypinyin`, `pykakasi`, `transliterate`, and `indic-transliteration`.
5. **POS Tagging**: English translations were tagged using `en_core_web_sm` (spaCy) to provide a unified grammatical classification across all languages.
