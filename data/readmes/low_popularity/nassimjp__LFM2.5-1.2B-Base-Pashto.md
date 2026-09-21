---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE

language:
  - en
  - ar
  - zh
  - fr
  - de
  - ja
  - ko
  - es
  - ps

pipeline_tag: text-generation

tags:
  - liquid
  - lfm2.5
  - edge
  - pashto

base_model: LiquidAI/LFM2.5-1.2B-Base
---


## **2️⃣ TOKENIZER**

```python
# ======================================================
# 2️⃣ TOKENIZER
# ======================================================
PASHTO_ATOMS = ["ښ","څ","ځ","ڼ","ږ","ډ","ټ","ړ","ئ","ې","ۍ","ګ",
                "ک","ی","گ","چ","ژ","پ","ۀ","أ","إ","آ","ؤ","ء","ٱ",
                "ٹ","ڈ","ڑ","ں","ھ","ے","ۓ","۰","۱","۲","۳","۴","۵","۶","۷","۸","۹"]
```

---

## **Training Requirements**

### **Continued Pretraining (CPT)**
Requires large‑scale Pashto corpora, deduped and domain‑balanced.

### **Supervised Fine‑Tuning (SFT)**
Requires high‑quality Pashto instruction datasets in chat format.

---

## **Thanks**

Special thanks to the open‑source community and Pashto NLP contributors whose work made this model possible.

---

## **Citation**

```
@article{liquidai2025lfm2,
  title={LFM2 Technical Report},
  author={Liquid AI},
  journal={arXiv preprint arXiv:2511.23404},
  year={2025}
}
```
## 📄 License

This model is released under the same license terms as the base model
(**LiquidAI/LFM2.5-1.2B-Base**).  
Please refer to the original model card for detailed license information.
