---
license: cc-by-sa-4.0
annotations_creators:
  - found
language_creators:
  - expert-generated
language:
  - af
  - am
  - ar
  - az
  - as
  - bm
  - bn
  - bo
  - bg
  - ca
  - cs
  - ku
  - da
  - de
  - el
  - en
  - es
  - et
  - eu
  - fi
  - fr
  - ff
  - om
  - gu
  - gn
  - ht
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - ig
  - id
  - it
  - is
  - jv
  - ja
  - ka
  - kn
  - kk
  - mn
  - km
  - rw
  - ky
  - ko
  - lo
  - ln
  - lt
  - lg
  - lv
  - ml
  - mr
  - mk
  - mt
  - mi
  - my
  - nl
  - 'no'
  - ne
  - ny
  - or
  - pa
  - ps
  - fa
  - mg
  - pl
  - pt
  - ro
  - ru
  - sn
  - si
  - sl
  - sv
  - sk
  - sd
  - sw
  - ta
  - te
  - tg
  - tl
  - th
  - ti
  - tn
  - ts
  - tr
  - uk
  - ur
  - uz
  - vi
  - wo
  - xh
  - yo
  - zh
  - ms
  - zu
  - multilingual
multilinguality:
  - multilingual
task_categories:
  - audio-classification
  - automatic-speech-recognition
  - audio-text-to-text
  - text-to-speech
  - question-answering
  - document-question-answering
pretty_name: Belebele-Fleurs
dataset_info:
- config_name: afr_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 1321576984.0
    num_examples: 309
  download_size: 697429945
  dataset_size: 1321576984.0
- config_name: amh_Ethi
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4735350571.0
    num_examples: 782
  download_size: 2518582786
  dataset_size: 4735350571.0
- config_name: arb_Arab
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 1516344836.0
    num_examples: 387
  download_size: 802576290
  dataset_size: 1516344836.0
- config_name: asm_Beng
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5596186237.0
    num_examples: 824
  download_size: 3017636971
  dataset_size: 5596186237.0
- config_name: azj_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4695408159.0
    num_examples: 759
  download_size: 2513843262
  dataset_size: 4695408159.0
- config_name: ben_Beng
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5752882522.0
    num_examples: 855
  download_size: 3136282526
  dataset_size: 5752882522.0
- config_name: bul_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4689171166.0
    num_examples: 873
  download_size: 2505604703
  dataset_size: 4689171166.0
- config_name: cat_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3478577853.0
    num_examples: 652
  download_size: 1857877410
  dataset_size: 3478577853.0
- config_name: ceb_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5328160039.0
    num_examples: 783
  download_size: 2836984523
  dataset_size: 5328160039.0
- config_name: ces_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4184004947.0
    num_examples: 802
  download_size: 2222498009
  dataset_size: 4184004947.0
- config_name: ckb_Arab
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5313934366.0
    num_examples: 842
  download_size: 2818314961
  dataset_size: 5313934366.0
- config_name: dan_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3579744686.0
    num_examples: 696
  download_size: 1921138648
  dataset_size: 3579744686.0
- config_name: deu_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4655172301.0
    num_examples: 804
  download_size: 2514299817
  dataset_size: 4655172301.0
- config_name: ell_Grek
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4676081230.0
    num_examples: 837
  download_size: 2495880530
  dataset_size: 4676081230.0
- config_name: eng_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3795562630.0
    num_examples: 844
  download_size: 2048956533
  dataset_size: 3795562630.0
- config_name: est_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3738347953.0
    num_examples: 736
  download_size: 1996763639
  dataset_size: 3738347953.0
- config_name: fin_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4808962381.0
    num_examples: 826
  download_size: 2583594472
  dataset_size: 4808962381.0
- config_name: fra_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4771909151.0
    num_examples: 839
  download_size: 2537876484
  dataset_size: 4771909151.0
- config_name: fuv_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 6574923107.0
    num_examples: 848
  download_size: 3501465907
  dataset_size: 6574923107.0
- config_name: gaz_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 1208450421.0
    num_examples: 252
  download_size: 633794246
  dataset_size: 1208450421.0
- config_name: guj_Gujr
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4941743312.0
    num_examples: 880
  download_size: 2674707067
  dataset_size: 4941743312.0
- config_name: hau_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 6720094918.0
    num_examples: 838
  download_size: 3664051325
  dataset_size: 6720094918.0
- config_name: heb_Hebr
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4723937383.0
    num_examples: 878
  download_size: 2537321008
  dataset_size: 4723937383.0
- config_name: hin_Deva
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2242460095.0
    num_examples: 515
  download_size: 1210901498
  dataset_size: 2242460095.0
- config_name: hrv_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5934802411.0
    num_examples: 896
  download_size: 3121833679
  dataset_size: 5934802411.0
- config_name: hun_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5104748515.0
    num_examples: 879
  download_size: 2745994747
  dataset_size: 5104748515.0
- config_name: hye_Armn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5418654048.0
    num_examples: 861
  download_size: 2886102322
  dataset_size: 5418654048.0
- config_name: ibo_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 7449052399.0
    num_examples: 838
  download_size: 3923089955
  dataset_size: 7449052399.0
- config_name: ind_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4259773565.0
    num_examples: 783
  download_size: 2307173322
  dataset_size: 4259773565.0
- config_name: isl_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 205392451.0
    num_examples: 81
  download_size: 108289354
  dataset_size: 205392451.0
- config_name: ita_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5068341448.0
    num_examples: 851
  download_size: 2722452061
  dataset_size: 5068341448.0
- config_name: jav_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5484070653.0
    num_examples: 835
  download_size: 2959104967
  dataset_size: 5484070653.0
