---
license: cc-by-nc-sa-4.0
task_categories:
- text-generation
- question-answering
tags:
- human feedback
- rlhf
- preferences
- reddit
- preference model
- RL
- NLG
- evaluation
size_categories:
- 100K<n<1M
language:
- ko
- en
---
# 🚢  Korean Stanford Human Preferences Dataset (Ko.SHP)

이 데이터셋은 자체 구축한 번역기를 활용하여 [stanfordnlp/SHP](https://huggingface.co/datasets/stanfordnlp/SHP) 데이터셋을 번역한 것입니다.
아래의 내용은 해당 번역기로 README 파일을 번역한 것입니다. 참고 부탁드립니다.

**If you mention this dataset in a paper, please cite the paper:** [Understanding Dataset Difficulty with V-Usable Information (ICML 2022)](https://proceedings.mlr.press/v162/ethayarajh22a.html).

## Summary

SHP는 요리에서 법률 조언에 이르기까지 18가지 다른 주제 영역의 질문/지침에 대한 응답에 대한 **385K 집단 인간 선호도** 데이터 세트이다.
기본 설정은 다른 응답에 대 한 한 응답의 유용성을 반영 하기 위한 것이며 RLHF 보상 모델 및 NLG 평가 모델 (예: [SteamSHP](https://huggingface.co/stanfordnlp/SteamSHP-flan-t5-xl))을 훈련 하는 데 사용 하도록 설정 됩니다.

각각의 예는 질문/지시 및 그 게시물에 대한 한 쌍의 최상위 코멘트를 갖는 레딧 게시물이며, 여기서 하나의 코멘트는 (종합적으로) 레딧 사용자에 의해 더 선호된다.
SHP는 댓글 A가 댓글 B 뒤에 작성되었지만 그럼에도 불구하고 점수가 더 높으면 표면적으로는 A가 B보다 더 선호된다는 사실을 이용한다.
A가 B보다 먼저 작성되었으면 더 높은 점수가 더 많은 가시성의 결과일 수 있기 때문에 결론을 내릴 수 없었다.
우리는 선호도 라벨이 어떤 반응이 덜 *유해*하기보다는 더 *도움이* 되는지를 반영하기 위한 데이터를 선택했으며 후자는 많은 과거 작업의 초점이다.

SHP는 [Anthropic의 HH-RLHF 데이터 세트](https://huggingface.co/datasets/Anthropic/hh-rlhf)와 어떻게 다른가요?
특히, SHP의 모든 데이터는 자연적으로 발생하고 인간이 작성하는 반면 HH-RLHF의 응답은 기계 작성되어 서로를 보완할 수 있는 두 가지 매우 다른 분포를 제공한다.

| Dataset              | Size | Input                      | Label                       | Domains           | Data Format                           | Length |
| -------------------- | ---- | -------------------------- | ---------------------------- | ------------------------- | ------------------------------------- | --------------- |
| SHP                  | 385K | 자연 발생 인간 작성 응답   | Collective Human Preference  | 18 (labelled)  | Question/Instruction + Response (Single-turn) | 최대 10.1K T5 토큰 |
| HH-RLHF    | 91K | LLM과의 대화  | 개별 인간 선호도  | 레이블이 지정되지 않음   | Live Chat (Multi-turn)              | 최대 1.5K T5 토큰 |

SHP는 [ELI5](https://huggingface.co/datasets/eli5#source-data)와 같이 Reddit을 스크래핑한 다른 데이터 세트와 어떻게 다른가요?
SHP는 타임스탬프 정보를 사용 하 여 선호도를 유추 하는 반면 ELI5는 주석 및 점수만 제공 합니다. 후자는 이전에 만든 주석이 더 많은 가시성에서 더 높은 점수를 얻는 경향이 있기 때문에 선호도를 유추 하기에 충분하지 않습니다.
또한 더 많은 도메인의 데이터를 포함합니다.

| Dataset              | Size | Comments + Scores  | Preferences  | Number of Domains  |
| -------------------- | ---- | ------------------ | -------------| ------------------ |
| SHP                  | 385K | Yes                | Yes          | 18  |
| ELI5                 | 270K | Yes                | No           | 3   |


## 데이터 구조

각 하위 레딧에 대해 하나씩 18개의 디렉터리가 있으며 각 디렉터리에는 학습, 유효성 검사 및 테스트 데이터를 위한 JSONL 파일이 포함되어 있습니다.
Huggingface의 `datasets` 라이브러리를 사용하여 데이터를 가져오는 방법은 다음과 같습니다.

```python
from datasets import load_dataset

# Load all the data 
dataset = load_dataset("stanfordnlp/shp")

# Load one of the subreddits
dataset = load_dataset("stanfordnlp/shp", data_dir="askculinary")
```

다음은 `askculinary/train.json`의 예입니다.
```
{
`post_id`:"qt3nxl",
`domain`:"askculinary_train",
`upvote_ratio`:0.98,
`history`:"라즈베리를 분해하는 가장 좋은 방법은 무엇입니까? 이와 같이, 그러나 개별 씨앗까지: https:\/\/i.imgur.com\/Z0c6ZKE.jpg  핀셋으로 분리해 왔는데 시간이 많이 걸립니다. 이번 주말까지 약 10파운드가 소요됩니다.
`c_root_id_A`:"hkh25sc",
`c_root_id_B`:"hkh25lp",
`created_at_utc_A`:1636822112,
`created_at_utc_B`:1636822110,
`score_A`:340,
`score_B`:166,
`human_ref_A`:"Pectinex, 아마도?  셀룰로오스를 분해하는 효소입니다. citrus를 사용하면 pectinex의 묽은 용액에 밤새 앉아 결합 조직을 분해하게 됩니다. 결국 완벽한 citrus supremes가 됩니다. 라즈베리를 더 짧은 시간 동안 앉게 되면 같은 방식으로 종자를 분리할 수 있는지 궁금합니다.  여기 예제가 있습니다. https:\/\/www.chefsteps.com\/activities\/perfect-citrus-supreme",
`human_ref_B`:"라즈베리 주스는 처음에는 밝은 얼룩을 만들지만 몇 주 후면 거의 아무것도 사라지기 시작합니다. 천연 염료 세계에서 탈주 염료로 알려진 것은 세탁이나 빛에 노출되지 않아도 사라질 것입니다. 그녀가 드레스에 이 얼룩의 멋진 사진을 많이 얻기를 바랍니다. 곧 그것이 그녀가 남긴 전부이기 때문입니다."
`labels`:1,
`seconds_difference`:2.0,
`score_ratio`:2.0481927711
}
```

상기 필드들은:
- ```post_id```: the ID of the Reddit post (string)
- ```domain```: subreddit and split the example is drawn from, separated by underscore (string)
- ```upvote_ratio```: 긍정 (일명 upvotes) (float) 게시물에서 받은 투표 비율입니다.
- ```history```: Post title concatented to post body (string)
- ```c_root_id_A```: comment A의 ID (string)
- ```c_root_id_B```: comment B (string)의 ID
- ```created_at_utc_A```: utc timestamp of when comment A is created (integer)
- ```created_at_utc_B```: utc timestamp of when comment B is created (integer)
- ```score_A```: (# positive votes - # negative votes + 1) received by comment A (integer)
- ```score_B```: (# positive votes - # negative votes + 1) received by comment B (integer)
- ```human_ref_A```: comment A의 텍스트 (string)
- ```human_ref_B```: comment B의 텍스트 (string)
- ```labels```: 선호도 레이블 -- A가 B보다 선호되는 경우 1이고, B가 A보다 선호되는 경우 0입니다. 레이블 분포가 대략 50/50이 되도록 무작위화되었습니다. (정수)
- ```seconds_difference```: 덜 선호되는 코멘트가 생성된 후 몇 초 후에 더 선호되는 코멘트가 생성되었는지(항상 >= 0일 것임) (정수)
- ```score_ratio```: 더 선호하는 댓글의 점수와 덜 선호하는 댓글의 점수의 비율 (>= 1) (float)


## Dataset Design

### 도메인 선택

데이터는 *서브레딧* 이라는 토픽별 포라로 구성된 공개 포럼인 Reddit에서 공급됩니다.
예를 들어 `askculinary` 하위 레딧은 사용자가 요리 관련 질문을 하고 다른 사용자에 의해 응답 되는 것입니다.

SHP에는 18개의 다른 하위 레딧에서 긁어낸 주석에 대한 열차, 유효성 검사 및 테스트 분할이 포함되어 있습니다. 우리는 다음을 기반으로 하위 레딧을 선택했습니다.
1. 잘 알려진 것인지 여부(가입자수 >= 100K)
2. 게시물이 질문 또는 지시를 내릴 것으로 예상되었는지 여부
3. 응답이 얼마나 *도움이* 되는지에 따라 평가되는지 여부
4. 코멘트가 전적으로 개인 경험에 대한 것이 아니라 일부 객관성에 뿌리를 두어야 하는지 여부(예: `askscience` 대 `AskAmericans`)입니다.

열차/검증/테스트 분할은 하위 레딧의 포스트 ID를 각각 90%/5%/5% 비율로 분할하여 생성되어 여러 분할에 포스트가 나타나지 않는다.
상이한 게시물들은 상이한 수의 코멘트들을 갖기 때문에, 각각의 분할에서의 선호들의 수는 정확히 90%/5%/5%가 아니다:

| subreddit          |    train | validation | test | total |
| ------------------ | -------: | ---------: | ---: | ----: |
| askacademia        |    31450 |       2095 | 1708 | 35253 |
| askanthropology    |     3910 |        203 |  268 |  4381 |
| askbaking          |    44007 |       2096 | 1544 | 47647 |
| askcarguys         |     3227 |        159 |  117 |  3503 |
| askculinary        |    45710 |       2094 | 2563 | 50367 |
| askdocs            |     6449 |        315 |  455 |  7219 |
| askengineers       |    57096 |       3154 | 2638 | 62888 |
| askhistorians      |    3264 |       113 | 164 | 3541 |
| askhr              |    8295 |       641 | 395 | 9331 |
| askphilosophy      | 10307 | 608 | 677 | 11592 |
| askphysics         | 7364 | 409 | 587 | 8360 |
| askscience         | 13316 | 899 | 977 | 15192 |
| asksciencefiction  | 29382 | 1576 | 1987 | 32945 |
| asksocialscience   | 2706 | 147 | 188 | 3041 |
| askvet             |     3300 |        170 |  224 |  3694 |
| changemyview       | 38173 | 1637 | 1836 | 41646 |
| explainlikeimfive  | 19592 | 1014 | 1070 | 21676 |
| legaladvice        | 21170 | 1106 | 1011 | 23287 |
| ALL | 348718 | 18436 | 18409 | 385563 |

### 데이터 선택

포스트/댓글의 점수는 1에 사용자로부터의 상향 투표 수(승인)를 곱하고 하향 투표 수(승인 취소)를 뺀 값입니다.
점수의 값은 상대적입니다. 트래픽이 많은 하위 레딧(게시물)에서는 점수가 높은 게시물(댓글)이 더 많습니다.
게시물에서 더 일찍 게시된 댓글은 단순히 노출이 많아 점수가 더 높은 경향이 있을 것이므로 선호도를 추론할 때 타임스탬프 정보를 사용하는 것이 필수적이다.

게시물 P와 두 개의 주석(A,B)이 주어지면 데이터 세트에 선호도 A > B만 포함했다.
1. A는 *늦지 않게* B로 작성되었고 A는 B보다 높은 점수를 갖는다.
2. 게시물은 2023년 이전에 만들어진 셀프-포스트(즉, 텍스트의 본문이고 다른 페이지로의 링크가 아님)이며, 편집되지 않았으며, NSFW(18 초과)가 아니다.
3. 삭제된 사용자, 사회자 또는 게시물 작성자에 의해 어떠한 코멘트도 이루어지지 않았다. 게시물은 삭제된 사용자 또는 진행자가 만들지 않았습니다.
4. 게시물은 점수가 >=10이고 각 코멘트는 점수가 >=2(적어도 한 번 이상 투표)이다.

주석이 있는 게시물은 `n` 데이터에서 최대 (`n` `2`) 환경 설정을 선택할 수 있습니다.
게시물당 댓글 수는 파레토 배포이기 때문에 상대적으로 적은 수의 게시물이 데이터를 지배하는 것을 방지하기 위해 게시물당 50개의 댓글으로 스크래핑을 제한했다.
이는 위의 모든 기준을 충족해야 하기 때문에 실제로는 훨씬 적은 수이지만 각 게시물에 데이터 집합에서 최대 (`50` `2`를 선택) 주석이 있을 수 있음을 의미 합니다.

레드딧은 서브레드딧마다 상위 1000개 이상의 게시물을 얻는 것을 매우 어렵게 만든다.
최상위 1,000개의 게시물부터 시작하여 Reddit의 검색 기능을 사용하여 각 게시물과 가장 유사한 25개의 게시물을 검색하여 하위 레딧당 최대 7500개의 고유한 게시물 ID를 얻었다.


### 전처리

전처리를 최소한으로 유지하려고 노력했습니다. 서브레디트-특정 약어는 확장되었다(예를 들어, "CMV"를 "내 견해를 변경"으로).
하이퍼링크에서, 참조 텍스트만이 유지되고 URL이 제거되었다(URL이 기입된 경우, 그것은 유지되었다).


## 기본 설정 모델 만들기

### Finetuning

인간 선호도(예를 들어, NLG 평가 또는 RLHF 보상 모델에 대해)를 예측하기 위해 모델을 피니튜닝하고자 하는 경우, 여기 몇 가지 유용한 팁이 있다:

1. **데이터를 전처리합니다.* * 총 입력 길이는 모델의 토큰 제한 (일반적으로 512 토큰)에 적합 해야 합니다.
FLAN-T5와 같은 모델은 위치 임베딩을 사용하지만 512개 토큰 이상의 입력에서 손실을 조정하면 손실이 수렴하지 않는다는 것을 발견했다.
이를 방지 하려면 게시글 텍스트 (`history` 필드에서)를 가능한 한 잘라서 전체 입력이 512 토큰 아래에 있도록 합니다 (그러나 주석을 잘리지 않음).
여전히 512 토큰 이상이면 예제를 건너뜁니다.
2. **충분히 큰 모델을 사용** 합니다.
모든 트레이닝 데이터에 걸쳐 단일 FLAN-T5-xl 모델을 피니튜닝하는 것은 72-73%(전체 입력이 토큰 한계 내에 맞는 예시의 모든 도메인에 걸쳐) 사이의 테스트 정확도를 제공해야 하며, 개별 서브레딧의 경우 65-80% 범위이다.
3. **도메인 내 예측을 수행 합니다.* * 하위 레딧이 관련이 없는 경우 도메인 외 성능이 좋지 않습니다 (예: 환경 설정을 미세 조정 하 고 환경 설정을 테스트 하는 경우 `askculinary` `askcarguys`).
4. **더 적은 에폭에 대해 훈련** InstructGPT 종이 페이퍼는 1 에폭에 대해서만 보상 모델을 훈련하는 것을 제안합니다.
동일한 코멘트가 여러 선호도에서 나타나기 때문에 데이터에 과적합되기 쉽다.
5. **더 적은 데이터에 대한 교육이 도움이 될 수 있습니다* *.
큰 `score_ratio`를 사용하는 환경 설정(예: 주석 B의 점수가 2배인 주석 A)은 모델을 조정하기 위한 더 강력한 신호를 제공하므로 특정 이상의 환경 설정만 고려하려는 것일 수 있습니다 `score_ratio`.
게시물당 선호도 수는 Pareto-distributed이므로 모델이 특정 게시물에 과도하게 적합 하는 것을 방지 하기 위해 특정 게시물에서 선호도 수를 제한 하는 것이 좋습니다.

### 평가

약한 기본 설정보다 강력한 기본 설정을 예측하는 것이 더 쉽기 때문에 단일 정확도 값을 보고하는 대신 성능 곡선을 `score_ratio`의 함수로 보고하는 것이 좋습니다.
예를 들어, 여기 위의 제안들을 사용하여 질문적 데이터에 대해 트레이닝된 FLAN-T5-xl 모델에 대한 정확도 곡선이 있다.
주황색 라인은 2+ 스코어 비율을 갖는 선호도에만 피니튜닝하고 과적합을 방지하기 위해 각 포스트로부터 5개 이하의 선호도를 사용하는 것이다:

로 이루어진 군에서 선택되는 어느 하나인 것을 특징으로 하는 유기 발광 표시 장치. [그래프](curve.png)

우리는 더 낮지만 더 높은 품질의 데이터를 미세 조정하는 것이 실제 단점이 없는 점수 비율이 3.5 미만인 테스트 데이터에 대한 더 높은 정확도로 이어진다는 것을 알 수 있다!
토큰 제한 내에 입력이 맞지 않는 예는 모델에서 처리할 것으로 예상할 수 없기 때문에 실험에서 제외되었다.

### SteamSHP - Open-Source Preference Model

우리는 SHP 데이터 세트와 Anthropic의 HH-RLHF의 도움 데이터 모두에 대해 두 개의 FLAN-T5 모델을 미세 조정했다. 그들은
- 테스트 데이터에서 72.8%를 달성하는 3B 매개 변수 모델인 [SteamSHP-XL](https://huggingface.co/stanfordnlp/SteamSHP-flan-t5-xl)입니다.
- 테스트 데이터에서 72.0%를 달성하는 780M 매개 변수 모델인 [SteamSHP-Large](https://huggingface.co/stanfordnlp/SteamSHP-flan-t5-large)입니다.

NLG 평가, RLHF에 대한 보상 모델 구축 또는 적합하다고 생각하는 다른 목적으로 스팀SHP를 사용하는 것이 좋습니다!


## 편향 및 제한 사항

### Biases

NSFW(18세 이상) 콘텐츠로 게시물을 걸러내고, 잘 조정되고 괴롭힘과 편협에 대한 정책이 있는 하위 레딧을 선택했지만 일부 데이터에는 차별적이거나 해로운 언어가 포함될 수 있다.
데이터는 데이터 세트 작성자의 보기를 반영하지 않습니다.
이러한 하위 레딧의 레딧 사용자도 광범위한 모집단을 대표하지 않는다.
하위 레딧별 인구 통계 정보는 사용할 수 없지만 전체 레딧 사용자는 불균형적으로 남성이며 선진국, 서양 및 영어 사용 국가에서 왔습니다 ([Pew Research](https://www.pewresearch.org/internet/2013/07/03/6-of-online-adults-are-reddit-users/)).
이 데이터에 대해 학습된 모델을 사용하기 전에 이 점을 염두에 두십시오.

### 제한 사항

SHP의 선호도 레이블은 지시/질문이 주어졌을 때 한 응답이 다른 응답과 얼마나 *도움이* 되는지 반영 하기 위한 것입니다.
SHP는 좋은 독성 검출기를 배우는 데 필요한 독성 함량을 포함하도록 설계되지 않았기 때문에 위해 최소화에서 사용하기 위한 것이 아니다.
환경 설정 레이블이 더 적은 해를 나타내는 데이터를 찾는 경우 [Anthropic의 HH-RLHF](https://huggingface.co/datasets/Anthropic/hh-rlhf)의 유해성 분할을 권장합니다.

또 다른 한계는 SHP에서 선호되는 응답이 반드시 더 사실적인 응답은 아니라는 것이다.
일부 논평은 그들의 반응을 정당화하기 위해 인용을 제공하지만 대부분은 그렇지 않다.
여기에는 `askhistorians` 하위 레딧과 같은 예외가 있으며, 이는 크게 조정되며 답변이 인용을 제공할 것으로 예상된다.

SHP의 집단 선호도 라벨은 가중치가 없는 합계를 취하기 전에 사용자에게 각 코멘트에 독립적으로 투표하도록 요청하면 반드시 얻을 수 있는 것은 아니다.
Reddit에 대한 주석 점수는 공개적이며 사용자 환경 설정에 영향을 미치는 것으로 알려져 있기 때문입니다. 높은 점수는 [(Muchnik et al., 2013)](https://pubmed.ncbi.nlm.nih.gov/23929980/)보다 긍정적인 표를 얻을 가능성을 높입니다.
이 "허딩 효과"가 사용자의 선호도를 일시적으로 또는 영구적으로 이동시키는지 여부는 불분명하다.
따라서, SHP가 집단적 인간 선호도를 반영하지만, SHP에 대해 훈련된 모델은 개별 선호도가 다르게 집계되는 설정으로 일반화되지 않을 수 있다(예를 들어, 사용자는 현재 코멘트 점수를 전혀 보지 않고 독립적으로 투표하고, 사용자는 부여 후 투표 등).
그렉 스토다드가 지적해줘서 고마워요


## License

Last updated: 03/01/2023

이 데이터 세트는 Reddit과 직접 통신 또는 서면 동의 없이 [Reddit API 사용 약관](https://docs.google.com/a/reddit.com/forms/d/e/1FAIpQLSezNdDNK1-P8mspSbmtC2r86Ee9ZRbC66u929cG2GX0T9UMyw/viewform)에 따라 Reddit을 스크래핑하여 만들었습니다.
사용 약관에 따라 "사용자 콘텐츠"는 Reddit이 아닌 사용자 자신이 소유하고 있으며 Reddit은 "사용자 콘텐츠를 복사 및 표시 하기 위해 독점적이지 않고 양도할 수 없으며 공개되지 않으며 취소할 수 있는 라이선스"를 부여 합니다.

Reddit을 스크래핑 하 여 만든 데이터 집합은 연구 커뮤니티에서 널리 사용 됩니다. 예를 들어 Facebook AI 리서치는 Reddit에서 스크래핑 된 데이터를 사용 하 여 라이선스 없이 사용 하도록 만든 2019년 [ELI5](https://huggingface.co/datasets/eli5#source-data) 데이터 집합을 만들었습니다.
인류성 AI는 다른 방법론을 사용 하 여 환경 설정에 대 한 [Reddit을 스크래핑](https://arxiv.org/pdf/2112.00861.pdf) 합니다. 그러나이 데이터는 공개 되지 않았습니다.
정기적인 일정에서 Reddit의 전체 덤프를 사용할 수 있도록 하는 [PushShift Reddit 데이터 세트](https://arxiv.org/abs/2001.08435)도 라이선스 없이 사용할 수 있습니다 (알고 있는 범위).

우리는 책임을 지지 않으며 이 데이터 세트의 다운스트림 사용을 명시적으로 또는 암시적으로 지지하지 않는다.
우리는 향후 어느 시점에서든 SHP 데이터 세트와 이 라이선스를 수정할 수 있는 권한을 보유합니다.


## Contact

데이터에 대한 질문이 있는 경우 kawin@stanford.edu에 문의하십시오.
이 데이터 세트는 카윈 에타야라흐, 하이디(첸유) 장, 이중 왕 및 단 주라프스키에 의해 생성되었다.

## 인용

SHP는 다음 논문에서 제안한 기법을 이용하여 생성하였다. SHP 또는 스팀SHP 모델을 사용하는 경우 이 작업을 인용하십시오.

```
@InProceedings{pmlr-v162-ethayarajh22a,
  title = 	 {Understanding Dataset Difficulty with $\mathcal{V}$-Usable Information},
  author =       {Ethayarajh, Kawin and Choi, Yejin and Swayamdipta, Swabha},
  booktitle = 	 {Proceedings of the 39th International Conference on Machine Learning},
  pages = 	 {5988--6008},
  year = 	 {2022},
  editor = 	 {Chaudhuri, Kamalika and Jegelka, Stefanie and Song, Le and Szepesvari, Csaba and Niu, Gang and Sabato, Sivan},
  volume = 	 {162},
  series = 	 {Proceedings of Machine Learning Research},
  month = 	 {17--23 Jul},
  publisher = {PMLR},
}
```

## 참조

Ethayarajh, K., Choi, Y. &amp; Swayamdipta, S. (2022). Understanding Dataset Difficulty with $\mathcal{V}$-Usable Information. <i>Proceedings of the 39th International Conference on Machine Learning</i>, in <i>Proceedings of Machine Learning Research</i>. 162:5988-6008 Available from https://proceedings.mlr.press/v162/ethayarajh22a.html.