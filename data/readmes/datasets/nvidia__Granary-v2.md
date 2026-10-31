---
license:
- openmdw-1.1
- cc-by-sa-4.0
task_categories:
- automatic-speech-recognition
- translation
- audio-text-to-text
- question-answering
language:
- ar
- as
- bg
- bn
- cs
- da
- de
- el
- en
- es
- et
- fa
- fi
- fil
- fr
- gu
- he
- hi
- hr
- hu
- id
- it
- ja
- kn
- ko
- lt
- lv
- ml
- mr
- mt
- nl
- or
- pa
- pl
- pt
- ro
- ru
- sk
- sl
- sv
- ta
- te
- th
- tr
- uk
- ur
- vi
- zh
pretty_name: Granary-v2
tags:
- granary
- multilingual
- nemo
- speech
dataset_info:
- config_name: ar
  features: &granary_en
  - name: audio_filepath
    dtype: string
  - name: duration
    dtype: float64
  - name: corpus
    dtype: string
  - name: source_lang
    dtype: string
  - name: tn_raw
    dtype: string
  - name: itn_raw
    dtype: string
  - name: itn_clean
    dtype: string
  - name: captioning_text
    dtype: string
  - name: code_switched_text
    dtype: string
  - name: speech_qa_text
    dtype: string
  - name: context_asr
    struct:
    - name: coarse_context_terms
      list: string
    - name: fine_context_terms
      list: string
    - name: distractor_terms
      list: string
    - name: confidence_coarse
      dtype: int64
    - name: confidence_fine
      dtype: int64
    - name: speaking_style
      dtype: string
    - name: estimated_difficulty
      dtype: int64
    - name: coarse_context_prompt
      dtype: string
    - name: fine_context_prompt
      dtype: string
    - name: distractor_prompt
      dtype: string
    - name: partial_context_prompt
      dtype: string
    - name: negative_context_prompt
      dtype: string
    - name: entity_categories
      struct:
      - name: person_name
        list: string
      - name: company_name
        list: string
      - name: product_name
        list: string
      - name: drug_name
        list: string
      - name: location_name
        list: string
      - name: organization_name
        list: string
      - name: event_name
        list: string
      - name: technical_term
        list: string
      - name: abbreviation
        list: string
  - name: translations
    struct:
    - name: en
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
  - name: preference_instructions
    list:
    - name: prompt
      dtype: string
    - name: target
      dtype: string
    - name: tags
      struct:
      - name: type
        dtype: string
      - name: target_lang
        dtype: string
  - name: high_quality
    dtype: bool
- config_name: ar_fleurs
  features: *granary_en
- config_name: as
  features: *granary_en
- config_name: as_fleurs
  features: *granary_en
- config_name: as_mcv26
  features: *granary_en
- config_name: bg
  features: &granary_fanout
  - name: audio_filepath
    dtype: string
  - name: duration
    dtype: float64
  - name: corpus
    dtype: string
  - name: source_lang
    dtype: string
  - name: tn_raw
    dtype: string
  - name: itn_raw
    dtype: string
  - name: itn_clean
    dtype: string
  - name: captioning_text
    dtype: string
  - name: code_switched_text
    dtype: string
  - name: speech_qa_text
    dtype: string
  - name: context_asr
    struct:
    - name: coarse_context_terms
      list: string
    - name: fine_context_terms
      list: string
    - name: distractor_terms
      list: string
    - name: confidence_coarse
      dtype: int64
    - name: confidence_fine
      dtype: int64
    - name: speaking_style
      dtype: string
    - name: estimated_difficulty
      dtype: int64
    - name: coarse_context_prompt
      dtype: string
    - name: fine_context_prompt
      dtype: string
    - name: distractor_prompt
      dtype: string
    - name: partial_context_prompt
      dtype: string
    - name: negative_context_prompt
      dtype: string
    - name: entity_categories
      struct:
      - name: person_name
        list: string
      - name: company_name
        list: string
      - name: product_name
        list: string
      - name: drug_name
        list: string
      - name: location_name
        list: string
      - name: organization_name
        list: string
      - name: event_name
        list: string
      - name: technical_term
        list: string
      - name: abbreviation
        list: string
  - name: translations
    struct:
    - name: en
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: ar
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: bg
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: cs
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: da
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: de
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: el
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: es
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: et
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: fi
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: fr
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: he
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: hi
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: hr
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: hu
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: it
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: ja
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: ko
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: lt
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: lv
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: mt
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: nl
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: pl
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: pt
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: ro
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: ru
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: sk
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: sl
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: sv
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: th
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: uk
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
    - name: zh
      struct:
      - name: translation_raw
        dtype: string
      - name: translation_quality_score
        dtype: float64
  - name: preference_instructions
    list:
    - name: prompt
      dtype: string
    - name: target
      dtype: string
    - name: tags
      struct:
      - name: type
        dtype: string
      - name: target_lang
        dtype: string
  - name: high_quality
    dtype: bool
- config_name: bg_fleurs
  features: *granary_en
- config_name: bg_mcv26
  features: *granary_en
- config_name: bg_voxpopuli
  features: *granary_fanout
- config_name: bn
  features: *granary_en
- config_name: bn_fleurs
  features: *granary_en
- config_name: bn_mcv26
  features: *granary_en
- config_name: cs
  features: *granary_fanout
- config_name: cs_fleurs
  features: *granary_en
- config_name: cs_mcv26
  features: *granary_en
- config_name: cs_voxpopuli
  features: *granary_fanout
- config_name: cs_voxpopuli_improved
  features: *granary_en
- config_name: da
  features: *granary_fanout
- config_name: da_fleurs
  features: *granary_en
- config_name: da_mcv26
  features: *granary_en
- config_name: da_voxpopuli
  features: *granary_fanout
- config_name: de
  features: *granary_fanout
- config_name: de_fleurs
  features: *granary_en
- config_name: de_mcv26
  features: *granary_en
- config_name: de_mls
  features: *granary_en
- config_name: de_voxpopuli
  features: *granary_fanout
- config_name: de_voxpopuli_improved
  features: *granary_en
- config_name: el
  features: *granary_fanout
- config_name: el_fleurs
  features: *granary_en
- config_name: el_mcv26
  features: *granary_en
- config_name: el_voxpopuli
  features: *granary_fanout
- config_name: en
  features: *granary_fanout
- config_name: en_ami
  features: *granary_fanout
- config_name: en_europarl
  features: *granary_fanout
- config_name: en_fleurs
  features: *granary_fanout
- config_name: en_google_speech_commands
  features: *granary_fanout
- config_name: en_librilight
  features: *granary_fanout
- config_name: en_librispeech_pc
  features: *granary_fanout
- config_name: en_mcv26
  features: *granary_fanout
- config_name: en_mls
  features: *granary_fanout
- config_name: en_nsc
  features: *granary_fanout
- config_name: en_people_speech
  features: *granary_fanout
- config_name: en_vctk
  features: *granary_fanout
- config_name: en_voxpopuli
  features: *granary_fanout
- config_name: en_voxpopuli_improved
  features: *granary_fanout
- config_name: es
  features: *granary_fanout
- config_name: es_fleurs
  features: *granary_en
- config_name: es_mcv26
  features: *granary_en
- config_name: es_mls
  features: *granary_en
- config_name: es_voxpopuli
  features: *granary_fanout
- config_name: es_voxpopuli_improved
  features: *granary_en
- config_name: et
  features: *granary_fanout
- config_name: et_fleurs
  features: *granary_en
- config_name: et_mcv26
  features: *granary_en
- config_name: et_voxpopuli
  features: *granary_fanout
- config_name: et_voxpopuli_improved
  features: *granary_en
- config_name: fa
  features: *granary_en
- config_name: fa_fleurs
  features: *granary_en
- config_name: fi
  features: *granary_fanout
- config_name: fi_fleurs
  features: *granary_en
- config_name: fi_mcv26
  features: *granary_en
- config_name: fi_voxpopuli
  features: *granary_fanout
- config_name: fi_voxpopuli_improved
  features: *granary_en
- config_name: fil
  features: *granary_en
- config_name: fil_fleurs
  features: *granary_en
- config_name: fr
  features: *granary_fanout
- config_name: fr_fleurs
  features: *granary_en
- config_name: fr_mcv26
  features: *granary_en
- config_name: fr_mls
  features: *granary_en
- config_name: fr_voxpopuli
  features: *granary_fanout
- config_name: fr_voxpopuli_improved
  features: *granary_en
- config_name: gu
  features: *granary_en
- config_name: gu_fleurs
  features: *granary_en
- config_name: he
  features: *granary_en
- config_name: he_fleurs
  features: *granary_en
- config_name: he_mcv26
  features: *granary_en
- config_name: hi
  features: *granary_en
- config_name: hi_fleurs
  features: *granary_en
- config_name: hi_mcv26
  features: *granary_en
- config_name: hr
  features: *granary_fanout
