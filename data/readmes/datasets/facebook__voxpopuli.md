---
annotations_creators: []
language:
- en
- de
- fr
- es
- pl
- it
- ro
- hu
- cs
- nl
- fi
- hr
- sk
- sl
- et
- lt
language_creators: []
license:
- cc0-1.0
- other
multilinguality:
- multilingual
pretty_name: VoxPopuli
size_categories: []
source_datasets: []
tags: []
task_categories:
- automatic-speech-recognition
task_ids: []
dataset_info:
- config_name: cs
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 12588060116.726
    num_examples: 18902
  - name: validation
    num_bytes: 700843826.563
    num_examples: 1103
  - name: test
    num_bytes: 714178772.784
    num_examples: 1123
  download_size: 11548798948
  dataset_size: 14003082716.073
- config_name: de
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 61623291127.568
    num_examples: 108473
  - name: validation
    num_bytes: 1149953416.507
    num_examples: 2109
  - name: test
    num_bytes: 1112380619.272
    num_examples: 1968
  download_size: 52639035844
  dataset_size: 63885625163.347
- config_name: en
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 118431996153.336
    num_examples: 182482
  - name: validation
    num_bytes: 1147990403.766
    num_examples: 1753
  - name: test
    num_bytes: 1143640745.808
    num_examples: 1842
  download_size: 98803059660
  dataset_size: 120723627302.91
- config_name: en_accented
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: test
    num_bytes: 6026063102.197
    num_examples: 8387
  download_size: 4946727051
  dataset_size: 6026063102.197
- config_name: es
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 36090680559.936
    num_examples: 50922
  - name: validation
    num_bytes: 1173795492.383
    num_examples: 1631
  - name: test
    num_bytes: 1163226173.4
    num_examples: 1528
  download_size: 31735446877
  dataset_size: 38427702225.719
- config_name: et
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 525978460.0
    num_examples: 834
  - name: validation
    num_bytes: 31718470.0
    num_examples: 50
  - name: test
    num_bytes: 29766659.0
    num_examples: 51
  download_size: 490583763
  dataset_size: 587463589.0
- config_name: fi
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 5231900907.4
    num_examples: 7878
  - name: validation
    num_bytes: 460480456.0
    num_examples: 718
  - name: test
    num_bytes: 304525221.0
    num_examples: 478
  download_size: 4951807012
  dataset_size: 5996906584.4
- config_name: fr
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 48361894011.26
    num_examples: 73561
  - name: validation
    num_bytes: 1150144123.605
    num_examples: 1727
  - name: test
    num_bytes: 1123907283.428
    num_examples: 1742
  download_size: 42134193246
  dataset_size: 50635945418.29301
- config_name: hr
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 8023013076.105
    num_examples: 10987
  - name: validation
    num_bytes: 976946572.365
    num_examples: 1285
  - name: test
    num_bytes: 499681683.0
    num_examples: 666
  download_size: 7764022128
  dataset_size: 9499641331.47
- config_name: hu
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 12401737446.88
    num_examples: 18120
  - name: validation
    num_bytes: 747920493.132
    num_examples: 1076
  - name: test
    num_bytes: 711079430.21
    num_examples: 1110
  download_size: 11578901379
  dataset_size: 13860737370.222
- config_name: it
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 17507657225.08
    num_examples: 22576
  - name: validation
    num_bytes: 1015408546.14
    num_examples: 1257
  - name: test
    num_bytes: 994989586.882
    num_examples: 1177
  download_size: 17099228937
  dataset_size: 19518055358.102
- config_name: lt
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 308829896.0
    num_examples: 456
  - name: validation
    num_bytes: 2897005.0
    num_examples: 3
  - name: test
    num_bytes: 27957133.0
    num_examples: 42
  download_size: 288416179
  dataset_size: 339684034.0
- config_name: multilang
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 381494362201.104
    num_examples: 587798
  - name: validation
    num_bytes: 12204917860.392
    num_examples: 18636
  - name: test
    num_bytes: 10549966622.584
    num_examples: 16991
  download_size: 334147849368
  dataset_size: 404249246684.08
- config_name: nl
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 10439951381.608
    num_examples: 20968
  - name: validation
    num_bytes: 637129232.64
    num_examples: 1230
  - name: test
    num_bytes: 605082732.55
    num_examples: 1137
  download_size: 9841686925
  dataset_size: 11682163346.797998
