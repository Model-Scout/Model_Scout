---
license: apache-2.0
task_categories:
- text-generation
language:
- ko
size_categories:
- n<1K
---
# Ko-Arena-Hard-Auto

한국어 / [English](README_EN.md)

[리더보드](https://qwopqwop200.github.io/ko-arena-hard-auto/leaderboard.html) / [코드](https://github.com/qwopqwop200/ko-arena-hard-auto/tree/main)

ko-arena-hard-auto-v0.1는 한국어를 벤치마킹하기위한 자동 평가 도구의 질문 데이터셋입니다.
인간의 선호도와 높은 상관관계와 분리력을 가지고 있는 벤치마크 데이터셋인 [arena-hard-auto-v0.1](https://huggingface.co/datasets/lmarena-ai/arena-hard-auto-v0.1) 를 `GPT-4o`와 `o1`을 사용하여 한국어로 번역하고 수작업으로 검수한 데이터셋입니다.<br>

더 자세한 세부사항과 벤치마킹 결과는 [ko-arena-hard-auto 코드](https://github.com/qwopqwop200/ko-arena-hard-auto)를 참조하세요.
또한 원본 벤치마크에 관심이 있으시면 [arena-hard-auto 코드](https://github.com/lmarena/arena-hard-auto)를 참조하세요.

원래 문제의 형식을 유지하기 힘들어서 변경했습니다.<br>
인덱스 : `1, 28, 29`<br>
문제를 한국어로 유도하기 위해 문제 형식을 변경했습니다. 원래는 코드만 존재합니다.<br>
인덱스 : `30, 379, 190`<br>

참고문헌:
```
@article{li2024crowdsourced,
  title={From Crowdsourced Data to High-Quality Benchmarks: Arena-Hard and BenchBuilder Pipeline},
  author={Li, Tianle and Chiang, Wei-Lin and Frick, Evan and Dunlap, Lisa and Wu, Tianhao and Zhu, Banghua and Gonzalez, Joseph E and Stoica, Ion},
  journal={arXiv preprint arXiv:2406.11939},
  year={2024}
}
```