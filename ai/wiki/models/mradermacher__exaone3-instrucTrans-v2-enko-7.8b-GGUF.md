---
type: "model"
id: "mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF"
source: "huggingface"
url: "https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF"
downloads: 590
task:
  - "[[번역]]"
input_modality:
  - "[[텍스트 (입력 형식)|텍스트]]"
output_modality:
  - "[[텍스트 (출력 형식)|텍스트]]"
language:
  - "[[영어]]"
  - "[[한국어]]"
commercial_use:
  - "[[이용 조건 미확인]]"
---
# mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF

> model · [Hugging Face](https://huggingface.co/mradermacher/exaone3-instrucTrans-v2-enko-7.8b-GGUF)

## 분류

- **작업**: [[번역]] — metadata · task.matched = `translation` · 신뢰도 high
- **입력 형식**: [[텍스트 (입력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **출력 형식**: [[텍스트 (출력 형식)|텍스트]] — task_rule · task:translation = `text` · 신뢰도 medium
- **언어**: [[영어]] — metadata · language_codes = `en` · 신뢰도 high
- **언어**: [[한국어]] — metadata · language_codes = `ko` · 신뢰도 high
- **상업 이용**: [[이용 조건 미확인]] — metadata · license · 신뢰도 high

## 학습 데이터

- [[Translation-EnKo__trc_uniform_313k_eval_45_filtered|Translation-EnKo/trc_uniform_313k_eval_45_filtered]]
- [[nayohan__aihub-en-ko-translation-12m|nayohan/aihub-en-ko-translation-12m]]
- [[nayohan__instruction_en_ko_translation_1.4m|nayohan/instruction_en_ko_translation_1.4m]]
