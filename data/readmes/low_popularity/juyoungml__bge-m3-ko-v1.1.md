---
base_model: BAAI/bge-m3
datasets:
- nlpai-lab/ko-triplet-v1.0
language:
- ko
library_name: sentence-transformers
metrics:
- cosine_accuracy
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:744862
- loss:ModifiedGISTEmbedLoss
widget:
- source_sentence: 부산 중앙버스전용차로(BRT) 구간 횡단보도에서 처음으로 발생한 사고는 뭐지?
  sentences:
  - 지난 30일 오후 11시 10분쯤 부산 해운대구 우동 동백역 버스정류소 앞 도로에서 1차로를 달리던 A(75)씨의 SM5 승용차가 정류소 방향으로
    횡단보도를 건너는 B(70·여)씨를 치었다.
  - 광원은 광감작제가 최대 광독성능을 나타내는 \( 630 \mathrm{~nm} \) diode laser (Biolitec, Germany)를
    사용하였다.
  - '중앙버스 정류장 및 버스전용차로 설치(31개 노선) '
- source_sentence: 이황의 설은 호발설입니다. 이이의 설은 무엇인가요?
  sentences:
  - '변희재


    변희재는 2014년 5월에도 프로야구 선수인 오승환과의 열애설에 대해서 "김규리의 자작극"이라고 주장 하면서, 김규리로 개명한 김민선에 대해
    "김규리 이름은 원래 김민선이었죠. ... 남의 이름으로 자신의 전과를 백지세탁하는 교활한 자입니다. ... 온갖 저질 거짓선동으로 자신의
    이름을 먹칠한 뒤, 멀쩡한 ''김규리''라는 남의 이름으로 나타날 수가 있습니까. ... 그 시절 청산가리킴은 ''학교1''에서 배두나 따라다니는
    엑스트라에 불과했습니다. 광우병 거짓난동으로 친노종북에 붙은 뒤 남의 이름 빼앗은거죠."라고 인식공격성 발언을 했다. 이에 대해 누리꾼들은
    "김규리 오승환 열애설 사실이든 아니든 변희재는 뭐하는 사람이지?" "김규리 오승환 열애설, 변희재는 왜 끼어든 거지?" 등의 반응을 보였다.'
  - '이이


    즉 이황의 설은 호발설이고 이이는 일도설이었다. 하지만 이황의 칠정설인 기발이승설만을 취한 것이다. 반면에 그의 사단설인 이발기수(理發氣隨)설을
    비판하였다. 또한 그것은 이황과 사단칠정설논쟁을 벌인 기대승의 영향을 받은 것이다. 또한 서경덕에 대해서도 기중심의 설로서 독창적이지만 문제가
    있다며 비판한다. 그의 설은 기가 운동하고 이는 그 원인이 된다는 설에 근거한 것이다. 그는 자기의 주장을 발전시키면서 이 주장이 주자의 뜻과
    어긋나면 주자가 잘못 된 것이라고까지 하는 자신을 얻게 된 것이다. 이같이 그는 학문으로 유명할 뿐 아니라 경세가(經世家)로서도 혁혁한 업적을
    남겼다. 훗날 영남의 유직이 효종원년에 올린 상소문에서 이이의 설을 불교와 육왕(육구연과 왕수인)과 같은 주기설로서 이단이라고 공격하였다.
    그는 이황이야말로 주리설로서 정학이라는 사상에 근거하여 이이를 비판했던 것이다. 그후 주리설은 정학이고 주기설은 이단이라고 여겨지게 되었다.
    그 상소로 인하여 유직은 조정으로부터 처벌받아 과거시험을 응시할 수 있는 자격을 박탈당하였다. 하지만 이이 역시 기의 뿌리가 이라고 말하였기
    때문에 주리설이라고 할 수 있다. 또한 이황과 이이 모두 기의 뿌리가 리라고 했기 때문에 모두 이일원론 또는 이기일원론이라고 할 수 있다.
    그의 저작인 《동호문답(東湖問答)》, 《성학집요(聖學輯要)》, 《인심도심설(人心道心說)》, 《시무육조소(時務六條疏)》 등은 모두 임금의 도리와
    시무를 논한 명저로 그의 정치에 대한 태도는 유학자의 이상인 요순시대를 실현하는 것이었다.'
  - 무거운 책상을 잘못 옮기면 바닥이 다 망가진다.
