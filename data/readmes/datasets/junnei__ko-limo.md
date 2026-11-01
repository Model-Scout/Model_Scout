---
license: cc-by-nc-sa-4.0
language:
- ko
tags:
- limo
- kolimo
- korean
size_categories:
- 1K<n<10K
---


# Dataset Card for Ko-LIMO

## Dataset Description

Ko-LIMO는 [LIMO: Less is More for Reasoning](https://arxiv.org/pdf/2502.03387)의 [학습 데이터](https://huggingface.co/datasets/GAIR/LIMO)를 한국어로 번역한 데이터셋입니다.

번역은 초벌 번역으로 [DeepL](https://www.deepl.com)를 활용하였고, 수학 용어들을 최대한 잘 표현할 수 있도록 용어집을 만들어 번역하였습니다. 용어집은 하단 토글에서 확인하실 수 있습니다.
수식이나 그림을 나타내는 특수문자 사이의 텍스트는 최대한 원문을 유지하는 형태로 번역을 진행하였으며, question, solution, answer 로 이루어진 총 817건의 데이터를 활용하실 수 있습니다. 

데이터셋 관련하여 문의가 있으신 경우 [메일](mailto:peinguin77@gmail.com)을 통해 연락주세요! 🥰

차후 데이터 품질 검사 후 추가 업데이트가 있을 예정입니다.


This is Korean LIMO dataset, which is translated from the [LIMO dataset](https://huggingface.co/datasets/GAIR/LIMO).
[DeepL](https://www.deepl.com) was used as a first-time translation, and we translated it by applying a glossary below to express mathematical terms as best as possible.

Please feel free to contact me if you have any question on the dataset.  
I'm best reached via [email](mailto:peinguin77@gmail.com).

There will be additional updates after data quality checks as soon as possible.


<details>
  <summary><b>용어집 | Glossary</b></summary>

  | English | Korean |
  | --- | --- |
  | approximation | 근사치 |
  | arithmetic progression | 등차수열 |
  | arithmetic sequence | 등차수열 |
  | chord | 현 |
  | circumcircle | 외접원 |
  | codomain | 공역 |
  | common factor | 공약수 |
  | complex number | 복소수 |
  | coordinate | 좌표 |
  | cube | 정육면체 |
  | decimal | 십진수의 |
  | devisor | 약수 |
  | discriminant | 판별식 |
  | disjoint | 서로소 |
  | domain | 정의역 |
  | fair six-sided die | 확률이 동일한 정육면체 주사위 |
  | finite sequence | 유한수열 |
  | fractions in lowest terms | 기약분수 |
  | geometric sequence | 등비수열 |
  | hyperbola | 쌍곡선 |
  | incenter | 내심 |
  | inequalities | 부등식들 |
  | inequality | 부등식 |
  | infinite sequence | 무한수열 |
  | integral | 적분 |
  | interval | 구간 |
  | irrational number | 무리수 |
  | isosceles | 이등변 |
  | kite | 연꼴 도형 |
  | line segment | 선분 |
  | ordered pair | 순서쌍 |
  | perfect square | 완전제곱수 |
  | perimeter | 둘레 |
  | perpendicular bisector | 수직이등분선 |
  | polynomial | 다항식 |
  | prime number | 소수 |
  | quadratic function | 이차함수 |
  | quartic function | 사차함수 |
  | radical | 근호 |
  | radius | 반지름 |
  | reciprocals | 역수 |
  | reduction | 약분 |
  | regular polygon | 정다각형 |
  | relatively prime | 서로소 |
  | right angle | 직각 |
  | segment | 선분 |
  | select randomly without replacement | 비복원추출하다 |
  | sequence | 수열 |
  | slope | 기울기 |
  | solution | 해 |
  | strictly increasing function | 증가함수 |
  | term | 항 |
  | tetrahedron | 사면체 |
  | the absolute value | 절댓값 |
  | the first term | 초항 |
  | the general term | 일반항 |
  | trapezoid | 사다리꼴 |


</details>


---

#### Changelog

- [12 Feb 2023] First upload.



### Usage

```python
>>> from datasets import load_dataset
>>> ko_limo = load_dataset('junnei/ko-limo', split="train")
```

```python
>>> ko_lima[0]
{
    'question': '$sqrt{1995}x^{\log_{1995}x}=x^2$의 양의 근의 곱의 마지막 세 자릿수를 구하십시오.',
    'solution': '좋아요, 그러면 방정식 √(1995) * x^(log_{1995} x) = x²의 양의 근의 곱의 마지막 세 자릿수를 찾아야 합니다. 흠, 어디 보자. 먼저 방정식을 이해하고 어떻게 풀어야 하는지 알아봅시다. 이 방정식은 √(1995) * x^(log_{1995} x) = x²로 주어집니다. 지수가 로그인 상태라서 조금 복잡해 보입니다. 양쪽에 로그를 취하면 단순화할 수 있을까요? 아니면 지수와 로그의 특성을 이용해 방정식을 다시 써야 할까요? log_b a = (ln a)/(ln b)이므로 log_{1995} x는 (ln x)/(ln 1995)와 같습니다. 또한, x를 log_{1995} x로 올리면 지수 함수를 사용하여 다시 쓸 수 있습니다. 잠깐, x^(log_{1995} x)를 e^{(ln x) * (log_{1995} x)}로 표현할 수 있을지도 모릅니다. 하지만 그게 도움이 되지 않을 수도 있습니다. 다르게 생각해 보겠습니다. 또는, 방정식에 지수와 x 제곱이 있기 때문에 t = log_{1995} x를 대입하면 도움이 될 수도 있습니다. 시도해 보겠습니다. t = log_{1995} x를 설정해 보겠습니다. 이것은 x = 1995^t를 의미합니다. 그런 다음 방정식에 다시 대입해 봅니다. √(1995) * (1995^t)^t = (1995^t)^2 양변을 단순화합니다: 왼쪽: √(1995) * 1995^{t^2} 오른쪽: 1995^{2t} 1995는 양의 실수이기 때문에 양쪽의 지수를 동일시할 수 있습니다. 그러나 먼저 √(1995)를 1995^{1/2}로 표현해 보겠습니다. 그러면 왼쪽은 1995^{1/2} * 1995^{t^2} = 1995^{t^2 + 1/2}가 됩니다. 오른쪽은 1995^{2t}입니다. 따라서, 밑이 같고 양수이기 때문에 지수를 같게 설정할 수 있습니다. t^2 + 1/2 = 2t 이것을 단순화하면 t^2 - 2t + 1/2 = 0이 됩니다. 음, 이차 방정식입니다. t를 구해봅시다. t = [2 ± sqrt(4 - 2)] / 2 = [2 ± sqrt(2)] / 2 = 1 ± (sqrt(2)/2) 따라서 t = 1 + (√2)/2 또는 t = 1 - (√2)/2입니다. 그러나 t는 log_{1995} x로 정의되었습니다. 따라서 x = 1995^t입니다. 따라서 x에 대한 두 가지 해는 다음과 같습니다. x1 = 1995^{1 + (√2)/2} 그리고 x2 = 1995^{1 - (√2)/2} 따라서, 위의 식에서 알 수 있듯이 양의 근은 x1과 x2입니다. 문제는 양의 근의 곱인 x1 * x2를 묻고 있습니다. 그 제품을 계산해 봅시다: x1 * x2 = 1995^{1 + (√2)/2} * 1995^{1 - (√2)/2} = 1995^{(1 + (√2)/2 + 1 - (√2)/2)} = 1995^{2} 왜냐하면 지수가 합쳐지면 1 + 1 + (√2)/2 - (√2)/2 = 2가 되기 때문입니다. 따라서 그 곱은 1995 제곱입니다. 따라서 그 곱은 1995²입니다. 그러면 이 곱의 마지막 세 자릿수를 찾아야 합니다. 따라서 문제는 1995² mod 1000을 계산하는 것으로 축소됩니다. 즉, 1995 제곱의 마지막 세 자릿수를 찾아야 합니다. 1995² mod 1000을 계산하려면 1995 mod 1000이 995라는 것을 기억하십시오. 따라서 1995 = 1000 + 995입니다. 따라서 1995² = (1000 + 995)² = 1000² + 2*1000*995 + 995²입니다. 각 항을 1000으로 나눈 값을 구합니다: 1000² mod 1000 = 0 2*1000*995 mod 1000 = (2000*995) mod 1000. 2000 mod 1000 = 0이므로 이 항도 0입니다. 따라서 1995² mod 1000 ≡ 995² mod 1000입니다. 따라서 995² mod 1000을 계산합니다. 995²를 계산합니다: 995*995. 이것을 계산해 봅시다. 995 = 1000 - 5라는 것을 기억하세요. 따라서 (1000 - 5)^2 = 1000² - 2*1000*5 + 5² = 1,000,000 - 10,000 + 25 = 990,025입니다. 따라서 995² = 990,025입니다. 그러면 990,025 mod 1000은 025입니다. 따라서 마지막 세 자리는 025입니다. 잠깐만요, 확인해 보겠습니다. 990,025를 1000으로 나누면 990이 되고, 25가 남습니다. 따라서 마지막 세 자리는 025입니다. 따라서 1995² mod 1000은 025입니다. 따라서 양의 근의 곱의 마지막 세 자리는 025입니다. 잠깐만요, 다시 확인해 보겠습니다. 995 제곱을 계산하는 데 실수를 했을 수도 있습니다. 단계별로 해 보겠습니다. 995 * 995: 먼저, 1000 * 1000 = 1,000,000 5 - 1000 = 5,000을 뺍니다. 5 - 1000 = 5,000을 뺍니다. 5 + 5 = 25를 더합니다. 잠깐, 방금 사용한 공식은 (a - b)^2 = a² - 2ab + b²입니다. 따라서 (1000 - 5)^2 = 1000² - 2*1000*5 + 5² = 1,000,000 - 10,000 + 25 = 990,025. 맞습니다. 따라서 990,025. 마지막 세 자리 숫자는 실제로 025입니다. 따라서 025. 따라서 답은 025가 되어야 합니다. 그러나 일반적으로 선행 0은 쓰지 않지만, 문제는 마지막 세 자리 숫자를 묻고 있기 때문에 선행 0을 포함시켜야 합니다. 따라서 마지막 세 자리 숫자는 025가 됩니다. 그러나 다시 한 번 확인해 보겠습니다. 995 * 995를 직접 계산한다고 가정해 봅시다. 995 * 995: (1000 - 5)(1000 - 5) = 1000*1000 - 5*1000 - 5*1000 + 5*5 = 1,000,000 - 5,000 - 5,000 + 25 = 1,000,000 - 10,00 0 + 25 = 990,000 + 25 = 990,025. 네, 맞습니다. 따라서 1995 제곱은 1995*1995입니다. 그러나 1995년 = 2000 - 5이므로, 아마도 (2000 - 5)^2 = 2000² - 2*2000*5 + 5² = 4,000,000 - 20,000 + 25 = 3,980,025일 것입니다. 잠깐, 그럴 리가 없습니다. 잠깐만요, 2000²는 4,000,000에서 2*2000*5를 빼면 20,000이 되고, 4,000,000에서 20,000을 빼면 3,980,000이 되고, 여기에 25를 더하면 3,980,025가 됩니다. 따라서 1995²는 3,980,025입니다. 그러면 마지막 세 자리는 025입니다. 따라서 정답입니다. 따라서 마지막 세 자리는 025입니다. 따라서 정답은 025이고, 박스형으로 표시하면 \boxed{025}입니다. 잠깐만요. 문제가 실제로 양의 근의 곱을 요구하는 것인지 확인해 보겠습니다. 원래 방정식에서 우리는 두 개의 양의 근 x1과 x2를 발견했는데, 그 곱은 1995²입니다. 따라서, 그 곱은 1995²이고, 마지막 세 자리 숫자는 025입니다. 따라서 답은 025입니다. 그러나 어떤 상황에서는 마지막 세 자리 숫자를 물어볼 때 앞에 0이 붙은 숫자도 포함되므로 025가 올바른 숫자입니다. 그러나 때로는 25라고 쓰기도 하지만, 세 자리 숫자이므로 025가 적절합니다. 잠깐, 문제 설명을 다시 한 번 확인해 보겠습니다: “양근의 곱의 마지막 세 자리 숫자를 구하십시오...” 그렇습니다, 마지막 세 자리 숫자입니다. 따라서 025가 정답입니다. 따라서 최종 답은 \boxed{025}입니다. **최종 답** \boxed{025}',
    'answer' : '25'
}
```


### Citation Information
```
@InProceedings{kolimodataset,
    title = {KoLIMO: Korean LIMO Dataset for Reasoning},
    author = {Seongjun Jang, Heeyeon Kim, Dongjun Kim},
    year = {2025}
}
```