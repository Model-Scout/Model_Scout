---
license: mit
language:
- ko
tags:
- information-retrieval
- beir
- korean
- retrieval
- evaluation
- community-qa
size_categories:
- 10K<n<100K
task_categories:
- text-retrieval
configs:
- config_name: corpus
  data_files:
  - split: corpus
    path: corpus/corpus-*
- config_name: default
  data_files:
  - split: test
    path: data/test-*
- config_name: queries
  data_files:
  - split: queries
    path: queries/queries-*
dataset_info:
- config_name: corpus
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  - name: title
    dtype: string
  splits:
  - name: corpus
    num_bytes: 902704545
    num_examples: 50222
  download_size: 521965901
  dataset_size: 902704545
- config_name: default
  features:
  - name: query-id
    dtype: string
  - name: corpus-id
    dtype: string
  - name: score
    dtype: int64
  splits:
  - name: test
    num_bytes: 312972
    num_examples: 6289
  download_size: 134823
  dataset_size: 312972
- config_name: queries
  features:
  - name: _id
    dtype: string
  - name: text
    dtype: string
  splits:
  - name: queries
    num_bytes: 262600
    num_examples: 1454
  download_size: 159651
  dataset_size: 262600
---

# KommunityRetrieval Korean BEIR Dataset

한국어 커뮤니티 스타일 질의 검색을 위한 BEIR 형식의 평가 데이터셋입니다.

## 데이터셋 개요

이 데이터셋은 한국어 정보 검색 모델의 성능을 평가하기 위해 구축된 BEIR 형식의 벤치마크 데이터셋입니다. 나무위키 문서를 기반으로 하여 다양한 스타일의 질의와 관련 문서 쌍을 포함하고 있습니다.

## 데이터셋 특징

- **문서 소스**: 나무위키
- **문서 전처리**: 최소화된 전처리로 인해 매우 긴 문서 길이
- **질의 유형**: 3가지 스타일을 포괄
  - 키워드 스타일: "보스턴 레드삭스 밤비노 저주"
  - 의문문 스타일: "한세주와 만나면 회중시계가 어떻게 변하나요?"
  - 커뮤니티 질의 스타일: "애들아 도사의 무녀에서 히요리가 유카리 구하려고 엄청난 희생까지 한 거 같은데 주인공으로서 무슨 역할이었는지 진짜 가물가물함ㅠㅠ 알려주라!"

## 데이터셋 구축 방법

1. **문서 샘플링**: 나무위키 코퍼스에서 어휘 빈도와 문서 밀집도 등을 고려하여 일부 문서 샘플링
2. **질의 생성**: Qwen3 모델을 사용하여 샘플링된 문서에 대한 질의 생성
3. **관련 문서 검색**: 생성된 질의와 관련된 문서를 검색하여 top-k 후보 수집
4. **품질 검증**: LLM judge를 통해 각 질의-문서 쌍의 answerable 여부를 판단하고 필터링

## 데이터셋 통계

### 기본 통계

| 항목 | 개수 |
|------|------|
| **총 질의 수** | 1,454개 |
| **총 문서 수** | 50,222개 |
| **총 질의-문서 쌍** | 6,289개 |
| **평균 문서/질의** | 4.33개 |

### 질의별 관련 문서 분포

| 관련 문서 수 | 질의 개수 | 비율 |
|-------------|-----------|------|
| 1개 | 302 | 20.77% |
| 2개 | 342 | 23.52% |
| 3개 | 189 | 13.00% |
| 4개 | 130 | 8.94% |
| 5개 | 104 | 7.15% |
| 6개 | 82 | 5.64% |
| 7개 | 63 | 4.33% |
| 8개 | 51 | 3.51% |
| 9개 | 40 | 2.75% |
| 10개 | 27 | 1.86% |
| 11-19개 | 188 | 12.93% |

### 파일별 통계

| 파일명 | 레코드 수 | 크기 | 설명 |
|--------|-----------|------|------|
| `queries.jsonl` | 1,454 | 0.27 MB | 질의 데이터 |
| `corpus.jsonl` | 50,222 | 863.18 MB | 문서 데이터 (실제 text 포함) |
| `qrels.jsonl` | 6,289 | 0.48 MB | 질의-문서 관련성 데이터 |
| `qrels.tsv` | 6,289 | 0.23 MB | TSV 형식의 관련성 데이터 |

## 데이터 구조

### queries.jsonl
```json
{"_id": "query_000001", "text": "질의 내용"}
```

### corpus.jsonl
```json
{"_id": "문서_ID", "text": "문서 내용", "title": "문서 제목"}
```

### qrels.jsonl / qrels.tsv
```json
{"query_id": "query_000001", "doc_id": "문서_ID", "relevance": 1}
```

## 사용법

### Hugging Face Datasets 사용

```python
from datasets import load_dataset

# 전체 데이터셋 로드
dataset = load_dataset("junyoungson/KomuRetrieval")

# 각 구성 요소별로 로드
queries = load_dataset("junyoungson/KomuRetrieval", "queries", split="queries")
corpus = load_dataset("junyoungson/KomuRetrieval", "corpus", split="corpus")
qrels = load_dataset("junyoungson/KomuRetrieval", split="test")

print(f"Queries: {len(queries)}")
print(f"Corpus: {len(corpus)}")
print(f"Qrels: {len(qrels)}")
```

## 라이선스

이 데이터셋은 MIT 라이선스 하에 배포됩니다.

```
MIT License

Copyright (c) 2024 KommunityRetrieval

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 인용

이 데이터셋을 사용하시는 경우, 다음과 같이 인용해 주세요:

```bibtex
@dataset{kommunity_retrieval_2024,
  title={KommunityRetrieval: Korean Community-style Query Retrieval Benchmark},
  author={Junyoung Son, Youngjoon Jang, Taemin Lee, SeongTae Hong},
  year={2024},
  url={https://huggingface.co/datasets/junyoungson/KomuRetrieval},
  license={MIT}
}
```

## 기여

이 데이터셋에 대한 피드백이나 개선 제안이 있으시면 이슈를 생성해 주세요.

## 관련 링크

- [Hugging Face Dataset](https://huggingface.co/datasets/junyoungson/KomuRetrieval)
- [BEIR Framework](https://github.com/beir-cellar/beir)
- [나무위키](https://namu.wiki/)