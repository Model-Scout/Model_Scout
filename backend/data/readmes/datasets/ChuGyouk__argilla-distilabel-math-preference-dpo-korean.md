---
license: apache-2.0
language:
  - en
  - ko
---

# Dataset Information

This is a gpt-4o-2024-08-06 Korean translated-version of [argilla/distilabel-math-preference-dpo](https://huggingface.co/datasets/argilla/distilabel-math-preference-dpo?row=13). 

I used OpenAI BATCH API with prompt below, temperature=0.0, max_tokens=4000, seed=0. Total cost was 11.71$.

Note that for the 1317th data, because it did not satisfy the format given in the instruction, I modified it. (For example, for <translated_question> mark, even this was translated as <의문>.)

## Prompt
>You are tasked with translating English text into Korean for Direct Preference Optimization training data. This data consists of a question, a chosen response, and a rejected response. Your goal is to accurately translate the content while preserving the meaning and structure of the original text.
>
>Here is the content to translate:
>
>Question:
>\<question\>
>{QUESTION}
>\</question\>
>
>Chosen Response:
>\<chosen_response\>
>{CHOSEN_RESPONSE}
>\</chosen_response\>
>
>Rejected Response:
>\<rejected_response\>
>{REJECTED_RESPONSE}
>\</rejected_response\>
>
>Please follow these steps:
>
>1. Translate the question from English to Korean.
>2. Translate the chosen response from English to Korean.
>3. Translate the rejected response from English to Korean.
>
>Follow these guidelines when translating:
>
>1. Translate the text from English to Korean accurately, maintaining the original meaning and tone.
>2. Do not translate mathematical expressions or equations. Leave them as they are in the original text.
>3. Preserve any formatting, such as white spaces, line breaks or bullet points, in your translation.
>4. Maintain the distinction between the chosen response and the rejected response in your translation. This difference should be clear in the Korean version as well.
>
>Provide your translation in the following format:
>
>\<translated_question\>
>[Insert Korean translation of the question here]
>\</translated_question\>
>
>\<translated_chosen_response\>
>[Insert Korean translation of the chosen response here]
>\</translated_chosen_response\>
>
>\<translated_rejected_response\>
>[Insert Korean translation of the rejected response here]
>\</translated_rejected_response\>
>
>Ensure that the distinction between the chosen and rejected responses remains clear in your translation. Also, Ensure that the difference between the chosen response and the rejected response remains clear in the Korean translation. The nuances that make one response preferred over the other should be preserved. If there are any culturally specific references or idioms that don't have a direct Korean equivalent, provide the closest appropriate translation and add a brief explanation in parentheses if necessary.

