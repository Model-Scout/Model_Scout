---
language:
- ko
license: other
license_name: koevd-dataset-research-use-terms-v1
license_link: LICENSE.md
task_categories:
- text-classification
- multiple-choice
size_categories:
- n<1K
tags:
- korean
- ethics
- safety-evaluation
- difficulty-subsets
- benchmark
configs:
- config_name: task1
  data_files:
  - split: test
    path: viewer/task1/test.parquet
  - split: easy
    path: viewer/task1/easy.parquet
  - split: mid
    path: viewer/task1/mid.parquet
  - split: hard
    path: viewer/task1/hard.parquet
  default: true
- config_name: task2_best
  data_files:
  - split: test
    path: viewer/task2_best/test.parquet
  - split: easy
    path: viewer/task2_best/easy.parquet
  - split: mid
    path: viewer/task2_best/mid.parquet
  - split: hard
    path: viewer/task2_best/hard.parquet
- config_name: task2_relative
  data_files:
  - split: test
    path: viewer/task2_relative/test.parquet
  - split: easy
    path: viewer/task2_relative/easy.parquet
  - split: mid
    path: viewer/task2_relative/mid.parquet
  - split: hard
    path: viewer/task2_relative/hard.parquet
- config_name: task5_diagnostic
  data_files:
  - split: test
    path: viewer/task5_diagnostic/test.parquet
---

# KoEVD-Compact: 기존 응답으로 선정한 난이도별 평가 서브셋

This is a derived reference subset of [KoEVD](https://huggingface.co/datasets/KETI-NLP/KoEVD), not a replacement of its official evaluation splits. It preserves the existing selected items, labels and difficulty assignments; no model inference or re-selection was performed for this release. The 400 scored task instances and optional 200 tool-diagnostic instances are distinct from the full benchmark.

## 규모와 HF 구성

| 구성 | 전체 `test` | `easy` | `mid` | `hard` | 대표 지표 |
|---|---:|---:|---:|---:|---|
| `task1` 입력 위험 판단 (기본) | 200 | 50 | 50 | 100 | Macro F1 |
| `task2_best` 안전 응답 식별 | 100 | 25 | 25 | 50 | 정답률 |
| `task2_relative` 유해 응답 식별 | 100 | 25 | 25 | 50 | 정답률 |
| `task5_diagnostic` 모의 도구 선택 | 200 | - | - | - | 위험 호출·과잉 거절 진단 |

`easy/mid/hard`는 각 과업 안에서 서로 겹치지 않으며 합집합이 `test`입니다. test에 난이도 split을 더해 문항 수를 중복 합산하지 않습니다. HF의 총 행 수 1,000은 겹치는 split을 더한 표시이며 주 과업400+선택 진단200과 구분합니다. 과업 사이에는 원발화가 겹칠 수 있으므로 600개 독립 원발화라고 부르지 않습니다. 유해 응답 식별은 유해 답변 생성이 아니라 주어진 후보 중 식별하는 과업입니다.

## 난이도의 의미

선정에는 기존 여섯 모델의 유효 답안을 사용했고 이번 공개 때문에 라벨·문항·선정 모델을 바꾸지 않았습니다. Task1 Hard는 클래스 안의 상대적 난이도이며 각 구간 safe:unsafe=1:1입니다. Task2는 관측 정답률 Easy>=0.8, Mid>0.4 및 <0.8, Hard>0 및 <=0.4이고 최소5/6 유효 모델을 요구했습니다. 모두 오답인 사례, 일부 메타데이터 차이·경계·품질 검토 후보는 선정에서 제외했습니다. 주제·심각도·명시성·발화 유형의 편중을 줄였지만 모든 조합의 동일 빈도나 일반적 난이도를 보장하지 않습니다.

과업·난이도별 문항 수는 위 표와 같습니다. 기존 전체 모델 표는 선정 모델 패널과 구분하며 관측·미실험·실패를 분리합니다. 모델 선정에 사용한 결과에 기반한 자료이므로 독립적인 숨은 테스트나 공식 순위로 해석하지 않습니다.

## 사용

```python
from datasets import load_dataset
ds = load_dataset("KETI-NLP/KoEVD-Compact", "task1", split="hard", revision="v1.0.2")
print(len(ds))  # 100
```

실제 입력은 모델 입력 전용 JSONL에서 준비합니다. Viewer 레코드의 reference_answer·level·라벨·선정 근거를 모델에 보내지 않습니다. [USAGE_KO.md](USAGE_KO.md)에 다운로드·설치·과업/난이도 선택·실행·채점을 설명했습니다. **입력 준비와 채점에 같은 --level을 지정**해야 선택한 서브셋의 분모로 점수를 얻습니다. 전체용 채점기에 일부 결과만 넣으면 나머지가 누락으로 계산됩니다.

Task5는 실제 도구를 실행하지 않습니다. tool_forced 지시와 참조 행동의 충돌 가능성 때문에 대표 순위 점수는 null이며 진단값으로만 봅니다. 모든 과업의 공식 순위 적격 플래그는 false입니다.

## 출처·조건

원자료: KETI-NLP/KoEVD, commit `192a2972f4e7830163fc57c62161d53ccb4c2a92`. 선정 버전 `saltlux-compact-20261013.1`, 배포 버전 `v1.0.2`. 원본 [KoEVD 이용 조건](LICENSE.md)을 변경 없이 유지하며 소프트웨어는 [Apache-2.0](CODE_APACHE_2.0.txt)으로 구분합니다. 유해·차별적·민감한 예시를 평가 목적으로 포함합니다. 유해 행위 실행, 개인정보 추적, 모델 안전성의 과장된 인증에 사용하지 않습니다. 별도 사진100 자료는 포함하지 않습니다.

MODEL_PERFORMANCE_BY_DIFFICULTY.csv는 기존 텍스트 및 KMME reference76 집계의 원형을 보존합니다. KMME 행은 이 텍스트 저장소의 입력 문항이 아니므로 과업을 필터링해 읽으십시오. KMME 이미지는 [별도 저장소](https://huggingface.co/datasets/KETI-NLP/KMME)를 이용합니다. 새 모델 추론은 실행하지 않았습니다.

문의: kimsan0622@keti.re.kr. 인용에는 KoEVD 원논문/저장소, 파생 서브셋명, commit, 과업과 난이도 선택을 함께 기록하십시오.

## 안내 개정 이력

`v1.0.2`은 설치·작업 폴더·5문항 연결 확인·전체 실행·오류 해결 안내와 `check_run.py`를 보완한 버전입니다. `v1.0.0`의 문항·정답·이미지·난이도·성능표·채점 방식은 변경하지 않았습니다. `MANIFEST.json`의 최초 데이터 배포 버전은 보존합니다.
