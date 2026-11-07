# HF 수집 경로 — 어떤 사실을 어디서, 어느 단계에서 가져오나

[`README.md`](README.md)가 "무엇을 가져야 하는가"를 정하고, 이 문서가
"어디서 가져오는가"를 정한다. 아래 표의 모든 경로는 `ai/backfill/raw/`에
받아 둔 실제 HF 응답 1,803건으로 확인했다.

---

## 1. HF가 한 번의 호출로 주는 것

```
GET https://huggingface.co/api/models/{model_id}?blobs=true
```

`blobs=true`가 핵심이다. 이걸 붙이면 `siblings`에 파일 크기가 들어온다.

실제 응답(GGUF 전용 레포):

```json
{
  "id": "SL-AI/GRaPE-2.5-Helios-GGUF",
  "author": "SL-AI",
  "sha": "9ea1a6e2c57fa63f9770fc096954d0f51feb2365",
  "lastModified": "2026-09-13T20:43:45.000Z",
  "gated": false,
  "private": false,
  "disabled": false,
  "downloads": 267,
  "likes": 2,
  "pipeline_tag": "image-text-to-text",
  "library_name": "transformers",
  "tags": ["transformers", "gguf", "qwen3.5", "..."],
  "cardData": { "license": "...", "language": [...], "base_model": [...], "tags": [...] },
  "config": { "architectures": [...], "model_type": "...", "tokenizer_config": {...} },
  "safetensors": { "total": 4022468096, "parameters": { "BF16": 4022468096 } },
  "gguf": { "total": 9197093888, "architecture": "qwen35", "context_length": 262144 },
  "siblings": [ { "rfilename": "model-Q4_K_M.gguf", "size": 4812451840, "blobId": "..." } ],
  "usedStorage": 46369040736,
  "model-index": null
}
```

### 이미 응답에 들어오는데 읽지 않던 것

| 키 | 보유율 (표본 1,817) | 지금 쓰는가 | 무엇을 해결하나 |
|---|---:|---|---|
| `gated` | 1,804 (99.3%) | **안 쓴다** | Q7 "내려받아 써도 되나"의 0% |
| `siblings[].size` | 1,804 (99.3%) | **안 쓴다** | 실제 파일 용량. Q2의 측정 근거 |
| `sha` | 전부 | **안 쓴다** | `identity.revision`. 재현 기준점 |
| `lastModified` | 전부 | **안 쓴다** | 신선도 |
| `usedStorage` | 1,796 | **쓰지 않는다** | 현재 스냅샷 크기가 아니다. 2절의 "쓰지 않는 이유" 참고 |
| `gguf.{total, architecture, context_length}` | 1,292 | **안 쓴다** | 파라미터·컨텍스트·아키텍처 누락 1,527/1,459/1,425개 |
| `safetensors.parameters` | 235 | 일부 | **dtype 맵이다.** `{"BF16": 4022468096}` |
| `config.architectures` / `config.model_type` | 568개 응답에 포함 | 파일을 따로 내려받는다 | 아래 주의 참고 |
| `model-index` | 87 / 1,817 | 안 쓴다 | 구조화된 벤치마크 점수 |

두 가지가 특히 중요하다.

1. **`gated`는 지금도 응답에 들어오고 있다.** 수집하지 않은 것뿐이다.
   Q7이 0%인 것은 데이터가 없어서가 아니다.
2. **`safetensors.parameters`는 dtype → 파라미터 수 맵이다.** safetensors 레포라면
   `config.json`을 내려받지 않고도 `technical.dtype`을 알 수 있다. 지금 `02`는
   `total`만 보고 있다.

### 주의 — `api.config`는 `config.json` 전체가 아니다

선별된 일부만 온다. 실측(응답 568건에 `config`가 있었다):

| `config`의 키 | 등장 |
|---|---:|
| `model_type` | 477 |
| `architectures` | 418 |
| `tokenizer_config` | 400 |
| `chat_template_jinja` | 113 |
| `auto_map` | 38 |
| `quantization_config` | 21 |
| `num_experts_per_tok` / `num_experts` | 각 6 |
| **`torch_dtype`** | **0** |
| **`max_position_embeddings`** | **0** |

따라서:

- `architectures`·`model_type`·`tokenizer_config`는 API로 충분하다.
- **`torch_dtype`과 `max_position_embeddings`는 `config.json`을 내려받아야 한다.**
  최상위에만 있는 것도 아니다 — 멀티모달 모델은 `text_config`·`language_config`·
  `decoder`·`llm_config` 하위에 둔다. `02_enrich_metadata.NESTED_CONFIG_KEYS`가
  이미 그 목록을 갖고 있다.
- MoE 전문가 수(`num_experts_per_tok`)는 API에 오는 경우가 있다. 활성 파라미터
  유도에 필요한 값이다.

---

