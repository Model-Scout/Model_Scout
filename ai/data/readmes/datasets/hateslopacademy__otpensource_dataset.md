---
datasets:
- hateslopacademy/otpensource_dataset
tags:
- fashion
- clothing
- e-commerce
- image-to-text
- korean
license: cc-by-4.0
language:
- ko
- en
size_categories: 1K<n<10K
task_categories:
- image-to-text
- text-classification
task_ids:
- image-captioning
- sentiment-analysis
---



# Dataset Card for otpensource_dataset

This dataset contains curated information about fashion items, focusing on various categories, subcategories, genders, seasons, and unique features. It is intended for use in AI applications related to fashion recommendation systems, trend analysis, and image-to-text generation.

## Dataset Details

### Dataset Description


This dataset includes 8,998 examples of Korean Mushinsa fashion data, each with detailed attributes such as `category`, `gender`, `season`, `color`, `material`, and more. Each entry also includes an image URL linking to the item's image. The dataset was collected through web crawling and manually curated to ensure data quality.

- **Curated by:** Hateslop Academy otpensource team.
- **Language(s) (NLP):** Korean, English
- **License:** Creative Commons Attribution 4.0 International

### Dataset Sources

- **Repository:** [Hugging Face Dataset Repository](https://huggingface.co/datasets/hateslopacademy/otpensource_data)

## Uses

```bibtex
dataset = load_dataset('hateslopacademy/otpensource_dataset', split='train')
```

### Direct Use

This dataset is intended for:
- Fashion recommendation systems.
- AI-driven cataloging of fashion items.
- Training image-to-text generation models.
- NLP-based trend analysis for the fashion industry.

### Out-of-Scope Use


- Misuse in generating fake or misleading fashion descriptions.
- Applications requiring highly detailed material specifications or custom measurements.

## Dataset Structure

Each dataset entry includes the following fields:
- `big_category`: High-level fashion category (e.g., Outerwear, Tops).
- `sub_category`: More specific category (e.g., Trench Coat, Hoodie).
- `gender`: Target gender for the item (e.g., Male, Female, Unisex).
- `season`: Seasonal applicability (e.g., SS, FW).
- `product_name`: Name of the product.
- `color`: Primary color of the item.
- `material`: Material used for the item (if available).
- `feature`: Unique features or descriptions (e.g., Slim Fit, Floral Print).
- `image_url`: URL linking to the image of the product.

## Dataset Creation

### Source Data

<무신사>
https://www.musinsa.com

#### Data Collection and Processing

Data was collected from 무신사(Mushinsa) website. Each entry was manually curated to ensure accuracy and consistency in labeling. Tools like BeautifulSoup, Selenium, and custom Python scripts were used for data extraction.


## Bias, Risks, and Limitations

- The dataset is limited to publicly available information and may not represent all cultural contexts.
- Certain categories or styles may be underrepresented due to data availability.

### Recommendations

Users should be cautious about biases in the dataset, such as overrepresentation of specific styles or brands.

**BibTeX:**

```bibtex
@dataset{otpensource_fashion,
  author = {HateslopAcademy otpensource team},
  year = {2025},
  title = {OtpenSource Fashion Dataset},
  publisher = {Hugging Face Datasets},
  url = {https://huggingface.co/datasets/hateslopacademy/otpensource_dataset}
}
```

## Glossary [optional]

- **SS:** Spring/Summer season.
- **FW:** Fall/Winter season.
- **Feature:** Unique design aspects of the clothing item.


## Dataset Card Authors

- Dataset creation: HateslopAcademy Otpensource team.
- Dataset card: Hugging Face Community.

## Dataset Card Contact

HateslopAcademy
<Hateslop@gmail.com>

