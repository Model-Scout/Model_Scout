---
annotations_creators:
- machine-generated
language:
- ko
license: cc-by-nc-4.0
multilinguality:
- monolingual
size_categories:
- n<1K
source_datasets:
- original
task_categories:
- text-to-audio
pretty_name: Sound Atelier Korean Upbeat Lo-Fi Benchmark (10 Tracks)
tags:
- music
- lofi
- korean
- yue2
- sound-atelier
- audio-quality
- ebu-r128
---

# 🎵 Sound Atelier Korean Upbeat Lo-Fi Dataset (v1.0)

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Audio Format](https://img.shields.io/badge/Format-MP3%20320kbps-blue.svg)]()
[![Quality Screened](https://img.shields.io/badge/Screening-EBU%20R128%20%2B%20Whisper-green.svg)]()

## 📌 개요 (Overview)
본 데이터셋은 **사운드 아틀리에(Sound Atelier)** 자율 음악 생성 엔진을 통해 제작된 **10곡의 한국어 신나는 로파이(Upbeat Lo-Fi) 완곡(3~4분) 벤치마크 음원**입니다.

인간 개발자의 개별 가사 대필이나 수동 편곡 없이, **로컬 AI 자율 기획·작사(Rule Zero 중복 회피 룰) → YuE2 신경망 음원 합성 → EBU R128 음향 다이내믹스 및 Whisper 음성 인식 전수 검수**를 통과한 100% 무결점 음원으로 구성되어 있습니다.

---

## 🎼 10곡 트랙 상세 목록 (Track Catalog)

| 트랙 | 파일 경로 | 곡 제목 | 재생 시간 | 다이나믹스 (LRA) | 한국어 발음 일치율 | 내부 무음 | 판정 |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Track 01** | `data/track_01_warm_sunshine_way.mp3` | 따스한 햇살 길 | 3분 27초 (207.2s) | 11.1 LU | 98.5% | 0초 | **PASSED** |
| **Track 02** | `data/track_02_han_river_breeze.mp3` | 한강 바람을 타고 | 3분 54초 (234.1s) | 5.0 LU | 98.8% | 0초 | **PASSED** |
| **Track 03** | `data/track_03_alleyway_vinyl.mp3` | 골목의 레코드 | 3분 03초 (183.3s) | 6.5 LU | 99.5% | 0초 | **PASSED** |
| **Track 04** | `data/track_04_after_the_rain.mp3` | 비 갠 뒤 | 3분 38초 (218.8s) | 4.7 LU | 97.2% | 0초 | **PASSED** |
| **Track 05** | `data/track_05_rooftop_lemonade.mp3` | 옥상 정원의 레모네이드 | 3분 47초 (227.0s) | 4.4 LU | 99.4% | 0초 | **PASSED** |
| **Track 06** | `data/track_06_night_view_earphones.mp3` | 이어폰 속 야경 | 3분 37초 (217.7s) | 3.2 LU | 97.0% | 0초 | **PASSED** |
| **Track 07** | `data/track_07_weekend_bakery.mp3` | 주말 아침 베이커리 | 3분 19초 (199.7s) | 2.9 LU | 99.1% | 0초 | **PASSED** |
| **Track 08** | `data/track_08_moonlit_drive.mp3` | 달빛으로 물든 드라이브 | 3분 13초 (193.1s) | 5.0 LU | 99.0% | 0초 | **PASSED** |
| **Track 09** | `data/track_09_green_park_bench.mp3` | 푸른 공원 벤치 | 3분 22초 (202.8s) | 2.9 LU | 98.1% | 0초 | **PASSED** |
| **Track 10** | `data/track_10_festival_lights.mp3` | 축제의 불빛 | 3분 26초 (206.7s) | 4.4 LU | 99.9% | 0초 | **PASSED** |

---

## 🛡️ 품질 검수 기준 (Screening Criteria)
1. **가사 중복 배제 (Rule Zero)**: 벌스와 코러스 간의 무의미한 문장 반복을 0%로 제한
2. **다이나믹 레인지 (EBU R128 LRA)**: 단순 루프 정체를 차단하기 위해 `LRA >= 0.5 LU` 유지
3. **가창 언어 인식 (Whisper)**: 한국어 발음 신뢰도 95% 이상 엄격 통과
4. **신호 무결성**: 3초 이상의 중간 무음 구간 원천 배제

---

## 📜 라이선스 (License: CC BY-NC 4.0)
* 본 데이터셋은 **비상업적 연구, 학술 분석, 개인적 감상 목적**으로 자유롭게 청취 및 연구할 수 있습니다.
* 상업적 용도의 무단 배포, 재판매, 상업적 스트리밍 등록은 금지되어 있으며, 상업적 라이선싱 문의는 사운드 아틀리에(Sound Atelier) 팀으로 문의 바랍니다.
