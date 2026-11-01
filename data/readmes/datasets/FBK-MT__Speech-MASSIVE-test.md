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
  - name: test
    num_bytes: 13262388103.0
    num_examples: 35688
  download_size: 11927817444
  dataset_size: 13262388103.0
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
  - name: test
    num_bytes: 1119181327.0
    num_examples: 2974
  download_size: 1018547457
  dataset_size: 1119181327.0
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
  - name: test
    num_bytes: 1180482816.0
    num_examples: 2974
  download_size: 1041137735
  dataset_size: 1180482816.0
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
  - name: test
    num_bytes: 1251037095.0
    num_examples: 2974
  download_size: 1086481251
  dataset_size: 1251037095.0
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
  - name: test
    num_bytes: 917715093.0
    num_examples: 2974
  download_size: 882715495
  dataset_size: 917715093.0
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
  - name: test
    num_bytes: 1143852777.0
    num_examples: 2974
  download_size: 1019442321
  dataset_size: 1143852777.0
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
  - name: test
    num_bytes: 921644366.0
    num_examples: 2974
  download_size: 867570054
  dataset_size: 921644366.0
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
  - name: test
    num_bytes: 1143656146.0
    num_examples: 2974
  download_size: 1004936327
  dataset_size: 1143656146.0
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
  - name: test
    num_bytes: 1111068483.0
    num_examples: 2974
  download_size: 1008112754
  dataset_size: 1111068483.0
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
  - name: test
    num_bytes: 1126090758.0
    num_examples: 2974
  download_size: 974574306
  dataset_size: 1126090758.0
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
  - name: test
    num_bytes: 1190460054.0
    num_examples: 2974
  download_size: 1064179171
  dataset_size: 1190460054.0
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
  - name: test
    num_bytes: 1037699266.0
    num_examples: 2974
  download_size: 925672107
  dataset_size: 1037699266.0
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
  - name: test
    num_bytes: 1119499928.0
    num_examples: 2974
  download_size: 1034327505
  dataset_size: 1119499928.0
configs:
- config_name: all
  data_files:
  - split: test
    path: all/test-*
- config_name: ar-SA
  data_files:
  - split: test
    path: ar-SA/test-*
- config_name: de-DE
  data_files:
  - split: test
    path: de-DE/test-*
- config_name: es-ES
  data_files:
  - split: test
    path: es-ES/test-*
- config_name: fr-FR
  data_files:
  - split: test
    path: fr-FR/test-*
- config_name: hu-HU
  data_files:
  - split: test
    path: hu-HU/test-*
- config_name: ko-KR
  data_files:
  - split: test
    path: ko-KR/test-*
- config_name: nl-NL
  data_files:
  - split: test
    path: nl-NL/test-*
- config_name: pl-PL
  data_files:
  - split: test
    path: pl-PL/test-*
- config_name: pt-PT
  data_files:
  - split: test
    path: pt-PT/test-*
- config_name: ru-RU
  data_files:
  - split: test
    path: ru-RU/test-*
- config_name: tr-TR
  data_files:
  - split: test
    path: tr-TR/test-*
- config_name: vi-VN
  data_files:
  - split: test
    path: vi-VN/test-*
---

# Speech-MASSIVE Test Split

This dataset repository is **_only_** for `test` split of Speech-MASSIVE.

`train` and `dev` splits are available in the separate dataset repository. [https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE](https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE)