- config_name: jpn_Jpan
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2946432247.0
    num_examples: 590
  download_size: 1600204018
  dataset_size: 2946432247.0
- config_name: kan_Knda
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3554826830.0
    num_examples: 606
  download_size: 1975103591
  dataset_size: 3554826830.0
- config_name: kat_Geor
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 1721617148.0
    num_examples: 372
  download_size: 927696223
  dataset_size: 1721617148.0
- config_name: kaz_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 6414631274.0
    num_examples: 870
  download_size: 3429143107
  dataset_size: 6414631274.0
- config_name: kea_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5144742658.0
    num_examples: 770
  download_size: 2797781391
  dataset_size: 5144742658.0
- config_name: khk_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5162621083.0
    num_examples: 869
  download_size: 2720720587
  dataset_size: 5162621083.0
- config_name: khm_Khmr
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2485030372.0
    num_examples: 439
  download_size: 1331377064
  dataset_size: 2485030372.0
- config_name: kir_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4853152090.0
    num_examples: 811
  download_size: 2578226837
  dataset_size: 4853152090.0
- config_name: kor_Hang
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2578906312.0
    num_examples: 535
  download_size: 1374610547
  dataset_size: 2578906312.0
- config_name: lao_Laoo
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 1743552264.0
    num_examples: 346
  download_size: 947988554
  dataset_size: 1743552264.0
- config_name: lin_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 7700082152.0
    num_examples: 778
  download_size: 4174517500
  dataset_size: 7700082152.0
- config_name: lit_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5076063385.0
    num_examples: 834
  download_size: 2686738787
  dataset_size: 5076063385.0
- config_name: lug_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5464636888.0
    num_examples: 703
  download_size: 2897617677
  dataset_size: 5464636888.0
- config_name: luo_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3087291382.0
    num_examples: 512
  download_size: 1584768164
  dataset_size: 3087291382.0
- config_name: lvs_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2682008095.0
    num_examples: 555
  download_size: 1444964552
  dataset_size: 2682008095.0
- config_name: mal_Mlym
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5386280878.0
    num_examples: 809
  download_size: 2955248301
  dataset_size: 5386280878.0
- config_name: mar_Deva
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 6465055207.0
    num_examples: 869
  download_size: 3520545265
  dataset_size: 6465055207.0
- config_name: mkd_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3390202546.0
    num_examples: 667
  download_size: 1826472415
  dataset_size: 3390202546.0
- config_name: mlt_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5323890122.0
    num_examples: 816
  download_size: 2853160463
  dataset_size: 5323890122.0
- config_name: mri_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 9910328387.0
    num_examples: 877
  download_size: 5366184778
  dataset_size: 9910328387.0
- config_name: mya_Mymr
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 6537958064.0
    num_examples: 864
  download_size: 3473242775
  dataset_size: 6537958064.0
- config_name: nld_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2936062189.0
    num_examples: 674
  download_size: 1580031502
  dataset_size: 2936062189.0
- config_name: nob_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3223729748.0
    num_examples: 635
  download_size: 1727069260
  dataset_size: 3223729748.0
- config_name: npi_Deva
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5523444178.0
    num_examples: 876
  download_size: 2934225115
  dataset_size: 5523444178.0
- config_name: nso_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5214380593.0
    num_examples: 569
  download_size: 2820054584
  dataset_size: 5214380593.0
- config_name: nya_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5171597207.0
    num_examples: 752
  download_size: 2798443867
  dataset_size: 5171597207.0
- config_name: ory_Orya
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 952123794.0
    num_examples: 220
  download_size: 530607239
  dataset_size: 952123794.0
- config_name: pan_Guru
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 1790548604.0
    num_examples: 396
  download_size: 981900813
  dataset_size: 1790548604.0
- config_name: pbt_Arab
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3363027226.0
    num_examples: 628
  download_size: 1793620479
  dataset_size: 3363027226.0
- config_name: pes_Arab
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5254241288.0
    num_examples: 673
  download_size: 2841830079
  dataset_size: 5254241288.0
- config_name: pol_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4081649841.0
    num_examples: 765
  download_size: 2178140885
  dataset_size: 4081649841.0
- config_name: por_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5067443206.0
    num_examples: 791
  download_size: 2728057508
  dataset_size: 5067443206.0
- config_name: ron_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4918450774.0
    num_examples: 815
  download_size: 2651664539
  dataset_size: 4918450774.0
- config_name: rus_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4088257099.0
    num_examples: 819
  download_size: 2205120246
  dataset_size: 4088257099.0
- config_name: slk_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2314088471.0
    num_examples: 513
  download_size: 1275825426
  dataset_size: 2314088471.0
- config_name: slv_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3512597020.0
    num_examples: 724
  download_size: 1860950627
  dataset_size: 3512597020.0
- config_name: sna_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4943509770.0
    num_examples: 735
  download_size: 2636061545
  dataset_size: 4943509770.0
- config_name: snd_Arab
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5905092711.0
    num_examples: 878
  download_size: 3199596548
  dataset_size: 5905092711.0
- config_name: som_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 7045590404.0
    num_examples: 874
  download_size: 3795317446
  dataset_size: 7045590404.0
- config_name: spa_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3379035485.0
    num_examples: 659
  download_size: 1802935790
  dataset_size: 3379035485.0
- config_name: srp_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4608181984.0
    num_examples: 766
  download_size: 2492717750
  dataset_size: 4608181984.0
- config_name: swe_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3621750448.0
    num_examples: 681
  download_size: 1878869280
  dataset_size: 3621750448.0
- config_name: swh_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5654478598.0
    num_examples: 780
  download_size: 3051736604
  dataset_size: 5654478598.0
