---
language:
  - multilingual
  - af
  - am
  - ar
  - as
  - az
  - be
  - bg
  - bn
  - br
  - bs
  - ca
  - cs
  - cy
  - da
  - de
  - el
  - en
  - eo
  - es
  - et
  - eu
  - fa
  - fi
  - fr
  - fy
  - ga
  - gd
  - gl
  - gu
  - ha
  - he
  - hi
  - hr
  - hu
  - hy
  - id
  - is
  - it
  - ja
  - jv
  - ka
  - kk
  - km
  - kn
  - ko
  - ku
  - ky
  - la
  - lo
  - lt
  - lv
  - mg
  - mk
  - ml
  - mn
  - mr
  - ms
  - my
  - ne
  - nl
  - 'no'
  - om
  - or
  - pa
  - pl
  - ps
  - pt
  - ro
  - ru
  - sa
  - sd
  - si
  - sk
  - sl
  - so
  - sq
  - sr
  - su
  - sv
  - sw
  - ta
  - te
  - th
  - tl
  - tr
  - ug
  - uk
  - ur
  - uz
  - vi
  - xh
  - yi
  - zh
pretty_name: All of Common Crawl News, 100+ languages, preprocessed and cleaned
task_categories:
- text-classification
- question-answering
- text-generation
- text2text-generation
size_categories:
- 100M<n<1B
tags:
- news
configs:
  - config_name: "default"
    data_files: "*.parquet"
  - config_name: "2016"
    data_files: "2016*"
  - config_name: "2017"
    data_files: "2017*"
  - config_name: "2018"
    data_files: "2018*"
  - config_name: "2019"
    data_files: "2019*"
  - config_name: "2020"
    data_files: "2020*"
  - config_name: "2021"
    data_files: "2021*"
  - config_name: "2022"
    data_files: "2022*"
  - config_name: "2023"
    data_files: "2023*"
  - config_name: "2024"
    data_files: "2024*"

---

This dataset is the result of processing all WARC files in the [CCNews Corpus](https://commoncrawl.org/blog/news-dataset-available), from the beginning (2016) to June of 2024.
The data has been cleaned and deduplicated, and language of articles have been detected and added. The process is similar to what HuggingFace's [DataTrove](https://github.com/huggingface/datatrove) does.

Overall, it contains about 600 million news articles in more than 100 languages from all around the globe.

For license information, please refer to [CommonCrawl's Terms of Use](https://commoncrawl.org/terms-of-use).

Sample Python code to explore this dataset:

```python
from datasets import load_dataset
from tqdm import tqdm

# Load the news articles **crawled** in the year 2016 (but not necessarily published in 2016), in streaming mode
dataset = load_dataset("stanford-oval/ccnews", name="2016", streaming=True) # `name` can be one of 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024

# Print information about the dataset
print(dataset)

# Iterate over a few examples
print("\nFirst few examples:")
for i, example in enumerate(dataset["train"].take(5)):
    print(f"Example {i + 1}:")
    print(example)
    print()

# Count the number of articles (in 2016)
row_count = 0
for _ in tqdm(dataset["train"], desc="Counting rows", unit=" rows", unit_scale=True, unit_divisor=1000):
    row_count += 1

# Print the number of rows
print(f"\nTotal number of articles: {row_count}")

# Extract all Arabic (ar) articles
for row in tqdm(dataset["train"], desc="Extracting articles", unit=" rows", unit_scale=True, unit_divisor=1000):
    if row["language"] == "ar":
        print(row)
```