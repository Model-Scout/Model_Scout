---
license:
- odc-by
- cc-by-4.0
language:
- ko
- en
task_categories:
- text-generation
size_categories:
- 10M<n<100M
pretty_name: Perdix Pretrain Data
tags:
- pretraining
- web
- math
- korean
configs:
- config_name: korean
  data_files: fineweb2-kor/data/kor_Hang/train/*.parquet
- config_name: web_en
  data_files: dclm-baseline/**/*.parquet
- config_name: math
  data_files: finemath-4plus/finemath-4plus/*.parquet
---

# Perdix-Pretrain-Data

[Perdix-1.1B-Base](https://huggingface.co/prismdata/Perdix-1.1B-Base) 사전학습에 쓴 원본 데이터를 그대로 모아 둔 것입니다. 새로 만든 데이터는 없고, 아래 세 공개 데이터셋에서 실제로 쓴 parquet 파일만 골라 복사했습니다. 어떤 파일을 어떤 비율로 썼는지 남겨 두려는 목적입니다.

The exact subset of three public datasets (DCLM-baseline, FineWeb2 kor_Hang, FineMath 4+) used to pretrain Perdix-1.1B-Base. Files are unmodified copies; this repository only records which shards were used. 335 parquet files, about 89.7M documents, 178 GB.

## 구성

| 폴더 | 원 데이터셋 | 파일 | 문서 수 | 크기 | 토큰 수* | 라이선스 |
|---|---|---|---|---|---|---|
| `fineweb2-kor/` | [HuggingFaceFW/fineweb-2](https://huggingface.co/datasets/HuggingFaceFW/fineweb-2) `kor_Hang/train` 전부 | 25 | 60.9M | 105.8 GB | 45.6B | ODC-By |
| `dclm-baseline/` | [mlfoundations/dclm-baseline-1.0-parquet](https://huggingface.co/datasets/mlfoundations/dclm-baseline-1.0-parquet) 일부 | 246 | 22.1M | 53.9 GB | 29.7B | CC-BY-4.0 |
| `finemath-4plus/` | [HuggingFaceTB/finemath](https://huggingface.co/datasets/HuggingFaceTB/finemath) `finemath-4plus` 전부 | 64 | 6.7M | 18.4 GB | 10.8B | ODC-By |

\* Perdix 토크나이저(BPE 49,152)로 센 값. 문서 사이 `<|endoftext|>` 포함.

DCLM-baseline은 전체가 수 TB라 일부만 썼습니다. global-shard 01~10 각각의 `local-shard_0_of_10`에서 앞쪽 파일만 골랐고(01~06은 shard 0~24, 07~10은 shard 0~23), 고르는 규칙은 `download_raw_data.sh`에 그대로 있습니다. FineWeb2 한국어와 FineMath 4+는 train 전부입니다.

각 parquet의 컬럼은 원 데이터셋 그대로이며, 학습에는 `text` 컬럼만 썼습니다.

## 학습에 어떻게 썼나

- 세 소스를 합쳐 86B 토큰 중 30B 토큰을 학습했습니다. 각 소스에서 2,048토큰 창을 무작위로 뽑는 방식이라 같은 구간이 우연히 다시 뽑힐 수는 있지만, 전체를 한 바퀴 돌지는 않았습니다.
- 믹싱 비율은 영어 65% / 한국어 30% / 수학 5%에서 시작해 25% / 50% / 25%로 서서히 바꿨습니다.
- 이 parquet을 토큰화한 `.bin`은 [prismdata/Perdix-Pretrain-Packed](https://huggingface.co/datasets/prismdata/Perdix-Pretrain-Packed)에 따로 올려 두었습니다.
- 토큰화·패킹 코드는 `pretrain_data.py`, 학습 코드는 `pretrain.py`로 [github.com/theprismdata/Perdix](https://github.com/theprismdata/Perdix)에 있습니다.

## 받기

```bash
hf download prismdata/Perdix-Pretrain-Data --repo-type dataset --local-dir raw-data
```

원 저장소에서 같은 파일을 직접 받으려면 `download_raw_data.sh`를 쓰면 됩니다. 결과 폴더 구조가 같습니다.

```bash
DEST=raw-data ./download_raw_data.sh
```

## 라이선스

이 저장소는 원 데이터셋의 라이선스를 그대로 따릅니다.

- `fineweb2-kor/`, `finemath-4plus/`: [ODC-By 1.0](https://opendatacommons.org/licenses/by/1-0/). 원 데이터셋 카드에 따라 [Common Crawl 이용약관](https://commoncrawl.org/terms-of-use)도 함께 적용됩니다.
- `dclm-baseline/`: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/).

출처를 밝힐 때는 이 저장소가 아니라 원 데이터셋(FineWeb2, DCLM-baseline, FineMath)을 인용해 주세요. 원 데이터셋에서 특정 문서의 삭제 요청이 처리되면 이 저장소에도 반영하겠습니다.
