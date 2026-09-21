---
tags:
- summarization

language:
- ko

license: apache-2.0
---
[AI-HUB 도서자료 요약](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=93)
|model|sampling|ROUGE-1 (↑)|ROUGE-2 (↑)|ROUGE-L (↑)|
|:---:|:---:|:---:|:---:|:---:|
|-|-|-|-|-|
|ours|greedy|**49.87**|**34.44**|**41.65**|
|ainize/kobart-news|greedy|42.35|23.27|32.61|
|gogamza/kobart-summarization|greedy|39.92|25.26|33.86|
|noahkim/KoT5_new_summarization|greedy|40.75|19.60|29.44|

* **greedy** 는 최대길이 제한(max_length=256)과 repetition_penalty=2.0으로 단순 샘플링한 방법을 의미합니다.

More Information of [KoT5](https://bit.ly/3SrHq36)