- source_sentence: 실무, 학과들, 강하다, 많다, 대학
  sentences:
  - 최흥철(崔興喆, 1981년 12월 3일 ~ 현재)은 대한민국의 스키 점프 선수이다. 전라북도 무주에서 태어났다. 1997년부터 선수로 활동하였으며,
    2001년 폴란드 자코파네 유니버시아드에서 종합대회 사상 첫 메달을 획득한 스키 점프 1세대다. 또한 솔트 레이크 시티 2002년 동계 올림픽
    단체전(team large hill) 8위, 개인전(individual normal hill) 30위를 거둔 바 있다. 2002년 3월, 9월에
    있었던 대륙간컵 대회 개인전 일반(normal hill), K89 경기에서 각각 우승하였다. 2003년 세계스키연맹 경주(FIS Race)에서는
    단체전 K90 경기에 출전하여 김현기, 강칠구, 최용직과 함께 두 차례 우승하였다. 같은 대회에 개인전 K90에서는 3위에 올랐다.
  - 이 대학은 실무에 강한 학과들이 생각보다 많았다.
  - 재주라는 것은  예절, 음악, 활쏘기, 글쓰기, 말타기, 계산하기다.
- source_sentence: 속눈썹, 연장술, 받다, 눈, 이상, 생기다
  sentences:
  - 속눈썹 연장술을 받고 갑자기 눈에 이상이 생겼다.
  - 여자들이 한복을 차려 입고 머리에는 댕기를 땋았다.
  - 전통주, 과실주는 복분자, 흑미주, 소곡주, 고추술, 홍주 등으로 원료가 제각기 다 다르다.
- source_sentence: 미국에서 국가기술이전진흥법이 제정된 해는 언제인가
  sentences:
  - 미국은 1980년 「Bayh-Dole법」 제정 및 1995년 「국가기술이전진흥법」 제정을 계기로 기술이전 및 사업화 기반구축을 위해 정책적으로
    노력하고 있다. 국가기술이전센터(NTTC), 지역기술이전센터(RTTC), 연방연구소컨소시엄(FLC) 등 정부차원의 기술이전기관은 주로 총괄업무를
    담당하며, 민간기관, 연구소, 대학기술이전사무소(TLO)에서의 실제 기술거래가 활발한 편이다. 또한, 정부 R&D의 사업화 촉진을 위해 1982년
    「중소기업혁신개발법」(Small Business Innovation Development Enhancement Act)을 제정하고 SBIR(Small
    Business Innovation Research) 제도를 도입하여 1억불 이상 R&D자금을 지원하는 연방정부는 일정비율을 SBIR에 할당하도록
    의무화하였으며 그 결과 국방부, 에너지부, 상무부 등 11개 부처가 참여하여 2008년 기준으로 R&D자금의 2.5% 이상을 지원하고 있다.
  - '대마초


    대마초는 인류가 이용해 온 가장 오래된 약제 중 하나로, 현대에는 주로 오락적, 종교적(영적) 또는 의료적 목적으로 사용되고 있다. 국제 연합(UN)이
    2004년에 추정한 바에 따르면, 전 세계 성년 인구의 4% 정도(약 1억6,200만명)가 대마초를 1년에 1회 이상 흡연하고 있으며, 전
    세계 성년 인구의 0.6% 정도(약 2,250만명)가 1일 1회 이상 흡연하고 있다고 한다. 대마초의 소지나 사용, 판매행위는 그것이 갖고
    있는 각성 효과 때문에 20세기 초부터 전 세계 거의 대부분의 나라에서 불법으로 규정되었다. 전 세계 대부분 국가에서 대마초의 흡연은 불법이고
    그 재배와 유통은 엄격한 통제를 받지만, 일부 국가에서는 그러한 규제를 완화하고 있다.'
  - 우리사회에서 지역문화정책이 본격적으로 논의되기 시작한 1990년대 후반부터 현재까지 정부에서는 지역문화진흥에 대한 지속적인 정책개발이 이루어졌으며,
    이를 통해 다양한 정책사업들을 추진해왔다. 지역의 문화적 기초를 마련하기 위한 문화기반 시설인프라 확충 및 지역문화 전문주체의 구성 및 지원,
    지역 주민 문화향유를 위한 기획사업 및 프로그램 등 다양한 방식의 정책사업들이 추진되었으며 이를 통해 지역의 문화를 고양하기 위한 여러 가지
    정책과 정책사업이 추진되었다. 이러한 시대적 상황 하에서 지역문화에 대한 가치 발견과 지역문화진흥에 대한 제도적지원의 필요성이 지속적으로 제기
    되어온 바, 2014년 1월 ‘지역문화진흥법’이 제정되고 동년 7월에 본격 시행되었다. 문화체육관광부에서는 지역문화진흥법의 제정 및 시행을
    토대로 중앙정부 차원의 정책계획으로서 법에서 정하고 있는 지역문화진흥기본계획을 수립하고 그에 따른 정책사업 추진의 방향을 설정하고 있으며 각
    지역에 정책사업을 지원 및 시행하고 있다.
