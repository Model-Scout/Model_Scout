---
license: apache-2.0
language:
- multilingual
- en
- de
- fr
- es
- pt
- it
- nl
- pl
- ru
- uk
- tr
- ar
- fa
- he
- hi
- bn
- ur
- mr
- pa
- zh
- ja
- ko
- vi
- th
- id
- ms
- jv
- sw
- sv
- 'no'
- da
- fi
- cs
- ro
- hu
- el
library_name: transformers.js
pipeline_tag: text-classification
base_model:
- Horizon-Labs/phishing-scam-detector-base
tags:
- phishing
- phishing-detection
- scam-detection
- smishing
- spam-detection
- fraud-detection
- email-security
- multilingual
- modernbert
- mmbert
- onnx
- transformers.js
widget:
- text: 'Your parcel could not be delivered. Pay the 1.99 EUR customs fee within 24h:
    dhl-redelivery.example.com'
  example_title: Parcel scam
- text: Hi, running 10 min late, see you at the cafe
  example_title: Normal message
- text: "Ihr Konto wurde gesperrt. Best\xE4tigen Sie Ihre Daten innerhalb von 24 Stunden:\
    \ sparkasse-sicher.example.de"
  example_title: German phishing
- text: MEGA SALE 70% off all shoes this weekend only! Shop now
  example_title: Marketing spam
---



# phishing-scam-detector-base (ONNX)


