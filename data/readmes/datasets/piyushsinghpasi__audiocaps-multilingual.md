---
license: cc-by-nc-4.0
task_categories:
- audio-text-to-text
language:
- en
- bn
- gu
- hi
- kn
- ml
- mr
- ne
- pa
- ta
- te
- ur
- ar
- zh
- cs
- nl
- fr
- de
- el
- he
- id
- it
- ja
- ko
- fa
- pl
- pt
- ro
- ru
- es
- tr
- uk
- vi
---

# AudioCaps Multilingual Evaluation Dataset

## Description

This dataset extends **AudioCaps** with multilingual captions in **33 language variants** (34 caption columns as we have 2 version of translation for Hindi, one from [IndicTrans2](https://github.com/AI4Bharat/IndicTrans2) and other from [AYA](https://huggingface.co/CohereLabs/aya-23-35B)).
Each audio clip is paired with the original English AudioCaps caption and
machine-translated or curated captions in multiple languages.

The dataset is intended primarily for **evaluation and analysis** of multilingual
and cross-lingual audio–text models.

---

## Dataset Structure

- **Audio**: WAV files
- **Metadata**: CSV with one audio clip per row  
  *(Note: each audio clip in AudioCaps is associated with multiple captions; the metadata retains the original identifiers for traceability.)*
- **Languages**: 33 language variants

---

## Columns

- `audio`: 10 second of 32khz Audio file corresponding to the youtube clip
- `caption`: Original English AudioCaps caption
- `<lang_code>`: Caption in the target language (translated)

Language columns where the optional `_AYA` suffix exists denotes captions generated using the [**AYA multilingual model**](https://huggingface.co/CohereLabs/aya-23-35B), otherwise IndicTrans2 is used for Indic languages.

---

## Dataset Statistics

- **Total samples**: 4,785
- **Unique audio clips**: 957 (5 captions per audio)

The original AudioCaps dataset contains **4,875 caption rows** corresponding to **975 unique audio clips**.  
Due to the unavailability of **18 audio files** at the time of dataset construction, audio waveforms for these clips could not be downloaded.

For these missing audio clips:
- The original English captions and all multilingual translations are still available in our github codebase - https://github.com/piyushsinghpasi/M2M/tree/main/Synthetic_Multilingual_Eval_Dataset
- The captions corresponding to missing audio files are omitted from huggingface release

As a result, this release contains **957 audio files** aligned with **4,785 caption entries**.

---

## Language Coverage

The dataset contains captions in **34 language variants**, covering Indic and non-Indic languages.

### Indic languages
Generated using IndicTrans2 

| Language | Common code | Dataset column | Notes |
|--------|------------|----------------|------|
| Bengali | bn | `ben_Beng` | |
| Gujarati | gu | `guj_Gujr` | |
| Hindi | hi | `hin_Deva` | IndicTrans2 generated |
| Hindi | hi | `hin_Deva_AYA` | AYA-generated |
| Kannada | kn | `kan_Knda` | |
| Malayalam | ml | `mal_Mlym` | |
| Marathi | mr | `mar_Deva` | |
| Nepali | ne | `npi_Deva` | |
| Punjabi | pa | `pan_Guru` | |
| Tamil | ta | `tam_Taml` | |
| Telugu | te | `tel_Telu` | |
| Urdu | ur | `urd_Arab` | |

---

### Non-Indic / global languages

| Language | Common code | Dataset column |
|--------|------------|----------------|
| English | en | `caption` |
| Arabic | ar | `arb_Arab_AYA` |
| Chinese (Simplified) | zh-Hans | `zho_Hans_AYA` |
| Chinese (Traditional) | zh-Hant | `zho_Hant_AYA` |
| Czech | cs | `ces_Latn_AYA` |
| Dutch | nl | `nld_Latn_AYA` |
| French | fr | `fra_Latn_AYA` |
| German | de | `deu_Latn_AYA` |
| Greek | el | `ell_Grek_AYA` |
| Hebrew | he | `heb_Hebr_AYA` |
| Indonesian | id | `ind_Latn_AYA` |
| Italian | it | `ita_Latn_AYA` |
| Japanese | ja | `jpn_Jpan_AYA` |
| Korean | ko | `kor_Hang_AYA` |
| Persian | fa | `pes_Arab_AYA` |
| Polish | pl | `pol_Latn_AYA` |
| Portuguese | pt | `por_Latn_AYA` |
| Romanian | ro | `ron_Latn_AYA` |
| Russian | ru | `rus_Cyrl_AYA` |
| Spanish | es | `spa_Latn_AYA` |
| Turkish | tr | `tur_Latn_AYA` |
| Ukrainian | uk | `ukr_Cyrl_AYA` |
| Vietnamese | vi | `vie_Latn_AYA` |

---

## Notes on Language Variants

- All language identifiers use **ISO-639-3** codes with explicit **script tags (ISO-15924)**.
- The `_AYA` suffix denotes captions generated using the **AYA multilingual model**.
- The dataset includes **two Hindi variants** (`hin_Deva` and `hin_Deva_AYA`), `hin_Deva` is used in evaluations by us.

---

## Usage

```python
from datasets import load_dataset

ds = load_dataset("piyushsinghpasi/audiocaps-multilingual", split="test")

sample = ds[0]
audio = sample["audio"]
caption_en = sample["caption"]
caption_hi = sample["hin_Deva"]
caption_fr = sample["fra_Latn_AYA"]
```

---

## License & Citation

We release this data under CC by NC 4.0 as it comply with the original AudioCaps dataset, AYA and IndicTrans2 model licences at the time of data creation Feb 2025 and release Jan 2025. We request users should also independently verify license compliance.


Citation: The data is part of work accepted into EACL 2026. 

```
@inproceedings{pasi-2026-multilingual,
    title = "Multilingual-To-Multimodal ({M}2{M}): Unlocking New Languages with Monolingual Text",
    author = "Pasi, Piyush Singh",
    editor = "Demberg, Vera  and
      Inui, Kentaro  and
      Marquez, Llu{\'i}s",
    booktitle = "Findings of the {A}ssociation for {C}omputational {L}inguistics: {EACL} 2026",
    month = mar,
    year = "2026",
    address = "Rabat, Morocco",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.findings-eacl.143/",
    doi = "10.18653/v1/2026.findings-eacl.143",
    pages = "2750--2771",
    ISBN = "979-8-89176-386-9",
    abstract = "Multimodal models excel in English, supported by abundant image-text and audio-text data, but performance drops sharply for other languages due to limited multilingual multimodal resources. Existing solutions rely on machine translation, while advances in multilingual text modeling remain underutilized. We introduce M2M, a lightweight alignment method that learns only a few linear layers{--}using English text alone{--}to map multilingual text embeddings into multimodal space. Despite its simplicity, M2M matches baseline performance in English (94.9{\%} Recall@10) and achieves strong zero-shot transfer (89.5{\%} Recall@10 averaged across 11 languages, 10 unseen) on XTD Text-to-Image retrieval. Qualitative t-SNE visualizations show that multilingual embeddings align tightly with multimodal representations, while weight analysis reveals that the transformation reshapes embedding geometry rather than performing trivial rotations. Beyond image-text retrieval, M2M demonstrates robustness across datasets and tasks, extending to Audio-Text retrieval and Text-to-Image generation. We release [code and checkpoints](https://github.com/piyushsinghpasi/M2M) along with multilingual evaluation datasets: [MSCOCO Multilingual 30K](https://huggingface.co/datasets/piyushsinghpasi/mscoco-multilingual-30k), [AudioCaps Multilingual](https://huggingface.co/datasets/piyushsinghpasi/audiocaps-multilingual), and [Clotho Multilingual](https://huggingface.co/datasets/piyushsinghpasi/clotho-multilingual)."
}
```