- config_name: tam_Taml
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3849928833.0
    num_examples: 714
  download_size: 2060754219
  dataset_size: 3849928833.0
- config_name: tel_Telu
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2710509575.0
    num_examples: 567
  download_size: 1453506468
  dataset_size: 2710509575.0
- config_name: tgk_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3466965147.0
    num_examples: 632
  download_size: 1836266294
  dataset_size: 3466965147.0
- config_name: tgl_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3521747690.0
    num_examples: 505
  download_size: 1944891399
  dataset_size: 3521747690.0
- config_name: tha_Thai
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4391092533.0
    num_examples: 745
  download_size: 2373882345
  dataset_size: 4391092533.0
- config_name: tur_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 3781792503.0
    num_examples: 706
  download_size: 2023965910
  dataset_size: 3781792503.0
- config_name: ukr_Cyrl
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4141799202.0
    num_examples: 773
  download_size: 2217292261
  dataset_size: 4141799202.0
- config_name: urd_Arab
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2162223158.0
    num_examples: 482
  download_size: 1146920089
  dataset_size: 2162223158.0
- config_name: uzn_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4941238038.0
    num_examples: 812
  download_size: 2646926766
  dataset_size: 4941238038.0
- config_name: vie_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4871565136.0
    num_examples: 847
  download_size: 2621996970
  dataset_size: 4871565136.0
- config_name: wol_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2675304049.0
    num_examples: 495
  download_size: 1327127473
  dataset_size: 2675304049.0
- config_name: xho_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 7209281056.0
    num_examples: 900
  download_size: 3841482084
  dataset_size: 7209281056.0
- config_name: yor_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4500184372.0
    num_examples: 652
  download_size: 2483974070
  dataset_size: 4500184372.0
- config_name: zho_Hans
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 5326687452.0
    num_examples: 888
  download_size: 2859612274
  dataset_size: 5326687452.0
- config_name: zho_Hant
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 2787256479.0
    num_examples: 527
  download_size: 1516121058
  dataset_size: 2787256479.0
- config_name: zsm_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 4323922189.0
    num_examples: 749
  download_size: 2323029241
  dataset_size: 4323922189.0
- config_name: zul_Latn
  features:
  - name: link
    dtype: string
  - name: question_number
    dtype: int64
  - name: flores_passage
    dtype: string
  - name: question
    dtype: string
  - name: mc_answer1
    dtype: string
  - name: mc_answer2
    dtype: string
  - name: mc_answer3
    dtype: string
  - name: mc_answer4
    dtype: string
  - name: correct_answer_num
    dtype: string
  - name: dialect
    dtype: string
  - name: ds
    dtype: timestamp[us]
  - name: sentence_data
    list:
    - name: URL
      dtype: string
    - name: audio
      sequence:
        audio:
          sampling_rate: 16000
    - name: domain
      dtype: string
    - name: filename
      sequence: string
    - name: fleurs_id
      dtype: int64
    - name: full_paragraph
      dtype: bool
    - name: gender
      sequence: string
    - name: has_hyperlink
      dtype: int64
    - name: has_image
      dtype: int64
    - name: id
      dtype: int64
    - name: num_samples
      sequence: int64
    - name: raw_transcription
      dtype: string
    - name: seamlessm4t_asr
      sequence: string
    - name: seamlessm4t_asr_cer
      sequence: float64
    - name: seamlessm4t_asr_translation
      sequence: string
    - name: seamlessm4t_asr_wer
      sequence: float64
    - name: sentence
      dtype: string
    - name: sentence_idx
      dtype: int64
    - name: speaker_id
      sequence: int64
    - name: split
      sequence: string
    - name: topic
      dtype: string
    - name: transcription
      dtype: string
    - name: whisper_asr
      sequence: string
    - name: whisper_asr_cer
      sequence: float64
    - name: whisper_asr_translation
      sequence: string
    - name: whisper_asr_wer
      sequence: float64
  splits:
  - name: test
    num_bytes: 7229958526.0
    num_examples: 838
  download_size: 3874798473
  dataset_size: 7229958526.0
configs:
- config_name: afr_Latn
  data_files:
  - split: test
    path: data/afr_Latn/test-*
- config_name: amh_Ethi
  data_files:
  - split: test
    path: data/amh_Ethi/test-*
- config_name: arb_Arab
  data_files:
  - split: test
    path: data/arb_Arab/test-*
- config_name: asm_Beng
  data_files:
  - split: test
    path: data/asm_Beng/test-*
- config_name: azj_Latn
  data_files:
  - split: test
    path: data/azj_Latn/test-*
- config_name: ben_Beng
  data_files:
  - split: test
    path: data/ben_Beng/test-*
- config_name: bul_Cyrl
  data_files:
  - split: test
    path: data/bul_Cyrl/test-*
- config_name: cat_Latn
  data_files:
  - split: test
    path: data/cat_Latn/test-*
- config_name: ceb_Latn
  data_files:
  - split: test
    path: data/ceb_Latn/test-*
- config_name: ces_Latn
  data_files:
  - split: test
    path: data/ces_Latn/test-*
- config_name: ckb_Arab
  data_files:
  - split: test
    path: data/ckb_Arab/test-*
- config_name: dan_Latn
  data_files:
  - split: test
    path: data/dan_Latn/test-*
- config_name: deu_Latn
  data_files:
  - split: test
    path: data/deu_Latn/test-*
- config_name: ell_Grek
  data_files:
  - split: test
    path: data/ell_Grek/test-*
- config_name: eng_Latn
  data_files:
  - split: test
    path: data/eng_Latn/test-*
- config_name: est_Latn
  data_files:
  - split: test
    path: data/est_Latn/test-*
