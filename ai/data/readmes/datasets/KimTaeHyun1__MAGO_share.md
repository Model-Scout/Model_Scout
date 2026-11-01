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
- config_name: AIHub_2k
  data_files:
  - split: data
    path: AIHub_2k_20261028/labels/part-*.parquet
- config_name: Gemini_5k_KO
  data_files:
  - split: data
    path: Gemini_5k_KO_20261028/labels/part-*.parquet
---

# MAGO share — 3개 데이터셋 음성·라벨 게시 완료

AIHub 2k, Gemini 4.7k, Gemini 5k KO의 아래 원음 패키지와 공통 라벨이 모두 고정 commit에서 검증됐습니다.
기존 Gemini_4p7k YAML config는 그대로 유지하고, 두 데이터셋의 완료 검증 후 AIHub_2k·Gemini_5k_KO config를 추가했습니다. HF의 `data` split은 조회용 인덱스이며 실제 훈련용 분할이나 현재 학습 사용을 뜻하지 않습니다.

| 폴더 | 검증된 게시 범위 |
|---|---|
| `AIHub_2k_20261028/` | 1,665,812행·약2,042.12시간. 새 gzip TAR 62개, 실제 패키지 513,068,563,276B. 원음 WAV/FLAC 및 원본 JSON/instruction/tag sidecar 보존 |
| `Gemini_4p7k_20261028/` | KO 1,003,739개·약4,721.06시간. audio-only TAR 40개 420,952,135,680B, 원음 본문 420,181,581,136B, 최신 v1.2 라벨. 기존 완료본 변경 없음 |
| `Gemini_5k_KO_20261028/` | KO 1,041,026개·약4,682.97시간. audio-only TAR 47개 449,559,214,080B, 원음 본문 448,759,778,413B. 보존용 원문 bilingual gzip 3개는 그대로 유지 |

## 라벨·원음 연결과 보존

공통 Parquet는 동일한 36개 열이며, 음성은 데이터셋 폴더 기준 `audio_archive` + `audio_member`로 연결합니다. 음성 바이트를 Parquet에 내장하지 않습니다.
AIHub/Gemini5k의 활성 locator는 이번 약10GB 패키지를 가리키며, `original_record_json`과 `labels/original/` 안의 옛 경로는 원문 출처 증적입니다. 원문과 원본 라벨 바이트는 수정하지 않았습니다.
AIHub는 약10GB 목표·압축 출력 상한11GB이며 실제 크기는 각 `archive_manifest.json`에 기록했습니다. Gemini5k 새 TAR는 각각 10,000,000,000B 이하입니다. 패키지 크기에는 TAR 헤더/패딩, AIHub의 경우 압축·sidecar도 포함되므로 순수 음성량과 구분합니다.

`caption`은 실제 음성을 기술하는 설명, `instruction_ko/en`은 발화 지시문, `generation_prompt`는 생성 요청입니다. Gemini에 새 음성 분석 caption을 만들지 않았고 없는 필드는 null입니다.
AIHub train/validation과 원래 선정·QC 플래그는 현재 학습 사용의 증거가 아닙니다. Gemini5k 활성 인덱스·음성은 KO만이며 원문 gzip에는 KO+EN 라벨이 함께 들어 있습니다. EN 음성은 포함하지 않습니다.
Gemini5k의 1,205개 `.flac` 파일명은 실제 RIFF/WAVE PCM16 24kHz mono이며 `audio_format=wav`가 정확합니다. 확장자로 container를 판단하지 마세요. 파일명·원음 바이트·native sampling rate는 변환하지 않았습니다.

새 패키징은 원음 재인코딩·리샘플링·삭제를 하지 않았습니다. G4는 audio-only TAR로 옛 내부 JSON을 제외했고, AIHub는 원래 sidecar까지 보존합니다. 옛 TAR의 SHA256을 새 TAR에 재사용하지 않으며 새 archive와 공개 member SHA256 proof를 구분합니다.
20261028/20261029는 공유 준비·게시 snapshot 날짜이며 생성/녹음/캡션 작성일을 추정한 값이 아닙니다. 데이터별 원래 이용·재배포 조건은 유지됩니다. 소유자 정책은 Public + 수동 승인 Gated이며 접근 설정은 운영자가 관리합니다.
