---
dataset_info:
  features:
  - name: category
    dtype:
      class_label:
        names:
          '0': people
          '1': animals
          '2': food
          '3': objects
          '4': vehicles
          '5': architecture
          '6': places
  - name: subcategory
    dtype:
      class_label:
        names:
          '0': portrait
          '1': home-cooked meal
          '2': beach
          '3': action shot
          '4': countryside
          '5': futuristic building
          '6': household pet
          '7': common household object
          '8': exotic animal
          '9': modeling photoshoot
          '10': forest
          '11': cityscape
          '12': ancient building
          '13': headshot
          '14': spacecraft
          '15': wrapped food product
          '16': close-up
          '17': fresh produce
          '18': industrial building
          '19': alien object
          '20': marine vehicle
          '21': common outdoor animal
          '22': body part macro
          '23': restaurant meal
          '24': alien animal
          '25': aircraft
          '26': exotic object
          '27': profile
          '28': product packaging
          '29': modern building
          '30': slice of life
          '31': land vehicle
  - name: prompt
    dtype: string
  - name: tags
    dtype: string
  splits:
  - name: train
    num_bytes: 960640
    num_examples: 800
  download_size: 581408
  dataset_size: 960640
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---
