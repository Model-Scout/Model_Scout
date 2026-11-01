---
license: cc-by-sa-4.0
language:
- ko
task_categories:
- question-answering
- text-retrieval
pretty_name: RAG QA (Korean Wikipedia)
configs:
- config_name: dataset
  default: true
  data_files:
  - split: test
    path: dataset.jsonl
- config_name: corpus
  data_files:
  - split: corpus
    path: corpus.jsonl
---

# Surromind/rag-qa-benchmark-ko

한국어 위키백과에서 생성한 **RAG 검색·생성 동시 평가용** 벤치마크입니다.
검색 품질(hit@k)과 생성 품질(f1·BERTScore)을 같은 데이터로 잽니다.

## 구성

| 파일 | 행 수 | 용도 |
|---|---:|---|
| `dataset.jsonl` | 1000 | 질문·정답·정답 청크 id |
| `corpus.jsonl` | 1370 | 검색 후보 청크 풀 (KB 적재용) |

QA 를 가진 청크는 1000개이고, 나머지는 오답 후보(distractor)로 남습니다 —
검색 난이도를 유지하려면 corpus 를 통째로 적재해야 합니다.

### `dataset.jsonl`

```json
{"question": "금성의 표면 온도는 섭씨 몇도 이상인가?", "answer": "400도 이상", "expected_chunk_ids": ["<chunk_id>"]}
```

| 필드 | 설명 |
|---|---|
| `question` | 질문. 대상을 특정하는 고유명사를 포함해 단독으로 읽힙니다 |
| `answer` | 단답형 정답(명사구, 20자 이내). 객관식은 번호 없이 정답 내용만 |
| `expected_chunk_ids` | 정답 근거 청크의 `chunk_id` 목록 |

### `corpus.jsonl`

```json
{"chunk_id": "<uuid>", "chunk_text": "= 태양계 =\n== 태양 ==\n...", "source_file": "태양계.txt", "chunk_index": 12}
```

`chunk_text` 앞부분에는 문서·섹션 제목 계보(`= 문서 =` / `== 섹션 ==`)가 붙어 있습니다.

## 사용법

```python
from datasets import load_dataset

qa     = load_dataset("Surromind/rag-qa-benchmark-ko", "dataset", split="test")
corpus = load_dataset("Surromind/rag-qa-benchmark-ko", "corpus", split="corpus")
```

corpus 는 KB 에 그대로 적재해야 하는 경우가 많아 **원본 파일**로도 받을 수 있습니다.
config 선언과 무관하게 `corpus.jsonl` 은 레포 루트에 그대로 있습니다.

```python
from huggingface_hub import hf_hub_download

path = hf_hub_download("Surromind/rag-qa-benchmark-ko", filename="corpus.jsonl", repo_type="dataset")
```

## 문서별 청크 수

| 원본 문서 | 청크 |
|---|---:|
| 마야 문명.txt | 194 |
| 배드민턴.txt | 72 |
| 범고래.txt | 157 |
| 비행기.txt | 21 |
| 스마트폰.txt | 251 |
| 열대 우림.txt | 76 |
| 영국.txt | 182 |
| 인공위성.txt | 62 |
| 인터라켄.txt | 43 |
| 지구.txt | 51 |
| 축구.txt | 123 |
| 태양계.txt | 138 |

## 생성 방법

1. 한국어 위키백과에서 문서 본문을 추출하고 각주·외부 링크 등 관례 섹션을 제거
2. 섹션 단위로 청킹하며 제목 계보를 각 청크 앞에 붙임
3. 청크마다 LLM 으로 QA 생성 (목록형·본문이 짧은 청크는 생성 대상에서 제외)
4. LLM 이 청크 본문과 대조해 문항을 심사 — 근거가 없거나 어긋나는 문항을 삭제·수정
5. 사람이 청크 본문과 대조해 전수 검수 — 정답이 여럿인 문항, 부정형, 동어반복,
   원문 오역, 문서 내 사실 충돌 등을 삭제하거나 수정

사용한 모델 — 생성 `gpt-oss-120b` · 정제 `gpt-oss-120b`

대상 문서:

- 마야 문명
- 배드민턴
- 범고래
- 비행기
- 스마트폰
- 열대 우림
- 영국
- 인공위성
- 인터라켄
- 지구
- 축구
- 태양계

## 라이선스

본문이 한국어 위키백과에서 유래하므로 [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) 을 따릅니다.
출처: [한국어 위키백과](https://ko.wikipedia.org) (기여자 다수).

*생성일 2026-08-21*
