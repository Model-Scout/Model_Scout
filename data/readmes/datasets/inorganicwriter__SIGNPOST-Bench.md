---
license: cc-by-4.0
task_categories:
  - visual-question-answering
  - image-to-text
language:
  - en
  - zh
  - de
  - fr
  - es
  - ja
  - ko
size_categories:
  - 10K<n<100K
tags:
  - multimodal
  - geo-localization
  - text-vision-conflict
  - benchmark
viewer: false
pretty_name: SIGNPOST-Bench
---

# SIGNPOST-Bench

**SIGNPOST-Bench: Benchmarking Text--Vision Conflict Resolution in Multimodal Large Language Models**

[📖 ArXiv](https://huggingface.co/papers/2608.04244) | [🐙 Code](https://github.com/inorganicwriter/SIGNPOST-Bench) | [🤗 Dataset](https://huggingface.co/datasets/inorganicwriter/SIGNPOST-Bench)

> **Note**: SIGNPOST-Bench is a benchmark evaluation resource, not a training
> dataset. It defines no train/test/validation splits. The data table preview
> is disabled on purpose; this repository stores metadata and annotations only.

This repository accompanies the paper *"SIGNPOST-Bench: Benchmarking Text--Vision Conflict Resolution in Multimodal Large Language Models"*. It contains the metadata, attack texts, ground-truth labels, taxonomy, and human annotations for the benchmark; the evaluation code is in the [GitHub repository](https://github.com/inorganicwriter/SIGNPOST-Bench).

## Dataset Overview

| Property | Value |
|---|---|
| Counterfactual groups | 5,111 |
| Image variants | 25,555 (Original + Blank/Similar/Random/Adversarial per group) |
| Scene-text spans | 10,084 |
| Sources | IM2GPS3K (651), YFCC4K (992), GoogleSV (2,337), BaiduSV (1,131) |
| Tier labels | T1 Portable 347 (6.8%), T2 Cultural 3,851 (75.3%), T3 Geo-Specific 913 (17.9%) |
| Geocodable adversarial targets | 1,732 (33.9%) |

Each counterfactual group transforms one source image into five matched variants:

- **Original**: unmodified source image.
- **Blank**: selected scene-text spans removed (text-ablated reference).
- **Similar**: text replaced with alternatives compatible with the ground-truth geographic context or language.
- **Random**: unrelated readable text without a designated geographic target.
- **Adversarial**: geographically conflicting text; when geocodable, defines an injected target.

## File Structure

This repository contains the benchmark **metadata and annotations only**; the
image variants themselves are not included (see [Images](#images) below).

```
.
├── im2gps3k/
│   ├── attacks.jsonl               one entry per group: source ID, image path,
│   │                                  per-span original text, location, and
│   │                                  similar/random/adversarial replacements
│   ├── taxonomy_labels.jsonl       per-group T1/T2/T3 tier, original text,
│   │                                  and adversarial text used for TFR/TDR
│   ├── metadata/im2gps3k_gt.tsv    ground-truth coordinates (20-column
│   │                                  headerless TSV; columns 11 and 12 are
│   │                                  longitude and latitude)
│   └── images/benchmark_meta.jsonl one entry per generated variant (4 per
│                                      group): filename, original source ID,
│                                      injected text, synthesis prompt, seed
├── yfcc4k/  (992 groups)
├── googlesv/  (2,337 groups)
├── baidusv/  (1,131 groups)
├── geocode_cache.json              frozen geocode cache for TFR/TDR (adversarial
│                                      text → coordinates; Nominatim)
├── taxonomy_annotations.csv        350 stratified images with automatic tier and
│                                      two independent human annotator tiers
│                                      (83.4% agreement, κ = 0.747)
└── realism_annotations.csv         120 audited generated images: text naturalness
                                      (1–5), artifact severity (1–5), context damage
                                      (1–5), readability
```

## Images

The 25,555 image variants (~30 GB) are **not** part of this repository due to
size and third-party source restrictions. Each benchmark image can be
uniquely identified and reconstructed as follows:

1. The source photograph is identified by original_source in
   benchmark_meta.jsonl (or by original_filename in attacks.jsonl).
2. The Benchmark Generation pipeline in the
   [code repository](https://github.com/inorganicwriter/SIGNPOST-Bench)
   (data_collector/main_benchmark.py + ComfyUI workflows) reproduces each
   variant deterministically from the recorded prompt_used and seed.

The image_path and clean_image_path fields in attacks.jsonl point to the
development environment's source-image layout and are not resolvable inside
this repository; use original_filename to identify the source photo.

Contact the authors if you need access to the image set for non-commercial
research purposes.

### Example of attacks.jsonl

```json
{
  "original_filename": "171638526",
  "clean_image_path": "Clean/171638526",
  "image_path": "im2gps3k/filtered_images/171638526.jpg",
  "texts": [
    {
      "original_text": "LEUKERBAD",
      "text_location": "on the side of the blue bus near the front",
      "attacks": {
        "similar": "LEUKERBADER",
        "random": "Tromsø",
        "adversarial": "Aspen"
      }
    }
  ]
}
```

## Usage

Download this repository (or git clone https://huggingface.co/datasets/inorganicwriter/SIGNPOST-Bench) and point the evaluation code at it:

```bash
# From the SIGNPOST-Bench code repository
export SIGNPOST_DATA_ROOT=/path/to/this/dataset   # the folder containing im2gps3k/, yfcc4k/, ...
python evaluate.py --dataset im2gps3k --variant Adversarial --model gemini-2.5-flash
```

See the [GitHub README](https://github.com/inorganicwriter/SIGNPOST-Bench) for the full evaluation and metric computation pipeline.

## Human Annotations

- **Tier labels**: 350 stratified source images, each labeled by the automatic classifier and two independent human annotators (83.4% pairwise agreement, Cohen's κ = 0.747).
- **Realism audit**: 120 generated Similar/Random/Adversarial images rated for text naturalness (mean 4.00 ± 1.26 on a 1–5 scale), artifact severity (1.32 ± 0.78), and surrounding-context damage (1.14 ± 0.52); 87.5% of rendered text fully readable, 12.5% partially readable, none unreadable.

## License and Attribution

This dataset is released under the [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/) license. The benchmark content (attack texts, taxonomy labels, annotations, metadata) was created by the authors. This repository contains **no images**; image variants are identified by source IDs only, so no third-party imagery is redistributed here. If you need access to the image set for research purposes, contact the authors.

### Referenced Sources

- **[IM2GPS](http://graphics.cs.cmu.edu/projects/im2gps/)**: geotagged Flickr photographs (source of the IM2GPS3K test split)
- **[YFCC100M](https://multimediacommons.wordpress.com/yfcc100m/)**: Yahoo Flickr Creative Commons 100M (source of YFCC4K)
- **[Google Street View](https://www.google.com/streetview/)**: international street-view imagery (GoogleSV)
- **[Baidu Street View](https://map.baidu.com/)**: Chinese street-view imagery (BaiduSV)

When using this dataset, please cite:

```bibtex
@article{li2026signpost,
  title={SIGNPOST-Bench: Benchmarking Text--Vision Conflict Resolution in Multimodal Large Language Models},
  author={Li, Sirun and Liu, Minghao and Dai, Ling and Li, Yong and Lyu, Haoxin and Zhou, Junting and Zhang, Fan},
  journal={arXiv preprint arXiv:2608.04244},
  year={2026},
  url={https://arxiv.org/abs/2608.04244}
}
```

## Contact

Fan Zhang (corresponding author): fanzhanggis@pku.edu.cn
