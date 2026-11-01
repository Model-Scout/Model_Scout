---
annotations_creators:
- crowdsourced
language_creators:
- found
language:
- ar
- de
- es
- fr
- hu
- ko
- nl
- pl
- pt
- ru
- tr
- vi
license:
- cc-by-nc-sa-4.0
multilinguality:
- multilingual
size_categories:
- 10K<n<100K
source_datasets:
- extended
task_categories:
- audio-classification
- text-classification
- zero-shot-classification
- automatic-speech-recognition
task_ids: []
pretty_name: A Multilingual Speech Dataset for SLU and Beyond
tags:
- spoken language understanding
- slot filling
- intent classification
- speech translation
- speaker identification
dataset_info:
- config_name: all
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 532077103.0
    num_examples: 1380
  - name: validation
    num_bytes: 9234162673.0
    num_examples: 24396
  - name: train
    num_bytes: 8663179158.0
    num_examples: 23028
  download_size: 23732148508
  dataset_size: 18429418934.0
- config_name: ar-SA
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 48998773.0
    num_examples: 115
  - name: validation
    num_bytes: 734995890.0
    num_examples: 2033
  download_size: 1393604308
  dataset_size: 783994663.0
- config_name: de-DE
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 53545483.0
    num_examples: 115
  - name: validation
    num_bytes: 806014344.0
    num_examples: 2033
  - name: train
    num_bytes: 4364110141.0
    num_examples: 11514
  download_size: 9122884630
  dataset_size: 5223669968.0
- config_name: es-ES
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 46618371.0
    num_examples: 115
  - name: validation
    num_bytes: 876039204.0
    num_examples: 2033
  download_size: 1630709565
  dataset_size: 922657575.0
- config_name: fr-FR
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 43676175.0
    num_examples: 115
  - name: validation
    num_bytes: 760221849.0
    num_examples: 2033
  - name: train
    num_bytes: 4299069019.0
    num_examples: 11514
  download_size: 8798367724
  dataset_size: 5102967043.0
- config_name: hu-HU
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 43331409.0
    num_examples: 115
  - name: validation
    num_bytes: 787279684.0
    num_examples: 2033
  download_size: 1521560467
  dataset_size: 830611093.0
- config_name: ko-KR
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 49080895.0
    num_examples: 115
  - name: validation
    num_bytes: 734437927.0
    num_examples: 2033
  download_size: 1389365701
  dataset_size: 783518822.0
- config_name: nl-NL
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 43916209.0
    num_examples: 115
  - name: validation
    num_bytes: 742356980.0
    num_examples: 2033
  download_size: 1399350280
  dataset_size: 786273189.0
- config_name: pl-PL
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 37669862.0
    num_examples: 115
  - name: validation
    num_bytes: 775875548.0
    num_examples: 2033
  download_size: 1485329685
  dataset_size: 813545410.0
- config_name: pt-PT
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 43021520.0
    num_examples: 115
  - name: validation
    num_bytes: 760254037.0
    num_examples: 2033
  download_size: 1440053674
  dataset_size: 803275557.0
- config_name: ru-RU
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 41945958.0
    num_examples: 115
  - name: validation
    num_bytes: 779872923.0
    num_examples: 2033
  download_size: 1454761676
  dataset_size: 821818881.0
- config_name: tr-TR
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 40817549.0
    num_examples: 115
  - name: validation
    num_bytes: 750493456.0
    num_examples: 2033
  download_size: 1441835987
  dataset_size: 791311005.0