model-index:
- name: SentenceTransformer based on BAAI/bge-m3
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: dev
      type: dev
    metrics:
    - type: cosine_accuracy
      value: 0.99
      name: Cosine Accuracy
---

# SentenceTransformer based on BAAI/bge-m3

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) on the [ko-triplet-v1.0](https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0) dataset. It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) <!-- at revision 5617a9f61b028005a4858fdac845db406aefb181 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 1024 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [ko-triplet-v1.0](https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0)
- **Language:** ko
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("scottsuk0306/bge-m3-ko-v1.1")
# Run inference
sentences = [
    '미국에서 국가기술이전진흥법이 제정된 해는 언제인가',
    '미국은 1980년 「Bayh-Dole법」 제정 및 1995년 「국가기술이전진흥법」 제정을 계기로 기술이전 및 사업화 기반구축을 위해 정책적으로 노력하고 있다. 국가기술이전센터(NTTC), 지역기술이전센터(RTTC), 연방연구소컨소시엄(FLC) 등 정부차원의 기술이전기관은 주로 총괄업무를 담당하며, 민간기관, 연구소, 대학기술이전사무소(TLO)에서의 실제 기술거래가 활발한 편이다. 또한, 정부 R&D의 사업화 촉진을 위해 1982년 「중소기업혁신개발법」(Small Business Innovation Development Enhancement Act)을 제정하고 SBIR(Small Business Innovation Research) 제도를 도입하여 1억불 이상 R&D자금을 지원하는 연방정부는 일정비율을 SBIR에 할당하도록 의무화하였으며 그 결과 국방부, 에너지부, 상무부 등 11개 부처가 참여하여 2008년 기준으로 R&D자금의 2.5% 이상을 지원하고 있다.',
    '우리사회에서 지역문화정책이 본격적으로 논의되기 시작한 1990년대 후반부터 현재까지 정부에서는 지역문화진흥에 대한 지속적인 정책개발이 이루어졌으며, 이를 통해 다양한 정책사업들을 추진해왔다. 지역의 문화적 기초를 마련하기 위한 문화기반 시설인프라 확충 및 지역문화 전문주체의 구성 및 지원, 지역 주민 문화향유를 위한 기획사업 및 프로그램 등 다양한 방식의 정책사업들이 추진되었으며 이를 통해 지역의 문화를 고양하기 위한 여러 가지 정책과 정책사업이 추진되었다. 이러한 시대적 상황 하에서 지역문화에 대한 가치 발견과 지역문화진흥에 대한 제도적지원의 필요성이 지속적으로 제기 되어온 바, 2014년 1월 ‘지역문화진흥법’이 제정되고 동년 7월에 본격 시행되었다. 문화체육관광부에서는 지역문화진흥법의 제정 및 시행을 토대로 중앙정부 차원의 정책계획으로서 법에서 정하고 있는 지역문화진흥기본계획을 수립하고 그에 따른 정책사업 추진의 방향을 설정하고 있으며 각 지역에 정책사업을 지원 및 시행하고 있다.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 1024]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Triplet

* Dataset: `dev`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator)

| Metric              | Value    |
|:--------------------|:---------|
| **cosine_accuracy** | **0.99** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### ko-triplet-v1.0

* Dataset: [ko-triplet-v1.0](https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0) at [1f5d72d](https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0/tree/1f5d72d21ae8309b5221a588b13930b423385bff)
* Size: 744,862 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                             | positive                                                                             | negative                                                                           |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                               | string                                                                             |
  | details | <ul><li>min: 9 tokens</li><li>mean: 22.12 tokens</li><li>max: 146 tokens</li></ul> | <ul><li>min: 10 tokens</li><li>mean: 92.69 tokens</li><li>max: 1815 tokens</li></ul> | <ul><li>min: 8 tokens</li><li>mean: 99.24 tokens</li><li>max: 880 tokens</li></ul> |
