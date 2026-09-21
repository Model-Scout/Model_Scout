---
library_name: transformers
base_model: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
base_model_revision: 9b74e35d4c7e4ffec489f4171273caca8948a2b9
language:
- ko
tags:
- transformers
- causal-lm
- lora
- clora
- korean
license: apache-2.0
---

# HyperCLOVA X SEED Think-14B CLoRA 71875-3000

## 모델 개요

이 모델은 naver-hyperclovax/HyperCLOVAX-SEED-Think-14B pristine Base에 AI Hub 71875 필수의료 의학지식 QA 데이터 3,000개를 사용해 공식 CLoRA orthogonal regularization을 적용한 SFT 결과입니다. 기존 Vanilla LoRA와 동일한 학습 데이터와 LoRA capacity를 유지하면서, Base 모델의 기존 능력 보존을 목표로 k=64, lambda=0.005 설정을 사용했습니다. 학습이 끝난 LoRA adapter를 pristine Base에 병합한 standalone BF16 모델입니다.

## 베이스 모델

- Base: naver-hyperclovax/HyperCLOVAX-SEED-Think-14B
- Revision: 9b74e35d4c7e4ffec489f4171273caca8948a2b9

## 학습 설정

- Method: CLoRA orthogonal regularization + LoRA SFT
- Data: AI Hub 71875, clean 3,000 samples
- LoRA: r=16, alpha=32, dropout=0.05
- Target modules: q/k/v/o_proj, gate/up/down_proj
- Learning rate: 5e-5
- Scheduler: cosine, warmup ratio 3%
- Epoch: 1, effective batch size: 16
- Sequence length: 4096, BF16, packing=false
- Seed/data seed: 42
- CLoRA: k=64, lambda=0.005
- Output: merged standalone BF16 checkpoint

## 활용 데이터

- AI Hub 71875 필수의료 의학지식 QA
- URL: https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=71875

## 로컬 B1 benchmark

B1_constrained 단일 probe, 5개 주 지표의 parsed accuracy 평균입니다. 실제 K-AI 리더보드 결과가 아닙니다.

| 평균 | KMMLU-Pro | CLIcK | HLE(Ko) | MuSR(Ko) | Com2-main(Ko) |
|---:|---:|---:|---:|---:|---:|
| 0.4725 | 0.4578 | 0.7439 | 0.0463 | 0.5587 | 0.5556 |
