---
language: ko
tags:
- intent-classification
datasets:
- kor_3i4k
license: cc-by-nc-4.0
---

## Finetuning
- Pretrain Model : [klue/roberta-small](https://github.com/KLUE-benchmark/KLUE)
- Dataset for fine-tuning : [3i4k](https://github.com/warnikchow/3i4k) 
  - Train : 46,863
  - Validation : 8,271 (15% of Train)
  - Test : 6,121
- Label info 
  - 0: "fragment",
  - 1: "statement",
  - 2: "question",
  - 3: "command",
  - 4: "rhetorical question",
  - 5: "rhetorical command",
  - 6: "intonation-dependent utterance"
- Parameters of Training
```
{
    "epochs": 3 (setting 10 but early stopped),
    "batch_size":32,
    "optimizer_class": "<keras.optimizer_v2.adam.Adam'>",
    "optimizer_params": {
        "lr": 5e-05
    },
    "min_delta": 0.01
}
```

## Usage
``` python
from transformers import RobertaTokenizerFast, RobertaForSequenceClassification, TextClassificationPipeline

# Load fine-tuned model by HuggingFace Model Hub
HUGGINGFACE_MODEL_PATH = "bespin-global/klue-roberta-small-3i4k-intent-classification"
loaded_tokenizer = RobertaTokenizerFast.from_pretrained(HUGGINGFACE_MODEL_PATH )
loaded_model = RobertaForSequenceClassification.from_pretrained(HUGGINGFACE_MODEL_PATH )

# using Pipeline
text_classifier = TextClassificationPipeline(
    tokenizer=loaded_tokenizer, 
    model=loaded_model, 
    return_all_scores=True
)

# predict
text = "your text"

preds_list = text_classifier(text)
best_pred = preds_list[0]
print(f"Label of Best Intentatioin: {best_pred['label']}")
print(f"Score of Best Intentatioin: {best_pred['score']}")
```

## Evaluation
```
                               precision    recall  f1-score   support

                      command       0.89      0.92      0.90      1296
                     fragment       0.98      0.96      0.97       600
intonation-depedent utterance       0.71      0.69      0.70       327
                     question       0.95      0.97      0.96      1786
           rhetorical command       0.87      0.64      0.74       108
          rhetorical question       0.61      0.63      0.62       174
                    statement       0.91      0.89      0.90      1830

                     accuracy                           0.90      6121
                    macro avg       0.85      0.81      0.83      6121
                 weighted avg       0.90      0.90      0.90      6121
```


## Citing & Authors
<!--- Describe where people can find more information -->
[Jaehyeong](https://huggingface.co/jaehyeong) at [Bespin Global](https://www.bespinglobal.com/)