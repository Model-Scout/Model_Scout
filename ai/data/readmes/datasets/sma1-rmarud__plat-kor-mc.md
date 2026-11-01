---
language:
- ko
license: cc-by-nc-sa-4.0
task_categories:
- question-answering
- multiple-choice
tags:
- legal
- tax-law
- korean-law
- multiple-choice
- benchmark
size_categories:
- n<1K
---

# PLAT-KOR-MC

**PLAT (Predicting the Legitimacy of punitive Additional Tax)** - 한국어 객관식 (적법/부적법)

## 데이터셋 설명

한국 조세법 판례 100개를 적법/위법 2지선다형 문제로 구성한 데이터셋입니다.

## 데이터셋 구조

| 필드 | 타입 | 설명 |
|------|------|------|
| `case_no` | string | 사건 번호 (예: "2011구합2638") |
| `case_info` | string | 사건 개요 (당사자, 배경) |
| `facts` | string | 사건 사실관계 |
| `claims` | string | 원고와 피고의 주장 |
| `reasoning` | string | 법원의 법적 판단 |
| `decision` | string | 법원의 최종 판결 |
| `lawfulness` | boolean | 과세 처분의 적법 여부 (True/False) |

## 사용법

아래의 github를 참조.
https://github.com/lbox-kr/plat

## 인용

```bibtex
@misc{choi2026taxationperspectiveslargelanguage,
      title={Taxation Perspectives from Large Language Models: A Case Study on Additional Tax Penalties}, 
      author={Eunkyung Choi and Youngjin Suh and Siun Lee and Hongseok Oh and Juheon Kang and Won Hur and Hun Park and Wonseok Hwang},
      year={2026},
      eprint={2503.03444},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2503.03444}, 
}
```

## 라이선스

CC BY-NC-SA 4.0