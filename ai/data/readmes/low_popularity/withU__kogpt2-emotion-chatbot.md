# KoGPT2-emotion-chatbot
kogpt2 on hugging face Transformers for Psychological Counseling
- [full project link](https://github.com/jiminAn/Capstone_2022)

## how to use
```
from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast

model = GPT2LMHeadModel.from_pretrained("withU/kogpt2-emotion-chatbot")
tokenizer = PreTrainedTokenizerFast.from_pretrained("withU/kogpt2-emotion-chatbot")

input_ids = tokenizer.encode("안녕", add_special_tokens=False, return_tensors="pt")
output_sequences = model.generate(input_ids=input_ids, do_sample=True, max_length=80, num_return_sequences=4)
for generated_sequence in output_sequences:
    generated_sequence = generated_sequence.tolist()
    print("GENERATED SEQUENCE : {0}".format(tokenizer.decode(generated_sequence, clean_up_tokenization_spaces=True)))
```
## dataset finetuned on
- [wellness dataset](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-006)
- [emotion corpus of conversations](https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-010)
- [chatbot data](https://jeongukjae.github.io/tfds-korean/datasets/korean_chatbot_qa_data.html)
## references
- [WelllnessConversation-LanguageModel](https://github.com/nawnoes/WellnessConversation-LanguageModel)
- [KoGPT2: SKT-AI](https://github.com/SKT-AI/KoGPT2)