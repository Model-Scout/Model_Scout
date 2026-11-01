---
license: apache-2.0
language:
- ko
---

## Usage
```bash
pip install datasets
```

```python
from datasets import load_dataset

dataset = load_dataset("dev7halo/korean-mcfaq")
```

```
DatasetDict({
    train: Dataset({
        features: ['Unnamed: 0', '제목', '등록일', '질문', '답변'],
        num_rows: 2452
    })
})
```

```
# dataset['train'][0]
{'Unnamed: 0': 0,
 '제목': "'언젠가', '언젠가는'의 표현",
 '등록일': '2019. 12. 6. ',
 '질문': '\n\t\t \n\t\t \n\t\t"저는 언젠가 간호사가 되고 싶어요."와 같이 쓸 때, 미래의 불특정한 때를 나타내는 \'언젠가\'라는 단어를 \'언젠가는\'이라고 써도 되나요? \'언젠가\'가 표준어인 것 같은데, 뒤에 \'는\'을 쓴 \'언젠가는\'이 더 많이 쓰이는 것 같아요.\n\t\t \n\t\t \n\t',
 '답변': "\n\t\t\t \n\t\t\t \n\t\t\t\xa0'미래의 어느 때에 가서는'을 뜻하는 부사 '언젠가'를 강조하기 위하여, '강조'의 뜻을 나타내는 보조사 '는'을 붙여 '언젠가는'과 같이 쓸 수 있습니다.\n\t\t\t \n\t\t"}
```

# Github

[Github](https://github.com/HaloKim/korean-mcfaq)