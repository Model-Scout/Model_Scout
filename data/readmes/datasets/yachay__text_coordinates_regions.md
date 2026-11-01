---
license: mit
tags:
- multilingual
- text
- coordinates
- geospatial
- translation
- NER
- geo
- geo-tagged
- named-entity-recognition
- natural-language-processing
- geographic-data
- geolocation
- twitter
- reddit
task_categories:
- feature-extraction
- token-classification
- text-classification
pretty_name: Multilingual Geo-Tagged Social Media Posts (by 123 world regions)
language:
- en
- zh
- es
- hi
- ar
- bn
- pt
- ru
- ja
- pa
- de
- jv
- ms
- te
- vi
- ko
- fr
- mr
- ta
- ur
- tr
- it
- th
- gu
- fa
- pl
size_categories:
- 100M<n<1B
---


# Dataset Card for Multilingual Geo-Tagged Social Media Posts (by 123 world regions)

## Dataset Description

- **Homepage:**  https://huggingface.co/datasets/yachay/text_coordinates_regions
- **Repository:** https://github.com/Yachay-AI/byt5-geotagging#datasets
- **Paper:** https://dev.to/yachayai/applying-machine-learning-to-geolocate-twitter-posts-2m1d
- **Leaderboard:** 
- **Point of Contact:** admin-team@yachay.ai

### Dataset Summary

The "Regions" dataset is a multilingual corpus that encompasses textual data from the 123 most populated regions worldwide, with each region's data organized into separate .json files. This dataset consists of approximately 500,000 text samples, each paired with its geographic coordinates.

**Key Features:**

- **Textual Data:** The dataset contains 500,000 text samples.
- **Geocoordinates:** Each text sample is associated with geocoordinates.
- **Regional Coverage:** The dataset encompasses 123 of the world's most populated regions.
- **Tweet Data:** Within each region, there are 5,000 individual tweets/comments.


### Supported Tasks and Leaderboards

This dataset is well-suited for tasks such as geotagging, where the objective is to associate text with specific geographical locations. It can also be utilized for geolocation analysis, sentiment analysis in regional contexts, and regional text classification.


### Languages

**Multilingual Dataset**

This dataset is multilingual and contains text data in various languages from around the world. It does not have a fixed set of languages, and the language composition may vary across different versions or updates of the dataset.

## Dataset Structure

**Structure and Naming Convention:**

The naming convention for the JSON files follows the format "c_0.json" to "c_122.json," where "c_" represents the region category followed by a unique identifier

```bash 
/
├── .gitattributes
├── README.md
├── c_0.json                 # Each .json file attributes to one of 123 regions
├── c_1.json
├── ...
├── c_122.json
```

### Data Instances

The Regions dataset consists of a total of 500,000 data instances, with each instance comprising a text sample and its associated geocoordinates. These instances are distributed across the 123 in each json file.

### Data Fields

**Text (text):** This field contains the text sample, typically holds natural language text data, such as comments, tweets, or any text-based content.

**Coordinates (coordinates):**  This field includes geographical coordinates, latitude and longitude, providing the geographic location associated with the text.

```json
{
  "text": "sample text",
  "coordinates": [
    "-75.04057630341867",
    "40.01714225600481"
  ]
}
```

### Data Splits

This dataset is not pre-partitioned into training, validation, and test data splits, providing flexibility for users to split the data according to their specific research or application needs. Users can customize the data partitioning to suit their machine learning experiments and analytical requirements.

## Dataset Creation

2021

### Curation Rationale

The "Regions" dataset was created with an objective to train and enhance geotagging textual models. With 500,000 text samples, each paired with geocoordinates, it offers a resource for developing models that can associate text with specific geographical locations. Whether for geolocation analysis or other tasks merging text and geographic information, this dataset serves as a valuable training tool.

### Source Data

#### Initial Data Collection and Normalization

The initial data collection process focused on gathering geotagged comments from social media platforms, with a primary emphasis on Twitter.

#### Who are the source language producers?

Twitter Community 

### Annotations

#### Annotation process

The coordinates in this dataset have been derived from metadata sources.

#### Who are the annotators?

No manual annotation was conducted for this dataset.

## Considerations for Using the Data

### Social Impact of Dataset

The "Regions" dataset, with its multilingual text and geographic coordinates, presents an opportunity to advance research in geospatial NLP. However, it is crucial for users to exercise caution and ethical responsibility when handling location-related data to mitigate any potential privacy concerns or misuse.

### Discussion of Biases

It's essential to acknowledge that the data collected from social media platforms may contain inherent biases, influenced by user demographics and platform dynamics. Researchers should be mindful of these biases and consider potential implications in their analyses.

### Other Known Limitations

- The dataset's multilingual nature may lead to varying data quality and linguistic diversity across regions.
- The use of geotagged social media comments means that the dataset may not cover less active or less represented regions. 
- The accuracy of geocoordinates is subject to inherent limitations of the data sources used for collection.
  
## Additional Information

### Dataset Curators

Yachay AI

### Licensing Information

MIT