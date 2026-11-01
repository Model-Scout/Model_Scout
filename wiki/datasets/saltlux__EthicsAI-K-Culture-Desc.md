---
type: "dataset"
id: "saltlux/EthicsAI-K-Culture-Desc"
source: "huggingface"
url: "https://huggingface.co/datasets/saltlux/EthicsAI-K-Culture-Desc"
downloads: 16
summary: "한국 문화 맥락 이해를 평가하는 530개 시나리오 기반 객관식 질문 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[질의응답]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
input_length:
  - "[[단문]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[문화·관광]]"
dataset_role:
  - "[[평가용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[소규모 데이터]]"
---
# saltlux/EthicsAI-K-Culture-Desc

> dataset · [Hugging Face](https://huggingface.co/datasets/saltlux/EthicsAI-K-Culture-Desc)

한국 문화 맥락 이해를 평가하는 530개 시나리오 기반 객관식 질문 데이터셋입니다.

## 분류

- **작업**: [[질의응답]] — metadata · readme, task_categories = `multiple-choice` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:question_answering = `각 항목은 문화적 설명, 실제 상황을 묘사한 시나리오, 그리고 상세한 해설이 포함된 객관식 질문으로 구성되어 있습니다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:question_answering = `객관식 질문 및 정답 정보` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **입력 길이**: [[단문]] — viewer_stats · viewer_statistics = `440` · 신뢰도 medium
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[문화·관광]] — ner · readme = `한국 문화 맥락 이해 벤치마크는 실생활 시나리오와 대화를 통해 거대언어모델(LLM)의 한국 문화 맥락 이해 능력을 평가하기 위해 설계된 데이터셋입니다.` · 신뢰도 medium
- **데이터 용도**: [[평가용]] — ner · readme = `한국 문화에 대한 모델의 맥락적 이해도를 평가하기 위해 설계된 530개의 시나리오 기반 객관식 질문을 포함하는 한국 문화 이해 벤치마크 데이터셋입니다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[소규모 데이터]] — metadata · size_categories = `999.0` · 신뢰도 high

샘플 길이: `ScenarioBody` 열 p90 660자 ≈ 440 토큰 (viewer statistics, default/train)
