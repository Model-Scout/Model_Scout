---
language:
- ko
license: other
license_name: cc-by-nc-4.0-qa-with-kogl-images
license_link: LICENSE
task_categories:
- visual-question-answering
size_categories:
- 100K<n<1M
configs:
- config_name: all
  default: true
  data_files:
  - split: release
    path:
    - data/simple_name/*.parquet
    - data/multi_attr/*.parquet
- config_name: simple_name
  data_files:
  - split: release
    path: data/simple_name/*.parquet
- config_name: multi_attr
  data_files:
  - split: release
    path: data/multi_attr/*.parquet
---

# Korean Heritage Single-Turn SFT — Noncommercial Release

Target repository: `KETI-NLP/korean-heritage-qa`.

문화재 사진 1장과 user/assistant 1쌍으로 이루어진 한국어 QA 데이터입니다.
이름 식별 `simple_name`과 이름·시대·지정연도·소재지·분류를 묻는
`multi_attr` 문항을 포함합니다. 설명문 발췌 문항, reverse QA,
생성 VQA DPO와 합성 이미지는 포함하지 않습니다.

| 데이터셋 | KOGL-1 | KOGL-2 | 합계 |
|---|---:|---:|---:|
| simple_name | 82,040 | 5,610 | 87,650 |
| multi_attr | 277,900 | 19,700 | 297,600 |
| 합계 | 359,940 | 25,310 | 385,250 |

위 표의 KOGL 유형은 사진 자체의 조건입니다. **두 데이터셋의 자체 QA는 모두 CC BY-NC 4.0이며, QA 예제 전체의 상업적 이용은 이번 공개 라이선스에서 허용하지 않습니다.**

고유 이미지는 8,765장입니다. 같은 이미지가 여러 문항에 사용됩니다.
이미지는 Parquet에 실제 바이트로 포함되어 로컬 파일 경로에 의존하지 않습니다.

## Fields

| 필드 | 의미 |
|---|---|
| id | 원천 데이터셋 종류와 원천 행 번호 |
| dataset_type | `simple_name` 또는 `multi_attr` |
| image | Hugging Face Image, 내장 이미지 바이트 |
| messages | user 질문과 assistant 정답. 이미지 위치는 `<image>` 표시 |
| qa_license | 모두 `CC-BY-NC-4.0` |
| image_license | 원본 사진의 `KOGL-1` 또는 `KOGL-2` |
| license_scope | 자체 QA와 제3자 사진의 적용 범위를 구분 |
| source_url | 사진별 라이선스를 확인할 수 있는 원문 페이지 |
| source_image_url | 원래 사진 URL |
| license_url | 공공누리 이용조건 |
| attribution | 출처표시 문구 |
| image_sha256 | 이미지 파일 SHA-256 |

자체 QA와 사진의 조건을 함께 준수해야 합니다. 사진에 적용되는 공공누리
조건은 QA에 적용하는 CC BY-NC 4.0으로 대체되지 않습니다.
라이선스 전문과 적용 범위는 LICENSE를 참조하십시오.

## Loading

```python
from datasets import load_dataset

repo_id = "KETI-NLP/korean-heritage-qa"
ds = load_dataset(repo_id, "all", split="release", streaming=True)
row = next(iter(ds))
print(row["dataset_type"], row["qa_license"], row["image_license"])
print(row["messages"])
row["image"].show()

# One task subset:
multi_attr = load_dataset(repo_id, "multi_attr", split="release", streaming=True)
```

## Split and ordering

`release`는 공개 후보 전체를 의미합니다. 원래 HF train/test 분할을
복원한 것이 아니며, 원천의 두 분할에서 선별된 항목을 포함합니다.
별도의 평가용 holdout은 제공하지 않습니다. 압축을 위해 같은 이미지의
문항을 묶어 저장했으므로 학습 시 shuffle이 필요합니다. 평가 분할을
만들 때에는 최소한 image_sha256을 기준으로 묶고, 가능하면 문화재 단위로
나누어 같은 문화재의 다른 문항이 양쪽에 섞이지 않도록 해야 합니다.

## Rights and limitations

2026-10-05에 확인한 국가유산포털의 사진별 공공누리 표시를 기준으로
선별했습니다. 수정된 현재 이미지의 배포에 맞춰 1·2유형만 포함했습니다.
사진은 원천 수집 과정에서 RGB JPEG로 변환되었고, 이번 변환에서는 그
바이트를 그대로 보존했습니다. 원문 조건을 새로운 CC 라이선스로
대체하지 않습니다. QA 예제 전체는 비상업적 이용 조건으로 제공합니다.

자체 작성 QA 중 발행자가 권리를 보유한 부분은 CC BY-NC 4.0으로 제공합니다.
출처표시, 변경사항 표시, 비상업적 이용 조건을 준수해야 합니다.
제3자 이미지는 각 image_license에 따라 이용하십시오. 이 라이선스는
사실정보 자체나 법률상 자유롭게 이용할 수 있는 요소에 새 권리를 설정하지 않습니다.

권리자는 자체 QA에 대해 나중에 별도의 상업적 이용허락을 부여할 수 있습니다.
이는 KOGL-2 사진의 비상업 조건을 변경하지 않습니다. 이번 공개본에는
상업적 이용허락이 부여되어 있지 않습니다. 필터 결과는 법률 의견서가 아닙니다.

`ATTRIBUTIONS.jsonl`에 이미지별 출처·이용조건·변경 내역을 보존했습니다.
`AUDIT_NOTES.txt`에는 제외와 보류 기준이 있습니다. 이름과 속성의 정확도,
문항 품질을 새로 전수 검수한 데이터셋은 아닙니다.

공식 자료:

- https://www.kogl.or.kr/info/license.do
- https://www.khs.go.kr/html/HtmlPage.do?pg=/guide/copyright.jsp&mn=NS_08_03
- https://www.heritage.go.kr/heri/cul/selectCulImageList.do
