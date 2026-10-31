---
type: "dataset"
id: "HuggingFaceFW/fineweb-2"
source: "huggingface"
url: "https://huggingface.co/datasets/HuggingFaceFW/fineweb-2"
downloads: 133446
summary: "1000개 이상의 언어에 대해 고품질 사전학습 데이터를 제공하는 FineWeb2 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "wide_multilingual"
task:
  - "[[텍스트 생성]]"
  - "[[언어 모델링]]"
input_modality:
  - "[[표 (입력 형식)|표]]"
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
  - "[[다국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
dataset_size:
  - "[[초대규모 데이터]]"
---
# HuggingFaceFW/fineweb-2

> dataset · [Hugging Face](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2)

1000개 이상의 언어에 대해 고품질 사전학습 데이터를 제공하는 FineWeb2 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · task_categories = `text-generation` · 신뢰도 low
- **작업**: [[언어 모델링]] — ner · readme = `bringing high quality pretraining data to over 1000 🗣️ languages` · 신뢰도 low
- **입력 형식**: [[표 (입력 형식)|표]] — metadata · modality = `tabular` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation, task:language_modeling = `bringing high quality pretraining data to over 1000 🗣️ languages` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation, task:language_modeling = `bringing high quality pretraining data to over 1000 🗣️ languages` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **언어**: [[다국어]] — metadata · languages = `1813 languages` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1785` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `odc-by` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `This is the second iteration of the popular 🍷 FineWeb dataset, bringing high quality pretraining data to over 1000 🗣️ languages.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `The 🥂 FineWeb2 dataset is fully reproducible, available under the permissive ODC-By 1.0 license and extensively validated through hundreds of ablation experimen` · 신뢰도 medium
- **데이터 규모**: [[초대규모 데이터]] — metadata · size_categories = `9999999999.0` · 신뢰도 high

샘플 길이: `text` 열 p90 7139자 ≈ 1785 토큰 (viewer statistics, kor_Hang/test)

## 이 데이터로 학습한 모델

- [[ATH-MaaS__Marco-Mini-Base|ATH-MaaS/Marco-Mini-Base]]
- [[ATH-MaaS__Marco-Mini-Global-Base|ATH-MaaS/Marco-Mini-Global-Base]]
- [[ATH-MaaS__Marco-Nano-Base|ATH-MaaS/Marco-Nano-Base]]
- [[AneekC__quipu-moe-1B-A149M|AneekC/quipu-moe-1B-A149M]]
- [[AneekC__quipu-moe-1B-A149M-chat|AneekC/quipu-moe-1B-A149M-chat]]
- [[AneekC__quipu-moe-1B-A149M-chat-distill|AneekC/quipu-moe-1B-A149M-chat-distill]]
- [[Horizon-Labs__multilingual-embedding-base|Horizon-Labs/multilingual-embedding-base]]
- [[Horizon-Labs__multilingual-embedding-small|Horizon-Labs/multilingual-embedding-small]]
- [[Horizon-Labs__multilingual-sentiment-base|Horizon-Labs/multilingual-sentiment-base]]
- [[Horizon-Labs__multilingual-sentiment-small|Horizon-Labs/multilingual-sentiment-small]]
- [[Horizon-Labs__prompt-injection-guard-base|Horizon-Labs/prompt-injection-guard-base]]
- [[Horizon-Labs__prompt-injection-guard-large|Horizon-Labs/prompt-injection-guard-large]]
- [[Horizon-Labs__prompt-injection-guard-small|Horizon-Labs/prompt-injection-guard-small]]
- [[PsycheFoundation__consilience-40b-7Y9v38s5|PsycheFoundation/consilience-40b-7Y9v38s5]]
- [[WaveCut__Qwen3.5-2B-MLX-DWQ-4bit|WaveCut/Qwen3.5-2B-MLX-DWQ-4bit]]
- [[cooler8__ZeliDesk-sLM-1B|cooler8/ZeliDesk-sLM-1B]]
- [[ikhou__dict-xs|ikhou/dict-xs]]
- [[prismdata__Perdix-1.1B-Base|prismdata/Perdix-1.1B-Base]]
- [[shopkeeper__kor-finewiki-1b-base|shopkeeper/kor-finewiki-1b-base]]
- [[skt__A.X-K2|skt/A.X-K2]]
- [[skt__A.X-K2-NVFP4|skt/A.X-K2-NVFP4]]