- config_name: hr_fleurs
  features: *granary_en
- config_name: hr_mcv26
  features: *granary_en
- config_name: hr_voxpopuli
  features: *granary_fanout
- config_name: hr_voxpopuli_improved
  features: *granary_en
- config_name: hu
  features: *granary_fanout
- config_name: hu_fleurs
  features: *granary_en
- config_name: hu_mcv26
  features: *granary_en
- config_name: hu_voxpopuli
  features: *granary_fanout
- config_name: hu_voxpopuli_improved
  features: *granary_en
- config_name: id
  features: *granary_en
- config_name: id_fleurs
  features: *granary_en
- config_name: it
  features: *granary_fanout
- config_name: it_fleurs
  features: *granary_en
- config_name: it_mcv26
  features: *granary_en
- config_name: it_mls
  features: *granary_en
- config_name: it_voxpopuli
  features: *granary_fanout
- config_name: it_voxpopuli_improved
  features: *granary_en
- config_name: ja
  features: *granary_en
- config_name: ja_fleurs
  features: *granary_en
- config_name: ja_mcv26
  features: *granary_en
- config_name: kn
  features: *granary_en
- config_name: kn_fleurs
  features: *granary_en
- config_name: ko
  features: *granary_en
- config_name: ko_fleurs
  features: *granary_en
- config_name: ko_mcv26
  features: *granary_en
- config_name: lt
  features: *granary_fanout
- config_name: lt_fleurs
  features: *granary_en
- config_name: lt_mcv26
  features: *granary_en
- config_name: lt_voxpopuli
  features: *granary_fanout
- config_name: lt_voxpopuli_improved
  features: *granary_en
- config_name: lv
  features: *granary_fanout
- config_name: lv_fleurs
  features: *granary_en
- config_name: lv_mcv26
  features: *granary_en
- config_name: lv_voxpopuli
  features: *granary_fanout
- config_name: ml
  features: *granary_en
- config_name: ml_fleurs
  features: *granary_en
- config_name: ml_mcv26
  features: *granary_en
- config_name: mr
  features: *granary_en
- config_name: mr_fleurs
  features: *granary_en
- config_name: mr_mcv26
  features: *granary_en
- config_name: mt
  features: *granary_fanout
- config_name: mt_fleurs
  features: *granary_en
- config_name: mt_mcv26
  features: *granary_en
- config_name: mt_voxpopuli
  features: *granary_fanout
- config_name: nl
  features: *granary_fanout
- config_name: nl_fleurs
  features: *granary_en
- config_name: nl_mcv26
  features: *granary_en
- config_name: nl_mls
  features: *granary_en
- config_name: nl_voxpopuli
  features: *granary_fanout
- config_name: nl_voxpopuli_improved
  features: *granary_en
- config_name: or
  features: *granary_en
- config_name: or_fleurs
  features: *granary_en
- config_name: or_mcv26
  features: *granary_en
- config_name: pa
  features: *granary_en
- config_name: pa_fleurs
  features: *granary_en
- config_name: pa_mcv26
  features: *granary_en
- config_name: pl
  features: *granary_fanout
- config_name: pl_fleurs
  features: *granary_en
- config_name: pl_mcv26
  features: *granary_en
- config_name: pl_mls
  features: *granary_en
- config_name: pl_voxpopuli
  features: *granary_fanout
- config_name: pl_voxpopuli_improved
  features: *granary_en
- config_name: pt
  features: *granary_fanout
- config_name: pt_falar
  features: *granary_en
- config_name: pt_fleurs
  features: *granary_en
- config_name: pt_mcv26
  features: *granary_en
- config_name: pt_mls
  features: *granary_en
- config_name: pt_voxpopuli
  features: *granary_fanout
- config_name: ro
  features: *granary_fanout
- config_name: ro_fleurs
  features: *granary_en
- config_name: ro_mcv26
  features: *granary_en
- config_name: ro_voxpopuli
  features: *granary_fanout
- config_name: ro_voxpopuli_improved
  features: *granary_en
- config_name: ru
  features: *granary_en
- config_name: ru_dusha
  features: *granary_en
- config_name: ru_fleurs
  features: *granary_en
- config_name: ru_golos
  features: *granary_en
- config_name: ru_mcv26
  features: *granary_en
- config_name: sk
  features: *granary_fanout
- config_name: sk_fleurs
  features: *granary_en
- config_name: sk_mcv26
  features: *granary_en
- config_name: sk_voxpopuli
  features: *granary_fanout
- config_name: sk_voxpopuli_improved
  features: *granary_en
- config_name: sl
  features: *granary_fanout
- config_name: sl_fleurs
  features: *granary_en
- config_name: sl_mcv26
  features: *granary_en
- config_name: sl_voxpopuli
  features: *granary_fanout
- config_name: sl_voxpopuli_improved
  features: *granary_en
- config_name: sv
  features: *granary_fanout
- config_name: sv_fleurs
  features: *granary_en
- config_name: sv_mcv26
  features: *granary_en
- config_name: sv_voxpopuli
  features: *granary_fanout
- config_name: ta
  features: *granary_en
- config_name: ta_fleurs
  features: *granary_en
- config_name: te
  features: *granary_en
- config_name: te_fleurs
  features: *granary_en
- config_name: te_mcv26
  features: *granary_en
- config_name: th
  features: *granary_en
- config_name: th_fleurs
  features: *granary_en
- config_name: th_mcv26
  features: *granary_en
- config_name: tr
  features: *granary_en
- config_name: tr_fleurs
  features: *granary_en
- config_name: uk
  features: *granary_en
- config_name: uk_fleurs
  features: *granary_en
- config_name: uk_mcv26
  features: *granary_en
- config_name: ur
  features: *granary_en
- config_name: ur_fleurs
  features: *granary_en
- config_name: ur_mcv26
  features: *granary_en
- config_name: vi
  features: *granary_en
- config_name: vi_fleurs
  features: *granary_en
- config_name: vi_mcv26
  features: *granary_en
- config_name: zh
  features: *granary_en
- config_name: zh_fleurs
  features: *granary_en
configs:
- config_name: ar_fleurs
  data_files:
  - path:
    - ar/fleurs/ar_asr.jsonl.gz
    split: asr
- config_name: as_fleurs
  data_files:
  - path:
    - as/fleurs/as_asr.jsonl.gz
    split: asr
- config_name: as_mcv26
  data_files:
  - path:
    - as/mcv26/as_asr.jsonl.gz
    split: asr
- config_name: bg_fleurs
  data_files:
  - path:
    - bg/fleurs/bg_asr.jsonl.gz
    split: asr
- config_name: bg_mcv26
  data_files:
  - path:
    - bg/mcv26/bg_asr.jsonl.gz
    split: asr
- config_name: bg_voxpopuli
  data_files:
  - path:
    - bg/voxpopuli/bg_asr.jsonl.gz
    split: asr
- config_name: bn_fleurs
  data_files:
  - path:
    - bn/fleurs/bn_asr.jsonl.gz
    split: asr
- config_name: bn_mcv26
  data_files:
  - path:
    - bn/mcv26/bn_asr.jsonl.gz
    split: asr
- config_name: cs_fleurs
  data_files:
  - path:
    - cs/fleurs/cs_asr.jsonl.gz
    split: asr
- config_name: cs_mcv26
  data_files:
  - path:
    - cs/mcv26/cs_asr.jsonl.gz
    split: asr
- config_name: cs_voxpopuli
  data_files:
  - path:
    - cs/voxpopuli/cs_asr.jsonl.gz
    split: asr
- config_name: cs_voxpopuli_improved
  data_files:
  - path:
    - cs/voxpopuli_improved/cs_asr.jsonl.gz
    split: asr
- config_name: da_fleurs
  data_files:
  - path:
    - da/fleurs/da_asr.jsonl.gz
    split: asr
- config_name: da_mcv26
  data_files:
  - path:
    - da/mcv26/da_asr.jsonl.gz
    split: asr
- config_name: da_voxpopuli
  data_files:
  - path:
    - da/voxpopuli/da_asr.jsonl.gz
    split: asr
- config_name: de_fleurs
  data_files:
  - path:
    - de/fleurs/de_asr.jsonl.gz
    split: asr
- config_name: de_mcv26
  data_files:
  - path:
    - de/mcv26/de_asr.jsonl.gz
    split: asr
- config_name: de_mls
  data_files:
  - path:
    - de/mls/de_asr.jsonl.gz
    split: asr
- config_name: de_voxpopuli
  data_files:
  - path:
    - de/voxpopuli/de_asr.jsonl.gz
    split: asr
- config_name: de_voxpopuli_improved
  data_files:
  - path:
    - de/voxpopuli_improved/de_asr.jsonl.gz
    split: asr
- config_name: el_fleurs
  data_files:
  - path:
    - el/fleurs/el_asr.jsonl.gz
    split: asr
- config_name: el_mcv26
  data_files:
  - path:
    - el/mcv26/el_asr.jsonl.gz
    split: asr
