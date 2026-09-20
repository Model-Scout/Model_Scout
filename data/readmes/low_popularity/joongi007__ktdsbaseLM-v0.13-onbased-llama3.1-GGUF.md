---
base_model: AIDX-ktds/ktdsbaseLM-v0.13-onbased-llama3.1
license: apache-2.0
pipeline_tag: text-generation
language:
- ko
model-index:
- name: joongi007/ktdsbaseLM-v0.13-onbased-llama3.1-GGUF
  results: []
---
- Original model is [AIDX-ktds/ktdsbaseLM-v0.13-onbased-llama3.1](https://huggingface.co/AIDX-ktds/ktdsbaseLM-v0.13-onbased-llama3.1) - [ce04fba](https://huggingface.co/AIDX-ktds/ktdsbaseLM-v0.13-onbased-llama3.1/tree/ce04fba937dd7d8e83e7eabdd31e1ca5b0727cf4)
- quantized using [llama.cpp](https://github.com/ggerganov/llama.cpp) - [b3889](https://github.com/ggerganov/llama.cpp/releases/tag/b3889)

### Prompt(LM Studio)
```prompt
<|start_header_id|>system<|end_header_id|>

{System}
<|eot_id|><|start_header_id|>user<|end_header_id|>

{User}
<|eot_id|><|start_header_id|>assistant<|end_header_id|>

{Assistant}
```

### Example(`Q4_K_M`)
```
user : 「국민건강보험법」제44조, 「국민건강보험법 시행령」제19조,「약관의 규제에 관한 법률」제5조, 「상법」제54조 참조 판단 해줘
답변:
assistant : 해당 관련 조문들을 살펴보면 다음과 같다.

1. 국민건강보험법 제44조 :

 "약과 화장품 및 의약용 세일러 등에 관한 규정을 정할 수 있다."

2. 국민건강보험법 시행령 제19조 :

"제 44조(의약품·화장품·의약용세일러등의규제)에 따른 규정은 다음 각 호와 같다.

① 약, 의약품, 화장품 및 의약용 세일러에 관한 사항
② 제조업자 또는 판매업자의 부당한 행위(행위로 인하여 건강을 해할 우려가 있는 행위, 그 밖의 사해로운 행위)를 방지하기 위하여 필요한 사항"

3. 약관의 규제에 관한 법률 제5조 :

"(제1조에서 정하는 바에 따라) 약관의 내용 및 작성은 다음 각 목의 규정을 기준으로 한다.

① 의약품 또는 화장품을 제조, 판매, 수입, 판매한 자가 약과 화장품법, 국민건강보험법·국민안전처법률 제 3조제1항,약품안전관리법 등 법령에 따라야 함
② 약관이 제2호의 법령에서 규정하는 의약품 또는 화장품 관련 법령 및 규율을 위반하는 것은 안될 것

③ 위의 규정을 위반하여 약관을 작성한 경우에는 그 약관의 내용은 무효로 하며, 그 법률상 책임이 있을 수 있다."

4. 상법 제54조 :

"(제51조 제1항에서 정하는 바에 의한 판매와 같은 물의 이전과 그에 준하는 권리수증은 이 법의 규정에 의하여 정함이 없는 경우에는 일반적으로 법적사실관계를形成한다고 인정할 수 없지 않다."

해당 관련 조문들을 살펴보면, 약관의 내용 및 작성은 국민건강보험법 제44조에서 제시한 바와 같이 약, 화장품 및 의약용 세일러 등에 관한 규정을 정할 수 있다. 그리고 약과 화장품법, 국민건강보험법·국민안전처법률 제 3조제1항, 약품안전관리법 등 법령에 따라야 한다는 내용이 제5조에서 명시되어있다.

이에 따른다면 위와 같은 관련 조문들은 약관의 규제에 관한 법률에서 의약품 또는 화장품을 제조, 판매, 수입, 판매한 자가 약과 화장품법, 국민건강보험법·국민안전처법률 제 3조제1항, 약품안전관리법 등 법령에 따라야 함으로 규정하고 있다.
```