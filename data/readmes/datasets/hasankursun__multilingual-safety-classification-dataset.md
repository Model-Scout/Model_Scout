---
language:
- multilingual
- am
- bn
- bs
- bg
- ceb
- cs
- de
- en
- fr
- gu
- ha
- hi
- hr
- hu
- id
- it
- ja
- kn
- kk
- km
- rw
- ko
- lg
- ml
- mr
- mi
- my
- nl
- nso
- ny
- fa
- pl
- pt
- ro
- ru
- si
- sl
- sn
- sd
- so
- st
- es
- sr
- ta
- tt
- te
- th
- tn
- ts
- tr
- ug
- uk
- ur
- uz
- vi
- wo
- yo
- zh
- zu
license: cc-by-nc-sa-4.0
task_categories:
- text-classification
tags:
- safety
- content-moderation
- multilingual
- machine-translation
size_categories:
- 100K<n<1M
---

# Multilingual Safety Classification Dataset

A multilingual dataset for safety classification across 60 languages, created by **Hasan Kurşun** through machine translation of English safety prompts using NLLB-200-3.3B.

## Dataset Details

**Processed by:** Hasan Kurşun  
**Author:** Hasan Kurşun  
**Year:** 2025  
**Source Dataset:** [mvrcii/safety-moderation-benchmark](https://huggingface.co/datasets/mvrcii/safety-moderation-benchmark)  
**Translation Model:** facebook/nllb-200-3.3B

### Languages (60)

**African Languages (16):** Amharic, Hausa, Kinyarwanda, Luganda, Northern Sotho, Nyanja, Shona, Somali, Southern Sotho, Swahili (implied via tsn/tso), Tswana, Tsonga, Wolof, Yoruba, Zulu

**Asian Languages (24):** Bengali, Gujarati, Hindi, Indonesian, Japanese, Kannada, Kazakh, Khmer, Korean, Malayalam, Marathi, Burmese, Persian, Sinhala, Sindhi, Tamil, Telugu, Thai, Turkish, Uyghur, Urdu, Uzbek, Vietnamese, Chinese (Simplified & Traditional)

**European Languages (19):** Bosnian, Bulgarian, Czech, German, English, French, Croatian, Hungarian, Italian, Dutch, Polish, Portuguese, Romanian, Russian, Slovenian, Spanish, Serbian, Tatar, Ukrainian

**Oceanic Languages (1):** Māori

### Dataset Structure

Each split contains JSONL files with the following schema:

```json
{
  "prompt": "translated safety-related text",
  "safety_label": 0,  // 0=safe, 1=needs review, 2=unsafe
  "lang": "spa_Latn"  // BCP-47 style language code with script
}

```

### Data Splits

* **Train:** ~80% of data per language
* **Test:** ~20% of data per language
* Each language maintains stratified splits by `safety_label`

## Dataset Creation

### Source Data

This dataset is derived from [mvrcii/safety-moderation-benchmark](https://huggingface.co/datasets/mvrcii/safety-moderation-benchmark), which provides high-quality English safety prompts across various risk categories.

### Translation Process

1. **Source:** English safety prompts from mvrcii/safety-moderation-benchmark
2. **Model:** `facebook/nllb-200-3.3B` (No Language Left Behind)
3. **Method:**
* Random language assignment to ensure distribution
* Batch translation (batch_size=32)
* BFloat16 precision on GPU
* Confidence scoring for quality assessment


4. **Quality Control:** Languages with poor translation quality were removed

### Safety Labels

* **Label 0 (Safe):** Content that poses no safety concerns
* **Label 1 (Needs Review):** Ambiguous content requiring human judgment
* **Label 2 (Unsafe):** Content violating safety guidelines

## Intended Use

### Primary Uses

* Training multilingual content moderation models
* Cross-lingual safety classification research
* Evaluating model performance across diverse languages
* Low-resource language safety research

### Out-of-Scope

* This dataset should not be the sole basis for production moderation systems
* Translations may contain artifacts; human review recommended for critical applications
* Not suitable for languages outside the 60 included

## Limitations

1. **Machine Translation Artifacts:** Some nuance may be lost in translation
2. **Label Distribution:** May not reflect real-world safety content ratios
3. **Cultural Context:** Safety norms vary by culture; labels reflect English-centric perspective
4. **Script Representation:** Uses specific scripts (e.g., `zho_Hans` vs `zho_Hant`)

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{kursun_multilingual_safety_2025,
  title={Multilingual Safety Classification Dataset},
  author={Kurşun, Hasan},
  year={2025},
  url={[https://huggingface.co/datasets/hasankursun/multilingual-safety-classification](https://huggingface.co/datasets/hasankursun/multilingual-safety-classification)},
  note={60 languages, translated from mvrcii/safety-moderation-benchmark using NLLB-200-3.3B}
}

```

Please also cite the original source dataset:

```bibtex
@dataset{mvrcii_safety_moderation,
  title={Safety Moderation Benchmark},
  author={mvrcii},
  publisher={HuggingFace},
  url={[https://huggingface.co/datasets/mvrcii/safety-moderation-benchmark](https://huggingface.co/datasets/mvrcii/safety-moderation-benchmark)}
}

```

## Dataset Statistics

* **Total Languages:** 60
* **Language Families:** ~15 (Niger-Congo, Indo-European, Sino-Tibetan, Afro-Asiatic, etc.)
* **Scripts:** Latin, Cyrillic, Arabic, Devanagari, Bengali, Gujarati, Kannada, Malayalam, Tamil, Telugu, Ethiopic, Thai, Khmer, Burmese, Sinhala, CJK, Korean
* **Total Samples:** Varies by language (check individual splits)

## Ethical Considerations

* Dataset contains content labeled as "unsafe" for training purposes
* Researchers should handle unsafe content responsibly
* Cultural context of "safety" may differ across regions
* Not all 7000+ world languages are represented

## Acknowledgments

* **mvrcii:** For the original safety-moderation-benchmark dataset
* **NLLB Team (Meta AI):** For the powerful multilingual translation model

## Contact

For questions or issues regarding this dataset:

* **Author:** Hasan KURŞUN

```

```