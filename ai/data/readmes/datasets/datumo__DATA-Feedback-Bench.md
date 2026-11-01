---
license: cc-by-4.0
pretty_name: BENCHMARK-Feedback-Bench-v0.1
language:
  - ko
  - en
tags:
  - evaluator
  - rubric
  - benchmark
---

# BENCHMARK-Feedback-Bench-v0.1

- 소유자: 권용훈
- 작성일: 2026-03-24
- 상태: active

## 1. 데이터셋 요약

### 1.1 목적 / 사용된 프로젝트명

| 항목       | 내용                                                          |
| -------- | ----------------------------------------------------------- |
| 데이터셋 목적  | LLM evaluator의 루브릭 준수 능력(rubric following)을 측정하기 위한 평가 벤치마크 |
| 사용 프로젝트명 | E-Star Evaluator                                            |
| 평가 대상    | 루브릭 기반 응답 평가 모델                                             |
| 주요 활용 방식 | 한국어 및 영어 환경에서 evaluator의 5점 척도 판정 성능 비교                     |
| 한국어 벤치마크 | Ko Feedback Bench                                           |
| 영어 벤치마크  | Feedback Bench                                              |
| 평가 설정    | Reference-free, debate 기반 재레이블링                             |
| 데이터셋 버전  | v0.1                                                        |

본 벤치마크는 제안 evaluator가 참조 답안에 의존하지 않고, 주어진 평가 기준과 점수별 설명을 따라 모델 응답의 품질을 판정할 수 있는지를 검증하기 위해 사용한다.

### 1.2 주요 특성

| 항목                     | 내용                                    |
| ---------------------- | ------------------------------------- |
| 총 인스턴스 수               | 2,000개                                |
| 데이터 분할                 | `ko_feedback_bench`, `feedback_bench` |
| 한국어 데이터                | 1,000개                                |
| 영어 데이터                 | 1,000개                                |
| 레이블 척도                 | 1~5점                                  |
| 원천 데이터                 | Feedback Bench                        |
| 한국어 데이터 생성 방식          | 영어 원본의 기계번역 및 검수                      |
| 레이블 생성 방식              | 복수 judge 모델의 debate 기반 재레이블링          |
| Reference answer 사용 여부 | 평가 입력에서 제외                            |
| 생성 유형                  | Human+AI                              |

#### 데이터 분할

| Split               | 언어     |      샘플 수 | 설명                                                   |
| ------------------- | ------ | --------: | ---------------------------------------------------- |
| `ko_feedback_bench` | 한국어    |     1,000 | 영어 원본의 instruction, rubric 및 response를 한국어로 변환한 벤치마크 |
| `feedback_bench`    | 영어     |     1,000 | 원본 영어 데이터를 reference-free 설정으로 재구성하고 재레이블링한 벤치마크     |
| **합계**              | 한국어·영어 | **2,000** | 언어 간 비교를 위한 대응형 데이터 구성                               |

두 split은 완전히 독립적인 2,000개 평가 사례가 아니라, 동일하거나 대응되는 평가 사례를 영어와 한국어로 구성한 paired benchmark이다. 따라서 언어 통합 성능을 계산하거나 통계 검정을 수행할 때 두 split을 독립 표본처럼 취급하지 않도록 주의해야 한다.

#### 데이터 필드

| 필드                        | 타입     | 설명                                             |
| ------------------------- | ------ | ---------------------------------------------- |
| `orig_instruction`        | string | 평가 대상 응답을 생성할 때 사용된 원본 instruction             |
| `orig_criteria`           | string | 응답 평가에 적용되는 루브릭 기준                             |
| `orig_score1_description` | string | 1점에 해당하는 평가 기준 설명                              |
| `orig_score2_description` | string | 2점에 해당하는 평가 기준 설명                              |
| `orig_score3_description` | string | 3점에 해당하는 평가 기준 설명                              |
| `orig_score4_description` | string | 4점에 해당하는 평가 기준 설명                              |
| `orig_score5_description` | string | 5점에 해당하는 평가 기준 설명                              |
| `orig_response`           | string | evaluator가 평가할 모델 응답                           |
| `user`                    | string | instruction, rubric 및 response를 결합한 평가 입력 프롬프트 |
| `system`                  | string | evaluator의 역할과 출력 규칙을 정의한 시스템 프롬프트             |
| `orig_score`              | int    | Debate 기반 합의 절차로 재부여된 1~5점 레이블                 |