* Samples:
  | anchor                                                                                        | positive                                                                                                                                                                                                                     | negative                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  |:----------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>글쓰기, 대회, 참가료, 받다</code>                                                                 | <code>글쓰기 대회는 참가자한테 일정분의 참가료를 받았다.</code>                                                                                                                                                                                    | <code>재주는 예절, 음악, 활쏘기, 글쓰기, 말타기, 계산하기 등등 이다.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | <code>"K리그 2002 시즌"에서 기록한 관객의 수보다 독일 고틀리프 다임러 경기장에서 개최된 "제4회 세계 육상 선수권 대회"의 관객 수가 많았나?</code> | <code>1993년 세계 육상 선수권 대회. 제4회 세계 육상 선수권 대회는 국제 육상 경기 연맹 주관으로 1993년 8월 13일에서 8월 22일까지 독일 슈투트가르트 고틀리프 다임러 경기장에서 열린 국제 육상 대회이다. 독일에서 열린 첫 번째 세계 육상 선수권 대회였다. 187개국 선수 1630명이 참가했으며, 대회 역사상 가장 많은 수인 58만 5000명의 관중이 입장했다.</code> | <code>송강호. 경력. 1996-2000: 초기 경력과 주목 받다. 1999년에는 강제규 감독의 영화 《쉬리》에 이장길 역할로 출연했다. 이 영화는 관객수 582만 명을 기록하며 당시 국내 최다 관객 영화 기록을 갱신했고, 최초로 500만 관객을 넘어섰다. 2000년에는 코미디 영화 《반칙왕》에서 첫 주연을 맡았다. 이 영화에서 그는 은행원이자 레슬러 대호 역할로 캐스팅 되어 영화를 위해 레슬링 훈련을 했었다. 이후 송강호는 이 영화가 가장 인상 깊다고 꼽으며 "물리적으로 가장 극한의 상황까지 간 작품이었다는 생각이 든다. 만약 지금 레슬링을 다시 한다면 죽을 거다"라고 말했다. 같은 해 그는 박찬욱 감독의 영화 《공동경비구역 JSA》에서 오경필 중사 역할로 출연했다. 이 영화는 이전까지 반공이데올로기에서 벗어나지 못했던 분단 소재 한국영화의 시각을 인간애로 확장한 작품으로 583만 명의 관객수를 기록하며 역대 흥행 1위 영화로 기록했다. 송강호는 2019년 매체와의 인터뷰에서 배우 인생의 전환점이 됐다고 언급하며 “두 영화가 개봉한 2000년은 배우 생활 초반의 분기점이 됐다”고 말했다. 한 영화 관계자는 송강호에게 "《반칙왕》에서 보여준뛰어난 연기를 보고 그 이상의 연기는 나올 수 없을 것이라 생각했다. 이번 영화를 보고 내가 당신 연기의 한계를 너무 낮게 잡았음을 알았다"고 말했다. 《매일경제》의 프리뷰에서는 "송강호가 그려낸 따뜻하고 넉넉한 오경필 중사는 군기가 한참 빠져 서로 노닥거리는 것으로 비칠수도 있는 모습들을 눈물나는 형제애로 잡아주는 든든한 받침대다"라고 리뷰했다. 이러한 호평 속에 제1회 부산영화평론가협회상, 제38회 대종상영화제, 제3회 도빌아시아영화제, 에서 남우주연상을 수상했고, 이 외에도 백상예술대상에서 인기상을 받는 등 다수의 시상식에서 연기력과 스타성에서 인정을 받았다.</code> |
  | <code>트리거는 데이터를 저장시켜?</code>                                                                  | <code>트리거는 안테나 시험 장비를 구동시켜 시나리오를 발생시키며, 시나리오에 따라 안테나부의 송신기와 수신기를 제어 및 측정하여 데이터를 저장하 게 된다.</code>                                                                                                                             | <code>영화관에서는 왜 대부분의 관객이 실감나게 소리가 잘 들리는 걸까? 디자인이 Ugly하지만 왜 CRT일때는 소리가 잘 들렸을까? 이런 질문에 대한 해답을 영화관 스크린속에서 찾을 수 있었다.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
* Loss: <code>__main__.ModifiedGISTEmbedLoss</code> with these parameters:
  ```json
  {'guide': SentenceTransformer(
    (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: NewModel 
    (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
    (2): Normalize()
  ), 'temperature': 0.01}
  ```

### Evaluation Dataset

#### ko-triplet-v1.0

