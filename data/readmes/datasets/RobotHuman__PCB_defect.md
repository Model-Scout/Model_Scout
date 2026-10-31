---
license: mit
task_categories:
- image-classification
- object-detection
language:
- en
- ko
pretty_name: PCB Defects Dataset
size_categories:
- 1K<n<10K
---


# ⚡ 데이터셋 요약
- 본 데이터셋은 naked PCB(부품 실장 전 PCB) 이미지로 구성되어 있으며, 총 1386장, 6종 결함, 이미지당 3~5개 결함을 포함
- 이미지는 실제 AOI 유사 촬영 시스템으로 템플릿 보드를 촬영한 뒤, Photoshop으로 결함을 삽입해 합성
- 즉, “현장(real) 결함”이 아니라, 제어된 합성 결함이라는 점이 데이터 해석/일반화에서 중요한 전제
<br><br>


# 🌳 데이터셋 구조
```
PCB_defect/
├── README.md
├── Meta Data/
│   └── Huang et al.(2019), A PCB Dataset for Defects Detection and Classification.pdf
├── Missing_hole/                      # 결함 유형
│   ├── missing_hole01.jpg             # [입력] PCB 이미지
│   ├── missing_hole02.jpg
│   ├── missing_hole03.jpg
│   ├── missing_hole01_annotation.xml  # [출력] PCB 결함 영역 Bounding box 좌표
│   ├── missing_hole02_annotation.xml
│   ├── missing_hole03_annotation.xml
│   └── ...
├── Mouse_bite/  
├── Open_circuit/  
├── Short/  
├── Spur/  
└── Spurious_copper/  
```

  **<결함 유형 6가지>**
- Missing Hole(구멍 누락): 뚫려 있어야 할 구멍이 없음
- Mouse Bite(마우스 바이트): 배선이나 패드 끝부분이 갉아먹은 듯이 깎여 나감
- Open Circuit(단선): 연결되어야 할 회로가 끊어짐
- Short(단락): 서로 닿지 않아야 할 회로가 붙어버림
- Spur(돌기): 회로 옆으로 작게 튀어나온 구리 잔여물
- Spurious Copper(구리 잔여물): 회로와 상관없는 위치에 흩뿌려진 구리 조각
<br><br>


## 🎯 AI 모델 설명(모델 개발 완료 시)
- **사용 알고리즘:** Reference 비교 기반 검출 알고리즘 + CNN
- **모델 사용 목적:** 결함 위치 검출, 결함 유형 분류
- **모델 입력값:** PCB 이미지
- **모델 출력값:** PCB 결함 유형
<br><br>


# ⛏️ 데이터셋 출처
- **저장소:** https://www.kaggle.com/datasets/akhatova/pcb-defects
- **논문:** Huang, Weibo, and Peng Wei. "A PCB dataset for defects detection and classification." arXiv preprint arXiv:1901.08204 (2019)
- **기관:** Open Lab on Human Robot Interaction, Peking University
- **설비/제품:** -
<br><br>


# 👨‍💻 작성자 정보
- **데이터셋 구축 기관:** 한국전자기술연구원 자율제조연구센터
- **담당자명:** 박동현
- **연락처:** userid@keti.re.kr / 010-5555-6666
- **작성 일자:** 2026.01.13
- **데이터셋 공개 가능 여부:** 공개 가능
<br><br>

