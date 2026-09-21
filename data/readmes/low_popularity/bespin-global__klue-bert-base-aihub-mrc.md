---
language: ko
tags:
- bert
- mrc
datasets:
- aihub
license: cc-by-nc-4.0
---
## Demo
 - [https://huggingface.co/spaces/bespin-global/Bespin-QuestionAnswering](https://huggingface.co/spaces/bespin-global/Bespin-QuestionAnswering)


## Finetuning
- Pretrain Model : [klue/bert-base](https://github.com/KLUE-benchmark/KLUE)
- Dataset for fine-tuning : [AIHub 기계독해 데이터셋](https://aihub.or.kr/aidata/86) 
  - 표준 데이터 셋(25m) + 설명 가능 데이터 셋(10m)
  - Random Sampling (random_seed: 1234)
    - Train : 30m
    - Test : 5m
- Parameters of Training
```
{
    "epochs": 4,
    "batch_size":8,
    "optimizer_class": "<class 'transformers.optimization.AdamW'>",
    "optimizer_params": {
        "lr": 3e-05
    },
    "weight_decay: 0.01
}
```

## Usage
```python
## Load Transformers library
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

def predict_answer(qa_text_pair):
    # Encoding
    encodings = tokenizer(context, question, 
                      max_length=512, 
                      truncation=True,
                      padding="max_length", 
                      return_token_type_ids=False,
                      return_offsets_mapping=True
                      )
    encodings = {key: torch.tensor([val]).to(device) for key, val in encodings.items()}             

    # Predict
    pred = model(encodings["input_ids"], attention_mask=encodings["attention_mask"])
    start_logits, end_logits = pred.start_logits, pred.end_logits
    token_start_index, token_end_index = start_logits.argmax(dim=-1), end_logits.argmax(dim=-1)
    pred_ids = encodings["input_ids"][0][token_start_index: token_end_index + 1]
    answer_text = tokenizer.decode(pred_ids)

    # Offset
    answer_start_offset = int(encodings['offset_mapping'][0][token_start_index][0][0])
    answer_end_offset = int(encodings['offset_mapping'][0][token_end_index][0][1])
    answer_offset = (answer_start_offset, answer_end_offset)
 
    return {'answer_text':answer_text, 'answer_offset':answer_offset}


## Load fine-tuned MRC model by HuggingFace Model Hub ##
HUGGINGFACE_MODEL_PATH = "bespin-global/klue-bert-base-aihub-mrc"
tokenizer = AutoTokenizer.from_pretrained(HUGGINGFACE_MODEL_PATH)
model = AutoModelForQuestionAnswering.from_pretrained(HUGGINGFACE_MODEL_PATH).to(device)


## Predict ## 
context = '''애플 M2(Apple M2)는 애플이 설계한 중앙 처리 장치(CPU)와 그래픽 처리 장치(GPU)의 ARM 기반 시스템이다. 
인텔 코어(Intel Core)에서 맥킨토시 컴퓨터용으로 설계된 2세대 ARM 아키텍처이다. 애플은 2022년 6월 6일 WWDC에서 맥북 에어, 13인치 맥북 프로와 함께 M2를 발표했다. 
애플 M1의 후속작이다. M2는 TSMC의 '향상된 5나노미터 기술' N5P 공정으로 만들어졌으며, 이전 세대 M1보다 25% 증가한 200억개의 트랜지스터를 포함하고 있으며, 최대 24기가바이트의 RAM과 2테라바이트의 저장공간으로 구성할 수 있다. 
8개의 CPU 코어(성능 4개, 효율성 4개)와 최대 10개의 GPU 코어를 가지고 있다. M2는 또한 메모리 대역폭을 100 GB/s로 증가시킨다. 
애플은 기존 M1 대비 CPU가 최대 18%, GPU가 최대 35% 향상됐다고 주장하고 있으며,[1] 블룸버그통신은 M2맥스에 CPU 코어 12개와 GPU 코어 38개가 포함될 것이라고 보도했다.'''
question = "m2가 m1에 비해 얼마나 좋아졌어?"

qa_text_pair = {'context':context, 'question':question}
result = predict_answer(qa_text_pair)
print('Answer Text: ', result['answer_text'])  # 기존 M1 대비 CPU가 최대 18 %, GPU가 최대 35 % 향상
print('Answer Offset: ', result['answer_offset'])  # (410, 446)
```

## Citing & Authors

<!--- Describe where people can find more information -->
[Jaehyeong](https://huggingface.co/jaehyeong) at [Bespin Global](https://www.bespinglobal.com/)