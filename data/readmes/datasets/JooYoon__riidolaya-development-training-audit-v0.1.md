---
license: apache-2.0
language:
- ko
- en
tags:
- riidolaya
- diagnostics
- synthetic
- ai-references
- golang
---
# riidolaya 개발 주장: 학습 자료 점검 v0.1

[English](README.en.md) · [개발 기록](https://github.com/teamswyg/laya-tools/issues/155) · [Go 원본 코드](https://github.com/teamswyg/laya-tools/tree/45c01ab5ddf04902cd85fb03fc6751071d14fd12/cmd/riido-statehint-claims-training-audit)

이 저장소는 **기존 공개 학습 자료에 대한 집계 진단 기록**입니다. 다음 튜닝 전에 자료의 분포와 AI 참조 판정의 일관성을 확인하려고 만들었습니다. 새로운 학습 말뭉치·모델·사람 정답셋이 아니며, 모델 추론이나 실제 앱 표시의 품질을 평가한 자료도 아닙니다.

## 확인한 내용

원본은 1,680행·840한국어/영어쌍·280관련 그룹입니다. 각 언어 840행에서 true / false / unknown 수는 다음과 같습니다. false는 긍정 주장의 부재이며 작업 미완료라는 뜻이 아닙니다.

| 주장 | 한국어 | 영어 |
| --- | --- | --- |
| 응답 요청 | 206 / 544 / 90 | 205 / 545 / 90 |
| 현재 진행 보고 | 284 / 499 / 57 | 284 / 499 / 57 |
| 완료 보고 | 318 / 456 / 66 | 316 / 458 / 66 |

진행·완료의 unknown은 약 6.8%·7.9%입니다. Unicode 코드 포인트 16개 이하는 0행이며 17–32개는 한국어 24행·영어 0행입니다. 이는 학습 분포와 입력 길이 관측입니다. 실제 업무 분포, 의미 난이도, 모델 토큰 수 또는 앞선 모델 실패 원인으로 확대 해석하지 않습니다. 소문자·공백 정규화 후 정확한 중복/라벨 충돌은 0건이지만 의미 중복과 그룹 독립성은 미확인입니다.

라벨·모델 점수·오류를 사용하지 않은 고정 그룹 해시 순서로 40그룹·240행을 골랐습니다. 새 AI 역할이 원판정을 보지 않고 모든 첫 판정을 봉인한 뒤 비교했습니다. 720항목 중 716개(99.44%), 세 항목 전체가 같은 행은 236/240(98.33%)였습니다. 2언어쌍·2그룹의 4항목 이견은 원판정과 재판정 모두 보존하며 아직 결론내리지 않았습니다. 원본 라벨은 바꾸지 않았습니다.

이는 **AI 참조 일관성**입니다. 같은 문장 틀과 상관된 AI 판단이 남으며 전체 1,680행을 의미 검토한 결과도 아닙니다. 원래 근거 구간·설명은 비교 export에 없어서 목표 값만 비교했습니다. 모델 정확도·사람 정답·실사용 합격·공개 자료 품질 인증을 뜻하지 않습니다.

## 파일과 사용법

- [training.aggregate.json](training.aggregate.json): 전체 학습 분포·길이·근거 구간·정확한 중복 집계.
- [reference-consistency.aggregate.json](reference-consistency.aggregate.json): 독립 AI 재판정과 원판정의 집계 비교 및 한계.
- [resources.aggregate.json](resources.aggregate.json): Go 점검 프로세스 1회 자원 관측.
- [provenance.json](provenance.json), [manifest.json](manifest.json): 출처와 SHA-256/바이트 수. manifest는 자기 자신을 해시하지 않습니다.

원본 학습 자료는 [별도 불변 HF 버전](https://huggingface.co/JooYoon/riidolaya-development-claim-hints-mlp16-v0.1/tree/31705b576851edba30f10c0e26fd22793ffc6f56)에 그대로 두고 여기에는 복제하지 않습니다. 원본 SHA-256: `c5b5a0adbc721d73213d4565c6a7c430094f31b8e7502fb5249e7ed40a3da837`. JSON 집계만 다운로드해 읽거나, [고정 소스](https://github.com/teamswyg/laya-tools/tree/45c01ab5ddf04902cd85fb03fc6751071d14fd12/experiments/state-hints-training-audit)의 재현 스크립트를 저장소 루트에서 실행할 수 있습니다.

```sh
bash scripts/verify-claims-training-audit.sh
```

Go 1.27.1 도구는 고정된 자체 공개 학습 SHA만 허용하고 배열 기반으로 집계합니다. 출력은 집계이며 모델 로드·추론·Fit·앱 변경 경로가 없습니다. CI의 공개 Go 집계 재현과 전체 소스 검사가 **두 운영체제에서 통과**했습니다([run](https://github.com/teamswyg/laya-tools/actions/runs/37587560067)). CI 통과가 확인되더라도 제품 효용의 증거는 아닙니다.

Apple M4 Pro·24GiB·macOS 26.6.2에서 전체 점검 1회는 wall 0.61초/user CPU 0.04초/최대 RSS 13,205,504B였습니다. 읽기·해시·JSON 해석·집계·출력을 포함한 단일 관측이며 모델 추론 속도나 처리량 보증이 아닙니다. GPU/MPS는 사용하지 않았습니다.

이번 Fit 0회, 누적 연구 Fit 23회, 운영 합격 모델 없음, 앱 쓰기 0회·자동 적용 기본 OFF입니다. [표시 기준 제안](https://github.com/teamswyg/laya-tools/blob/45c01ab5ddf04902cd85fb03fc6751071d14fd12/experiments/state-hints-claims/PRODUCT-MARKING.ko.md)은 버전이 확인된 **댓글의 주장**을 대상으로 하며 전체 태스크 상태와 구분합니다. 사람 판정과 실제 유용성 검증은 남아 있습니다.

집계와 문서는 자체 제작 Apache-2.0입니다. 원문·행/업무 식별자·개별 AI 참조/점수·실제 업무 댓글·인증정보·모델 가중치·원시 프로파일은 이 저장소에 없습니다. `training-audit-v0.1`은 게시 시 고정할 예정인 태그이며, 게시와 원격 검증 기록은 별도로 issue155에 남깁니다.


봇 병합 `231b65013a4e64804adff48dd034525d0951f079`의 트리가 고정 학습 점검 소스와 같습니다. 원격 게시 revision·태그·바이트 검증은 별도 GitHub 기록에서 확인합니다.
