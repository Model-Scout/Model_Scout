# LGBT-targeted HateSpeech Comments Dataset (Korean)

LGBT-targeted HateSpeech Comments on NAVER News articles(about Queer Parade)

# LGBT HateSpeech Comments Dataset (Korean)

## Background

Hate speech becomes a major social issue, breaking our relationships and threating our society members.
However, in most Korean datasets about hate speech, there're very few samples related to LGBT(and other minorities, too).

## Content

This dataset contains the `contents` column and `label` column, 1 labeled as "hate speech" and 0 as negative samples(NOT-Hatespeech comments).

## Data gathering & Tagging

### Train Data

- Hate Speech (label 1): Augmented dataset with user information - comments in target news, who spoke the hate speech previously(in relevant news articles)
- Non-hate speech (label 0): BEEP Paper, non-biased, non-hate speech in trainset ( from https://www.kaggle.com/c/korean-hate-speech-detection/overview )

### Test Data

- Hate Speech (label 1): HateSpeech tagged by researcher
- Non-Hate speech (label 0): Non-hate speech or pro-LGBT texts tagged by researcher + BEEP Paper, non-biased, non-hate speech in dev set ( from https://www.kaggle.com/c/korean-hate-speech-detection/overview )

## Acknowledgements

This dataset has NOT cross-validated by several researchers.
This dataset will be updated with another validation.

출처: Kaggle (junbumlee/lgbt-hatespeech-comments-at-naver-news-korean)
태그: social science, nlp, text, online communities, social networks
라이선스: CC BY-SA 4.0
수정일: 2021-04-02T02:13:54.610Z
