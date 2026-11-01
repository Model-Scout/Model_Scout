---
license: odc-by
pretty_name: OpenSubtitles2024 multi-aligned 40-langs 15-movies
task_categories:
- translation
language:
- ar
- bg
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fr
- he
- hi
- hr
- hu
- id
- it
- ko
- lt
- lv
- ms
- nl
- 'no'
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- ta
- te
- tr
- uk
- vi
- zh
language_bcp47:
- pt-BR
- zh-CN
- zh-TW
dataset_info:
  features:
  - name: id
    dtype: string
  - name: movie_id
    dtype: string
  - name: segment_id
    dtype: int32
  - name: translation
    struct:
    - name: ar
      dtype: string
    - name: bg
      dtype: string
    - name: cs
      dtype: string
    - name: da
      dtype: string
    - name: de
      dtype: string
    - name: el
      dtype: string
    - name: en
      dtype: string
    - name: es
      dtype: string
    - name: et
      dtype: string
    - name: fa
      dtype: string
    - name: fi
      dtype: string
    - name: fr
      dtype: string
    - name: he
      dtype: string
    - name: hi
      dtype: string
    - name: hr
      dtype: string
    - name: hu
      dtype: string
    - name: id
      dtype: string
    - name: it
      dtype: string
    - name: ko
      dtype: string
    - name: lt
      dtype: string
    - name: lv
      dtype: string
    - name: ms
      dtype: string
    - name: nl
      dtype: string
    - name: 'no'
      dtype: string
    - name: pl
      dtype: string
    - name: pt
      dtype: string
    - name: pt_BR
      dtype: string
    - name: ro
      dtype: string
    - name: ru
      dtype: string
    - name: sk
      dtype: string
    - name: sl
      dtype: string
    - name: sr
      dtype: string
    - name: sv
      dtype: string
    - name: ta
      dtype: string
    - name: te
      dtype: string
    - name: tr
      dtype: string
    - name: uk
      dtype: string
    - name: vi
      dtype: string
    - name: zh_CN
      dtype: string
    - name: zh_TW
      dtype: string
  splits:
  - name: devtest
    num_bytes: 15480860
    num_examples: 6005
  download_size: 15187620
  dataset_size: 15480860
configs:
- config_name: default
  data_files:
  - split: devtest
    path: data/devtest-*
---

# Dataset Summary

This dataset is a **multi-parallel evaluation subset** derived from the OpenSubtitles2024 corpus.  
It contains **synchronized subtitle segments from 15 movies / TV episodes aligned across 40 languages**, enabling multilingual and multi-target machine translation evaluation.

The dataset is part of the held-out benchmark released with *OpenSubtitles2024* and is designed for **evaluation and development of multilingual machine translation systems and multilingual language models**.

Unlike standard bilingual test sets, all translations in this dataset correspond to the **same subtitle segments across all languages**, forming a fully multi-parallel structure.

Key properties:

- **Languages:** 40  
- **Movies / episodes:** 15  
- **Alignment:** synchronized multi-parallel subtitle segments  
- **Primary use:** multilingual MT evaluation

## Dataset Description

### Source

The data originates from community-contributed subtitles available on **OpenSubtitles.org** and distributed through the **OPUS** corpus collection.

Subtitles from multiple languages for the same movie or TV episode were aligned using timestamp overlap signals between subtitle segments. Alignment quality was estimated using alignment density scores and temporal overlap metrics.

### Multi-parallel Benchmark Construction

The multi-parallel benchmark was constructed through the following steps:

1. Identify subtitle collections where multiple languages exist for the same movie or episode.
2. Build a connected alignment graph linking subtitle files across languages.
3. Select pivot languages that maximize alignment quality and coverage.
4. Synchronize sentence alignments across all languages by merging pairwise alignments.

To ensure high quality, only subtitle pairs with **alignment density ≥ 0.9** were considered.  
The final benchmark contains **40 languages aligned across 15 movies**, providing a balanced trade-off between language coverage and dataset size.

### Intended Uses

The dataset is primarily intended for multilingual machine translation evaluation. Because all languages share the same underlying subtitle segments, the dataset is particularly useful for **multi-parallel evaluation settings**.

**Please note that, this dataset is intended strictly for evaluation and benchmarking purposes. Training models on this dataset, or including it in automatically collected web-scale training corpora, may lead to benchmark contamination and invalidate evaluation results.**

## Dataset Structure

Each record corresponds to a single aligned subtitle segment.

### Data Fields

- `id`: string  
  Unique identifier of the subtitle segment.

- `movie_id`: string  
  Identifier of the movie or episode from which the subtitle segment originates.

- `segment_id`: int32  
  Segment index within the movie.

- `translation`: dict  
  A dictionary mapping language codes to subtitle text.

Example:

```json
{
  "id": "29342064_19395018_1_4:000010",
  "movie_id": "29342064_19395018_1_4",
  "segment_id": 10,
  "translation": {
    "en": "Where are you going?",
    "fi": "Minne olet menossa?",
    "es": "¿Adónde vas?",
    ...
  }
}
````

## Splits

| Split     | Description                                                                                   |
| --------- | --------------------------------------------------------------------------------------------- |
| `devtest` | Multi-parallel evaluation set consisting of subtitle segments aligned across all 40 languages |

## Dataset Creation

### Alignment Method

Subtitle alignment relies primarily on **temporal overlap between subtitle timestamps**.
A dynamic programming algorithm maximizes overlap between subtitle segments across languages.

Additional procedures include:

* language identification using a modern language detection model
* subtitle normalization and segmentation
* synchronization of misaligned subtitles using lexical anchor points
* filtering based on alignment density and duration ratio

These steps help mitigate noise common in user-contributed subtitle data. 

### Quality Filtering

Several filtering criteria were applied:

* alignment density threshold (≥ 0.9 for the multilingual benchmark)
* minimum subtitle duration ratio
* removal of corrupted or incomplete subtitle files

## Limitations

Users should be aware of several limitations:

* **Noise and inconsistencies:** Subtitles may contain translation errors or stylistic variations.
* **Informal domain:** The data reflects conversational movie dialogue and may not generalize to formal text domains.
* **Segment alignment variability:** Subtitle segmentation may differ across languages, which can introduce minor inconsistencies.

## Licensing

This dataset is released under the **ODC-BY license**.
The dataset redistributes subtitle texts originally contributed to OpenSubtitles.org.
The authors do not claim ownership of the subtitle content and maintain a takedown policy for copyright holders. 

## Citation

If you use this dataset, please cite:

```
@inproceedings{tiedemann-luo-2026-opensubtitles2024,
  title={OpenSubtitles2024: A Massively Parallel Dataset of Movie Subtitles for MT Development and Evaluation},
  author={Tiedemann, Jörg and Luo, Hengyu},
  booktitle={Proceedings of the 15th edition of the Language Resources and Evaluation Conference (LREC 2026)},
  year={2026}
}
```

## Acknowledgements

This work was supported by the European Union's Horizon Europe research and innovation programme under grant agreement No 101070350, by the OpenEuroLLM project, co-funded by the Digital Europe Programme under GA no. 101195233, and by the AI-DOC program hosted at the Finnish Center of Artificial Intelligence (decision number VN/3137/2024-OKM-6). The authors wish to also thank CSC - IT Center for Science, Finland,  and LUMI supercomputers, owned by the EuroHPC Joint Undertaking, for providing computational resources.