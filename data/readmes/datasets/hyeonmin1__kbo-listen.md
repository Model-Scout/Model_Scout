---
license: cc-by-4.0
language:
- ko
task_categories:
- automatic-speech-recognition
pretty_name: KBO-Listen
size_categories:
- 1K<n<10K
---

# KBO-Listen: 야구 중계를 듣고 볼카운트 맞히기

야구 중계 음성을 듣고, 질의 시각마다 볼-스트라이크-아웃(B-S-O)을 맞히는 음성인식 챌린지 데이터셋입니다.
실제 KBO 경기 기록(2023~2026)을 바탕으로 합성한 중계 음성입니다 (가상의 캐스터·해설위원 목소리).

| split | 클립 (Easy / Hard) | 공개 파일 |
|---|---|---|
| train | 1,000 (500 / 500) | audio, queries, gt, scripts, meta |
| dev | 100 (50 / 50) | audio, queries, gt, meta |
| test | 200 (100 / 100) | audio, queries, meta (정답 비공개) |

- `audio/{clip_id}.wav`: 24kHz mono, 반 이닝 분량 (평균 약 97초, 총 약 35시간)
- `queries.json`: `{"clip_id": [t1, t2, ...]}` 질의 시각(초)
- `gt.json`: `{"clip_id": [{"t": 13.59, "b": 0, "s": 1, "o": 0}, ...]}`
- `scripts.jsonl`: 발화별 텍스트·화자·시작/끝 시각 (train만)
- `meta.jsonl`: 트랙(easy/hard), 태그, 시즌, 목소리 등

평가 코드·베이스라인·데이터 생성 과정: https://github.com/jhm991231/kbo-listen

경기 기록 출처: [slothman3878/kbo_playbyplay](https://huggingface.co/datasets/slothman3878/kbo_playbyplay) (CC BY 4.0).
음성 합성: Qwen3-TTS (Apache 2.0). Hard 트랙 대본 의역: Qwen3-32B (Apache 2.0).
