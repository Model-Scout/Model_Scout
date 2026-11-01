---
type: "dataset"
id: "Algocean/gk-synthetic-data-2026-ko"
source: "huggingface"
url: "https://huggingface.co/datasets/Algocean/gk-synthetic-data-2026-ko"
downloads: 26
summary: "외부 teacher 모델의 고급 지식과 장문 설명 능력을 한국어 SFT용으로 증류한 합성 데이터셋입니다."
readme_status: "ok"
readme_language: "mixed"
korean_focus: "ko_only"
task:
  - "[[텍스트 생성]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
data_format:
  - "[[JSON]]"
dataset_size:
  - "[[중규모 데이터]]"
---
# Algocean/gk-synthetic-data-2026-ko

> dataset · [Hugging Face](https://huggingface.co/datasets/Algocean/gk-synthetic-data-2026-ko)

외부 teacher 모델의 고급 지식과 장문 설명 능력을 한국어 SFT용으로 증류한 합성 데이터셋입니다.

## 분류

- **작업**: [[텍스트 생성]] — metadata · readme, task_categories = `text-generation` · 신뢰도 medium
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · modality, readme, task:generation = ``user` 메시지는 정책, 기술, 보안, 거시경제, 기후, 우주개발 같은 2026년 기준 고급 주제에 대한 질문이다.` · 신뢰도 high
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme, task:generation = ``assistant` 메시지는 한국어 장문 답변이며, 최신 사실과 일반 원리를 구분하고 실무적 함의와 한계를 함께 설명한다.` · 신뢰도 medium
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `2026년 기준 고급 주제에 대한 질문이다.` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `한국어 SFT용으로 증류한 데이터셋이다.` · 신뢰도 medium
- **데이터 형식**: [[JSON]] — metadata · format = `json` · 신뢰도 high
- **데이터 규모**: [[중규모 데이터]] — metadata · size_categories = `99999.0` · 신뢰도 high
