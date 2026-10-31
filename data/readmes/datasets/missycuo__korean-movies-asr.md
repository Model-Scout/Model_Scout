---
language:
- ko
- vi
task_categories:
- automatic-speech-recognition
tags:
- speech
- audio
- korean-speech
dataset_info:
  features:
  - name: movie_name
    dtype: string
  - name: audio_id
    dtype: int64
  - name: audio
    dtype: audio
  - name: korean_text
    dtype: string
  - name: vi_text
    dtype: string
  - name: duration
    dtype: float64
  - name: korean_text_with_timestamps
    dtype: string
  - name: start_time
    dtype: float64
  - name: end_time
    dtype: float64
configs:
- config_name: Alive
  data_files:
  - split: train
    path: Alive/Alive.parquet
- config_name: Badland_Hunters
  data_files:
  - split: train
    path: Badland_Hunters/Badland_Hunters.parquet
- config_name: Ballerina
  data_files:
  - split: train
    path: Ballerina/Ballerina.parquet
- config_name: Believer_2
  data_files:
  - split: train
    path: Believer_2/Believer_2.parquet
- config_name: Business_Proposal
  data_files:
  - split: train
    path: Business_Proposal/*.parquet
- config_name: Carter
  data_files:
  - split: train
    path: Carter/Carter.parquet
- config_name: D.P
  data_files:
  - split: train
    path: D.P/*.parquet
- config_name: Dream
  data_files:
  - split: train
    path: Dream/Dream.parquet
- config_name: Goedam
  data_files:
  - split: train
    path: Goedam/*.parquet
- config_name: Gyeongseong_Creature
  data_files:
  - split: train
    path: Gyeongseong_Creature/*.parquet
- config_name: Hometown_Cha-Cha-Cha
  data_files:
  - split: train
    path: Hometown_Cha-Cha-Cha/*.parquet
- config_name: Kill_Boksoon
  data_files:
  - split: train
    path: Kill_Boksoon/Kill_Boksoon.parquet
- config_name: King_the_Land
  data_files:
  - split: train
    path: King_the_Land/*.parquet
- config_name: Love_to_Hate_You
  data_files:
  - split: train
    path: Love_to_Hate_You/*.parquet
- config_name: Mission_Cross
  data_files:
  - split: train
    path: Mission_Cross/Mission_Cross.parquet
- config_name: Our_Beloved_Summer
  data_files:
  - split: train
    path: Our_Beloved_Summer/*.parquet
- config_name: Queen_of_Tears
  data_files:
  - split: train
    path: Queen_of_Tears/*.parquet
- config_name: Resident_Playbook
  data_files:
  - split: train
    path: Resident_Playbook/*.parquet
- config_name: Seoul_Vibe
  data_files:
  - split: train
    path: Seoul_Vibe/Seoul_Vibe.parquet
- config_name: Squid_Game
  data_files:
  - split: train
    path: Squid_Game/*.parquet
- config_name: Suspicious_Partner
  data_files:
  - split: train
    path: Suspicious_Partner/*.parquet
- config_name: Svaha_The_Sixth_Finger
  data_files:
  - split: train
    path: Svaha_The_Sixth_Finger/Svaha_The_Sixth_Finger.parquet
- config_name: Sweet_and_Sour
  data_files:
  - split: train
    path: Sweet_and_Sour/Sweet_and_Sour.parquet
- config_name: The_8th_Night
  data_files:
  - split: train
    path: The_8th_Night/The_8th_Night.parquet
- config_name: The_Call
  data_files:
  - split: train
    path: The_Call/The_Call.parquet
- config_name: The_Pirates_The_Last_Royal_Treasure
  data_files:
  - split: train
    path: The_Pirates_The_Last_Royal_Treasure/The_Pirates_The_Last_Royal_Treasure.parquet
- config_name: The_Trauma_Code_Heroes_on_Call
  data_files:
  - split: train
    path: The_Trauma_Code_Heroes_on_Call/*.parquet
- config_name: Time_to_Hunt
  data_files:
  - split: train
    path: Time_to_Hunt/Time_to_Hunt.parquet
- config_name: Weak_Hero
  data_files:
  - split: train
    path: Weak_Hero/*.parquet
- config_name: Welcome_to_Samdal-ri
  data_files:
  - split: train
    path: Welcome_to_Samdal-ri/*.parquet
- config_name: Wonderland
  data_files:
  - split: train
    path: Wonderland/Wonderland.parquet
---

# Korean Movies ASR Dataset

Tổng hợp 31 phim tiếng Hàn.