---
language:
- ko
---
# kgrammar-testset
The [kgrammar-testset](https://github.com/davidkim205/keval/blob/master/datasets/pairs_kgrammar_test_962.jsonl) is a dataset designed for training and validating the [kgrammar](https://huggingface.co/collections/davidkim205/keval-2-67ac5400f5eef4984cc5dbbb) model, which identifies grammatical errors in Korean text and outputs the number of detected errors.

The kgrammar-testset was generated using GPT-4o. To create error-containing documents, a predefined prompt was used to introduce grammatical mistakes into responses when given a question. The dataset is structured to ensure a balanced distribution, consisting of 50% general questions, 25% math-related questions, 25% coding-related questions.

This composition helps prevent mathematical expressions and code snippets from being mistakenly identified as grammatical errors.
~~~
예시와 같이 다음 질문에 한글 외 문자가 포함된 문장으로 답변하세요. 태국어, 영어, 러시아어 등 다양한 언어를 무작위로 선택하세요.
## 예시
저는 사람입니다. 저는 100年의 경험을 가지고 있습니다. 저는 무엇이든 can do it! 저는 제가 무엇을 하는지 知道합니다.

{질문}
~~~

## kgrammar-testset Structure
The kgrammar-testset is stored in JSONL format and consists of 80 JSON objects. Each JSON object includes the following keys.
- **id**: A unique identifier representing the sequence number of the data entry within the dataset.
- **inaccuracy**: The ground truth label indicating the number of grammatical errors in the given input text.
- **pairs**
    - **prompt**: A predefined instruction that requests error detection and specifies the output format.
    - **input**: The text provided for grammatical error detection.
```json
{
  "id": 1,
  "inaccuracy": 1,
  "pairs": [
    {
      "prompt": "한국어 문맥상 부자연스러운 부분을 찾으시오. 오류 문장과 개수는 <incorrect grammar> </incorrect grammar> tag, 즉 <incorrect grammar> - 오류 문장과 설명 </incorrect grammar> 안에 담겨 있으며, <wrong count> </wrong count> tag, 즉 <wrong count> 오류 개수 </wrong count> 이다.",
      "input": "가장 적은 S등급을 받은 통신사는 LG유플러스 입니다. 그들의 S등급 지역은 243곳でした. 이는 다른 두 통신사에 비해 적습니다."
    }
  ]
}
```
