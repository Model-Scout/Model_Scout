---
license: other
license_name: youtube-terms-of-service
license_link: https://www.youtube.com/t/terms
task_categories:
- text-classification
language:
- ko
tags:
- youtube
- korean
- sentiment-analysis
- social-media
- user-generated-content
pretty_name: Korean YouTube Comment Sentiment Dataset
size_categories:
- 1K<n<10K
---
# Korean YouTube Comment Sentiment Dataset

## Data Overview
### Summary

본 데이터셋은 유튜브에서 수집된 **한국어 댓글 5,482개**와 이에 대응하는 **감정 레이블**(긍정, 부정, 중립, 불명확)로 구성된 감정 분류용 데이터셋입니다.

- 주요 레이블: `긍정`, `부정`, `중립`, `불명확`

### Features
- **수집 대상**: 요리, 뷰티, 게임, 여행, 쇼핑 등 분야의 **10만 명 이상 구독자를 보유한 유튜브 채널**
- **형식**: JSON (`id`, `text`, `label`)
- **검수**: 한국인 검수자에 의한 **수작업 라벨링 및 교차 검토**

본 데이터셋은 구어체, 이모지, 줄임말 등 실제 사용자 표현이 반영되어 있습니다.

## Dataset Structure

### Dataset Fields

| Field      | Type   | Description                                                                 |
|------------|--------|-----------------------------------------------------------------------------|
| `id`      | string | 각 댓글의 고유 ID|
| `text`    | string | 유튜브 댓글 본문 텍스트 |
| `label`   | string | 감정 레이블. [`긍정`, `부정`, `중립`, `불명확`]|
| `..` | .. | ..|


In our repository, the dataset is divided into the following splits:
- `train`: 3,421개
- `validation`: 868개
- `test`: 1,193개


## Dataset Details

### Source Data

- 2024년 상반기, **구독자 10만 명 이상**을 보유한 한국 유튜버의 영상 댓글 수집  
- 수집 분야: 요리, 뷰티, 게임, 여행, 쇼핑 등

### Annotations

- 콘텐츠 맥락을 이해하는 **한국인 검수자 5인**이 직접 수작업 라벨링  
- 해석이 모호한 사례는 검토 후 `uncertain`으로 분류

### Privacy

모든 댓글에서 사용자 계정명, 영상 URL 등의 개인정보는 제거되었으며,  
실제 사용자 식별이 불가능하도록 가명 처리 또는 제거 작업을 수행했습니다.  
다만, 댓글 내용 중 일부에 유추 가능한 채널명, 인물명, 지명 등이 **잔존할 가능성이 있습니다**.

이 데이터는 연구 목적으로만 제공되며, 원본 유튜브 사용자와 직접적인 연계가 되지 않도록 유의 바랍니다.

## Additional Information

### Licensing Information

이 데이터셋은 YouTube에서 수집된 댓글을 기반으로 하며, YouTube의 [이용약관](https://www.youtube.com/t/terms)을 준수합니다.  
모든 사용자 이름, ID, 영상 링크 등 개인정보는 제거하였으나, 일부 표현에 사용자명 또는 채널명을 암시하는 정보가 **잔존할 수 있습니다**.  

이 데이터셋은 **비상업적 연구 목적**으로만 사용 가능하며, 재배포는 금지됩니다.  
YouTube 또는 원 작성자의 권리를 침해하지 않도록 주의해 주세요.

## Disclaimer

This dataset contains user-generated content originally posted on YouTube.  
All data has been anonymized and is presented for academic research purposes only.  
Redistribution or use for commercial purposes is not permitted.

If you are a rights holder and believe your content has been used improperly, please contact us at suil0109@gmail.com.

### Citation Information

```
@misc{korean_youtube_sentiment_2025,  
  title={Korean YouTube Comment Sentiment Dataset},  
  author={Hanjun Jung, Jinsoo Kim, Junhyeok Choi, Suil Lee, Seongjae Kang},  
  year={2025},  
  publisher={Hugging Face},  
}
```

### Contributions
**Repository:** [링크]  

**Email**: suil0109@gmail.com

**Team**
- Hanjun Jung
- Jinsoo Kim
- Junhyeok Choi
- Suil Lee
- Seongjae Kang