---
pretty_name: "M-PEDES: A Multilingual Benchmark for Text-Based Person Retrieval"
language:
- ar
- de
- es
- fr
- ja
- ko
- ru
- zh
license: other
license_name: m-pedes-research-only-license-v1.0
annotations_creators:
- machine-generated
language_creators:
- machine-generated
multilinguality:
- translation
source_datasets:
- extended
tags:
- multilingual
- text
- text-based-person-retrieval
- person-re-identification
- cross-modal-retrieval
- evaluation
configs:
- config_name: cuhk-pedes-ar
  data_files:
  - split: test
    path: data/CUHK-PEDES_ar.json

- config_name: cuhk-pedes-de
  data_files:
  - split: test
    path: data/CUHK-PEDES_de.json

- config_name: cuhk-pedes-es
  data_files:
  - split: test
    path: data/CUHK-PEDES_es.json

- config_name: cuhk-pedes-fr
  data_files:
  - split: test
    path: data/CUHK-PEDES_fr.json

- config_name: cuhk-pedes-ja
  data_files:
  - split: test
    path: data/CUHK-PEDES_ja.json

- config_name: cuhk-pedes-ko
  data_files:
  - split: test
    path: data/CUHK-PEDES_ko.json

- config_name: cuhk-pedes-ru
  data_files:
  - split: test
    path: data/CUHK-PEDES_ru.json

- config_name: cuhk-pedes-zh
  default: true
  data_files:
  - split: test
    path: data/CUHK-PEDES_zh.json

- config_name: icfg-pedes-ar
  data_files:
  - split: test
    path: data/ICFG-PEDES_ar.json

- config_name: icfg-pedes-de
  data_files:
  - split: test
    path: data/ICFG-PEDES_de.json

- config_name: icfg-pedes-es
  data_files:
  - split: test
    path: data/ICFG-PEDES_es.json

- config_name: icfg-pedes-fr
  data_files:
  - split: test
    path: data/ICFG-PEDES_fr.json

- config_name: icfg-pedes-ja
  data_files:
  - split: test
    path: data/ICFG-PEDES_ja.json

- config_name: icfg-pedes-ko
  data_files:
  - split: test
    path: data/ICFG-PEDES_ko.json

- config_name: icfg-pedes-ru
  data_files:
  - split: test
    path: data/ICFG-PEDES_ru.json

- config_name: icfg-pedes-zh
  data_files:
  - split: test
    path: data/ICFG-PEDES_zh.json

- config_name: rstpreid-ar
  data_files:
  - split: test
    path: data/RSTPReid_ar.json

- config_name: rstpreid-de
  data_files:
  - split: test
    path: data/RSTPReid_de.json

- config_name: rstpreid-es
  data_files:
  - split: test
    path: data/RSTPReid_es.json

- config_name: rstpreid-fr
  data_files:
  - split: test
    path: data/RSTPReid_fr.json

- config_name: rstpreid-ja
  data_files:
  - split: test
    path: data/RSTPReid_ja.json

- config_name: rstpreid-ko
  data_files:
  - split: test
    path: data/RSTPReid_ko.json

- config_name: rstpreid-ru
  data_files:
  - split: test
    path: data/RSTPReid_ru.json

- config_name: rstpreid-zh
  data_files:
  - split: test
    path: data/RSTPReid_zh.json
---

# M-PEDES

M-PEDES is an evaluation-only benchmark for **multilingual text-based
person retrieval (M-TBPR)**. It extends the test sets of
[CUHK-PEDES](https://doi.org/10.1109/CVPR.2017.551),
[ICFG-PEDES](https://github.com/zifyloo/SSAN), and
[RSTPReid](https://doi.org/10.1145/3474085.3475369) from English to
Arabic, German, Spanish, French, Japanese, Korean, Russian, and Chinese.

The repository contains translated annotations only. It does **not**
include training data, original English captions, or original
pedestrian images.

## Dataset Summary

| Source dataset | Queries per language | Target languages |
|---|---:|---:|
| CUHK-PEDES | 6,156 | 8 |
| ICFG-PEDES | 19,848 | 8 |
| RSTPReid | 2,000 | 8 |
| **Total** | **28,004** | **8** |

In total, M-PEDES contains **224,032 translated queries**. The
translations were generated with GPT-5.2 using retrieval-aware prompts
that emphasize the preservation of fine-grained visual attributes. A
10% stratified sample was manually audited. Across the full benchmark,
the average cross-lingual semantic similarity is 0.891, back-translation
BLEU is 29.6, and attribute preservation is 97.6%. Full construction,
quality-control, and evaluation details are provided in the accompanying
paper.

## Data Format

Each configuration follows `{source-dataset}-{language}` and contains
one `test` split. For example, `cuhk-pedes-zh` provides:

```json
{
  "id": 12004,
  "file_path": "train_query/p8848_s17661.jpg",
  "caption_idx": 0,
  "caption_zh": "一个穿着蓝白条纹背心、绿色裤子和粉色鞋子的男人。"
}
```

`caption_XX` denotes the translated description, where `XX` is the
target-language code.

## Usage

```python
from datasets import load_dataset

dataset = load_dataset(
    "younght/MPEDES",
    "cuhk-pedes-zh",
    split="test",
)
print(dataset[0])
```

Users must obtain the corresponding source images from the original
dataset providers and resolve each record's `file_path` relative to the
appropriate dataset root.

## Intended Use

M-PEDES is intended for evaluating multilingual and cross-lingual
text-based person retrieval. Results should be reported separately for
each source dataset and language using the evaluation protocol described
in the accompanying paper.

## Limitations and License

The captions are machine-generated translations and may retain noise or
ambiguity from the original English annotations.

The multilingual translations and original documentation are released
under the [M-PEDES Research-Only License v1.0](LICENSE) for
non-commercial academic research and educational use. Source images,
English captions, identifiers, paths, and other upstream materials are
not licensed by M-PEDES and remain subject to their original terms.
Users must obtain the source datasets independently from their official
providers.

## Citation

If you use M-PEDES in your research, please cite:

```bibtex
@inproceedings{yang2026gram,
  author    = {Yang, Haotian and Peng, Cheng and Wang, Haobo and Zhu, Zhen and Tang, Xiu and Yuan, Gongsheng and Xie, Zhongle and Wu, Sai and Wang, Weiqiang and Cheng, Yu},
  title     = {Beyond Contrastive: Generative Reranking for Multilingual Text-Based Person Retrieval},
  booktitle = {Proceedings of the 34th ACM International Conference on Multimedia},
  series    = {MM '26},
  year      = {2026},
  month     = nov,
  location  = {Rio de Janeiro, Brazil},
  doi       = {10.1145/3767308.3835886},
  isbn      = {979-8-4007-2213-4/2026/11},
  publisher = {Association for Computing Machinery},
  license   = {CC BY 4.0}
}
```

Please also cite the original CUHK-PEDES, ICFG-PEDES, and RSTPReid
papers.