- config_name: el_voxpopuli
  data_files:
  - path:
    - el/voxpopuli/el_asr.jsonl.gz
    split: asr
- config_name: en_ami
  data_files:
  - path:
    - en/ami/en_asr.jsonl.gz
    split: asr
- config_name: en_europarl
  data_files:
  - path:
    - en/europarl/en_asr.jsonl.gz
    split: asr
- config_name: en_fleurs
  data_files:
  - path:
    - en/fleurs/en_asr.jsonl.gz
    split: asr
- config_name: en_google_speech_commands
  data_files:
  - path:
    - en/google_speech_commands/en_asr.jsonl.gz
    split: asr
- config_name: en_librilight
  data_files:
  - path:
    - en/librilight/en_asr.part00.jsonl.gz
    - en/librilight/en_asr.part01.jsonl.gz
    - en/librilight/en_asr.part02.jsonl.gz
    - en/librilight/en_asr.part03.jsonl.gz
    split: asr
- config_name: en_librispeech_pc
  data_files:
  - path:
    - en/librispeech_pc/en_asr.jsonl.gz
    split: asr
- config_name: en_mcv26
  data_files:
  - path:
    - en/mcv26/en_asr.jsonl.gz
    split: asr
- config_name: en_mls
  data_files:
  - path:
    - en/mls/en_asr.jsonl.gz
    split: asr
- config_name: en_nsc
  data_files:
  - path:
    - en/nsc/en_asr.jsonl.gz
    split: asr
- config_name: en_people_speech
  data_files:
  - path:
    - en/people_speech/en_asr.jsonl.gz
    split: asr
- config_name: en_vctk
  data_files:
  - path:
    - en/vctk/en_asr.jsonl.gz
    split: asr
- config_name: en_voxpopuli
  data_files:
  - path:
    - en/voxpopuli/en_asr.jsonl.gz
    split: asr
- config_name: en_voxpopuli_improved
  data_files:
  - path:
    - en/voxpopuli_improved/en_asr.jsonl.gz
    split: asr
- config_name: es_fleurs
  data_files:
  - path:
    - es/fleurs/es_asr.jsonl.gz
    split: asr
- config_name: es_mcv26
  data_files:
  - path:
    - es/mcv26/es_asr.jsonl.gz
    split: asr
- config_name: es_mls
  data_files:
  - path:
    - es/mls/es_asr.jsonl.gz
    split: asr
- config_name: es_voxpopuli
  data_files:
  - path:
    - es/voxpopuli/es_asr.jsonl.gz
    split: asr
- config_name: es_voxpopuli_improved
  data_files:
  - path:
    - es/voxpopuli_improved/es_asr.jsonl.gz
    split: asr
- config_name: et_fleurs
  data_files:
  - path:
    - et/fleurs/et_asr.jsonl.gz
    split: asr
- config_name: et_mcv26
  data_files:
  - path:
    - et/mcv26/et_asr.jsonl.gz
    split: asr
- config_name: et_voxpopuli
  data_files:
  - path:
    - et/voxpopuli/et_asr.jsonl.gz
    split: asr
- config_name: et_voxpopuli_improved
  data_files:
  - path:
    - et/voxpopuli_improved/et_asr.jsonl.gz
    split: asr
- config_name: fa_fleurs
  data_files:
  - path:
    - fa/fleurs/fa_asr.jsonl.gz
    split: asr
- config_name: fi_fleurs
  data_files:
  - path:
    - fi/fleurs/fi_asr.jsonl.gz
    split: asr
- config_name: fi_mcv26
  data_files:
  - path:
    - fi/mcv26/fi_asr.jsonl.gz
    split: asr
- config_name: fi_voxpopuli
  data_files:
  - path:
    - fi/voxpopuli/fi_asr.jsonl.gz
    split: asr
- config_name: fi_voxpopuli_improved
  data_files:
  - path:
    - fi/voxpopuli_improved/fi_asr.jsonl.gz
    split: asr
- config_name: fil_fleurs
  data_files:
  - path:
    - fil/fleurs/fil_asr.jsonl.gz
    split: asr
- config_name: fr_fleurs
  data_files:
  - path:
    - fr/fleurs/fr_asr.jsonl.gz
    split: asr
- config_name: fr_mcv26
  data_files:
  - path:
    - fr/mcv26/fr_asr.jsonl.gz
    split: asr
- config_name: fr_mls
  data_files:
  - path:
    - fr/mls/fr_asr.jsonl.gz
    split: asr
- config_name: fr_voxpopuli
  data_files:
  - path:
    - fr/voxpopuli/fr_asr.jsonl.gz
    split: asr
- config_name: fr_voxpopuli_improved
  data_files:
  - path:
    - fr/voxpopuli_improved/fr_asr.jsonl.gz
    split: asr
- config_name: gu_fleurs
  data_files:
  - path:
    - gu/fleurs/gu_asr.jsonl.gz
    split: asr
- config_name: he_fleurs
  data_files:
  - path:
    - he/fleurs/he_asr.jsonl.gz
    split: asr
- config_name: he_mcv26
  data_files:
  - path:
    - he/mcv26/he_asr.jsonl.gz
    split: asr
- config_name: hi_fleurs
  data_files:
  - path:
    - hi/fleurs/hi_asr.jsonl.gz
    split: asr
- config_name: hi_mcv26
  data_files:
  - path:
    - hi/mcv26/hi_asr.jsonl.gz
    split: asr
- config_name: hr_fleurs
  data_files:
  - path:
    - hr/fleurs/hr_asr.jsonl.gz
    split: asr
- config_name: hr_mcv26
  data_files:
  - path:
    - hr/mcv26/hr_asr.jsonl.gz
    split: asr
- config_name: hr_voxpopuli
  data_files:
  - path:
    - hr/voxpopuli/hr_asr.jsonl.gz
    split: asr
- config_name: hr_voxpopuli_improved
  data_files:
  - path:
    - hr/voxpopuli_improved/hr_asr.jsonl.gz
    split: asr
- config_name: hu_fleurs
  data_files:
  - path:
    - hu/fleurs/hu_asr.jsonl.gz
    split: asr
- config_name: hu_mcv26
  data_files:
  - path:
    - hu/mcv26/hu_asr.jsonl.gz
    split: asr
- config_name: hu_voxpopuli
  data_files:
  - path:
    - hu/voxpopuli/hu_asr.jsonl.gz
    split: asr
- config_name: hu_voxpopuli_improved
  data_files:
  - path:
    - hu/voxpopuli_improved/hu_asr.jsonl.gz
    split: asr
- config_name: id_fleurs
  data_files:
  - path:
    - id/fleurs/id_asr.jsonl.gz
    split: asr
- config_name: it_fleurs
  data_files:
  - path:
    - it/fleurs/it_asr.jsonl.gz
    split: asr
- config_name: it_mcv26
  data_files:
  - path:
    - it/mcv26/it_asr.jsonl.gz
    split: asr
- config_name: it_mls
  data_files:
  - path:
    - it/mls/it_asr.jsonl.gz
    split: asr
- config_name: it_voxpopuli
  data_files:
  - path:
    - it/voxpopuli/it_asr.jsonl.gz
    split: asr
- config_name: it_voxpopuli_improved
  data_files:
  - path:
    - it/voxpopuli_improved/it_asr.jsonl.gz
    split: asr
- config_name: ja_fleurs
  data_files:
  - path:
    - ja/fleurs/ja_asr.jsonl.gz
    split: asr
- config_name: ja_mcv26
  data_files:
  - path:
    - ja/mcv26/ja_asr.jsonl.gz
    split: asr
- config_name: kn_fleurs
  data_files:
  - path:
    - kn/fleurs/kn_asr.jsonl.gz
    split: asr
- config_name: ko_fleurs
  data_files:
  - path:
    - ko/fleurs/ko_asr.jsonl.gz
    split: asr
- config_name: ko_mcv26
  data_files:
  - path:
    - ko/mcv26/ko_asr.jsonl.gz
    split: asr
- config_name: lt_fleurs
  data_files:
  - path:
    - lt/fleurs/lt_asr.jsonl.gz
    split: asr
- config_name: lt_mcv26
  data_files:
  - path:
    - lt/mcv26/lt_asr.jsonl.gz
    split: asr
- config_name: lt_voxpopuli
  data_files:
  - path:
    - lt/voxpopuli/lt_asr.jsonl.gz
    split: asr
- config_name: lt_voxpopuli_improved
  data_files:
  - path:
    - lt/voxpopuli_improved/lt_asr.jsonl.gz
    split: asr
- config_name: lv_fleurs
  data_files:
  - path:
    - lv/fleurs/lv_asr.jsonl.gz
    split: asr
- config_name: lv_mcv26
  data_files:
  - path:
    - lv/mcv26/lv_asr.jsonl.gz
    split: asr
- config_name: lv_voxpopuli
  data_files:
  - path:
    - lv/voxpopuli/lv_asr.jsonl.gz
    split: asr
