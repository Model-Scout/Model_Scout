---
license: other
license_name: mixed-sources-see-readme
language:
  - ko
task_categories:
  - audio-classification
tags:
  - audio
  - sound-event-detection
  - keyword-spotting
size_categories:
  - 100K<n<1M
---

# Edge Audio Dataset

## 출처 및 라이선스

이 데이터셋은 **여러 출처를 합친 것이고, 출처마다 라이선스가 다르다.**
단일 라이선스로 배포되지 않으므로 사용 전 아래를 각각 확인해야 한다.

| 라벨 | 출처 | 라이선스 |
|---|---|---|
| `alarm`, `fire_alarm`, `water`, `scream`, `glass_break`, `bicycle`, `gunshot`, `baby_cry`(울음분) | **AI Hub** (한국지능정보사회진흥원) | ⚠️ **재배포 제한** — 아래 참고 |
| `baby_cry`(일부) | [ESC-50](https://github.com/karolpiczak/ESC-50) (Piczak, 2015) | **CC BY-NC 3.0** — 비상업 한정, 출처 표기 필수 |
| `baby_cry`(일부) | [donateacry-corpus](https://github.com/gveres/donateacry-corpus) | 원 저장소 확인 필요 |
| `knock` | Knocking Sound Effects With Emotional Intentions | 원 배포처 확인 필요 |
| `cat_meow`, `dog_bark`, `car_horn` | 수집처 혼재 (README 상단 참고) | 확인 필요 |
| `background` | 위 전체에서 무음 판정된 클립 | 원 출처 라이선스를 그대로 따름 |
| `musan_mixed_2s/**` | 위 클립 + [MUSAN](https://www.openslr.org/17/) `noise/` (Snyder et al., 2015) 혼합 | 원 클립 라이선스 **+ MUSAN CC BY 4.0** (출처 표기 필수) |

### ⚠️ AI Hub 데이터 관련 고지

`S-2110xx_*`, `S-2111xx_*` 형식의 파일은 AI Hub 제공 데이터에서 유래한다.
AI Hub 이용약관은 일반적으로 **제3자 재배포를 제한**한다. 이 repo에는 해당 원본(`raw/`)과
파생 클립(`clips_2s/`)이 모두 포함되어 있다.

- 이 데이터를 사용하려면 **AI Hub에서 직접 원본을 내려받고 해당 약관에 동의**하는 것이 안전하다.
- 권리자의 요청이 있으면 해당 파일을 즉시 내린다. Discussions 탭이나 repo 소유자에게 연락 바란다.
- 폴더명이 영어로 바뀌었을 뿐 **원본 데이터의 권리관계는 그대로**다.

### 비상업 조건

ESC-50이 **CC BY-NC**이므로, 이 데이터셋을 통째로 쓴 결과물은
**상업적 이용이 불가하다**. 상업적 용도라면 ESC-50 유래 클립
(`baby_cry/**/ESC50_*`)을 제외해야 한다.

### 인용

```
ESC-50: K. J. Piczak. "ESC: Dataset for Environmental Sound Classification."
Proceedings of the 23rd ACM International Conference on Multimedia, 2015.

MUSAN: D. Snyder, G. Chen, D. Povey. "MUSAN: A Music, Speech, and Noise Corpus."
arXiv:1510.08484, 2015. (CC BY 4.0)
```

---


> 함께 볼 문서
> - [`스크립트_안내.md`](스크립트_안내.md) — 각 스크립트·CSV 가 무엇이고 언제 돌리는지
> - [`CHANGELOG.md`](CHANGELOG.md) — 2026-07-19 재정비에서 무엇이 왜 바뀌었는지, 남은 문제
> - [`데이터 추가 안내0716김예원.txt`](데이터%20추가%20안내0716김예원.txt) — 0716 데이터 추가 원본 안내

음향 이벤트 분류 학습용 데이터셋. 라벨별로 **원본(`raw/`)** 과 **2초 전처리·증강 클립(`clips_2s/`)** 을 한 폴더 안에 둔다.

- **원본**: 2,778개 (13개 라벨)
- **클립**: 80,049개 = 원본분할 29,040 (그중 무음판정 7,071) + 증강 51,009
- **MUSAN Noise 혼합 클립**: 240,147개 = 위 80,049개 × SNR 20/15/10 dB (`musan_mixed_2s/`, 약 29GB)
- **클립 포맷**: WAV, float32, [-1.0, 1.0], 16,000 Hz, mono, 2.0초 (32,000 샘플)
- **분할 방식**: 2초 슬라이딩 윈도우, hop 1초 (50% 오버랩), 2초 미만 잔여 구간은 버림
- **무음 판정**: 클립을 100ms×20개 세그먼트로 나눠 peak 세그먼트 RMS가 **-30 dBFS 미만**이면 `background` 로 분류

## 폴더 구조

```
├── gunshot/
│   ├── raw/           297   원본 (8~22초)
│   └── clips_2s/    4,257   2초 분할·증강
├── fire_alarm/  water/  scream/  bicycle/  baby_cry/     (동일 구조)
├── car_horn/  cat_meow/  dog_bark/  knock/               (동일 구조)
│
│   ── clips_2s 가 10,000개를 넘는 라벨은 part_XX 로 쪼개져 있다 ──
├── alarm/
│   ├── raw/           403
│   └── clips_2s/
│       ├── part_00/  7,905
│       └── part_01/  7,905
├── glass_break/
│   ├── raw/           258
│   └── clips_2s/
│       ├── part_00/  6,152
│       └── part_01/  6,151
├── background/                무음 판정분 (raw 없음)
│   └── clips_2s/
│       ├── part_00/  7,071
│       └── part_01/  7,071
│
├── musan_mixed_2s/          MUSAN Noise 혼합본 (라벨 폴더 구조 동일, raw 없음)
│   ├── alarm/clips_2s/part_00..04/      47,430
│   ├── background/clips_2s/part_00..04/ 42,426
│   ├── glass_break/clips_2s/part_00..03/ 36,909
│   ├── baby_cry/  water/  fire_alarm/  gunshot/  bicycle/   (part_XX 로 분할)
│   └── car_horn/  cat_meow/  dog_bark/  knock/  scream/    (clips_2s/ 평면)
├── musan_mix_metadata.csv   musan_mixed_2s 전체 인덱스 (240,147행)
├── esc50/                   ESC-50 JSON sidecar 190개 (wav 는 라벨 폴더로 이동)
├── data_augmented/src/      전처리 파이프라인 코드
├── clip_metadata.csv        clips_2s 전체 인덱스
├── generate_musan_mixes.py, verify_musan_mixes.py   MUSAN 혼합 생성·검증
└── dataset_labels.csv, integrated_*.csv
```

> ⚠️ **`part_XX` 하위 폴더 주의**
>
> Hugging Face는 **디렉터리당 파일 10,000개**가 하드 제한이다. `alarm`(15,810),
> `glass_break`(12,303), `background`(14,142)는 이를 넘어서 `clips_2s/part_00/`,
> `part_01/` 로 나눠 저장했다. 나머지 라벨은 `clips_2s/` 평면 그대로다.
`musan_mixed_2s/` 도 같은 규칙이다 (10,000개 초과 라벨은 `part_00..part_NN`, 아래 표 참고).
>
> **경로를 직접 조합하지 말고 `clip_metadata.csv` / `musan_mix_metadata.csv` 의 `filepath` 컬럼을 쓸 것.**
> 이 컬럼에는 part 경로가 이미 반영되어 있다. 로컬에서 평면 구조로 되돌리려면:
>
> ```python
> import pandas as pd, re
> df = pd.read_csv("clip_metadata.csv")
> df["flat"] = df.filepath.str.replace(r"/part_\d+/", "/", regex=True)
> ```
>
> 분할 기준은 파일명 정렬 후 균등 분배라서 재현 가능하다.

> **파일명 유니코드 정규화 (2026-10-29)**: 한글이 들어간 파일명은 전부 **NFC** 로 통일했다.
> 그 전에는 `car_horn/` 의 `1.자동차_…` 계열 519개와 `데이터 추가 안내0716김예원.txt` 가 macOS 식 **NFD**
> (자모 분리)로 올라가 있어서, CSV(NFC)의 경로와 문자열이 달라 정확히 일치 검색하면 찾아지지 않았다.
> 내용은 그대로이고 이름만 바꿨다. 이 repo 를 이전에 받아 둔 경우 해당 파일은 이름이 바뀌었으니 다시 받는다.
> macOS 에서 직접 경로를 만들어 쓴다면 `unicodedata.normalize("NFC", path)` 로 정규화한 뒤 비교한다.

폴더명은 CSV의 `label` 값을 그대로 쓴다. 수집처 폴더(`개소리`, `고양이소리`, `자동차경적`,
`Knocking Sound Effects…`, `donateacry_…`)는 각각 `dog_bark`, `cat_meow`, `car_horn`,
`knock`, `baby_cry` 로 흡수됐다.

### 라벨명 규칙 (이 repo 한정)

원본 데이터셋의 한글 라벨 폴더는 이 repo에서 영어로 바뀌었다. 매핑은
`.efficientat_eval_code/prepare_manifest.py` 의 `DEFAULT_LABEL_MAP` 과 동일하다.

| 원본(한글) | repo | 원본(한글) | repo |
|---|---|---|---|
| 경보 | `alarm` | 유리깨지는소리 | `glass_break` |
| 화재경보 | `fire_alarm` | 자전거 | `bicycle` |
| 물소리 | `water` | 총 | `gunshot` |
| 비명 | `scream` | 울음 | `baby_cry` 로 **병합** |

`울음`(AI Hub 사람 울음)은 기존 `baby_cry`(ESC-50 + donateacry)와 같은 폴더에 들어간다.
파일명 충돌은 없다. 두 출처를 구분해야 하면 `clip_metadata.csv` 의 `source_file` 을 쓴다.

`background/clips_2s/` 의 파일명 접두어(`울음__`, `경보__` 등)는 **한글 그대로 유지**된다.
원래 라벨을 영어로 조회하려면 파일명이 아니라 `clip_metadata.csv` 의 `origin_label` 컬럼을 쓴다.

> `musan_mixed_2s/`(MUSAN Noise 혼합본, 약 29GB)는 **2026-10-29 부터 이 repo에 포함**된다.
> 원본 클립만 필요하면 `allow_patterns`/`ignore_patterns` 로 `musan_mixed_2s/**` 를 제외하고 받으면 된다.
> 로컬에서 다시 만들려면 `generate_musan_mixes.py` 를 쓴다 (seed 42, 결정론적).

## 라벨별 수량

| 라벨 | raw | clips_2s | 독립 소스 |
|---|---:|---:|---:|
| baby_cry † | 336 | 9,204 | 325 |
| car_horn | 80 | 771 | 57 |
| cat_meow | 168 | 2,772 | 127 |
| dog_bark | 118 | 1,305 | 106 |
| knock | 536 | 417 | 85 |
| alarm | 403 | 15,810 | 395 |
| water | 238 | 6,714 | 195 |
| scream | 94 | 2,457 | 90 |
| glass_break | 258 | 12,303 | 255 |
| bicycle | 81 | 3,747 | 78 |
| gunshot | 297 | 4,257 | 254 |
| fire_alarm | 169 | 6,150 | 167 |
| background | — | 14,142 | 1,058 |
| **합계** | **2,778** | **80,049** | |

† `baby_cry` 는 원본 `울음`(146 raw / 6,396 clips)과 `baby_cry`(190 raw / 2,808 clips)를 합친 값이다.

### MUSAN 혼합본 수량 (`musan_mixed_2s/`)

각 라벨의 clips_2s × 3 (SNR 20/15/10). `baby_cry` 는 `울음` 혼합본(19,188)과 `baby_cry` 혼합본(8,424)을 합친 값이다.

| 라벨 | 혼합 클립 | 폴더 분할 |
|---|---:|---|
| alarm | 47,430 | part_00~04 (9,486 ×5) |
| background | 42,426 | part_00~04 (8,486 / 8,485 ×4) |
| glass_break | 36,909 | part_00~03 (9,228 / 9,227 ×3) |
| baby_cry | 27,612 | part_00~02 (9,204 ×3) |
| water | 20,142 | part_00~02 (6,714 ×3) |
| fire_alarm | 18,450 | part_00~01 (9,225 ×2) |
| gunshot | 12,771 | part_00~01 (6,386 / 6,385) |
| bicycle | 11,241 | part_00~01 (5,621 / 5,620) |
| cat_meow | 8,316 | 평면 |
| scream | 7,371 | 평면 |
| dog_bark | 3,915 | 평면 |
| car_horn | 2,313 | 평면 |
| knock | 1,251 | 평면 |
| **합계** | **240,147** | |

`raw` 보다 `clips_2s` 소스 수가 적은 건 2초 미만이라 클립이 안 나온 파일(합계 539개, 대부분 `knock`) 때문이다.

> ⚠️ **원본 누락**: `integrated_test_labels_0716.csv` 는 원본 4,756개를 등재하지만 디스크에는
> 2,778개만 있다 (gunshot 1,670→297, glass_break 482→258, car_horn 340→80). 그래서 gunshot 클립이
> 4,257개에 그친다. 누락 원본을 채운 뒤 아래 재생성 3단계를 다시 돌리면 그대로 반영된다.

## 재생성 (3단계)

`edge_audio_dataset/` 에서 실행한다.

```bash
# 1) 0716 CSV → 디스크에 실존하는 원본만 (2,778행)
python make_source_manifest.py

# 2) 2초 분할 + 무음판정 + 증강 → data_augmented/processed_all/<label>/
python -m data_augmented.src.pipeline \
    --manifest integrated_all_0716.csv --input . \
    --output data_augmented/processed_all \
    --log-file data_augmented/pipeline_all.log

# 3) 클립을 <label>/clips_2s/ 로 옮기고 clip_metadata.csv 재생성
python restructure_dataset.py     # 최초 1회 (CSV 경로 재작성 포함, --dry-run 먼저 권장)
python make_clip_metadata.py
```

4-class만 다시 만들려면 1단계를 이렇게 바꾼다:

```bash
python make_source_manifest.py --output integrated_target4_0716.csv \
    --labels gunshot glass_break bicycle baby_cry
```

## 4-class 학습

`baby_cry / bicycle / glass_break / gunshot`. 노트북 7절이 `clip_metadata.csv` 를 읽어
manifest를 만들고, **최소 클래스(bicycle 3,747)에 맞춰 클래스당 3,747개로 downsample** 한다 → 14,988행.

| canonical | 원본 라벨 | 클립 | balance 후 |
|---|---|---:|---:|
| baby_cry | 울음(AI Hub) + baby_cry(ESC-50 + donateacry) | 9,204 | 3,747 |
| bicycle | bicycle | 3,747 | 3,747 |
| glass_break | glass_break | 12,303 | 3,747 |
| gunshot | gunshot | 4,257 | 3,747 |

## 파일명 규칙

```
{원본파일명}_{시작초}_{orig|augN-태그[-태그]}.wav
예) ESC50_1-187207-A-20_0_aug1-shf-gan.wav
    → 원본 ESC50_1-187207-A-20 의 0초 지점 클립에 shf+gan 증강 적용 (1번째 증강본)
```

background 클립은 원래 속했던 라벨이 접두어로 붙는다:

```
{원본라벨}__{원본파일명}_{시작초}_{variant}.wav
예) baby_cry__ESC50_1-22694-A-20_0_orig.wav
```

## clip_metadata.csv 컬럼

| 컬럼 | 설명 |
|---|---|
| `filepath` | edge_audio_dataset/ 기준 상대 경로 (`gunshot/clips_2s/….wav`) |
| `label` | 학습 라벨 (폴더명, NFC 정규화) |
| `source_file` | 원본 음원 파일명 (확장자 제외) |
| `start_sec` | 원본에서 잘라낸 시작 위치(초) |
| `variant` | `orig`(원본) 또는 `aug1`/`aug2`(증강본 번호) |
| `aug_tags` | 적용된 증강 조합, `+` 구분 (예: `shf+gan`) |
| `is_augmented` | 0=원본, 1=증강 |
| `origin_label` | background 클립만: 무음 판정 전 원래 라벨 |

## 증강 태그

증강본 하나당 변환 1~2개를 무작위 조합 적용 (파라미터는 `data_augmented/src/config.py`, SEED=42).
원본:증강 비율 — 이벤트 라벨 **1:2**, background **1:1** (무음 성격 유지 목적).

| 태그 | 변환 | 파라미터 |
|---|---|---|
| `shf` | Time Shift | ±0.5초 (fraction ±0.25, rollover) |
| `gan` | Gain | -6 ~ +6 dB (background는 -6 ~ +3 dB) |
| `agn` | Gaussian Noise | amplitude 0.001 ~ 0.015 |
| `drc` | Dynamic Range 압축/확장 | threshold -30~-15 dB, ratio 1.5~3.0(압축)/1.2~1.6(확장) |
| `ngt` | Noise Gate | threshold -45~-35 dB, 감쇠 12~24 dB |

background 라벨은 무음 성격을 해치지 않도록 `shf`, `gan`만 사용한다 (`agn`/`drc`/`ngt` 제외).

## train/val 분할 시 주의

같은 `source_file`에서 나온 클립들은 서로 겹치는 구간을 공유하므로(50% 오버랩 + 증강),
**클립 단위가 아니라 `source_file` 단위로 분할**해야 데이터 누수가 없다. 노트북의
manifest 빌더가 `group_id = aug_{source_file}` 를 만들고, 학습 스크립트가 `--group-col group_id`
로 GroupKFold를 돌린다.

## MUSAN Noise 오프라인 증강

`generate_musan_mixes.py`는 `clip_metadata.csv`의 전체 클립(기존 증강 및
`background` 포함)에 MUSAN의 **Noise**만 섞는다. Music·Speech는 사용하지 않는다.
원본과 기존 증강본은 바꾸지 않고, 각 입력 클립의 SNR 20/15/10 dB 혼합본을
`musan_mixed_2s/<label>/clips_2s/`에 쓴다.

**이 repo 에서의 위치**: `musan_mixed_2s/<label>/clips_2s/[part_XX/]{원본클립명}_musan-snr{20|15|10}.wav`.
라벨 폴더명은 원본과 같은 영어 규칙(`울음`→`baby_cry` 병합 포함)이고, `part_XX` 분할은 원본 트리와
같은 방식(파일명 정렬 후 균등 분배, 폴더당 10,000개 이하)이다. 분할 경계는 원본 `clips_2s` 와 다르므로
`musan_mix_metadata.csv` 의 `filepath` 를 그대로 써야 한다. `source_filepath` 는 이 repo 의
`clip_metadata.csv` `filepath`(part 경로 포함)와 1:1 로 맞춰 두었다.

MUSAN 에서는 `noise/free-sound/`, `noise/sound-bible/` 의 774개 파일만 쓰였다 (Music·Speech 미사용).
`musan_source` 는 MUSAN 배포본 기준 상대 경로이고 MUSAN 원본 자체는 이 repo 에 없다.

> ⚠️ **background 혼합본의 노이즈 레벨**: background 클립은 peak RMS −30 dBFS 미만이라 SNR 기준이
> 거의 전부 −30 dBFS 바닥값으로 고정된다 (42,426개 중 42,423개). 따라서 섞인 노이즈는 −40~−50 dBFS 수준으로
> 이벤트 라벨 혼합본보다 훨씬 조용하다. "시끄러운 환경의 background" 를 대표한다고 보면 안 된다.

```bash
# 자동 다운로드를 쓸 때만 필요
pip install -r ../requirements-mac.txt

# 첫 실행: MUSAN Noise를 .cache/musan/에 내려받아 전체 생성
python generate_musan_mixes.py --data-root .

# 이미 내려받은 MUSAN으로 작은 스모크 실행
python generate_musan_mixes.py --data-root . --musan-root /path/to/musan --limit 10

# 생성 결과·메타데이터·SNR·원본 그룹 연결 검증
python verify_musan_mixes.py --data-root .
```

### musan_mix_metadata.csv 컬럼 (240,147행)

| 컬럼 | 설명 |
|---|---|
| `filepath` | repo 기준 상대 경로 (`musan_mixed_2s/<label>/clips_2s/[part_XX/]….wav`) |
| `source_filepath` | 섞기 전 클립의 `clip_metadata.csv` `filepath` (part 경로 포함) |
| `label`, `source_file`, `start_sec`, `is_augmented`, `origin_label`, `group_id` | 원본 클립에서 그대로 상속 (`label`/`origin_label` 은 영어) |
| `variant` | 항상 `musan` |
| `aug_tags` | `musan_snr20` / `musan_snr15` / `musan_snr10` |
| `musan_snr` | 목표 SNR (dB) |
| `musan_source`, `musan_start_sample` | 사용한 MUSAN noise 파일(MUSAN 루트 기준)과 시작 샘플 |
| `seed` | 42 |
| `clean_rms_reference` | SNR 계산 기준 RMS (= max(클린 RMS, −30 dBFS)) |
| `noise_rms`, `measured_snr_db` | 혼합 후 측정한 noise RMS 와 실제 SNR |
| `status`, `error` | 전 행 `complete` |

원본 클립과 그 MUSAN 혼합본은 같은 `group_id` 를 가지므로, train/val 분할은 여기서도 `group_id` 단위로 해야 한다.

`musan_mix_metadata.csv`는 출력·원본 경로, 라벨, `source_file`,
`group_id=aug_<source_file>`, MUSAN Noise 파일/시작 샘플, SNR, RMS, seed,
완료 상태를 보관한다. 완료 행과 WAV가 함께 있으면 재실행 시 건너뛰고, WAV가
사라졌거나 실패 행이면 같은 seed와 동일 선택으로 다시 만든다.

클린 RMS가 −30 dBFS보다 작으면 −30 dBFS를 SNR 계산 기준으로 사용한다. 혼합 후
피크가 1.0을 넘으면 clean/noise를 함께 축소하므로 SNR은 유지된다.
