"use client";

import { useLayoutEffect, useRef, useState } from "react";
import type { Candidate, Pipeline } from "@/lib/api";

// Pastel versions of the app's colors: models are brand purple, data is ok green (text-brand / text-ok).
const styles = {
  data: { name: "데이터", card: "border-[#c9e6d4] bg-[#eef8f2]", tag: "text-ok", marker: "border-[#c9e6d4] bg-[#eef8f2]" },
  model: { name: "모델", card: "border-[#e6d2e2] bg-[#f6ecf3]", tag: "text-brand", marker: "border-[#e6d2e2] bg-[#f6ecf3]" },
  step: { name: "처리", card: "border-line bg-soft", tag: "text-muted", marker: "border-line bg-soft" },
  sft: { name: "파인튜닝(선택)", card: "border-dashed border-[#c99bc1] bg-[#f6ecf3]", tag: "text-brand", marker: "border-dashed border-[#c99bc1] bg-white" },
  output: { name: "결과", card: "border-2 border-brand bg-white", tag: "text-muted", marker: "" },
};
type Kind = keyof typeof styles;

// shortcut: a fine-tuning step is recognised by its label, since the graph JSON has no step kind; add one if this misfires.
const TRAINING = /파인튜닝|SFT|LoRA|fine-?tun/i;
const PUBLIC = /^(?:data_go_kr|seoul_open_data|data-go-kr|seoul)(?:\/|$)|^(?:공공데이터포털|서울 열린데이터광장)$/;
const NUMBERS = "①②③④⑤⑥⑦⑧⑨";

type Node = Pipeline["nodes"][number] & { candidate?: Candidate; kind: Kind; track: boolean; col: number; row: number; span: number };

function layout(pipeline: Pipeline, candidates: Candidate[]) {
  const byId = new Map(candidates.map((c) => [c.id, c]));
  const targets = (id: string) => pipeline.edges.filter((e) => e.source === id).map((e) => e.target);
  const sources = (id: string) => pipeline.edges.filter((e) => e.target === id).map((e) => e.source);
  const nodes: Node[] = pipeline.nodes.map((node) => {
    const candidate = byId.get(node.candidate_id ?? "");
    const kind: Kind = candidate
      ? candidate.type === "dataset" ? "data" : candidate.group === "sft" ? "sft" : "model"
      : TRAINING.test(node.label) ? "sft" : targets(node.id).length ? "step" : "output";
    return { ...node, candidate, kind, track: kind === "sft", col: 0, row: 0, span: 1 };
  });
  const byNode = new Map(nodes.map((n) => [n.id, n]));
  // Data that only feeds the fine-tuning track belongs to that track, not to the service flow.
  for (let changed = true; changed; ) {
    changed = false;
    for (const n of nodes) {
      const out = targets(n.id);
      if (!n.track && out.length && out.every((t) => byNode.get(t)!.track)) n.track = changed = true;
    }
  }
  for (const track of [false, true]) {
    const group = nodes.filter((n) => n.track === track);
    // Track cards sit one column right of whatever feeds them, so a track card lands under the stage it follows.
    const depth = (n: Node): number => Math.max(-1, ...sources(n.id).map((s) => byNode.get(s)!)
      .filter((s) => track || !s.track).map((s) => (s.track === track ? depth(s) : s.col))) + 1;
    group.forEach((n) => (n.col = depth(n)));
    const last = Math.max(0, ...group.map((n) => n.col));
    for (const n of group) if (n.kind === "output") n.col = last;
    const taken = new Set<string>();
    for (const n of [...group].sort((a, b) => a.col - b.col)) {
      const placed = sources(n.id).map((s) => byNode.get(s)!).filter((s) => s.track === track && s.col < n.col);
      let row = placed.length ? Math.min(...placed.map((s) => s.row)) : 0;
      while (taken.has(`${n.col}:${row}`)) row++;
      n.row = row;
      taken.add(`${n.col}:${row}`);
    }
    // A lone result spans every row so each input arrow reaches it straight across.
    const outputs = group.filter((n) => n.col === last && n.kind === "output");
    if (outputs.length === 1 && group.filter((n) => n.col === last).length === 1) {
      outputs[0].row = 0;
      outputs[0].span = Math.max(1, ...group.map((n) => n.row + 1));
    }
  }
  const main = nodes.filter((n) => !n.track);
  const columns = Math.max(1, ...nodes.map((n) => n.col + 1));
  let models = 0;
  const headers = Array.from({ length: Math.max(0, ...main.map((n) => n.col + 1)) }, (_, col) => {
    const kinds = new Set(main.filter((n) => n.col === col).map((n) => n.kind));
    const name = kinds.has("output") ? "결과" : kinds.size === 1 && kinds.has("data") ? "입력 데이터"
      : kinds.size === 1 && kinds.has("model") ? (models++ ? "후처리 모델" : "모델") : "처리";
    return `${NUMBERS[col] ?? col + 1} ${name}`;
  });
  const edges = pipeline.edges.flatMap((e) => {
    const from = byNode.get(e.source);
    const to = byNode.get(e.target);
    return from && to ? [{ ...e, from, to }] : [];
  });
  return { nodes, main, track: nodes.filter((n) => n.track), columns, headers, edges };
}