- config_name: vi-VN
  features:
  - name: id
    dtype: string
  - name: locale
    dtype: string
  - name: partition
    dtype: string
  - name: scenario
    dtype:
      class_label:
        names:
          '0': social
          '1': transport
          '2': calendar
          '3': play
          '4': news
          '5': datetime
          '6': recommendation
          '7': email
          '8': iot
          '9': general
          '10': audio
          '11': lists
          '12': qa
          '13': cooking
          '14': takeaway
          '15': music
          '16': alarm
          '17': weather
  - name: scenario_str
    dtype: string
  - name: intent_idx
    dtype:
      class_label:
        names:
          '0': datetime_query
          '1': iot_hue_lightchange
          '2': transport_ticket
          '3': takeaway_query
          '4': qa_stock
          '5': general_greet
          '6': recommendation_events
          '7': music_dislikeness
          '8': iot_wemo_off
          '9': cooking_recipe
          '10': qa_currency
          '11': transport_traffic
          '12': general_quirky
          '13': weather_query
          '14': audio_volume_up
          '15': email_addcontact
          '16': takeaway_order
          '17': email_querycontact
          '18': iot_hue_lightup
          '19': recommendation_locations
          '20': play_audiobook
          '21': lists_createoradd
          '22': news_query
          '23': alarm_query
          '24': iot_wemo_on
          '25': general_joke
          '26': qa_definition
          '27': social_query
          '28': music_settings
          '29': audio_volume_other
          '30': calendar_remove
          '31': iot_hue_lightdim
          '32': calendar_query
          '33': email_sendemail
          '34': iot_cleaning
          '35': audio_volume_down
          '36': play_radio
          '37': cooking_query
          '38': datetime_convert
          '39': qa_maths
          '40': iot_hue_lightoff
          '41': iot_hue_lighton
          '42': transport_query
          '43': music_likeness
          '44': email_query
          '45': play_music
          '46': audio_volume_mute
          '47': social_post
          '48': alarm_set
          '49': qa_factoid
          '50': calendar_set
          '51': play_game
          '52': alarm_remove
          '53': lists_remove
          '54': transport_taxi
          '55': recommendation_movies
          '56': iot_coffee
          '57': music_query
          '58': play_podcasts
          '59': lists_query
  - name: intent_str
    dtype: string
  - name: utt
    dtype: string
  - name: annot_utt
    dtype: string
  - name: worker_id
    dtype: string
  - name: slot_method
    sequence:
    - name: slot
      dtype: string
    - name: method
      dtype: string
  - name: judgments
    sequence:
    - name: worker_id
      dtype: string
    - name: intent_score
      dtype: int8
    - name: slots_score
      dtype: int8
    - name: grammar_score
      dtype: int8
    - name: spelling_score
      dtype: int8
    - name: language_identification
      dtype: string
  - name: tokens
    sequence: string
  - name: labels
    sequence: string
  - name: audio
    dtype:
      audio:
        sampling_rate: 16000
  - name: path
    dtype: string
  - name: is_transcript_reported
    dtype: bool
  - name: is_validated
    dtype: bool
  - name: speaker_id
    dtype: string
  - name: speaker_sex
    dtype: string
  - name: speaker_age
    dtype: string
  - name: speaker_ethnicity_simple
    dtype: string
  - name: speaker_country_of_birth
    dtype: string
  - name: speaker_country_of_residence
    dtype: string
  - name: speaker_nationality
    dtype: string
  - name: speaker_first_language
    dtype: string
  splits:
  - name: train_115
    num_bytes: 39454913.0
    num_examples: 115
  - name: validation
    num_bytes: 726320851.0
    num_examples: 2033
  download_size: 1421726907
  dataset_size: 765775764.0
configs:
- config_name: all
  data_files:
  - split: train_115
    path: all/train_115-*
  - split: validation
    path: all/validation-*
  - split: train
    path: all/train-*
- config_name: ar-SA
  data_files:
  - split: train_115
    path: ar-SA/train_115-*
  - split: validation
    path: ar-SA/validation-*
- config_name: de-DE
  data_files:
  - split: train_115
    path: de-DE/train_115-*
  - split: validation
    path: de-DE/validation-*
  - split: train
    path: de-DE/train-*
- config_name: es-ES
  data_files:
  - split: train_115
    path: es-ES/train_115-*
  - split: validation
    path: es-ES/validation-*
- config_name: fr-FR
  data_files:
  - split: train_115
    path: fr-FR/train_115-*
  - split: validation
    path: fr-FR/validation-*
  - split: train
    path: fr-FR/train-*
- config_name: hu-HU
  data_files:
  - split: train_115
    path: hu-HU/train_115-*
  - split: validation
    path: hu-HU/validation-*
- config_name: ko-KR
  data_files:
  - split: train_115
    path: ko-KR/train_115-*
  - split: validation
    path: ko-KR/validation-*
- config_name: nl-NL
  data_files:
  - split: train_115
    path: nl-NL/train_115-*
  - split: validation
    path: nl-NL/validation-*
- config_name: pl-PL
  data_files:
  - split: train_115
    path: pl-PL/train_115-*
  - split: validation
    path: pl-PL/validation-*
