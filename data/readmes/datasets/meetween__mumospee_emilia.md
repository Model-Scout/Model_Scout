---
license: cc-by-nc-4.0
language:
- en
- zh
- ja
- de
- fr
- ko
---

### Dataset Summary

This dataset is a modified version of the [Emilia](https://huggingface.co/datasets/amphion/Emilia-Dataset) corpus, converted into parquet format to facilitate optimized I/O operations in high-performance and distributed computing environments.
The Emilia dataset is a comprehensive, multilingual dataset with the following features:

- containing over 101k hours of speech data;
- covering six different languages: English (En), Chinese (Zh), German (De), French (Fr), Japanese (Ja), and Korean (Ko);
- containing diverse speech data with various speaking styles from diverse video platforms and podcasts on the Internet, covering various content genres such as talk shows, interviews, debates, sports commentary, and audiobooks.

This release covers the **core Emilia** corpus (the six languages above); the separate Emilia-YODAS collection is not included. Both the audio shards and the segment metadata are kept aligned, so every metadata row points to a shard present in this repository.

---

### Source Data

- **Original Dataset**: [Emilia](https://huggingface.co/datasets/amphion/Emilia-Dataset)
- **License**: This derived dataset is shared under the same license (CC-BY-NC-4.0), with modifications only to format for efficiency.

### Modifications

- **Data Format**: Converted from the original WebDataset `.tar` archives to parquet format to enhance I/O performance for distributed training, reducing latency during data loading and retrieval.
- **Efficiency Optimization**: Restructured for reduced storage footprint and faster I/O on high-performance clusters by leveraging parquet’s efficient compression and columnar storage.
- **Scope**: Restricted to the six core Emilia languages (de, en, fr, ja, ko, zh), so the audio and metadata folders stay aligned.

### Dataset Structure

- **File Format**: Parquet files.
- **Languages**: 6 languages (de, en, fr, ja, ko, zh).
- **Audio Sampling Rate**: 24 kHz, MP3 encoded.

The repository contains two top-level folders:

#### `emilia-parquet/` — segment audio + per-segment fields

Sharded per language at `emilia-parquet/{lang}/{LANG}-B{nnnnnn}.tar.parquet` (one converted parquet per original Emilia `.tar`). Each row is one utterance-level segment with its MP3 audio embedded; a language's segments are striped across that language's shards.

| column          | type                                            | description                                                       |
| --------------- | ----------------------------------------------- | ----------------------------------------------------------------- |
| `__key__`       | string                                          | sample id, e.g. `EN_B00000_S00000_W000000`                        |
| `__url__`       | string                                          | provenance: source tar in `amphion/Emilia-Dataset`                |
| `mp3`           | struct<`array`: binary, `path`: string, `sampling_rate`: int64> | `array` = raw MP3 bytes, `path` = `<key>.mp3`, `sampling_rate` = 24000 |
| `dnsmos`        | double                                          | DNSMOS P.835 OVRL audio-quality score                             |
| `duration`      | double                                          | segment duration in seconds                                       |
| `id`            | string                                          | sample id (same as `__key__`)                                     |
| `language`      | string                                          | language code                                                     |
| `speaker`       | string                                          | speaker / session id, e.g. `EN_B00000_S00000`                     |
| `text`          | string                                          | transcript                                                        |
| `wav`           | string                                          | relative segment path, e.g. `EN_B00000/EN_B00000_S00000/mp3/EN_B00000_S00000_W000000.mp3` |

#### `metadata/` — per-segment metadata

One file per language at `metadata/emilia_<LANG>.parquet`. Each row is one Emilia segment.

| column       | type    | description                                                            |
| ------------ | ------- | ---------------------------------------------------------------------- |
| `path`       | string  | segment path (matches the `wav` field of the audio shard)              |
| `url`        | string  | URL of the `emilia-parquet/` shard that holds this segment's audio     |
| `type`       | string  | constant `"audio"`                                                     |
| `duration`   | float64 | segment duration in seconds                                            |
| `language`   | string  | language code                                                          |
| `transcript` | string  | transcript                                                            |
| `tag`        | string  | constant `"Emilia"`                                                   |
| `split`      | string  | constant `"train"`                                                    |
| `license`    | string  | constant `"CC-BY-NC-4.0"`                                             |

Totals: 40,237,814 segments across 6 languages, ~101,585 hours of audio, in 2,360 audio shards (~2.45 TB).

### Statistics

**Overall**

- 6 languages, 40,237,814 segments, **~101,585 hours** of audio.
- 2,360 audio shards (~2.45 TB), MP3 at 24 kHz.
- Average segment duration: **9.09 s**.
- Chinese (zh) and English (en) dominate (~49 % and ~46 % of hours); de, fr, ja, ko together make up under 5 %.

**Per language**

| lang | rows         | hours      | shards | audio size | avg segment (s) | % hours |
| ---- | -----------: | ---------: | -----: | ---------: | --------------: | ------: |
| de   |      653,109 |    1,590.5 |     90 |    35.1 GB |            8.77 |  1.57 % |
| en   |   18,109,854 |   46,757.7 |  1,140 |  1085.2 GB |            9.29 | 46.03 % |
| fr   |      543,710 |    1,381.7 |    100 |    60.5 GB |            9.15 |  1.36 % |
| ja   |      869,662 |    1,715.5 |     70 |    81.0 GB |            7.10 |  1.69 % |
| ko   |       92,182 |      217.2 |     40 |     4.7 GB |            8.48 |  0.21 % |
| zh   |   19,969,297 |   49,922.5 |    920 |  1186.1 GB |            9.00 | 49.14 % |
| **total** | **40,237,814** | **101,585.1** | **2,360** | **~2.45 TB** | **9.09** | **100 %** |

### Usage

This dataset is ideal for use in large-scale multilingual speech-to-text and text-to-speech tasks, especially in distributed and high-performance computing environments. The parquet format enhances usability by minimizing I/O overhead, making it well-suited for high-throughput training.

### Attribution

This dataset is based on the original [Emilia](https://huggingface.co/datasets/amphion/Emilia-Dataset) dataset, with modifications for I/O optimization by converting to parquet format. Please cite the original Emilia dataset in any publications or projects using this dataset.

### Changelog

#### Version 1.1 (2026-06-25)

- Recovered the 62 missing Japanese shards (Ja was previously 8/70); `ja/` is now complete at 70 shards, rebuilt from `amphion/Emilia-Dataset`.
- Rebuilt 4 corrupt English shards (`EN-B000160`, `EN-B000370`, `EN-B000501`, `EN-B001100`) that had unreadable parquet footers.
- Renamed the English audio folder `english/` → `en/` so it matches the other languages and the metadata URLs.
- Replaced the per-language CSV metadata with regenerated parquet metadata, sourced directly from the audio shards: corrected per-row download `url`s, clean UTF-8 transcripts, `duration` stored as `float64`, and a fixed `license` value of `CC-BY-NC-4.0`.

### Citation

```bibtex
@inproceedings{emilia,
    author={He, Haorui and Shang, Zengqiang and Wang, Chaoren and Li, Xuyuan and Gu, Yicheng and Hua, Hua and Liu, Liwei and Yang, Chen and Li, Jiaqi and Shi, Peiyang and Wang, Yuancheng and Chen, Kai and Zhang, Pengyuan and Wu, Zhizheng},
    title={Emilia: An Extensive, Multilingual, and Diverse Speech Dataset for Large-Scale Speech Generation},
    booktitle={Proc.~of SLT},
    year={2024}
}

@inproceedings{emilialarge,
    author={He, Haorui and Shang, Zengqiang and Wang, Chaoren and Li, Xuyuan and Gu, Yicheng and Hua, Hua and Liu, Liwei and Yang, Chen and Li, Jiaqi and Shi, Peiyang and Wang, Yuancheng and Chen, Kai and Zhang, Pengyuan and Wu, Zhizheng},
    title={Emilia: A Large-Scale, Extensive, Multilingual, and Diverse Dataset for Speech Generation},
    booktitle={arXiv:2501.15907},
    year={2025}
}
```
