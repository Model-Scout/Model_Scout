---
license: mit
datasets:
- kakaobrain/kor_nli
- kakaobrain/kor_nlu
- klue/klue
language:
- ko
metrics:
- spearmanr
- pearsonr
pipeline_tag: sentence-similarity
---

# 🍊 SimCSE-KO

## 1. Intro

**한국어 SimCSE(BERT, Supervised)** 모델입니다.      
Princeton NLP의 코드가 아닌 새로운 코드를 이용해 학습되었습니다.          
두 문장 사이의 코사인 유사도를 계산해 의미적 관련성을 판단할 수 있습니다.  

- Github: [https://github.com/millet04/SimCSE-KO](https://github.com/millet04/SimCSE-KO)
- Original Code: [https://github.com/princeton-nlp/SimCSE](https://github.com/princeton-nlp/SimCSE)


## 2. Experiments Settings

- Model: klue/bert-base
- Dataset: KorNLI-train (supervised training), KorSTS-dev (evaluation)
- epoch: 1
- max length: 64
- batch size: 256
- learning rate: 5e-5
- drop out: 0.1
- temp: 0.05
- pooler: cls
- 1 A100 GPU

## 3. Performance

## (1) KorSTS-test
|Model|AVG|Cosine Pearson|Cosine Spearman|Euclidean Pearson|Euclidean Spearman|Manhatten Pearson|Manhatten Spearman|Dot Pearson|Dot Spearman|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|SimCSE-BERT-KO<br>(unsup)|72.85|73.00|72.77|72.96|72.92|72.93|72.86|72.80|72.53|
|SimCSE-BERT-KO<br>(sup)|**85.98**|**86.05**|**86.00**|**85.88**|**86.08**|**85.90**|**86.08**|**85.96**|**85.89**|
|SimCSE-RoBERTa-KO<br>(unsup)|75.79|76.39|75.57|75.71|75.52|75.65|75.42|76.41|75.63|
|SimCSE-RoBERTa-KO<br>(sup)|83.06|82.67|83.21|83.22|83.27|83.24|83.28|82.54|83.03|82.92|

## (2) Klue-dev
|Model|AVG|Cosine Pearson|Cosine Spearman|Euclidean Pearson|Euclidean Spearman|Manhatten Pearson|Manhatten Spearman|Dot Pearson|Dot Spearman|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|SimCSE-BERT-KO<br>(unsup)|65.27|66.27|64.31|66.18|64.05|66.00|63.77|66.64|64.93|
|SimCSE-BERT-KO<br>(sup)|**83.96**|**82.98**|**84.32**|**84.32**|**84.30**|**84.28**|**84.20**|**83.00**|**84.29**|
|SimCSE-RoBERTa-KO<br>(unsup)|80.78|81.20|80.35|81.27|80.36|81.28|80.40|81.13|80.26|
|SimCSE-RoBERTa-KO<br>(sup)|85.31|84.14|85.64|86.09|85.68|86.04|85.65|83.94|85.30|

## Citing
```
@article{gao2021simcse,
   title={{SimCSE}: Simple Contrastive Learning of Sentence Embeddings},
   author={Gao, Tianyu and Yao, Xingcheng and Chen, Danqi},
   booktitle={Empirical Methods in Natural Language Processing (EMNLP)},
   year={2021}
}
@article{ham2020kornli,
 title={KorNLI and KorSTS: New Benchmark Datasets for Korean Natural Language Understanding},
 author={Ham, Jiyeon and Choe, Yo Joong and Park, Kyubyong and Choi, Ilji and Soh, Hyungjoon},
 journal={arXiv preprint arXiv:2004.03289},
 year={2020}
}
@misc{park2021klue,
      title={KLUE: Korean Language Understanding Evaluation},
      author={Sungjoon Park and Jihyung Moon and Sungdong Kim and Won Ik Cho and Jiyoon Han and Jangwon Park and Chisung Song and Junseong Kim and Yongsook Song and Taehwan Oh and Joohong Lee and Juhyun Oh and Sungwon Lyu and Younghoon Jeong and Inkwon Lee and Sangwoo Seo and Dongjun Lee and Hyunwoo Kim and Myeonghwa Lee and Seongbo Jang and Seungwon Do and Sunkyoung Kim and Kyungtae Lim and Jongwon Lee and Kyumin Park and Jamin Shin and Seonghyun Kim and Lucy Park and Alice Oh and Jungwoo Ha and Kyunghyun Cho},
      year={2021},
      eprint={2105.09680},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
