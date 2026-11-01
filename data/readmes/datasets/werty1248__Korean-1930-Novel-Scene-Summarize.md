---
license: mit
task_categories:
- summarization
language:
- ko
---

## 한국 저작권 만료 소설에 대한 씬 분리 및 요약 데이터 셋

- 원천 데이터 출처: https://gongu.copyright.or.kr/gongu/wrt/wrtCl/listWrtText.do?menuNo=200019
- 총 96개 소설 수집 및 전처리
  - 한자가 많은 소설 제외
  - 한자 제거, 띄어쓰기 전처리 수행
 
### 씬 분리
- 사용 모델: Gemini-1.5-Flash
- (띄어쓰기 포함) 100자 이상, 1200자 미만으로 적절한 문장에서 씬 단위로 분리하도록 지시
- 총 12,108씬 생성

### 요약
- 사용 모델: Gemini-1.5-Flash(때때로 GPT-4o)
- 각 Scene에서 인물, 주요 소품, 사건을 추출하고, 요약(scenario)을 생성하도록 함