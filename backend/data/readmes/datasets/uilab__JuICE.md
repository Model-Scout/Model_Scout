---
license: cc-by-4.0
task_categories:
- text-generation
- question-answering
- text-classification
language:
- en
- ko
- id
- bn
configs:
- config_name: error-level
  data_files: data/JuICE_error_group_level.csv 
- config_name: response-level
  data_files: data/JuICE_response_level.csv
- config_name: sentence-level
  data_files: data/JuICE_sentence_level.csv
---

# JuICE: A Benchmark for Evaluating LLM-Judge in Identifying Cultural Errors (NeurIPS 2026, E&D Track)

## Sources
- **Paper:** [arXiv](https://arxiv.org/abs/2605.26955)
- **Webpage:** [https://jinjh0123.github.io/JuICE/](https://jinjh0123.github.io/JuICE/)
- **GitHub Repository:** [jinjh0123/JuICE](https://github.com/jinjh0123/JuICE)
- **HuggingFace Datasets:** [uilab/JuICE](https://huggingface.co/datasets/uilab/JuICE)

## About
We present **JuICE** (Benchmark for LLM-**Ju**dge in **I**dentifying **C**ultural **E**rrors), a multilingual dataset of 7,470 span-level annotations of cultural and linguistic errors, collected from native speakers in long-form LLM responses. It covers 1,050 query-response pairs from four countries (the United States, South Korea, Indonesia, and Bangladesh), in both English and their countries' main languages.

## Data Description

- `country`: Target country: `us`, `korea`, `indonesia`, or `bangladesh`.
- `language`: Language code: `en` (English), `ko` (Korean), `id` (Indonesian), or `bn` (Bengali).
- `qa_id`: Unique identifier of a query-response pair: `{country}_{query_id}_{language_type}_{respondent_model}`.
- `query`: Query provided to the response-generating model.
- `response`: Model-generated response.

**span-level** (error-level & response-level)
- `error_groups`: Object containing the aggregated error groups, keyed by `error_group_id`.
    - `errors`: Object containing the individual error annotations in the group, keyed by `error_id`.
        - `paragraph_idx_list`: Zero-based indices of the paragraphs in `response_text` containing the error span. Paragraphs within each response are separated by `\n\n`.
        - `detector_id`: Identifier of the human annotator or model that detected the error.
        - `detector_type`: Detector source: `human` or `model`.
        - `span`: Text span identified as erroneous.
        - `explanation`: Explanation of why the span is erroneous.
        - `raw_annotation`: Original annotation stored as a JSON-encoded string.
        - `thick_category`: Category assigned using the error taxonomy for thick evaluation.
    - `paragraph_idx_list`: Union of the paragraph indices associated with the individual errors in the group.
    - `thick_categories`: Union of the taxonomy categories assigned to the individual errors in the group.

**sentence-level** 
- `sentence_idx`: String identifier locating a sentence within `response_text`, in the format `{paragraph_index}_{line_index}_{sentence_index}`, where all three indices are zero-based.
- `error_ids`: IDs of the individual error annotations associated with the sentence, corresponding to `error_id` keys above. An empty list indicates that the sentence has no annotated errors.
- `category`: List of taxonomy categories associated with the sentence's errors.


## Evaluation
To evaluate LLM-judges using JuICE, see our [GitHub repository](https://github.com/jinjh0123/JuICE).


## BibTex
```
@misc{jin-etal-2026-juice,
      title={{J}u{ICE}: {A} Benchmark for Evaluating {LLM}-{J}udge in Identifying Cultural Errors}, 
      author={Jiho Jin and Junho Myung and Juhyun Oh and Junyeong Park and Rifki Afina Putri and Sunipa Dev and Vinodkumar Prabhakaran and Alice Oh},
      year={2026},
      eprint={2605.26955},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.26955}, 
}
```
