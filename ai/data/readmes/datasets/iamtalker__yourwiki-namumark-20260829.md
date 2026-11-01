---
license: cc-by-nc-sa-2.0
language:
- ko
pretty_name: YourWiki namumark dump of Namuwiki 20260829
tags:
- namuwiki
- wiki
- namumark
- korean
size_categories:
- 1M<n<10M
---

나무위키 나무마크 덤프 2026-08-29 (Namuwiki namumark dump 20260829)
======================================================================

무엇인가
- 나무위키(namu.wiki) 문서 1,787,556개 + 틀 21,480개 = 1,809,036개를 나무마크(위키 문법)로 담은 덤프입니다.
- 나무위키 공식 덤프(2015~2021)와 같은 JSON 형식입니다:
  [{"namespace": 0, "title": "...", "text": "나무마크 원문", "contributors": [...],
    "last_modified": "원 문서 최근 수정 시각", "source": "출처 설명"}, ...]
  공식 덤프를 읽던 도구(위키 엔진, 분석 도구)에서 그대로 쓸 수 있습니다.
- 파일: yourwiki-namumark-20260829-build20260928.7z (덤프 기준일 2026-08-29, 빌드 2026-09-28)
  7z 안에 JSON 파일 하나(namuwiki_20260829_namumark.json), 풀면 약 31GB, 압축 5,462,788,206바이트
  MD5     2466239f09c0b164ab0c9fcad65af85f
  SHA-256 7cc470f1eee12823c60db9cc628ef6656924c8f76bc054545ac476e84976d6ff

어떻게 만들었나
- 문서: archive.org 의 "Namuwiki 나무위키 Dump 20260829"(namuwiki-data-dump-20260829,
  나무위키 화면을 크롤링한 HTML)를 나무마크로 되돌렸습니다.
  광고·사이트 틀·크롤링 방지용 가짜 요소를 걷어내고 표·색·접기·각주·분류·넘겨주기를 복원했습니다.
- 틀: 2026 크롤링에는 틀 문서가 없어 2020-03-02 나무위키 공식 덤프(21,054개)와
  알파위키 2023-01-04 비공식 덤프(더위키 배포)의 틀 원본으로 채웠습니다.
- 한계: 크롤링한 화면에서 되돌렸기 때문에 문서 안의 틀은 펼쳐진 상태([include(...)] 가 아니라 내용 그대로)입니다.
  기여자 목록은 크롤링 덤프에 없어 contributors 가 비어 있습니다(원 문서의 역사: https://namu.wiki/history/문서명).
  이미지는 없습니다.
- 변환 도구와 설치 키트: https://github.com/iamtalker/yourwiki (유어위키)

라이선스
** 이 데이터는 CC BY-NC-SA 2.0 KR입니다. 상업적 이용은 금지됩니다. 이 키트를 사용해 광고를 붙이거나 상업적으로 운영하는 것은 라이선스 위반입니다. **
- 문서의 저작권은 각 기여자에게 있으며 CC BY-NC-SA 2.0 KR 로 이용할 수 있습니다.
  https://creativecommons.org/licenses/by-nc-sa/2.0/kr/
  - 저작자 표시: 각 문서의 원 주소 https://namu.wiki/w/문서명 과 그 역사(기여자 목록)를 밝혀 주세요.
  - 비영리: 영리 목적으로 쓸 수 없습니다.
  - 동일조건변경허락: 이 덤프로 만든 결과물도 같은 라이선스로 공개해야 합니다.
- 원 크롤링 덤프의 archive.org 항목에는 CC BY-NC-ND 4.0 으로 표기되어 있으나, 각 문서에 적힌 원 라이선스는
  CC BY-NC-SA 2.0 KR 이며 SA 조항에 따라 파생물도 같은 라이선스를 따라야 하므로 이 덤프는 CC BY-NC-SA 2.0 KR 로 배포합니다.

이 덤프는 나무위키 운영사(umanle S.R.L.)와 관계없는 비공식 자료입니다.
