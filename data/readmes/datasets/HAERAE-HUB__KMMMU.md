---
language:
- ko
size_categories:
- 1K<n<10K
license: cc-by-nc-4.0
---

# KMMMU (Korean MMMU)

> technical report https://arxiv.org/abs/2604.13058

> link to evaluation tutorial! https://github.com/HAE-RAE/KMMMU 

KMMMU is a Korean version of MMMU: a multimodal benchmark designed to evaluate **college-/exam-level reasoning** that requires combining **images + Korean text**.

This dataset contains **3,466** questions collected from Korean exam sources including:

- Civil service recruitment exams
- National Technical Qualifications
- National Competency Standard (NCS) exams
- Academic Olympiads

## Key statistics

- **Total questions:** 3,466
- **Total images:** 3,628
- **Questions with in-image text:** 2,550  
  (images contain text such as Korean or other languages)
- **Questions without in-image text:** 1,078
- **Korean-specific questions:** 300  

---

# Load the dataset

```python
from datasets import load_dataset

ds = load_dataset(
    "HAERAE-HUB/KMMMU",
    data_files="kmmmu.csv",
)

df = ds["train"].to_pandas()
df.head()
```


---
# Dataset Structure

Each row in the dataset contains:

- question: The problem statement (Korean)
- answer: The gold answer
- question_type: Question type category
- image_link: A list (string format) of image URLs associated with the question
(Some questions contain multiple images.)


---
# Loading Images

The image_link field stores a list of full image URLs in string format.
It must be parsed before use.

```python
import requests
from PIL import Image
from io import BytesIO

df_images = []
for _,row in df.iterrows():
    images = []
    
    for link in eval(row.image_link):
        response = requests.get(link, timeout=30)
        image = Image.open(BytesIO(response.content)).convert("RGB")
        images.append(image)

    df_images.append(images)
```


### Point of Contact
For any questions contact us via the following email:)
```
naa012@cau.ac.kr, guijin.son@snu.ac.kr
```