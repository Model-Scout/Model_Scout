---
language:
- ko
license: other
license_name: all-rights-reserved
pretty_name: Korean RAG PII Span Classification SFT
task_categories:
- text-classification
size_categories:
- 10K<n<100K
tags:
- synthetic
- pii
- sft
- conversational
- rag
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train.clean.jsonl
  - split: validation
    path: data/valid.clean.jsonl
  - split: test
    path: data/test.clean.jsonl
---

# Korean RAG PII Span Classification SFT

한국어 문서 기반 RAG 응답에서 지정된 `candidate` span이 특정 자연인에게
연결되는 정보인지 `PII` 또는 `NOT_PII`로 분류하도록 만든 지도 미세조정
(SFT) 데이터셋입니다. 각 레코드는 Qwen 계열 채팅 형식의 `system`, `user`,
`assistant` 메시지 세 개로 구성됩니다.

이 저장소는 `bbanany/final-mode` 모델의 미세조정과 평가에 실제 사용한
토크나이징 직전 JSONL 분할을 보존합니다.

## Dataset structure

| Split | File | Rows | Use |
|---|---|---:|---|
| train | `data/train.clean.jsonl` | 15,875 | QLoRA training |
| validation | `data/valid.clean.jsonl` | 1,984 | Training-time evaluation and checkpoint selection |
| test | `data/test.clean.jsonl` | 1,983 | Final held-out evaluation |
| **Total** |  | **19,842** |  |

각 JSONL 레코드의 최상위 필드는 `messages` 하나입니다.

```json
{
  "messages": [
    {"role": "system", "content": "...분류 지침..."},
    {
      "role": "user",
      "content": "{\"answer\":\"...\",\"candidate\":{\"text\":\"김민수\",\"tag\":\"NAME\",\"start\":13,\"end\":16}}"
    },
    {"role": "assistant", "content": "PII"}
  ]
}
```

`user.content`는 JSON 문자열이며 다음 정보를 포함합니다.

- `answer`: 분류할 한국어 RAG 응답 문맥
- `candidate.text`: 판정 대상 문자열
- `candidate.tag`: 후보 개인정보 유형
- `candidate.start`, `candidate.end`: Python 문자열 슬라이스 기준 오프셋
- 불변 조건: `answer[start:end] == candidate.text`

정답은 마지막 assistant 메시지의 `PII` 또는 `NOT_PII`입니다.

## Preparation and integrity

프로젝트의 합성·템플릿 기반 한국어 업무 문맥 레코드 23,000건을 합친 뒤
레코드 전체가 완전히 같은 중복 3,158건을 제거했습니다. 이후
`(candidate.tag, label)`을 층화 기준으로 사용하여 seed `20260810`으로
80/10/10 재분할했습니다.

- 정리 후 고유 레코드: 19,842건
- train/validation/test 사이 완전 일치 중복: 각각 0건
- 후보 태그: 23종
- 전처리 및 검증 코드: `scripts/prepare_dataset.py`
- 상세 분포와 검증 결과: `dataset_report.json`
- 파일 무결성 값: `checksums.sha256`

원본의 `*.clean.jsonl` 내용을 수정하거나 Parquet으로 재직렬화하지 않고 실제
학습에 사용한 UTF-8 JSONL 바이트를 그대로 업로드했습니다.

## Loading

```python
from datasets import load_dataset

dataset = load_dataset("bbanany/final-mode-dataset")
print(dataset)
print(dataset["train"][0]["messages"])
```

## Training details

연결 모델은 `Qwen/Qwen2.5-3B-Instruct`를 기반으로 했습니다. 학습 시 각
`messages` 레코드에 모델 토크나이저의 chat template을 적용했으며, system과
user 토큰은 loss에서 제외하고 마지막 assistant 라벨 토큰만 학습했습니다.
최대 길이는 512 토큰이었고 학습 및 validation 레코드의 truncation은
0건이었습니다.

## Intended use

- 한국어 RAG 응답에 포함된 candidate span의 PII 문맥 분류 연구
- PII/NOT_PII 이진 분류 모델의 지도 미세조정 및 평가
- 문맥에 따라 같은 형태의 문자열을 자연인 정보와 비인적 값으로 구분하는 연구

## Limitations and safety

- 데이터는 합성·업무 문맥 중심이며 실제 운영 문서의 분포를 대표하지 않습니다.
- 합성을 의도한 이름, 연락처, 주소 및 식별자 형태의 값이 포함됩니다. 우연히
  실제 인물이나 실제 식별자와 일치할 가능성을 완전히 배제할 수 없습니다.
- 의미상 유사한 합성 문장이 분할 사이에 존재할 수 있습니다.
- 클래스는 `PII`와 `NOT_PII` 두 개뿐이며 새로운 태그와 언어 변형에는 별도
  검증이 필요합니다.
- 이 데이터셋이나 이를 학습한 모델은 개인정보 처리 여부를 확정하는 법률 판단
  도구가 아닙니다.

## License and access

현재 저장소에는 공개 재사용 라이선스를 부여하지 않았습니다. 원천 템플릿의
재배포 권리와 합성 식별자의 공개 안전성 검토가 끝날 때까지 저장소를 private로
유지하는 것을 권장합니다. 별도 서면 허가 없이 재배포하거나 상업적으로 사용하지
마십시오. 자세한 내용은 `LICENSE`를 확인하세요.