`ko_feedback_bench`에서는 `orig_instruction`, `orig_criteria`, 점수별 설명 및 `orig_response`가 한국어로 제공된다. `feedback_bench`에서는 동일한 필드가 영어로 제공된다.

#### 데이터 구조

```text
DatasetDict({
    ko_feedback_bench: Dataset({
        features: [
            "orig_instruction",
            "orig_score3_description",
            "orig_score4_description",
            "orig_response",
            "orig_score1_description",
            "orig_criteria",
            "orig_score2_description",
            "orig_score5_description",
            "user",
            "system",
            "orig_score"
        ],
        num_rows: 1000
    }),
    feedback_bench: Dataset({
        features: [
            "orig_instruction",
            "orig_score3_description",
            "orig_score4_description",
            "orig_response",
            "orig_score1_description",
            "orig_criteria",
            "orig_score2_description",
            "orig_score5_description",
            "user",
            "system",
            "orig_score"
        ],
        num_rows: 1000
    })
})
```

### 1.3 생성/수집 배경

기존 Feedback Bench는 영어 환경에서 evaluator의 루브릭 기반 평가 능력을 측정하기 위해 구축된 벤치마크이다. 그러나 영어 데이터만으로는 한국어 evaluator가 한국어 instruction, rubric 및 response를 얼마나 정확히 해석하고 평가하는지 검증하기 어렵다.

이를 보완하기 위해 원본 Feedback Bench의 1,000개 평가 인스턴스를 한국어로 변환하여 Ko Feedback Bench를 구축하였다. 영어 원본과 한국어 변환본은 동일한 평가 구조를 유지하므로 evaluator의 성능 차이가 단순한 문제 구성 차이보다 언어적 차이에서 발생하는지 비교할 수 있다.

또한 영어와 한국어 데이터 모두 원본 reference answer를 평가 입력에서 제외하고, 복수 judge 모델의 debate 기반 합의 절차를 통해 레이블을 다시 부여하였다. Reference-free 설정은 실제 산업 환경에서 정답 예시 없이 instruction, rubric 및 평가 대상 response만으로 품질을 판단해야 하는 조건을 반영한다.

### 1.4 민감도

**민감도: 하 — 외부 노출 가능**

원천 데이터와 본 가공 데이터셋은 CC BY 4.0 조건에 따라 공개 및 재배포할 수 있다. 외부 공개 시에는 원 저작자와 원본 데이터 출처를 표시하고, 한국어 번역, reference 제거 및 debate 기반 재레이블링 등 변경사항을 명시해야 한다.

단, 공개 전 내부 시스템 프롬프트, 미공개 모델 정보 또는 운영 환경과 관련된 정보가 포함되어 있지 않은지 별도로 확인한다.

---

## 2. 데이터셋 생성 방식

### Data Collection / Generation

### 2.1 원천 데이터 소스

| 항목         | 내용                       |
| ---------- | ------------------------ |
| 원본 데이터셋    | Feedback Bench           |
| 저자         | Kim et al., 2024a        |
| 원본 인스턴스 수  | 1,000개                   |
| 원본 언어      | 영어                       |
| 데이터 유형     | 루브릭 기반 모델 응답 평가 데이터      |
| 원본 라이선스    | CC BY 4.0                |
| 원본 저장소     | 정확한 URL 및 사용 버전 추가 기재 필요 |
| 원본 다운로드 시점 | 추가 기록 필요                 |

### 2.2 데이터 EDA 및 핵심 특징

#### 원본 대비 변경점

| 항목               | 원본 Feedback Bench | 본 데이터셋                               |
| ---------------- | ----------------- | ------------------------------------ |
| 언어               | 영어                | 영어 및 한국어                             |
| 데이터 규모           | 1,000개            | 영어 1,000개 + 한국어 1,000개               |
| 루브릭 구조           | 원본 카테고리 및 5점 척도   | 원본 구조 유지                             |
| 한국어 버전           | 없음                | instruction, rubric, response 번역본 제공 |
| Reference answer | 원본 평가 구성에 포함      | 평가 입력에서 제외                           |
| 레이블              | 원본 레이블            | Debate 기반 5점 레이블로 교체                 |
| 평가 방식            | 원본 설정             | Reference-free                       |
| 언어 간 비교          | 지원하지 않음           | 대응되는 영어·한국어 split 비교 가능              |