- config_name: ml_fleurs
  data_files:
  - path:
    - ml/fleurs/ml_asr.jsonl.gz
    split: asr
- config_name: ml_mcv26
  data_files:
  - path:
    - ml/mcv26/ml_asr.jsonl.gz
    split: asr
- config_name: mr_fleurs
  data_files:
  - path:
    - mr/fleurs/mr_asr.jsonl.gz
    split: asr
- config_name: mr_mcv26
  data_files:
  - path:
    - mr/mcv26/mr_asr.jsonl.gz
    split: asr
- config_name: mt_fleurs
  data_files:
  - path:
    - mt/fleurs/mt_asr.jsonl.gz
    split: asr
- config_name: mt_mcv26
  data_files:
  - path:
    - mt/mcv26/mt_asr.jsonl.gz
    split: asr
- config_name: mt_voxpopuli
  data_files:
  - path:
    - mt/voxpopuli/mt_asr.jsonl.gz
    split: asr
- config_name: nl_fleurs
  data_files:
  - path:
    - nl/fleurs/nl_asr.jsonl.gz
    split: asr
- config_name: nl_mcv26
  data_files:
  - path:
    - nl/mcv26/nl_asr.jsonl.gz
    split: asr
- config_name: nl_mls
  data_files:
  - path:
    - nl/mls/nl_asr.jsonl.gz
    split: asr
- config_name: nl_voxpopuli
  data_files:
  - path:
    - nl/voxpopuli/nl_asr.jsonl.gz
    split: asr
- config_name: nl_voxpopuli_improved
  data_files:
  - path:
    - nl/voxpopuli_improved/nl_asr.jsonl.gz
    split: asr
- config_name: or_fleurs
  data_files:
  - path:
    - or/fleurs/or_asr.jsonl.gz
    split: asr
- config_name: or_mcv26
  data_files:
  - path:
    - or/mcv26/or_asr.jsonl.gz
    split: asr
- config_name: pa_fleurs
  data_files:
  - path:
    - pa/fleurs/pa_asr.jsonl.gz
    split: asr
- config_name: pa_mcv26
  data_files:
  - path:
    - pa/mcv26/pa_asr.jsonl.gz
    split: asr
- config_name: pl_fleurs
  data_files:
  - path:
    - pl/fleurs/pl_asr.jsonl.gz
    split: asr
- config_name: pl_mcv26
  data_files:
  - path:
    - pl/mcv26/pl_asr.jsonl.gz
    split: asr
- config_name: pl_mls
  data_files:
  - path:
    - pl/mls/pl_asr.jsonl.gz
    split: asr
- config_name: pl_voxpopuli
  data_files:
  - path:
    - pl/voxpopuli/pl_asr.jsonl.gz
    split: asr
- config_name: pl_voxpopuli_improved
  data_files:
  - path:
    - pl/voxpopuli_improved/pl_asr.jsonl.gz
    split: asr
- config_name: pt_falar
  data_files:
  - path:
    - pt/falar/pt_asr.jsonl.gz
    split: asr
- config_name: pt_fleurs
  data_files:
  - path:
    - pt/fleurs/pt_asr.jsonl.gz
    split: asr
- config_name: pt_mcv26
  data_files:
  - path:
    - pt/mcv26/pt_asr.jsonl.gz
    split: asr
- config_name: pt_mls
  data_files:
  - path:
    - pt/mls/pt_asr.jsonl.gz
    split: asr
- config_name: pt_voxpopuli
  data_files:
  - path:
    - pt/voxpopuli/pt_asr.jsonl.gz
    split: asr
- config_name: ro_fleurs
  data_files:
  - path:
    - ro/fleurs/ro_asr.jsonl.gz
    split: asr
- config_name: ro_mcv26
  data_files:
  - path:
    - ro/mcv26/ro_asr.jsonl.gz
    split: asr
- config_name: ro_voxpopuli
  data_files:
  - path:
    - ro/voxpopuli/ro_asr.jsonl.gz
    split: asr
- config_name: ro_voxpopuli_improved
  data_files:
  - path:
    - ro/voxpopuli_improved/ro_asr.jsonl.gz
    split: asr
- config_name: ru_dusha
  data_files:
  - path:
    - ru/dusha/ru_asr.jsonl.gz
    split: asr
- config_name: ru_fleurs
  data_files:
  - path:
    - ru/fleurs/ru_asr.jsonl.gz
    split: asr
- config_name: ru_golos
  data_files:
  - path:
    - ru/golos/ru_asr.jsonl.gz
    split: asr
- config_name: ru_mcv26
  data_files:
  - path:
    - ru/mcv26/ru_asr.jsonl.gz
    split: asr
- config_name: sk_fleurs
  data_files:
  - path:
    - sk/fleurs/sk_asr.jsonl.gz
    split: asr
- config_name: sk_mcv26
  data_files:
  - path:
    - sk/mcv26/sk_asr.jsonl.gz
    split: asr
- config_name: sk_voxpopuli
  data_files:
  - path:
    - sk/voxpopuli/sk_asr.jsonl.gz
    split: asr
- config_name: sk_voxpopuli_improved
  data_files:
  - path:
    - sk/voxpopuli_improved/sk_asr.jsonl.gz
    split: asr
- config_name: sl_fleurs
  data_files:
  - path:
    - sl/fleurs/sl_asr.jsonl.gz
    split: asr
- config_name: sl_mcv26
  data_files:
  - path:
    - sl/mcv26/sl_asr.jsonl.gz
    split: asr
- config_name: sl_voxpopuli
  data_files:
  - path:
    - sl/voxpopuli/sl_asr.jsonl.gz
    split: asr
- config_name: sl_voxpopuli_improved
  data_files:
  - path:
    - sl/voxpopuli_improved/sl_asr.jsonl.gz
    split: asr
- config_name: sv_fleurs
  data_files:
  - path:
    - sv/fleurs/sv_asr.jsonl.gz
    split: asr
- config_name: sv_mcv26
  data_files:
  - path:
    - sv/mcv26/sv_asr.jsonl.gz
    split: asr
- config_name: sv_voxpopuli
  data_files:
  - path:
    - sv/voxpopuli/sv_asr.jsonl.gz
    split: asr
- config_name: ta_fleurs
  data_files:
  - path:
    - ta/fleurs/ta_asr.jsonl.gz
    split: asr
- config_name: te_fleurs
  data_files:
  - path:
    - te/fleurs/te_asr.jsonl.gz
    split: asr
- config_name: te_mcv26
  data_files:
  - path:
    - te/mcv26/te_asr.jsonl.gz
    split: asr
- config_name: th_fleurs
  data_files:
  - path:
    - th/fleurs/th_asr.jsonl.gz
    split: asr
- config_name: th_mcv26
  data_files:
  - path:
    - th/mcv26/th_asr.jsonl.gz
    split: asr
- config_name: tr_fleurs
  data_files:
  - path:
    - tr/fleurs/tr_asr.jsonl.gz
    split: asr
- config_name: uk_fleurs
  data_files:
  - path:
    - uk/fleurs/uk_asr.jsonl.gz
    split: asr
- config_name: uk_mcv26
  data_files:
  - path:
    - uk/mcv26/uk_asr.jsonl.gz
    split: asr
- config_name: ur_fleurs
  data_files:
  - path:
    - ur/fleurs/ur_asr.jsonl.gz
    split: asr
- config_name: ur_mcv26
  data_files:
  - path:
    - ur/mcv26/ur_asr.jsonl.gz
    split: asr
- config_name: vi_fleurs
  data_files:
  - path:
    - vi/fleurs/vi_asr.jsonl.gz
    split: asr
- config_name: vi_mcv26
  data_files:
  - path:
    - vi/mcv26/vi_asr.jsonl.gz
    split: asr
- config_name: zh_fleurs
  data_files:
  - path:
    - zh/fleurs/zh_asr.jsonl.gz
    split: asr
- config_name: ar
  data_files:
  - path:
    - ar/fleurs/ar_asr.jsonl.gz
    split: asr
- config_name: as
  data_files:
  - path:
    - as/fleurs/as_asr.jsonl.gz
    - as/mcv26/as_asr.jsonl.gz
    split: asr
- config_name: bg
  data_files:
  - path:
    - bg/fleurs/bg_asr.jsonl.gz
    - bg/mcv26/bg_asr.jsonl.gz
    - bg/voxpopuli/bg_asr.jsonl.gz
    split: asr
- config_name: bn
  data_files:
  - path:
    - bn/fleurs/bn_asr.jsonl.gz
    - bn/mcv26/bn_asr.jsonl.gz
    split: asr
- config_name: cs
  data_files:
  - path:
    - cs/fleurs/cs_asr.jsonl.gz
    - cs/mcv26/cs_asr.jsonl.gz
    - cs/voxpopuli/cs_asr.jsonl.gz
    - cs/voxpopuli_improved/cs_asr.jsonl.gz
    split: asr
