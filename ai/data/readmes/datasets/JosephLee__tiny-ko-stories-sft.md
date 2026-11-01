---
license: cc-by-4.0
language:
- ko
task_categories:
- text-generation
tags:
- korean
- children-stories
- instruction-tuning
- education
pretty_name: Tiny-Ko-Stories SFT
---

# Tiny-Ko-Stories SFT (요청 → 이야기)

『모두의 LLM with 파이썬』 실습용 지시 미세조정(SFT) 데이터입니다.

| 필드 | 내용 |
|---|---|
| `request` | 이야기를 요청하는 짧은 문장 |
| `story` | 요청에 해당하는 어린이 이야기 |

- train 43,852쌍 / validation 2,308쌍
- 이야기 길이 340자 이하

## 출처와 변경 사항

이 데이터는 psymon의 [Tiny-Ko-Stories](https://huggingface.co/datasets/psymon/Tiny-Ko-Stories)
([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/))를 가공한 것입니다.

- 원본의 1,000,001번째 이야기부터 150,000편을 사용했습니다.
- 340자를 넘는 이야기는 제외했습니다.
- 이야기 앞부분에서 등장인물 이름, 동물, 장소, 때를 규칙으로 찾아 요청 문장을 자동 생성했습니다.
- 이야기 본문은 바꾸지 않았습니다.

원본은 여러 AI 모델로 생성된 합성 데이터이며, 원본 카드의 권장·비권장 용도와 한계가 이 데이터에도 그대로 적용됩니다.
사실 질의응답 학습이나 사람 검수 없는 어린이 대상 서비스에는 적합하지 않습니다.

## 라이선스

CC BY 4.0. 사용할 때 이 데이터셋과 원본 Tiny-Ko-Stories의 출처를 함께 표기해 주세요.
