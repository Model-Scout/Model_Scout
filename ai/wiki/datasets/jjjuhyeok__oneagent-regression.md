---
type: "dataset"
id: "jjjuhyeok/oneagent-regression"
source: "huggingface"
url: "https://huggingface.co/datasets/jjjuhyeok/oneagent-regression"
downloads: 18
summary: "OneAgent 컴퓨터 앱 조작 기능 회귀 검증용 시드 시나리오 모음 데이터셋입니다."
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
  - "[[조건부 이용]]"
domain:
  - "[[일반]]"
dataset_role:
  - "[[학습용]]"
---
# jjjuhyeok/oneagent-regression

> dataset · [Hugging Face](https://huggingface.co/datasets/jjjuhyeok/oneagent-regression)

OneAgent 컴퓨터 앱 조작 기능 회귀 검증용 시드 시나리오 모음 데이터셋입니다.

## 분류

- **작업**: [[텍스트 분류]] — ner · readme = `OneAgent(컴퓨터유즈)의 앱 조작 기능을 회귀 검증하는 시드 시나리오 모음입니다.` · 신뢰도 low
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — ner · readme, task:classification = ``instruct` — OneAgent에 줄 실제 지시문.` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — ner · readme = ``verify` — 정답(무엇을 어떻게 확인하나): engine(com/cdp/file/vlm), 기대 값·서식·개수 등.` · 신뢰도 low
- **언어**: [[한국어]] — metadata · languages = `ko` · 신뢰도 high
- **상업 이용**: [[조건부 이용]] — metadata · license = `other` · 신뢰도 high
- **도메인**: [[일반]] — ner · readme = `OneAgent Computer Use — 리그레션 테스트 데이터셋` · 신뢰도 low
- **데이터 용도**: [[학습용]] — ner · readme = `OneAgent를 수정할 때마다 예전에 되던 기능이 조용히 깨졌는지 자동으로 잡아내는 데 쓰입니다.` · 신뢰도 low