- config_name: da
  data_files:
  - path:
    - da/fleurs/da_asr.jsonl.gz
    - da/mcv26/da_asr.jsonl.gz
    - da/voxpopuli/da_asr.jsonl.gz
    split: asr
- config_name: de
  data_files:
  - path:
    - de/fleurs/de_asr.jsonl.gz
    - de/mcv26/de_asr.jsonl.gz
    - de/mls/de_asr.jsonl.gz
    - de/voxpopuli/de_asr.jsonl.gz
    - de/voxpopuli_improved/de_asr.jsonl.gz
    split: asr
- config_name: el
  data_files:
  - path:
    - el/fleurs/el_asr.jsonl.gz
    - el/mcv26/el_asr.jsonl.gz
    - el/voxpopuli/el_asr.jsonl.gz
    split: asr
- config_name: en
  data_files:
  - path:
    - en/ami/en_asr.jsonl.gz
    - en/europarl/en_asr.jsonl.gz
    - en/fleurs/en_asr.jsonl.gz
    - en/google_speech_commands/en_asr.jsonl.gz
    - en/librilight/en_asr.part00.jsonl.gz
    - en/librilight/en_asr.part01.jsonl.gz
    - en/librilight/en_asr.part02.jsonl.gz
    - en/librilight/en_asr.part03.jsonl.gz
    - en/librispeech_pc/en_asr.jsonl.gz
    - en/mcv26/en_asr.jsonl.gz
    - en/mls/en_asr.jsonl.gz
    - en/nsc/en_asr.jsonl.gz
    - en/people_speech/en_asr.jsonl.gz
    - en/vctk/en_asr.jsonl.gz
    - en/voxpopuli/en_asr.jsonl.gz
    - en/voxpopuli_improved/en_asr.jsonl.gz
    split: asr
- config_name: es
  data_files:
  - path:
    - es/fleurs/es_asr.jsonl.gz
    - es/mcv26/es_asr.jsonl.gz
    - es/mls/es_asr.jsonl.gz
    - es/voxpopuli/es_asr.jsonl.gz
    - es/voxpopuli_improved/es_asr.jsonl.gz
    split: asr
- config_name: et
  data_files:
  - path:
    - et/fleurs/et_asr.jsonl.gz
    - et/mcv26/et_asr.jsonl.gz
    - et/voxpopuli/et_asr.jsonl.gz
    - et/voxpopuli_improved/et_asr.jsonl.gz
    split: asr
- config_name: fa
  data_files:
  - path:
    - fa/fleurs/fa_asr.jsonl.gz
    split: asr
- config_name: fi
  data_files:
  - path:
    - fi/fleurs/fi_asr.jsonl.gz
    - fi/mcv26/fi_asr.jsonl.gz
    - fi/voxpopuli/fi_asr.jsonl.gz
    - fi/voxpopuli_improved/fi_asr.jsonl.gz
    split: asr
- config_name: fil
  data_files:
  - path:
    - fil/fleurs/fil_asr.jsonl.gz
    split: asr
- config_name: fr
  data_files:
  - path:
    - fr/fleurs/fr_asr.jsonl.gz
    - fr/mcv26/fr_asr.jsonl.gz
    - fr/mls/fr_asr.jsonl.gz
    - fr/voxpopuli/fr_asr.jsonl.gz
    - fr/voxpopuli_improved/fr_asr.jsonl.gz
    split: asr
- config_name: gu
  data_files:
  - path:
    - gu/fleurs/gu_asr.jsonl.gz
    split: asr
- config_name: he
  data_files:
  - path:
    - he/fleurs/he_asr.jsonl.gz
    - he/mcv26/he_asr.jsonl.gz
    split: asr
- config_name: hi
  data_files:
  - path:
    - hi/fleurs/hi_asr.jsonl.gz
    - hi/mcv26/hi_asr.jsonl.gz
    split: asr
- config_name: hr
  data_files:
  - path:
    - hr/fleurs/hr_asr.jsonl.gz
    - hr/mcv26/hr_asr.jsonl.gz
    - hr/voxpopuli/hr_asr.jsonl.gz
    - hr/voxpopuli_improved/hr_asr.jsonl.gz
    split: asr
- config_name: hu
  data_files:
  - path:
    - hu/fleurs/hu_asr.jsonl.gz
    - hu/mcv26/hu_asr.jsonl.gz
    - hu/voxpopuli/hu_asr.jsonl.gz
    - hu/voxpopuli_improved/hu_asr.jsonl.gz
    split: asr
- config_name: id
  data_files:
  - path:
    - id/fleurs/id_asr.jsonl.gz
    split: asr
- config_name: it
  data_files:
  - path:
    - it/fleurs/it_asr.jsonl.gz
    - it/mcv26/it_asr.jsonl.gz
    - it/mls/it_asr.jsonl.gz
    - it/voxpopuli/it_asr.jsonl.gz
    - it/voxpopuli_improved/it_asr.jsonl.gz
    split: asr
- config_name: ja
  data_files:
  - path:
    - ja/fleurs/ja_asr.jsonl.gz
    - ja/mcv26/ja_asr.jsonl.gz
    split: asr
- config_name: kn
  data_files:
  - path:
    - kn/fleurs/kn_asr.jsonl.gz
    split: asr
- config_name: ko
  data_files:
  - path:
    - ko/fleurs/ko_asr.jsonl.gz
    - ko/mcv26/ko_asr.jsonl.gz
    split: asr
- config_name: lt
  data_files:
  - path:
    - lt/fleurs/lt_asr.jsonl.gz
    - lt/mcv26/lt_asr.jsonl.gz
    - lt/voxpopuli/lt_asr.jsonl.gz
    - lt/voxpopuli_improved/lt_asr.jsonl.gz
    split: asr
- config_name: lv
  data_files:
  - path:
    - lv/fleurs/lv_asr.jsonl.gz
    - lv/mcv26/lv_asr.jsonl.gz
    - lv/voxpopuli/lv_asr.jsonl.gz
    split: asr
- config_name: ml
  data_files:
  - path:
    - ml/fleurs/ml_asr.jsonl.gz
    - ml/mcv26/ml_asr.jsonl.gz
    split: asr
- config_name: mr
  data_files:
  - path:
    - mr/fleurs/mr_asr.jsonl.gz
    - mr/mcv26/mr_asr.jsonl.gz
    split: asr
- config_name: mt
  data_files:
  - path:
    - mt/fleurs/mt_asr.jsonl.gz
    - mt/mcv26/mt_asr.jsonl.gz
    - mt/voxpopuli/mt_asr.jsonl.gz
    split: asr
- config_name: nl
  data_files:
  - path:
    - nl/fleurs/nl_asr.jsonl.gz
    - nl/mcv26/nl_asr.jsonl.gz
    - nl/mls/nl_asr.jsonl.gz
    - nl/voxpopuli/nl_asr.jsonl.gz
    - nl/voxpopuli_improved/nl_asr.jsonl.gz
    split: asr
- config_name: or
  data_files:
  - path:
    - or/fleurs/or_asr.jsonl.gz
    - or/mcv26/or_asr.jsonl.gz
    split: asr
- config_name: pa
  data_files:
  - path:
    - pa/fleurs/pa_asr.jsonl.gz
    - pa/mcv26/pa_asr.jsonl.gz
    split: asr
- config_name: pl
  data_files:
  - path:
    - pl/fleurs/pl_asr.jsonl.gz
    - pl/mcv26/pl_asr.jsonl.gz
    - pl/mls/pl_asr.jsonl.gz
    - pl/voxpopuli/pl_asr.jsonl.gz
    - pl/voxpopuli_improved/pl_asr.jsonl.gz
    split: asr
- config_name: pt
  data_files:
  - path:
    - pt/falar/pt_asr.jsonl.gz
    - pt/fleurs/pt_asr.jsonl.gz
    - pt/mcv26/pt_asr.jsonl.gz
    - pt/mls/pt_asr.jsonl.gz
    - pt/voxpopuli/pt_asr.jsonl.gz
    split: asr
- config_name: ro
  data_files:
  - path:
    - ro/fleurs/ro_asr.jsonl.gz
    - ro/mcv26/ro_asr.jsonl.gz
    - ro/voxpopuli/ro_asr.jsonl.gz
    - ro/voxpopuli_improved/ro_asr.jsonl.gz
    split: asr
- config_name: ru
  data_files:
  - path:
    - ru/dusha/ru_asr.jsonl.gz
    - ru/fleurs/ru_asr.jsonl.gz
    - ru/golos/ru_asr.jsonl.gz
    - ru/mcv26/ru_asr.jsonl.gz
    split: asr
- config_name: sk
  data_files:
  - path:
    - sk/fleurs/sk_asr.jsonl.gz
    - sk/mcv26/sk_asr.jsonl.gz
    - sk/voxpopuli/sk_asr.jsonl.gz
    - sk/voxpopuli_improved/sk_asr.jsonl.gz
    split: asr
