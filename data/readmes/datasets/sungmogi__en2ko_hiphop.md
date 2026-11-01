---
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: test
    path: data/test-*
  - split: valid
    path: data/valid-*
dataset_info:
  features:
  - name: id
    dtype: int64
  - name: translation
    struct:
    - name: en
      dtype: string
    - name: ko
      dtype: string
  splits:
  - name: train
    num_bytes: 5061272.804687347
    num_examples: 46158
  - name: test
    num_bytes: 281254.92317741335
    num_examples: 2565
  - name: valid
    num_bytes: 281145.272135239
    num_examples: 2564
  download_size: 4172120
  dataset_size: 5623673
task_categories:
- translation
language:
- en
- ko
pretty_name: en2ko_hiphop
size_categories:
- 10K<n<100K
---
# Dataset Card for "en2ko_hiphop"

## Copyright Disclaimer

The dataset "en2ko_hiphop" was curated from publicly available sources and is believed to be in the public domain. The translations provided in this dataset are the work of volunteers and members of the community, and they have been collected and curated to facilitate research and analysis. However, it is important to acknowledge that copyright issues cannot be entirely ruled out. Therefore, users of the dataset should exercise caution when using it. The author of en2ko_hiphop does not assume any legal responsibility for the use of the dataset. If you have any questions or concerns regarding the dataset's copyright status, please contact the author at sungcho2023@u.northwestern.edu.


## Acknowledgements

I gratefully acknowledge DanceD(http://danced.co.kr/) of Korean Hiphop community HIPHOPLE(https://hiphople.com/). All English-to-Korean translations have been provided by DanceD.