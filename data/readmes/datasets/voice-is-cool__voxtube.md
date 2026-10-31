---
dataset_info:
  homepage: https://idrnd.github.io/VoxTube/
  description: VoxTube - a multilingual speaker recognition dataset
  license: CC-BY-NC-SA-4.0
  citation: "@inproceedings{yakovlev23_interspeech,
  author={Ivan Yakovlev and Anton Okhotnikov and Nikita Torgashov and Rostislav Makarov and Yuri Voevodin and Konstantin Simonchik},
  title={{VoxTube: a multilingual speaker recognition dataset}},
  year=2023,
  booktitle={Proc. INTERSPEECH 2023},
  pages={2238--2242},
  doi={10.21437/Interspeech.2023-1083}
  }"
  features:
  - name: upload_date
    dtype: date32
  - name: segment_id
    dtype: int32
  - name: video_id
    dtype: string
  - name: channel_id
    dtype: string
  - name: language
    dtype: string
  - name: gender
    dtype: string
  - name: spk_id
    dtype: int32
  - name: spk_estim_age
    dtype: float32
  - name: spk_estim_age_mae
    dtype: float32
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  splits:
  - name: train
    num_bytes: 222149986832.446
    num_examples: 4459754
  download_size: 220167447157
  dataset_size: 222149986832.446
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: cc-by-nc-sa-4.0
task_categories:
- audio-classification
language:
- en
- ru
- es
- pt
- fr
- ar
- it
- de
- tr
- nl
- ko
pretty_name: VoxTube
size_categories:
- 1M<n<10M
extra_gated_fields:
  Name: text
  Affiliation: text
  Email: text
  I understand the applicability and accept the limitations of CC-BY-NC-SA license of this dataset that NO commercial usage is allowed: checkbox
  By clicking on "Access repository" below, I agree to not attempt to determine the identity of speakers in the dataset: checkbox

---

# The VoxTube Dataset

The [VoxTube](https://idrnd.github.io/VoxTube) is a multilingual speaker recognition dataset collected from the **CC BY 4.0** YouTube videos. It includes 5.040 speaker identities pronouncing ~4M utterances in 10+ languages. For the underlying data collection and filtering approach details please refer to [[1]](#citation).

## Dataset Structure

### Data Instances

A typical data point comprises the audio signal iself, with additional labels like speaker id / session id (*video_id*) / language / gender etc. 

```
{'upload_date': datetime.date(2018, 5, 2),
 'segment_id': 11,
 'video_id': 'vIpK78CL1so',
 'channel_id': 'UC7rMVNUr7318I0MKumPbIKA',
 'language': 'english',
 'gender': 'male',
 'spk_id': 684,
 'spk_estim_age': 23.5572452545166,
 'spk_estim_age_mae': 3.6162896156311035,
 'audio': {'path': 'UC7rMVNUr7318I0MKumPbIKA/vIpK78CL1so/segment_11.mp3',
  'array': array([-0.00986903, -0.01569703, -0.02005875, ..., -0.00247505,
         -0.01329966, -0.01462782]),
  'sampling_rate': 16000}}
```

### Data Fields

- **channel_id**: YouTube channel ID from which speaker ID (`spk_id`) is derived.
- **video_id**: YouTube video ID, or session for speaker.
- **segment_id**: ID of chunk of video's audio, that passed filtration process. 
- **upload_date**: Date time object representing the date when video was uploaded to YouTube.
- **language**: Language of the channel / speaker.
- **gender**: Gender of the channel / speaker.
- **spk_id**: Infered integer speaker ID from **channel_id**.
- **spk_estim_age**: Label of speaker age (not accurate) based on voice-based automatic age estimation & calibrated based on the upload_date of all videos for a given channel.
- **spk_estim_age_mae**: MAE of **spk_estim_age** (might be considered as confidence).
- **audio**: audio signal of a 4 seconds *mp3* segment from **channel_id/video_id**

## Dataset description

### Main statistics
| Dataset properties           | Stats     |
|:-----------------------------|:----------|
| # of POI                     | 5.040     |
| # of videos                  | 306.248   |
| # of segments                | 4.439.888 |
| # of hours                   | 4.933     |
| Avg # of videos per POI      | 61        |
| Avg # of segments per POI    | 881       |
| Avg length of segments (sec) | 4         |

###  Language and gender distributions
![Distributions](./lang_gender.jpeg)

Language and gender labels of each speaker are available in original repo [here](https://github.com/IDRnD/VoxTube/blob/main/resources/language_gender_meta.csv).

## License

The dataset is licensed under **CC BY-NC-SA 4.0**, please see the complete version of the [license](LICENSE).

Please also note that the provided metadata is relevant on the February 2023 and the corresponding CC BY 4.0 video licenses are valid on that date. ID R&D Inc. is not responsible for changed video license type or if the video was deleted from the YouTube platform. If you want your channel meta to be deleted from the dataset, please [contact ID R&D Inc.](https://www.idrnd.ai/contact-us) with a topic *"VoxTube change request"*.


## Development

Official repository [live repository](https://github.com/IDRnD/VoxTube) for opening issues.

## Citation

Please cite the paper below if you make use of the dataset:

```
@inproceedings{yakovlev23_interspeech,
  author={Ivan Yakovlev and Anton Okhotnikov and Nikita Torgashov and Rostislav Makarov and Yuri Voevodin and Konstantin Simonchik},
  title={{VoxTube: a multilingual speaker recognition dataset}},
  year=2023,
  booktitle={Proc. INTERSPEECH 2023},
  pages={2238--2242},
  doi={10.21437/Interspeech.2023-1083}
}
```````