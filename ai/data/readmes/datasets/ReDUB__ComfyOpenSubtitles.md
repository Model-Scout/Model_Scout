---
license: unknown
task_categories:
- translation
language:
- en
- ru
- fr
- es
- ar
- zh
- ko
- ja
- de
pretty_name: ComfyOpenSubtitles
size_categories:
- 10M<n<100M
---

# ComfyOpenSubtitles

## Dataset Description

ComfyOpenSubtitles is a multilingual dataset that contains parallel translations of subtitles from various languages. It includes pairs of input and target languages, along with the corresponding subtitles.

### Languages

The dataset supports the following languages:
- English (en)
- Russian (ru)
- French (fr)
- Spanish (es)
- Arabic (ar)
- Simplified Chinese (zh-cn)
- Korean (ko)
- Japanese (ja)
- German (de)

## Dataset Structure

### Data Instances

Here are some examples of data instances:

- Input Language: English
  Target Language: Russian
  Input Text: "Oh, bud... what have you done?"
  Output Text: "Эх, Кореш... Что ж вы наделали?"

- Input Language: Spanish
  Target Language: French
  Input Text: "This is a beautiful sunset."
  Output Text: "C'est un magnifique coucher de soleil."

### Data Fields

The dataset includes the following fields for each instance:
- `input_language`: The language of the input text.
- `target_language`: The language of the target translation.
- `input_text`: The input text in the source language.
- `output_text`: The corresponding translation in the target language.

### Data Splits

The dataset is typically divided into training splits with varying sizes.

## Dataset Creation

### Curation Rationale

The dataset was created to provide a multilingual collection of subtitles and their translations for research and natural language processing tasks.

### Source Data

The source data for this dataset consists of subtitles from various movies and TV shows.

### Personal and Sensitive Information

The dataset may contain text from movies and TV shows, which may include personal or sensitive information related to the content of those shows.

### Other Known Limitations

Some data may be inaccurate. Be careful.

## Acknowledgments

- https://huggingface.co/datasets/open_subtitles