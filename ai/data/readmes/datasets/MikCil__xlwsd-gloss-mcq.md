---
dataset_info:
  features:
  - name: instance_id
    dtype: string
  - name: language
    dtype: string
  - name: language_code
    dtype: string
  - name: pos
    dtype: string
  - name: lemma
    dtype: string
  - name: surface
    dtype: string
  - name: num_candidates
    dtype: int64
  - name: gold_synset
    dtype: string
  - name: messages_mcq
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: messages_gloss
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 2666235412
    num_examples: 1583531
  - name: dev
    num_bytes: 7781360
    num_examples: 4428
  - name: test
    num_bytes: 47279231
    num_examples: 27102
  download_size: 555554596
  dataset_size: 2721296003
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: dev
    path: data/dev-*
  - split: test
    path: data/test-*
license: other
license_name: xl-wsd-non-commercial
license_link: https://sapienzanlp.github.io/xl-wsd/license/
language:
- en
- eu
- bg
- ca
- zh
- hr
- da
- nl
- et
- fr
- gl
- de
- hu
- it
- ja
- ko
- sl
- es
task_categories:
- multiple-choice
- text-classification
- text-generation
tags:
- word-sense-disambiguation
- wsd
- multilingual
- gloss
- lexical-semantics
- wordnet
- definition-generation
pretty_name: XL-WSD Gloss MCQ and Generation
size_categories:
- 1M<n<10M
extra_gated_prompt: By submitting this form, you agree to the XL-WSD [License Agreement](https://sapienzanlp.github.io/xl-wsd/license/)
extra_gated_fields:
  Name: text
  Affiliation: text
  Country: country
  I agree to use this model for non-commercial use ONLY: checkbox
---

# XL-WSD Gloss Multiple-Choice Question and Generation

A multilingual Word Sense Disambiguation (WSD) dataset using BabelNet and WordNet glosses, formatted in two chat-style variants:

1. **Multiple-choice disambiguation** (`messages_mcq`), where the model selects the correct sense definition from a list of candidate glosses.
2. **Gloss generation** (`messages_gloss`), where the model generates the meaning of the target word in context without being shown candidate answers.

This dataset is a processed adaptation of [XL-WSD](https://sapienzanlp.github.io/xl-wsd/), an extra-large cross-lingual evaluation framework for Word Sense Disambiguation.

## Dataset Description

This dataset reformulates WSD as instruction-style chat data suitable for training and evaluating language models.

Each example is built around a target word in context and provides two alternative supervision views:

- **MCQ view:** the model is shown the sentence and a numbered list of candidate glosses, and must output the number of the correct answer.
- **Gloss-generation view:** the model is shown the sentence and target word, and must produce the correct gold gloss directly.

Both views correspond to the same underlying disambiguation instance and the same gold synset.

### Source

This dataset is derived from **XL-WSD** (Pasini et al., 2021), which provides sense-annotated development and test sets in 18 languages from six linguistic families, along with language-specific silver training data.

- **Original Dataset:** [https://sapienzanlp.github.io/xl-wsd/](https://sapienzanlp.github.io/xl-wsd/)
- **Original Paper:** [XL-WSD: An Extra-Large and Cross-Lingual Evaluation Framework for Word Sense Disambiguation](https://ojs.aaai.org/index.php/AAAI/article/view/17609) (AAAI 2021)
- **Original Code:** [https://github.com/SapienzaNLP/xl-wsd-code](https://github.com/SapienzaNLP/xl-wsd-code)

## Dataset Processing

This adaptation applies several filtering and transformation steps to create a clean multiple-choice format suitable for training and evaluating language models.

### Preprocessing Steps

1. **Language-Matched Glosses Only**  
   Candidate glosses are filtered to include only those in the same language as the target sentence. Cross-lingual gloss candidates (e.g., English glosses for a French sentence) are removed to ensure the task tests sense disambiguation rather than cross-lingual understanding.

2. **Polysemous Lemmas Only**  
   Instances where the target lemma has only one candidate sense (monosemous) are removed. This ensures every example requires genuine disambiguation between multiple plausible options.

3. **Single Correct Answer Per Row**  
   The original XL-WSD data occasionally contains instances with multiple valid gold synsets. To ensure models are not penalized for selecting any correct answer while maintaining a single-choice format, these instances are expanded into multiple rows. Each row contains exactly one correct candidate plus all incorrect candidates.
   
   *Example:* If an instance has candidates A, B, C, D where both A and B are correct:
   - Row 1: candidates A, C, D (correct answer: A)
   - Row 2: candidates B, C, D (correct answer: B)

   In the MCQ view, each row includes one correct candidate plus all incorrect candidates.  
   In the gloss-generation view, each row uses the gloss corresponding to that row’s gold synset as the target output.

4. **Multi-Occurrence Disambiguation**  
   When a target word appears multiple times in a sentence, the prompt specifies which occurrence is being disambiguated (e.g., "bank (2nd occurrence)"). Instances where the occurrence cannot be reliably determined are discarded.

5. **Deterministic Candidate Shuffling**  
   Candidate options are shuffled deterministically based on the instance ID to prevent position bias while ensuring reproducibility.

6. **Validation Safeguards**  
   Any instance that would result in zero correct candidates or zero incorrect candidates after filtering is discarded.

## Dataset Schema

Each example contains the following fields:

| Field            | Type   | Description                                                                      |
| ---------------- | ------ | -------------------------------------------------------------------------------- |
| `instance_id`    | string | Unique identifier (with `_v0`, `_v1` suffixes for expanded multi-gold instances) |
| `language`       | string | Full language name (e.g., "English", "French")                                   |
| `language_code`  | string | ISO language code (e.g., "en", "fr")                                             |
| `pos`            | string | Part of speech tag                                                               |
| `lemma`          | string | Lemma of the target word                                                         |
| `surface`        | string | Surface form of the target word as it appears in the sentence                    |
| `num_candidates` | int    | Number of candidate glosses                                                      |
| `gold_synset`    | string | BabelNet synset ID of the correct answer                                         |
| `messages_mcq` | list | Chat-format messages for the multiple-choice task |
| `messages_gloss` | list | Chat-format messages for the gloss-generation task |

### Message Format

Both message fields follow a chat format compatible with common LLM fine-tuning frameworks.

### `messages_mcq`

The model receives a prompt containing the sentence, target word, and numbered candidate glosses, and must answer with the number of the correct option.

```python
[
    {"role": "user", "content": "<prompt with sentence and numbered candidates>"},
    {"role": "assistant", "content": "<answer number>"}
]
````

### `messages_gloss`

The model receives a prompt containing the sentence and target word, but no candidate list. It must generate the correct gold gloss for the target sense.

```python
[
    {"role": "user", "content": "<prompt asking for the meaning of the target word in context>"},
    {"role": "assistant", "content": "<gold gloss>"}
]
````

## Languages

The dataset covers 18 languages from six linguistic families:

|Code|Language|Code|Language|
|---|---|---|---|
|`en`|English|`hu`|Hungarian|
|`eu`|Basque|`it`|Italian|
|`bg`|Bulgarian|`ja`|Japanese|
|`ca`|Catalan|`ko`|Korean|
|`zh`|Chinese|`sl`|Slovenian|
|`hr`|Croatian|`es`|Spanish|
|`da`|Danish|`fr`|French|
|`nl`|Dutch|`gl`|Galician|
|`et`|Estonian|`de`|German|

## Usage

### Loading the Dataset

```python
from datasets import load_dataset

# Load all splits
dataset = load_dataset("MikCil/xlwsd-gloss-mcq")

# Access specific splits
train_data = dataset["train"]
dev_data = dataset["dev"]
test_data = dataset["test"]
```

### Filtering by Language

```python
# English only
english_data = dataset.filter(lambda x: x["language_code"] == "en")

# Multiple languages
target_langs = ["en", "fr", "de", "es"]
multilingual_data = dataset.filter(lambda x: x["language_code"] in target_langs)
```

### Example Instance

```python
example = dataset["dev"][0]
print(example["messages_mcq"][0]["content"])
print(example["messages_gloss"][0]["content"])
```

### Training with Transformers

```python
from transformers import AutoTokenizer
from trl import SFTTrainer

tokenizer = AutoTokenizer.from_pretrained("your-model")

def format_mcq(example):
    return {
        "text": tokenizer.apply_chat_template(
            example["messages_mcq"],
            tokenize=False
        )
    }

def format_gloss(example):
    return {
        "text": tokenizer.apply_chat_template(
            example["messages_gloss"],
            tokenize=False
        )
    }

train_mcq = dataset["train"].map(format_mcq)
train_gloss = dataset["train"].map(format_gloss)
```

## Evaluation

When evaluating models on this dataset, note that the candidate order for the MCQ task is deterministically shuffled.

The correct answer is always a single digit corresponding to the position of the correct gloss in the numbered list.

## License

This dataset is a processed version of XL-WSD v1 downloaded from [https://sapienzanlp.github.io/xl-wsd/](https://sapienzanlp.github.io/xl-wsd/), made available under the **XL-WSD Non-Commercial License**. Full license: [https://sapienzanlp.github.io/xl-wsd/license/](https://sapienzanlp.github.io/xl-wsd/license/)

### Attribution Requirements

When using this dataset, you must:

1. Credit the original XL-WSD authors
2. Include the URI to the original dataset
3. Indicate that this is a processed/adapted version
4. Include or link to the license

## Citation

### This Dataset

```bibtex
@misc{xlwsd-gloss-mcq,
  title = {XL-WSD Gloss MCQ: A Multiple-Choice Adaptation of XL-WSD},
  author = {Michele Ciletti},
  year = {2026},
  howpublished = {\url{https://huggingface.co/datasets/MikCil/xlwsd-gloss-mcq}},
}
```

### Original XL-WSD

```bibtex
@inproceedings{pasini-etal-xl-wsd-2021,
  title = {{XL-WSD}: An Extra-Large and Cross-Lingual Evaluation Framework for Word Sense Disambiguation},
  author = {Pasini, Tommaso and Raganato, Alessandro and Navigli, Roberto},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
  year = {2021}
}
```

### Underlying Resources

This dataset builds upon numerous WordNets and evaluation datasets. See the [XL-WSD documentation](https://sapienzanlp.github.io/xl-wsd/) for the complete list of citations for individual language resources.

## Contact

For issues specific to this processed version, please open an issue on the [dataset repository](https://huggingface.co/datasets/MikCil/xlwsd-gloss-mcq).

For questions about the original XL-WSD data, refer to the [XL-WSD contacts page](https://sapienzanlp.github.io/xl-wsd/).