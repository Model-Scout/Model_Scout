---
language:
- ko
task_categories:
- text-to-speech
configs:
- config_name: Gemini_4p7k
  data_files:
  - split: data
    path: Gemini_4p7k_20261028/labels/part-*.parquet
---

# MAGO share — Gemini 4.7k 게시 완료

Gemini 4.7k의 라벨과 새 audio-only TAR40개가 게시·검증됐습니다. AIHub2k와 Gemini5k는 **METADATA_ONLY**이며 그 두 config는 비활성화 상태입니다.
HF의 `data` split은 조회용 인덱스 전체를 뜻하고 실제 훈련용 재분할이나 현재 학습 사용을 뜻하지 않습니다.

| 폴더 | 게시 범위 |
|---|---|
| `Gemini_4p7k_20261028/` | KO1,003,739개, 약4,721시간. 원음본문420.181581136GB와 새 audio-only TAR40개420.952135680GB, 최신v1.2라벨 |
| `AIHub_2k_20261028/` | 라벨·인덱스1,665,812행만. 원음332패키지는 미포함 / METADATA_ONLY |
| `Gemini_5k_KO_20261028/` | KO인덱스1,041,026행과 원문bilingual라벨만. 원음 미포함 / METADATA_ONLY |

## 원본과 라벨 보존

공통 Parquet는 동일한 36개 열을 사용하고, 음성은 `audio_archive` + `audio_member`로 연결합니다. 음성 바이트를 Parquet 안에 넣지 않습니다.
`caption`(실제 음성을 기술하는 설명), `instruction_ko/en`(발화 지시문), `generation_prompt`(실제 생성 요청)를 구분합니다.
Gemini에 실제 음성 분석 caption을 새로 만들어 넣지 않습니다. 원본에 없는 필드는 null을 유지합니다.

원본 라벨은 바이트 그대로 보관하고 공통 인덱스의 `original_record_json`에도 원래 필드와 타입·값을 남깁니다.
증적용 원문에는 원래 출처 경로·기존 문서가 포함될 수 있습니다. 그것은 현재 서버에서 실행할 경로나 현재 게시 상태를 안내하는 문서가 아닙니다.
원래 SHA256SUMS가 가리키는 옛 TAR와 이번 새 TAR의 무결성 표는 구분해야 합니다.

AIHub의 train/validation과 Gemini의 원래 분할·선정 플래그는 현 훈련 사용 증명이 아닙니다.
Gemini 5k 활성 인덱스·향후 음성은 KO만 대상이며, 보존용 원본 gzip 3개에는 KO+EN 행이 함께 들어 있습니다. EN 음성은 이번 KO 폴더 대상에 포함하지 않습니다.

원본 데이터별 이용·재배포 조건을 유지합니다. 소유자 정책은 Public + 수동 승인 Gated이며 접근 설정은 운영자가 관리합니다.

새 TAR는 기존 audio_archive/audio_member 경로를 유지하고 음성만 담습니다. 옛 TAR 내부 JSON은 제외했습니다. 원음 바이트·샘플링레이트는 변환하지 않았으며 새 size/SHA256은 G4 archive_manifest.json에 기록했습니다. 원문 SHA256SUMS의 옛 TAR 해시를 이번 새 TAR에 재사용하지 않습니다.
