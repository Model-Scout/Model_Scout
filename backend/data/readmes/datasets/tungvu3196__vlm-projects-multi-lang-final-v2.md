
---
# This is a Dataset Card in YAML format.
language: # Add all your language codes here
 - en
 - vi
 - fr
 - de
 - es
 - ru
 - ko
 - zh
 - ja
 - th
 - id
 - ms
 - ar
 - hi
 - tr
 - pt
task_categories:
- question-answering
- visual-question-answering
# This section defines the different subsets (configurations)
configs:
- config_name: English
  data_files:
  - split: train
    path: data/english/train.parquet
  - split: test
    path: data/english/test.parquet
- config_name: Vietnamese
  data_files:
  - split: train
    path: data/vietnamese/train.parquet
  - split: test
    path: data/vietnamese/test.parquet
- config_name: French
  data_files:
  - split: train
    path: data/french/train.parquet
  - split: test
    path: data/french/test.parquet
- config_name: German
  data_files:
  - split: train
    path: data/german/train.parquet
  - split: test
    path: data/german/test.parquet
- config_name: Spanish
  data_files:
  - split: train
    path: data/spanish/train.parquet
  - split: test
    path: data/spanish/test.parquet
- config_name: Russian
  data_files:
  - split: train
    path: data/russian/train.parquet
  - split: test
    path: data/russian/test.parquet
- config_name: Korean
  data_files:
  - split: train
    path: data/korean/train.parquet
  - split: test
    path: data/korean/test.parquet
- config_name: Mandarin
  data_files:
  - split: train
    path: data/mandarin/train.parquet
  - split: test
    path: data/mandarin/test.parquet
- config_name: Japanese
  data_files:
  - split: train
    path: data/japanese/train.parquet
  - split: test
    path: data/japanese/test.parquet
- config_name: Thai
  data_files:
  - split: train
    path: data/thai/train.parquet
  - split: test
    path: data/thai/test.parquet
- config_name: Indonesian
  data_files:
  - split: train
    path: data/indonesian/train.parquet
  - split: test
    path: data/indonesian/test.parquet
- config_name: Malay
  data_files:
  - split: train
    path: data/malay/train.parquet
  - split: test
    path: data/malay/test.parquet
- config_name: Arabic
  data_files:
  - split: train
    path: data/arabic/train.parquet
  - split: test
    path: data/arabic/test.parquet
- config_name: Hindi
  data_files:
  - split: train
    path: data/hindi/train.parquet
  - split: test
    path: data/hindi/test.parquet
- config_name: Turkish
  data_files:
  - split: train
    path: data/turkish/train.parquet
  - split: test
    path: data/turkish/test.parquet
- config_name: Portuguese
  data_files:
  - split: train
    path: data/portuguese/train.parquet
  - split: test
    path: data/portuguese/test.parquet

# This section provides detailed information for the Dataset Viewer
dataset_info:
  - config_name: English
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Vietnamese
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: French
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: German
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Spanish
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Russian
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Korean
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Mandarin
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Japanese
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Thai
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Indonesian
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Malay
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Arabic
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Hindi
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Turkish
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
  - config_name: Portuguese
    features: 
      - name: No.
        dtype: int64
      - name: Patient ID
        dtype: string
      - name: Slide
        dtype: string
      - name: Deliverable
        dtype: string
      - name: Original
        dtype: string
      - name: Status
        dtype: string
      - name: Remove Status
        dtype: string
      - name: Doctor
        dtype: string
      - name: Start date
        dtype: float64
      - name: Q1
        dtype: string
      - name: A1
        dtype: string
      - name: Q2
        dtype: string
      - name: A2
        dtype: string
      - name: Q3
        dtype: string
      - name: A3
        dtype: string
      - name: Q4
        dtype: string
      - name: A4
        dtype: string
      - name: Notes
        dtype: string
      - name: image
        dtype: image
      - name: image_with_bboxes
        dtype: image
      - name: Google Drive Link
        dtype: string
      - name: rotated_link
        dtype: string

    splits:
      - name: train
        num_examples: 10783
      - name: test
        num_examples: 1542
---

# My Final Multilingual Medical VQA Dataset

This dataset is organized into multiple configurations (subsets), one for each language.
You can load a specific language subset like this:

```python
from datasets import load_dataset

# Load the Vietnamese training data
vi_train = load_dataset("tungvu3196/vlm-projects-multi-lang-final-v2", "Vietnamese", split="train")

# Load the English testing data
en_test = load_dataset("tungvu3196/vlm-projects-multi-lang-final-v2", "English", split="test")