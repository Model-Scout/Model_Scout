---
dataset_info:
  features:
  - name: system
    dtype: string
  - name: question
    dtype: string
  - name: think
    dtype: string
  - name: answer
    dtype: string
  - name: question_ko
    dtype: string
  - name: answer_ko
    dtype: string
  - name: system_ko
    dtype: string
  splits:
  - name: train
    num_bytes: 376980280
    num_examples: 16707
  download_size: 146221274
  dataset_size: 376980280
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
license: apache-2.0
language:
- en
- ko
---

- Let them think in English.

- English system prompt + Korean question + English thinking + Korean answer

#### System message changes

```
Your role as an assistant involves thoroughly exploring questions ...(중략)...

<|begin_of_solution|> {final formatted, precise, and clear solution **written in the same language as the question.**} <|end_of_solution|> ...(하략)
```

#### Translation

- Translated with ```gemini-2.0-flash```

- Question

  - ```Return your final response within \\boxed{}.```, ```Generate an executable Python ...(하략)``` 문구 제거 후 번역, 번역 완료 후 다시 추가

```
아래 텍스트는 질문-답변으로 이루어진 데이터 셋 중 질문에 해당하는 텍스트입니다. 질문에 포함된 정보를 정확하게 전달하면서, 한국 사람이 작성한 질문인 것처럼 자연스럽게 번역해 주세요.
Latex 구문 또는 프로그래밍 코드가 포함된 경우, 더 꼼꼼하게 번역에 유의해 주세요.

---

{question}
```

- Answer

```
아래 텍스트는 **질문-답변**으로 이루어진 영어 데이터 셋과, **질문**에 대한 한국어 번역 결과입니다.
당신의 역할은 질문의 번역 결과를 참고삼아, 원래의 영어 답변을 한국어로 **번역**하는 것입니다.
번역 과정에서는 한국인이 사용하는 표준적인 한국어를 사용하여 자연스럽게 작성하되, 문장 단위로 영어 원문과 매칭이 되도록, 빠짐없이 모든 내용을 번역하세요.
특히 Latex, Markdown 구문 또는 프로그래밍 코드가 포함된 경우, 원문에 사용된 명령어를 있는 그대로 유지하세요. 이제 데이터를 제공하겠습니다.

---

<question_english>{question}
</question_english>

<question_korean>{question_ko}
</question_korean>

<answer_english>{answer}
</answer_english>
```

- Filtering
  - Latex grammer check (rule-based detection + manual judgment)
  - Boxed answer check (rule-based detection + manual judgment)
    - 3 data are dropped