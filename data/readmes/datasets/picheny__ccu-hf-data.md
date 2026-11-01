---
language:
- ko
- zh
- he
- tr
task_categories:
- automatic-speech-recognition
pretty_name: CCU Multilingual Speech Dataset
size_categories:
- 100K<n<1M
license: other
license_name: creative-commons-filtered-subset
---

# CCU Multilingual Speech Dataset

## Dataset Summary
This dataset contains segmented speech audio and transcripts for multiple languages:
Korean (ko), Chinese (zh), Hebrew (he), and Turkish (tr).It was inspired by data collected for the DARPA CCU [(Cross-Cultural Understanding Program)] (https://www.darpa.mil/research/programs/computational-cultural-understanding) and meant to resemble that data. 

Data is organized by language/split folders such as:
- `ko_train`
- `ko_dev`
- `ko_test`
(and similarly for `zh`, `he`, `tr`)

Each split includes:
- `<split>.tsv` (metadata / transcript table)
- audio files under `files_000/`, `files_001/`, ... (for large splits)

## Languages
- ko (Korean)
- zh (Chinese)
- he (Hebrew)
- tr (Turkish)

## Data Fields
TSV columns are:
- audio path (relative path to wav file)
- transcript / text


## Splits
Current split naming convention:
- `<lang>_train`
- `<lang>_dev`
- `<lang>_test`

Example:
- `ko_train/train.tsv`
- `ko_dev/dev.tsv`
- `ko_test/test.tsv`

## Attribution

When using or redistributing items from this dataset, please credit each item as:

> *"[title]"* by [uploader] ([uploader_id]), [webpage_url],
> licensed under Creative Commons Attribution (reuse allowed)
> *(or: license unconfirmed, selected via YouTube CC filter)*.
> Audio extracted, segmented, and transcripts cleaned for speech research.

See [ATTRIBUTION.txt](ATTRIBUTION.txt) for additional information and  per-language breakdown.

## Licensing
This release uses a filtered subset from the original data collection process intended to include Creative Commons licensed content.
The license details for the data are in the files `license_lang_filtered.csv`

## Dataset Creation
Audio was segmented from source media and exported as WAV for ASR use.
Large splits may store audio in multiple subdirectories (`files_000`, `files_001`, ...) to satisfy repository file-count limits.

## Intended Uses
- ASR model training
- ASR evaluation across languages
- Multilingual speech research
- Cultural understanding research 

## Limitations
- Transcript quality may vary by language/source.
- Source-domain bias is possible.
- Users should independently verify licensing and suitability for downstream use.

## Citation
If you use this dataset, please cite this dataset page and acknowledge the original source creators listed in attribution files.
