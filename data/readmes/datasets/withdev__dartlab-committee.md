---
license: apache-2.0
language:
  - ko
tags:
  - finance
  - investment-research
  - evidence
pretty_name: DartLab Trading AI Agent Committee
---

# DartLab — Trading AI Agent Committee

**이 데이터셋은 종목 추천이 아닙니다.** 사용자가 이미 세운 투자 판단을 5단계 AI 위원회가
근거 중심으로 **검증**한 기록입니다. 최종 결론은 매수/매도 의견이 아니라 **판단의 검증 상태**입니다.

## 구조

```
index.json                       목록 — 사례별 요약(검증 상태·근거 커버리지·실패한 위원 수 등)
cases/<caseId>/<runId>.json      심의 1건 전문
```

재실행은 덮어쓰지 않고 새 `runId` 로 쌓입니다. `index.json` 은 사례별 최신 run 만 가리킵니다.

## 검증 상태(verdict)

| 값 | 의미 |
|---|---|
| `VALIDATED` | 근거·반대논리·실행계획·위험 관점에서 판단이 견딤 |
| `VALIDATED_WITH_CONDITIONS` | 견디되 명시된 조건이 전제 |
| `HOLD_FOR_MORE_EVIDENCE` | 지지도 반박도 못 함 — **판단이 틀렸다는 뜻이 아님** |
| `REJECTED` | 논지의 핵심 가정이 근거와 어긋남 |
| `INSUFFICIENT_EVIDENCE` | 수집된 근거가 판정 가능한 수준이 아님 — **데이터의 한계** |
| `INSUFFICIENT_INPUT` | 제출된 판단이 불완전 |

`REJECTED`(판단의 문제)와 `INSUFFICIENT_EVIDENCE`(데이터의 한계)는 다릅니다.

## 정직성 규약

- 모든 주장에 검증 가능한 `evidenceId` 가 붙습니다. 존재하지 않는 근거를 인용한 심의는 게시되지 않습니다.
- 기준 시점(`asOf`) 이후 데이터가 섞인 심의는 게시되지 않습니다.
- 값이 `null` 인 근거는 **없는 것**이며 `0` 이 아닙니다. 조회 실패를 추정치로 채우지 않습니다.
- 확보하지 못한 데이터는 `quality.missingCriticalData` 에 이름으로 남습니다.
- 실행에 실패한 위원은 `status: "failed"` 로 표시되며 성공한 것처럼 집계되지 않습니다.
- 수치는 결정론적 코드가 원본에서 조회하고, LLM 은 해석·검증만 합니다.

## 면책

정보 제공 목적입니다. **투자 권유나 자문이 아니며, 수익을 보장하지 않습니다.**
과거 성과가 미래를 보장하지 않습니다. 투자 판단과 그 결과에 대한 책임은 이용자 본인에게 있습니다.

각 사례의 분석 기준시각·데이터 기준시각·사용 모델·근거 출처는 해당 JSON 의
`provenance` 와 `evidenceSnapshot` 에 기록돼 있습니다.