- config_name: sl
  data_files:
  - path:
    - sl/fleurs/sl_asr.jsonl.gz
    - sl/mcv26/sl_asr.jsonl.gz
    - sl/voxpopuli/sl_asr.jsonl.gz
    - sl/voxpopuli_improved/sl_asr.jsonl.gz
    split: asr
- config_name: sv
  data_files:
  - path:
    - sv/fleurs/sv_asr.jsonl.gz
    - sv/mcv26/sv_asr.jsonl.gz
    - sv/voxpopuli/sv_asr.jsonl.gz
    split: asr
- config_name: ta
  data_files:
  - path:
    - ta/fleurs/ta_asr.jsonl.gz
    split: asr
- config_name: te
  data_files:
  - path:
    - te/fleurs/te_asr.jsonl.gz
    - te/mcv26/te_asr.jsonl.gz
    split: asr
- config_name: th
  data_files:
  - path:
    - th/fleurs/th_asr.jsonl.gz
    - th/mcv26/th_asr.jsonl.gz
    split: asr
- config_name: tr
  data_files:
  - path:
    - tr/fleurs/tr_asr.jsonl.gz
    split: asr
- config_name: uk
  data_files:
  - path:
    - uk/fleurs/uk_asr.jsonl.gz
    - uk/mcv26/uk_asr.jsonl.gz
    split: asr
- config_name: ur
  data_files:
  - path:
    - ur/fleurs/ur_asr.jsonl.gz
    - ur/mcv26/ur_asr.jsonl.gz
    split: asr
- config_name: vi
  data_files:
  - path:
    - vi/fleurs/vi_asr.jsonl.gz
    - vi/mcv26/vi_asr.jsonl.gz
    split: asr
- config_name: zh
  data_files:
  - path:
    - zh/fleurs/zh_asr.jsonl.gz
    split: asr
---

<div align="center">
<img src="figures/granary-v2-icon.png" alt="Granary-v2" width="420"/>
</div>

# Granary-v2: Multilingual Speech Recognition, Translation and Instruction Data

<div align="center" style="line-height: 1;">
  <a href="https://developer.nvidia.com/nemotron" target="_blank" style="margin: 2px;">
    <img alt="Homepage" src="https://img.shields.io/badge/%F0%9F%8F%A0Nemotron%20Developer%20Page-Learn%20More%20Here%21-536af5?color=76B900&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/audio/granary_v2/" target="_blank" style="margin: 2px;">
    <img alt="Granary Pipeline" src="https://img.shields.io/badge/%F0%9F%9B%A0%EF%B8%8FGranary%20Pipeline-View%20Code-536af5?color=76B900&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://research.nvidia.com/labs/nemotron/files/granary-v2.pdf" target="_blank" style="margin: 2px;">
    <img alt="Tech Report" src="https://img.shields.io/badge/%F0%9F%93%9DTech%20Report-Read%20Now%21-536af5?color=76B900&logoColor=white" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://discord.gg/9xpKQtVvrk" target="_blank" style="margin: 2px;">
    <img alt="Discord" src="https://img.shields.io/badge/Discord-NVIDIA%20AI%20Developer-7289da?logo=discord&logoColor=white&color=7289da" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div align="center" style="line-height: 1;">
  <a href="#granary-v2-license" style="margin: 2px;">
    <img alt="License: OpenMDW-1.1 / CC BY-SA 4.0" src="https://img.shields.io/badge/License-OpenMDW--1.1%20%2F%20CC%20BY--SA%204.0-f5de53" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

**Granary-v2** is NVIDIA's second release of generated labels and instruction pairs
for multilingual speech. It re-processes a broad set of source corpora through
an entirely new labelling pipeline that produces not just transcripts and translations, but
inverse text normalization, captioning, code-switching and speech-QA targets, plus
ready-to-train instruction pairs.

<div align="center">
<img src="figures/granary-v2-pipeline.gif" alt="Animated walkthrough: one audio sample moves through segmentation, two ASR backbones, and text enrichment" width="1364"/>
</div>

> [!NOTE]
> **The pipeline source is already public.** All of it lives in
> [NeMo Curator](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/audio/granary_v2).
> The full end-to-end runs and the per-stage scripts will follow soon.

## Overview

- **48 languages** across **16 source corpora**
- Labels for **463,062 hours** of source speech
- **approximately 165,300 hours** flagged high-quality by the pipeline's own gate
- **approximately 92,496 hours** of X→English speech translation
- **approximately 39,375 hours** of English→X speech translation, each record fanned out
  to 31 targets at once (`ar`, `bg`, `cs`, `da`, `de`, `el`, `es`, `et`, `fi`, `fr`, `he`, `hi`, `hr`, `hu`, `it`, `ja`, `ko`, `lt`, `lv`, `mt`, `nl`, `pl`, `pt`, `ro`, `ru`, `sk`, `sl`, `sv`, `th`, `uk`, `zh`)
- **Six text targets per utterance**: normalized transcript, ITN, captioning,
  code-switched, speech-QA, and translation

### Supported Languages

Arabic, Assamese, Bengali, Bulgarian, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Filipino, Finnish, French, German, Greek, Gujarati, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Kannada, Korean, Latvian, Lithuanian, Malayalam, Maltese, Marathi, Odia, Persian, Polish, Portuguese, Punjabi, Romanian, Russian, Slovak, Slovenian, Spanish, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese.

## Hours by corpus

