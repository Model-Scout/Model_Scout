---
language:
- en
- ko
size_categories:
- 100K<n<1M
task_categories:
- translation
---
# AI Hub Ko-En Translation Dataset (Integrated)

AI Hub의 한-영 번역 관련 데이터셋 8개를 병합한 자료입니다.
병합 시 총 데이터 개수는 10,416,509개 이며, train / validation / test는 8:1:1 비율로 분할되었습니다.

- base-10m: 병합 데이터 100% 사용, 총 10,416,509개
- mini-1m: 병합 데이터 10% 사용 (base-10m의 각 세트 내에서 10% 임의 선택), 총 1,041,651개
- tiny-100k: 병합 데이터 1% 사용 (base-10m의 각 세트 내에서 1% 임의 선택), 총 104,165개

## Subsets

활용한 데이터셋 목록은 다음과 같으며, 데이터셋 이름 옆 번호는 aihubshell에서의 datasetkey입니다.

- [전문분야 한영 말뭉치](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=111) (111)
  - 총 개수: 1,350,000
  - 중복 제거 후 개수: 1,350,000
  - 사용 칼럼: '한국어', '영어'
- [한국어-영어 번역 말뭉치(기술과학)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=124) (124)
  - 총 개수: 1,344,631
  - 중복 제거 후 개수: 1,344,631
  - 사용 칼럼: 'ko', 'en'
- [한국어-영어 번역 말뭉치(사회과학)](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=125) (125)
  - 총 개수: 1,361,845
  - 중복 제거 후 개수: 1,361,825
  - 사용 칼럼: 'ko', 'en'
- [한국어-영어 번역(병렬) 말뭉치](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=126) (126)
  - 총 개수: 1,602,418
  - 중복 제거 후 개수: 1,599,924
  - 사용 칼럼: '원문', '번역문'
- [산업정보 연계 주요국 특허 영-한 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=563) (563)
  - 총 개수: 359,999
  - 중복 제거 후 개수: 358,424
  - 사용 칼럼: 'astrt_cont_kor', 'astrt_cont_eng'
- [일상생활 및 구어체 한-영 번역 병렬 말뭉치 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71265) (71265)
  - 총 개수: 2,700,345
  - 중복 제거 후 개수: 2,486,058
  - 사용 칼럼: 'ko', 'en'
- [기술과학 분야 한-영 번역 병렬 말뭉치 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71266) (71266)
  - 총 개수: 1,350,162
  - 중복 제거 후 개수: 1,328,987
  - 사용 칼럼: 'ko', 'en'
- [방송콘텐츠 한국어-영어 번역 말뭉치](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&aihubDataSe=data&dataSetSn=71382) (71382)
  - 총 개수: 587,084
  - 중복 제거 후 개수: 586,660
  - 사용 칼럼: '원문', '최종번역문'
