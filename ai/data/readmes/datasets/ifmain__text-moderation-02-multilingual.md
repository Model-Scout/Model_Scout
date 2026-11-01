---
license: apache-2.0  
datasets:  
  - ifmain/text-moderation-410K  
language:  
  - en  
  - de  
  - fr  
  - es  
  - it  
  - sv  
  - fi  
  - pl  
  - cs  
  - lv  
  - zh  
  - ja  
  - ko  
  - ru  
  - uk  
  - be  
  - kk  
---

This dataset is based on [Kaggle](https://www.kaggle.com/code/danofer/reddit-comments-scores-nlp/).  
It represents a version of [@ifmain/text-moderation-410K](https://huggingface.co/datasets/ifmain/text-moderation-410K) that has been cleansed of semantically similar values and normalized to a 50/50 ratio of negative and neutral entries.

The dataset contains 1.5M entries (91K * 17 languages).  

Before use, augmentation is recommended! (e.g., character substitution to bypass moderation).
For augmentation, you can use [@ifmain/StringAugmentor](https://github.com/ifmain/StringAugmentor).  

Enjoy using it!