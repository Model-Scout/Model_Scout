---
license: cc-by-4.0
language:
- zh
- yue
- ja
- ko
- vi
- th
- id
- ms
- hi
- ar
- tr
- fa
- fil
- en
- de
- fr
- es
- pt
- it
- nl
- ru
- pl
- sv
- da
- fi
- cs
- el
- hu
- ro
- mk
tags:
- speech
- asr
- audio
- multilingual
pretty_name: FLEURS Full (Test Set) - 30 Languages
size_categories:
- 10K<n<100K
---

# FLEURS Full - Test Set for ASR Benchmarking

Complete test set of [Google FLEURS](https://huggingface.co/datasets/google/fleurs) for all 30 languages supported by Qwen3-ASR, prepared for benchmarking with [FluidAudio](https://github.com/anthropics/voicelink/tree/main/FluidAudio).

## Languages (30)

### Asian Languages (13)

| Code | Language | Samples |
|------|----------|---------|
| cmn_hans_cn | Chinese (Mandarin) | 945 |
| yue_hant_hk | Cantonese | 819 |
| ja_jp | Japanese | 650 |
| ko_kr | Korean | 382 |
| vi_vn | Vietnamese | 857 |
| th_th | Thai | 1,021 |
| id_id | Indonesian | 687 |
| ms_my | Malay | 749 |
| hi_in | Hindi | 418 |
| ar_eg | Arabic (Egyptian) | 428 |
| tr_tr | Turkish | 743 |
| fa_ir | Persian | 871 |
| fil_ph | Filipino | 964 |

### European Languages (17)

| Code | Language | Samples |
|------|----------|---------|
| en_us | English | 350 |
| de_de | German | 350 |
| fr_fr | French | 350 |
| es_419 | Spanish (Latin America) | 350 |
| pt_br | Portuguese (Brazil) | 919 |
| it_it | Italian | 865 |
| nl_nl | Dutch | 364 |
| ru_ru | Russian | 775 |
| pl_pl | Polish | 758 |
| sv_se | Swedish | 759 |
| da_dk | Danish | 930 |
| fi_fi | Finnish | 918 |
| cs_cz | Czech | 723 |
| el_gr | Greek | 650 |
| hu_hu | Hungarian | 905 |
| ro_ro | Romanian | 883 |
| mk_mk | Macedonian | 973 |

**Total: ~21,000 samples**

## Format

Each language directory contains:
- `{lang_code}.trans.txt` - Transcriptions in format: `file_id transcription`
- `{lang_code}_XXXX.wav` - Audio files (16kHz mono WAV)

## Usage with FluidAudio

```bash
# Run Qwen3-ASR benchmark on all languages
swift run -c release fluidaudiocli qwen3-benchmark --dataset fleurs \
  --languages cmn_hans_cn,yue_hant_hk,ja_jp,ko_kr,vi_vn,th_th,id_id,ms_my,hi_in,ar_eg,tr_tr,fa_ir,fil_ph,en_us,de_de,fr_fr,es_419,pt_br,it_it,nl_nl,ru_ru,pl_pl,sv_se,da_dk,fi_fi,cs_cz,el_gr,hu_hu,ro_ro,mk_mk

# Or benchmark specific languages
swift run -c release fluidaudiocli qwen3-benchmark --dataset fleurs \
  --languages cmn_hans_cn,ja_jp,ko_kr,en_us
```

## Related Datasets

- [alexwengg/fleurs-asia](https://huggingface.co/datasets/alexwengg/fleurs-asia) - Asian languages only
- [FluidInference/fleurs](https://huggingface.co/datasets/FluidInference/fleurs) - European languages (subset)

## Source

Extracted from [Google FLEURS](https://huggingface.co/datasets/google/fleurs) test split.

## License

CC-BY-4.0 (same as original FLEURS)

## Citation

```bibtex
@article{fleurs2022arxiv,
  title = {FLEURS: Few-shot Learning Evaluation of Universal Representations of Speech},
  author = {Conneau, Alexis and Ma, Min and Khanuja, Simran and Zhang, Yu and Axelrod, Vera and Dalmia, Siddharth and Riber, Jason and Talber, Clara and Bapna, Ankur},
  journal={arXiv preprint arXiv:2205.12446},
  year={2022}
}
```
