---
pretty_name: "Non-Latin Scene Text"
license: other
license_name: kled-commercial-training-license
license_link: https://www.kled.ai/datasets/non-latin-script-text
language:
- hi
- ar
- th
- ru
- zh
- bn
- my
- ko
- ja
task_categories:
- image-to-text
- object-detection
tags:
- kled
- commercial-license
- consented-data
- human-collected
- sample-on-request
- image
- real-world-capture
- phone-capture
- labeled
- camera-original
- provenance
size_categories:
- 10K<n<100K
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
source_datasets:
- original
multilinguality:
- multilingual
viewer: false
gated: manual
extra_gated_heading: "Request a sample set of Non-Latin Scene Text"
extra_gated_prompt: "Kled delivers sample sets and licensed data by email, not through Hugging Face. Tell us a little about your work and the Kled data team will send a sample set and pricing. Your request goes to team@kled.ai."
extra_gated_fields:
  Company or lab: text
  Role: text
  What are you building: text
  Volume you need:
    type: select
    options:
    - Sample set only
    - Under 10,000 items
    - 10,000 to 100,000 items
    - 100,000 or more items
    - Full dataset
    - Custom collection on the Kled contributor base
  I agree to be contacted by Kled about this request: checkbox
extra_gated_button_content: "Request a sample set"
extra_gated_description: "Prefer email? Write to team@kled.ai with the dataset name in the subject line."
---
# Dataset Card for Non-Latin Scene Text

<p align="center"><img src="https://knrucgucrxvizxlraxgn.supabase.co/storage/v1/object/public/task-images/v3/49/header-8586e4bb.jpg" alt="Non-Latin Scene Text" width="520"></p>

> Sharp photos of real-world writing in Devanagari, Arabic, Thai, Cyrillic, Han and other non-Latin scripts, tagged.

