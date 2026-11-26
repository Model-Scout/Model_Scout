import type { Candidate, Pipeline } from "./api";

/** A basic flow from the candidates when the writer gave none: input -> each task's top model in turn -> result,
 * service data into the first model, and the fine-tuning branch when there is an SFT candidate. */
export function fallbackPipeline(candidates: Candidate[]): Pipeline | null {
  const { training, service } = combinations(candidates);
  // One model per task (tags[0]): a "both" model's role also carries its SFT reason, which reads as a new role.
  const tasks = new Set<string>();
  const lines = candidates.filter((c) => {
    if (c.type !== "model" || c.group === "sft" || tasks.has(c.tags[0] ?? "")) return false;
    tasks.add(c.tags[0] ?? "");
    return true;
  }).map((model) => ({ model }));
  if (lines.length === 0) return null;
  const nodes: Pipeline["nodes"] = [];
  const edges: Pipeline["edges"] = [];
  const add = (id: string, label: string, candidate_id?: string) => {
    if (!nodes.some((n) => n.id === id)) nodes.push({ id, label, candidate_id });
  };
  const first = lines[0].model.id;
  // Needs come most important first, which is usually the order work flows (받아쓰기 -> 요약): chain them.
  add("in", "사용자 입력");
  let previous = "in";
  for (const { model } of lines) {
    add(model.id, model.name, model.id);
    edges.push({ source: previous, target: model.id });
    previous = model.id;
  }
  add("out", "결과");
  edges.push({ source: previous, target: "out" });
  for (const d of service) {
    add(d.id, d.name, d.id);
    edges.push({ source: d.id, target: first });
  }
  const main = new Set(lines.map((l) => l.model.id));
  const sft = candidates.find((c) => c.type === "model" && c.group === "sft")
    ?? candidates.find((c) => c.type === "model" && c.group === "both" && !main.has(c.id));
  if (sft) {
    add("sft-step", "파인튜닝 (SFT)");
    add(sft.id, sft.name, sft.id);
    for (const d of training) {
      add(d.id, d.name, d.id);
      edges.push({ source: d.id, target: "sft-step" });
    }
    edges.push({ source: "sft-step", target: sft.id }, { source: sft.id, target: first, label: "파인튜닝 모델 제공" });
  }
  return { nodes, edges };
}

/** One line per need: its top model and the data linked to it, then the project-level data. */
export function combinations(candidates: Candidate[]) {
  const byId = new Map(candidates.map((c) => [c.id, c]));
  const roles = new Set<string>();
  const lines: { model: Candidate; datasets: Candidate[] }[] = [];
  // Candidates keep the backend's need-then-rank order, so the first model naming a role is that need's top pick.
  for (const m of candidates) {
    if (m.type !== "model") continue;
    const own = m.role.split(" / ");
    if (own.every((r) => roles.has(r))) continue;
    own.forEach((r) => roles.add(r));
    lines.push({ model: m, datasets: m.related.map((id) => byId.get(id)).filter((d): d is Candidate => d?.type === "dataset").slice(0, 2) });
  }
  const datasets = candidates.filter((c) => c.type === "dataset");
  const byRole = (role: string) => datasets.filter((d) => d.role.includes(role)).slice(0, 3);
  return { lines, training: byRole("프로젝트 학습·평가"), service: byRole("서비스 데이터") };
}