- config_name: fin_Latn
  data_files:
  - split: test
    path: data/fin_Latn/test-*
- config_name: fra_Latn
  data_files:
  - split: test
    path: data/fra_Latn/test-*
- config_name: fuv_Latn
  data_files:
  - split: test
    path: data/fuv_Latn/test-*
- config_name: gaz_Latn
  data_files:
  - split: test
    path: data/gaz_Latn/test-*
- config_name: guj_Gujr
  data_files:
  - split: test
    path: data/guj_Gujr/test-*
- config_name: hau_Latn
  data_files:
  - split: test
    path: data/hau_Latn/test-*
- config_name: heb_Hebr
  data_files:
  - split: test
    path: data/heb_Hebr/test-*
- config_name: hin_Deva
  data_files:
  - split: test
    path: data/hin_Deva/test-*
- config_name: hrv_Latn
  data_files:
  - split: test
    path: data/hrv_Latn/test-*
- config_name: hun_Latn
  data_files:
  - split: test
    path: data/hun_Latn/test-*
- config_name: hye_Armn
  data_files:
  - split: test
    path: data/hye_Armn/test-*
- config_name: ibo_Latn
  data_files:
  - split: test
    path: data/ibo_Latn/test-*
- config_name: ind_Latn
  data_files:
  - split: test
    path: data/ind_Latn/test-*
- config_name: isl_Latn
  data_files:
  - split: test
    path: data/isl_Latn/test-*
- config_name: ita_Latn
  data_files:
  - split: test
    path: data/ita_Latn/test-*
- config_name: jav_Latn
  data_files:
  - split: test
    path: data/jav_Latn/test-*
- config_name: jpn_Jpan
  data_files:
  - split: test
    path: data/jpn_Jpan/test-*
- config_name: kan_Knda
  data_files:
  - split: test
    path: data/kan_Knda/test-*
- config_name: kat_Geor
  data_files:
  - split: test
    path: data/kat_Geor/test-*
- config_name: kaz_Cyrl
  data_files:
  - split: test
    path: data/kaz_Cyrl/test-*
- config_name: kea_Latn
  data_files:
  - split: test
    path: data/kea_Latn/test-*
- config_name: khk_Cyrl
  data_files:
  - split: test
    path: data/khk_Cyrl/test-*
- config_name: khm_Khmr
  data_files:
  - split: test
    path: data/khm_Khmr/test-*
- config_name: kir_Cyrl
  data_files:
  - split: test
    path: data/kir_Cyrl/test-*
- config_name: kor_Hang
  data_files:
  - split: test
    path: data/kor_Hang/test-*
- config_name: lao_Laoo
  data_files:
  - split: test
    path: data/lao_Laoo/test-*
- config_name: lin_Latn
  data_files:
  - split: test
    path: data/lin_Latn/test-*
- config_name: lit_Latn
  data_files:
  - split: test
    path: data/lit_Latn/test-*
- config_name: lug_Latn
  data_files:
  - split: test
    path: data/lug_Latn/test-*
- config_name: luo_Latn
  data_files:
  - split: test
    path: data/luo_Latn/test-*
- config_name: lvs_Latn
  data_files:
  - split: test
    path: data/lvs_Latn/test-*
- config_name: mal_Mlym
  data_files:
  - split: test
    path: data/mal_Mlym/test-*
- config_name: mar_Deva
  data_files:
  - split: test
    path: data/mar_Deva/test-*
- config_name: mkd_Cyrl
  data_files:
  - split: test
    path: data/mkd_Cyrl/test-*
- config_name: mlt_Latn
  data_files:
  - split: test
    path: data/mlt_Latn/test-*
- config_name: mri_Latn
  data_files:
  - split: test
    path: data/mri_Latn/test-*
- config_name: mya_Mymr
  data_files:
  - split: test
    path: data/mya_Mymr/test-*
- config_name: nld_Latn
  data_files:
  - split: test
    path: data/nld_Latn/test-*
- config_name: nob_Latn
  data_files:
  - split: test
    path: data/nob_Latn/test-*
- config_name: npi_Deva
  data_files:
  - split: test
    path: data/npi_Deva/test-*
- config_name: nso_Latn
  data_files:
  - split: test
    path: data/nso_Latn/test-*
- config_name: nya_Latn
  data_files:
  - split: test
    path: data/nya_Latn/test-*
- config_name: ory_Orya
  data_files:
  - split: test
    path: data/ory_Orya/test-*
- config_name: pan_Guru
  data_files:
  - split: test
    path: data/pan_Guru/test-*
- config_name: pbt_Arab
  data_files:
  - split: test
    path: data/pbt_Arab/test-*
- config_name: pes_Arab
  data_files:
  - split: test
    path: data/pes_Arab/test-*
- config_name: pol_Latn
  data_files:
  - split: test
    path: data/pol_Latn/test-*
- config_name: por_Latn
  data_files:
  - split: test
    path: data/por_Latn/test-*
- config_name: ron_Latn
  data_files:
  - split: test
    path: data/ron_Latn/test-*
- config_name: rus_Cyrl
  data_files:
  - split: test
    path: data/rus_Cyrl/test-*
- config_name: slk_Latn
  data_files:
  - split: test
    path: data/slk_Latn/test-*
- config_name: slv_Latn
  data_files:
  - split: test
    path: data/slv_Latn/test-*
- config_name: sna_Latn
  data_files:
  - split: test
    path: data/sna_Latn/test-*
- config_name: snd_Arab
  data_files:
  - split: test
    path: data/snd_Arab/test-*
- config_name: som_Latn
  data_files:
  - split: test
    path: data/som_Latn/test-*
- config_name: spa_Latn
  data_files:
  - split: test
    path: data/spa_Latn/test-*