#### 핵심 특징

* 영어 원본 1,000개와 이에 대응하는 한국어 변환본 1,000개로 구성된다.
* 두 언어 split은 동일한 루브릭 카테고리 및 5점 평가 구조를 유지한다.
* `orig_score`는 이름과 달리 원본 레이블이 아니라 debate 기반으로 재부여된 레이블이다.
* Reference answer를 제외하여 evaluator가 평가 기준만으로 독립적인 판단을 수행하도록 설계하였다.
* 동일한 평가 사례에 대한 영어·한국어 성능 차이를 비교할 수 있다.
* 한국어 split은 기계번역 품질과 문화·언어적 자연스러움의 영향을 받을 수 있다.

#### 추가 기록이 필요한 EDA 항목

* 한국어와 영어 split의 샘플 ID 대응 관계
* 루브릭 카테고리별 인스턴스 수
* 언어별 1~5점 레이블 분포
* 영어와 한국어 대응 샘플 간 레이블 일치율
* Debate 이전·이후 레이블 변경률
* Judge 모델 간 초기 합의율 및 최종 합의율
* 번역 검수 전·후 수정 비율
* instruction, rubric 및 response별 토큰 길이 분포
* 중복 또는 준중복 인스턴스 비율
* 학습 데이터와 벤치마크 간 instruction, response 및 rubric 중복 여부

#### 필드명 관련 주의사항

`orig_score`는 일반적으로 원본 점수를 의미하는 이름으로 해석될 수 있으나, 실제로는 debate 기반 재레이블링 결과를 저장한다. 데이터 사용자의 혼동을 줄이기 위해 향후 버전에서는 다음 중 하나를 권장한다.

* `debate_score`로 필드명 변경
* `orig_score`는 원본 점수로 유지하고 `debate_score`를 별도 추가
* 데이터 카드에 `orig_score`가 재레이블링 결과라는 점을 명시

### 2.3 가공 또는 생성 방식

**생성 유형: Human+AI**

사람이 데이터 변환 범위, reference-free 평가 설정, 번역 검수 기준, debate 절차 및 최종 데이터 구조를 설계하였다. 한국어 초벌 번역과 재레이블링은 AI를 활용하였으며, 한국어 번역 결과는 사람이 검수하였다.

#### Ko Feedback Bench 구축 절차

1. 원본 Feedback Bench의 다음 필드를 기계번역으로 한국어화한다.

   * Instruction
   * 평가 기준 및 점수별 루브릭 설명
   * Model response
2. 한국어 변환 과정에서 원문의 평가 의미와 점수 기준이 유지되는지 검수한다.
3. 어색하거나 의미가 달라진 번역 표현을 수정한다.
4. 원본 reference answer를 evaluator 입력에서 제외한다.
5. 한국어 instruction, rubric 및 response를 평가 프롬프트 형식으로 결합한다.
6. 복수 judge 모델의 debate 기반 합의 절차를 수행한다.
7. 합의 결과에 따라 1~5점 레이블을 새로 부여한다.
8. 최종 결과를 `ko_feedback_bench` split으로 구성한다.

#### Feedback Bench 영어 재구성 절차

1. 원본 Feedback Bench의 영어 instruction, rubric 및 response를 유지한다.
2. 원본 reference answer를 evaluator 입력에서 제외한다.
3. 한국어 데이터와 동일한 평가 프롬프트 구조를 적용한다.
4. 동일한 복수 judge 모델의 debate 기반 합의 절차를 수행한다.
5. 합의 결과에 따라 1~5점 레이블을 새로 부여한다.
6. 최종 결과를 `feedback_bench` split으로 구성한다.

#### Debate 기반 재레이블링 절차

* 복수 judge 모델이 각 인스턴스를 독립적으로 평가한다.
* 각 모델은 instruction, rubric 및 response를 바탕으로 1~5점 점수를 제안한다.
* 모델들은 다른 judge의 판단과 근거를 상호 검토한다.
* 상호 검토 후 초기 점수를 유지하거나 수정한다.
* 사전에 정의된 합의 규칙에 따라 최종 점수를 결정한다.
* 합의가 성립하지 않거나 출력 형식이 유효하지 않은 샘플의 처리 기준은 별도로 기록한다.

