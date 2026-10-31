---
license: mit
task_categories:
- translation
- token-classification
language:
- ko
- en
size_categories:
- 10K<n<100K
---
| Column Name        | Type                  | Description                          | 설명                         |
|--------------------|-----------------------|--------------------------------------|----------------------------|
| Form               | `str`                 | Registered word entry                | 단어                         |
| Part of Speech     | `str` or `None`       | Part of speech of the word in Korean | 품사                         |
| Korean Definition  | `List[str]`                 | Definition of the word in Korean     | 해당 단어의 한글 정의               |
| English Definition | `List[str]` or `None` | Definition of the word in English    | 한글 정의의 영문 번역본              |
| Usages             | `List[str]` or `None` | Sample sentence or dialogue          | 해당 단어의 예문 (문장 또는 대화 형식)    |
| Vocabulary Level   | `str` or `None`       | Difficulty of the word (3 levels)    | 단어의 난이도 ('초급', '중급', '고급') |
| Semantic Category  | `str` or `None`       | Semantic category of the word        | 단어 분류 (ex. '자연 > 기상 및 기후') |

For more information, visit:
- https://github.com/binjang/NIKL-dictionary-parser
- https://krdict.korean.go.kr/kor/mainAction