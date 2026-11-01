---
pretty_name: "Korean Conversations"
license: other
license_name: kled-commercial-training-license
license_link: https://www.kled.ai/datasets/conversations-in-korean
language:
- ko
task_categories:
- automatic-speech-recognition
- audio-classification
tags:
- kled
- commercial-license
- consented-data
- human-collected
- sample-on-request
- audio
- speech-audio
- phone-capture
- global
- labeled
- speech
- diarization
- korean
annotations_creators:
- crowdsourced
language_creators:
- crowdsourced
source_datasets:
- original
multilinguality:
- monolingual
viewer: false
gated: manual
extra_gated_heading: "Request a sample set of Korean Conversations"
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
# Dataset Card for Korean Conversations

<p align="center"><img src="https://knrucgucrxvizxlraxgn.supabase.co/storage/v1/object/public/task-images/v3/109/header-dba92921.jpg" alt="Korean Conversations" width="520"></p>

> Natural Korean conversations, 3 to 60 minutes, every participant consenting in-app, speaker turns marked and named.

Collected through the Kled app by consenting contributors and licensed for commercial training. The files are delivered by Kled under license, not downloaded from this repository. Use **Request a sample set** at the top of this page, or write to [team@kled.ai](mailto:team@kled.ai). Catalog entry: [kled.ai/datasets/conversations-in-korean](https://www.kled.ai/datasets/conversations-in-korean?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=conversations-in-korean).

## Dataset Details

### Dataset Description

Adults talk naturally for three minutes to an hour, with every speaker confirming consent inside the app before the recording starts, so consent is recorded for every participant, not merely the uploader. Nothing is scripted or prompted. Speakers are separated in the app: the contributor marks each speaker change as it happens and assigns it to a named participant, so every recording ships as a master track plus per-speaker turn segments. Audio comes from a phone microphone in the room, so there is natural overlap and room acoustics, the conditions diarization systems break on; no transcripts. Korean conversational speech is otherwise locked up: AI Hub's corpora, KsponSpeech among them, are released to Korean nationals and need separate approval for overseas use. This one is commercially licensed.

- **Curated by:** Kled ([useKled](https://huggingface.co/useKled))
- **Collected through:** Phone microphone (in app)
- **Language(s):** Korean
- **Regions:** Global, 100+ countries
- **Volume:** 500+ hours (approx. 30 GB)
- **Contributors:** 2,000+
- **Modality:** Audio
- **Format:** M4A
- **Resolution:** M4A (AAC) at the phone's native sample rate
- **Annotations:** Labeled (named speaker turns, master track plus per-speaker segments)
- **Quality control:** 99%+ passed QA review
- **License:** Non-exclusive commercial training license ([terms](https://www.kled.ai/datasets/conversations-in-korean?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=conversations-in-korean)); exclusivity available on request
- **Consent:** Each contributor opted in to this use when they uploaded.

### Dataset Sources

- **Catalog page:** [kled.ai/datasets/conversations-in-korean](https://www.kled.ai/datasets/conversations-in-korean?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=conversations-in-korean)
- **Sample set:** through the access request at the top of this page, or [team@kled.ai](mailto:team@kled.ai)
- **Publisher:** [huggingface.co/useKled](https://huggingface.co/useKled)

## Uses

### Direct Use

- Korean conversational ASR
- Diarization training with named speaker turns
- Dialogue and turn-taking modeling

### Out-of-Scope Use

Redistribution or resale of the files, use outside the terms of the commercial training license, and any attempt to identify or contact contributors or people who appear in the data. Uses that require labels this set does not carry should be scoped with the data team first.

## Dataset Structure

### Data Instances

One recording per record, delivered as M4A. Volume: 500+ hours.

### Data Fields

- **File:** the M4A file as captured or uploaded by the contributor
- **Labels:** Labeled (named speaker turns, master track plus per-speaker segments), entered by the contributor at capture and checked at review.
- **Capture metadata:** capture tool, country of capture, submission time
- **Review status:** QA outcome (99%+ passed QA review)

Field names and the manifest format are confirmed with the sample set.

### Data Splits

Delivered as one set. Subsets by country, language or label, and custom splits, are available on request.

## Dataset Creation

### Curation Rationale

The dataset exists because the public alternatives named in the description are non-commercial, synthetic, small or collected elsewhere. Kled runs the task as a paid brief in its app so that the data is captured on purpose, under the capture rules above, by people who have opted in to commercial use.

### Source Data

#### Data Collection and Processing

Contributors complete the task in the Kled app. Capture tool: Phone microphone (in app). Each submission is reviewed against the task brief; submissions that break the capture rules are rejected. 99%+ passed QA review. Files are delivered as M4A, in the resolution noted above.

#### Who are the source data producers?

Kled contributors, who complete paid data tasks on their own phones. This task was open to contributors worldwide. Kled has 625,000+ contributors in 100+ countries, strongest in Southeast Asia, the United States and Europe.

### Annotations

#### Annotation process

Labeled (named speaker turns, master track plus per-speaker segments). The label is entered by the contributor as part of the task and checked at review against the task brief; it is a contributor label, not an expert annotation, unless the description above says otherwise.

#### Who are the annotators?

The contributors themselves, at the moment of capture. Kled reviewers check each submission against the task brief.

#### Personal and Sensitive Information

Every item was contributed by its owner, who opted in to this use at upload. The task brief states what may and may not appear in a submission, and reviewers reject submissions that break those rules. Kled's data handling practices are documented at [trust.kled.ai](https://trust.kled.ai/); questions about handling requirements for your use go to [team@kled.ai](mailto:team@kled.ai).

## Bias, Risks, and Limitations

Coverage follows the contributor base: strongest in Southeast Asia, the United States and Europe, thinner elsewhere, and not limited by region for this task. Devices, settings and conditions vary by contributor, which is the point of the collection and also means no two items are captured under identical conditions. Where labels are contributor-entered, they are checked at review but are not expert annotations. Volumes are the current scope of the task and grow as collection continues.

### Recommendations

Request a sample set and run it against your task before licensing. Ask for per-country or per-language counts where they matter to your use.

## Licensing Information

Non-exclusive commercial training license; exclusivity on request. Each contributor opted in to this use when they uploaded. The license terms are on the [catalog page](https://www.kled.ai/datasets/conversations-in-korean?utm_source=huggingface&utm_medium=dataset_card&utm_campaign=conversations-in-korean).

## Citation

```bibtex
@misc{kled_conversations_in_korean_2026,
  title        = {Korean Conversations},
  author       = {Kled},
  year         = {2026},
  url          = {https://www.kled.ai/datasets/conversations-in-korean},
  note         = {Commercially licensed dataset collected through the Kled app. Sample sets on request.}
}
```

## Dataset Card Contact

Kled data team: [team@kled.ai](mailto:team@kled.ai)

## Related Kled datasets

- [Consented Group Conversations](https://huggingface.co/datasets/useKled/record-a-conversation-with-someone)
- [Full Support Conversations (5,000 threads)](https://huggingface.co/datasets/useKled/customer-support-conversations)
- [Read Speech, 2,800 Phrases (500,000 clips)](https://huggingface.co/datasets/useKled/read-these-phrases-aloud)
- [Speech in Real Noise (10,000 clips)](https://huggingface.co/datasets/useKled/record-in-a-noisy-place)
