---
language:
- ko
---
# keval_test
The [keval-testset](https://github.com/davidkim205/keval/blob/master/datasets/pairs_keval_test_2098.jsonl) is a dataset designed for training and validating the [keval](https://huggingface.co/davidkim205/keval-2-1b) model.
The keval model follows the [LLM-as-a-judge](https://huggingface.co/spaces/davidkim205/ko-bench) approach, which evaluates LLMs by assessing their responses to prompts from the [ko-bench](https://huggingface.co/spaces/davidkim205/ko-bench) dataset. In other words, the keval model assigns scores to LLM-generated responses based on predefined evaluation criteria.
The keval-testset serves as a crucial resource for training and validating the keval model, enabling precise benchmarking and comparison of various LLMs.

## keval-testset Structure 
The **keval-testset** is stored in JSONL format and consists of 22 JSON objects. Each JSON object contains the following keys.
- **id**: A unique identifier representing the sequence number of the data entry within the dataset.
- **score**: The ground truth evaluation score assigned to the LLM’s response. The score is an integer ranging from 0 to 10 and serves as the label for training the keval model.
- **pairs**: A collection of elements used to generate and evaluate LLM responses based on ko-bench prompts. Each entry in pairs consists of 'The prompt given to the LLM', 'The selected question from the ko-bench dataset', 'The LLM-generated response to the given question'.
~~~
{
  "id": 1,
  "score": 0,
  "pairs": [
    {
      "prompt": "당신은 도움이 되는 어시스턴트입니다.",
      "input": "[지시]\n 공정한 심판으로서 아래에 표시된 사용자 질문에 대한 AI 어시스턴트의 응답 품질을 평가해주세요. 질문과 대답의 언어가 동일하지 않으면 무조건 0점입니다. 평가에서는 응답의 유용성, 관련성, 정확성, 깊이, 창의성, 상세함 등의 요소를 고려해야 합니다. 평가를 시작하기 전에 짧은 설명을 제공하세요. 가능한 한 객관적으로 평가하세요. 설명을 제공한 후 다음 형식을 엄격히 따라 1에서 10점 사이로 평가해야 합니다: \"[[rating]]\", 예를 들어: \"Rating: [[5]]\".\n\n[Question]\n다음과 같은 주가 기록을 바탕으로 2022년 매월 최고 및 최저 종가를 추출합니다. 결과를 각 월에 한 줄이 할당된 CSV 문자열로 반환합니다.\n 날짜, 시가, 고가, 저가, 종가, 거래량\n2022-01-01,150.02,155.28,148.50,153.80,15678900\n2022-01-02,154.32,157.25,153.48,156.25,19874500\n2022-02-01,160.50,163.28,159.50,161.80,14326700\n2022-02-02,161.80,164.25,161.30,163.90,17689200\n2022-03-01,165.40,168.35,163.10,166.80,16253400\n2022-03-02,167.00,169.85,165.50,168.20,19 568100\n\n[어시스턴트 답변의 시작]\nBased on the provided data, below is the CSV string with the highest and lowest closing prices for each month:\n\n```\n날짜,최고종가,최저종가\n2022-01,156.25,153.80\n2022-02,163.90,161.80\n2022-03,168.20,166.80\n```\n\nThis CSV string shows the highest and lowest closing prices for each month in 2022. The first column represents the month, the second column represents the highest closing price, and the third column represents the lowest closing price.\n[어시스턴트 답변의 끝]"
    }
  ]
}
~~~