- config_name: pl
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 22255439519.03
    num_examples: 34665
  - name: validation
    num_bytes: 1128491688.807
    num_examples: 1691
  - name: test
    num_bytes: 1139283257.081
    num_examples: 1831
  download_size: 20560438868
  dataset_size: 24523214464.918
- config_name: ro
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 17342967766.164
    num_examples: 24259
  - name: validation
    num_bytes: 1037009834.212
    num_examples: 1418
  - name: test
    num_bytes: 992719002.245
    num_examples: 1383
  download_size: 16501664145
  dataset_size: 19372696602.621002
- config_name: sk
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 6942255847.456
    num_examples: 10616
  - name: validation
    num_bytes: 458524499.0
    num_examples: 696
  - name: test
    num_bytes: 401681777.0
    num_examples: 604
  download_size: 6419963713
  dataset_size: 7802462123.456
- config_name: sl
  features:
  - name: audio_id
    dtype: string
  - name: language
    dtype:
      class_label:
        names:
          '0': en
          '1': de
          '2': fr
          '3': es
          '4': pl
          '5': it
          '6': ro
          '7': hu
          '8': cs
          '9': nl
          '10': fi
          '11': hr
          '12': sk
          '13': sl
          '14': et
          '15': lt
          '16': en_accented
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: raw_text
    dtype: string
  - name: normalized_text
    dtype: string
  - name: gender
    dtype: string
  - name: speaker_id
    dtype: string
  - name: is_gold_transcript
    dtype: bool
  - name: accent
    dtype: string
  splits:
  - name: train
    num_bytes: 1375125062.8
    num_examples: 2099
  - name: validation
    num_bytes: 637851620.0
    num_examples: 889
  - name: test
    num_bytes: 188485344.0
    num_examples: 309
  download_size: 1798502222
  dataset_size: 2201462026.8
configs:
- config_name: cs
  data_files:
  - split: train
    path: cs/train-*
  - split: validation
    path: cs/validation-*
  - split: test
    path: cs/test-*
- config_name: de
  data_files:
  - split: train
    path: de/train-*
  - split: validation
    path: de/validation-*
  - split: test
    path: de/test-*
- config_name: en
  data_files:
  - split: train
    path: en/train-*
  - split: validation
    path: en/validation-*
  - split: test
    path: en/test-*
- config_name: en_accented
  data_files:
  - split: test
    path: en_accented/test-*
- config_name: es
  data_files:
  - split: train
    path: es/train-*
  - split: validation
    path: es/validation-*
  - split: test
    path: es/test-*
- config_name: et
  data_files:
  - split: train
    path: et/train-*
  - split: validation
    path: et/validation-*
  - split: test
    path: et/test-*
- config_name: fi
  data_files:
  - split: train
    path: fi/train-*
  - split: validation
    path: fi/validation-*
  - split: test
    path: fi/test-*
- config_name: fr
  data_files:
  - split: train
    path: fr/train-*
  - split: validation
    path: fr/validation-*
  - split: test
    path: fr/test-*
- config_name: hr
  data_files:
  - split: train
    path: hr/train-*
  - split: validation
    path: hr/validation-*
  - split: test
    path: hr/test-*
- config_name: hu
  data_files:
  - split: train
    path: hu/train-*
  - split: validation
    path: hu/validation-*
  - split: test
    path: hu/test-*
- config_name: it
  data_files:
  - split: train
    path: it/train-*
  - split: validation
    path: it/validation-*
  - split: test
    path: it/test-*
- config_name: lt
  data_files:
  - split: train
    path: lt/train-*
  - split: validation
    path: lt/validation-*
  - split: test
    path: lt/test-*
- config_name: multilang
  data_files:
  - split: train
    path: multilang/train-*
  - split: validation
    path: multilang/validation-*
  - split: test
    path: multilang/test-*
- config_name: nl
  data_files:
  - split: train
    path: nl/train-*
  - split: validation
    path: nl/validation-*
  - split: test
    path: nl/test-*
- config_name: pl
  data_files:
  - split: train
    path: pl/train-*
  - split: validation
    path: pl/validation-*
  - split: test
    path: pl/test-*
- config_name: ro
  data_files:
  - split: train
    path: ro/train-*
  - split: validation
    path: ro/validation-*
  - split: test
    path: ro/test-*
- config_name: sk
  data_files:
  - split: train
    path: sk/train-*
  - split: validation
    path: sk/validation-*
  - split: test
    path: sk/test-*