type Select = { selectedId?: string; onSelect?: (id: string) => void };

function Card({ node, cardRef, selectedId, onSelect }: { node: Node; cardRef: (el: HTMLElement | null) => void } & Select) {
  const { kind, candidate, label, note } = node;
  const isData = kind === "data";
  const look: Kind = kind === "sft" && !candidate ? "step" : kind;
  const [tag, title, sub] = isData
    ? [node.track ? "파인튜닝용 데이터" : PUBLIC.test(candidate?.source_id ?? "") || PUBLIC.test(candidate?.source ?? "") ? "공공데이터" : "데이터셋",
      label, note || candidate?.name]
    : candidate
      ? [kind === "sft" ? "파인튜닝 모델 · SFT" : label.includes(candidate.name) ? candidate.tags[0] ?? "모델" : label, candidate.name, note || (kind === "sft" ? label : candidate.role)]
      : [kind === "output" ? "결과" : node.track ? "학습 단계" : "처리", label, note];
  const className = `relative z-10 flex min-w-0 flex-col justify-center rounded-xl border px-4 py-3 text-left ${styles[look].card}`;
  const style = { gridColumn: node.col + 1, gridRow: `${node.row + 1} / span ${node.span}` };
  const body = (
    <>
      <span className={`text-[11px] font-semibold ${styles[look].tag}`}>{tag}</span>
      <b className={`[overflow-wrap:anywhere] leading-snug ${kind === "output" ? "text-base" : "text-sm"}`}>{title}</b>
      {sub && <span className={`mt-0.5 text-xs text-muted ${kind === "output" ? "" : "line-clamp-2"}`}>{sub}</span>}
    </>
  );
  // Candidate cards open the same detail panel as the model and data lists.
  return candidate && onSelect ? (
    <button ref={cardRef} aria-current={candidate.id === selectedId} onClick={() => onSelect(candidate.id)} style={style}
      className={`${className} transition hover:shadow-md aria-[current=true]:ring-2 ${isData ? "aria-[current=true]:ring-ok/60" : "aria-[current=true]:ring-brand/60"}`}>
      {body}
    </button>
  ) : (
    <div ref={cardRef} className={className} style={style}>{body}</div>
  );
}

type Line = { key: string; d: string; dashed: boolean; sft: boolean; label?: string; x: number; y: number; vertical: boolean };

