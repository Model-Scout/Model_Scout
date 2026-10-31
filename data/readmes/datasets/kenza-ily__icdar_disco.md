---
task_categories:
- feature-extraction
language:
- ar
- zh
- hi
- ja
- ko
- la
size_categories:
- n<1K
---
# ICDAR_mini Dataset

A balanced mini subset of the ICDAR (International Conference on Document Analysis and Recognition) dataset with 50 samples per language. Includes actual document images and ground truth OCR text.

## Dataset Details

- **Total Samples**: 500
- **Total Images**: 500
- **Languages**: 10
  - Arabic (50 samples)
  - Bangla (50 samples)
  - Chinese (50 samples)
  - Hindi (50 samples)
  - Japanese (50 samples)
  - Korean (50 samples)
  - Latin (50 samples)
  - Mixed (50 samples)
  - None (50 samples)
  - Symbols (50 samples)

## File Structure

```
├── README.md
├── icdar_mini_index.json          # Dataset metadata
├── icdar_mini_Arabic.json         # Language-specific data
├── icdar_mini_Bangla.json
├── ...
└── images/
    ├── tr_img_00001.jpg
    ├── tr_img_00002.jpg
    └── ... (500 image files)
```

Each language subset is stored as a separate JSON file, and corresponding images are in the `images/` directory.

## Data Format

Each sample is a row in the dataset with the following columns:
- `image`: Document image
- `ground_truth`: OCR ground truth text
- `language`: Language of the document (e.g., "Latin", "Arabic", etc.)
- `sample_id`: Unique identifier for the sample

Example sample:
```json
{
  "sample_id": "icdar_tr_img_07848",
  "image_path": "images/tr_img_07848.jpg",
  "ground_truth": "Text content...",
  "metadata": {
    "dataset": "ICDAR",
    "language": "Latin",
    "num_text_lines": 49,
    "image_size": [3264, 2448]
  }
}
```

## Usage

```python
from datasets import load_dataset

# Load the dataset
dataset = load_dataset("kenza-ily/icdar-mini")

# Access a sample
sample = dataset["train"][0]
print(f"Image: {sample['image']}")
print(f"Ground Truth: {sample['ground_truth']}")
print(f"Language: {sample['language']}")
print(f"Sample ID: {sample['sample_id']}")

# Iterate through samples by language
for sample in dataset["train"]:
    if sample['language'] == 'Latin':
        print(f"{sample['sample_id']}: {sample['ground_truth'][:50]}...")
```

## Citation

If you use this dataset, please cite both the original ICDAR 2015 Robust Reading Competition paper and the DISCO paper, which introduces this evaluation subset.
``` bibtex
@inproceedings{karatzas2015icdar,
  title={{ICDAR} 2015 Competition on Robust Reading},
  author={Karatzas, Dimosthenis and Gomez-Bigorda, Lluis and Nicolaou, Anguelos and Ghosh, Suman and Bagdanov, Andrew and Iwamura, Masakazu and Matas, Jiri and Neumann, Lukas and Chandrasekhar, Vijay Ramaseshan and Lu, Shijian and Shafait, Faisal and Uchida, Seiichi and Valveny, Ernest},
  booktitle={2015 13th International Conference on Document Analysis and Recognition (ICDAR)},
  pages={1156--1160},
  year={2015},
  organization={IEEE}
}

@inproceedings{benkirane2026disco,
  title={{DISCO}: Document Intelligence Suite for Comparative Evaluation},
  author={Benkirane, Kenza and Asenov, Martin and Goldwater, Daniel and Ghodsi, Aneiss},
  booktitle={ICLR 2026 Workshop on Multimodal Intelligence},
  year={2026},
  url={arxiv.org/abs/2603.23511}
}
```

## License

This subset follows the original ICDAR dataset license.