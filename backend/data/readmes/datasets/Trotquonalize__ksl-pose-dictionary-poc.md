---
language:
  - ko
license: cc-by-nc-sa-4.0
task_categories:
  - text-generation
  - text-to-image
  - other
tags:
  - sign-language
  - korean-sign-language
  - ksl
  - keypoint
  - openpose
  - pose-estimation
  - text-to-pose
  - sign-language-production
pretty_name: KSL Pose Dictionary (PoC)
size_categories:
  - 1K<n<10K
---

# KSL Pose Dictionary (PoC)

**한국수어(KSL) text-to-pose 시제품용 keypoint 데이터셋.**

[`docent_AI_sign_research_02`](https://github.com/JangHyun-bin/docent_AI_sign_research_02) 프로젝트에서 생성. Neural Sign Actors (CVPR 2024) 접근법을 KSL에 적용하는 Path B (Dictionary-based) 시제품의 핵심 데이터셋.

## 개요

| 자산 | 갯수 | 키포인트 |
|---|---|---|
| **sldict keypoint** (국립국어원 한국수어사전) | 1,444 단어 | OpenPose 137 (RTMW-DW-L-M 추출) |
| **NIASL2021 gloss segmentation keypoint** (재난 안전 도메인) | 2,287 base gloss | OpenPose 137 (NIASL 원본) |
| **Hybrid sign index** | 4,511 unique signs | 단어 → keypoint 경로 매핑 |
| **Stage 1 학습 corpus** | 20,085 samples (train 18,067 / val 986 / test 1,032) | (한국어 문장, KSL gloss 시퀀스) |
| **KSL vocab** | 2,984 unique base lemma | gloss frequency table |

**Coverage:** NIASL2021 raw gloss interval의 **93.3%**가 본 index로 직접 매핑 가능.

## 디렉토리 구조

```
ksl-pose-dictionary-poc/
├── README.md                          (본 파일)
├── data/
│   ├── sldict_keypoints/              (1,444 × ~1.5MB = 2.1GB)
│   │   └── {origin_no}.json
│   ├── niasl_keypoints/               (2,287 × ~25KB = 57MB)
│   │   └── {idx:04d}_{base}.json
│   ├── hybrid_sign_index.json         (3.5K aliases)
│   ├── niasl_kp_dict_meta.json
│   ├── sldict_niasl_mapping.json
│   ├── hybrid_v3_verification.json
│   └── stage1/
│       ├── train.jsonl                (18,067)
│       ├── val.jsonl                  (986)
│       ├── test.jsonl                 (1,032)
│       ├── ksl_vocab.json
│       └── sample_preview.json
└── docs/
    └── SCHEMA.md
```

## Keypoint JSON 형식 (OpenPose 137)

각 keypoint JSON 파일:

```json
{
  "origin_no": "22",
  "gloss": "안녕하세요",
  "fps": 30.0,
  "frame_count": 248,
  "width": 700,
  "height": 466,
  "keypoint_format": "openpose137",
  "landmarks": {
    "pose": [[x, y, c, ...] * 25, ...],     // body 25 keypoint × frames
    "face": [[x, y, c, ...] * 70, ...],     // face 70 × frames
    "left_hand": [[x, y, c, ...] * 21, ...],
    "right_hand": [[x, y, c, ...] * 21, ...]
  }
}
```

총 137 keypoint × frames. 좌표는 픽셀 단위.

## Stage 1 학습 corpus 형식

각 line (jsonl):

```json
{
  "id": "NIA_SL_G1_COLDWAVE000032_1_TW07",
  "korean_text": "25일 19시 경기지역 한파, 강풍경보, 비닐하우스 등 시설물 피해없게 주의하세요",
  "gloss_seq": ["날1", "시:7시", "경기1", ...],
  "gloss_seq_base": ["날", "시", "경기", ...],
  "n_glosses": 12,
  "duration_s": 17.5,
  "disaster_cat": "1.자연재난",
  "studio": true
}
```

`korean_text` → `gloss_seq_base` 매핑이 KLUE-BERT seq2seq fine-tune의 (input, target) 쌍.

## 원본 데이터 출처

| 데이터 | 출처 | 라이선스 |
|---|---|---|
| sldict 1,444 mp4 | https://sldict.korean.go.kr (국립국어원) | 정부 공공 (출처 표기) |
| NIASL2021 영상·JSON | AI Hub #114 (dataSetSn=636) — EQ4ALL + KETI + KAIST + 강남대 | AI Hub 연구용 |
| Stage 1 corpus | NIASL2021 derivative (korean_text + sign_script 추출) | AI Hub 연구용 |

원본 video는 본 dataset에 포함 안 됨. 다음으로 직접 다운로드:
- sldict: `scripts/sldict_bulk_download.py` (정부 공공 자료, 1.5GB)
- NIASL2021: AI Hub 신청 + 승인 → `aihubshell -mode d` (12GB tar)

## 사용 예시

### 1. Hybrid index lookup

```python
import json
from huggingface_hub import snapshot_download

# 전체 또는 일부 다운로드
local_dir = snapshot_download(
    repo_id="Trotquonalize/ksl-pose-dictionary-poc",
    repo_type="dataset",
    allow_patterns=["data/hybrid_sign_index.json", "data/niasl_keypoints/*"],
)

with open(f"{local_dir}/data/hybrid_sign_index.json") as f:
    hybrid = json.load(f)

print(hybrid['aliases']['병원'])
# {'source': 'niasl', 'gloss': '병원', 'kp_format': 'openpose137',
#  'kp_path': 'data/niasl_keypoints/0123_병원.json'}
```

### 2. Keypoint 시퀀스 로드 + 시각화

```python
with open(f"{local_dir}/data/niasl_keypoints/0000_지역.json") as f:
    kp = json.load(f)

pose_per_frame = kp['landmarks']['pose']  # [n_frames, 25*3]
# 각 frame: 25 keypoint × (x, y, confidence)
```

### 3. Stage 1 학습 (KLUE-BERT seq2seq)

```python
from datasets import load_dataset

ds = load_dataset(
    "Trotquonalize/ksl-pose-dictionary-poc",
    data_files={
        "train": "data/stage1/train.jsonl",
        "validation": "data/stage1/val.jsonl",
        "test": "data/stage1/test.jsonl",
    }
)

# fine-tune KLUE-BERT or any Korean LM on (korean_text → gloss_seq_base)
```

## 처리 파이프라인

1. **sldict 영상 수집**: Camoufox + Playwright로 sldict.korean.go.kr crawling (1,444 mp4)
2. **sldict keypoint 추출**: RTMW-DW-L-M (mmpose / rtmlib), ONNX Runtime GPU
3. **NIASL2021 다운로드**: AI Hub `aihubshell -mode d` → 12GB tar
4. **NIASL gloss segmentation**: `sign_script.gloss_id` × `start/end` timestamp로 137-kp frame range 추출
5. **Hybrid index**: NIASL 우선 (재난 도메인) + sldict fallback (일반 vocab)
6. **Stage 1 corpus**: `(korean_text, gloss_seq_base)` 쌍 추출 + text-level split

상세: [scripts/](https://github.com/JangHyun-bin/docent_AI_sign_research_02/tree/main/scripts)

## 라이선스

**CC BY-NC-SA 4.0** (Creative Commons Attribution-NonCommercial-ShareAlike).

- 연구·교육·비상업적 사용 허용
- 출처 표기 필수
- ShareAlike: 파생물도 동일 라이선스
- **상업 사용은 금지** (AI Hub NIASL2021 라이선스 조건 일치)

상업 사용 시 AI Hub + 국립국어원과 별도 라이선스 계약 필요.

## 인용 (Citation)

```bibtex
@misc{ksl_pose_dictionary_poc_2026,
  title  = {KSL Pose Dictionary (PoC) — A 4,511-sign hybrid keypoint dataset for Korean sign language production research},
  author = {JangHyun-bin},
  year   = {2026},
  url    = {https://huggingface.co/datasets/Trotquonalize/ksl-pose-dictionary-poc},
  note   = {Derivative of sldict (국립국어원) and NIASL2021 (AI Hub \#114, EQ4ALL+KETI+KAIST+강남대)},
}
```

## 관련 자료

- **Project repo**: https://github.com/JangHyun-bin/docent_AI_sign_research_02
- **Research log**: [`docs/research-log.md`](https://github.com/JangHyun-bin/docent_AI_sign_research_02/blob/main/docs/research-log.md)
- **Deep-research 보고서**: `research/notes/final_report_neural-sign-actors-ksl-80fbae.md`

## 한계

1. **NMM (비수지 신호)** — 본 dataset의 137 keypoint에는 NIASL 원본의 nms_script (눈썹·고개 흔들기 등) interval 정보 없음. Stage 3 NMM 룰은 별도 적용 필요.
2. **농인 평가 미수행** — 본 dataset은 PoC 시제품용. Production 적용 전 KAD(한국농아인협회) 또는 지역 농인협회 자문 mandatory.
3. **재난 도메인 편향** — NIASL2021이 재난 안전 corpus라 KSL vocab이 그 쪽에 편중. 일반 도메인은 sldict로 보완 필요.
4. **단일 signer**: sldict는 각 단어 1명 signer 영상. signer diversity 부족.

## 변경 이력

- v0.1 (2026-05-27): 초기 release
  - sldict 1,444 단어 (RTMW 137-kp 추출)
  - NIASL2021 2,287 base gloss segmentation
  - Hybrid index 4,511 signs
  - Stage 1 corpus 20,085 samples