| Corpus | Languages | Hours | High-quality h | AST (X→en) h | AST (en→X) h | Source corpus license |
|---|---:|---:|---:|---:|---:|---|
| **[VoxPopuli (MOSEL labels)](https://mt.fbk.eu/mosel/)** (`voxpopuli`) | 23 | 380,711 | 123,192 | 84,999 | 8,990 | CC0 / CC-BY-4.0 labels |
| **[LibriLight](https://github.com/facebookresearch/libri-light)** (`librilight`) | 1 | 49,334 | 25,898 | 0 | 25,725 | MIT |
| **[People's Speech](https://mlcommons.org/en/peoples-speech/)** (`people_speech`) | 1 | 8,598 | 3,807 | 0 | 826 | [CC BY (`clean` partition)](https://huggingface.co/datasets/MLCommons/peoples_speech#licensing-information) |
| **[Multilingual LibriSpeech](https://www.openslr.org/94/)** (`mls`) | 8 | 7,805 | 3,073 | 1,848 | 103 | CC-BY-4.0 |
| **[FalAR](https://huggingface.co/datasets/inesc-id/FalAR)** (`falar`) | 1 | 4,715 | 1,605 | 1,602 | — | CC-BY-4.0 |
| **[Common Voice 26.0](https://commonvoice.mozilla.org/en/datasets)** (`mcv26`) | 39 | 3,871 | 2,837 | 2,372 | 496 | CC0-1.0 |
| **[National Speech Corpus](https://www.imda.gov.sg/NationalSpeechCorpus)** (`nsc`) | 1 | 2,785 | 1,647 | 0 | 1,689 | Singapore Open Data Licence |
| **[VoxPopuli (re-labelled)](https://github.com/facebookresearch/voxpopuli)** (`voxpopuli_improved`) | 16 | 1,277 | 527 | 562 | 160 | CC0 / CC-BY-4.0 labels |
| **[Golos](https://github.com/salute-developers/golos)** (`golos`) | 1 | 1,208 | 715 | 744 | — | Custom (Salute Developers) |
| **[Europarl-ASR](https://www.mllp.upv.es/git-pub/ggarces/Europarl-ASR/)** (`europarl`) | 1 | 1,023 | 605 | 0 | 613 | CC-BY-4.0 |
| **[LibriSpeech-PC](https://www.openslr.org/145/)** (`librispeech_pc`) | 1 | 953 | 953 | 0 | 686 | CC-BY-4.0 |
| **[FLEURS](https://huggingface.co/datasets/google/fleurs)** (`fleurs`) | 48 | 412 | 213 | 226 | 5 | CC-BY-4.0 |
| **[Dusha](https://github.com/salute-developers/golos/tree/master/dusha)** (`dusha`) | 1 | 204 | 104 | 143 | — | Custom (Salute Developers) |
| **[VCTK](https://datashare.ed.ac.uk/handle/10283/3443)** (`vctk`) | 1 | 82 | 76 | 0 | 76 | ODC-By 1.0 |
| **[AMI Meeting Corpus](https://lhotse.readthedocs.io/en/stable/_modules/lhotse/recipes/ami.html)** (`ami`) | 1 | 70 | 24 | 0 | 4 | CC-BY-4.0 |
| **[Google Speech Commands](https://www.tensorflow.org/datasets/catalog/speech_commands)** (`google_speech_commands`) | 1 | 15 | 15 | 0 | 2 | CC-BY-4.0 |
| **Total** | **48** | **463,062** | **~165,300** | **92,496** | **39,375** | |

Totals describe only the manifests in this public release. ASR hours and translation into English are calculated from the reported corpus durations. High-quality and translation-out totals are approximate because the source values are rounded. Translation targets do not add audio hours.

The table lists source-corpus licenses. The released labels and instruction pairs are governed by [OpenMDW-1.1](LICENSE), except for the `people_speech` subset, which is governed by [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt). See [License](#license) for the subset mapping.

This repository contains label manifests only. Obtain audio from the linked source distributors under their applicable licenses and access terms.

## 🎧 Getting the audio

The commands below obtain source corpora from their distributors. Check the source licenses and access terms before downloading. Loading `nvidia/Granary-v2` downloads label manifests only; obtain source audio separately.

This repository ships **manifests only** — no audio travels with it. Every
`audio_filepath` is instead a self-describing identifier:

```
data_<lang>_<corpus>_<source path, with "/" replaced by "_">
```

So `data_de_mcv26_cv-corpus-26.0-2026-06-12_de_clips_common_voice_de_21137340.opus`
is `cv-corpus-26.0-2026-06-12/de/clips/common_voice_de_21137340.opus` in the Common
Voice 26.0 release. Fetch a corpus from its own distributor, then join on that
suffix.

Source audio remains subject to its distributor's terms. See the Source corpus license column in [Hours by corpus](#hours-by-corpus). See [License](#license) for the terms that apply to the released labels and instruction pairs.

The four routes below are ordered by how much work the download takes. Open the one
your corpus is in.

<table>
<tr>
<td valign="top" width="25%">
<b>1 · One HF command</b><br><br>
<code>people_speech</code> · 8,598 h<br>
<code>falar</code> · 4,715 h<br>
<code>fleurs</code> · 412 h
</td>
<td valign="top" width="25%">
<b>2 · Direct download</b><br><br>
<code>librilight</code> · 49,334 h<br>
<code>mls</code> · 7,805 h<br>
<code>golos</code> · 1,208 h<br>
<code>librispeech_pc</code> · 953 h<br>
<code>dusha</code> · 204 h<br>
<code>vctk</code> · 82 h<br>
<code>google_speech_commands</code> · 15 h
</td>
<td valign="top" width="25%">
<b>3 · Corpus tooling</b><br><br>
<code>voxpopuli</code> · 380,711 h<br>
<code>voxpopuli_improved</code> · 1,277 h<br>
<code>europarl</code> · 1,023 h<br>
<code>ami</code> · 70 h
</td>
<td valign="top" width="25%">
<b>4 · Gated access</b><br><br>
<code>mcv26</code> · 3,871 h<br>
<code>nsc</code> · 2,785 h
</td>
</tr>
</table>

<details>
<summary><b>1 · One Hugging Face command</b></summary>

```bash
pip install -U "huggingface_hub[cli]" datasets
```

| Corpus | Hours | How |
|---|---:|---|
| **People's Speech** (`people_speech`) | 8,598 | `hf download MLCommons/peoples_speech --repo-type dataset --include "clean/*"` — we release labels for the government-origin subset of `clean`. The released manifests are governed by [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt). Obtain source audio under the distributor's terms. |
| **FalAR** (`falar`) | 4,715 | `load_dataset("inesc-id/FalAR")` — the audio is embedded in the Parquet shards, so load it rather than fetching files |
| **FLEURS** (`fleurs`) | 412 | `load_dataset("google/fleurs", "ar_eg")` — the config is `<lang>_<region>` |

</details>

<details>
<summary><b>2 · Direct download</b></summary>

| Corpus | Hours | Archive |
|---|---:|---|
| **LibriLight** (`librilight`) | 49,334 | `https://dl.fbaipublicfiles.com/librilight/data/large.tar` (3.06 TB) — we use the **`large`** 60k-hour segmentation; `small` and `medium` sit alongside it in the [repo](https://github.com/facebookresearch/libri-light) |
| **Multilingual LibriSpeech** (`mls`) | 7,805 | `https://dl.fbaipublicfiles.com/mls/mls_<lang>.tar.gz` for `english`, `german`, `dutch`, `french`, `spanish`, `italian`, `portuguese`, `polish` — an `_opus` variant of each exists; full index at [OpenSLR 94](https://www.openslr.org/94/) |
| **Golos** (`golos`) | 1,208 | `https://cdn.chatwm.opensmodel.sberdevices.ru/golos/train_crowd{0..9}.tar` (127 GB total) — we use the **crowd** partition, and `crowd9` carries the manifests. Whole set in Opus: `golos_opus.tar` |
| **LibriSpeech-PC** (`librispeech_pc`) | 953 | The audio is plain LibriSpeech: `https://www.openslr.org/resources/12/train-{clean-100,clean-360,other-500}.tar.gz`. [OpenSLR 145](https://www.openslr.org/145/) adds only the punctuated and capitalised text |
| **Dusha** (`dusha`) | 204 | `https://cdn.chatwm.opensmodel.sberdevices.ru/dusha/crowd.tar` (30 GB) — **crowd only**; the podcast partition ships no audio for licensing reasons and we use none of it |
| **VCTK** (`vctk`) | 82 | `https://datashare.ed.ac.uk/bitstream/handle/10283/3443/VCTK-Corpus-0.92.zip` (11.7 GB) |
| **Google Speech Commands** (`google_speech_commands`) | 15 | `http://download.tensorflow.org/data/speech_commands_v0.02.tar.gz` (2.4 GB) |

</details>

<details>
<summary><b>3 · Needs the corpus's own tooling</b></summary>

**VoxPopuli** — the two VoxPopuli leaves come from the same repository but
**different subsets**, so they take different commands. `voxpopuli` (380,711 h) is
the **v2 unlabelled** release, carrying the MOSEL pseudo-labels that seeded ours
([`FBK-MT/mosel`](https://huggingface.co/datasets/FBK-MT/mosel)); `voxpopuli_improved`
(1,277 h) is the transcribed ASR subset, re-labelled by us.

> [!IMPORTANT]
> Mind the `_v2` suffix. `--subset bg` is the v1 release and is roughly **4× smaller**
> than the `bg_v2` our manifests were built from.

```bash
git clone https://github.com/facebookresearch/voxpopuli && cd voxpopuli
pip install -r requirements.txt

# `voxpopuli` -> the v2 UNLABELLED subset, per language ("400k" fetches all 23 at once)
python -m voxpopuli.download_audios     --root ./data --subset bg_v2
python -m voxpopuli.get_unlabelled_data --root ./data --subset bg_v2

# `voxpopuli_improved` -> the transcribed ASR subset
python -m voxpopuli.download_audios --root ./data --subset asr
python -m voxpopuli.get_asr_data    --root ./data --lang cs
```

**Europarl-ASR** (`europarl`, 1,023 h) — clone the MLLP repository and run its fetch
scripts:

```bash
git clone https://www.mllp.upv.es/git-pub/ggarces/Europarl-ASR.git
```

**AMI** (`ami`, 70 h) — download through the
[Lhotse recipe](https://lhotse.readthedocs.io/en/stable/_modules/lhotse/recipes/ami.html)
with the **IHM** (individual headset microphone) setting; every record we ship is an
individual headset channel, so SDM/MDM audio will not align.

```bash
pip install lhotse && lhotse download ami --mic ihm ./ami
```

</details>

<details>
<summary><b>4 · Gated access</b></summary>

| Corpus | Hours | What it takes |
|---|---:|---|
| **Common Voice 26.0** (`mcv26`) | 3,871 | Download the per-language `cv-corpus-26.0-2026-06-12` archive from the [Common Voice portal](https://commonvoice.mozilla.org/en/datasets) (email-gated); the `mozilla-foundation/common_voice_*` mirrors on the Hub lag the latest release |
| **National Speech Corpus** (`nsc`) | 2,785 | Request access from [IMDA Singapore](https://www.imda.gov.sg/how-we-can-help/national-speech-corpus) — there is no direct download |

</details>

## Repository Structure

```
nvidia/Granary-v2/
└── <language>/                 # ISO 639-1 codes
    └── <corpus>/
        └── <lang>_asr.jsonl.gz
```

One or more manifest files per (language, corpus). Large manifests can be split into shards.

Unlike Granary-v1, there is no separate `<lang>_ast-en.jsonl`: every translation travels
inline in each record's `translations` field, alongside its quality-estimation score. The
manifest files for each (language, corpus) carry both the ASR and the AST targets.

`translations` is keyed by target language, and the release runs in **both directions**.
Non-English audio is translated into English, which is the `AST (X→en) h` column. English
audio is translated the other way, into 31 targets at once (`ar`, `bg`, `cs`, `da`, `de`, `el`, `es`, `et`, `fi`, `fr`, `he`, `hi`, `hr`, `hu`, `it`, `ja`, `ko`, `lt`, `lv`, `mt`, `nl`, `pl`, `pt`, `ro`, `ru`, `sk`, `sl`, `sv`, `th`, `uk`, `zh`) — that is the
`AST (en→X) h` column, and it is why corpora like LibriLight and VCTK show no X→English
hours yet still carry translation.

Coverage is per-record, and a present key is **not** a usable translation: the pipeline
writes a stub with an empty `translation_raw` where its quality estimator rejected the
candidate. **Test `translation_raw` for non-emptiness** rather than assuming a key means
a translation. Both table columns count distinct audio, once per record however many
targets it carries, so neither double-counts and the two never sum past a corpus's hours.

## 🚀 Quick Start

These examples load the released label manifests. Obtain the source audio separately as described in [Getting the audio](#-getting-the-audio). The `people_speech` records retain their CC BY-SA 4.0 license when loaded through the combined `en` configuration; see [License](#license).

```python
from datasets import load_dataset

# 🌍 Language-level access (every corpus for that language)
ds = load_dataset("nvidia/Granary-v2", "de")

# 🎯 Corpus-specific access, named <lang>_<corpus>
ds = load_dataset("nvidia/Granary-v2", "de_mcv26")
ds = load_dataset("nvidia/Granary-v2", "en_librilight")
ds = load_dataset("nvidia/Granary-v2", "ja_mcv26")

# 📡 Streaming for large configs
ds = load_dataset("nvidia/Granary-v2", "en", streaming=True)
```

## 📊 Data Sample Structure

```python
{
    "audio_filepath": str,            # Identifier used to locate source audio
    "duration": float,                # Duration in seconds
    "corpus": str,                    # source corpus name
    "source_lang": str,               # Source language code, e.g. "de"

    "tn_raw": str,                    # Primary transcript, text-normalized with P&C
    "itn_raw": str,                   # Inverse-text-normalized transcript
    "itn_clean": str,                 # ITN transcript after cleanup
    "captioning_text": str,           # Natural-language description of the audio
    "code_switched_text": str,        # Transcript with code-switching preserved
    "speech_qa_text": str,            # Q/A pair grounded in the audio ("SKIP" if N/A)

    "context_asr": dict | None,       # Coarse/fine context terms and entity categories
    "translations": dict,             # {"en": {"translation_raw": str,
                                      #          "translation_quality_score": float}}
    "preference_instructions": list,  # [{"prompt": str, "target": str, "tags": {}}, ...]
    "high_quality": bool | None,      # pipeline quality gate -- see note below
}
```

The pipeline uses 16 kHz mono audio for labeling. Source distributors can provide audio in other formats.

> **On `high_quality`.** The flag records the pipeline's quality check.
> Approximately 165,300 hours in this public release pass it. Context and
> translation coverage vary by record. Early translation runs also included
> records outside the high-quality subset. Check each target for a usable value.

`preference_instructions` is a **derived training view**, not a core target: it packs
the fields above into ready-to-train prompt/target pairs for instruction tuning. The
pairs add no information beyond the other fields, so ignore them if you are training a
plain ASR or AST model.

<a id="granary-v2-license"></a>

## 📄 License

This dataset is governed by the OpenMDW License Agreement, version 1.1, except for the People_Speech subset, which is governed by the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

- **OpenMDW-1.1:** See [LICENSE](LICENSE) and the [official agreement](https://openmdw.ai/license/1-1/).
- **People_Speech exception:** See [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt) and the [official license](https://creativecommons.org/licenses/by-sa/4.0/).

`People_Speech` refers to the released `people_speech` corpus, stored at `en/people_speech/en_asr.jsonl.gz` and available through configuration `en_people_speech`. CC BY-SA 4.0 also applies to these records when they are accessed through the combined `en` configuration. OpenMDW-1.1 applies to the other released manifests. See [NOTICE](NOTICE) for the subset mapping.

Obtain source audio separately from its distributors under the applicable upstream terms. The licenses above describe the dataset materials released in this repository.

## 📚 Citation

If you use Granary-v2, please cite the [NVIDIA technical report](https://research.nvidia.com/labs/nemotron/files/granary-v2.pdf) below.
The report describes the curation system and distinguishes the full processed
collection from the public release subset.

```bibtex
@techreport{koluguri2026granaryv2,
  title       = {Granary-v2: Scalable Multilingual Speech Data Curation for Predictable and Controllable Model Outputs},
  author      = {Nithin Rao Koluguri and Meline Mkrtchyan and Nune Tadevosyan and Aaftab V and Sushmitha Deva and Fan Qian and Davit Karamyan and
                 Kunal Dhawan and Taejin Park and Piotr {\.Z}elasko and Arushi Dhingra and Viraj Karandikar and Shuoyang Ding and Slyne Deng and
                 Onur Yilmaz and Praateek Mahajan and Utkarsh Vaidya and Nikolay Karpov and Jagadeesh Balam and Boris Ginsburg},
  institution = {NVIDIA},
  type        = {Technical Report},
  year        = {2026},
  url         = {https://research.nvidia.com/labs/nemotron/files/granary-v2.pdf}
}
```

For background on Granary-v1, see the Granary-v1 paper in the References section.

## Dataset Description:

Granary-v2 provides synthetic text labels and instruction pairs for multilingual speech. The repository contains compressed JSONL manifests. Obtain the source audio from the distributors listed in the [Hours by corpus](#hours-by-corpus) table. The Overview and data sample sections above describe the available targets and fields.

## Dataset Owner(s):

NVIDIA Corporation

## Dataset Creation Date:

October 28, 2026

## Version: 2.0

Previous Version(s): [Granary-v1 (1.0)](https://huggingface.co/datasets/nvidia/Granary).

Relationship to Previous Version(s): Granary-v2 replaces the labelling pipeline and expands the release to 48 languages and 16 source entries. It adds inverse text normalization, captioning, code-switching, speech-QA, context terms, and instruction pairs. Translations are stored in each record's `translations` field, keyed by target language, and run in both directions: non-English audio into English, and English audio into 31 target languages.

## License/Terms of Use:

This dataset is governed by the OpenMDW License Agreement, version 1.1, except for the People_Speech subset, which is governed by the Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0).

See [License](#license), [LICENSE](LICENSE), [CC BY-SA 4.0](LICENSES/CC-BY-SA-4.0.txt), and [NOTICE](NOTICE) for the license texts and subset mapping. Obtain source audio separately from its distributors under their applicable terms.

## Intended Usage:

Use the dataset for automatic speech recognition, speech translation in both directions (non-English audio into English, and English audio into 31 target languages), and speech instruction tuning. Additional targets support inverse text normalization, audio captioning, code-switching, speech question answering, and contextual speech recognition. Target availability varies by record; see the Data Sample Structure section above.

## Dataset Characterization

- **Data Collection Method:** Manually-Collected. This release uses existing source corpora. The repository distributes manifests; obtain the audio from the source distributors.
- **Labeling Method:** Synthetic. The pipeline produces labels with automatic speech and text models.

## Dataset Format

The repository contains compressed JSONL manifests (`.jsonl.gz`). Each line contains one utterance record. The manifest files for each language and corpus contain the available ASR and speech translation targets. Translations are stored in the `translations` field, keyed by target language.

See [Repository Structure](#repository-structure), Quick Start, and Data Sample Structure above for file paths, loading examples, and record fields.

## Dataset Quantification

| Measure | Value |
|---|---:|
| Languages | 48 |
| Source entries | 16 |
| ASR hours | 463,062 |
| Hours marked high-quality by the pipeline | approximately 165,300 |
| Speech translation hours (X→English) | 92,496 |
| Speech translation hours (English→X) | 39,375 |

Speech translation uses audio already included in the ASR total. See [Hours by corpus](#hours-by-corpus) above for the corpus distribution.

## Sources

The [Hours by corpus](#hours-by-corpus) table lists all 16 source entries, with links to their sources and their source-corpus licenses. This repository distributes manifests. Obtain the audio from each source distributor under that corpus's terms.

## Reference(s):

- Nithin Rao Koluguri, Meline Mkrtchyan, Nune Tadevosyan, et al. (2026). [*Granary-v2: Scalable Multilingual Speech Data Curation for Predictable and Controllable Model Outputs*](https://research.nvidia.com/labs/nemotron/files/granary-v2.pdf). NVIDIA technical report.
- [Granary-v1 dataset](https://huggingface.co/datasets/nvidia/Granary).
- [Granary-v1 paper: Speech Recognition and Translation Dataset in 25 European Languages](https://arxiv.org/abs/2505.13404) — describes the v1 pipeline, which this release supersedes.
- [Granary-v2 curation pipeline in NeMo Curator](https://github.com/NVIDIA-NeMo/Curator/tree/main/tutorials/audio/granary_v2).
- [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo) — for training on these manifests.

The Citation section above provides the Granary-v2 NVIDIA technical report citation. The Granary-v1 paper describes the earlier release.

## Ethical Considerations:

NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications. Developers should work with their internal developer teams to ensure this dataset meets requirements for the relevant industry and use case and addresses unforeseen product misuse.

Please report quality, risk, security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).
