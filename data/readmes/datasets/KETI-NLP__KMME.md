---
language:
- ko
license: other
license_name: kmme-research-and-evaluation-use-terms-v1
license_link: LICENSE.md
task_categories:
- visual-question-answering
size_categories:
- n<1K
tags:
- image
- text
- korean
- ethics
- safety-evaluation
- synthetic
- multiple-choice
configs:
- config_name: full168
  data_files:
  - split: test
    path: viewer/full168/test.parquet
  default: true
- config_name: reference76
  data_files:
  - split: test
    path: viewer/reference76/test.parquet
---

# KMME: Korean Multimodal Evidence-grounded Evaluation

KMME evaluates whether a model limits its description and inferences to visual evidence, including whose record or statement it is, consent, roles, time and source. It is not a universal ethical-ability score. This public distribution preserves the full frozen **168 items / 42 four-image families**, with 28 items per category, and a separately identified **reference76** subset for historical comparison.

## 구성과 선택

| 구성 | 규모 | 용도 |
|---|---:|---|
| `full168` / `test` (기본) | 168문항·42묶음 | 전체 고정본 평가 |
| `reference76` / `test` | 76문항·19묶음 | 기존 솔트룩스 전달 후보·기존 성능표와 비교 |

두 구성은 겹칩니다. 76문항은 전체168의 부분집합이며 244개의 독립 문항이 아닙니다. KMME는 난이도별 공개 셋으로 나누지 않았습니다. 별도 KoEVD 텍스트 난이도별 자료는 [KoEVD-Compact](https://huggingface.co/datasets/KETI-NLP/KoEVD-Compact)에서 제공합니다.

같은 묶음의 질문·선택지는 같고 이미지 근거가 변하며 정답 A/B/C/D가 한 번씩 배치됩니다. 각 문항은 독립 호출하고 다른 변형을 함께 보여주지 않습니다. 정답·유형·해설은 모델 입력에서 제외합니다.

## 실행

다운로드·설치·전체 명령은 [USAGE_KO.md](USAGE_KO.md)를 참조합니다. 공개 버전은 `v1.0.2`, 원자료 버전은 `4.4.5-frozen.1`입니다.

```python
from datasets import load_dataset
ds = load_dataset("KETI-NLP/KMME", "full168", split="test", revision="v1.0.2")
print(len(ds))  # 168
```

전체 레코드에는 정답이 있습니다. 이를 통째로 프롬프트로 보내지 마십시오. 제공 변환기는 이미지·질문·선택지만 사용합니다. 결과는 문항 정답률과 네 변형을 모두 맞힌 묶음의 비율 F4를 함께 봅니다. 누락·API 실패·파싱 실패는 전체 분모에서 제외하지 않습니다.

## 기존 성능과 검토 한계

`reference76/`의 기존 표는 이미지 조건 9개·이미지 제외 조건 10개 모델의 **76문항 결과**입니다. 이를 full168 성능으로 인용하지 마십시오. 기존 난이도 정보도 이 선정 자료에 대한 관측값이며 새 모델을 대상으로 재선별한 결과가 아닙니다. 전체168에는 개발 과정의 검토 우려로 별도 분석에서 제외됐던 문항도 포함합니다. 보편적 합의 정답이나 신규 독립 인간 검증을 보증하지 않습니다. reference76은 기존에 자료를 접한 두 연구원의 일치와 문제 신고 여부를 고려해 선정한 자료입니다. 공식 순위 적격 인증은 없습니다.

## 이미지 출처와 이용 조건

생성·편집 이미지와 프로그램 렌더링을 사용한 가상 장면입니다. 실제 인물·사건을 촬영한 사진 벤치마크로 설명하지 않습니다. 확인된 생성 로그에는 OpenRouter의 `openai/gpt-image-2`, 내장 이미지 도구, PIL 조합이 있고 모든 편집의 실제 모델 ID가 반환된 것은 아닙니다. 특히 KR43-MIS-02 후속 합성 네 장의 최종 파일은 식별되었지만 세부 생성 영수증은 불완전합니다. 이 한계는 남긴 채 버전을 고정하며 권리의 법적 확실성을 인증하지 않습니다.

양재희 연구원이 별도로 수집한 Unsplash94/Pexels6 사진100 데이터는 이 저장소에 포함하지 않습니다. 파일과 이미지 해시는 최종 동결본에 대조했습니다. 사람별 검토 응답·세션·DB·내부 비용·API 원문은 배포하지 않습니다.

[LICENSE.md](LICENSE.md)는 기업을 포함한 연구·교육·평가와 평가 플랫폼 연동을 허용하고, 학습·튜닝·재판매·데이터 자체의 제품 편입은 별도 협의하도록 정합니다. 보유하지 않은 제3자 권리까지 새로 부여하는 조건은 아닙니다. 소프트웨어는 [Apache-2.0](CODE_APACHE_2.0.txt)으로 구분합니다. 유해·차별적 오답 문구를 연구자의 견해나 실제 인물에 대한 주장으로 해석하지 않습니다.

인용: KMME, KETI-NLP, 4.4.5-frozen.1, 사용 구성과 실제 release commit을 기록하십시오. 확정되지 않은 논문·DOI는 넣지 않았습니다. 문의·오류·권리 문제: kimsan0622@keti.re.kr.

## 안내 개정 이력

`v1.0.2`은 설치·작업 폴더·5문항 연결 확인·전체 실행·오류 해결 안내와 `check_run.py`를 보완한 버전입니다. `v1.0.0`의 문항·정답·이미지·난이도·성능표·채점 방식은 변경하지 않았습니다. `MANIFEST.json`의 최초 데이터 배포 버전은 보존합니다.