## 2. 필드별 수집 경로

| 계약 필드 | 1차 출처 | 2차 (1차가 없을 때) | 단계 | 비고 |
|---|---|---|---|---|
| `identity.model_id` | `list_models` | — | 1 | |
| `identity.author` | `api.author` | `model_id` 앞부분 | 2A | |
| `identity.revision` | `api.sha` | — | 2A | 없으면 재현 불가 |
| `identity.last_modified` | `api.lastModified` | — | 2A | |
| `identity.gated` | `api.gated` | — | 2A | **못 받으면 `unknown`.** `false`로 추정하지 않는다 |
| `identity.private` | `api.private` | — | 2A | |
| `discovery.downloads` / `likes` | `list_models` → `api` | — | 1 → 2A | 2A 값이 더 최신 |
| `discovery.canonical_model_id` | `cardData.base_model` + 파일명 규칙 | — | 2B | 기존 `family` 로직 유지 |
| `capability.primary_task` | `api.pipeline_tag` | `tags` | 1 | |
| `capability.languages` | `cardData.language` | README 본문 | 2A → 3 | README 유도는 `inferred` |
| `capability.korean_verified` | `cardData.language`에 `ko` | README 한국어 비중 | 2A → 3 | |
| `capability.translation_pairs` | `cardData.tags`, README | — | 2B | 없으면 `not_applicable` |
| `capability.embedding_dimensions` | `config.hidden_size` | `sentence_bert_config.json` | 2A | 임베딩 과제만 |
| `capability.reranker` | `library_name`, `tags` | README | 2B | |
| `technical.architecture` | `api.config.architectures` | `gguf.architecture` | 2A | **응답에 이미 있다** |
| `technical.model_type` | `api.config.model_type` | `gguf.architecture` | 2A | |
| `technical.parameter_count_total` | `api.safetensors.total` | `gguf.total` | 2A | 둘 다 HF가 파일을 파싱한 값 = `verified` |
| `technical.parameter_count_active` | 원본 `config.json`의 `num_experts_per_tok` | — | 2B | MoE만. 불명확하면 `conflict` |
| `technical.context_length` | `api.config.max_position_embeddings` | `gguf.context_length` | 2A | 센티넬(2³²−1 등) 걸러낸다 |
| `technical.dtype` | `api.safetensors.parameters` 키 | `config.torch_dtype` | 2A | GGUF는 `not_applicable` |
| `artifacts.formats.*` | `siblings[].rfilename` 패턴 | — | 2A | **`tags`를 믿지 않는다.** 아래 참고 |
| `artifacts.formats.*.total_bytes` | `siblings[].size` 합 | **없음** | 2A | 측정값. 크기가 없으면 `unknown` |
| `artifacts.formats.gguf.quantization` | 파일명의 `Q4_K_M`·`IQ3_XS` 패턴 | — | 2B | 한 레포에 여러 벌이 있다 |
| `deployment.targets.*` | `siblings`의 포맷 존재 → `artifact_present` | README 명시 → `documented` | 2B | 등급을 뭉개지 않는다 |
| `deployment.vram_estimate` | `artifacts.*.total_bytes` (`basis: artifact_bytes`) | `parameter_count × dtype` (`basis: parameter_count`) | 2B | 전자가 측정값이므로 우선 |
| `legal.license_raw` | `cardData.license` | `tags`의 `license:*` | 2A | |
| `legal.license_file` | `LICENSE` / `LICENSE.md` / `LICENSE.txt` / `COPYING` / `NOTICE` | — | 2A | 원문 수집까지만. LLM 자동 판정 안 한다 |
| `legal.commercial_status` | `taxonomy.normalize("commercial_use", license_raw)` | — | 2B | 매핑 테이블을 새로 만들지 않는다 |
| `legal.base_model_constraint` | `cardData.base_model` → 원본의 `commercial_status` | — | 2B | 더 제한적이면 표시. 덮어쓰지 않는다 |
| `quality.results` | `model-index` | README 표 파싱 (`06`) | 2B | `evidence_ref`로 원문 위치를 남긴다 |
| `semantic.*` | README 본문 → LLM | — | 3 | **사실 필드가 아니다.** 하드 필터가 읽지 않는다 |

---

### `usedStorage`를 쓰지 않는 이유

처음에는 `siblings[].size` 합의 교차 검증 출처로 쓰려 했다. **버렸다.**
현재 스냅샷의 크기가 아니기 때문이다.

중앙값만 보면 일치한다(1.000). 그런데 표본 1,796건 중 **521건(29%)이 2% 밖**이고
꼬리가 극단적이다.

```
yongzx/gpt2-finetuned-oscar-ko   siblings  404MB  vs  usedStorage  709GB   0.001배
CohereLabs/tiny-aya-l2-thinker   siblings  6.7GB  vs  usedStorage  429GB   0.016배
RANITBAG/on_the_way              siblings  1.6GB  vs  usedStorage  630MB   2.509배
```