## Dataset Description
Speech-MASSIVE is a multilingual Spoken Language Understanding (SLU) dataset comprising the speech counterpart for a portion of the [MASSIVE](https://aclanthology.org/2023.acl-long.235) textual corpus. Speech-MASSIVE covers 12 languages (Arabic, German, Spanish, French, Hungarian, Korean, Dutch, Polish, European Portuguese, Russian, Turkish, and Vietnamese) from different families and inherits from MASSIVE the annotations for the intent prediction and slot-filling tasks. MASSIVE utterances' labels span 18 domains, with 60 intents and 55 slots. Full train split is provided for French and German, and for all the 12 languages (including French and German), we provide few-shot train, dev, test splits. Few-shot train (115 examples) covers all 18 domains, 60 intents, and 55 slots (including empty slots).

Our extension is prompted by the scarcity of massively multilingual SLU datasets and the growing need for versatile speech datasets to assess foundation models (LLMs, speech encoders) across diverse languages and tasks. To facilitate speech technology advancements, we release Speech-MASSIVE publicly available with [CC-BY-NC-SA-4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en).

Speech-MASSIVE is accepted at INTERSPEECH 2024 (Kos, GREECE) and nominated for the ISCA best student paper award.


## Dataset Summary
- `test`: test split available for all the 12 languages
- ⚠️ `dev`, `train_115`, `train` splits are available in  the separate dataset repository. [https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE](https://huggingface.co/datasets/FBK-MT/Speech-MASSIVE) ⚠️
- `dev`: dev split available for all the 12 languages
- `train_115`: few-shot split available for all the 12 languages (all 115 samples are cross-lingually aligned)
- `train`: train split available for French (fr-FR) and German (de-DE)

| lang | split      | # sample | # hrs | total # spk </br>(Male/Female/Unidentified) |
|:---:|:---:|:---:|:---:|:---:|
| ar-SA | dev | 2033 | 2.12 | 36 (22/14/0) |
| | test | 2974 | 3.23 | 37 (15/17/5) |
| | train_115 | 115 | 0.14 | 8 (4/4/0) |
| de-DE | dev | 2033 | 2.33 | 68 (35/32/1) |
| | test | 2974 | 3.41 | 82 (36/36/10) |
| | train | 11514 | 12.61 | 117 (50/63/4) |
| | train_115 | 115 | 0.15 | 7 (3/4/0) |
| es-ES | dev | 2033 | 2.53  | 109 (51/53/5) |
| | test | 2974 | 3.61  | 85 (37/33/15) |
| | train_115 | 115 | 0.13 | 7 (3/4/0) |
| fr-FR | dev | 2033 | 2.20 | 55 (26/26/3) |
| | test | 2974 | 2.65 | 75 (31/35/9) |
| | train | 11514 | 12.42 | 103 (50/52/1) |
| | train_115 | 115 | 0.12 | 103 (50/52/1) |
| hu-HU | dev | 2033 | 2.27 | 69 (33/33/3) |
| | test | 2974 | 3.30 | 55 (25/24/6) |
| | train_115 | 115 | 0.12 | 8 (3/4/1) |
| ko-KR | dev | 2033 | 2.12 | 21 (8/13/0) |
| | test | 2974 | 2.66 | 31 (10/18/3) |
| | train_115 | 115 | 0.14 | 8 (4/4/0) |
| nl-NL | dev | 2033 | 2.14 | 37 (17/19/1) |
| | test | 2974 | 3.30 | 100 (48/49/3) |
| | train_115 | 115 | 0.12 | 7 (3/4/0) |
| pl-PL | dev | 2033 | 2.24 | 105 (50/52/3) |
| | test | 2974 | 3.21 | 151 (73/71/7) |
| | train_115 | 115 | 0.10 | 7 (3/4/0) |
| pt-PT | dev | 2033 | 2.20 | 107 (51/53/3) |
| | test | 2974 | 3.25 | 102 (48/50/4) |
| | train_115 | 115 | 0.12 | 8 (4/4/0) |
| ru-RU | dev | 2033 | 2.25 | 40 (7/31/2) |
| | test | 2974 | 3.44 | 51 (25/23/3) |
| | train_115 | 115 | 0.12 | 7 (3/4/0) |
| tr-TR | dev | 2033 | 2.17 | 71 (36/34/1) |
| | test | 2974 | 3.00 | 42 (17/18/7) |
| | train_115 | 115 | 0.11 | 6 (3/3/0) |
| vi-VN | dev | 2033 | 2.10 | 28 (13/14/1) |
| | test | 2974 | 3.23 | 30 (11/14/5) |
|| train_115 | 115 | 0.11 | 7 (2/4/1) |


## How to use

### How to use

The `datasets` library allows you to load and pre-process your dataset in pure Python, at scale. The dataset can be downloaded and prepared in one call to your local drive by using the `load_dataset` function. 

For example, to download the French config, simply specify the corresponding language config name (i.e., "fr-FR" for French):

```python
from datasets import load_dataset

speech_massive_fr_test = load_dataset("FBK-MT/Speech-MASSIVE-test", "fr-FR", split="test", trust_remote_code=True)
```

In case you don't have enough space in the machine, you can stream dataset by adding a `streaming=True` argument to the `load_dataset` function call. Loading a dataset in streaming mode loads individual samples of the dataset at a time, rather than downloading the entire dataset to disk.
```python
from datasets import load_dataset

speech_massive_de_test = load_dataset("FBK-MT/Speech-MASSIVE-test", "de-DE", split="test", streaming=True, trust_remote_code=True)
list(speech_massive_de_test.take(2))
```

You can also load all the available languages and splits at once.
And then access each split.
```python
from datasets import load_dataset

speech_massive = load_dataset("FBK-MT/Speech-MASSIVE-test", "all", trust_remote_code=True)
multilingual_test = speech_massive['test']
```


## Dataset Structure

### Data configs
- `all`: load all the 12 languages in one single dataset instance
- `lang`: load only `lang` in the dataset instance, by specifying one of below languages
  - ```ar-SA, de-DE, es-ES, fr-FR, hu-HU, ko-KR, nl-NL, pl-PL, pt-PT, ru-RU, tr-TR, vi-VN```

### Data Splits
- `test`: test split available for all the 12 languages
> [!WARNING]
> `validation`, `train_115` and `train` splits are uploaded to a separate dataset repository.
- `validation`: validation(dev) split available for all the 12 languages
- `train_115`: few-shot (115 samples) split available for all the 12 languages
- `train`: train split available for French (fr-FR) and German (de-DE)


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