- config_name: pt-PT
  data_files:
  - split: train_115
    path: pt-PT/train_115-*
  - split: validation
    path: pt-PT/validation-*
- config_name: ru-RU
  data_files:
  - split: train_115
    path: ru-RU/train_115-*
  - split: validation
    path: ru-RU/validation-*
- config_name: tr-TR
  data_files:
  - split: train_115
    path: tr-TR/train_115-*
  - split: validation
    path: tr-TR/validation-*
- config_name: vi-VN
  data_files:
  - split: train_115
    path: vi-VN/train_115-*
  - split: validation
    path: vi-VN/validation-*
---

# Speech-MASSIVE

## Dataset Description
Speech-MASSIVE is a multilingual Spoken Language Understanding (SLU) dataset comprising the speech counterpart for a portion of the [MASSIVE](https://aclanthology.org/2023.acl-long.235) textual corpus. Speech-MASSIVE covers 12 languages (Arabic, German, Spanish, French, Hungarian, Korean, Dutch, Polish, European Portuguese, Russian, Turkish, and Vietnamese) from different families and inherits from MASSIVE the annotations for the intent prediction and slot-filling tasks. MASSIVE utterances' labels span 18 domains, with 60 intents and 55 slots. Full train split is provided for French and German, and for all the 12 languages (including French and German), we provide few-shot train, validation, test splits. Few-shot train (115 examples) covers all 18 domains, 60 intents, and 55 slots (including empty slots).

Our extension is prompted by the scarcity of massively multilingual SLU datasets and the growing need for versatile speech datasets to assess foundation models (LLMs, speech encoders) across diverse languages and tasks. To facilitate speech technology advancements, we release Speech-MASSIVE publicly available with [CC-BY-NC-SA-4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en).

Speech-MASSIVE is accepted at INTERSPEECH 2024 (Kos, GREECE) and nominated for the ISCA best student paper award.


## Dataset Summary
- `validation`: validation split available for all the 12 languages
- `test`: test split available for all the 12 languages
- `train_115`: few-shot split available for all the 12 languages (all 115 samples are cross-lingually aligned)
- `train`: train split available for French (fr-FR) and German (de-DE)

| lang | split      | # sample | # hrs | total # spk </br>(Male/Female/Unidentified) |
|:---:|:---:|:---:|:---:|:---:|
| ar-SA | validation | 2033 | 2.12 | 36 (22/14/0) |
| | test | 2974 | 3.23 | 37 (15/17/5) |
| | train_115 | 115 | 0.14 | 8 (4/4/0) |
| de-DE | validation | 2033 | 2.33 | 68 (35/32/1) |
| | test | 2974 | 3.41 | 82 (36/36/10) |
| | train | 11514 | 12.61 | 117 (50/63/4) |
| | train_115 | 115 | 0.15 | 7 (3/4/0) |
| es-ES | validation | 2033 | 2.53  | 109 (51/53/5) |
| | test | 2974 | 3.61  | 85 (37/33/15) |
| | train_115 | 115 | 0.13 | 7 (3/4/0) |
| fr-FR | validation | 2033 | 2.20 | 55 (26/26/3) |
| | test | 2974 | 2.65 | 75 (31/35/9) |
| | train | 11514 | 12.42 | 103 (50/52/1) |
| | train_115 | 115 | 0.12 | 103 (50/52/1) |
| hu-HU | validation | 2033 | 2.27 | 69 (33/33/3) |
| | test | 2974 | 3.30 | 55 (25/24/6) |
| | train_115 | 115 | 0.12 | 8 (3/4/1) |
| ko-KR | validation | 2033 | 2.12 | 21 (8/13/0) |
| | test | 2974 | 2.66 | 31 (10/18/3) |
| | train_115 | 115 | 0.14 | 8 (4/4/0) |
| nl-NL | validation | 2033 | 2.14 | 37 (17/19/1) |
| | test | 2974 | 3.30 | 100 (48/49/3) |
| | train_115 | 115 | 0.12 | 7 (3/4/0) |
| pl-PL | validation | 2033 | 2.24 | 105 (50/52/3) |
| | test | 2974 | 3.21 | 151 (73/71/7) |
| | train_115 | 115 | 0.10 | 7 (3/4/0) |
| pt-PT | validation | 2033 | 2.20 | 107 (51/53/3) |
| | test | 2974 | 3.25 | 102 (48/50/4) |
| | train_115 | 115 | 0.12 | 8 (4/4/0) |
| ru-RU | validation | 2033 | 2.25 | 40 (7/31/2) |
| | test | 2974 | 3.44 | 51 (25/23/3) |
| | train_115 | 115 | 0.12 | 7 (3/4/0) |
| tr-TR | validation | 2033 | 2.17 | 71 (36/34/1) |
| | test | 2974 | 3.00 | 42 (17/18/7) |
| | train_115 | 115 | 0.11 | 6 (3/3/0) |
| vi-VN | validation | 2033 | 2.10 | 28 (13/14/1) |
| | test | 2974 | 3.23 | 30 (11/14/5) |
|| train_115 | 115 | 0.11 | 7 (2/4/1) |


## How to use

### How to use

The `datasets` library allows you to load and pre-process your dataset in pure Python, at scale. The dataset can be downloaded and prepared in one call to your local drive by using the `load_dataset` function. 

For example, to download the French config, simply specify the corresponding language config name (i.e., "fr-FR" for French):

```python
from datasets import load_dataset

speech_massive_fr_train = load_dataset("FBK-MT/Speech-MASSIVE", "fr-FR", split="train")
```

In case you don't have enough space in the machine, you can stream dataset by adding a `streaming=True` argument to the `load_dataset` function call. Loading a dataset in streaming mode loads individual samples of the dataset at a time, rather than downloading the entire dataset to disk.
```python
from datasets import load_dataset

speech_massive_de_train = load_dataset("FBK-MT/Speech-MASSIVE", "de-DE", split="train", streaming=True)
list(speech_massive_de_train.take(2))
```

You can also load all the available languages and splits at once.
And then access each split.
```python
from datasets import load_dataset

speech_massive = load_dataset("FBK-MT/Speech-MASSIVE", "all")
multilingual_validation = speech_massive['validation']
```

Or you can load dataset's all the splits per language to separate languages more easily.
```python
from datasets import load_dataset, interleave_datasets, concatenate_datasets

# creating full train set by interleaving between German and French
speech_massive_de = load_dataset("FBK-MT/Speech-MASSIVE", "de-DE")
speech_massive_fr = load_dataset("FBK-MT/Speech-MASSIVE", "fr-FR")
speech_massive_train_de_fr = interleave_datasets([speech_massive_de['train'], speech_massive_fr['train']])

# creating train_115 few-shot set by concatenating Korean and Russian
speech_massive_ko = load_dataset("FBK-MT/Speech-MASSIVE", "ko-KR")
speech_massive_ru = load_dataset("FBK-MT/Speech-MASSIVE", "ru-RU")
speech_massive_train_115_ko_ru = concatenate_datasets([speech_massive_ko['train_115'], speech_massive_ru['train_115']])
```

## Dataset Structure

### Data configs
- `all`: load all the 12 languages in one single dataset instance
- `lang`: load only `lang` in the dataset instance, by specifying one of below languages
  - ```ar-SA, de-DE, es-ES, fr-FR, hu-HU, ko-KR, nl-NL, pl-PL, pt-PT, ru-RU, tr-TR, vi-VN```

### Data Splits
- `validation`: validation(dev) split available for all the 12 languages
- `train_115`: few-shot (115 samples) split available for all the 12 languages
- `train`: train split available for French (fr-FR) and German (de-DE)

> [!WARNING]
> `test` split is uploaded as a separate dataset on HF to prevent possible data contamination
- ⚠️ `test`: available **_only_** in the separate HF dataset repository. ⚠️
- [https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE-test](https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE-test)

### Data Instances

```json
{
  // Start of the data collected in Speech-MASSIVE
  'audio': {
    'path': 'train/2b12a21ca64a729ccdabbde76a8f8d56.wav', 
    'array': array([-7.80913979e-...7259e-03]),
    'sampling_rate': 16000},
  'path': '/path/to/wav/file.wav',
  'is_transcript_reported': False,
  'is_validated': True,
  'speaker_id': '60fcc09cb546eee814672f44',
  'speaker_sex': 'Female',
  'speaker_age': '25',
  'speaker_ethnicity_simple': 'White',
  'speaker_country_of_birth': 'France',
  'speaker_country_of_residence': 'Ireland',
  'speaker_nationality': 'France',
  'speaker_first_language': 'French',
  // End of the data collected in Speech-MASSIVE

  // Start of the data extracted from MASSIVE 
  // (https://huggingface.co/datasets/AmazonScience/massive/blob/main/README.md#data-instances)
  'id': '7509',
  'locale': 'fr-FR',
  'partition': 'train',
  'scenario': 2,
  'scenario_str': 'calendar',
  'intent_idx': 32,
  'intent_str': 'calendar_query',
  'utt': 'après les cours de natation quoi d autre sur mon calendrier mardi',
  'annot_utt': 'après les cours de natation quoi d autre sur mon calendrier [date : mardi]',
  'worker_id': '22',
  'slot_method': {'slot': ['date'], 'method': ['translation']},
  'judgments': {
    'worker_id': ['22', '19', '0'], 
    'intent_score': [1, 2, 1],
    'slots_score': [1, 1, 1],
    'grammar_score': [4, 4, 4],
    'spelling_score': [2, 1, 2],
    'language_identification': ['target', 'target', 'target']
    },
  'tokens': ['après', 'les', 'cours', 'de', 'natation', 'quoi', 'd', 'autre', 'sur', 'mon', 'calendrier', 'mardi'], 
  'labels': ['Other', 'Other', 'Other', 'Other', 'Other', 'Other', 'Other', 'Other', 'Other', 'Other', 'Other', 'date'],
  // End of the data extracted from MASSIVE
}
```
### Data Fields

`audio.path`: Original audio file name

`audio.array`: Read audio file with the sampling rate of 16,000

`audio.sampling_rate`: Sampling rate

`path`: Original audio file full path

`is_transcript_reported`: Whether the transcript is reported as 'syntatically wrong' by crowd-source worker

`is_validated`: Whether the recorded audio has been validated to check if the audio matches transcript exactly by crowd-source worker

`speaker_id`: Unique hash id of the crowd source speaker

`speaker_sex`: Speaker's sex information provided by the crowd-source platform ([Prolific](http://prolific.com))
- Male
- Female
- Unidentified : Information not available from Prolific

`speaker_age`: Speaker's age information provided by Prolific
- age value (`str`)
- Unidentified : Information not available from Prolific

`speaker_ethnicity_simple`: Speaker's ethnicity information provided by Prolific
- ethnicity value (`str`)
- Unidentified : Information not available from Prolific

`speaker_country_of_birth`: Speaker's country of birth information provided by Prolific
- country value (`str`)
- Unidentified : Information not available from Prolific

`speaker_country_of_residence`: Speaker's country of residence information provided by Prolific
- country value (`str`)
- Unidentified : Information not available from Prolific

`speaker_nationality`: Speaker's nationality information provided by Prolific
- nationality value (`str`)
- Unidentified : Information not available from Prolific

`speaker_first_language`: Speaker's first language information provided by Prolific
- language value (`str`)
- Unidentified : Information not available from Prolific


### Limitations

As Speech-MASSIVE is constructed based on the MASSIVE dataset, it inherently retains certain grammatical errors present in the original MASSIVE text. Correcting these errors was outside the scope of our project. However, by providing the `is_transcripted_reported` attribute in Speech-MASSIVE, we enable users of the dataset to be aware of these errors.


## License

All datasets are licensed under the [CC-BY-NC-SA-4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en).

### Acknowledgements

The speech collection was funded by the EU Horizon Europe (HE) Research and Innovation programme under grant No. 101070631 (UTTER project).

### Citation Information

Speech-MASSIVE is accepted at INTERSPEECH 2024 (Kos, Greece).
You can access the Speech-MASSIVE paper on [Interspeech archive](https://www.isca-archive.org/interspeech_2024/lee24i_interspeech.html) or [arXiv (same paper content but with appendix)](https://arxiv.org/abs/2408.03900).
Please cite the paper when referencing the Speech-MASSIVE corpus as:

```
@inproceedings{lee24i_interspeech,
  title     = {{Speech-MASSIVE: A Multilingual Speech Dataset for SLU and Beyond}},
  author    = {Beomseok Lee and Ioan Calapodescu and Marco Gaido and Matteo Negri and Laurent Besacier},
  year      = {2024},
  booktitle = {{Interspeech 2024}},
  pages     = {817--821},
  doi       = {10.21437/Interspeech.2024-957},
  issn      = {2958-1796},
}
```