Collected through the Kled app by consenting contributors and licensed for commercial training. The files are delivered by Kled under license, not downloaded from this repository. Use **Request a sample set** at the top of this page, or write to [team@kled.ai](mailto:team@kled.ai). Catalog entry: [kled.ai/datasets/non-latin-script-text](https://www.kled.ai/datasets/non-latin-script-text?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=non-latin-script-text).

## Dataset Details

### Dataset Description

Contributors in the 54 eligible countries, where everyday writing uses a non-Latin script, choose the script they are photographing, then shoot any text in it, on signs, packaging, documents or screens, close enough that the characters are sharp; Latin-only and unreadable shots are refused. The script tag is applied at capture by someone who reads the script; Devanagari, Arabic script, Thai, Cyrillic, Han, Bengali and Burmese are all in scope. No transcriptions are included. The non-Latin world is where scene-text models are weakest and training data thinnest: MTVQA covers nine languages, and HierText and TextOCR are Flickr-era and mostly English. Per-script counts are available on request.

- **Curated by:** Kled ([useKled](https://huggingface.co/useKled))
- **Collected through:** Phone camera (in app)
- **Language(s):** Hindi, Arabic, Thai, Russian, Chinese, Bengali, Burmese, Korean, Japanese
- **Regions:** Countries using non-Latin scripts (54 countries)
- **Volume:** 25,000+ photos (approx. 75 GB)
- **Contributors:** 1,000+
- **Modality:** Images
- **Format:** JPG / PNG / HEIC
- **Resolution:** Native phone camera resolution (JPG, PNG, HEIC)
- **Annotations:** Labeled (script tag)
- **Quality control:** QA review on every submission
- **License:** Non-exclusive commercial training license ([terms](https://www.kled.ai/datasets/non-latin-script-text?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=non-latin-script-text)); exclusivity available on request
- **Consent:** Each contributor opted in to this use when they uploaded.

### Dataset Sources

- **Catalog page:** [kled.ai/datasets/non-latin-script-text](https://www.kled.ai/datasets/non-latin-script-text?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=non-latin-script-text)
- **Sample set:** through the access request at the top of this page, or [team@kled.ai](mailto:team@kled.ai)
- **Publisher:** [huggingface.co/useKled](https://huggingface.co/useKled)

## Uses

### Direct Use

- Multilingual scene-text detection and recognition
- Script identification
- Text-centric VQA beyond Latin

### Out-of-Scope Use

Redistribution or resale of the files, use outside the terms of the commercial training license, and any attempt to identify or contact contributors or people who appear in the data. Uses that require labels this set does not carry should be scoped with the data team first.

## Dataset Structure

### Data Instances

One photo per record, delivered as JPG / PNG / HEIC. Volume: 25,000+ photos.

### Data Fields

- **File:** the JPG / PNG / HEIC file as captured or uploaded by the contributor
- **Labels:** Labeled (script tag), entered by the contributor at capture and checked at review.
- **Capture metadata:** capture tool, country of capture, submission time
- **Review status:** QA outcome (QA review on every submission)

Field names and the manifest format are confirmed with the sample set.

### Data Splits

Delivered as one set. Subsets by country, language or label, and custom splits, are available on request.

## Dataset Creation

### Curation Rationale

The dataset exists because the public alternatives named in the description are non-commercial, synthetic, small or collected elsewhere. Kled runs the task as a paid brief in its app so that the data is captured on purpose, under the capture rules above, by people who have opted in to commercial use.

### Source Data

#### Data Collection and Processing

Contributors complete the task in the Kled app. Capture tool: Phone camera (in app). Each submission is reviewed against the task brief; submissions that break the capture rules are rejected. QA review on every submission. Files are delivered as JPG / PNG / HEIC, in the resolution noted above.

#### Who are the source data producers?

Kled contributors, who complete paid data tasks on their own phones. This task was open to contributors in the 54 eligible countries where everyday writing uses a non-Latin script. Kled has 625,000+ contributors in 100+ countries, strongest in Southeast Asia, the United States and Europe.

### Annotations

#### Annotation process

Labeled (script tag). The label is entered by the contributor as part of the task and checked at review against the task brief; it is a contributor label, not an expert annotation, unless the description above says otherwise.

#### Who are the annotators?

The contributors themselves, at the moment of capture. Kled reviewers check each submission against the task brief.

#### Personal and Sensitive Information

Every item was contributed by its owner, who opted in to this use at upload. The task brief states what may and may not appear in a submission, and reviewers reject submissions that break those rules. Kled's data handling practices are documented at [trust.kled.ai](https://trust.kled.ai/); questions about handling requirements for your use go to [team@kled.ai](mailto:team@kled.ai).

## Bias, Risks, and Limitations

Coverage follows the contributor base: strongest in Southeast Asia, the United States and Europe, thinner elsewhere, and limited to the 54 eligible countries where everyday writing uses a non-Latin script for this task. Devices, settings and conditions vary by contributor, which is the point of the collection and also means no two items are captured under identical conditions. Where labels are contributor-entered, they are checked at review but are not expert annotations. Volumes are the current scope of the task and grow as collection continues.

### Recommendations

Request a sample set and run it against your task before licensing. Ask for per-country or per-language counts where they matter to your use.

## Licensing Information

Non-exclusive commercial training license; exclusivity on request. Each contributor opted in to this use when they uploaded. The license terms are on the [catalog page](https://www.kled.ai/datasets/non-latin-script-text?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=non-latin-script-text).

## Citation

```bibtex
@misc{kled_non_latin_script_text_2026,
  title        = {Non-Latin Scene Text},
  author       = {Kled},
  year         = {2026},
  url          = {https://www.kled.ai/datasets/non-latin-script-text},
  note         = {Commercially licensed dataset collected through the Kled app. Sample sets on request.}
}
```

## Dataset Card Contact

Kled data team: [team@kled.ai](mailto:team@kled.ai)

## Related Kled datasets

- [Six-View Product Photos (10,000 products)](https://huggingface.co/datasets/useKled/all-six-faces-of-one-package)
- [Naturally Failed Photos (150,000 photos)](https://huggingface.co/datasets/useKled/bad-photos-you-d-normally-delete)
- [SEA Construction Sites (5,000 photos)](https://huggingface.co/datasets/useKled/building-sites)
- [Nutrition Label Panels (50,000 photos)](https://huggingface.co/datasets/useKled/food-labels)