LFS 히스토리를 포함한 과금 기준 용량으로 보인다. 삭제된 리비전의 바이트가 남아
있는 쪽은 `siblings` 합보다 훨씬 크고, 반대로 작은 경우도 있다.

**중앙값만 보고 교차 검증에 썼으면 정상 모델 521건에 거짓 경고가 붙었다.**
`resolvers/artifacts.py`는 `usedStorage`를 읽지 않는다. `siblings[].size`가
없으면 그대로 `unknown`으로 둔다 — **대신 쓸 2차 출처가 없다.**

### `tags`가 아니라 파일 목록을 봐야 하는 이유

```
SL-AI/GRaPE-2.5-Helios-GGUF
  tags       ["gguf", "safetensors", ...]        ← safetensors 태그가 붙어 있다
  실제 파일   *.gguf 6개 + mmproj-BF16.gguf       ← safetensors 파일은 없다
```

표본 1,804건을 전수로 비교한 결과다.

| 판정 기준 | 실제 파일과 불일치 |
|---|---:|
| `"safetensors" in tags` | 49개 (2.7%) |
| `"gguf" in tags` | 1개 (0.1%) |

`artifacts.formats.*.present`는 `siblings[].rfilename` 확장자로만 판정한다.

---

## 3. 따로 내려받아야 하는 파일

`api` 응답에 없어서 `hf_hub_download`가 필요한 것만 남긴다.

| 파일 | 왜 필요 | 단계 | 비용 |
|---|---|---|---|
| `README.md` | `semantic.*`, `quality.results`, 언어 유도 | 2A | 큼. 기존대로 캐시한다 |
| `LICENSE` 류 | `legal.license_file` | 2A | 작음 (수 KB) |
| `config.json` | `max_position_embeddings`, `torch_dtype`, MoE 전문가 수 | 2A | `api.config`가 일부를 주므로 **누락 필드가 있을 때만** |
| `tokenizer_config.json` | `model_max_length` (컨텍스트 2차 출처) | 2A | `api.config.tokenizer_config`가 일부를 준다 |

### LICENSE 수집의 기대 효과 — 측정값

`other`/`null` 라이선스 모델에 실제 LICENSE 파일이 있는 비율이다.

| 라이선스 상태 | 표본 | LICENSE 파일 있음 | 전체 코퍼스 환산 |
|---|---:|---:|---|
| `other` | 334 | 118 (**35.3%**) | 949개 중 약 335개 |
| `null` | 262 | 19 (7.3%) | 277개 중 약 20개 |
| 이름 있는 라이선스 | 1,207 | 87 (7.2%) | 교차 검증용 |

**`other` 949개 중 약 335개를 "사람이 읽어 판정할 수 있는 상태"로 만들 수 있다.**
자동으로 `permitted`가 되는 것이 아니다. 원문과 해시를 모아 검토 큐에 올리는
것까지가 파이프라인의 일이다.

`null` 277개는 대부분 복구 불가다. **전부 채울 수 없다는 것을 계약이 인정한다.**
그 경우 사용자에게 할 말이 `legal.user_message`에 적혀 있다.

---

## 4. 외부 문서는 어디까지 허용하나

`official_doc:` 출처를 쓸 수 있는 경로를 제한한다. 아무 블로그나 가져오면
근거의 등급이 무너진다.

```
① 현재 모델 저장소
     ↓ 없으면
② cardData.base_model 이 가리키는 공식 원본 저장소
     ↓ 없으면
③ 그 조직의 공식 라이선스·사용 약관 페이지
   (meta.com/llama/license, ai.google.dev/gemma/terms 등)
     ↓ 없으면
④ unknown. 추측하지 않는다.
```

③까지만 `official_doc:<URL>`로 기록한다. ④는 `provenance.review_queue`에
올려 사람이 본다.

---

## 5. 현재 보유 상태

`ai/backfill/raw/`에 HF 원본 응답 1,803건이 있다. 코퍼스 3,872개 중 46.6%다.
빈 필드가 있는 모델만 받았기 때문이다.

재적재에서는 전체를 받는다. 이유는 두 가지다.

- `gated`·`sha`·`siblings[].size`는 **지금 값이 있는 모델에도 없다.**
  빈 필드 기준으로 고르면 이 셋을 못 채운다.
- 기존 값의 교차 검증이 필요하다. `artifacts.gguf` 플래그는 파일명 패턴으로
  판정한 값인데, HF의 `gguf` 메타데이터와 어긋나는 모델이 있다. 둘 중 하나가
  틀렸다는 신호이고, 어느 쪽인지는 전수로 봐야 안다.

호출 비용은 모델당 1회, 간격 0.12초로 약 8분이다. 유료 API가 아니다.
