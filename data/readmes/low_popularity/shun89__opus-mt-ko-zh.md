---
license: apache-2.0
language:
- ko
- zh
metrics:
- bleu
pipeline_tag: translation
---


from transformers import MarianMTModel, MarianTokenizer

model = MarianMTModel.from_pretrained(“shun89/opus-mt-ko-zh”)

tokenizer = MarianTokenizer.from_pretrained(“shun89/opus-mt-ko-zh”)

text = '오피스 빌딩이 너무 현대적이라 사무 환경이 편안하네요!'

inputs = tokenizer(texts, return_tensors="pt",padding=True, truncation=True, max_length=256)

outputs = model.generate(**inputs)

result= " ".join(tokenizer.batch_decode(outputs, skip_special_tokens=True))

print("待翻译语句：",text)

print("翻译结果：",result)

