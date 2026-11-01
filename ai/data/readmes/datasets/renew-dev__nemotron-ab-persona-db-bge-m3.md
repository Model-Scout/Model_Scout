---
language:
  - ko
license: cc-by-4.0
size_categories:
  - 100K<n<1M
task_categories:
  - sentence-similarity
  - feature-extraction
tags:
  - persona
  - vector-database
  - chromadb
  - bge-m3
  - korean
  - marketing
  - nemotron
pretty_name: Nemotron-AB Persona VectorDB (bge-m3, 19~59세)
viewer: false
source_datasets:
  - nvidia/Nemotron-Personas-Korea
---

# Nemotron-AB Persona VectorDB (BAAI/bge-m3, 19~59세)

> **Pre-built Chroma vector DB of 669,558 Korean personas (NVIDIA `Nemotron-Personas-Korea`, ages 19–59) embedded with `BAAI/bge-m3` (1024-d, fp16, `max_seq_length=512`). Ready-to-query for Korean A/B persona simulation.**

NVIDIA [`Nemotron-Personas-Korea`](https://huggingface.co/datasets/nvidia/Nemotron-Personas-Korea) 데이터셋에서
**19~59세 한국인 페르소나 669,558건**을 [`BAAI/bge-m3`](https://huggingface.co/BAAI/bge-m3) 로 임베딩해
**[Chroma](https://github.com/chroma-core/chroma) PersistentClient** 디스크 포맷으로 묶어 둔
사전 빌드 벡터 데이터베이스입니다.

마케팅·UI 카피·공지 등 한국어 단문/이미지 A/B 변형을 합성 페르소나에 노출시켜
LLM 으로 시뮬레이션 평가하는 [`nemotron-ab`](https://github.com/renew-dev/nemotron-mini) 프로젝트에서
즉시 검색에 사용할 수 있도록 만들어졌습니다.

> **`persona_db` 디렉터리 자체를 다운로드해서 그대로 사용**합니다. 일반 `datasets` 라이브러리로 로드하는 형식이 아닙니다.

## 무엇이 들어 있나

- 컬렉션: `marketing_personas`
- 행(row) 수: **669,558**
- 메타데이터 필드: `uuid`, `age`, `age_bucket`(`20s`/`30s`/`40s`/`50s`, 19세는 20s), `sex`, `occupation`,
  `province`, `district`, `marital_status`, `education_level`, `family_type`, `housing_type`, `military_status`
- 문서(`documents`) 본문: `age | sex | marital_status | education_level | family_type | housing_type |
  military_status | occupation | province | district | persona | professional_persona |
  hobbies_and_interests | career_goals_and_ambitions` 를 ` | ` 로 연결한 한국어 문자열

상세한 임베딩 텍스트 구성 순서·해시·파일 크기는 [`manifest.json`](./manifest.json) 을 참고하세요.

## 임베딩 사양

| 항목 | 값 |
|---|---|
| 모델 | `BAAI/bge-m3` (MIT) |
| 차원 | **1024** |
| 정규화 | `normalize_embeddings=True` (cosine ≡ inner product) |
| 토크나이저 `max_seq_length` | **512** (데이터 max 토큰 507 / p99 462) |
| 인퍼런스 정밀도 | FP16 (CUDA) |
| Chroma distance | `l2` (정규화 임베딩이라 `≈ 2·(1−cos)`) |

> **검색 시 동일 모델·동일 정규화·동일 텍스트 스키마를 써야 의미가 보존됩니다.**
> 다른 모델로 만든 쿼리 임베딩을 섞어 쓰면 안 됩니다.

## 다운로드

총 용량 약 **11.2 GB** (HNSW 인덱스 포함). HF Hub LFS 가 자동 처리합니다.

### 방법 A — `hf` CLI (권장)

```bash
hf download renew-dev/nemotron-ab-persona-db-bge-m3 \
  --repo-type dataset \
  --local-dir ./persona_db
```

### 방법 B — Python (`huggingface_hub`)

```python
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="renew-dev/nemotron-ab-persona-db-bge-m3",
    repo_type="dataset",
    local_dir="./persona_db",
)
```

## 무결성 검증

`manifest.json` 에 모든 파일의 SHA-256 이 포함되어 있습니다.

```bash
cd persona_db
python - <<'PY'
import hashlib, json
m = json.load(open("manifest.json"))
for rel, expected in m["sha256"].items():
    h = hashlib.sha256(open(rel, "rb").read()).hexdigest()
    print(rel, "OK" if h == expected else f"MISMATCH (got {h[:16]}…)")
PY
```

## 사용 예시 (Chroma 직접)

```python
import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="./persona_db")
col = client.get_collection("marketing_personas")

model = SentenceTransformer("BAAI/bge-m3", device="cuda")
model.max_seq_length = 512
model.half()  # CUDA에서만

q = "30대 워킹맘, 자녀 교육과 가족 여행"
qe = model.encode([q], normalize_embeddings=True, convert_to_numpy=True)[0].tolist()

res = col.query(
    query_embeddings=[qe],
    n_results=5,
    where={"$and": [
        {"age_bucket": {"$eq": "30s"}},
        {"sex": {"$eq": "여자"}},
    ]},
    include=["metadatas", "documents", "distances"],
)
for m, d, dist in zip(res["metadatas"][0], res["documents"][0], res["distances"][0]):
    print(f"dist={dist:.4f}  {m['age']}세 {m['sex']} {m['occupation']} {m['province']}/{m['district']}")
    print(f"  {d[:120]}…")
```

## 라이선스 / Attribution

- **본 데이터셋 산출물(VectorDB)**: **CC-BY-4.0** (원본 `Nemotron-Personas-Korea` 와 동일 — 코드 라이선스와 별개)
- **빌드 도구 소스** ([nemotron-ab](https://github.com/renew-dev/nemotron-mini)): **Apache-2.0**
- 원본 데이터셋: **`nvidia/Nemotron-Personas-Korea`** ([CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/))
- 임베딩 모델: [`BAAI/bge-m3`](https://huggingface.co/BAAI/bge-m3) (MIT, 가중치 자체는 본 리포에 포함되지 않음)

### 사용 시 표기 의무

CC-BY-4.0 의무에 따라 사용처(논문·블로그·서비스·리포 등)에서 다음 두 가지를 명시해 주세요.

1. 원본 출처: **NVIDIA `Nemotron-Personas-Korea` (CC-BY-4.0)**
2. 변경 사실: "19~59세 필터링 + `BAAI/bge-m3` 1024차원 임베딩 + Chroma 인덱스화" 를 포함한 파생물임

## 변경/가공 내역

원본 대비 다음 가공이 적용되었습니다.

- `19 ≤ age ≤ 59` 필터 (해당 외 레코드 제외)
- 메타데이터 14개 필드만 추출하여 Chroma 메타데이터로 저장
- `age_bucket` 파생 필드(`20s`/`30s`/`40s`/`50s`, 19세는 20s) 추가
- 위 텍스트 스키마(`v1`)로 `documents` 생성 후 임베딩

## 빌드 재현

[`nemotron-ab` 리포의 `scripts/build_vectordb.py`](https://github.com/renew-dev/nemotron-mini/blob/main/scripts/build_vectordb.py)
로 동일하게 빌드할 수 있습니다.

```bash
python scripts/build_vectordb.py --device cuda
# 기본값: --max-seq-length 512 --encode-batch-size 128 --fp16 auto
```

TITAN RTX 24GB 기준 약 100~150 rows/s, 전체 약 90~120 분 소요됩니다.

## 한계 / 주의

- 합성 데이터 기반이므로 개인정보(PII) 는 포함하지 않으나, **실제 한국 인구 분포와 동일하다고 보장하지 않습니다.**
- `documents` 필드는 검색용으로 만든 단일 문자열이며, 원본 데이터셋의 모든 페르소나 서브 카테고리
  (`sports_persona`, `arts_persona` 등) 가 다 들어 있는 건 아닙니다.
- Chroma 가 사용하는 디스크 포맷에 의존하므로, Chroma 버전 호환성을 깬 업그레이드가 있을 경우
  재빌드가 필요할 수 있습니다.

## 인용

```bibtex
@misc{nemotron_ab_persona_db_bge_m3,
  title  = {Nemotron-AB Persona VectorDB (bge-m3, 19~59)},
  author = {renew-dev},
  year   = {2026},
  howpublished = {\url{https://huggingface.co/datasets/renew-dev/nemotron-ab-persona-db-bge-m3}},
  note   = {Built from NVIDIA Nemotron-Personas-Korea (CC-BY-4.0) with BAAI/bge-m3 embeddings.}
}
```
