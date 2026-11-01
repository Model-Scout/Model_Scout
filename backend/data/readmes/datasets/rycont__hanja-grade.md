---
license: unknown
language:
- ko
pretty_name: Hanja Grade
size_categories:
- 1K<n<10K
---

# 한국어문회 등급별 선정한자 CSV 데이터셋

[사단법인 한국어문회](https://www.hanja.re.kr/)에서 분류한 급수별 한자 데이터셋입니다. 공식 홈페이지의 학습자료 / 기타자료에 업로드된 Xls 파일을 CSV 파일로 변환하여 제공합니다.

데이터의 저작권은 한국어문회에 있습니다. 데이터의 오류나 문제가 있을 경우 이슈를 남겨주시면 확인 후 수정하겠습니다.

## 데이터 구성

### 필드

```typescript
interface Hanja {
    // 대표 독음
    main_sound: string;

    // 한국어문회 분류 급수
    level: string;

    // 한자
    hanja: string;

    // 의미
    meaning: Meaning[];

    // 부수
    radical: string;

    // 획수
    strokes: number;

    // 총 획수
    total_strokes: number;
}

type Meaning = [
    // 의미
    string[],

    // 한자 독음
    string[]
]
```

---

Made with ❤️ by [rycont](https://bento.me/3)
