# Smart Korean beef auction price 스마트 한우 경매

Korean beef auction data from 한우경매.kr

### Context

The datasets are from a [website](http://www.xn--289al3w02jixo.kr/) for the Korean beef Online Auctions, by 축산플랫폼 주식회사.
I made a structured dataset by collecting and adjusting '혈통우'(pedigree cow) and '큰소'(big cow) auction results related datasets.

k-beef_raw.csv : whole data   

beef_train.csv : datasets for train  

beef_test.csv : datasets for test without '상태', '낙찰가' colums.    

beef_answer.csv : answers(price) for test   

### Content

일자 : the time in days that the bid was placed, from the start of the auction
번호 : unique identifier of an auction
출하주 : seller's name
개체번호 : unique identifier of an each cow
성별: gender of an each cow - 암(Female) , 수(male)
kpn : Korean Proven Bull No
계대 : generation of each kpn cow
중량 : weight
최저가 : reservation price
낙찰가 : winning bid
상태 : status
비고 : characteristics of each cow (ex. scars, pregnant, kpn...) 
종류 : type of cow - '혈통우'(pedigree cow) and '큰소'(big cow)
지역 : region


### Acknowledgements

The original dataset can be found [here](http://www.xn--289al3w02jixo.kr/dev/web/auction_result.html?code=10).


### Inspiration

For each cow, what is the relationship between '종류', kpn, and the '최저가'? 
Why don't you tokenize the '비고'. 
Read csv as pandas with encoding='cp949'.
refer to [한우경매 예측](https://www.kaggle.com/c/korean-beef-action/data)

출처: Kaggle (jskim1738/smart-korean-beef-auction)
태그: categorical, animals, tabular, text
라이선스: Unknown
수정일: 2021-12-31T06:46:03.540Z
