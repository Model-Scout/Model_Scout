---
annotations_creators:
- other
language:
- ko
language_creators:
- other
license:
- apache-2.0
multilinguality:
- multilingual
pretty_name: Korean wikipedia dataset for GPT-2 training
size_categories:
- 100M<n<1B
source_datasets: []
tags:
- gpt2
- korean
- wikipedia
- pertained
task_categories:
- question-answering
- text2text-generation
- translation
- visual-question-answering
task_ids:
- open-domain-qa
- closed-domain-qa
- closed-domain-qa
- dialogue-generation
- visual-question-answering

viewer: true

---

# Dataset Card for korean_wikipedia_dataset_for_GPT2

## Table of Contents
- [Table of Contents](#table-of-contents) 
- [Dataset Description](#dataset-description) 
  - [Dataset Summary](#dataset-summary)
  - [Languages](#languages) 
- [Dataset Structure](#dataset-structure) 
  - [Data Instances](#data-instances) 
  - [Data Fields](#data-fields) 
  - [Data Splits](#data-splits) 
- [Dataset Creation](#dataset-creation)
  - [Source Data](#source-data)
- [Considerations for Using the Data](#considerations-for-using-the-data) 
  - [Social Impact of Dataset](#social-impact-of-dataset) 
  - [Discussion of Biases](#discussion-of-biases) 
  - [Other Known Limitations](#other-known-limitations) 
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators) 
  - [Contributions](#contributions)

## Dataset Description

Entire Korean language Wikipedia data for GPT-2 training as of August 1st, 2022.

email: oscar.eaglewatch@gmail.com

### Dataset Summary

This is to make a pre-trained GPT-2 Korean model

### Languages

Korean

## Dataset Structure

### Data Instances

Train wikipedia article count: 334420

validation wikipedia article count: 83605

### Data Fields

'text'

### Data Splits

80% vs. 20%, randomly, according to the Pareto Principle.

## Dataset Creation

### Source Data

Wikipedia
https://dumps.wikimedia.org/kowiki/latest/kowiki-latest-pages-articles.xml.bz2

## Considerations for Using the Data

### Social Impact of Dataset

None

### Discussion of Biases

None

### Other Known Limitations

None

## Additional Information

### Dataset Curators

Yongwoo Jeong

