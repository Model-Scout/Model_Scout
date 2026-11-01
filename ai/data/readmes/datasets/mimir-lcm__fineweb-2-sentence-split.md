---
license: odc-by
language:
- ar
- be
- bg
- bn
- bs
- ca
- cs
- cy
- da
- de
- es
- fr
- he
- hi
- hr
- id
- it
- ja
- kn
- ko
- lv
- mk
- ml
- mr
- ne
- nl
- or
- pl
- pt
- ro
- ru
- sk
- sl
- sr
- sv
- sw
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
configs:
  - config_name: arb_Arab
    data_files:
      - split: train
        path: arb_Arab/*
  - config_name: bel_Cyrl
    data_files:
      - split: train
        path: bel_Cyrl/*
  - config_name: ben_Beng
    data_files:
      - split: train
        path: ben_Beng/*
  - config_name: bos_Latn
    data_files:
      - split: train
        path: bos_Latn/*
  - config_name: bul_Cyrl
    data_files:
      - split: train
        path: bul_Cyrl/*
  - config_name: cat_Latn
    data_files:
      - split: train
        path: cat_Latn/*
  - config_name: ces_Latn
    data_files:
      - split: train
        path: ces_Latn/*
  - config_name: cym_Latn
    data_files:
      - split: train
        path: cym_Latn/*
  - config_name: dan_Latn
    data_files:
      - split: train
        path: dan_Latn/*
  - config_name: deu_Latn
    data_files:
      - split: train
        path: deu_Latn/*
  - config_name: fra_Latn
    data_files:
      - split: train
        path: fra_Latn/*
  - config_name: heb_Hebr
    data_files:
      - split: train
        path: heb_Hebr/*
  - config_name: hin_Deva
    data_files:
      - split: train
        path: hin_Deva/*
  - config_name: hrv_Latn
    data_files:
      - split: train
        path: hrv_Latn/*
  - config_name: ind_Latn
    data_files:
      - split: train
        path: ind_Latn/*
  - config_name: ita_Latn
    data_files:
      - split: train
        path: ita_Latn/*
  - config_name: jpn_Jpan
    data_files:
      - split: train
        path: jpn_Jpan/*
  - config_name: kan_Knda
    data_files:
      - split: train
        path: kan_Knda/*
  - config_name: kor_Hang
    data_files:
      - split: train
        path: kor_Hang/*
  - config_name: lvs_Latn
    data_files:
      - split: train
        path: lvs_Latn/*
  - config_name: mal_Mlym
    data_files:
      - split: train
        path: mal_Mlym/*
  - config_name: mar_Deva
    data_files:
      - split: train
        path: mar_Deva/*
  - config_name: mkd_Cyrl
    data_files:
      - split: train
        path: mkd_Cyrl/*
  - config_name: nld_Latn
    data_files:
      - split: train
        path: nld_Latn/*
  - config_name: npi_Deva
    data_files:
      - split: train
        path: npi_Deva/*
  - config_name: ory_Orya
    data_files:
      - split: train
        path: ory_Orya/*
  - config_name: pol_Latn
    data_files:
      - split: train
        path: pol_Latn/*
  - config_name: por_Latn
    data_files:
      - split: train
        path: por_Latn/*
  - config_name: ron_Latn
    data_files:
      - split: train
        path: ron_Latn/*
  - config_name: rus_Cyrl
    data_files:
      - split: train
        path: rus_Cyrl/*
  - config_name: slk_Latn
    data_files:
      - split: train
        path: slk_Latn/*
  - config_name: slv_Latn
    data_files:
      - split: train
        path: slv_Latn/*
  - config_name: spa_Latn
    data_files:
      - split: train
        path: spa_Latn/*
  - config_name: srp_Cyrl
    data_files:
      - split: train
        path: srp_Cyrl/*
  - config_name: swe_Latn
    data_files:
      - split: train
        path: swe_Latn/*
  - config_name: swh_Latn
    data_files:
      - split: train
        path: swh_Latn/*
  - config_name: tam_Taml
    data_files:
      - split: train
        path: tam_Taml/*
  - config_name: tel_Telu
    data_files:
      - split: train
        path: tel_Telu/*
  - config_name: tha_Thai
    data_files:
      - split: train
        path: tha_Thai/*
  - config_name: tur_Latn
    data_files:
      - split: train
        path: tur_Latn/*
  - config_name: ukr_Cyrl
    data_files:
      - split: train
        path: ukr_Cyrl/*
  - config_name: urd_Arab
    data_files:
      - split: train
        path: urd_Arab/*
  - config_name: vie_Latn
    data_files:
      - split: train
        path: vie_Latn/*
  - config_name: zho_Hans
    data_files:
      - split: train
        path: zho_Hans/*
  - config_name: zho_Hant
    data_files:
      - split: train
        path: zho_Hant/*
---

[Fineweb 2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) split into sentences. Instances per languages were sampled by us to balance the data w.r.t. Fineweb-edu.

To split the text into sentences we used the **sat3-l** model from the [wtpsplit](https://github.com/segment-any-text/wtpsplit) library. 

We fix a sentence threshold of 0.02 and a maximum sentence length of 256.

If you use this dataset, you should cite:

```
@misc{penedo2025fineweb2pipelinescale,
  title={FineWeb2: One Pipeline to Scale Them All -- Adapting Pre-Training Data Processing to Every Language}, 
  author={Guilherme Penedo and Hynek Kydlíček and Vinko Sabolčec and Bettina Messmer and Negar Foroutan and Amir Hossein Kargaran and Colin Raffel and Martin Jaggi and Leandro Von Werra and Thomas Wolf},
  year={2025},
  eprint={2506.20920},
  archivePrefix={arXiv},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2506.20920}, 
}

@misc{musacchio2026mimirlargescalemultilingualconcept,
      title={Mimir: Large-scale Multilingual Concept Modeling}, 
      author={Elio Musacchio and Lucia Siciliani and Pierpaolo Basile},
      year={2026},
      eprint={2605.25263},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2605.25263}, 
}
```