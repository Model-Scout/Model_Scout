---
license: other
task_categories:
  - text-to-speech
  - audio-classification
language:
  - ko
tags:
  - asmr
  - korean
  - tts
  - voice-clone
  - speech
size_categories:
  - 1K<n<10K
---

# Povel Hearheart Dataset

한국어 성인 ASMR 음성 데이터셋. Hearheart.com에서 수집한 1,142개 오디오 파일을 처리하여 5,238개 세그먼트로 분할.

## Dataset Structure

```
raw/hearheart/audio/           # 원본 1,142개 WAV 파일 (4.8GB, 29.3시간)
processed/hearheart/
  ├── vocals/                  # Demucs 보컬 분리 결과 (4.8GB)
  ├── segments/segments/       # VAD 세그먼트 5,238개 WAV (3.5GB)
  ├── segments/segment_index.json  # 세그먼트 인덱스
  ├── encoded.jsonl            # 코덱 인코딩 결과 4,744개 (79MB)
  ├── filtered.jsonl           # 필터링 결과
  └── demucs_results.json      # Demucs 처리 메타데이터
```

## Processing Pipeline

```
원본 오디오 → Demucs (음원 분리) → VAD (음성 구간 감지) → Whisper (전사) → 품질 필터링 → 코덱 인코딩
```

1. **Demucs**: 배경 음악/노이즈에서 보컬 분리
2. **VAD (Voice Activity Detection)**: 음성 구간 자동 감지 및 세그먼트 분할
3. **Whisper**: 한국어 전사 (STT)
4. **Quality Filtering**: 품질 기준 미달 세그먼트 제거
5. **Codec Encoding**: Qwen3-TTS 12Hz 16-channel RVQ 코덱으로 인코딩

## Audio Specifications

- Sample Rate: 24kHz
- Channels: Mono
- Bit Depth: 16-bit PCM
- Format: WAV

## Use Cases

- **Voice Clone Reference**: TTS 모델의 voice clone 레퍼런스 오디오로 사용
- **TTS Fine-tuning**: 음성 합성 모델 학습 데이터
- **Audio Classification**: ASMR 음성 분류 연구

## Related Project

- GitHub: [povel-project](https://github.com/Hyeonseop-Shin/povel-project)

## Citation

이 데이터셋은 연구 목적으로 수집되었습니다.