* Dataset: [ko-triplet-v1.0](https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0) at [1f5d72d](https://huggingface.co/datasets/nlpai-lab/ko-triplet-v1.0/tree/1f5d72d21ae8309b5221a588b13930b423385bff)
* Size: 744,862 evaluation samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                             | positive                                                                             | negative                                                                            |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                               | string                                                                              |
  | details | <ul><li>min: 8 tokens</li><li>mean: 22.19 tokens</li><li>max: 100 tokens</li></ul> | <ul><li>min: 12 tokens</li><li>mean: 98.72 tokens</li><li>max: 1262 tokens</li></ul> | <ul><li>min: 11 tokens</li><li>mean: 95.33 tokens</li><li>max: 741 tokens</li></ul> |
* Samples:
  | anchor                                                                              | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | negative                                                      |
  |:------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------|
  | <code>지하, 차도, 빠져나가다, 우회전, 하다, 목적지, 도착하다</code>                                      | <code>지하 차도를 재빨리 빠져나가자마자 우회전을 하면 목적지에 도착한다.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | <code>재주라는 것은  예절, 음악, 활쏘기, 글쓰기, 말타기, 계산하기다.</code>           |
  | <code>본문의 표 6에서 packet length = 0.5이고 노드수가 4일 때 Basic CSMA/CA의 수학적분석값은 얼마일까?</code> | <code><table border><caption>표 6. 패킷 길이에 따른 IEEE 802.11 MAC 프로토콜의 시뮬레이션 결과와 Analytic 결과 비교</caption> <tbody><tr><td rowspan=3>노드의 수</td><td colspan=4>packet length = 0.5</td><td colspan=4>packet length = 0.3</td></tr><tr><td colspan=2>Basic CSMA/CA</td><td colspan=2>RTS/CTS 프로토콜</td><td colspan=2>Basic CSMA/CA</td><td colspan=2>RTS/CTS 프로토콜</td></tr><tr><td>시뮬레이션</td><td>수학적분석</td><td>시뮬레이션</td><td>수학적분석</td><td>시뮬레이션</td><td>수학적분석</td><td>시뮬레이션</td><td>수학적분석</td></tr><tr><td>1</td><td>0.670</td><td>0.672</td><td>0.682</td><td>0.673</td><td>0.625</td><td>0.625</td><td>0.570</td><td>0.571</td></tr><tr><td>2</td><td>0.772</td><td>0.770</td><td>0.746</td><td>0.735</td><td>0.708</td><td>0.710</td><td>0.650</td><td>0.652</td></tr><tr><td>3</td><td>0.779</td><td>0.781</td><td>0.780</td><td>0.772</td><td>0.739</td><td>0.738</td><td>0.690</td><td>0.690</td></tr><tr><td>4</td><td>0.780</td><td>0.783</td><td>0.785</td><td>0.784</td><td>0.740</td><td>0.741</td><td>0.700</td><td>0.701</td></tr><tr><td>5...</code> | <code>표 5 및 6은 수학적 분석의 결과값과 컴퓨터 시뮬레이션을 한 결과값을 비교한 표이다.</code> |
  | <code>점심시간, 유산소, 운동, 하다</code>                                                      | <code>건강을 위하여 점심시간에 유산소 운동을 했다.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | <code>흑미밥과 바지락미역국, 닭볶음, 냉이무침, 무말랭이, 배추김치가 오늘 점심이다.</code>     |
* Loss: <code>__main__.ModifiedGISTEmbedLoss</code> with these parameters:
  ```json
  {'guide': SentenceTransformer(
    (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: NewModel 
    (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
    (2): Normalize()
  ), 'temperature': 0.01}
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 4
- `gradient_accumulation_steps`: 8
- `learning_rate`: 0.0001
- `num_train_epochs`: 1
- `lr_scheduler_type`: cosine
- `warmup_ratio`: 0.1
- `bf16`: True
- `dataloader_num_workers`: 2
- `optim`: adamw_torch_fused
- `ddp_find_unused_parameters`: True
- `dataloader_persistent_workers`: True
- `push_to_hub`: True
- `hub_model_id`: scottsuk0306/bge-m3-ko-v1.1
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 4
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 8
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 0.0001
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: cosine
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: True
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: True
- `dataloader_num_workers`: 2
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: True
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: True
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: True
- `resume_from_checkpoint`: None
- `hub_model_id`: scottsuk0306/bge-m3-ko-v1.1
- `hub_strategy`: every_save
- `hub_private_repo`: False
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch | Step | Training Loss | dev_cosine_accuracy |
|:-----:|:----:|:-------------:|:-------------------:|
| 0     | 0    | -             | 0.99                |
| 0.128 | 10   | 0.016         | -                   |
| 0.256 | 20   | 0.0252        | -                   |
| 0.384 | 30   | 0.0362        | -                   |
| 0.512 | 40   | 0.0335        | -                   |
| 0.64  | 50   | 0.028         | -                   |
| 0.768 | 60   | 0.0328        | -                   |
| 0.896 | 70   | 0.0131        | -                   |


### Framework Versions
- Python: 3.11.9
- Sentence Transformers: 3.3.1
- Transformers: 4.45.1
- PyTorch: 2.4.0+cu121
- Accelerate: 1.1.1
- Datasets: 2.19.2
- Tokenizers: 0.20.0

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->