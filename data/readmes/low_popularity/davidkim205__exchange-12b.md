---
language:
- ko
base_model:
- google/gemma-3-12b-it
library_name: transformers
---

# davidkim205/exchange-12b
The **exchange-12b** model is an exchange rate prediction model that maximizes exchange rate prediction performance by applying `Supervised Fine-Tuning (SFT)` and `Direct Preference Optimization (DPO)` technologies to **Google's Gemma3 (12B)** architecture.
The exchange-12b model analyzes factors affecting exchange rates based on Prompt and Foreign Exchange Market-Related Data (exchange rate data, key economic indicator data, news data) and predicts the exchange rate for the next day. It predicts the USD/KRW exchange rate and outputs the exchange rate prediction results in CSV format.
What makes this model different is that it is built on LLM (Large Language Model), which allows it to provide insight into the future of the uncertain forex market. In addition, it effectively processes and analyzes complex and diverse financial data, while integrating various unstructured data sources in real time to reflect the ever-changing foreign exchange market situation, enabling faster and more accurate exchange rate predictions than the existing method of direct human analysis and prediction.

## Model Details
- **Base Model**: [google/gemma-3-12b-it](https://huggingface.co/google/gemma-3-12b-it)
- **Base Model Release Date**: March 12, 2025
- **Context Length**: 128k
- **License**: [gemma](https://ai.google.dev/gemma/terms)
- **Model Type**: Text Generation
- **Fine-Tuning Techniques**
    - SFT (Supervised Fine-Tuning) Trained on diverse market data to improve the model's predictive accuracy, allowing for a more precise reflection of exchange rate fluctuation patterns.
    - DPO (Direct Preference Optimization) Optimized the model's predictions based on user preferences to enhance usability in practical scenarios.

## Usage Application Form
To use this model, please complete the application form and submit it via email [[davidkim205@gmail.com](mailto:davidkim205@gmail.com)]. Access will be granted after your application is reviewed and approved.
We appreciate your cooperation and look forward to assisting you.
```
1. **Name:**
   - (e.g., John Doe)
2. **Date of Birth:**
   - (e.g., January 1, 1990)
3. **Affiliation:**
   - Are you applying as a company or an individual? [ ] Company  [ ] Individual
   - Company Name (if applicable):
   - Department (if applicable):
4. **Position/Role:**
   - (e.g., Data Scientist, Researcher, etc.)
5. **Contact Information:**
   - Email:
   - Phone Number:

6. **Purpose of Use:**
   - (e.g., Research and Development, Commercial use, Educational purposes, etc.)

7. **Detailed Reason for Use:**
   - 1. Name and version of the model you wish to use:
   - 2. Reason for selecting this model:
   - 3. Objectives to achieve using this model:
   - 4. Expected use cases (please describe in as much detail as possible):

8. **Data Security and Ethical Use Plan:**
   - (Please describe your plans for data protection and ethical use.)
```

## Usage
```
from transformers import AutoTokenizer, Gemma3ForConditionalGeneration
import torch

tokenizer = AutoTokenizer.from_pretrained("davidkim205/exchange-12b")
model = Gemma3ForConditionalGeneration.from_pretrained(
    "davidkim205/exchange-12b",
    device_map="auto",
    torch_dtype=torch.bfloat16,
)

text="""{주어진 다양한 금융 데이터와 뉴스 내용을 통해 24시간 USD 환율 데이터를 예측하시오. CSV 형식으로 Date,Name,Open,High,Low,Close으로 예측 결과를 제공하시오.

## USD Data
Date,Name,Open,High,Low,Close
2025-02-25,USD,1428.4,1435.0,1426.7,1433.1
2025-02-26,USD,1433.1,1436.4,1428.9,1436.3
2025-02-27,USD,1436.3,1447.3,1432.9,1446.3

## DOW Data
Date,Name,Open,High,Low,Close
2025-02-25,DOW,43467.0,43734.4,43302.6,43313.6
2025-02-26,DOW,43313.6,43858.7,43283.0,43813.8
2025-02-27,DOW,43813.8,43879.9,43318.9,43809.3

## KOSDAQ Data
Date,Name,Open,High,Low,Close
2025-02-25,KOSDAQ,766.8,773.9,765.3,769.0
2025-02-26,KOSDAQ,769.0,774.2,766.7,774.1
2025-02-27,KOSDAQ,774.1,776.6,760.1,760.1

## 2025-02-27 News
1. **EUR/USD**: 유로/달러 환율은 1.0500 아래에서 유지되고 있으며, 트럼프의 EU 관세 부과는 예상된 일이었다.  
2. **CNY/USD (위안화)**: 중국 중앙은행(PBoC)은 위안화 환율을 달러당 7.1740으로 조정.  
3. **GBP/USD (영국 파운드)**: 파운드/달러 환율은 1.2685를 기록하며 2025년 최고 수준에 도달했으나, 조정 가능성이 있다.  
4. **코스피 및 원/달러 환율 동향** - 코스피 지수 0.73% 하락, 원/달러 환율 0.67% 상승하며 1443.0원에 마감.  
5. **트럼프 관세 발언으로 인한 환율 변동** - 트럼프의 EU 관세 부과 발언으로 달러 강세, 원/달러 환율 9.9원 상승.  
}"""

messages = [
    {"role": "user", "content": text},
]
input_ids = tokenizer.apply_chat_template(messages, return_tensors="pt", return_dict=True).to("cuda")

outputs = model.generate(**input_ids, max_new_tokens=256)
print(tokenizer.decode(outputs[0]))
```
```
Date,Name,Open,High,Low,Close
2025-02-28,USD,1446.3,1463.8,1445.4,1461.8
```

## Evaluation
### Ranking
Ranking refers to the process of ordering multiple values to assess their relative magnitude. The following table ranks the accuracy of currency predictions, calculated based on the Mean Absolute Percentage Error (MAPE) between the predicted High and Low values from various banks and models and the actual USD exchange rates for March 2025. MAPE provides a standardized measure of error, where lower values indicate higher prediction accuracy.

To evaluate the model’s performance under different data conditions, we compared results using exchange rate data from Yahoo Finance, KEB Hana Bank, and SMBS (Seoul Money Brokerage Services). The `Average` column represents the overall average MAPE across all data sources(Yahoo Finance, KEB Hana Bank, SMBS). The `Yahoo Finance`, `KEB Hana Bank` and `SMBS` columns represent the average MAPE for High and Low values calculated using each respective data source.

|     Rank      | Site                                                                                                                                                                                                                               |    Average    | Yahoo Finance | KEB Hana Bank |     SMBS      |
|       -       | -                                                                                                                                                                                                                                  |       -       |       -       |       -       |       -       |
|       1       | [Korea Trade Insurance Corp.](https://www.ksure.or.kr/rh-fx/cntnts/i-505/web.do)                                                                                                                                                   |     0.18      |     0.17      |     0.19      |     0.18      |
|       2       | [**exchange-12b**](https://huggingface.co/davidkim205/exchange-12b)                                                                                                                                                                    |     0.19      |     0.17      |     0.21      |     0.20      |
|       3       | [Shinhan Bank](https://bank.shinhan.com/index.jsp#020501040100)                                                                                                                                                                    |     0.20      |     0.19      |     0.20      |     0.20      |
|       4       | [iM Bank](https://www.imbank.co.kr/cms/dev/fpm/ebz_fnm_fne06.html)                                                                                                                                                                 |     0.21      |     0.20      |     0.23      |     0.21      |
|       4       | [KOOKMIN BANK](https://obank.kbstar.com/quics?page=C101426#loading)                                                                                                                                                                |     0.21      |     0.19      |     0.23      |     0.21      |
|       4       | [Woori Bank](https://spot.wooribank.com/pot/Dream?withyou=FXXRT0027)                                                                                                                                                               |     0.21      |     0.19      |     0.23      |     0.21      |
|       7       | [exchange-8b](https://huggingface.co/davidkim205/exchange-8b)                                                                                                                                                                      |     0.22      |     0.21      |     0.24      |     0.22      |
|       8       | [exchange-3b](https://huggingface.co/davidkim205/exchange-3b)                                                                                                                                                                      |     0.23      |     0.23      |     0.23      |     0.23      |
|       8       | [KEB Hana Bank](https://biz.kebhana.com/cont/support/support10/support101/index.jsp)                                                                                                                                               |     0.23      |     0.22      |     0.23      |     0.24      |
|       8       | [Toss Securities](https://news.einfomax.co.kr/news/articleList.html?sc_area=A&view_type=sm&sc_word=%5B%EC%98%A4%EB%8A%98+%EC%99%B8%ED%99%98%EB%94%9C%EB%9F%AC+%ED%99%98%EC%9C%A8+%EC%98%88%EC%83%81%EB%A0%88%EC%9D%B8%EC%A7%80%5D) |     0.23      |     0.22      |     0.24      |     0.23      |
|      11       | [exchange-1b](https://huggingface.co/davidkim205/exchange-1b)                                                                                                                                                                  |     0.25      |     0.25      |     0.26      |     0.24      |

_More detailed Evaluation Results can be found in the [Technical Report](https://davidkim205.github.io/ai_exchange_dealer.html)._
