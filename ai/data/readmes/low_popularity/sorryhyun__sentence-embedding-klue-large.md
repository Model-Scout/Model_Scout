---
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- feature-extraction
- sentence-similarity
- transformers
license: cc-by-sa-4.0
datasets:
- klue
language:
- ko
---

본 모델은 multi-task loss (MultipleNegativeLoss -> AnglELoss) 로, KlueNLI 및 KlueSTS 데이터로 학습되었습니다. 학습 코드는 다음 [Github hyperlink](https://github.com/comchobo/SFT_sent_emb?tab=readme-ov-file)에서 보실 수 있습니다.

## Usage (Huggingface inference API)

```python
import requests

API_URL = "https://api-inference.huggingface.co/models/sorryhyun/sentence-embedding-klue-large"
headers = {"Authorization": "your_HF_token"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    "inputs": {
        "source_sentence": "좋아요, 추천, 알림설정까지",
        "sentences": [
            "좋아요 눌러주세요!!",
            "좋아요, 추천 등 유투버들이 좋아해요",
            "알림설정을 눌러주시면 감사드리겠습니다."
        ]
    },
})
if __name__ == '__main__':
  print(output)
```

## Usage (HuggingFace Transformers)

```python
from transformers import AutoTokenizer, AutoModel, DataCollatorWithPadding
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm
from datasets import Dataset

device = torch.device('cpu')
batch_size=1

# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('sorryhyun/sentence-embedding-klue-large')
collator = DataCollatorWithPadding(tokenizer=tokenizer)
model = AutoModel.from_pretrained('sorryhyun/sentence-embedding-klue-large').to(device)

tokenized_data = tokenizer(sentences, padding=True, truncation=True)
tokenized_data = Dataset.from_dict(tokenized_data)
dataloader = DataLoader(tokenized_data, batch_size=batch_size, pin_memory=True, collate_fn=collator)
all_outputs = torch.zeros((len(tokenized_data), 1024)).to(device)
start_idx = 0

# I used mean-pool method for sentence representation
with torch.no_grad():
  for inputs in tqdm(dataloader):
    inputs = {k: v.to(device) for k, v in inputs.items()}
    representations, _ = model(**inputs, return_dict=False)
    attention_mask = inputs["attention_mask"]
    input_mask_expanded = (attention_mask.unsqueeze(-1).expand(representations.size()).to(representations.dtype))
    summed = torch.sum(representations * input_mask_expanded, 1)
    sum_mask = input_mask_expanded.sum(1)
    sum_mask = torch.clamp(sum_mask, min=1e-9)
    end_idx = start_idx + representations.shape[0]
    all_outputs[start_idx:end_idx] = (summed / sum_mask)
    start_idx = end_idx

```


## Evaluation Results

| Organization | Backbone Model | KlueSTS average | KorSTS average |
| -------- | ------- | ------- | ------- |
| team-lucid | DeBERTa-base | 54.15 | 29.72 |
| monologg | Electra-base | 66.97 | 40.98 |
| LMkor | Electra-base | 70.98 | 43.09 |
| deliciouscat | DeBERTa-base | - | 67.65 |
| BM-K    | Roberta-base | 82.93 | **85.77** |
| Klue    | Roberta-large | **86.71** | 71.70 |
| Klue (Hyperparameter searched) | Roberta-large | 86.21 | 75.54 |

기존 한국어 문장 임베딩 모델은 mnli, snli 등 영어 데이터셋을 기계번역하여 학습된 점을 참고삼아 Klue 데이터셋으로 대신 학습해 보았습니다.

그 결과, Klue-Roberta-large 모델 기반으로 학습했을 경우 KlueSTS 및 KorSTS 테스트셋에 모두에 대해 준수한 성능을 보여, 좀 더 elaborate한 representation을 형성하는 것으로 사료했습니다.

다만 평가 수치는 하이퍼파라미터 세팅, 시드 넘버 등으로 크게 달라질 수 있으므로 참고하시길 바랍니다.

## Training
NegativeRank loss -> simcse loss 로 학습했습니다.

