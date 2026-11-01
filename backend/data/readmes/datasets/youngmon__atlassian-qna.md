---
license: mit
task_categories:
- question-answering
language:
- en
- ko
- zh
- ja
- es
- ru
pretty_name: Question and Answer for Atlassian Products
size_categories:
- 100K<n<1M
---

### 📄 Question and Answer for Atlassian Products

#### Dataset Sources
- [Atlassian Community](https://community.atlassian.com/)

#### Data Description

The dataset primarily includes **questions**, **answers**, **tags**, and **URLs**.

- **Questions** contain the author, title, and content of the post.
- **Answers** include usage instructions, solutions, and other information provided by engineers and users.
- **Tags** represent the categories or topics of the post.
- **URLs** provide links to the original documents.


#### Dataset Structure

- `question`: The main question posted by the user, including the author, title, and content of the post.
  - `author`: The name of the person who asked the question.
  - `title`: The title of the question.
  - `body`: The content or body of the question.

- `answers`: A list of answers provided by other users or engineers, with potential follow-up comments.
  - `author`: The name of the person who answered.
  - `body`: The body of the answer.
  - `comments`: A list of comments on the answer.
    - `author`: The name of the person who commented.
    - `body`: The content of the comment.

- `tags`: A list of tags associated with the post.
- `url`: The URL link to the original document or post.

```
{
  "question" : {
      "author",
      "title",
      "body"
  },
  "answers" : [
    {
      "author",
      "body",
      "comments" : [
        {
          "author",
          "body"
        }
        ...
      ]
    }
    ...
  ],
  "tags" : [ tag ... ],
  "url" : string
}
```

#### How to Use

```python
from datasets import load_dataset

dataset = load_dataset("youngmon/atlassian-qna")
```

#### License
- MIT