재현성을 위해 실제 사용한 judge 모델명과 버전, debate 라운드 수, 합의 기준, 동률 처리 방식, 프롬프트 버전 및 생성 파라미터를 추가로 기록해야 한다.

### 2.4 알려진 한계 및 사용 시 주의사항

#### 번역 품질의 영향

Ko Feedback Bench는 기계번역을 기반으로 하므로 어휘 선택, 문장 자연스러움, 높임법 및 문화적 맥락에서 번역 노이즈가 존재할 수 있다. 번역 오류는 evaluator의 한국어 이해 능력과 무관한 성능 저하 요인이 될 수 있다.

#### 레이블링 절차의 공유

학습 데이터와 벤치마크가 동일하거나 유사한 debate 기반 레이블링 절차로 구축되었다면, 평가 결과는 절대적인 평가 품질뿐 아니라 해당 judge 모델군의 합의 기준과 제안 evaluator가 얼마나 정렬되어 있는지도 반영할 수 있다.

#### 언어별 레이블 등가성

영어와 한국어 split을 각각 재레이블링했다면 동일한 원본 사례라도 최종 레이블이 달라질 수 있다. 언어 간 성능을 직접 비교하기 전에 대응 샘플의 레이블 일치율과 변경 사유를 확인해야 한다.

#### 통계적 독립성

영어와 한국어 데이터는 서로 대응되는 번역 쌍이므로 총 2,000개를 독립 표본으로 간주해서는 안 된다. 언어 간 차이 분석에는 paired accuracy, paired agreement 또는 대응표본 기반 검정을 사용하는 것이 적절하다.

#### 데이터 오염 가능성

평가 대상 모델 또는 evaluator가 원본 Feedback Bench, 한국어 번역본이나 재레이블링 결과를 학습에 사용했는지 확인해야 한다. 특히 동일한 데이터 생성 절차를 사용한 SFT 데이터와 benchmark 간 중복 여부를 검증해야 한다.

---

## 3. 라이선스

### 3.1 원천 데이터 및 가공 데이터 라이선스

* 라이선스: **CC BY 4.0**
* 원본 데이터: Feedback Bench
* 원 저자: Kim et al., 2024a
* 원본 저장소 및 논문 링크: 추가 기재 필요

CC BY 4.0은 자료의 복제, 재배포, 수정 및 가공을 허용한다. 따라서 영어 원본의 reference 제거, 한국어 번역 및 debate 기반 재레이블링을 통해 생성된 본 데이터셋도 라이선스 조건을 준수하는 범위에서 공개할 수 있다.

### 3.2 외부 이용 및 배포 조건

외부 공개 또는 재배포 시 다음 정보를 함께 제공해야 한다.

1. 원 저작자 및 Feedback Bench 출처
2. CC BY 4.0 라이선스명과 라이선스 링크
3. 원본 데이터에 적용한 변경사항

   * 한국어 기계번역 및 사람 검수
   * Reference answer 제거
   * 평가 프롬프트 재구성
   * Debate 기반 레이블 재생성
4. 관련 연구의 인용 정보
5. 원 저작자가 본 가공 데이터셋이나 평가 결과를 보증한다는 인상을 주지 않는 고지

### 3.3 변경사항 권장 고지문

```text
This dataset is derived from Feedback Bench (Kim et al., 2024a).

The original English instances were reconfigured for reference-free
evaluation and relabeled using a multi-model debate procedure.
A Korean split was created by machine translation and human review.

The dataset is distributed under the Creative Commons Attribution
4.0 International License (CC BY 4.0).
```

### 3.4 인용 정보

현재 문서에는 Feedback Bench(Kim et al., 2024a)의 정확한 논문명과 BibTeX가 포함되어 있지 않다. 외부 공개 전 원본 논문 정보를 확인하여 다음 형식으로 추가한다.

```bibtex
@inproceedings{feedback-bench-2024,
    title     = {확인 필요},
    author    = {Kim et al.},
    booktitle = {확인 필요},
    year      = {2024}
}
```
