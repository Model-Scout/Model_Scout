---
language:
- ko
---

# ko-math-500

**ko-math-500** is a Korean-translated subset of 500 representative problems from the widely used MATH (Mathematics Aptitude Test of Heuristics) dataset, designed to evaluate the mathematical reasoning abilities of large language models.

The ko-math-500 subset is based on the standard evaluation set of 500 problems used in the 2023 paper Let’s Verify Step by Step for model performance comparison. The original dataset is publicly available at [HuggingFaceH4/MATH-500](https://huggingface.co/datasets/HuggingFaceH4/MATH-500). 

 The Korean translation was performed using the GPT-4o model. The data is structured in JSON format and includes LaTeX math expressions.

## Subject Distribution

| Subject                | Label    | Count |
|:-----------------------|:---------|------:|
| Algebra                | 대수학      |   124 |
| Intermediate Algebra   | 중급 대수학   |    97 |
| Prealgebra             | 기초 대수학   |    82 |
| Number Theory          | 정수론      |    62 |
| Precalculus            | 미적분학 준비  |    56 |
| Geometry               | 기하학      |    41 |
| Counting & Probability | 조합론 및 확률 |    38 |

## Structure

- `problem` : the math question
- `solution` : the detailed solution
- `answer` : the final answer
- `subject` : the math domain (one of seven subjects: Algebra, Counting & Probability, Geometry, Intermediate Algebra, Number Theory, Prealgebra, Precalculus)
- `level` : difficulty level represented by an integer from 1 to 5, where a subject’s easiest problems are assigned a level of 1 and the hardest problems are assigned a level of 5
- `id` : a unique identifier for each problem

```json
[
  {
    "problem": "직교 좌표 $(0,3)$를 극 좌표로 변환하시오. 답은 $r > 0$ 및 $0 \\leq \\theta < 2 \\pi$를 만족하는 형식 $(r,\\theta)$로 나타내시오.",
    "solution": "주어진 점 $(0,3)$에 대해 $r$은 다음과 같이 계산된다:\n\\[ r = \\sqrt{0^2 + 3^2} = 3. \\]  \n또한, 원점을 $(0,3)$과 연결하는 선은 양의 $x$축에 대해 $\\frac{\\pi}{2}$의 각도를 형성한다는 것을 알 수 있다.\n\n[asy]  \nunitsize(0.8 cm);  \n\ndraw((-0.5,0)--(3.5,0));  \ndraw((0,-0.5)--(0,3.5));  \ndraw(arc((0,0),3,0,90),red,Arrow(6));  \n\ndot((0,3), red);  \nlabel(\"$(0,3)$\", (0,3), W);  \ndot((3,0), red);  \n[/asy]  \n\n따라서, 극 좌표는 $\\boxed{\\left( 3, \\frac{\\pi}{2} \\right)}$이다.",
    "answer": "\\left( 3, \\frac{\\pi}{2} \\right)",
    "subject": "미적분학 준비",
    "level": 2,
    "id": "test/precalculus/807.json"
  }
]
```