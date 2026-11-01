---
dataset_info:
  features:
  - name: id
    dtype: string
  - name: word
    dtype: string
  - name: pos
    dtype: string
  - name: definition
    dtype: string
  - name: word_type
    dtype: string
  - name: sample
    sequence: string
  - name: sentence_wiki
    sequence: string
  - name: word_wiki
    sequence:
      sequence: string
  - name: sentence_kci
    sequence:
      sequence: string
  - name: word_kci
    sequence:
      sequence: string
  - name: gemini-2.5-pro-exp-03-25
    sequence: string
  - name: gpt-4.1-mini
    sequence: string
  - name: deepseek-chat-v3-0324
    sequence: string
  splits:
  - name: train
    num_bytes: 259610304
    num_examples: 116694
  download_size: 154709948
  dataset_size: 259610304
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- en
- ko
---

v0.1: 예제 및 번역 추가

v0.2: wiki 실사용 사례 추가

v0.3: KCI 논문 사례 추가



- wiki/논문 사례가 엄밀하지 못하여 개선 필요...

---

- ID, Word, POS, definition은 [WordNet](https://wordnet.princeton.edu/)에서 가져왔습니다.
  - 모든 ID는 유일하지만, id에 포함된 단어가 word는 아닙니다. 데이터 가공 과정에서의 실수 + 원본 WordNet에서 발생한 오타 교정 때문입니다.
- word_type, sample은 **gemini-2.5-pro-exp-03-25**를 이용하여 인공적으로 생성되었습니다.
- sentence_wiki: [한국어 위키피디아](https://huggingface.co/datasets/wikimedia/wikipedia)에서, 실제로 해당 단어가 한국어와 원문 모두 표기되어 있는 문장을 추출하였습니다.
  - 문장 추출 및 검증에는 **gemini-2.5-pro-exp-03-25**와 **Qwen3-30B-A3B** 모델이 사용되었습니다.
  - AI 검증 특성상, 잘못 추출된 경우가 있을 수 있습니다. (예시: elder.n.03 - (교회의)장로, wiki 예제에는 존윅3의 엘더, 엘더베리와 같은 과일 등이 포함되어 있음)
- word_wiki: sentence_wiki 문장에서 해당 단어의 번역 결과입니다.
- sentence_kci: KCI 논문 제목 및 초록에서 해당 단어가 사용되었을 때의 영문 제목/초록과 국문 제목/초록 쌍입니다.
  - 마찬가지로 AI 검증이 이루어졌지만, 잘못 추출된 경우가 있을 수 있으며, 원문을 그대로 사용한 경우도 포함되어 있습니다. (예시: elder.n.03 - (교회의)장로, kci 예제에서는 노인/엘더스크롤 관련 사용례들이 등장함)
- word_kci: sentence_kci 문장에서 해당 단어의 번역 결과입니다.
- gemini-2.5-pro-exp-03-25, gpt-4.1-mini, deepseek-chat-v3-0324: 각 모델에게 word, pos, definition, sample을 주고, 단어를 한글로 번역해 달라고 요청한 결과입니다.

---

위키, 논문 사례는 밑둥썩음병(bottom rot) 등의 전문 용어 번역을 개선할 수 있을 것 같으나, 택(tack)(항해 용어), 환상박피(girdle)의 경우 위키/논문 사례가 적절하지 못해 방해를 일으킴

위키, 논문 사례가 존재하는 데이터 자체가 전체 단어의 절반 미만임