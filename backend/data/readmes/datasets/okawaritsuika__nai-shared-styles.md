---
language:
  - ko
  - en
tags:
  - novelai
  - image
  - text
  - art-style
  - not-for-all-audiences
viewer: false
---

# NAI shared styles

아카라이브 AI 그림 채널의 그림체 공유 게시글에서 수집한 예제 이미지와 NovelAI 생성 메타데이터입니다. V4.5·V5 그림체를 탐색하고 원본 게시글, 프롬프트와 생성 설정을 함께 확인하기 위한 자료입니다. 성인 대상 자료를 포함합니다.

## 파일과 사용법

- `NAImakeArtistGroup_shared_images_20261024_webp.zip`: 품질 90 WebP 이미지와 연결·무결성 검증용 `manifest.json`.
- `arca_style_seed.sqlite`: 게시글 출처, 이미지별 프롬프트·네거티브·모델·생성 설정을 담은 메타데이터 전용 SQLite DB.
- `archive_info.json`: ZIP 크기, 파일 수, SHA-256, 이미지 원본 대비 용량 및 검증 결과.

이번 배포의 시드와 다운로드 정보가 반영된 [NAImakeArtistGroup](https://github.com/okawaritsuika/NAImakeArtistGroup)에서 **공유 그림체 수집 → Hugging Face에서 빠르게 받기**를 사용하거나 같은 ZIP을 직접 받아 **내 ZIP 설치**를 선택할 수 있습니다. SQLite의 `arca_style_items`와 `arca_style_images`는 `item_id`로 연결됩니다. 이미지팩은 매니페스트의 게시글 주소와 안정 이미지 주소로 연결하며, EXIF UserComment의 JSON으로도 각 이미지의 프롬프트와 생성 설정을 읽을 수 있습니다.

이미지 4,425장, 게시글 583개이며 ZIP은 693,983,676 bytes입니다. 모든 이미지의 생성 메타데이터 보존을 검증했습니다. 입력 이미지 합계 3,034,891,349 bytes에서 ZIP 기준 77.1% 줄었습니다.

이전 앱은 그 버전에 고정된 이미지팩을 사용합니다. 이전 ZIP은 호환성을 위해 유지합니다.

## 수집과 변환

수집 기준일은 2026-10-24입니다. 기존 V4.5 공유 자료와 V5 출시 이후 공유 글을 대상으로 합니다. 공개 공유 의도가 있는 게시글을 선택하되, 이는 별도의 재배포 라이선스가 확인되었다는 뜻은 아닙니다. 명시적인 재배포 금지 및 미성년 관련 위험 신호가 확인된 항목은 공개 대상에서 제외합니다. 전체 게시판이나 모든 모델·그림체를 빠짐없이 대표하는 데이터셋은 아닙니다.

원본은 로컬에 보존하고 배포용 사본만 WebP로 변환합니다. 해상도를 유지하고, PNG 텍스트·NovelAI stealth·기존 WebP EXIF에서 읽은 전체 생성 JSON을 WebP EXIF에 보존합니다. 변환 전후 프롬프트·네거티브·캐릭터 프롬프트·모델·생성 설정을 모두 비교하며 불일치한 파일은 배포하지 않습니다. 화질 압축은 손실 압축이지만 메타데이터는 이 검증 기준으로 보존합니다.

## 출처, 권리와 삭제 요청

원문 게시글 주소는 DB와 ZIP 매니페스트의 `source_url`에 보존합니다. 원 게시글에는 별도 라이선스가 없는 경우가 많으며, 이 저장소는 개별 이미지·프롬프트에 새로운 CC0·상업적 이용·학습 허가를 부여하지 않습니다. 각 자료에 적용되는 권리와 원문 조건을 확인해야 합니다.

원 게시자·권리자가 제외를 요청하려면 이 저장소의 [Community](https://huggingface.co/datasets/okawaritsuika/nai-shared-styles/discussions)에 원문 주소 또는 파일 식별자를 알려 주세요. 민감한 개인정보는 게시하지 마세요. 정책 위반 신고는 Hugging Face의 신고 기능을 이용할 수 있습니다.

개인 사용자 DB 전체, 평가 기록, 로컬 메모·경로, 로그인 쿠키 및 API 키는 배포하지 않습니다.
