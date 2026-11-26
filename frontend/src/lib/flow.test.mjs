// Run: node src/lib/flow.test.mjs (Node 22.6+ strips the TypeScript types)
import assert from "node:assert/strict";
import { fallbackPipeline } from "./flow.ts";

const model = (id, group, role = "차트 이해") => ({ id, type: "model", name: id.split("/").pop(), group, role, tags: ["chart"], related: [] });
const data = (id, role) => ({ id, type: "dataset", name: id, role, related: [] });

// Models only, like the chart app answer that came back without a graph.
// The "both" model's role carries its SFT reason too ("차트 이해 / 정확도 개선"): still not a second main model.
const p = fallbackPipeline([model("model:a/main", "need"), model("model:b/alt", "need"), model("model:c/both", "both", "차트 이해 / 정확도 개선"), model("model:d/sft", "sft", "SFT")]);
assert.deepEqual(p.nodes.map((n) => n.id), ["in", "model:a/main", "out", "sft-step", "model:d/sft"]);
assert.ok(p.edges.some((e) => e.source === "model:d/sft" && e.target === "model:a/main"));

// Data goes to the right side: service data into the model, training data into the SFT step.
const q = fallbackPipeline([model("model:a/main", "need"), model("model:d/sft", "sft", "SFT"),
  data("dataset:s", "서비스 데이터"), data("dataset:t", "프로젝트 학습·평가")]);
assert.ok(q.edges.some((e) => e.source === "dataset:s" && e.target === "model:a/main"));
assert.ok(q.edges.some((e) => e.source === "dataset:t" && e.target === "sft-step"));

// Two tasks run one after the other (받아쓰기 -> 요약), not side by side.
const stt = { ...model("model:w/stt", "need", "받아쓰기"), tags: ["speech_recognition"] };
const sum = { ...model("model:t/sum", "need", "요약"), tags: ["summarization"] };
const chain = fallbackPipeline([stt, sum]).edges.map((e) => `${e.source}>${e.target}`);
assert.deepEqual(chain, ["in>model:w/stt", "model:w/stt>model:t/sum", "model:t/sum>out"]);

assert.equal(fallbackPipeline([data("dataset:s", "서비스 데이터")]), null);
console.log("flow ok");
