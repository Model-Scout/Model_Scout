---
type: "dataset"
id: "withdev/dartlab-committee"
source: "huggingface"
url: "https://huggingface.co/datasets/withdev/dartlab-committee"
downloads: 6
summary: "DartLab Trading AI Agent Committee 데이터셋은 투자 판단의 근거 중심 검증 기록입니다."
readme_status: "ok"
readme_language: "ko"
korean_focus: "ko_only"
task:
  - "[[텍스트 분류]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[한국어]]"
commercial_use:
  - "[[상업 이용 가능]]"
domain:
  - "[[금융·경제]]"
dataset_role:
  - "[[학습용]]"
---
# withdev/dartlab-committee

> dataset · [Hugging Face](https://huggingface.co/datasets/withdev/dartlab-committee)

DartLab Trading AI Agent Committee 데이터셋은 투자 판단의 근거 중심 검증 기록입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `판단의 검증 상태` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:classification = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = `최종 결론은 매수/매도 의견이 아니라 판단의 검증 상태입니다.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[상업 이용 가능]] — metadata · license = `apache-2.0` · 신뢰도 high
- **도메인**: [[금융·경제]] — tag_match · readme, tags = `finance` · 신뢰도 medium
- **데이터 용도**: [[학습용]] — ner · readme = `사용자가 이미 세운 투자 판단을 5단계 AI 위원회가 근거 중심으로 검증한 기록입니다.` · 신뢰도 low
