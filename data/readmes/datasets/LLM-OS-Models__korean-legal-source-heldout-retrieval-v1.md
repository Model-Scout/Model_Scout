---
language:
- ko
license: other
task_categories:
- text-retrieval
pretty_name: Korean Legal Source-Document-Held-Out Retrieval v1
tags:
- legal
- retrieval
- korean
- mteb
---

# Korean Legal Source-Document-Held-Out Retrieval v1

한국 법령·행정규칙·판례·자치법규의 source-native 구조로 만든 10,000-query retrieval
holdout이다. 학습에 사용한 250K 법률 데이터와 같은 네 Legalize-KR repository를
사용하지만, 선택된 10,000개 `source_document_sha256`는 학습 provenance에 한 번도
등장하지 않는다.

## 독립성

- independence grade: `I` (same-repository, whole-source-document-held-out)
- grade `Z`/unseen-source는 아님
- training source candidate ID overlap: `0`
- training source document SHA-256 overlap: `0`
- Sionic 9 + official MTEB Korean v1 exact query overlap: `0`
- Sionic 9 + official MTEB Korean v1 exact positive/corpus overlap: `0`
- unique queries / positives / source documents: `10,000 / 10,000 / 10,000`

독립 verifier는 27개 benchmark hash file을 다시 스캔했으며 `verified: true`를 냈다.
manifest SHA-256은
`f475d358622598f2263d2f802c6028c3b0c0ec437458799a3f24dbb70d4aacdf`다.

## Source 분포

| Repository | Rows | Pinned revision |
|---|---:|---|
| `legalize-kr/admrule-kr` | 2,998 | `64a5a272909ab5bc077b0ad9519ef31de8febb46` |
| `legalize-kr/legalize-kr` | 1,006 | `db3cd760c14042ee04fd9166e1bdbb662fc999bc` |
| `legalize-kr/ordinance-kr` | 2,998 | `6443e5dd5833d863219064cd362111f516430bec` |
| `legalize-kr/precedent-kr` | 2,998 | `40cd00e54df19d98562abb170c8ff51fd6fe2c2e` |

## 파일

- `queries.jsonl`: `_id`, query `text`, source provenance metadata
- `corpus.jsonl`: `_id`, `title`, positive passage, source provenance metadata
- `qrels.jsonl`: `query-id`, `corpus-id`, relevance `score=1`
- `provenance.jsonl`: candidate/document/text hashes와 pinned source metadata
- `manifest.json`: 입력·출력 SHA, benchmark blocklist, exclusion/selection assertion

각 query는 source-native positive 하나만 qrel로 갖는다. 다른 corpus passage도 실제로
관련될 수 있으므로 qrel은 exhaustive human relevance judgment가 아니다. NDCG@10과
Recall@10을 이 한계와 함께 보고해야 한다.

## 재현

Builder, 독립 verifier, pinned configuration과 실행 문서는
https://github.com/LLM-OS-Models/Embedding 의
`scripts/build_legal_source_holdout.py`, `configs/legal_source_holdout_v1.json`,
`docs/24_LEGAL_SOURCE_HELDOUT_RETRIEVAL.md`에 있다.

원문의 이용 조건은 각 upstream Legalize-KR repository 선언을 따른다. 이 dataset card는
upstream content 권리를 재허가하지 않는다.
