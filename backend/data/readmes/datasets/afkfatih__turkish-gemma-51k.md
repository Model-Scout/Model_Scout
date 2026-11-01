---
language:
- tr
license: apache-2.0
task_categories:
- text-generation
- question-answering
tags:
- turkish
- chat
- instruction-following
- gemma
- conversational
size_categories:
- 10K<n<100K
---

# Turkish Chat Dataset - Gemma Format

Bu dataset, Türkçe sohbet ve talimat takip etme görevleri için hazırlanmış 51.914 konuşma örneği içerir.

## 📊 Dataset Özeti

- **Dil:** Türkçe
- **Format:** Chat/Conversation
- **Örnek Sayısı:** 51,914
- **Kaynak:** [afkfatih/turkishdataset](https://huggingface.co/datasets/afkfatih/turkishdataset)

## 🎯 Kullanım Alanları

- Türkçe sohbet botları eğitimi
- Instruction-tuning
- Fine-tuning LLM modelleri (Gemma, Llama, vb.)
- Türkçe doğal dil anlama

## 📝 Format

Her örnek şu yapıya sahiptir:

```json
[
  {
    "role": "system",
    "content": "Sen 'Gemma 3' adında sıcak, içten ve anlayışlı bir asistansın."
  },
  {
    "role": "user",
    "content": "Bugün çok yorgunum, motive olamıyorum."
  },
  {
    "role": "assistant",
    "content": "Yorgun hissetmen normal 🫶 Belki biraz dinlen, sonra küçük bir adımla başla."
  }
]
```

## 🚀 Hızlı Başlangıç

```python
from datasets import load_dataset
import json

# Dataset'i yükle
dataset = load_dataset("YOUR_USERNAME/YOUR_DATASET_NAME")

# İlk örneği incele
print(json.dumps(dataset['train'][0], ensure_ascii=False, indent=2))
```

## 💻 Model Eğitimi İçin

```python
from datasets import load_dataset

# Dataset'i yükle
ds = load_dataset("YOUR_USERNAME/YOUR_DATASET_NAME", split="train")

# Unsloth, Transformers veya benzeri kütüphanelerle eğitim
# Her örnek zaten chat formatında
```

## 📋 Dataset İçeriği

Dataset aşağıdaki türde konuşmaları içerir:
- Genel sohbet
- Soru-cevap
- Talimat takibi
- Günlük konuşmalar
- Bilgi paylaşımı

## ⚖️ Lisans

Apache 2.0

## 🙏 Teşekkürler

Bu dataset [afkfatih/turkishdataset](https://huggingface.co/datasets/afkfatih/turkishdataset) kullanılarak oluşturulmuştur.

## 📧 İletişim

Sorularınız için issue açabilirsiniz.