- config_name: srp_Cyrl
  data_files:
  - split: test
    path: data/srp_Cyrl/test-*
- config_name: swe_Latn
  data_files:
  - split: test
    path: data/swe_Latn/test-*
- config_name: swh_Latn
  data_files:
  - split: test
    path: data/swh_Latn/test-*
- config_name: tam_Taml
  data_files:
  - split: test
    path: data/tam_Taml/test-*
- config_name: tel_Telu
  data_files:
  - split: test
    path: data/tel_Telu/test-*
- config_name: tgk_Cyrl
  data_files:
  - split: test
    path: data/tgk_Cyrl/test-*
- config_name: tgl_Latn
  data_files:
  - split: test
    path: data/tgl_Latn/test-*
- config_name: tha_Thai
  data_files:
  - split: test
    path: data/tha_Thai/test-*
- config_name: tur_Latn
  data_files:
  - split: test
    path: data/tur_Latn/test-*
- config_name: ukr_Cyrl
  data_files:
  - split: test
    path: data/ukr_Cyrl/test-*
- config_name: urd_Arab
  data_files:
  - split: test
    path: data/urd_Arab/test-*
- config_name: uzn_Latn
  data_files:
  - split: test
    path: data/uzn_Latn/test-*
- config_name: vie_Latn
  data_files:
  - split: test
    path: data/vie_Latn/test-*
- config_name: wol_Latn
  data_files:
  - split: test
    path: data/wol_Latn/test-*
- config_name: xho_Latn
  data_files:
  - split: test
    path: data/xho_Latn/test-*
- config_name: yor_Latn
  data_files:
  - split: test
    path: data/yor_Latn/test-*
- config_name: zho_Hans
  data_files:
  - split: test
    path: data/zho_Hans/test-*
- config_name: zho_Hant
  data_files:
  - split: test
    path: data/zho_Hant/test-*
- config_name: zsm_Latn
  data_files:
  - split: test
    path: data/zsm_Latn/test-*
- config_name: zul_Latn
  data_files:
  - split: test
    path: data/zul_Latn/test-*
---


# Belebele-Fleurs


Belebele-Fleurs is a dataset suitable to evaluate two core tasks:

- **Multilingual Spoken Language Understanding (Listening Comprehension):** For each spoken paragraph, the task is to answer a multiple-choice question. The question and four answer choices are provided in text form.
- **Multilingual Long-Form Automatic Speech Recognition (ASR) with Diverse Speakers:** By concatenating sentence-level utterances, long-form audio clips (ranging from 30 seconds to 1 minute 30 seconds) can be created. These clips feature a diverse set of speakers, making the dataset suitable for robust ASR evaluations.

## Dataset creation

This dataset processes and merges all available multilingual data from the Fleurs, Flores, and Belebele datasets.
It aligns the Belebele test subset with the corresponding segments from the interesected Fleurs-Flores data.

The processing pipeline involves the following steps:
1. Remove all silent and noisy files from Fleurs.
2. Match Fleurs into Flores
3. Matches concatenated Flores sentences into Belebele for Fleurs-Flores paragraphs that are fully available.
4. Uploads the merged and aligned dataset to a Hugging Face Hub repository.

