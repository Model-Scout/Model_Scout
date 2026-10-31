---
license: cdla-sharing-1.0
dataset_info:
- config_name: arabic
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 2050273337.3987067
    num_examples: 1712361
  - name: test
    num_bytes: 101641945.60129331
    num_examples: 84890
  download_size: 1037665708
  dataset_size: 2151915283
- config_name: azerbaijani
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 1756408398.6204288
    num_examples: 1715809
  - name: test
    num_bytes: 87002053.3795713
    num_examples: 84991
  download_size: 960349473
  dataset_size: 1843410452
- config_name: chinese
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 2051351450.1030862
    num_examples: 2879487
  - name: test
    num_bytes: 82156301.89691366
    num_examples: 115323
  download_size: 1230853607
  dataset_size: 2133507752
- config_name: english
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 2130468095.0648887
    num_examples: 2635469
  - name: test
    num_bytes: 88476700.93511136
    num_examples: 109449
  download_size: 1152374780
  dataset_size: 2218944796
- config_name: farsi
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 180685727.81538463
    num_examples: 132568
  - name: test
    num_bytes: 26267088.184615385
    num_examples: 19272
  download_size: 90266765
  dataset_size: 206952816
- config_name: german
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 533611365.478921
    num_examples: 282059
  - name: test
    num_bytes: 56136659.521079004
    num_examples: 29673
  download_size: 291925721
  dataset_size: 589748025
- config_name: hebrew
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 21481769.852342676
    num_examples: 20686
  - name: test
    num_bytes: 7198667.147657325
    num_examples: 6932
  download_size: 13506171
  dataset_size: 28680437
- config_name: hindi
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 92442873.73794927
    num_examples: 40027
  - name: test
    num_bytes: 22834154.262050726
    num_examples: 9887
  download_size: 39719056
  dataset_size: 115277028
- config_name: korean
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 2969638578.050348
    num_examples: 2632457
  - name: test
    num_bytes: 123384434.94965227
    num_examples: 109375
  download_size: 1498460065
  dataset_size: 3093023013
- config_name: spanish
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 2911961182.6516333
    num_examples: 4058317
  - name: test
    num_bytes: 101357465.3483666
    num_examples: 141259
  download_size: 1509916798
  dataset_size: 3013318648
- config_name: turkish
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 1769035666.3545604
    num_examples: 1810342
  - name: test
    num_bytes: 85714595.64543971
    num_examples: 87716
  download_size: 998323956
  dataset_size: 1854750262
- config_name: vietnamese
  features:
  - name: story
    dtype: string
  splits:
  - name: train
    num_bytes: 2667052064.602918
    num_examples: 2493325
  - name: test
    num_bytes: 113306591.3970817
    num_examples: 105926
  download_size: 1354090093
  dataset_size: 2780358656
configs:
- config_name: arabic
  data_files:
  - split: train
    path: arabic/train-*
  - split: test
    path: arabic/test-*
- config_name: azerbaijani
  data_files:
  - split: train
    path: azerbaijani/train-*
  - split: test
    path: azerbaijani/test-*
- config_name: chinese
  data_files:
  - split: train
    path: chinese/train-*
  - split: test
    path: chinese/test-*
- config_name: english
  data_files:
  - split: train
    path: english/train-*
  - split: test
    path: english/test-*
- config_name: farsi
  data_files:
  - split: train
    path: farsi/train-*
  - split: test
    path: farsi/test-*
- config_name: german
  data_files:
  - split: train
    path: german/train-*
  - split: test
    path: german/test-*
- config_name: hebrew
  data_files:
  - split: train
    path: hebrew/train-*
  - split: test
    path: hebrew/test-*
- config_name: hindi
  data_files:
  - split: train
    path: hindi/train-*
  - split: test
    path: hindi/test-*
- config_name: korean
  data_files:
  - split: train
    path: korean/train-*
  - split: test
    path: korean/test-*
- config_name: spanish
  data_files:
  - split: train
    path: spanish/train-*
  - split: test
    path: spanish/test-*
- config_name: turkish
  data_files:
  - split: train
    path: turkish/train-*
  - split: test
    path: turkish/test-*
- config_name: vietnamese
  data_files:
  - split: train
    path: vietnamese/train-*
  - split: test
    path: vietnamese/test-*
