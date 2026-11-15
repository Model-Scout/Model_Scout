---
language: ko
license: mit
base_model: klue/bert-base
pipeline_tag: text-classification
tags: [voice-phishing, korean, klue, bert, onnx, int8, voicekeeper]
---
# VoiceKeeper · KLUE-BERT 보이스피싱 분류기

`klue/bert-base`를 보이스피싱/정상 이진 분류로 파인튜닝하고 **int8 ONNX**(111 MB)로 내보낸 모델입니다.
[VoiceKeeper](https://v-shield-ai-demo.onrender.com/) 서비스에서 LLM 판정과 나란히 쓰이는 독립 엔진입니다 (`onnxruntime` + `tokenizers`만으로 CPU 추론).

## 학습 데이터
- **시드 48건**: 금융감독원 보이스피싱 지킴이 공개 사례 유형을 따라 수작업 작성 (기관 사칭·안전계좌·자녀 사칭·스미싱·대출·투자 등). **학습에 사용하지 않고** 분포 밖 검증에만 사용.
- **합성 1,302건**: Gemini로 14개 사기 유형 × 3 형식(통화 전사·문자·카톡)과 12개 정상 유형을 생성. 정상 OTP 문자, 은행 입금 알림, 택배 안내처럼 사기 단어가 등장하는 **어려운 정상 예시** 포함.
- 학습/검증 분할은 합성 데이터 안에서만 수행하고 소수 클래스는 오버샘플링.

## 성능
| 세트 | n | 정확도 | 정밀도 | 재현율 | F1 |
| --- | --- | --- | --- | --- | --- |
| 합성 검증 | 162 | 0.988 | 1.000 | 0.977 | 0.988 |
| 시드(분포 밖) | 48 | 0.917 | 1.000 | 0.833 | 0.909 |

int8 양자화 전후 확률 평균 차이 0.005. 놓친 사례는 정중한 말투의 대출·환급·리딩방 유형이어서 서비스에서는 LLM 판정과 앙상블합니다.

## 사용
```python
import numpy as np, onnxruntime as ort
from tokenizers import Tokenizer
tok = Tokenizer.from_file('tokenizer.json'); tok.enable_truncation(192)
sess = ort.InferenceSession('model.onnx', providers=['CPUExecutionProvider'])
e = tok.encode('검찰청입니다. 안전한 계좌로 돈을 옮기고 가족에게는 말하지 마세요.')
logits = sess.run(['logits'], {'input_ids': [e.ids], 'attention_mask': [e.attention_mask], 'token_type_ids': [e.type_ids]})[0][0]
p = np.exp(logits - logits.max()); print('phishing prob', p[1] / p.sum())
```

참고용 점수이며 보정된 사기 확률이 아닙니다. 실제 신고 원문 데이터가 확보되면 `scripts/ml/train_klue.py`로 재학습할 수 있습니다.

```json
{
  "base_model": "klue/bert-base",
  "task": "voice-phishing vs benign (binary)",
  "max_len": 192,
  "epochs": 3,
  "batch": 16,
  "lr": 3e-05,
  "train_rows": 1232,
  "train_rows_note": "synthetic only, class-balanced by oversampling",
  "val_synthetic": {
    "n": 162,
    "accuracy": 0.988,
    "precision": 1.0,
    "recall": 0.977,
    "f1": 0.988
  },
  "seed_holdout_ood": {
    "n": 48,
    "accuracy": 0.917,
    "precision": 1.0,
    "recall": 0.833,
    "f1": 0.909,
    "note": "hand-written FSS-pattern seeds, never used in training"
  },
  "onnx_int8_mean_abs_diff_vs_fp32": 0.0054,
  "onnx_size_mb": 111.4,
  "cpu_latency_48_texts_s": 0.92,
  "data": {
    "seed": 48,
    "synthetic": 1302,
    "generator": "gemini-3.6-flash / 3.5-flash-lite",
    "hard_negatives": "real OTP, bank, parcel, government notices"
  },
  "trained_at": "2026-09-22 01:25",
  "labels": {
    "0": "benign",
    "1": "phishing"
  }
}
```
