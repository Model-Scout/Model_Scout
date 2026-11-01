---
license: cc-by-sa-4.0
language:
- ko
---
위키피디아 문서를 19개의 카테고리로 분류한 데이터셋입니다. 데이터에는 카테고리와 제목만 있습니다.

type1과 type2 전부 json 형식이며 type1은 key값이 제목, value값이 카테고리이며 type2는 key값이 카테고리, value값이 제목입니다. 문서 하나가 여러 개의 카테고리에 속해있는 경우도 있습니다.

분류 기준은 classification.csv를 참고하여 주시기 바랍니다. 카테고리 결정 기준은 signature가 문서에 포함되어 있는가이며 문서는 공백과 알파벳이 소문자로 변환된 채 비교되게 됩니다.

## 카테고리 종류

- human: 인간

- business_person: 기업인

- president: 대통령

- food: 음식

- creature: 생명체

- animal: 동물

- plant: 식물

- book: 책

- movie: 영화

- video_game: 게임

- music: 음악

- building: 건물

- ruins: 유적

- company: 회사

- language: 언어

- sofrware: 소프트웨어

- website: 웹사이트

- os: 운영 체제

- surname: 성씨

## data_type1.json

```
{
    "title": ["category", ...],
    ...
}
```

## data_type2.json

```
{
    "category": ["title", ...],
    ...
}
```