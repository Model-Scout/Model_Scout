---
dataset_info:
  features:
  - name: subreddit
    dtype: string
  - name: subreddit_id
    dtype: string
  - name: id
    dtype: string
  - name: link_id
    dtype: string
  - name: parent_id
    dtype: string
  - name: body
    dtype: string
  - name: created_utc
    dtype: timestamp[us]
  - name: ups
    dtype: int64
  - name: downs
    dtype: int64
  - name: score
    dtype: int64
  - name: author
    dtype: string
  - name: author_flair_text
    dtype: string
  - name: author_flair_css_class
    dtype: string
  - name: major_language
    dtype: string
  - name: korean_ratio
    dtype: float64
  - name: has_korean
    dtype: bool
  splits:
  - name: train
    num_bytes: 229757097
    num_examples: 589887
  download_size: 114982723
  dataset_size: 229757097
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
language:
- ko
- en
---

- Posts: [werty1248/Korea-Related-Reddit-posts](https://huggingface.co/datasets/werty1248/Korea-Related-Reddit-posts)

- **This dataset may contain aggressive content.**

### Source

- [Subreddit comments/submissions 2005-06 to 2024-12](https://academictorrents.com/details/1614740ac8c94505e4ecb9d88be8bed7b6afddd4?stats=True)
- Korea/Korean related **comments** only

### Subset

- Targeted subreddits
  - r/hanguk
  - r/Korea*
  - r/Korean*
  - r/kpop*
- Posts
  - Contains at least one Korean character in the selftext (body).
- Comments
  - Only comments that reply to Korean posts as defined above.

### Statistics

- Total data: 3.28TB
- Korea/Korean-related subreddit data: 3.66GB
  - 1,755,918 posts
  - 18,376,820 comments
- Posts including Korean character
  - 41,328 posts
- Posts written in Korean
  - 7,684 posts
- Comments reply to posts that including Korean character
  - 589,887 comments

### License

- **No license specified, the work may be protected by copyright.**
  - https://www.reddit.com/r/pushshift/comments/1akrhg3/separate_dump_files_for_the_top_40k_subreddits/

### Attribute
- subreddit: 레딧 채널명
- subreddit_id: 레딧 채널 id
- id: comment의 id
- link_id: post의 id
- parent_id: 상위 post/comment의 id
- body: 내용
- created_utc: 작성일시
- ups: 좋아요 수
- downs: 싫어요 수
- score: ups - downs ?
- author: 작성자
- major_language: 본문의 주요 언어
- korean_ratio: (한글 개수) / (한글 개수 + 알파벳 개수)
- has_korean: 본문에 한글 포함 여부 (항상 True)

```
@article{,
title= {Subreddit comments/submissions 2005-06 to 2024-12},
journal= {},
author= {Watchful1},
year= {},
url= {https://www.reddit.com/r/pushshift/comments/1itme1k/separate_dump_files_for_the_top_40k_subreddits/?},
abstract= {This is the top 40,000 subreddits from reddit's history in separate files. You can use your torrent client to only download the subreddit's you're interested in.
These are from the pushshift dumps from 2005-06 to 2024-12 which can be found here https://academictorrents.com/details/ba051999301b109eab37d16f027b3f49ade2de13
These are zstandard compressed ndjson files. Example python scripts for parsing the data can be found here https://github.com/Watchful1/PushshiftDumps
If you have questions, please reply to this reddit post or DM u/Watchful on reddit or respond to this post https://www.reddit.com/r/pushshift/comments/1akrhg3/separate_dump_files_for_the_top_40k_subreddits/},
keywords= {reddit},
terms= {},
license= {},
superseded= {}
}
```