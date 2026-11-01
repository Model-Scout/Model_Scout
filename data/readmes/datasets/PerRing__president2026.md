---
license: cc-by-4.0
language:
- ko
task_categories:
- question-answering
- text-generation
tags:
- knowledge-editing
- continual-pretraining
- synthetic
- korean
size_categories:
- 1K<n<10K
configs:
- config_name: qa
  default: true
  data_files:
  - split: train
    path: ko_qa.jsonl
- config_name: plain
  data_files:
  - split: train
    path: ko_plain.jsonl
---

# president2026

outdated된 지식을 가진 소형 언어모델에게 **2026년 9월 기준 대한민국·미국 대통령**을 가르치기 위한
한국어 합성 학습 데이터셋입니다.

`google/gemma-3-1b-it` 같은 모델은 학습 시점이 지나 "대한민국 대통령은?"에 윤석열,
"미국 대통령은?"에 조 바이든이라고 답합니다. 이 데이터셋은 그 지식을 덮어쓰기 위한 데이터셋입니다.

두 개의 config로 나뉩니다.

| config | 건수 | 형식 | 용도 |
|---|---:|---|---|
| `qa` | 906 | `messages` 대화 | SFT (답변 토큰에만 loss) |
| `plain` | 815 | 제목 + 본문 | 계속사전학습 CPT (전체 토큰에 loss) |

## 사용법

```python
from datasets import load_dataset

qa    = load_dataset("PerRing/president2026", "qa",    split="train")
plain = load_dataset("PerRing/president2026", "plain", split="train")

print(qa[0]["messages"])
# [{'role': 'user', 'content': '대한민국 대통령 이름 알려줘'},
#  {'role': 'assistant', 'content': '제21대 이재명 대통령입니다. 2025년 6월 4일에 취임했습니다.'}]

print(plain[0]["title"], plain[0]["text"])
```

config 이름을 생략하면 기본값인 `qa`가 로드됩니다.

특정 카테고리만 쓰려면 필터링합니다.

```python
correction = qa.filter(lambda r: r["meta"]["category"] == "correction")
news       = plain.filter(lambda r: r["meta"]["doctype"] == "straight_news")
```

### gemma-3 학습 포맷으로 변환

`qa`는 답변에만, `plain`은 전체 토큰에 loss를 거는 것이 의도된 사용법입니다.
TRL `SFTTrainer`는 `prompt`/`completion` 컬럼을 보면 `completion_only_loss`를 켜고
prompt 토큰을 마스킹하므로, **plain 행은 `prompt`를 빈 문자열로 두면** 마스킹될 토큰이
없어 그 행만 전체 토큰 학습이 됩니다.

```python
from transformers import AutoTokenizer
from datasets import concatenate_datasets

tok = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")

# TRL의 텍스트 경로는 토크나이즈할 때 <bos>를 자동으로 붙입니다.
# gemma 채팅 템플릿도 앞에 <bos>를 넣으므로, 떼지 않으면 '<bos><bos>'가 되어
# 학습과 추론의 분포가 어긋납니다.
def strip_bos(text):
    return text[len(tok.bos_token):] if text.startswith(tok.bos_token) else text

def render_qa(rec):
    m = rec["messages"]
    prompt = tok.apply_chat_template(m[:-1], tokenize=False, add_generation_prompt=True)
    full   = tok.apply_chat_template(m,      tokenize=False, add_generation_prompt=False)
    return {"prompt": strip_bos(prompt), "completion": full[len(prompt):]}

def render_plain(rec):
    doc = f"{rec['title']}\n\n{rec['text']}".strip()
    # prompt가 비어 마스킹될 토큰이 없으므로 전체 토큰에 loss가 걸립니다.
    # 끝의 <eos>는 TRL이 없으면 붙여주므로 직접 써도 중복되지 않습니다.
    return {"prompt": "", "completion": f"{doc}{tok.eos_token}"}

train = concatenate_datasets([
    qa.map(render_qa,       remove_columns=qa.column_names),
    plain.map(render_plain, remove_columns=plain.column_names),
])
```


## 스키마

**qa**

| 필드 | 설명 |
|---|---|
| `messages` | `role`(`system`/`user`/`assistant`) + `content`. 전부 단일턴이며, `system`은 날짜 앵커가 주어진 267건에만 있습니다 |
| `meta.category` | 아래 5종 |
| `meta.country` | `kr` / `us` / `both` |
| `meta.call_id` | 생성 시 teacher 호출 ID. **train/eval 분할은 이 단위로 하세요** (같은 호출 결과는 표현이 닮아 있어 무작위 분할 시 leakage가 생깁니다) |
| `meta.translated` | 영어로 생성된 뒤 한국어로 번역된 레코드 |
| `meta.flattened` | 멀티턴에서 단일턴으로 펼쳐진 레코드 |

| `category` | 건수 | 막으려는 실패 모드 |
|---|---:|---|
| `paraphrase` | 260 | 문자열 암기 — 표현이 바뀌면 옛 답으로 돌아감 |
| `correction` | 221 | 낡은 전제를 깐 유도 질문에 prior가 이김 |
| `derived` | 163 | 이름만 외우고 정당·취임일에서 무너짐 |
| `reversal` | 135 | reversal curse — 인물에서 직위를 못 찾음 |
| `time_anchor` | 127 | 시간 기준점이 과거에 고정됨 |

**plain**

| 필드 | 설명 |
|---|---|
| `title` | 문서 제목 |
| `text` | 문서 전문. 중앙값 464자, p95 837자 |
| `meta.doctype` | 아래 8종 |
| `meta.country` | `kr` 361 / `us` 454 |
| `meta.call_id`, `meta.translated` | qa와 동일 |

`doctype`: `analysis` 107, `timeline` 106, `qa_article` 105, `press_release` 105,
`encyclopedia` 105, `straight_news` 99, `editorial` 98, `english_news` 90.

같은 사실이 문체가 전혀 다른 문서에 반복 등장해야 표현에 독립적으로 박히기 때문에
문서 유형을 나눴습니다. 모든 문서에는 기준 시점 날짜가 최소 한 번 들어 있습니다.