This is an ONNX version of [Horizon-Labs/phishing-scam-detector-base](https://huggingface.co/Horizon-Labs/phishing-scam-detector-base). It was automatically converted and uploaded using [this Hugging Face Space](https://huggingface.co/spaces/onnx-community/convert-to-onnx).


## Usage with Transformers.js


See the pipeline documentation for `text-classification`: https://huggingface.co/docs/transformers.js/api/pipelines#module_pipelines.TextClassificationPipeline


---


# Phishing & Scam Detector (base, 307M): multilingual

Flags **phishing, scams and spam** in emails, SMS, chat and social-media messages in many languages. Three labels:

- **`fraud`**: phishing (fake bank, delivery, account or tax messages with links), scams (prizes, investment and crypto schemes,
  fake jobs, "hi mum, new number", romance, advance fee), requests for passwords, one-time codes or payment details, malware lures;
- **`spam`**: unwanted advertising and bulk marketing that is not trying to steal anything;
- **`legitimate`**: everything else, including genuine notifications that look similar (real one-time codes, delivery updates,
  bank alerts).

Built on [mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base), Apache-2.0, ONNX files for CPU and the browser
(transformers.js) included. Useful for message filtering and moderation, and for AI agents that read email or chats (see also
our [prompt-injection guard](https://huggingface.co/Horizon-Labs/prompt-injection-guard-base) for attacks on the agent itself).

- Score: `P(fraud) + P(spam)` for "unwanted", or `P(fraud)` alone if marketing is acceptable. The default threshold is 0.5;
  raise it to cut false positives (see the false-positive rates below).
- `onnx/model_quantized.onnx` (int8 embeddings, 641 MB) gives the same top label as fp32 for 99.8% of 520 benchmark texts.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Horizon-Labs/phishing-scam-detector-base", top_k=None)
print(clf("Your parcel could not be delivered. Pay the 1.99 EUR customs fee within 24h: dhl-redelivery.example.com"))
# [[{'label': 'fraud', 'score': ...}, {'label': 'legitimate', 'score': ...}, {'label': 'spam', 'score': ...}]]
```

transformers.js:

```js
import { pipeline } from "@huggingface/transformers";
const clf = await pipeline("text-classification", "Horizon-Labs/phishing-scam-detector-base", { dtype: "q8" });
console.log(await clf("Ihr Konto wurde gesperrt. Bestätigen Sie Ihre Daten: sparkasse-sicher.example.de", { top_k: null }));
```

## Evaluation

Public spam / phishing / smishing test sets, used only for evaluation. Every model is scored the same way (`code/`): AUC of its
"unwanted" probability (for this model `P(fraud) + P(spam)`), and F1 and false-positive rate at 0.5.

- **Real smishing in other languages** (the main test): Bengali / Banglish / code-mixed SMS
  ([shariul-islam/bengali-sms-smishing-dataset](https://huggingface.co/datasets/shariul-islam/bengali-sms-smishing-dataset), test split; smishing and promotions count as unwanted),
  Mozambican Portuguese SMS and Facebook messages ([MOZNLP/MOZ-Smishing](https://huggingface.co/datasets/MOZNLP/MOZ-Smishing)),
  Korean SMS ([jmjmjm3/kor-smishing-message](https://huggingface.co/datasets/jmjmjm3/kor-smishing-message)), up to 1,000 each.
- **English emails**: [zefang-liu/phishing-email-dataset](https://huggingface.co/datasets/zefang-liu/phishing-email-dataset) and
  [SetFit/enron_spam](https://huggingface.co/datasets/SetFit/enron_spam) test; **English SMS**: the UCI SMS Spam Collection; and its
  machine translation into 21 languages ([dbarbedillo/SMS_Spam_Multilingual_Collection_Dataset](https://huggingface.co/datasets/dbarbedillo/SMS_Spam_Multilingual_Collection_Dataset)).
  These classic sets are in or near the training data of several English baselines (marked in the note column), which explains
  their near-perfect English scores.

| model | licence | real smishing, 3 languages: AUC | F1 @ 0.5 | false-positive rate @ 0.5 | phishing & spam emails (English): AUC | SMS spam (English): AUC | SMS spam, 21 languages (machine-translated): AUC | note |
|---|---|---|---|---|---|---|---|---|
| **this model** (307M) | Apache-2.0 | 0.925 | 0.768 | 0.110 | 0.978 | 0.978 | 0.950 | multilingual |
| [cybersectony/phishing-email-detection-distilbert_v2.4.1](https://huggingface.co/cybersectony/phishing-email-detection-distilbert_v2.4.1) (67M) | Apache-2.0 | 0.606 | 0.715 | 0.880 | 0.999 | 0.759 | 0.664 | English emails and URLs |
| [ptouch/phishing-distilbert-cyber207](https://huggingface.co/ptouch/phishing-distilbert-cyber207) (67M) | none given | 0.485 | 0.664 | 0.738 | 0.991 | 0.892 | 0.720 | English |
| [ealvaradob/bert-finetuned-phishing](https://huggingface.co/ealvaradob/bert-finetuned-phishing) (110M) | Apache-2.0 | 0.797 | 0.763 | 0.672 | 1.000 | 0.999 | 0.965 | English emails, SMS, URLs, websites |
| [mshenoda/roberta-spam](https://huggingface.co/mshenoda/roberta-spam) (125M) | MIT | 0.803 | 0.823 | 0.332 | 0.996 | 0.999 | 0.974 | English spam messages |
| [mrm8488/bert-tiny-finetuned-sms-spam-detection](https://huggingface.co/mrm8488/bert-tiny-finetuned-sms-spam-detection) (4M) | none given | 0.834 | 0.779 | 0.541 | 0.450 | 0.994 | 0.964 | trained on the UCI SMS set (in-domain) |
| [mrm8488/bert-tiny-finetuned-enron-spam-detection](https://huggingface.co/mrm8488/bert-tiny-finetuned-enron-spam-detection) (4M) | Apache-2.0 | 0.735 | 0.709 | 0.959 | 0.983 | 0.735 | 0.785 | trained on Enron spam (in-domain) |
| Qwen/Qwen3.8-27B (teacher, prompted) (27B) | Apache-2.0 | 0.945 | 0.878 | 0.128 | 0.996 | 0.986 | 0.969 | our teacher, for reference |

- The table shows the released checkpoint. Two training seeds: real-smishing AUC 0.916 / 0.925,
  false-positive rate 0.122 / 0.110.
- On real smishing in Bengali, Portuguese and Korean this model ranks messages much better (AUC) and flags far fewer normal
  messages than the English models (their false-positive rates there: 0.33-0.96). Its F1 at 0.5 is lower than roberta-spam's
  because it is conservative at 0.5: on the Portuguese set it catches only 32% of smishing messages at
  0.5 (Bengali 95%, Korean 93%). Lower the threshold if missed scams cost more than false alarms.
- On the classic English sets it is slightly behind models trained on them.
- Machine-translated SMS by language (AUC): ar 0.952, bn 0.924, de 0.967, es 0.974, fr 0.975, hi 0.940, id 0.965, ja 0.949, jv 0.911, ko 0.937, mr 0.924, no 0.968, pa 0.881, pt 0.971, ru 0.958, sv 0.972, tr 0.962, uk 0.957, ur 0.947, zh 0.959.
- The `spam` / `fraud` split comes from our teacher; the public sets only distinguish wanted from unwanted, so only that is measured.

Per set:

| set | AUC | F1 @ 0.5 | false-positive rate | recall |
|---|---|---|---|---|
| Bengali / Banglish / English SMS (smishing + promotions) | 0.979 | 0.946 | 0.112 | 0.952 |
| Mozambican Portuguese SMS and Facebook (smishing) | 0.840 | 0.450 | 0.096 | 0.319 |
| Korean SMS (smishing) | 0.957 | 0.909 | 0.120 | 0.934 |
| phishing vs safe emails (English) | 0.978 | 0.916 | 0.112 | 0.943 |
| Enron spam vs ham (English) | 0.978 | 0.934 | 0.076 | 0.944 |
| UCI SMS spam (English) | 0.978 | 0.900 | 0.063 | 0.872 |

## Training

- **Messages**: 98,379 synthetic SMS, emails, chat, social-media and push messages in about 70 languages written by
  Qwen3.8-27B (Apache-2.0): per prompt 4 legitimate (half of them genuine notifications that resemble phishing), 2 spam and 4 fraud
  of one of 20 scam types (parcel fees, bank verification, tax refunds, prizes, fake jobs, crypto, romance, "new number", CEO fraud,
  fake login alerts, OTP theft, toll fines, ...). Plus 59,403 ordinary web snippets in 92 languages from
  [FineWeb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) / [FineWeb](https://huggingface.co/datasets/HuggingFaceFW/fineweb)
  (ODC-BY), so normal text stays normal. No test-set messages were used.
- **Labels**: Qwen3.8-27B (prompted) scored every text as legitimate / spam / fraud; the model learns the teacher's probabilities
  (soft labels). Checkpoint chosen on held-out teacher-labelled data.
- mmBERT-base, max length 384 tokens, learning rate 3e-5. Code: `code/` in this repository.

## Limitations

- Not a complete security product: it sees only the text, not sender reputation, links, attachments or headers. Use it as one
  signal among others, and review decisions that matter.
- False positives remain (about 11% of normal messages on the smishing test sets at 0.5), especially for genuine
  notifications with links and for promotions; tune the threshold on your own traffic.
- Trained on synthetic messages: new scam scripts, very long emails (truncated at 384 tokens) and rare languages are weaker. The
  Portuguese smishing set is the hardest here (AUC 0.840; at 0.5 it misses most of those messages).
