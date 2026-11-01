---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: source
    dtype: string
  - name: text
    dtype: string
  - name: char_count
    dtype: int64
  - name: source_dataset
    dtype: string
  - name: quality_score
    dtype: int64
  - name: content_value
    dtype: int64
  - name: annotation_model
    dtype: string
  - name: critical_error
    dtype: bool
  - name: noncritical_error
    dtype: bool
  splits:
  - name: train
    num_bytes: 2156642472
    num_examples: 500000
  - name: test
    num_bytes: 586765106
    num_examples: 4096
  download_size: 1529715908
  dataset_size: 2743407578
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
language:
- ko
---

# Ko-Edu-Annotation-500K

- 한국어 사전학습 데이터 퀄리티 평가 모델 학습 데이터 셋
- Annotation 시간 기준 1x 5090에서 약 24시간
- 내용
  - `quality_score`: 최종 어노테이션 점수
  - `content_score`: 파싱 에러를 무시했을 때 내용의 점수
  - `critical_error`: 파싱 에러(핵심 그림/표/수식 누락)로 인해 원문을 알아보기 힘듦
  - `noncritical_error`: 파싱 에러(표가 plane text로 변환 등)가 있지만 원문을 이해할수는 있음

## Annotation Model

- [LilaRest/gemma-4-31B-it-NVFP4-turbo](https://huggingface.co/LilaRest/gemma-4-31B-it-NVFP4-turbo)
  - Gemma-4-31B 모델에 Attention까지 NVFP4로 양자화 한 모델
  - Solar Pro 4, Qwen 3.8 Flash Next 모델과 함께 비교했을 때, 정성적 평가(edge case 확인) 및 정량적 평가(동일 모델 3회 반복 평가의 Spearman 상관 계수와 서로 다른 모델 간 평가 간 Spearman 상관 계수가 0.78->0.73 정도로 큰 차이 없음)를 들어, 해당 모델이 충분히 변별력이 있다고 판단했습니다.

## Features

- **교과 범위 외 지식도 고평가**

[HuggingFaceFW/fineweb-edu-llama3-annotations](https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu-llama3-annotations)는 교과 과정을 벗어난 고급 지식에 대해 목적에 어긋나므로 점수를 낮게 평가하도록 설계되었습니다.

하지만 시간이 지나 소형 모델도 교과 과정 이상의 지식을 이해할 수 있게 되었으므로 분류기의 평가 기준도 높아질 필요가 있습니다.

실제로 이후 [HuggingFaceFW/finepdfs_edu_classifier_v2_eng_Latn](https://huggingface.co/HuggingFaceFW/finepdfs_edu_classifier_v2_eng_Latn)에서는 초등/중등 수준의 교육적 데이터라는 표현을 빼고, 학술 기사나 전문가 수준의 지식에 4~5점을 주도록 하고 있습니다.

따라서 이 어노테이션 데이터도 초등/중등 교육 수준을 벗어난 데이터라도 학습 가치가 높다면 고득점을 받도록 지시문을 만들었습니다.

- **웹 데이터 이외의 데이터도 포함**

한국어 데이터를 개방해주신 분들 덕분에, 무작위 웹 크롤링으로 수집하기 힘든 데이터들, 즉 논문 초록/사업보고서/법률 정보/국민 청원 등의 데이터를 추가할 수 있었습니다.

물론 전체 데이터의 약 75%를 차지하는 fineweb-2 데이터를 포함하여, 90% 가까히가 여전히 웹 데이터이긴 합니다.

자세한 데이터 출처는 아래 출처를 참고해 주세요.

- **2,048토큰 Truncation**

어노테이션 모델은 텍스트의 앞부분 2,048토큰을 보고 평가를 수행했습니다.

만약 2,048토큰 이후에 교육적인 정보가 등장한다면, 모델이 잘못 평가했을 가능성이 있습니다.

토큰 수 비율

| 점수 | < 512 | < 1024 | < 2048 | < 4096 | < 8192 |
| --- | --- | --- | --- | --- | --- |
| 문서 수 | 213,674 | 350,068 | **448,910** | 486,691 | 496,406 |


- **파싱 에러 검출**

몇몇 웹 데이터들은 교육적이지만 핵심이 되는 그림, 표, 수식이 누락되어 알아보기 힘들 수 있습니다.

원문을 이해하기 힘들 정도라면 critical, 이해할 수는 있는 정도라면 noncritical 에러로 분류하였습니다.

만약 critical error가 있다면 최종 quality score를 3점 이상 줄 수 없도록 만들었습니다.

## Score Distribution


**Train set** 

| 점수 | 데이터 수 | 비율 |
| --- | --- | --- |
| 0 | 66,561 | 13.31% |
| 1 | 260,562 | 52.11% |
| 2 | 113,626 | 22.73% |
| 3 | 45,875 | 9.18% |
| 4 | 13,376 | 2.68% |
| 합계 | 500,000 | 100% |

- 파싱 에러(Critical): 1,764개 (0.353%)
- 파싱 에러(Noncritical): 9,378개 (1.876%)

**Test set** 

| 점수 | 데이터 수 | 비율 |
| --- | --- | --- |
| 0 | 1,091 | 26.64% |
| 1 | 720 | 17.58% |
| 2 | 975 | 23.80% |
| 3 | 647 | 15.80% |
| 4 | 663 | 16.19% |
| 합계 | 4,096 | 100% |

- 파싱 에러(Critical): 123개 (3.003%)
- 파싱 에러(Noncritical): 1,067개 (26.050%)
  - 금융 공시(DARTS) 데이터 등에서 표 내용이 plain 텍스트로 추출되는 등

## Data Source

한국어 Fineweb 2 웹 데이터: [minpeter/fineweb-2-edu-korean-raw](https://huggingface.co/datasets/minpeter/fineweb-2-edu-korean-raw)
한국어 웹 데이터: [HAERAE-HUB/KOREAN-WEBTEXT](https://huggingface.co/datasets/HAERAE-HUB/KOREAN-WEBTEXT)
CC 2025~2026 데이터: [chaannwooff/CC-korean](https://huggingface.co/datasets/chaannwooff/CC-korean)
논문 초록: [ddokbaro/KCI_data](https://huggingface.co/datasets/ddokbaro/KCI_data)
아마존 제품 리뷰: [KETI-AIR/kor_amazon_polarity](https://huggingface.co/datasets/KETI-AIR/kor_amazon_polarity)
금융공시: [chaannwooff/Dartdoc](https://huggingface.co/datasets/chaannwooff/Dartdoc)
법령 데이터: [chaannwooff/Korean_law](https://huggingface.co/datasets/chaannwooff/Korean_law)
네이버 검색 결과: [chaannwooff/korean-web2](https://huggingface.co/datasets/chaannwooff/korean-web2)
글결(블로그 데이터 셋): [minpeter/geulgyeol-blog-korean](https://huggingface.co/datasets/minpeter/geulgyeol-blog-korean)
국민청원: [heegyu/korean-petitions](https://huggingface.co/datasets/heegyu/korean-petitions)

모든 데이터는 MinHash 기법을 통해 중복을 제거한 후 사용했습니다. 중복 제거는 Fineweb-edu의 세팅을 따라하되, 속도를 위해 Kiwi 토크나이저 대신 Mecab을 사용했습니다.

데이터 셋을 제작/공개해주신 모든 분들께 감사드립니다.

## Prompt

```
다음 한국어 텍스트가 범용 언어모델의 사전학습에 제공하는 장기적·재사용 가능한 내용 가치를 0~4점으로 평가하세요. 학교 수업에 적합한지나 문체가 쉬운지가 아니라, 입력만으로 실제 학습할 수 있는 지식, 관계, 절차, 추론, 전문 표현을 평가합니다.

기본 원칙:
- 웹 검색 없이 사실성·출처 신뢰도·최신성을 추측하지 마세요. 기관명·논문체·인용 형식만으로 가점하거나 낯선 주장만으로 감점하지 마세요.
- 대학·전문 지식과 법령·판결·계약·공시·규격 같은 1차 자료도 실제 정의·조건·예외·권리·의무·수치 기준을 담으면 높게 평가할 수 있습니다.
- 사건 결과, 가격, 일정, 상품 소식, 개인 반응처럼 수명이 짧은 정보는 일반 원리·인과·제도·비교·역사적 의미를 충분히 설명하지 않으면 낮게 평가하세요.
- 구체적이고 완결적이며 다른 상황에도 적용 가능한 생활·안전·조리·수리·도구 사용 절차는 가치가 있습니다.
- 웹 입력은 완결된 글이 아니라 문서의 한 절·항목·사례·매뉴얼 구간일 수 있습니다. 현재 입력이 그 자체로 유용한 학습 단위를 이루면 서론·결론이나 원문 전체가 없다는 이유만으로 감점하지 마세요. 이 원칙은 단순 나열이나 맥락 없는 단편을 높게 평가하라는 뜻이 아닙니다.
- 길이, 전문 용어 수, 항목 수 자체는 점수 근거가 아닙니다.

A. 내용 가치(content_value, 0~4)
파싱 손상 벌점은 적용하지 말고, 현재 입력에 정상적으로 남아 읽을 수 있는 내용만 평가하세요.

먼저 다음 다섯 가지 가치 축을 확인하세요.
1) 개념과 관계: 중요한 정의·분류·구조·상호관계를 설명하는가?
2) 원인과 기제: 왜 또는 어떻게 일어나는지를 설명하는가?
3) 근거와 사례: 주장에 필요한 근거·수치·사례·비교를 연결하는가?
4) 적용과 절차: 다른 상황에 적용하거나 재현할 수 있는 방법·단계를 제공하는가?
5) 조건과 경계: 전제·예외·한계·위험·권리와 의무를 설명하는가?

0 — 재사용 가능한 학습 신호가 사실상 없음. 광고·연락처·가격·시설명 템플릿, 답 없는 질문, 단순 감상·인사, 맥락 없는 일회성 결과·상품 정보, 반복·스팸·깨진 문자열이 중심임.

1 — 한두 개의 구체적 사실이나 짧은 조언은 있으나 단편적·국소적이며 관계·이유·맥락·완결성이 거의 없음. 짧은 뉴스·후기·목록이 일부 사실만 전달하는 경우도 포함함.

2 — 서로 관련된 여러 사실이나 기본 설명·절차를 일관되게 제공하여 의미 있는 내용을 배울 수 있음. 다만 설명·관계·조건·적용이 대체로 얕거나 제한되어 있음.

3 — 강하고 재사용 가능한 학습 단위이지만, 복잡한 내용을 이해하거나 적용하는 데 필요한 관계·조건·근거·단계 중 중요한 부분의 전개가 중간 수준에 머묾. 한 가치 축이 구체적으로 전개되었거나 여러 축이 나타나더라도, 아직 깊이·연결·조건화가 충분하지 않은 경우임. 상세한 개념 소개, 이유가 있는 실용 조언, 유용하지만 분기와 조건이 단순한 절차, 핵심 구조는 드러나지만 세부 관계가 제한된 전문 자료가 포함됨.

4 — 다음 충분조건 중 하나 이상을 만족하는 매우 강하고 재사용 가능한 학습 단위임.
(가) 하나의 복잡한 개념·논증·절차가 정의, 기제, 근거·사례, 조건·분기, 단계 중 여러 구체적 요소를 통해 깊게 전개되어 이해하거나 적용할 수 있음.
(나) 둘 이상의 가치 축이 각각 실질적으로 전개되고 서로 연결됨.
(다) 법령·판결·계약·공시·규격·전문 기술 자료가 여러 중요한 조건·조항·권리·의무·예외·분기와 그 효과를 드러냄.
4점은 이상적인 교과서, 완결된 원문, 분야 전체의 개관, 흠 없는 문장을 위한 점수가 아닙니다. 현재 입력만으로 강한 지식 구조를 배우거나 복잡한 판단·절차를 수행할 수 있는 하나의 절·항목·사례도 4점입니다. 반대로 사이트 고유 정보, 장황한 나열, 전문적인 문체나 길이만으로는 4점이 아닙니다.

경계 판단:
- 0/1: 재사용 가능한 구체적 명제나 절차가 하나라도 있는가?
- 1/2: 단편 사실을 넘어 연결된 정보나 기본 설명이 있는가?
- 2/3: 한 가치 축이 구체적으로 전개되어 이유·구조·절차를 배울 수 있는가?
- 3/4: 폭넓음과 깊이를 동시에 요구하지 마세요. 위 4점 충분조건 중 하나라도 충족하면 4점이고, 유용하지만 관계·조건·근거·단계의 전개가 중간 수준이면 3점입니다.

B. 입력 무결성
내용 가치와 별도로 판정하세요.
- critical_dependency_missing: 직접 관찰되는 추출·파싱 손상으로 중심 주장·계산·절차·규범 관계의 필수 요소를 이해하거나 재현할 수 없는가?
- noncritical_damage: 위 값은 false이지만 세부 주장·예시·순서·표기·코드의 이해나 재현을 제한하는 비사소한 손상이 있는가?

수식의 변수·연산자·등식, 필수 코드·명령·인수, 표의 핵심 값·열, 법률 논증의 핵심 조항·단계가 실제로 유실된 증거가 있으면 critical_dependency_missing=true입니다. 특히 수식 자리의 공백 때문에 문장이 "행렬 은", "성분은 이다"처럼 이어지거나 주변 설명만으로 정확한 관계를 복원할 수 없다면, 일반 설명이 읽히더라도 중심 수학 내용에는 critical_dependency_missing=true입니다. 일부 예시나 세부 표기만 유실되고 중심 내용을 재현할 수 있으면 noncritical_damage=true입니다.

발췌되지 않은 앞뒤 내용, 번호 건너뜀, 구간 경계에서 잘린 문장, 익명화된 <NAME>, 소수의 오탈자만으로는 손상이 아닙니다. 긴 문서의 시작·중간·끝 표식과 구간 사이 생략도 손상이 아닙니다.

설명 없이 다음 JSON 객체 하나만 출력하세요.
- content_value: 0~4 정수
- critical_dependency_missing: 불리언
- noncritical_damage: 불리언
- confidence: 0.0~1.0 실수

평가할 텍스트:
<EXAMPLE>
```