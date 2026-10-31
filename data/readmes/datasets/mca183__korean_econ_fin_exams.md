---
language:
- ko
---

---
language:
- ko
---

# Korean Economics/Finance Exams Dataset

**Description**
---------------

This dataset contains a collection of Korean economic and financial exams, providing a valuable resource for natural language processing (NLP) tasks such as question answering, text classification, and language modeling.

**Dataset Details**
-------------------

* **Language**: Korean
* **Format**: JSON
* **Size**: 120 kB (1015 questions)
* **License**: COPYRIGHT (C) 2019 BY KICE

**Data Structure**
-----------------

Each example in the dataset consists of a JSON object with the following keys:

- `language`: Specifies the language code.
- `country`: Indicates the country.
- `file_name`: The name of the PDF file associated with this question
- `source`: The URL source of the question
- `license`: Copyright information
- `level`: Specifies the educational level.
- `category_en`: The category in English.
- `category_original_lang`: The category in the original language (Korean)
- `original_question_num`: The original question number.
- `question`: The full text of the question in Korean.
- `options`: An array containing four answer options
- `answer`: The correct answer


**Example**
------------

Here's an example of a single data point in the dataset:
```json
{
    "language": "kr",
    "country": "korea",
    "file_name": "프린트 _ 생글생글.pdf",
    "source": "https://sgsg.hankyung.com/article/2024021682211",
    "license": "COPYRIGHT (C) 2019 BY KICE",
    "level": "college",
    "category_en": "Economics/Finance",
    "category_original_lang": "경제·금융 상식 퀴즈 O X",
    "original_question_num": 3,
    "question": "불법 거래가 이뤄지는 시장을 OO마켓, 미국 증시가 대폭락한 1987년 10월 19일을 OO먼데이라고 한다. OO에 공통으로 들어갈 색상은?",
    "options": [
        "레드",
        "블루",
        "화이트",
        "블랙"
    ],
    "answer": 4
},
```

**Use Cases**
-------------

This dataset can be used for a variety of NLP tasks, including:

* Question answering: train a model to answer economic and financial questions
* Text classification: classify exam questions into categories (e.g., economics, finance)
* Language modeling: train a language model on the dataset to generate text related to economics and finance

**Citation**
------------

If you use this dataset in your research, please cite it as follows:

Michael Chang. (2024). Korean Econ Fin Exams Dataset. Retrieved from [생글+: 경제·금융 상식 퀴즈](https://sgsg.hankyung.com/sgplus/quiz)

**Acknowledgments**
-----------------

- Special thanks to Shivalika (shivalikasingh) and Harsha (majormelancholy) from Cohere For AI community for providing me the data to process, and letting me contribute to the global-exams project for Aya's benchmark.