task_categories:
- text-generation
language:
- ar
- az
- zh
- en
- fa
- de
- he
- hi
- ko
- es
- tr
- vi
pretty_name: Multilingual TinyStories
size_categories:
- 10M<n<100M
---


# Dataset Card for Multilingual TinyStories

## Dataset Details

### Dataset Description

The **Multilingual TinyStories** dataset contains translations of the original TinyStories dataset, which consists of synthetically generated short stories using a small vocabulary suitable for 3 to 4-year-olds. These stories were originally generated by GPT-3.5 and GPT-4. The multilingual versions have been translated into various languages, including Spanish, Chinese, German, Turkish, Farsi, Korean, Arabic, Vietnamese, Hebrew, and Hindi. This dataset is ideal for training and evaluating small language models (SLMs) in multiple languages. It allows researchers to explore scaling laws, interpretability, and other phenomena across different languages and smaller language models with fewer than 10 million parameters.

- **Curated by:** Aggregated and cleaned by Gabriel Adriano de Melo.
- **Original Dataset from:** 
- **Language(s) (NLP):** English, Spanish, Chinese, German, Turkish, Farsi, Korean, Arabic, Vietnamese, Hebrew, Hindi
- **License:** cdla-sharing-1.0

### Dataset Sources

- **Original Repository:** [roneneldan/TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories)
- **Original Paper:** [TinyStories: How Small Can Language Models Be and Still Speak Coherent English?](https://arxiv.org/abs/2305.07759)
- **Spanish Translation:** [rrobrenaud/multilingual_tinystories](https://huggingface.co/datasets/robrenaud/multilingual_tinystories)
- **Chinese Translation:** [52AI/TinyStoriesZh](https://huggingface.co/datasets/52AI/TinyStoriesZh)
- **Turkish Translation:** [umarigan/tinystories_tr](https://huggingface.co/datasets/umarigan/tinystories_tr)
- **Arabic Translation:** [sboughorbel/tinystories_dataset_arabic](https://huggingface.co/datasets/sboughorbel/tinystories_dataset_arabic)
- **Vietnamese Translation:** [nampdn-ai/tinystories-vietnamese](https://huggingface.co/datasets/nampdn-ai/tinystories-vietnamese)
- **Azerbaijani Translation:** [marinowskiii/tiny-stories-aze](https://huggingface.co/datasets/marinowskiii/tiny-stories-aze)
- **Korean Translation:** [g0ster/TinyStories-Korean](https://huggingface.co/datasets/g0ster/TinyStories-Korean)
- **German Rendition:** [SkySyrup/tinystories_german](https://huggingface.co/datasets/SkySyrup/tinystories_german)
- **Farsi Translation:** [taesiri/TinyStories-Farsi](https://huggingface.co/datasets/taesiri/TinyStories-Farsi)
- **Hindi Translation:** [vishnu2308/TinyStories-50k-Hindi](https://huggingface.co/datasets/vishnu2308/TinyStories-50k-Hindi)
- **Hebrew Translation:** [Norod78/TinyStoriesV2-GPT4-valid_heb-lineByLine-EoT](https://huggingface.co/datasets/Norod78/TinyStoriesV2-GPT4-valid_heb-lineByLine-EoT)



## Uses

### Direct Use

This dataset can be used for:
- Training small language models in multilingual settings.
- Evaluating language models' fluency, consistency, reasoning, and creativity across multiple languages.
- Exploring the scaling laws and interpretability of small language models with fewer than 10 million parameters.
- Analyzing language models in low-resource or specialized language domains.

### Out-of-Scope Use

This dataset is not recommended for:
- Use cases requiring complex linguistic expressions or advanced vocabulary.
- Training models designed for adult-level comprehension or advanced language understanding.
- Applications involving sensitive or personal information (as the dataset focuses on child-appropriate vocabulary).

## Dataset Structure

The dataset consists of several language-specific subsets, each containing short stories generated using a small vocabulary. The original stories were generated in English and then translated into other languages. The dataset is organized by language and may contain multiple splits (e.g., training, validation).

### Data Fields
Each entry in the dataset contains:
- **story:** The text of the story in the respective language.

Each language is separated in its own subset. If you don't want to download the whole dataset, you can download only a single language:

```python
from datasets import load_dataset

languages = ['english', 'spanish', 'chinese', 'turkish', 'arabic', 'vietnamese',
             'azerbaijani', 'korean', 'german', 'farsi', 'hindi', 'hebrew']

dataset = load_dataset("Gabrui/multilingual_TinyStories", "german")
```

### Splits

Training and Test splits are present. The test split is a hold-out for final evaluation after training and hyper-param selection.

## Dataset Creation

### Curation Rationale

The dataset was created to facilitate the training and evaluation of small language models (SLMs) that can still generate coherent, fluent, and consistent short stories in multiple languages. This multilingual version extends the original TinyStories dataset, allowing the exploration of language capabilities across different linguistic contexts.

### Source Data

#### Data Collection and Processing

The stories in this dataset were translated from the original English TinyStories, which were synthetically generated by GPT-3.5 and GPT-4. Translation contributions came from various sources, including individual users and communities, using both manual and automated translation methods. After aggregating the translations, the dataset was cleaned and pruned to remove duplicates and inconsistencies (buggy characters with low frequency).

#### Who are the source data producers?

The original TinyStories were generated by GPT-3.5 and GPT-4, and the translations were provided by a range of contributors from the Hugging Face community, including users who contributed specific language subsets (links provided above).
- **Original Repository:** [roneneldan/TinyStories](https://huggingface.co/datasets/roneneldan/TinyStories)
- **Spanish Translation:** [rrobrenaud/multilingual_tinystories](https://huggingface.co/datasets/robrenaud/multilingual_tinystories)
- **Chinese Translation:** [52AI/TinyStoriesZh](https://huggingface.co/datasets/52AI/TinyStoriesZh)
- **Turkish Translation:** [umarigan/tinystories_tr](https://huggingface.co/datasets/umarigan/tinystories_tr)
- **Arabic Translation:** [sboughorbel/tinystories_dataset_arabic](https://huggingface.co/datasets/sboughorbel/tinystories_dataset_arabic)
- **Vietnamese Translation:** [nampdn-ai/tinystories-vietnamese](https://huggingface.co/datasets/nampdn-ai/tinystories-vietnamese)
- **Azerbaijani Translation:** [marinowskiii/tiny-stories-aze](https://huggingface.co/datasets/marinowskiii/tiny-stories-aze)
- **Korean Translation:** [g0ster/TinyStories-Korean](https://huggingface.co/datasets/g0ster/TinyStories-Korean)
- **German Rendition:** [SkySyrup/tinystories_german](https://huggingface.co/datasets/SkySyrup/tinystories_german)
- **Farsi Translation:** [taesiri/TinyStories-Farsi](https://huggingface.co/datasets/taesiri/TinyStories-Farsi)
- **Hindi Translation:** [vishnu2308/TinyStories-50k-Hindi](https://huggingface.co/datasets/vishnu2308/TinyStories-50k-Hindi)
- **Hebrew Translation:** [Norod78/TinyStoriesV2-GPT4-valid_heb-lineByLine-EoT](https://huggingface.co/datasets/Norod78/TinyStoriesV2-GPT4-valid_heb-lineByLine-EoT)


## Bias, Risks, and Limitations

### Biases

Since the stories are synthetically generated and translated, there may be cultural biases inherent in the translation process, especially when translating concepts or terms that do not directly map across languages. Additionally, stories are simple and child-focused, which limits their diversity in complexity and subject matter.

### Risks

- **Risk of poor translation quality:** Inconsistencies or errors may arise due to automated translations or lack of expertise in certain languages.
- **Language-specific limitations:** The simplicity of vocabulary may not reflect the linguistic richness of all languages, and certain language-specific nuances may be lost in translation.

### Recommendations

When using this dataset, it is recommended to perform quality checks on the translations, especially if the dataset is used in formal evaluation settings. Additionally, consider supplementing this dataset with native speaker reviews to verify the linguistic integrity of the stories.

#### Personal and Sensitive Information

The dataset contains no personal, sensitive, or private information. It is composed solely of synthetic, child-appropriate short stories.

## Glossary

- **Small Language Models (SLMs):** Language models with fewer than 10 million parameters.
- **GPT-4 Grading:** A new paradigm where GPT-4 evaluates model outputs for grammar, creativity, and consistency.

