---
license: cc-by-nc-nd-4.0
dataset_info:
  features:
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: transcription
    dtype: string
  - name: raw_transcription
    dtype: string
  - name: orthographic_transcription
    dtype: string
  - name: phonetic_transcription
    dtype: string
  splits:
  - name: eval_clean
    num_bytes: 312716074
    num_examples: 3000
  - name: eval_other
    num_bytes: 429021568
    num_examples: 3000
  download_size: 732545966
  dataset_size: 741737642
configs:
- config_name: default
  data_files:
  - split: eval_clean
    path: data/eval_clean-*
  - split: eval_other
    path: data/eval_other-*
language:
- ko
pretty_name: KsponSpeech
---

# Dataset Card for KsponSpeech

## Dataset Description
- **Homepage:** [AIHub KsponSpeech corpus](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=123)
- **Paper:** [KsponSpeech: Korean Spontaneous Speech Corpus for Automatic Speech Recognition](https://www.mdpi.com/2076-3417/10/19/6936)
- **Point of Contact:** [Seung Yun](mailto:syun@etri.re.kr)

### Dataset Summary
The KsponSpeech is a large-scale spontaneous speech corpus in Korean. This corpus contains 969 hours of general open-domain dialog utterances, spoken by approximately 2,000 native Korean speakers in a clean environment. The data was collected by recording dialogues between two people conversing freely on various topics, and then manually transcribing the utterances.
Please note that we are only sharing the evaluation set of KsponSpeech, not the entire dataset. The evaluation set consists of two parts: eval_clean and eval_other. Eval_clean comprises 2.6 hours of audio, 3,000 files, and includes 60 speakers (30 male, 30 female). Eval_other comprises 3.8 hours of audio, 3,000 files, and also includes 60 speakers (30 male, 30 female).
(Note: The training data is provided only to domestic users in Korea.)

## Dataset Structure
### Data Fields

```
{
DatasetDict(
  eval_clean: Dataset({
    features: ['audio', 'transcription', 'raw_transcription', 'orthographic_transcription', 'phonetic_transcription'],
    num_rows: 3000
  })
  eval_other: Dataset({
    features: ['audio', 'transcription', 'raw_transcription', 'orthographic_transcription', 'phonetic_transcription'],
    num_rows: 3000
  })
)
}
```

- audio: A dictionary containing the path to the downloaded audio file, the decoded audio array, and the sampling rate.

- transcription: The transcription of the audio file, equivalent to the orthographic transcription.

- raw_transcription: The original transcript provided by KsponSpeech, including double transcription, disfluent tags, and other annotations.

- orthographic_transcription: Transcription written according to Korean standard orthographic rules.

- phonetic_transcription: Transcription written to reflect the original sound as closely as possible.

### Citation Information

```
@article{bang2020ksponspeech,
  title={Ksponspeech: Korean spontaneous speech corpus for automatic speech recognition},
  author={Bang, Jeong-Uk and Yun, Seung and Kim, Seung-Hi and Choi, Mu-Yeol and Lee, Min-Kyu and Kim, Yeo-Jeong and Kim, Dong-Hyun and Park, Jun and Lee, Young-Jik and Kim, Sang-Hun},
  journal={Applied Sciences},
  volume={10},
  number={19},
  pages={6936},
  year={2020},
  publisher={MDPI}
}
```

