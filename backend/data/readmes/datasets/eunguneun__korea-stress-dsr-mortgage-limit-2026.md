---
license: cc-by-4.0
language:
- ko
pretty_name: Korea Stress DSR Mortgage Limit 2026
tags:
- mortgage
- housing-finance
- dsr
- korea
- stress-dsr
configs:
- config_name: income_mortgage_limits
  data_files: income_mortgage_limits.csv
- config_name: credit_debt_mortgage_limits
  data_files: credit_debt_mortgage_limits.csv
---

# Korea Stress DSR Mortgage Limit 2026

2026년 한국의 스트레스 DSR 적용 조건을 바탕으로 연소득별 주택담보대출 추정 한도와 기존 신용대출 잔액에 따른 주담대 한도 변화를 정리한 공개 데이터셋입니다.

## Canonical source

- Resimanor 2026 주택금융·DSR 데이터센터  
  https://resimanor.com/housing-finance-dsr-data/
- 기준일: 2026-09-18

최신 설명, 계산 가정 및 정정 사항은 위 canonical source를 우선합니다.

## Archived versions

- Zenodo version 1.0 DOI: https://doi.org/10.5281/zenodo.22840870
- Zenodo concept DOI: https://doi.org/10.5281/zenodo.22840869
- Figshare DOI: https://doi.org/10.6084/m9.figshare.33948214
- GitHub: https://github.com/cheer710815-hub/resimanor-housing-finance-data

## Files

### income_mortgage_limits.csv

은행권 DSR 40%, 기존 대출 없음, 신규 주담대 실제금리 연 4.0%, 30년 만기, 원리금균등상환을 기본 가정으로 한 연소득별 비교 데이터입니다.

세 가지 심사금리 예시를 비교합니다.

- `no_stress`: 4.0%
- `regional_example`: 4.75%
- `capital_regulated_example`: 7.0%

### credit_debt_mortgage_limits.csv

연소득 8,000만원, 은행권 DSR 40%, 신용대출 금리 5%, 신용대출 DSR 산정만기 5년, 주담대 심사금리 7%, 주담대 30년 원리금균등상환을 가정한 비교 데이터입니다.

## Important notes

이 데이터는 동일한 가정에서 스트레스 DSR과 기존 부채가 주택담보대출 한도에 미치는 영향을 비교하기 위한 예시입니다. 실제 금융회사의 승인 한도를 의미하지 않습니다.

실제 대출 가능액은 LTV, 주택가격별 대출한도, 인정소득, 기존 부채, 금리 유형, 만기, 금융회사 내부 심사 등에 따라 달라질 수 있습니다.

## Source policy

제도 기준은 금융위원회 등 공식 자료를 우선합니다. 계산값과 제도 원문은 구분하여 제공합니다.

- 금융위원회 3단계 스트레스 DSR 시행방안: https://www.fsc.go.kr/no010101/84617
- 금융위원회 2026년 스트레스 DSR 변경시행 예고: https://better.fsc.go.kr/fsc_new/status/adminMap/PrvntcDetail.do?muNo=144&postNo=5349&stNo=11

## Citation

권장 표기:

> Resimanor, "2026 주택금융·DSR 데이터센터", 2026-09-18. https://resimanor.com/housing-finance-dsr-data/

## License

CC BY 4.0. 재사용 시 출처와 canonical source를 함께 표시해 주세요.
