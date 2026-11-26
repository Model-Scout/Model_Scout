// Run: node src/lib/spec.test.mjs (Node 22.6+ strips the TypeScript types)
import assert from "node:assert/strict";
import { buildPrompt, buildSpec } from "./spec.ts";
import { fallbackPipeline } from "./flow.ts";

const m = { id: "model:a/stt", type: "model", source_id: "a/stt", name: "stt", role: "받아쓰기", tags: [], url: null, related: [], group: "need",
  context_length: null, parameters_b: 1.5, checks: [{ label: "상업 이용", status: "check", reason: "라이선스 확인", quote: null }] };
const result = { title: "회의록 요약", summary: ["음성을 요약"], needs_check: ["GPU"], candidates: [m], assessment: null, combination: [] };
const pipeline = { nodes: [{ id: "in", label: "사용자 입력" }, { id: m.id, label: "stt", candidate_id: m.id }], edges: [{ source: "in", target: m.id }] };

const s = buildSpec(result, [{ role: "user", content: "회의 녹음 요약\n조건: 언어 한국어, 실행 환경 CPU만, 상업적 이용 가능." }], pipeline);
assert.ok(s.startsWith("# 회의록 요약 구현 명세"));
assert.ok(s.includes("- 사용자 입력 → stt"));
assert.ok(s.includes("- 상업 이용: 확인 필요 — 라이선스 확인"));
assert.ok(s.includes("조건: 언어 한국어, 실행 환경 CPU만, 상업적 이용 가능."));
// No flow: still lists the top model.
assert.ok(buildSpec(result, [], null).includes("### stt (모델)"));
// The prompt carries the spec itself: no SPEC.md needed beforehand.
assert.ok(buildPrompt(s).endsWith(s));

const pharmacy = {
  id: "dataset:example/pharmacy", source_id: "example/pharmacy", name: "심야약국 정보", type: "dataset",
  url: "https://example.com/pharmacy", role: "서비스 데이터", related: [],
  checks: [{ label: "지역", status: "check", reason: "제주만 제공", quote: "제주 심야약국" }],
};
const clinic = { ...pharmacy, id: "dataset:example/clinic", source_id: "example/clinic", name: "병의원 진료시간",
  url: "https://example.com/clinic", checks: [] };
const medical = { ...result, title: "문 연 병원·약국 찾기", candidates: [pharmacy, clinic] };
const turns = [
  { role: "user", content: "밤늦게나 주말에 문 연 약국과 병원을 찾아줘" },
  { role: "assistant", type: "clarify", content: "어느 지역을 대상으로 하나요?" },
  { role: "user", content: "서울이요" },
  { role: "assistant", type: "answer", display: "recommendation", content: "추천 완료" },
  { role: "user", content: "앞으로는 제주만 검색해 줘" },
  { role: "assistant", type: "answer", display: "recommendation", content: "다시 추천 완료" },
  { role: "user", content: "이 API는 왜 추천했어?" },
  { role: "assistant", type: "answer", display: "chat", content: "후보 설명" },
  { role: "user", content: "아직 추천되지 않은 지역" },
  { role: "assistant", type: "clarify", content: "어디인가요?" },
];
const dataOnly = buildSpec(medical, turns, fallbackPipeline(medical.candidates));
assert.ok(dataOnly.includes("## 추천 데이터 후보"));
assert.ok(dataOnly.includes("`example/pharmacy` · https://example.com/pharmacy"));
assert.ok(dataOnly.includes("`example/clinic` · https://example.com/clinic"));
assert.ok(dataOnly.includes("제주만 제공 · “제주 심야약국”"));
assert.ok(dataOnly.includes("2. (질문) 어느 지역을 대상으로 하나요?\n   (답변) 서울이요"));
assert.ok(dataOnly.includes("3. 앞으로는 제주만 검색해 줘"));
assert.ok(!dataOnly.includes("이 API는 왜 추천했어?"));
assert.ok(!dataOnly.includes("아직 추천되지 않은 지역"));

const dataFlow = { nodes: [{ id: "in", label: "지역 입력" }, { id: "data", label: "약국 조회", candidate_id: pharmacy.id }],
  edges: [{ source: "in", target: "data" }] };
const fresh = buildSpec({ ...medical, requirements: ["새 프로젝트 요구사항\n조건: 한국어."] }, turns, dataFlow);
const [used, additional] = fresh.split("## 추가 데이터 후보");
assert.ok(used.includes("### 심야약국 정보 (데이터)"));
assert.ok(additional.includes("### 병의원 진료시간 (데이터)"));
assert.ok(!additional.includes("심야약국 정보"));
assert.ok(buildPrompt(fresh).includes("새 프로젝트 요구사항"));
assert.ok(!fresh.includes("앞으로는 제주만 검색해 줘"));
console.log("ok");
