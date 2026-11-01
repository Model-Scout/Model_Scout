---
license: cc-by-4.0
task_categories:
- question-answering
- automatic-speech-recognition
language:
- ar
- bn
- en
- fi
- gu
- hi
- id
- ja
- kn
- ko
- ml
- mr
- ru
- sw
- ta
- te
- ur
pretty_name: Simple Voice Questions
size_categories:
- 100K<n<1M
configs:
- config_name: audio 
  features: 
    - name: utt_id
      dtype: string
    - name: waveform
      dtype:
        audio:
          sampling_rate: 16000
          decode: false
    - name: locale
      dtype: string
    - name: speaker_id
      dtype: string
    - name: speaker_age
      dtype: int32
    - name: speaker_gender
      dtype: string
    - name: environment
      dtype: string
    - name: text
      dtype: string
    - name: topk_salient_terms
      sequence:
        dtype: string
    - name: topk_salient_terms_timestamps
      sequence:
        sequence:
          dtype: float32
  data_files:
  - split: test
    path: "audio/*.parquet"
- config_name: audio_en_us_clean
  features: 
    - name: utt_id
      dtype: string
    - name: waveform
      dtype:
        audio:
          sampling_rate: 16000
          decode: false
    - name: locale
      dtype: string
    - name: speaker_id
      dtype: string
    - name: speaker_age
      dtype: int32
    - name: speaker_gender
      dtype: string
    - name: environment
      dtype: string
    - name: text
      dtype: string
    - name: topk_salient_terms
      sequence:
        dtype: string
    - name: topk_salient_terms_timestamps
      sequence:
        sequence:
          dtype: float32
  data_files:
  - split: test
    path: "audio/utts_en_us_clean.parquet"
- config_name: document_retrieval_cross_lang
  data_files:
  - split: test
    path: document_retrieval_cross_lang.parquet 
- config_name: document_retrieval_in_lang
  data_files:
  - split: test
    path: document_retrieval_in_lang.parquet 
- config_name: span_retrieval_cross_lang
  data_files:
  - split: test
    path: span_retrieval_cross_lang.parquet 
- config_name: span_retrieval_in_lang
  data_files:
  - split: test
    path: span_retrieval_in_lang.parquet 
- config_name: span_reasoning_cross_lang
  data_files:
  - split: test
    path: span_reasoning_cross_lang.parquet 
- config_name: span_reasoning_in_lang
  data_files:
  - split: test
    path: span_reasoning_in_lang.parquet 
---
# Simple Voice Questions

Simple Voice Questions (SVQ) is a set of short audio questions recorded in 26 locales across 17 languages under multiple audio conditions.

## Data Collection

Speakers were presented with recording instructions specifying the recording environment and text query to be recorded.
They recorded using their own phones or tablets under four conditions:
- clean: Record in quiet environment
- background speech noise: Record while audio from sources like podcasts, talk radio, or YouTube plays on a separate device (e.g., TV, tablet, computer, or another phone) at a normal listening volume, ensuring it is audible in the recording
- traffic noise: Record while speaker is a passenger within a moving vehicle. This includes various forms of transport like buses, trains, and cars (where someone else is driving)
- media noise: Record while background media (music, TV, movies, etc.) is playing on a separate device (TV, tablet, computer, or phone). The playback volume should be a normal listening level,sufficient to be audible in the recording.

In all conditions, speakers were instructed to minimize other background noise (like fans or conversations), hold their phone naturally, avoid extra sounds (like clicks or taps), use wired headphones if applicable, and speak naturally and expressively with emotion.

The query’s text comes from validation and test sets of the XTREME-UP’s retrieval and question answering benchmark datasets. The XTREME-UP dataset is a collection of TYDI QA datasets which are question answering datasets covering 11 typologically diverse languages and the professional translation of the cross-lingual open-retrieval question answering (XOR QA) dataset into 23 Indic languages.

The audio queries were approximately uniformly recorded across the four environmental conditions. To ensure speaker diversity, we attempted to cap the number of recordings per speaker at 250. This resulted in a total of 700unique speakers. We collected speaker gender information in four classes: female, male, non_binary, and no_answer. In addition, speakers were askedto report their age.

## Splits

The audio data in this release is presented as a single, comprehensive collection, rather than being pre-divided into training, validation, or testing subsets.
This decision stems directly from the design of the data acquisition process.
Specifically, text prompts and recording environments were randomly allocated across the speaker cohort.
While this approach promotes a rich variety of conditions, it introduces a complexity for traditional data splitting:
creating partitions that ensure no overlap of speakers and no overlap of text material between splits (a common best practice)
would lead to a substantial data reduction, estimated at around 40% of the total recordings.

The primary goal guiding this release strategy is to maximize the utility and volume of the data available to users.
Therefore, to avoid this significant data loss and provide the fullest possible dataset, the data is released in its entirety
as an undivided evaluation set. Users intending to train models with this data will need to devise and implement their own
splitting strategies, keeping in mind the inherent trade-offs between data volume and strict speaker/text disjointness
if they attempt to replicate such conditions.
