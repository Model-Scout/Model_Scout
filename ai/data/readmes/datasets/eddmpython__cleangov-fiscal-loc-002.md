---
license: other
language:
- ko
tags:
- korea
- public-finance
- parquet
configs:
- config_name: expenditure
  data_files:
  - split: train
    path:
    - objects/5b/5ba58b6a37bea9e6531e87b7ca353e3af9484e027cfacd755b587063b12e4438.parquet
    - objects/5d/5d6921ad04bdc512294a904fe343956e4a92ac53319401357e6975bfe4eb075a.parquet
    - objects/88/88a37d9bc090846e000f843a94380e8b91d22fd0f4fdfbbf681e445a8216a23a.parquet
    - objects/a5/a5695f665fc0697fa1acb623b66ba6e01686df06792ce708e2f351a7980f7ca6.parquet
    - objects/b3/b32d162e8e63cd4750f3f4cb1def4daf2b78069702b0b825e84e7e473be9c510.parquet
    - objects/e4/e411087f387f5aaec569015f061fb7735cc1761f9212943e27021439c8980fcb.parquet
    - objects/e5/e56e90c0e4836789827ae37d0e5a01d325d13ec15af316c04a15914fb0463007.parquet
    - objects/ec/ec6919ce32ebbb3a218c1a5556da2fad25a7940adf1aad684db9a7a1946e5408.parquet
    - objects/f5/f5ec2b1dfe0c972d02fc7c01c6386c0113541f948cc562788d13e9a0d7ada184.parquet
    - objects/fd/fdfe61ee23a178fcdb45622aef490087f3c00ea5cb6a9364fb89f3cd221e6d85.parquet
---

# 지방재정365 연도별 세부사업별 세출현황 파일

전국 지방자치단체의 연도별 세부사업별 세출(국비·시도비·시군구비 재원, 예산현액, 지출액, 잔액) 을 회계·분야·부문·세부사업 단위로 담은 연간 파일. 공공데이터포털(15138684) 은 LINK 형으로 등록되어 있고 실제 데이터는 지방재정365 공시 화면 (LF6000000.do?ntcaClsDvCd=FSL446) 에서 제공된다. 지방 사업의 예산→집행 백필과 연도별 정합성의 기준 파일이다.

출처: https://www.data.go.kr/data/15138684/fileData.do

이용 조건: 이용허락범위 제한 없음 (공공데이터포털 표기)

manifest.json은 현재 검증된 파일의 계층·원래 경로·SHA-256·크기·불변 객체 경로를 제공한다. 같은 commit revision으로 manifest와 객체를 내려받고 해시를 검증한다. 예산현액과 지출액은 합산하지 않는다.
