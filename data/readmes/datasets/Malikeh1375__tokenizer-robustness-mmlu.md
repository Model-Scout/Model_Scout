---
language:
- en
- ru
- zh
- ja
- de
- es
- fr
- it
- th
- ar
- tr
- ko
- hi
- bn
- te
- sw
license: cc-by-4.0
configs:
- config_name: original
  data_files:
    - split: dev
      path: original/dev/data-*
    - split: test
      path: original/test/data-*
- config_name: minor_spelling_errors
  data_files:
    - split: dev
      path: minor_spelling_errors/dev/data-*
    - split: test
      path: minor_spelling_errors/test/data-*
- config_name: spoken_language
  data_files:
    - split: dev
      path: spoken_language/dev/data-*
    - split: test
      path: spoken_language/test/data-*
- config_name: arabic
  data_files:
    - split: dev
      path: arabic/dev/data-*
    - split: test
      path: arabic/test/data-*
- config_name: telugu
  data_files:
    - split: dev
      path: telugu/dev/data-*
    - split: test
      path: telugu/test/data-*
- config_name: major_spelling_errors
  data_files:
    - split: dev
      path: major_spelling_errors/dev/data-*
    - split: test
      path: major_spelling_errors/test/data-*
- config_name: python
  data_files:
    - split: dev
      path: python/dev/data-*
    - split: test
      path: python/test/data-*
- config_name: java
  data_files:
    - split: dev
      path: java/dev/data-*
    - split: test
      path: java/test/data-*
- config_name: r
  data_files:
    - split: dev
      path: r/dev/data-*
    - split: test
      path: r/test/data-*
- config_name: unicode_text_formatting_challenges
  data_files:
    - split: dev
      path: unicode_text_formatting_challenges/dev/data-*
    - split: test
      path: unicode_text_formatting_challenges/test/data-*
- config_name: flipped_special_characters
  data_files:
    - split: dev
      path: flipped_special_characters/dev/data-*
    - split: test
      path: flipped_special_characters/test/data-*
- config_name: zalgo_homoglyphs
  data_files:
    - split: dev
      path: zalgo_homoglyphs/dev/data-*
    - split: test
      path: zalgo_homoglyphs/test/data-*
- config_name: code_switching
  data_files:
    - split: dev
      path: code_switching/dev/data-*
    - split: test
      path: code_switching/test/data-*
---

# Tokenizer Robustness MMLU Dataset

This dataset contains MMLU-formatted questions and answers designed to test tokenizer robustness across different text formats and languages.

## Dataset Description

The dataset consists of the same questions presented in 6 different formats, with both test (20 questions) and development (5 questions) sets:

1. **original** - Standard formatted questions
2. **minor_spelling_errors** - Questions with minor misspellings
3. **spoken_language** - Questions in casual spoken language style
4. **arabic** - Questions translated to Arabic
5. **telugu** - Questions translated to Telugu
6. **major_spelling_errors** - Questions with severe misspellings and text deformations
7. **python** - Questions with python codes asking for the final output
8. **java** - Questions with java codes asking for the final output
9. **r** - Questions with r codes asking for the final output
10. **unicode_text_formatting_challenges** - Original English questions with choices written with unicode text formatting challenges
11. **flipped_special_characters** - Original English questions with choices written with flipped or special characters
12. **zalgo_homoglyphs** - Original English questions with choices written in zalgo or homoglyphs text
13. **code_switching** - Questions and choices with code switching between different languages 

## Dataset Structure

Each configuration contains multiple-choice questions with identical answers, but formatted differently:

```json
{
  "question": "What is the capital of France?",
  "choices": ["London", "Berlin", "Paris", "Madrid"],
  "answer": "C"
}
```

## Usage

This dataset is designed for testing language model tokenizer robustness, particularly how models perform on the same knowledge when presented in different text formats or languages.

You can load a specific configuration using:

```python
from datasets import load_dataset

# Load a specific configuration
dataset = load_dataset("your-username/tokenizer-robustness-mmlu", "original")

# Access the test or dev split
test_data = dataset["test"]
dev_data = dataset["dev"]

# Print a sample
print(test_data[0])
```

## Configurations

Each configuration represents a different format of the same questions:

- `original`: Clean, well-formatted questions
- `minor_spelling_errors`: Questions with slight spelling mistakes
- `spoken_language`: Questions in casual, conversational language
- `arabic`: Questions translated to Arabic
- `telugu`: Questions translated to Telugu
- `major_spelling_errors`: Questions with extreme spelling errors
- `python`: Questions with python codes asking for the final output
- `java`: Questions with java codes asking for the final output
- `r`: Questions with r codes asking for the final output
- `unicode_text_formatting_challenges`: Original English questions with choices written with unicode text formatting challenges
- `flipped_special_characters`: Original English questions with choices written with flipped or special characters
- `zalgo_homoglyphs`: Original English questions with choices written in zalgo or homoglyphs text
- `code_switching`: Questions and choices with code switching between different languages 
