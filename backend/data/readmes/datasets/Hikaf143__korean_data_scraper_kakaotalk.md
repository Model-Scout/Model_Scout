---
license: other
license_name: mkd-proprietary
language:
- ko
- en
task_categories:
- text-generation
tags:
- korean
- conversational
- kakaotalk
- corpus
- llm-pretraining
size_categories:
- n<1K
---

# Korean Data Scraper — KakaoTalk Export Corpus

**© 주식회사 MKD(MKD Inc.) — 모든 권리 보유 (All rights reserved).**
본 데이터셋은 주식회사 MKD(MKD Inc.)가 자체적으로 생성·소유한 내부 데이터이며,
외부 공개 라이선스가 부여되지 않은 사내 전용(proprietary) 자료입니다.

`Korean_data_scraper` 프로젝트의 `kakaotalk_export` 소스가 생성한 코퍼스입니다.
사용자 본인이 참여자인 KakaoTalk 그룹 채팅방 2곳의 공식 대화 내보내기(`대화 내보내기`)
파일을 파싱한 결과이며, 웹 스크래핑이 아니라 사용자가 직접 소유한 원본 데이터를
가공한 것입니다.

**비공개(Private) 저장소입니다.** 원본 채팅에 사내 인프라 정보와 다수 참여자의
실명이 포함되어 있어, 아래 정제 과정을 거쳤더라도 외부 공개를 의도한 데이터셋이
아닙니다.

## 정제(scrubbing) 내역

- **화자 가명처리**: 모든 화자명을 `SPEAKER_1`, `SPEAKER_2`, ... 형태로 치환. 화자
  라벨뿐 아니라 본문에 등장하는 실명 언급(대화에 참여하지 않고 이름만 언급된
  인물 포함, 총 19명)까지 동일한 가명으로 통일해 치환.
- **PII 스크러빙**: 주민등록번호, 전화번호, 이메일, 카드번호 마스킹.
- **인프라/시크릿 스크러빙**: SSH 접속 정보, DB 커넥션 문자열(MongoDB 등), 서버
  IP 주소, `.env` 형태로 노출된 API 키·토큰·비밀번호(Firebase, GitHub, Figma 등)
  마스킹.
- **시스템 메시지 제거**: 초대/퇴장/방장 임명 등 KakaoTalk 자동 생성 공지문, 날짜
  구분선, 사진/동영상/이모티콘 등 미디어 플레이스홀더 제거.

정제 로직은 `src/kds/sources/kakaotalk_export.py`와 `src/kds/clean/pii.py`에 있습니다.

## 스키마

파일당 1개 레코드(JSONL), 필드는 다음과 같습니다.

| 필드 | 타입 | 설명 |
|---|---|---|
| `id` | string | `kakaotalk_export:<파일명>` 형태의 문서 ID |
| `source` | string | 항상 `"kakaotalk_export"` |
| `text` | string | 가명처리·정제된 전체 대화 본문 (`"SPEAKER_N: 메시지"` 줄바꿈으로 연결) |
| `url` | null | 해당 없음 |
| `license` | string | `"n/a (own data)"` |
| `meta.turn_count` | int | 파싱된 발화(턴) 수 |
| `meta.source_file` | string | 원본 내보내기 파일명 |

## 데이터

| 파일 | 발화 수 | 설명 |
|---|---|---|
| `chats.txt` 유래 | 6,853 | 팀 프로젝트/개발 관련 그룹 채팅 |
| `members.txt` 유래 | 544 | 조직 구성원 업무일지 채팅 |

## 사용 시 주의

- 가명처리는 화자 식별자와 알려진 실명 언급을 치환한 것이며, 완전한 익명화를
  보장하지 않습니다. 배포·재공유 전 반드시 재검토하세요.
- 라이선스가 `n/a (own data)`인 만큼 이 조직 외부로의 공유는 권장하지 않습니다.