Full details and scripts to compile this dataset are available at: [https://github.com/fdschmidt93/fleurs-slu](https://github.com/fdschmidt93/fleurs-slu)

## Example


```python
from datasets import load_dataset
eng_Latn = load_dataset("wuenlp/fleurs-belebele", "eng_Latn", split="test")
#
# Dataset({
#     features: ['link', 'question_number', 'flores_passage', 'question', 'mc_answer1', 'm
# c_answer2', 'mc_answer3', 'mc_answer4', 'correct_answer_num', 'dialect', 'ds', 'sentence
# _data'],
#     num_rows: 844
# })

```

`sentence_data: list[dict]` comprises the ordered sentence-level data of each available paragraph for Belebele for that language. Each utterance is wrapped in a list inside the sentence-level data. See 'Usage' below on an example function to unwrap the sentence data as you would like to use it.

```python
eng_Latn[0]["sentence_data"]
[{'URL': 'https://en.wikibooks.org/wiki/Accordion/Right_hand',
  'audio': [{'path': '9408178198244706031.wav', 'array': array([ 0.        ,  0.        ,  0.        , ..., -0.00086391, -0.00147504, -0.0025661 ]), 'sampling_rate': 16000},
            {'path': '12239315312712394265.wav', 'array': array([ 1.78813934e-07, -1.78813934e-07,  2.38418579e-07, ..., 6.80863857e-04,  5.23209572e-04,  6.05285168e-04]), 'sampling_rate': 16000}],
  'domain': 'wikibooks',
  'filename': ['9408178198244706031.wav', '12239315312712394265.wav'],
  'fleurs_id': 479,
  'full_paragraph': True,
  'gender': ['FEMALE', 'MALE'],
  'has_hyperlink': 0,
  'has_image': 0,
  'id': 479,
  'num_samples': [184320, 161280],
  'raw_transcription': 'Make sure your hand is as relaxed as possible while still hittin g all the notes correctly - also try not to make much extraneous motion with your fingers.',
  'seamlessm4t_asr': ['Make sure your hand is as relaxed as possible when still hitting all the notes correctly. Also, try not to make much extraneous motion with your fingers.',
   'make sure your hand is as relaxed as possible while still hitting all the notes correctly also try not to make much extraneous motion with your fingers'],
  'seamlessm4t_asr_cer': [0.045454545454545456, 0.025974025974025976],
  'seamlessm4t_asr_translation': ['Make sure your hand is as relaxed as possible when still hitting all the notes correctly. Also, try not to make much extraneous motion with your fingers.',
   'make sure your hand is as relaxed as possible while still hitting all the notes correctly also try not to make much extraneous motion with your fingers'],
  'seamlessm4t_asr_wer': [0.14285714285714285, 0.10714285714285714],
  'sentence': 'Make sure your hand is as relaxed as possible while still hitting all the notes correctly - also try not to make much extraneous motion with your fingers.',
  'sentence_idx': 0,
  'speaker_id': [11, 9],
  'split': ['train', 'train'],
  'topic': 'accordion/right hand',
  'transcription': 'make sure your hand is as relaxed as possible while still hitting all the notes correctly also try not to make much extraneous motion with your fingers',
  'whisper_asr': ['Make sure your hand is as relaxed as possible when still hitting all the notes correctly. Also, try not to make much extraneous motion with your fingers.',
   'Make sure your hand is as relaxed as possible while still hitting all the notes correctly. Also, try not to make much extraneous motion with your fingers.'],
  'whisper_asr_cer': [0.045454545454545456, 0.025974025974025976],
  'whisper_asr_translation': ['Make sure your hand is as relaxed as possible when still hitting all the notes correctly. Also, try not to make much extraneous motion with your 
fingers.',
   'Make sure your hand is as relaxed as possible while still hitting all the notes correctly. Also, try not to make much extraneous motion with your fingers.'],
  'whisper_asr_wer': [0.14285714285714285, 0.10714285714285714]}
  ,
 # ... and remaining sentences
 ]
```

## Usage

Below is an example of how to use the provided functions for selecting utterances from the Belebele-Fleurs dataset according to different criteria (e.g. minimizing or maximizing CER, or random selection). You can adjust the selection strategy (`strategy`) as needed.

After mapping, you will have columns for the processed passages using the selected criteria:

- `whisper_asr_flores_passage`
- `whisper_asr_translation_flores_passage`
- `seamlessm4t_asr_flores_passage`
- `seamlessm4t_asr_translation_flores_passage`

These contain concatenated transcripts or translations based on the chosen selection strategy.

### Selection Strategy:

You can choose how you want to select utterances:

- `strategy="best"`: Selects utterances with the minimal Character Error Rate (CER).
- `strategy="worst"`: Selects utterances with the maximal CER.
- `strategy="random"`: Selects utterances at random.

**Note:** The selection logic takes into account which models are supported for a given language. If a language is unsupported by one of the models, the function automatically adjusts to only consider CERs from the supported models.


```python
import random
import torch
from transformers.tokenization_utils_fast import PreTrainedTokenizerFast
from typing import Any, Callable

from transformers import AutoTokenizer


def select_audio_mapper(
    language: str,
    strategy: str = "best",
) -> Callable[[dict[str, list[Any]]], dict[str, list[Any]]]:
    """
    Create a mapping function for selecting audio data based on CER.

    Args:
        language (str): Language code for filtering unsupported models.
        strategy (str, optional): Selection strategy ('best', 'worst', or 'random'). Defaults to 'best'.

    Returns:
        Callable[[dict[str, list[Any]]], dict[str, list[Any]]]: A function for mapping dataset examples.

    Raises:
        ValueError: If an invalid selection strategy is provided.
    """

    keys = {
        "audio",
        "filename",
        "gender",
        "num_samples",
        "seamlessm4t_asr",
        "seamlessm4t_asr_cer",
        "seamlessm4t_asr_translation",
        "seamlessm4t_asr_wer",
        "speaker_id",
        "split",
        "whisper_asr",
        "whisper_asr_cer",
        "whisper_asr_translation",
        "whisper_asr_wer",
    }

    # Define unsupported languages for each model
    seamless_unsupported = {
        "ast_Latn",
        "hau_Latn",
        "kam_Latn",
        "kea_Latn",
        "lin_Latn",
        "mri_Latn",
        "nso_Latn",
        "oci_Latn",
        "tgl_Latn",
        "umb_Latn",
        "wol_Latn",
        "xho_Latn",
    }
    whisper_unsupported = {
        "ast_Latn",
        "ceb_Latn",
        "ckb_Arab",
        "fuv_Latn",
        "gle_Latn",
        "ibo_Latn",
        "kam_Latn",
        "kea_Latn",
        "kir_Cyrl",
        "lug_Latn",
        "luo_Latn",
        "nso_Latn",
        "tgl_Latn",
        "umb_Latn",
        "wol_Latn",
        "xho_Latn",
        "zul_Latn",
    }

    # Define selection strategy
    if strategy == "best":
        select_func = lambda scores: min(range(len(scores)), key=lambda i: scores[i])
    elif strategy == "worst":
        select_func = lambda scores: max(range(len(scores)), key=lambda i: scores[i])
    elif strategy == "random":
        select_func = lambda scores: random.randint(0, len(scores) - 1)
    else:
        raise ValueError("Invalid 'strategy'. Must be one of 'best', 'worst', or 'random'.")

    # Determine which models are supported for the given language
    if language not in whisper_unsupported and language not in seamless_unsupported:
        models = ["whisper_asr_cer", "seamlessm4t_asr_cer"]
    elif language in whisper_unsupported:
        models = ["seamlessm4t_asr_cer"]
    elif language in seamless_unsupported:
        models = ["whisper_asr_cer"]
    else:
        models = ["whisper_asr_cer", "seamlessm4t_asr_cer"]

    asr_keys = [
        "whisper_asr",
        "whisper_asr_translation",
        "seamlessm4t_asr",
        "seamlessm4t_asr_translation",
    ]

    def map_fn(examples: dict[str, list[Any]]) -> dict[str, list[Any]]:
        """
        Map function to process dataset examples by selecting CER-based audio data.

        Args:
            examples (dict[str, list[Any]]): Dataset examples.

        Returns:
            dict[str, list[Any]]: Processed dataset examples.
        """
        sentence_data_containers: list[list[list]] = examples["sentence_data"]

        paragraphs = {k: [] for k in asr_keys}

        for sentence_data in sentence_data_containers:
            collected_sentence_data = []
            for sentence in sentence_data:
                cer_lists = [sentence[model] for model in models]
                averaged_cer = [
                    sum(aligned_cer) / len(aligned_cer)
                    for aligned_cer in zip(*cer_lists)
                ]
                argmin_idx = select_func(averaged_cer)
                sentence_dict = {key: sentence[key][argmin_idx] for key in keys}
                sentence_dict["id"] = sentence["id"]
                collected_sentence_data.append(sentence_dict)

            collected_sentence_data = list(
                sorted(collected_sentence_data, key=lambda x: x["id"])
            )
            for key in asr_keys:
                texts = " ".join(
                    [line[key].strip() for line in collected_sentence_data]
                ).strip()
                paragraphs[key].append(texts)
        for key in asr_keys:
            examples[f"{key}_flores_passage"] = paragraphs[key]
        return examples

    return map_fn

from datasets import load_dataset

eng_Latn = load_dataset("wuenlp/belebele-fleurs", "eng_Latn", split="test")
mapper = select_audio_mapper("eng_Latn")
dataset = eng_Latn.map(
    mapper, batched=True, batch_size=30, remove_columns=["sentence_data"]
)
```


## Dataset statistics

| Language   |   Counts |
|:-----------|---------:|
| `eng_Latn`   |      844 |
| `afr_Latn`   |      309 |
| `amh_Ethi`   |      782 |
| `arb_Arab`   |      387 |
| `asm_Beng`   |      824 |
| `azj_Latn`   |      759 |
| `bul_Cyrl`   |      873 |
| `ben_Beng`   |      855 |
| `cat_Latn`   |      652 |
| `ceb_Latn`   |      783 |
| `ckb_Arab`   |      842 |
| `zho_Hans`   |      888 |
| `ces_Latn`   |      802 |
| `dan_Latn`   |      696 |
| `deu_Latn`   |      804 |
| `ell_Grek`   |      837 |
| `eng_Latn`   |      844 |
| `spa_Latn`   |      659 |
| `est_Latn`   |      736 |
| `pes_Arab`   |      673 |
| `fin_Latn`   |      826 |
| `tgl_Latn`   |      505 |
| `fra_Latn`   |      839 |
| `guj_Gujr`   |      880 |
| `afr_Latn`   |      309 |
| `hau_Latn`   |      838 |
| `heb_Hebr`   |      878 |
| `hin_Deva`   |      515 |
| `hrv_Latn`   |      896 |
| `hun_Latn`   |      879 |
| `hye_Armn`   |      861 |
| `ind_Latn`   |      783 |
| `ibo_Latn`   |      838 |
| `isl_Latn`   |       81 |
| `ita_Latn`   |      851 |
| `jpn_Jpan`   |      590 |
| `jav_Latn`   |      835 |
| `kat_Geor`   |      372 |
| `kea_Latn`   |      770 |
| `kaz_Cyrl`   |      870 |
| `khm_Khmr`   |      439 |
| `kan_Knda`   |      606 |
| `kor_Hang`   |      535 |
| `kir_Cyrl`   |      811 |
| `lug_Latn`   |      703 |
| `lin_Latn`   |      778 |
| `lao_Laoo`   |      346 |
| `lit_Latn`   |      834 |
| `luo_Latn`   |      512 |
| `lvs_Latn`   |      555 |
| `mri_Latn`   |      877 |
| `mkd_Cyrl`   |      667 |
| `mal_Mlym`   |      809 |
| `khk_Cyrl`   |      869 |
| `mar_Deva`   |      869 |
| `zsm_Latn`   |      749 |
| `mlt_Latn`   |      816 |
| `mya_Mymr`   |      864 |
| `nob_Latn`   |      635 |
| `npi_Deva`   |      876 |
| `nld_Latn`   |      674 |
| `nso_Latn`   |      569 |
| `nya_Latn`   |      752 |
| `ory_Orya`   |      220 |
| `pan_Guru`   |      396 |
| `pol_Latn`   |      765 |
| `pbt_Arab`   |      628 |
| `por_Latn`   |      791 |
| `ron_Latn`   |      815 |
| `rus_Cyrl`   |      819 |
| `snd_Arab`   |      878 |
| `slk_Latn`   |      513 |
| `slv_Latn`   |      724 |
| `sna_Latn`   |      735 |
| `som_Latn`   |      874 |
| `srp_Cyrl`   |      766 |
| `swe_Latn`   |      681 |
| `swh_Latn`   |      780 |
| `tam_Taml`   |      714 |
| `tel_Telu`   |      567 |
| `tgk_Cyrl`   |      632 |
| `tha_Thai`   |      745 |
| `tur_Latn`   |      706 |
| `ukr_Cyrl`   |      773 |
| `urd_Arab`   |      482 |
| `uzn_Latn`   |      812 |
| `vie_Latn`   |      847 |
| `wol_Latn`   |      495 |
| `xho_Latn`   |      900 |
| `yor_Latn`   |      652 |
| `zho_Hant`   |      527 |
| `zul_Latn`   |      838 |
| `fuv_Latn`   |      848 |
| `gaz_Latn`   |      252 |

## ASR Results

Complete per-language results can be found in ./results.csv. This CSV file will be updated continuously as new results become available.

### Description

The usage by split for the dataset is described below.

- **Training / Validaton**: The models are trained and validated on clean English paragraphs from the training and validation splits constructed by the compilation script provided by Belebele. For more details, refer to the script here: https://github.com/facebookresearch/belebele/blob/main/assemble_training_set.py. The created dataset is available at: [https://huggingface.co/datasets/WueNLP/belebele-fleurs-train-val-text](https://huggingface.co/datasets/WueNLP/belebele-fleurs-train-val-text)
- **Testing**: We concatenate the sentence-level in-language ASR and speech-to-English translations of SeamlessM4Tv2-Large and WhisperV3-Large to evaluate zero-shot cross-lingual transfer with `NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse` and translate-test on speech-to-English translations with `LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse`

 model                                                    | Input                                   | Utterance-ASR-Quality   |   seed |     LR |   Batch Size | eng_Latn   | avg   |
:---------------------------------------------------------|:----------------------------------------|:------------------------|-------:|-------:|-------------:|:-----------|:------|
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     43 | 0.0001 |           32 | 96.0%      | 65.4% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     42 | 0.0001 |           32 | 95.6%      | 63.5% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     44 | 0.0001 |           32 | 94.7%      | 62.6% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     44 | 0.0002 |           32 | 94.3%      | 61.9% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     43 | 0.0002 |           32 | 95.3%      | 61.7% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     42 | 0.0002 |           32 | 95.3%      | 60.6% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     43 | 0.0001 |           32 | 95.3%      | 59.9% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     43 | 0.0002 |           32 | 93.8%      | 59.4% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     44 | 0.0001 |           32 | 94.4%      | 59.4% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     42 | 0.0001 |           32 | 95.0%      | 58.3% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     43 | 0.0003 |           32 | 92.8%      | 57.9% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     43 | 0.0001 |           32 | 95.3%      | 57.5% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     44 | 0.0002 |           32 | 93.2%      | 56.5% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     43 | 0.0001 |           32 | 95.4%      | 56.4% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     42 | 0.0003 |           32 | 93.4%      | 56.4% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     42 | 0.0001 |           32 | 94.8%      | 56.2% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     44 | 0.0001 |           32 | 94.0%      | 55.8% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     43 | 0.0002 |           32 | 94.1%      | 55.4% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     44 | 0.0001 |           32 | 94.3%      | 55.3% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     44 | 0.0002 |           32 | 94.5%      | 55.3% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     43 | 0.0002 |           32 | 94.7%      | 55.3% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     42 | 0.0002 |           32 | 94.1%      | 54.8% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     42 | 0.0001 |           32 | 94.9%      | 54.6% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | SeamlessM4Tv2-Large English Translation | best                    |     44 | 0.0003 |           32 | 91.6%      | 54.6% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     42 | 0.0002 |           32 | 94.4%      | 54.3% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     44 | 0.0002 |           32 | 93.5%      | 53.6% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     43 | 0.0003 |           32 | 91.0%      | 52.7% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     43 | 0.0003 |           32 | 93.1%      | 52.6% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     42 | 0.0002 |           32 | 94.1%      | 52.0% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     42 | 0.0003 |           32 | 92.9%      | 51.7% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     42 | 0.0003 |           32 | 93.2%      | 50.1% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     43 | 0.0003 |           32 | 90.9%      | 50.1% |
 LLM2Vec-Meta-Llama-3.1-8B-Instruct-mntp-unsup-simcse     | WhisperV3-Large English Translation     | best                    |     44 | 0.0003 |           32 | 91.6%      | 49.8% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     42 | 0.0003 |           32 | 94.2%      | 48.0% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | WhisperV3-Large ASR                     | best                    |     44 | 0.0003 |           32 | 25.5%      | 25.1% |
 NLLB-LLM2Vec-Meta-Llama-31-8B-Instruct-mntp-unsup-simcse | SeamlessM4Tv2-Large ASR                 | best                    |     44 | 0.0003 |           32 | 26.9%      | 24.9% |

# Citation

Should you be using this dataset, please cite the original Belebele dataset. Our dataset will be released ASAP.

```
@inproceedings{bandarkar-etal-2024-belebele,
    title = "The Belebele Benchmark: a Parallel Reading Comprehension Dataset in 122 Language Variants",
    author = "Bandarkar, Lucas  and
      Liang, Davis  and
      Muller, Benjamin  and
      Artetxe, Mikel  and
      Shukla, Satya Narayan  and
      Husa, Donald  and
      Goyal, Naman  and
      Krishnan, Abhinandan  and
      Zettlemoyer, Luke  and
      Khabsa, Madian",
    editor = "Ku, Lun-Wei  and
      Martins, Andre  and
      Srikumar, Vivek",
    booktitle = "Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.acl-long.44",
    doi = "10.18653/v1/2024.acl-long.44",
    pages = "749--775",
    abstract = "We present Belebele, a multiple-choice machine reading comprehension (MRC) dataset spanning 122 language variants. Significantly expanding the language coverage of natural language understanding (NLU) benchmarks, this dataset enables the evaluation of text models in high-, medium-, and low-resource languages. Each question is based on a short passage from the FLORES-200 dataset and has four multiple-choice answers. The questions were carefully curated to discriminate between models with different levels of general language comprehension. The English dataset on its own proves difficult enough to challenge state-of-the-art language models. Being fully parallel, this dataset enables direct comparison of model performance across all languages. We use this dataset to evaluate the capabilities of multilingual masked language models (MLMs) and large language models (LLMs). We present extensive results and findings, notably that despite significant cross-lingual transfer in English-centric LLMs, much smaller MLMs pretrained on balanced multilingual data still understand far more languages. Overall, Belebele opens up new avenues for evaluating and analyzing the multilingual capabilities of NLP systems.",
}
```
