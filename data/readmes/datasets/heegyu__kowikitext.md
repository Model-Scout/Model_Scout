---
license: cc-by-sa-3.0
---
한국어 위키피디아 article 덤프(20221001)
- 1334694 rows
- download size: 474MB

```python
from datasets import load_dataset

ds = load_dataset("heegyu/kowikitext", "20221001")
ds["train"][0]
```

```
{'id': '5',
 'revid': '595831',
 'url': 'https://ko.wikipedia.org/wiki?curid=5',
 'title': '지미 카터',
 'text': '제임스 얼 카터 주니어(, 1924년 10월 1일 ~ )는 민주당 출신 미국 39대 대통령 (1977년 ~ 1981년)이다.\n생애.\n어린 시절.\n지미 카터는 조지아주 섬터 카운티 플레인스 마을에서 태어났다.\n조지아 공과대학교를 졸업하였다. 그 후 해군에 들어가 전함·원자력·잠수함의 승무원으로 일하였다. 1953년 미국 해군 대위로 예편하였고 이후 땅콩·면화 등을 가꿔 많은 돈을 벌었다. 그의 별명이 "땅콩 농부" (Peanut Farmer)로 알려졌다.\n정계 입문.\n1962년 조지아주 상원 의원 선거에서 낙선하나 그 선거가 부정선거 였음을 ... "
 }
```
