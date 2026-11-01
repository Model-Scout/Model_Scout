---
language:
- ko
license: cc-by-sa-4.0
task_categories:
- question-answering
tags:
- klue
- mrc
- sft
configs:
- config_name: default
  data_files:
  - split: train
    path: train.jsonl
  - split: validation
    path: validation.jsonl
---

# KLUE-MRC 전체 messages 데이터

KLUE-MRC의 원본 train 17,554행과 validation 5,841행을 `id`와
`messages`(system/user/assistant)로 변환한 수정본이다. 세 문제 유형과
원본 순서·ID·지문·질문을 모두 유지했으며 필터링하거나 자르지 않았다.

문맥과 질문을 주면 짧은 정답을 답하는 독해 학습용이다. 답 있는 문항은
첫 원본 정답을 assistant target으로 사용한다. 답 없는 문항은
`지문에서 답을 찾을 수 없습니다.`로 변환하며 그럴듯한 오답 후보를 쓰지 않는다.
평가할 때는 원본의 모든 허용 정답을 사용해야 한다.

원본 train과 validation에 같은 지문이 일부 존재한다. 원본 split을 그대로
공개하므로 미학습 문서 일반화 평가용 분리라고 해석하지 않는다.
validation은 평가 자료이며 학습에 섞지 않는다. 별도의 로컬 연구용
search/final 분리·모델·adapter·PDF·인증 정보는 이 저장소에 포함하지 않는다.
특정 학습 설정의 완료나 성능 개선을 보장하는 데이터셋이 아니다.

## 출처와 라이선스

- 원본: [klue/klue, mrc](https://huggingface.co/datasets/klue/klue/tree/349481ec73fff722f88e0453ca05c77a447d967c/mrc)
- 저자: Sungjoon Park et al., **KLUE: Korean Language Understanding Evaluation** (2021)
- [논문](https://arxiv.org/abs/2105.09680), [원본 인용 안내](https://huggingface.co/datasets/klue/klue#citation-information)
- 원본 및 이 변환본: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)
- 변경: 대화 형식으로 변환, 답 없음 target 추가, 답 있는 문항의 첫 정답 선택.
- revision·원본 parquet hash·변환 JSONL hash·행 수는 `source-manifest.json`에 기록했다.

```python
from datasets import load_dataset
data = load_dataset("YoungjaeDev/klue-mrc-messages")
print(data["train"][0]["messages"])
```
