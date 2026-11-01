---
license: other
license_name: mixed-kogl-public
language:
- ko
task_categories:
- image-to-text
tags:
- ocr
- korean
- government-documents
- benchmark
pretty_name: kordoc Korean public document OCR bench
size_categories:
- n<1K
configs:
- config_name: default
  data_files:
  - split: test
    path: "images/*"
---

# kordoc OCR bench — 한국 공문서 OCR 벤치

[kordoc](https://github.com/chrisryugj/kordoc)의 OCR 회귀 벤치(`bench/ocr-accuracy.mjs`)를 모델과 상관없이 돌릴 수 있게 옮긴 데이터셋입니다.
한국 공공기관 PDF(보도자료·예산서·계획서·회의록·법령 서식 등)의 쪽 이미지와, 그 쪽의 정답 텍스트를 담았습니다.

## 만든 방법

- **정답**: 텍스트층이 깨끗한 PDF 쪽(쪽당 200자 이상, 품질 신호 정상)을 골라 텍스트층을 kordoc으로 추출했습니다. 사람이 단 라벨이 아닙니다.
- **원본 PDF**: `pdf/` 에 문서 전체를 둡니다(kordoc 저장소 `bench/corpus/pdf/` 에 넣으면 저장소 벤치가 그대로 돕니다). web066 은 사진이 공공누리 범위 밖이라 쪽 이미지만 둡니다.
- **이미지**: 같은 쪽을 pdfium으로 216dpi(72dpi × 3) 렌더한 PNG입니다. kordoc OCR이 실제로 받는 입력과 같습니다.
- **채점에서 뺀 것**
  - 텍스트층 글자가 하나도 없는 그림 영역(인포그래픽·삽화·로고)은 이미지에서 흰색으로 가렸습니다. 정답이 그 글을 담을 수 없어서입니다(`masked_regions`, 픽셀 좌표).
  - 텍스트층에는 있지만 렌더되지 않는 글(흰 글·덮인 글)은 정답에서 뺐습니다(`hidden_text_removed`).
  - 래스터에 글꼴이 안 그려지는 쪽, 글줄 안 글자를 그림으로 찍은 쪽은 표본에서 뺐습니다.

**한계**: 깨끗한 렌더라서 실제 스캔의 잡음·기울기·저해상도는 반영하지 않습니다. 이 점수는 OCR 파이프라인의 상한(clean-render ceiling)입니다. 정답이 텍스트층이라 텍스트층 자체의 결함도 오차로 섞입니다.

## 필드 (`images/metadata.jsonl`, 쪽 하나에 한 줄)

| 필드 | 설명 |
|---|---|
| `file_name` / `id` | 쪽 이미지 / `<문서>_p<쪽번호>` |
| `doc`, `page` | 원본 PDF 파일명, 1부터 센 쪽 번호 |
| `width`, `height`, `dpi` | 이미지 크기(px), 렌더 해상도 |
| `text` | 정답 텍스트(문단·표 칸을 읽는 순서대로 줄바꿈으로 이음) |
| `markdown` | 같은 정답의 Markdown(표 구조 포함) |
| `kordoc_ppocrv5` | 기준선: kordoc 4.22.15 내장 OCR(PP-OCRv5 mobile det + korean rec)이 이 PNG를 읽은 결과 |
| `masked_regions` | 흰색으로 가린 그림 영역 `[x0, y0, x1, y1]` |
| `hidden_text_removed` | 정답에서 뺀 숨은 글 조각 수 |
| `publisher`, `source_url`, `license` | 원본 발행 기관, 받은 곳, 재배포 근거 |

## 채점

```bash
pip install rapidfuzz            # 없어도 돌지만 느립니다
python eval.py predictions.jsonl # 한 줄에 {"id": "...", "text": "..."}
python eval.py --column kordoc_ppocrv5
```

양쪽에 똑같이 정규화합니다: NFC → 모양이 같은 글자 접기(가운뎃점 계열, 로마 숫자, 전각 ASCII, ㎡ 같은 단위 글자, 물결, 큰 고리 ◯ → ○) → 줄임표 펴기 → 공백 전부 제거 → 리더 점(3개 이상) 제거.
구별되는 차이(○ vs O, ① vs 1, 【】 vs [])는 접지 않습니다.
읽는 순서에 민감한 CER과 함께, 순서와 상관없는 글자 재현율·정밀도(multiset)를 같이 냅니다.

## 기준선 (72쪽, 38문서)

| 엔진 | CER(micro) | CER(중앙값) | 글자 재현율 | 글자 정밀도 | 한글 재현율 |
|---|---|---|---|---|---|
| kordoc 4.22.15 (PP-OCRv5 mobile det + korean rec, CPU) | 0.0330 | 0.0144 | 0.9905 | 0.9944 | 0.9962 |

kordoc 저장소의 `bench/ocr-accuracy.mjs`는 53문서·102쪽을 PDF 경로로 읽고 문서 단위로 채점해 CER 0.0409를 냅니다. 이 데이터셋은 그 가운데 재배포 근거가 확인된 38문서·72쪽이고, 쪽 단위·이미지 입력이라 값이 조금 다릅니다(같은 102쪽을 이 방식으로 채점하면 CER 0.0374).
kordoc 안에서 새 모델을 비교하려면 저장소의 `node bench/ocr-accuracy.mjs --det=server` 처럼 엔진 옵션을 주고, 같은 PDF를 `bench/corpus/pdf/`에 두면 됩니다.

## 원본과 라이선스

모든 문서는 한국 국가기관·지방자치단체가 공개한 문서입니다. 문서마다 아래 근거로 재배포합니다.

- **공공누리 제1유형**: 출처를 표시하면 자유 이용(아래 표가 출처 표시입니다).
- **저작권법 제7조**: 법령(별지 서식 포함)·고시·공고는 보호받지 않는 저작물입니다.
- **저작권법 제24조의2①**: 국가·지방자치단체가 업무상 작성해 공표한 저작물은 허락 없이 이용할 수 있습니다.

각 문서의 권리는 원 발행 기관에 있습니다. 문제가 있으면 Discussions 에 알려 주시면 바로 내리겠습니다. eval.py·메타데이터·정답 정리는 MIT 입니다.

| 문서 | 발행 | 근거 | 받은 곳 |
|---|---|---|---|
| `assembly-minutes-1179.pdf` | 국회사무처 | 공공누리 제1유형 | [링크](https://record.assembly.go.kr/assembly/viewer/minutes/download/pdf.do?id=1179) |
| `assembly-minutes-1231.pdf` | 국회사무처 | 공공누리 제1유형 | [링크](https://record.assembly.go.kr/assembly/viewer/minutes/download/pdf.do?id=1231) |
| `bucheon-budget-2021.pdf` | 부천시 | 저작권법 제24조의2① | [링크](https://budget.bucheon.go.kr/docs/budget/depth1_1/2021/2021depth1/6_17.pdf) |
| `cbe-record-guide.pdf` | 행정안전부 국가기록원 | 저작권법 제24조의2① | [링크](https://www.archives.go.kr/next/common/downloadFile.do?up_filepath=2F6e6578742e646174612F6d616e616765725C32303235B3E25fB1E2B7CFB9B0B0FCB8AE5fC1F6C4A72e706466&up_filename=2025%EB%85%84_%EA%B8%B0%EB%A1%9D%EB%AC%BC%EA%B4%80%EB%A6%AC_%EC%A7%80%EC%B9%A8.pdf) |
| `changwon-plan2026.pdf` | 창원특례시 의창구 | 저작권법 제24조의2① | [링크](https://www.changwon.go.kr/cwportal/_res/gu/data/pdf/p11477_data01_2026.pdf) |
| `eval-perf-2025.pdf` | 법제처 (기획재정담당관실) | 저작권법 제24조의2① | [링크](https://www.evaluation.go.kr/upload2/atch/eval/20250508093024330.pdf) |
| `eval-rda-2022.pdf` | 농촌진흥청 (혁신행정법무담당관실) | 저작권법 제24조의2① | [링크](https://www.evaluation.go.kr/upload2/atch/eval/20230307133914500.pdf) |
| `geumcheon-budget.pdf` | 서울특별시 금천구 | 저작권법 제24조의2① | [링크](https://www.geumcheon.go.kr/site/portal/down/cts265_%EC%98%88%EC%82%B0%ED%8E%B8%EC%84%B1%EC%84%B8%EB%B6%80%EB%82%B4%EC%97%AD(%EC%A0%84%EC%B2%B4).pdf) |
| `gg-nonprofit-faq.pdf` | 경기도 | 저작권법 제24조의2① | [링크](https://www.gg.go.kr/uploads/CONTENTS/site/gg/(%EB%B6%99%EC%9E%843)2026%20%EA%B2%BD%EA%B8%B0%EB%8F%84%20%EB%B9%84%EC%98%81%EB%A6%AC%EB%B2%95%EC%9D%B8%20%EC%A3%BC%EC%9A%94%20%EC%A7%88%EC%9D%98%EC%9D%91%EB%8B%B5%20%EC%82%AC%EB%A1%80%EC%A7%91_v260114.pdf) |
| `goe-gongmun-guide.pdf` | 경기도교육청 (학교업무개선담당관) | 저작권법 제24조의2① | [링크](https://www.goe.go.kr/resource/old/BBSMSTR_000000000028/BBS_202410150153084250.pdf) |
| `goe-school-manual.pdf` | 경기도교육청 (학교설립과) | 저작권법 제24조의2① | [링크](https://www.goe.go.kr/goe/na/ntt/selectNttInfo.do?nttSn=1044245&mi=10961) |
| `goesan-budget-2013.pdf` | 충청북도 괴산군 | 저작권법 제24조의2① | [링크](https://goesan.go.kr/document/yesan/2013_3th_add/901.pdf) |
| `goheung-budget-culture.pdf` | 전라남도 고흥군 | 저작권법 제24조의2① | [링크](https://www.goheung.go.kr/home/www/down/www648/2026_0/3.%20%EC%9D%BC%EB%B0%98%ED%9A%8C%EA%B3%84%20%EC%84%B8%EC%B6%9C/11.%20%EB%AC%B8%ED%99%94%EC%B2%B4%EC%9C%A1%EA%B3%BC.pdf) |
| `goheung-plan2026.pdf` | 전라남도 고흥군 | 저작권법 제24조의2① | [링크](https://www.goheung.go.kr/home/www/down/www453/2026/(%EC%B4%9D%EA%B4%84)2026%EB%85%84%EB%8F%84%20%EC%A3%BC%EC%9A%94%EC%97%85%EB%AC%B4%EA%B3%84%ED%9A%8D.pdf) |
| `hampyeong-plan2026.pdf` | 전라남도 함평군 | 저작권법 제24조의2① | [링크](https://www.hampyeong.go.kr/upload/file/work/2026/00.pdf) |
| `ice-arc-2026.pdf` | 행정안전부 국가기록원 | 저작권법 제24조의2① | [링크](https://www.archives.go.kr/next/common/downloadFile.do?up_filepath=2F6e6578742e646174612F6d616e616765725C32303236B3E220B1E2B7CFB9B0B0FCB8AE20C1F6C4A72e706466&up_filename=2026%EB%85%84%20%EA%B8%B0%EB%A1%9D%EB%AC%BC%EA%B4%80%EB%A6%AC%20%EC%A7%80%EC%B9%A8.pdf) |
| `ice-election-cases.pdf` | 중앙선거관리위원회 | 저작권법 제24조의2① | [링크](https://www.nec.go.kr/site/nec/ex/bbs/View.do?cbIdx=1129&bcIdx=146509) |
| `ice-jci-2026.pdf` | 인천광역시교육청 | 저작권법 제24조의2① | [링크](https://www.ice.go.kr/upload/jci/na/bbs_1623/2026/05/4734549de1bc4bae9d2f7250ba897cd7.pdf) |
| `jangheung-plan2026.pdf` | 전라남도 장흥군 | 저작권법 제24조의2① | [링크](https://www.jangheung.go.kr/contents/14299/plan_2026.pdf) |
| `khs-budget-2014.pdf` | 문화재청 (현 국가유산청) | 저작권법 제24조의2① | [링크](https://www.khs.go.kr/html/common/private_02_n208.pdf) |
| `kmcc-press.pdf` | 방송통신위원회 (네트워크정책국 인터넷정책과) | 저작권법 제24조의2① | [링크](https://www.kcc.go.kr/user.do?mode=view&page=A05030000&boardId=1113&boardSeq=33198) |
| `naacc-2019-settle.pdf` | 행정중심복합도시건설청 | 저작권법 제24조의2① | [링크](https://naacc.go.kr/attach/jfile/jfile_contents/2019_out.pdf) |
| `rda-planfarm.pdf` | 농촌진흥청 | 저작권법 제24조의2① | [링크](https://www.rda.go.kr/download_file/planFarm.pdf) |
| `sbc-budget-review.pdf` | 성북구의회 예산결산특별위원회 | 저작권법 제24조의2① | [링크](https://www.sbc.go.kr/attach/record/SEONGBUK/appendix/a09/A0005525.pdf) |
| `seoul-archives-guide.pdf` | 서울기록원 (서울특별시) | 저작권법 제24조의2① | [링크](https://archives.seoul.go.kr/upload/files/2025/0819/105925527.pdf) |
| `topik-plan2026.pdf` | 교육부 (국립국제교육원 운영) | 저작권법 제7조(비보호 저작물) | [링크](https://exam.topik.go.kr/nasdata/webnas/raonkeditordata/BBS//2025/10/20251031_093545671_74607.pdf) |
| `web000_[산림청_공고_제2025-430호]_국산재_활용_한국형_목구조물_혁신_기술개발_사업_2026년도_신규과제_선정_계획_공고.pdf` | 산림청 | 저작권법 제7조(비보호 저작물) | [링크](https://www.iris.go.kr/contents/retrieveBsnsAncmView.do?ancmId=017219) |
| `web001_[산림청_공고_제2025-427호]_산림_지식재산_기반_유레카_기술개발_사업_2026년도_신규과제_선정_계획_공고.pdf` | 산림청 | 저작권법 제7조(비보호 저작물) | [링크](https://www.iris.go.kr/contents/retrieveBsnsAncmView.do?ancmId=017223) |
| `web044_(별첨3)_미래전략포럼_개요★.pdf` | 기획재정부 | 공공누리 제1유형 | [링크](https://www.korea.kr/common/download.do?fileId=198170369&tblKey=GMN) |
| `web045_moef-251217.pdf` | 행정안전부 (filename says moef but content is MOIS) | 공공누리 제1유형 | [링크](https://www.korea.kr/common/download.do?fileId=198302509&tblKey=GMN) |
| `web047_[별지_제5호서식]_개발행위_허가신청서(국토의_계획_및_이용에_관한_법률_시행규칙).pdf` | 법제처 국가법령정보센터 (국토교통부령) | 저작권법 제7조(비보호 저작물) | [링크](https://www.law.go.kr/법령/국토의계획및이용에관한법률시행규칙) |
| `web048_[별지_제3호서식]_대리인선임허가신청서(행정절차법_시행규칙).pdf` | 법제처 국가법령정보센터 (행정안전부령) | 저작권법 제7조(비보호 저작물) | [링크](https://www.law.go.kr/법령/행정절차법시행규칙) |
| `web049_[별지_제8호서식]_의약품등_(제조판매¸_수입_품목)_허가사항_변경허가_신청서(의약품_등의_안전에_관한_규칙).pdf` | 식품의약품안전처 (총리령) via 국가법령정보센터 | 저작권법 제7조(비보호 저작물) | [링크](https://www.law.go.kr/법령/의약품등의안전에관한규칙) |
| `web050_[별지_제35호서식]_양식업_허가신청서(양식산업발전법_시행규칙).pdf` | 해양수산부령 via 국가법령정보센터 | 저작권법 제7조(비보호 저작물) | [링크](https://www.law.go.kr/법령/양식산업발전법시행규칙) |
| `web051_[별지_제14호서식]_건축허가신청서_및_허가서(외국인투자_촉진법_시행규칙).pdf` | 법제처 국가법령정보센터 (산업통상자원부령) | 저작권법 제7조(비보호 저작물) | [링크](https://www.law.go.kr/법령/외국인투자촉진법시행규칙) |
| `web066_230920_글로벌_금융안정_콘퍼런스_보도자료.pdf` | 기획재정부 / KDI | 공공누리 제1유형 | [링크](https://www.korea.kr/common/download.do?fileId=197470181&tblKey=GMN) |
| `web069_★(제안요청서)_WTO_수산보조금_협정_기대효과(재공고).pdf` | 산업통상자원부 | 저작권법 제24조의2① | [링크](https://www.motir.go.kr/attach/down/c26df36c4f964b1523b31be51e734922/90397b08df1f043058ba7b23ccb55674/778bdbf5db9ced7c8fd52756c00bf0cd) |
| `yeosu-plan2026.pdf` | 여수시 | 저작권법 제24조의2① | [링크](https://www.yeosu.go.kr/contents/88/2026_plan2.pdf) |

### 재배포하지 않은 문서 (kordoc 벤치 53문서 중 15)

저작권 표시(All Rights Reserved), 용역 보고서, 공공기관 작성(공공누리 표시 없음), 공공누리 제4유형(변경금지 — 그림 영역 가림이 변경에 해당할 수 있음), 출처 미확인 문서는 넣지 않았습니다.

| 문서 | 발행 | 사유 | 받은 곳 |
|---|---|---|---|
| `archives-record-duty.pdf` | 행정자치부 국가기록원 | 출처 미확인 | — |
| `goesan-budget-2022.pdf` | 충청북도 괴산군 | 출처 미확인 | — |
| `gwd-info-plan.pdf` | 강원특별자치도 (용역 수행: ㈜씨앤엘컨설팅) | 라이선스 미확인 | [링크](https://state.gwd.go.kr/upload/board/BDFNPI02/1560bb3b-a937-403a-b65a-98a45097b667.pdf) |
| `ice-geomjeong-plan.pdf` | 인천광역시검정고시위원회 (인천광역시교육청) | 출처 미확인 | — |
| `korean-press-guide.pdf` | 국립국어원 | 공공누리 제4유형 | [링크](https://www.korean.go.kr/front/etcData/etcDataView.do?mn_id=208&etc_seq=663&pageIndex=1) |
| `korean-publang-2015.pdf` | 국립국어원 (연구: 강원대학교 한국어문화원, 책임 최홍열) | 공공누리 제4유형 | [링크](https://www.korean.go.kr/front/reportData/reportDataView.do?mn_id=207&searchOrder=&report_seq=1025&pageIndex=1) |
| `ktdb-transport-stats.pdf` | 국토교통부 / 한국교통연구원 국가교통DB(KTDB) (발간등록번호 11-1613000-100257-14) | 공공기관(한국교통연구원) 운영 — 공공누리 표시 없음 | [링크](https://www.ktdb.go.kr/DATA/pblcte/20260213104142919.pdf) |
| `nanet-press-gwanghwamun.pdf` | 서울특별시 관광정책과 / 서울관광재단 | 출처 미확인 | — |
| `pa-narabaeum-plan.pdf` | 국가공무원인재개발원 스마트개발과 | 출처 미확인 | — |
| `pcccr-attach.pdf` | 울산광역시 남구 (발간등록번호 57-3700200-100001-13) | 출처 미확인 | — |
| `pen-cyberbridge.pdf` | KAIST 과학영재교육연구원 (posted by 부산광역시교육청 home.pen.go.kr) | 라이선스 미확인 | [링크](https://home.pen.go.kr/upload/childpiage/na/bbs_3411/ntt_838023/doc_ff5cvcaed-f3vef-43v56-a8vf4-b9adv134ev380a_v2404.pdf) |
| `sokcho-budget.pdf` | 속초시 | 출처 미확인 | — |
| `web046_제안요청서.pdf` | 서울특별시 교통운영과 | 출처 미확인 | — |
| `web067_downloadBoardFile.pdf` | 국가기록원 (주관연구기관: 전북대학교 산학협력단; 발간등록번호 11-1741050-000059-01) | 라이선스 미확인 | [링크](https://www.archives.go.kr/next/common/downloadBoardFile.do?board_seq=98342&board_file_seq=1) |
| `web068_downloadFile.pdf` | 고용노동부 | 게시 기관이 공공누리 없는 자료는 사전 협의 필요라고 명시 | [링크](https://www.moel.go.kr/common/downloadFile.do?file_seq=20251201365&bbs_seq=20251200714&bbs_id=29) |
