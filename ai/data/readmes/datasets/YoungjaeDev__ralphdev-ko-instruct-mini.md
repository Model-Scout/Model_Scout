---
license: cc-by-sa-4.0
language:
  - ko
task_categories:
  - question-answering
  - text-generation
configs:
  - config_name: mini-128
    data_files:
      - split: train
        path: mini-128/train.jsonl
  - config_name: main-1024
    data_files:
      - split: train
        path: main-1024/train.jsonl
---

# RALPHDEV 한국어 짧은 답변 실습 데이터

이 데이터는 한국어 문단과 질문을 대화 형식으로 바꾼 소규모 SFT 실습 자료다. 모델이 주어진 문단에서 답을 찾아 짧게 쓰도록 학습하는 과정을 재현하는 데 쓴다. 공식 KLUE 벤치마크 점수를 보고하거나 일반적인 한국어 질의응답 성능을 대표하는 데이터가 아니다.

## 구성

| config | split | 행 수 | question_type 1 | question_type 2 |
|---|---:|---:|---:|---:|
| `mini-128` | `train` | 128 | 80 | 48 |
| `main-1024` | `train` | 1,024 | 640 | 384 |

두 config 모두 `train` split만 공개한다. `dev`와 `final`은 모델 선택과 최종 평가의 누출을 막기 위해 포함하지 않았다. SPRi 자료, 원문 PDF, 인증 정보도 포함하지 않았다.

각 `train.jsonl` 행은 원천 GUID를 유지한 `id`와 `messages`만 담는다. `messages`는 system, user, assistant 순서다. 별도 `provenance.jsonl`에는 같은 순서의 원천 GUID, 문서 출처, 제목, 질문 유형, 연결 성분 ID와 공식 정답을 기록했다.

## 저작자 표시와 변경 고지

원 저작물은 Sungjoon Park et al.의 **KLUE: Korean Language Understanding Evaluation**이다. [KLUE 데이터 카드의 Citation Information](https://huggingface.co/datasets/klue/klue#citation-information), [공식 KLUE 저장소](https://github.com/KLUE-benchmark/KLUE), [논문 원문](https://arxiv.org/abs/2105.09680)을 함께 확인할 수 있다. 원본과 이 수정본은 [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) 조건을 따른다. `mrc` config의 commit `349481ec73fff722f88e0453ca05c77a447d967c`을 고정해 사용했다.

이 배포물은 원 KLUE-MRC의 수정본이다. answerable 행과 유효한 공식 answer span을 필터링하고, 문단 또는 출처·제목 연결 성분을 격리했으며, 공식 train 일부를 추출해 `id`와 대화형 `messages`로 변환했다. 질문과 정답 문구는 합성·번역·윤문하지 않았다. `dev`와 `final`은 배포하지 않는다.

권장 인용은 공식 저장소가 제시한 다음 논문이다.

> Sungjoon Park et al. “KLUE: Korean Language Understanding Evaluation.” 2021.

이 수정본을 재배포하거나 다시 고치면 위 저작자·논문·원본 URL, 라이선스 URI를 보존하고 추가 변경 사항을 표시해야 한다.

## 추출 방법

`is_impossible=false`이고 비어 있지 않은 공식 정답의 span이 문단과 일치하는 행만 골랐다. 문단을 NFKC 정규화하고 공백을 합친 값이 같거나, 출처와 제목이 같은 행을 연결 성분으로 묶었다. 공식 train과 validation 양쪽에 걸친 성분은 모두 제외했다. 남은 공식 train 성분에서 seed 3407로 두 공개 config를 뽑았으며, 성분 경계의 남은 행을 다른 split에 다시 쓰지 않았다.

답변은 첫 번째 공식 정답을 그대로 사용했다. 답변을 새로 만들거나 번역·윤문하지 않았다. 따라서 이 데이터에는 합성 답변이 없다.

## 길이와 모델 조건

준비 단계에서는 commit으로 고정한 `unsloth/Qwen3.5-4B` processor의 chat template를 `enable_thinking=False`로 적용했다. 전체 학습 대화와 생성 prompt에 64 token을 더한 길이 가운데 큰 값을 검사했다. 후보 길이 1,024, 1,536, 2,048 token 중 두 config의 수량과 유형 할당을 만족하는 최소값인 1,024 token을 선택했고 문단을 자르지 않았다. 정확한 모델 revision과 파일 SHA-256은 배포물의 `manifest.json`에 있다.

## 사용 범위와 한계

이 데이터는 소규모 파인튜닝 절차를 설명하는 교육용 표본이다. 크기가 작고 KLUE-MRC의 일부 질문 유형만 정해진 비율로 담았으므로 공식 KLUE 평가나 실제 서비스 품질 판단에 쓰면 안 된다. 평가에는 원본 KLUE의 라이선스와 데이터 설명, 개인정보·편향 관련 주의사항도 함께 확인해야 한다.

원천과 가공 데이터는 CC BY-SA 4.0 조건에 따라 사용한다. 재배포하거나 수정본을 공개할 때 KLUE를 표시하고 동일 조건을 지켜야 한다.
