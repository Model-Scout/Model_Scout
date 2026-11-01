# Kc-MoE Pretrain & Finetune Dataset

Datasets used for training Kc-MoE model

[Kc-MoE](https://github.com/Quasar-Kim/kc-moe) 자연어 처리 모델 훈련에 사용된 데이터셋들입니다. 각 데이터셋별 세부 정보는 아래에서 찾아보실 수 있습니다. 

데이터 파일은 모두 parquet 형식으로 저장되어 있습니다. Pretrain용 데이터셋(kcbert-cleaned, khs-cleaned)는 dask dataframe을 이용해서 parquet 파일들이 담긴 디렉토리 자체를 `read_parquet`으로 열면 불러올 수 있습니다. Finetuning용 데이터셋(두개 제외 모두)는 pandas의 `read_parquet` 함수를 이용하면 dataframe 형식으로 불러 올 수 있습니다.

실제 사용 시 Tensorflow Dataset 형식으로 변환하는 게 더 편하고 빠를 수 있습니다. 위 Kc-MoE 레포지토리에서 변환 스크립트를 제공하니 실제 사용 시 이를 이용하는 걸 추천합니다.

아래 정보에서 토큰 개수는 Kc-MoE 모델의 sentencepiece 토크나이저 모델을 기준으로 센 것입니다.

# kcbert-cleaned

- URL: https://github.com/Beomi/KcBERT
- License: MIT

KcBERT 모델을 pretraining하는데 사용된 데이터셋. 뉴스 댓글로 이루어져 있음. 원 데이터에 위 레포지토리에서 제시된 클리닝을 적용함.

### 크기

- 평균 토큰 길이: 30.3 tokens
- 세트별 크기:
    - train: 317,871,849 samples ≈ 9.6B(9,600,000,000) tokens

### 컬럼

- `text`: 댓글 텍스트

### 예시

```json
{
    "text": "개한민국 수준 진짜 개탄스럽다"
}
```

# khs-cleaned

- URL: [https://www.kaggle.com/competitions/korean-hate-speech-detection](https://www.kaggle.com/competitions/korean-hate-speech-detection)
- License: CC BY-SA 4.0

Korean Hate Speech Detection 데이터셋의 unlabeled 셋. KcBERT v2022와 동일한 클리닝을 적용함.

### 크기

- train: 1,820,562 samples

### 컬럼

- `text`: 댓글 텍스트

### 예시

```json
{
    "text": "알바쓰고많이만들면되지 돈욕심없으면골목식당왜나온겨 기댕기게나하고 산에가서팔어라"
}
```

# nsmc

- URL: https://github.com/e9t/nsmc
- License: CC0 1.0

네이버 영화에서 수집한 리뷰 댓글들의 긍/부정을 분류하는 데이터셋.

### 크기

- train: 149,995 samples
- test: 49,997 samples

### 통계

- 글자: 평균 35.2 / 최대 158
- 토큰: 평균 19.6 / 최대 139 / 전체 3,924,825

### 컬럼

- `text`: 리뷰 텍스트
- `label`: 리뷰의 긍정/부정을 나타내는 항목. `0` - 부정적, `1`- 긍정적

### 예시

```json
{
	"text": "아 더빙.. 진짜 짜증나네요 목소리",
	"label": 0
}
```

# kornli

- URL: https://github.com/kakaobrain/KorNLUDatasets
- License: CC BY-SA 4.0

외국어 NLI(Natural Language Inference, 자연어 추론) 데이터셋들을 번역해서 만든 데이터셋. NLI는 주어진 전제에 대해 가설이 참인지, 거짓인지, 또는 판단할 수 없는지 구분하는 task다.

### 크기

- train: 942,808 samples
- validation: 2,490 samples
- test: 5,010 samples

### 통계

- text1
    - 글자: 평균 42.2 / 최대 853
    - 토큰: 평균 19.6 / 최대 139 / 전체 21,653,893
- text2
    - 글자: 평균 23.3 / 최대 205
    - 토큰: 평균 13.0 / 최대 201 / 전체 12,408,405

### 컬럼

- `text1`: 전제
- `text2`: 가설
- `label`: 두 문장의 관계. `neutral` - 중립, `contradiction` - 모순, `entailment` - 수반 중 하나.

### 예시
```json
{
	"text1": "그리고 그가 말했다, \"엄마, 저 왔어요.\"",
	"text2": "그는 한마디도 하지 않았다.",
	"label": "contradiction"
}
```


# korsts

- URL: https://github.com/kakaobrain/KorNLUDatasets
- License: CC BY-SA 4.0

주어진 두 문장의 의미의 유사성을 측정하는 STS(Semantic Textual Similarity) 데이터셋. STSbenchmark 데이터셋을 번역해서 만듦.

### 크기
- train: 5,749 samples
- validation: 1,500 samples
- test: 1,379 samples

### 통계

- text1
    - 글자: 평균 30.5 / 최대 205
    - 토큰: 평균 16.4 / 최대 87 / 전체 141,771
- text2
    - 글자: 평균 30.4 / 최대 140
    - 토큰: 평균 16.3 / 최대 72 / 전체 141,431

### 컬럼

- `text1`, `text2`: 문장
- `score`: 0~5 사이의 float로 나타낸 두 문장의 유사도.

### 예시

```json
{
	"text1": "한 여성이 기타를 연주하고 있다.",
	"text2": "한 남자가 기타를 치고 있다.",
	"score": 2.45
}
```

# Question Pair

- URL: https://github.com/songys/Question_pair
- License: MIT

두 질문이 동일한 의미인지 판단하는 데이터셋.

### 크기
- train: 6,199 samples
- validation: 689 examples
- test: 688 samples
    
### 통계

- text
    - 글자: 평균 13.5 / 최대 47
    - 토큰: 평균 7.4 / 최대 25 / 전체 56,697
- pair
    - 글자: 평균 13.2 / 최대 56
    - 토큰: 평균 7.3 / 최대 28 / 전체 55,452

### 컬럼

- `text`, `pair`: 질문.
- `label`: `0`-동일한 의미의 질문(`같음`), `1`- 다른 의미의 질문(`다름`)

### 예시

```json
{
  "text": "21살의 사랑에 대해",
	"pair": "사랑을 노력한다는게 말이 되나요?",
	"label": 1
}
```

# hate-speech

- URL: [https://www.kaggle.com/competitions/korean-hate-speech-detection](https://www.kaggle.com/competitions/korean-hate-speech-detection)
- License: CC BY-SA 4.0

기사에 달린 댓글의 혐오 댓글 여부를 분류하는 데이터셋.

### 크기
- train: 7,896 samples
- validation: 471 samples
- test: 974 samples

### 통계

- 글자: 평균 38.7 / 최대 137
- 토큰: 평균 21.1 / 최대 83 / 전체 176,832

### 컬럼

- `text`: 댓글.
- `label`: 댓글의 분류. `hate` / `offensive` / `none`

### 예시

처리 전:

```json
{
  "text": "설마 ㅈ 현정 작가 아니지??",
  "label": "hate"
}
```

출처: Kaggle (quasarkim/kcmoe-pretrain-finetune-dataset)
태그: text, korean
라이선스: Unknown
수정일: 2023-01-16T04:55:36.197Z
