---
task_categories:
- translation
- sentence-similarity
- feature-extraction
language:
- en
tags:
- multilingual
---
# Multilingual Parallel Sentences with Semantic Similarity Scores and Quality Metrics

This dataset is a diverse collection of parallel sentences in English and various other languages, sourced from multiple high-quality datasets. 
Each sentence pair includes a semantic similarity score calculated using the [Language-agnostic BERT Sentence Embedding (LaBSE) model](https://huggingface.co/sentence-transformers/LaBSE), 
along with additional quality metrics. 

### Supported Tasks

This dataset supports:
- Machine Translation
- Cross-lingual Semantic Similarity
- Multilingual Natural Language Understanding
- Translation Quality Estimation

### Languages

The dataset includes English paired with multiple languages from sources such as JW300, Europarl, TED Talks, OPUS-100, Tatoeba, Global Voices, and News Commentary.

Please see [sentence-transformers/parallel-sentences-datasets](https://huggingface.co/collections/sentence-transformers/parallel-sentences-datasets-6644d644123d31ba5b1c8785)
for the original sources.

## Dataset Structure

### Data Instances

Each instance contains:
- `english`: The English sentence (string)
- `non_english`: The corresponding sentence in another language (string)
- `distance`: Semantic similarity score (cosine distance) between the sentences (float)
- `quality`: Content quality score (float)
- `readability`: Readability score (float)
- `sentiment`: Sentiment score (float)

Example:
```json
{
  "english": "If we start to think exponentially, we can see how this is starting to affect all the technologies around us.",
  "non_english": "Če začnemo misliti eksponentno, vidimo, kako to začenja vplivati ​​na vse tehnologije okoli nas.",
  "distance": 0.05299,
  "quality": 0.3359375,
  "readability": 0.103515625,
  "sentiment": 0.45703125
}
```

### Data Splits

The dataset is divided into:

- Train: 867&thinsp;042 rows (90%)
- Validation: 96&thinsp;338 rows (10%)
- Total: 963&thinsp;380 rows (100%)

## Dataset Creation

Sentences were downloaded from different splits and configurations of each dataset, ensuring a rich variety of linguistic representations.
To ensure high quality, the dataset was deduplicated, and only sentence pairs with a semantic similarity score (`distance`) below 0.25 were included. 
A total of 5&thinsp;000 sentences were downloaded from each split of each dataset, resulting in a final distribution of 90% training and 10% validation.

### Annotations

Semantic similarity scores were generated using the LaBSE model by calculating cosine distances between embeddings. 
Additional metrics were annotated using the 
[quality](https://huggingface.co/agentlans/deberta-v3-base-zyda-2-quality), 
[readability](https://huggingface.co/agentlans/deberta-v3-base-zyda-2-readability), and
[sentiment](https://huggingface.co/agentlans/deberta-v3-base-zyda-2-sentiment) models.

## Considerations for Using the Data

### Social Impact

This dataset can enhance cross-lingual NLP models and applications by providing high-quality parallel sentences with semantic similarity and quality metrics.

### Known Limitations

- The semantic similarity (`distance`) and quality scores may not capture all nuances of cross-lingual similarity or translation quality.
- Coverage is limited to languages present in the source datasets.
- Filtering based on `distance < 0.25` may exclude some valid but less similar translations.