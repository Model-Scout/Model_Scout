---
type: "dataset"
id: "allenai/MADLAD-400"
source: "huggingface"
url: "https://huggingface.co/datasets/allenai/MADLAD-400"
downloads: 120618
summary: "MADLAD-400은 Common Crawl 기반 419개 언어의 문서 수준 다국어 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "not_ko"
task:
  - "[[임베딩]]"
  - "[[텍스트 생성]]"
  - "[[문서 검색]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# allenai/MADLAD-400

> dataset · [Hugging Face](https://huggingface.co/datasets/allenai/MADLAD-400)

MADLAD-400은 Common Crawl 기반 419개 언어의 문서 수준 다국어 데이터셋입니다.

## 분류

- **작업**: [[임베딩]] — ner · readme = `a document-level multilingual dataset based on Common Crawl` · 신뢰도 low
- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[문서 검색]] — ner · readme = `a document-level multilingual dataset based on Common Crawl` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:embedding, task:generation, task:retrieval = `a document-level multilingual dataset based on Common Crawl` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `a document-level multilingual dataset based on Common Crawl` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `a document-level multilingual dataset based on Common Crawl, covering 419 languages in total` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `This uses all snapshots of CommonCrawl available as of August 1, 2022.` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `inf` · 신뢰도 high

## 이 데이터로 학습한 모델

- [[CXDuncan__madlad400-3b-mt-optimized-quantized-onnx|CXDuncan/madlad400-3b-mt-optimized-quantized-onnx]]
- [[Heng666__madlad400-3b-mt-ct2-int8|Heng666/madlad400-3b-mt-ct2-int8]]
- [[JSCreatorPro__offline-cpu-madlad-400|JSCreatorPro/offline-cpu-madlad-400]]
- [[LifeAi-dev__madlad400-10b-ct2-float32|LifeAi-dev/madlad400-10b-ct2-float32]]
- [[Nextcloud-AI__madlad400-3b-mt-ct2-int8|Nextcloud-AI/madlad400-3b-mt-ct2-int8]]
- [[Nextcloud-AI__madlad400-3b-mt-ct2-int8_float32|Nextcloud-AI/madlad400-3b-mt-ct2-int8_float32]]
- [[NikolayKozloff__madlad400-10b-mt-Q8_0-GGUF|NikolayKozloff/madlad400-10b-mt-Q8_0-GGUF]]
- [[NostraEmpire__mirror-madlad400-3b-mt|NostraEmpire/mirror-madlad400-3b-mt]]
- [[cstr__madlad400-3b-ct2-int8|cstr/madlad400-3b-ct2-int8]]
- [[egekocabas__madlad400-7b-mt-Q5_K_M-GGUF|egekocabas/madlad400-7b-mt-Q5_K_M-GGUF]]
- [[google__madlad400-10b-mt|google/madlad400-10b-mt]]
- [[google__madlad400-3b-mt|google/madlad400-3b-mt]]
- [[google__madlad400-7b-mt|google/madlad400-7b-mt]]
- [[google__madlad400-7b-mt-bt|google/madlad400-7b-mt-bt]]
- [[google__madlad400-8b-lm|google/madlad400-8b-lm]]
- [[htafer__madlad400-10b-mt-Q4_K_M-GGUF|htafer/madlad400-10b-mt-Q4_K_M-GGUF]]
- [[jbochi__madlad400-10b-mt|jbochi/madlad400-10b-mt]]
- [[jbochi__madlad400-3b-mt|jbochi/madlad400-3b-mt]]
- [[jbochi__madlad400-7b-mt|jbochi/madlad400-7b-mt]]
- [[jbochi__madlad400-7b-mt-bt|jbochi/madlad400-7b-mt-bt]]
- [[mtsdurica__madlad400-3b-mt-Q4_K_M-GGUF|mtsdurica/madlad400-3b-mt-Q4_K_M-GGUF]]
- [[notjjustnumbers__madlad400-3b-mt-Q4_K_M-GGUF|notjjustnumbers/madlad400-3b-mt-Q4_K_M-GGUF]]
- [[santhosh__madlad400-3b-ct2|santhosh/madlad400-3b-ct2]]
