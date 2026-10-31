---
language:
- ko
license: other
tags:
- korean
- language-modeling
- kawk50m
---

# KAWK50M Training Data Archive

수집 원문, 정제 말뭉치, 토큰화 바이너리와 SFT 데이터의 전체 작업 사본입니다.

## 원본 데이터와 조건

- `HuggingFaceFW/fineweb-2`, `kor_Hang`, revision `af9c13333eb981300149d5ca60a8e9d659b276b9`: ODC-By-1.0 및 Common Crawl 이용 조건
- `Mkd-Yonas/keural-SFT-chatml-ko-v1`, revision `c56d7885efb37799deb1ecba471e4f6bf263852e`: Apache-2.0, CC-BY-4.0, CC0-1.0, MIT, ODC-By-1.0 허용 레코드만 선별
- `mkd-chanwoo/keural-rag-chatml-ko`, revision `aa9023d231a3451d25135d5aa84b12b48ca06450`: CC-BY-4.0 레코드

이 아카이브에는 여러 라이선스가 혼재하므로 단일 라이선스로 재허가하지 않습니다. 사용자는 각 원본의 라이선스와 귀속 조건을 따라야 합니다.

## 구성과 형식

- `raw/`: FineWeb2에서 받은 JSONL.GZ 원문과 수집 상태
- `clean-*`: 정규화·품질 필터·중복 제거 파생물
- `tokenized-*`: `uint16` 토큰 바이너리, 인덱스, manifest 및 상태 파일
- `sft-ko-v1/`: 5,120 토큰 길이로 패킹한 한국어 SFT 바이너리
- smoke, pilot, aborted 디렉터리도 재현성과 전체 작업 이력 보존을 위해 포함

웹 원문에는 개인정보, 유해 문구, 부정확한 정보가 남아 있을 수 있습니다. 공개 모델이나 서비스에 사용하기 전에 추가 개인정보·안전성 필터링을 수행하십시오.

이 저장소는 비공개 프로젝트 백업용입니다. 공개 전환 전에 원천 데이터 라이선스, 개인정보, 중복 파일 및 실패 실험 산출물을 검토해야 합니다.
