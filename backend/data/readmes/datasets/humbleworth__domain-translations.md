---
language:
- ar
- da
- de
- en
- es
- fi
- fr
- he
- hi
- id
- it
- ja
- ko
- nl
- pl
- pt
- ru
- sv
- tr
- zh
pretty_name: Multilingual Domain Name Translations
tags:
- translation
- multilingual
- domain-names
- embeddings
- text-generation
- zero-shot-classification
license: apache-2.0
task_categories:
- translation
- text-generation
- feature-extraction
multilinguality:
- multilingual
size_categories:
- 100K<n<1M
dataset_info:
  features:
  - name: domain
    dtype: string
  - name: base
    dtype: string
  - name: segmented
    dtype: string
  - name: source_lang
    dtype: string
  - name: translation_ar
    dtype: string
  - name: translation_da
    dtype: string
  - name: translation_de
    dtype: string
  - name: translation_en
    dtype: string
  - name: translation_es
    dtype: string
  - name: translation_fi
    dtype: string
  - name: translation_fr
    dtype: string
  - name: translation_he
    dtype: string
  - name: translation_hi
    dtype: string
  - name: translation_id
    dtype: string
  - name: translation_it
    dtype: string
  - name: translation_ja
    dtype: string
  - name: translation_ko
    dtype: string
  - name: translation_nl
    dtype: string
  - name: translation_pl
    dtype: string
  - name: translation_pt
    dtype: string
  - name: translation_ru
    dtype: string
  - name: translation_sv
    dtype: string
  - name: translation_tr
    dtype: string
  - name: translation_zh
    dtype: string
  splits:
  - name: train
    num_examples: 155004
  download_size: 50000000
  dataset_size: 155004
---

# Multilingual Domain Name Translations Dataset

## Dataset Description

This dataset contains 155,004 domain names with their multilingual translations across 20 languages. Each domain has been segmented into constituent words and translated while preserving semantic meaning and commercial appeal. The dataset is particularly valuable for domain name research, multilingual NLP tasks, and understanding how brand names and concepts translate across languages.

## Dataset Statistics

- **Total Records**: 155,004 domain translations
- **Unique Domains**: 154,811
- **Languages**: 20 (Arabic, Chinese, Danish, Dutch, English, Finnish, French, German, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Polish, Portuguese, Russian, Spanish, Swedish, Turkish)
- **Average Domain Length**: 10.9 characters
- **Average Words per Domain**: 2.3
- **Translation Coverage**: >99.9% (only 1 missing translation per language)

### Source Language Distribution
- English: 92.9% (144,074 domains)
- Spanish: 1.8% (2,848 domains)
- Chinese: 1.2% (1,871 domains)
- French: 0.8% (1,276 domains)
- Other languages: <1% each

## Dataset Structure

### Fields

- `domain`: The full domain name (e.g., "leadership-journey.com")
- `base`: Domain without TLD extension (e.g., "leadership-journey")
- `segmented`: Domain split into constituent words (e.g., "leadership journey")
- `source_lang`: Detected source language of the domain (ISO 639-1 code)
- `translation_[lang]`: Translation for each target language, where [lang] is the ISO 639-1 code

### Language Codes

| Code | Language | Code | Language |
|------|----------|------|----------|
| ar | Arabic | ja | Japanese |
| da | Danish | ko | Korean |
| de | German | nl | Dutch |
| en | English | pl | Polish |
| es | Spanish | pt | Portuguese |
| fi | Finnish | ru | Russian |
| fr | French | sv | Swedish |
| he | Hebrew | tr | Turkish |
| hi | Hindi | zh | Chinese (Simplified) |
| id | Indonesian | | |
| it | Italian | | |

## Examples

```csv
domain,base,segmented,source_lang,translation_ar,translation_da,...
leadership-journey.com,leadership-journey,leadership journey,en,رحلة القيادة,ledelsesrejse,...
xrdogepay.com,xrdogepay,xr doge pay,en,xr دوجي دفع,xr doge betaling,...
thememorydesign.com,thememorydesign,the memory design,en,تصميم الذاكرة,hukommelsen design,...
```

## Generation Process

The dataset was generated using the following methodology:

1. **Domain Selection**: Domains were sourced from a curated list of .com domains valued at over $20, ensuring commercial relevance and quality.

2. **Word Segmentation**: Each domain was segmented into constituent words using the `wordsegment` library, which uses unigram and bigram statistics to find the most probable word boundaries.

3. **Language Detection**: Source language was detected for each domain to handle non-English domains appropriately.

4. **Translation Generation**: Translations were generated using the DeepSeek-Chat model via the OpenAI-compatible API with the following approach:
   - Batch processing (5 domains per batch) for efficiency
   - Temperature of 0.3 for consistent, high-quality translations
   - Structured JSON output format
   - Parallel processing with 4 workers

5. **Quality Assurance**:
   - Retry logic for failed API calls
   - Validation of translation completeness
   - Preservation of brand names through phonetic transliteration when direct translation wasn't suitable
   - Manual review of sample outputs

## Use Cases

- **Multilingual Domain Embeddings**: Creating cross-lingual domain representations for similarity search and clustering across languages
- **Multilingual SEO**: Understanding how domain concepts translate for international markets
- **Brand Name Research**: Analyzing how brand names are adapted across languages
- **NLP Training**: Training models for domain name segmentation and translation
- **Linguistic Analysis**: Studying translation patterns and language-specific adaptations
- **Domain Investment**: Evaluating domain potential in international markets

## Limitations

- Translations are AI-generated and may not always reflect local market preferences
- Some technical or brand-specific terms may be transliterated rather than translated
- The dataset is biased towards English-origin domains (92.9%)
- Only .com domains are included

## License

This dataset is licensed under the Apache License 2.0. See the [LICENSE](https://www.apache.org/licenses/LICENSE-2.0) file for details.

## Citation

If you use this dataset, please cite:

```bibtex
@dataset{domain_translations_2025,
  title={Multilingual Domain Name Translations Dataset},
  author={Humbleworth},
  year={2025},
  publisher={Hugging Face},
  url={https://huggingface.co/datasets/humbleworth/domain-translations}
}
```

## Acknowledgments

- Translations generated using DeepSeek-Chat model
- Word segmentation performed using the `wordsegment` library