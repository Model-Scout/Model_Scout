# KR3: Korean Restaurant Reviews with Ratings

460K(+180K) Korean Sentiment Classification Dataset

## KR3: Korean Restaurant Reviews with Ratings
Korean sentiment classification dataset   

- Size: 460K(+180K)
- Language: Korean-centric

### ⚠️ Caution with `Rating` Column
0 stands for negative review, 1 stands for positive review, and 2 stands for ambiguous review.
**Note that rating 2 is not intended to be used directly for supervised learning(classification).** This data is included for additional pre-training purpose or other usage. 
In other words, this dataset is basically a **binary** sentiment classficiation task where labels are 0 and 1.

### 🔍 See More
See all the codes for crawling/preprocessing the dataset and experiments with KR3 in [GitHub Repo](https://github.com/Wittgensteinian/kr3)  
You can also download the dataset via hugging face `datasets` from [Hugging Face Hub](https://huggingface.co/datasets/Wittgensteinian/KR3). I recommend this way because of its ease of use.  

### Legal Issues
We concluded that the **non-commerical usage and release of KR3 fall into the range of fair use (공정 이용)** stated in the Korean copyright act (저작권법). We further clarify that we **did not agree to the terms of service** from any websites which might prohibit web crawling. In other words, web crawling we've done was proceeded without logging in to the website. Despite all of these, feel free to contact to any of the contributors if you notice any legal issues.

### Contributors & Acknowledgement
(Alphabetical order)

[Dongin Jung](https://github.com/dongin1009)

[Hyunwoo Kwak](https://github.com/Kwak-Hyun-woo)

[Kaeun Lee](https://github.com/Kaeun-Lee)

[Yejoon Lee](https://github.com/wittgensteinian)

This work was done as DIYA 4기. Compute resources needed for the work was supported by [DIYA](https://blog.diyaml.com) and surromind.ai.

출처: Kaggle (ninetyninenewton/kr3-korean-restaurant-reviews-with-ratings)
태그: finance, health, nlp, classification, transfer learning, restaurants, korea
라이선스: CC BY-NC-SA 4.0
수정일: 2022-02-25T07:33:13.663Z