export function PipelineDiagram({ pipeline, candidates, fineTuning, selectedId, onSelect }:
  { pipeline: Pipeline; candidates: Candidate[]; fineTuning?: string } & Select) {
  const { main, track, columns, headers, edges } = layout(pipeline, candidates);
  const sft = candidates.filter((c) => c.type === "model" && c.group === "sft");
  const box = useRef<HTMLDivElement>(null);
  const cards = useRef(new Map<string, HTMLElement>());
  const [lines, setLines] = useState<Line[]>([]);
  const signature = JSON.stringify(pipeline);

  // Arrows follow the cards' measured boxes, so they stay right when the layout wraps or resizes.
  useLayoutEffect(() => {
    const root = box.current;
    if (!root) return;
    const draw = () => {
      const origin = root.getBoundingClientRect();
      const rect = (id: string) => {
        const r = cards.current.get(id)!.getBoundingClientRect();
        return { l: r.left - origin.left, r: r.right - origin.left, t: r.top - origin.top, b: r.bottom - origin.top,
          cx: r.left - origin.left + r.width / 2, cy: r.top - origin.top + r.height / 2 };
      };
      // Arrows from the service flow into one card meet at a joint, so the card gets a single arrowhead.
      const joined = new Set(edges.filter((e) => !e.from.track && !e.to.track)
        .map((e) => e.to.id).filter((id, i, all) => all.indexOf(id) !== i));
      setLines(edges.map(({ from, to, label }) => {
        const s = rect(from.id);
        const t = rect(to.id);
        const base = { key: `${from.id}-${to.id}`, label, dashed: to.track, sft: from.track || to.track };
        if (from.track !== to.track && Math.abs(s.cx - t.cx) < (s.r - s.l) / 2) { // same column: straight up or down
          const [y1, y2] = s.t > t.b ? [s.t, t.b] : [s.b, t.t];
          return { ...base, d: `M${t.cx},${y1} V${y2}`, x: t.cx + 10, y: (y1 + y2) / 2, vertical: true };
        }
        if (from.track && !to.track) { // up from the fine-tuning track into the service flow
          const y = s.t > t.b ? t.b : t.t;
          return { ...base, d: `M${s.r},${s.cy} H${t.cx} V${y}`, x: t.cx + 10, y: (s.cy + y) / 2, vertical: true };
        }
        if (joined.has(to.id)) {
          const joint = t.l - 22;
          return { ...base, d: `M${s.r},${s.cy} H${joint} V${t.cy} H${t.l}`, x: (s.r + joint) / 2, y: s.cy, vertical: false };
        }
        const y = Math.min(Math.max(s.cy, t.t + 18), t.b - 18);
        if (y === s.cy) return { ...base, d: `M${s.r},${y} H${t.l}`, x: (s.r + t.l) / 2, y, vertical: false };
        const mid = (s.r + t.l) / 2;
        return { ...base, d: `M${s.r},${s.cy} H${mid} V${y} H${t.l}`, x: mid, y: (s.cy + y) / 2, vertical: false };
      }));
    };
    draw();
    const observer = new ResizeObserver(draw);
    observer.observe(root);
    return () => observer.disconnect();
    // eslint-disable-next-line react-hooks/exhaustive-deps -- edges are derived from the pipeline signature
  }, [signature]);

  const register = (id: string) => (el: HTMLElement | null) => void (el ? cards.current.set(id, el) : cards.current.delete(id));
  // Widen the gap between columns until the longest arrow label fits, in up to two lines, between its cards.
  const longest = Math.max(0, ...edges.map((e) => (e.label ?? "").length));
  const gap = Math.min(Math.max(56, longest <= 8 ? longest * 12 + 24 : Math.ceil(longest / 2) * 12 + 28), 120);
  const grid = { gridTemplateColumns: `repeat(${columns}, minmax(150px, 1fr))`, columnGap: gap, rowGap: 20 };
  const legend: Kind[] = ["data", "model", "step", "sft"];

  return (
    <section className="space-y-3 border-t border-line pt-4" aria-label="활용 흐름 제안">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <h3 className="text-base font-bold">활용 흐름 제안</h3>
        <ul className="flex flex-wrap gap-3 text-xs text-muted" aria-label="흐름도 범례">
          {legend.filter((k) => k !== "sft" || track.length || sft.length).map((k) => (
            <li key={k} className="flex items-center gap-1.5"><span className={`size-3 rounded-sm border ${styles[k].marker}`} />{styles[k].name}</li>
          ))}
        </ul>
      </div>
      {/* The padding keeps the selected card's ring from being clipped by the scroll box. */}
      <div className="-mx-1 overflow-x-auto p-1">
        <div ref={box} className="relative space-y-8" style={{ minWidth: columns * 150 + (columns - 1) * gap }}>
          <svg className="pointer-events-none absolute inset-0 z-0 size-full overflow-visible" aria-hidden>
            <defs>
              {["main", "sft"].map((id) => (
                <marker key={id} id={`arrow-${id}`} viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                  <path d="M0,0 L10,5 L0,10 z" fill={id === "sft" ? "#c08fc0" : "#b3a6b2"} />
                </marker>
              ))}
            </defs>
            {lines.map((l) => (
              <path key={l.key} d={l.d} fill="none" stroke={l.sft ? "#c08fc0" : "#b3a6b2"} strokeWidth={l.sft && !l.dashed ? 2 : 1.5}
                strokeDasharray={l.dashed ? "6 5" : undefined} markerEnd={`url(#arrow-${l.sft ? "sft" : "main"})`} />
            ))}
          </svg>
          {lines.filter((l) => l.label).map((l) => (
            <span key={l.key} className={`absolute z-20 rounded bg-white/90 px-1 text-center text-xs leading-tight break-keep text-muted ${l.vertical ? "-translate-y-1/2" : "-translate-x-1/2 -translate-y-[calc(100%+4px)]"}`}
              style={{ left: l.x, top: l.y, width: "max-content", maxWidth: gap - 8 }}>
              {l.label}
            </span>
          ))}

          <div className="grid" style={grid}>
            {headers.map((h, i) => (
              <span key={h} className="text-xs font-semibold text-muted" style={{ gridColumn: i + 1, gridRow: 1 }}>{h}</span>
            ))}
          </div>
          <div className="grid" style={grid}>
            {main.map((n) => <Card key={n.id} node={n} cardRef={register(n.id)} selectedId={selectedId} onSelect={onSelect} />)}
          </div>

          {(track.length > 0 || sft.length > 0) && (
            <div className="space-y-4">
              {track.length > 0 && (
                <div className="grid" style={grid}>
                  {track.map((n) => <Card key={n.id} node={n} cardRef={register(n.id)} selectedId={selectedId} onSelect={onSelect} />)}
                </div>
              )}
              {sft.length > 0 && (
                <p className="relative z-10 flex gap-2 rounded-xl border border-[#f0dfb5] bg-warn-soft px-4 py-3 text-sm leading-relaxed">
                  <span aria-hidden>💡</span>
                  <span>
                    <b>이렇게 파인튜닝해 보세요</b> · {fineTuning || sft[0].role}
                    <span className="mt-1 block text-xs text-muted">
                      출발점 후보: {sft.map((m, i) => <span key={m.id}>{i > 0 && ", "}<b className="text-brand">{m.name}</b></span>)}
                    </span>
                  </span>
                </p>
              )}
            </div>
          )}
        </div>
      </div>
      <ul className="sr-only" aria-label="단계별 연결">
        {edges.map(({ from, to, label }) => (
          <li key={`${from.id}-${to.id}`}>{from.candidate?.name ?? from.label} → {to.candidate?.name ?? to.label}{label && ` (${label})`}</li>
        ))}
      </ul>
    </section>
  );
}
