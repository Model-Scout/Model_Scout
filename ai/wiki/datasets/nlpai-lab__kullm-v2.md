---
type: "dataset"
id: "nlpai-lab/kullm-v2"
source: "huggingface"
url: "https://huggingface.co/datasets/nlpai-lab/kullm-v2"
downloads: 457
summary: "GPT4ALL, Dolly, Vicuna 데이터의 한국어 번역 데이터셋입니다."
readme_status: "ok"
readme_language: "en"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[중문]]"
commercial_use:
  - "[[상업 이용 가능]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# nlpai-lab/kullm-v2

> dataset · [Hugging Face](https://huggingface.co/datasets/nlpai-lab/kullm-v2)

GPT4ALL, Dolly, Vicuna 데이터의 한국어 번역 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = `Translated 'instruction', 'input', and 'output' in the dataset via the DeepL API` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = `Translated 'instruction', 'input', and 'output' in the dataset via the DeepL API` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[중문]] — viewer_stats · viewer_statistics = `1013` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **데이터 용도**: [[학습용]] — ner · readme, referenced_by_models = `>>> ds = load_dataset("nlpai-lab/kullm-v2", split="train")` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `999999.0` · 신뢰도 high

샘플 길이: `output` 열 p90 1520자 ≈ 1013 토큰 (viewer statistics, default/train)

## 같은 데이터의 사본·중복 등록

- `csujeong/kullm-v2.1`

## 이 데이터로 학습한 모델

- [[Edentns__DataVortexTL-1.1B-v0.1|Edentns/DataVortexTL-1.1B-v0.1]]
- [[heegyu__llama-2-ko-7b-chat|heegyu/llama-2-ko-7b-chat]]
- [[mradermacher__DataVortexTL-1.1B-v0.1-GGUF|mradermacher/DataVortexTL-1.1B-v0.1-GGUF]]
- [[mradermacher__DataVortexTL-1.1B-v0.1-i1-GGUF|mradermacher/DataVortexTL-1.1B-v0.1-i1-GGUF]]
- [[nlpai-lab__kullm-polyglot-5.8b-v2|nlpai-lab/kullm-polyglot-5.8b-v2]]
- [[prismdata__Perdix-1.1B-Instruct|prismdata/Perdix-1.1B-Instruct]]
- [[shopkeeper__kor-finewiki-1b-chat|shopkeeper/kor-finewiki-1b-chat]]
- [[tensorblock__DataVortexTL-1.1B-v0.1-GGUF|tensorblock/DataVortexTL-1.1B-v0.1-GGUF]]