- config_name: sl
  data_files:
  - split: train
    path: sl/train-*
  - split: validation
    path: sl/validation-*
  - split: test
    path: sl/test-*
---

# Dataset Card for Voxpopuli

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://github.com/facebookresearch/voxpopuli
- **Repository:** https://github.com/facebookresearch/voxpopuli
- **Paper:** https://arxiv.org/abs/2101.00390
- **Point of Contact:** [changhan@fb.com](mailto:changhan@fb.com), [mriviere@fb.com](mailto:mriviere@fb.com), [annl@fb.com](mailto:annl@fb.com)

### Dataset Summary

VoxPopuli is a large-scale multilingual speech corpus for representation learning, semi-supervised learning and interpretation.
The raw data is collected from 2009-2020 [European Parliament event recordings](https://multimedia.europarl.europa.eu/en/home). We acknowledge the European Parliament for creating and sharing these materials.
This implementation contains transcribed speech data for 18 languages.
It also contains 29 hours of transcribed speech data of non-native English intended for research in ASR for accented speech (15 L2 accents)

### Example usage

VoxPopuli contains labelled data for 18 languages. To load a specific language pass its name as a config name:

```python
from datasets import load_dataset

voxpopuli_croatian = load_dataset("facebook/voxpopuli", "hr")
```

To load all the languages in a single dataset use "multilang" config name:

```python
voxpopuli_all = load_dataset("facebook/voxpopuli", "multilang")
```

To load a specific set of languages, use "multilang" config name and pass a list of required languages to `languages` parameter:

```python
voxpopuli_slavic = load_dataset("facebook/voxpopuli", "multilang", languages=["hr", "sk", "sl", "cs", "pl"])
```

To load accented English data, use "en_accented" config name:

```python
voxpopuli_accented = load_dataset("facebook/voxpopuli", "en_accented")
```

**Note that L2 English subset contains only `test` split.**


### Supported Tasks and Leaderboards

* automatic-speech-recognition: The dataset can be used to train a model for Automatic Speech Recognition (ASR). The model is presented with an audio file and asked to transcribe the audio file to written text. The most common evaluation metric is the word error rate (WER).

Accented English subset can also be used for research in ASR for accented speech (15 L2 accents)

### Languages

VoxPopuli contains labelled (transcribed) data for 18 languages:

| Language | Code | Transcribed Hours | Transcribed Speakers | Transcribed Tokens |
|:---:|:---:|:---:|:---:|:---:|
| English | En | 543 | 1313 | 4.8M |
| German | De | 282 | 531 | 2.3M |
| French | Fr | 211 | 534 | 2.1M |
| Spanish | Es | 166 | 305 | 1.6M |
| Polish | Pl | 111 | 282 | 802K |
| Italian | It | 91 | 306 | 757K |
| Romanian | Ro | 89 | 164 | 739K |
| Hungarian | Hu | 63 | 143 | 431K |
| Czech | Cs | 62 | 138 | 461K |
| Dutch | Nl | 53 | 221 | 488K |
| Finnish | Fi | 27 | 84 | 160K |
| Croatian | Hr | 43 | 83 | 337K |
| Slovak | Sk | 35 | 96 | 270K |
| Slovene | Sl | 10 | 45 | 76K |
| Estonian | Et | 3 | 29 | 18K |
| Lithuanian | Lt | 2 | 21 | 10K |
| Total | | 1791 | 4295 | 15M |


Accented speech transcribed data has 15 various L2 accents:

| Accent | Code | Transcribed Hours | Transcribed Speakers |
|:---:|:---:|:---:|:---:|
| Dutch | en_nl | 3.52 | 45 |
| German | en_de | 3.52 | 84 |
| Czech | en_cs | 3.30 | 26 |
| Polish | en_pl | 3.23 | 33 |
| French | en_fr | 2.56 | 27 |
| Hungarian | en_hu | 2.33 | 23 |
| Finnish | en_fi | 2.18 | 20 |
| Romanian | en_ro | 1.85 | 27 |
| Slovak | en_sk | 1.46 | 17 |
| Spanish | en_es | 1.42 | 18 |
| Italian | en_it | 1.11 | 15 |
| Estonian | en_et | 1.08 | 6 |
| Lithuanian | en_lt | 0.65 | 7 |
| Croatian | en_hr | 0.42 | 9 |
| Slovene | en_sl | 0.25 | 7 |

## Dataset Structure

### Data Instances

```python
{
  'audio_id': '20180206-0900-PLENARY-15-hr_20180206-16:10:06_5',
  'language': 11,  # "hr"
  'audio': {
    'path': '/home/polina/.cache/huggingface/datasets/downloads/extracted/44aedc80bb053f67f957a5f68e23509e9b181cc9e30c8030f110daaedf9c510e/train_part_0/20180206-0900-PLENARY-15-hr_20180206-16:10:06_5.wav',
    'array': array([-0.01434326, -0.01055908,  0.00106812, ...,  0.00646973], dtype=float32),
    'sampling_rate': 16000
  },
  'raw_text': '',
  'normalized_text': 'poast genitalnog sakaenja ena u europi tek je jedna od manifestacija takve tetne politike.',
  'gender': 'female',
  'speaker_id': '119431',
  'is_gold_transcript': True,
  'accent': 'None'
}
```

### Data Fields

* `audio_id` (string) - id of audio segment
* `language` (datasets.ClassLabel) - numerical id of audio segment 
* `audio` (datasets.Audio) - a dictionary containing the path to the audio, the decoded audio array, and the sampling rate. In non-streaming mode (default), the path points to the locally extracted audio. In streaming mode, the path is the relative path of an audio inside its archive (as files are not downloaded and extracted locally).
* `raw_text` (string) - original (orthographic) audio segment text
* `normalized_text` (string) - normalized audio segment transcription
* `gender` (string) - gender of speaker
* `speaker_id` (string) - id of speaker
* `is_gold_transcript` (bool) - ?
* `accent` (string) - type of accent, for example "en_lt", if applicable, else "None".

### Data Splits

All configs (languages) except for accented English contain data in three splits: train, validation and test. Accented English `en_accented` config contains only test split.

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

The raw data is collected from 2009-2020 [European Parliament event recordings](https://multimedia.europarl.europa.eu/en/home)

#### Initial Data Collection and Normalization

The VoxPopuli transcribed set comes from aligning  the full-event source speech audio with the transcripts for plenary sessions. Official timestamps
are available for locating speeches by speaker in the full session, but they are frequently inaccurate, resulting in truncation of the speech or mixture
of fragments from the preceding or the succeeding speeches. To calibrate the original timestamps,
we perform speaker diarization (SD) on the full-session audio using pyannote.audio (Bredin et al.2020) and adopt the nearest SD timestamps (by L1 distance to the original ones) instead for segmentation. 
Full-session audios are segmented into speech paragraphs by speaker, each of which has a transcript available.

The speech paragraphs have an average duration of 197 seconds, which leads to significant. We hence further segment these paragraphs into utterances with a
maximum duration of 20 seconds. We leverage speech recognition (ASR) systems to force-align speech paragraphs to the given transcripts.
The ASR systems are TDS models (Hannun et al., 2019) trained with ASG criterion (Collobert et al., 2016) on audio tracks from in-house deidentified video data.

The resulting utterance segments may have incorrect transcriptions due to incomplete raw transcripts or inaccurate ASR force-alignment. 
We use the predictions from the same ASR systems as references and filter the candidate segments by a maximum threshold of 20% character error rate(CER).

#### Who are the source language producers?

Speakers are participants of the European Parliament events, many of them are EU officials.

### Annotations

#### Annotation process

[More Information Needed]

#### Who are the annotators?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

Gender speakers distribution is imbalanced, percentage of female speakers is mostly lower than 50% across languages, with the minimum of 15% for the Lithuanian language data.

VoxPopuli includes all available speeches from the 2009-2020 EP events without any selections on the topics or speakers.
The speech contents represent the standpoints of the speakers in the EP events, many of which are EU officials.


### Other Known Limitations


## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

The dataset is distributet under CC0 license, see also [European Parliament's legal notice](https://www.europarl.europa.eu/legal-notice/en/) for the raw data.

### Citation Information

Please cite this paper:

```bibtex
@inproceedings{wang-etal-2021-voxpopuli,
    title = "{V}ox{P}opuli: A Large-Scale Multilingual Speech Corpus for Representation Learning, Semi-Supervised Learning and Interpretation",
    author = "Wang, Changhan  and
      Riviere, Morgane  and
      Lee, Ann  and
      Wu, Anne  and
      Talnikar, Chaitanya  and
      Haziza, Daniel  and
      Williamson, Mary  and
      Pino, Juan  and
      Dupoux, Emmanuel",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.80",
    pages = "993--1003",
}
```

### Contributions

Thanks to [@polinaeterna](https://github.com/polinaeterna) for adding this dataset.
