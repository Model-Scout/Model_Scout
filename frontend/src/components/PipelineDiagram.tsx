"use client";

import { useLayoutEffect, useRef, useState } from "react";
import type { Candidate, Pipeline } from "@/lib/api";

// Pastel versions of the app colors: models brand purple, data ok green; steps and results stay plain white.
const styles = {
  data: { card: "border-[#bfdcc9] bg-[#f1f8f3]", tag: "text-ok" },
  model: { card: "border-[#e6d2e2] bg-[#f6ecf3]", tag: "text-brand" },
  step: { card: "border-line bg-white", tag: "text-muted" },
  sft: { card: "border-[#e3cfe0] bg-[#f7eff6]", tag: "text-brand" },
  output: { card: "border-line bg-white", tag: "text-muted" },
};
type Kind = keyof typeof styles;

// shortcut: a fine-tuning step is recognised by its label, since the graph JSON has no step kind; add one if this misfires.
const TRAINING = /파인튜닝|SFT|LoRA|fine-?tun/i;
const PUBLIC = /^(?:data_go_kr|seoul_open_data|data-go-kr|seoul)(?:\/|$)|^(?:공공데이터포털|서울 열린데이터광장)$/;

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
    // A card alone in its column spans every row and sits in the middle (see Card), so a chain of single cards
    // lines up straight across and level with the centre of a taller column of inputs.
    const rows = Math.max(1, ...group.map((n) => n.row + 1));
    for (const n of group) {
      if (group.filter((m) => m.col === n.col).length === 1) {
        n.row = 0;
        n.span = rows;
      }
    }
  }
  const main = nodes.filter((n) => !n.track);
  const columns = Math.max(1, ...nodes.map((n) => n.col + 1));
  const edges = pipeline.edges.flatMap((e) => {
    const from = byNode.get(e.source);
    const to = byNode.get(e.target);
    return from && to ? [{ ...e, from, to }] : [];
  });
  return { nodes, main, track: nodes.filter((n) => n.track), columns, edges };
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
  const className = `relative z-10 flex min-w-0 flex-col justify-center gap-1 rounded-lg border px-4 py-3.5 text-left ${styles[look].card}`;
  const style = { gridColumn: node.col + 1, gridRow: `${node.row + 1} / span ${node.span}`, alignSelf: node.span > 1 ? "center" : undefined };
  const body = (
    <>
      <span className={`text-xs font-semibold ${styles[look].tag}`}>{tag}</span>
      <b className="text-base leading-snug [overflow-wrap:anywhere]">{title}</b>
      {sub && <span className={`text-xs leading-relaxed text-muted ${kind === "output" ? "" : "line-clamp-2"}`}>{sub}</span>}
    </>
  );
  // Candidate cards open the same detail panel as the model and data lists.
  return candidate && onSelect ? (
    <button ref={cardRef} aria-current={candidate.id === selectedId} onClick={() => onSelect(candidate.id)} style={style}
      className={`${className} transition hover:border-ink/30 aria-[current=true]:ring-2 ${isData ? "aria-[current=true]:ring-ok" : "aria-[current=true]:ring-brand"}`}>
      {body}
    </button>
  ) : (
    <div ref={cardRef} className={className} style={style}>{body}</div>
  );
}

type Line = { key: string; d: string; dashed: boolean; sft: boolean; label?: string; x: number; y: number; vertical: boolean; room: number };

export function PipelineDiagram({ pipeline, candidates, selectedId, onSelect }: { pipeline: Pipeline; candidates: Candidate[] } & Select) {
  const { main, track, columns, edges } = layout(pipeline, candidates);
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
      // A card whose arrows to several cards say different things: bent arrows would share one trunk and stack their
      // labels at the same spot, so each one splits off right after the card and carries its label on its own branch.
      // Arrows that all say the same thing keep the shared trunk, where one label reads for all of them.
      const said = new Map<string, Set<string>>();
      for (const e of edges) {
        if (!e.from.track && !e.to.track) said.set(e.from.id, (said.get(e.from.id) ?? new Set()).add((e.label ?? "").trim()));
      }
      const fanned = new Set([...said].filter(([, labels]) => labels.size > 1).map(([id]) => id));
      setLines(edges.map(({ from, to, label }) => {
        const s = rect(from.id);
        const t = rect(to.id);
        const base = { key: `${from.id}-${to.id}`, label, dashed: to.track, sft: from.track || to.track };
        // A line between the service flow and the fine-tuning track may pass behind other cards in that column,
        // so its label sits in the free band just outside the track card, never at the line's middle.
        const trackCard = from.track ? s : t;
        const flowCard = from.track ? t : s;
        const band = trackCard.t > flowCard.b ? trackCard.t - 16 : trackCard.b + 16;
        if (from.track !== to.track && Math.abs(s.cx - t.cx) < (s.r - s.l) / 2) { // same column: straight up or down
          const [y1, y2] = s.t > t.b ? [s.t, t.b] : [s.b, t.t];
          return { ...base, d: `M${t.cx},${y1} V${y2}`, x: t.cx + 10, y: band, vertical: true, room: 240 };
        }
        if (from.track && !to.track) { // up from the fine-tuning track into the service flow
          const y = s.t > t.b ? t.b : t.t;
          return { ...base, d: `M${s.r},${s.cy} H${t.cx} V${y}`, x: t.cx + 10, y: band, vertical: true, room: 240 };
        }
        if (joined.has(to.id)) {
          const joint = t.l - 22;
          return { ...base, d: `M${s.r},${s.cy} H${joint} V${t.cy} H${t.l}`, x: (s.r + joint) / 2, y: s.cy, vertical: false, room: joint - s.r };
        }
        const y = Math.min(Math.max(s.cy, t.t + 18), t.b - 18);
        if (y === s.cy) return { ...base, d: `M${s.r},${y} H${t.l}`, x: (s.r + t.l) / 2, y, vertical: false, room: t.l - s.r };
        if (fanned.has(from.id)) {
          const split = s.r + 14;
          return { ...base, d: `M${s.r},${s.cy} H${split} V${y} H${t.l}`, x: (split + t.l) / 2, y, vertical: false, room: t.l - split };
        }
        // Bend at the same spot as joined arrows, so two bends never run side by side in one gap.
        const joint = t.l - 22;
        return { ...base, d: `M${s.r},${s.cy} H${joint} V${y} H${t.l}`, x: (s.r + joint) / 2, y: s.cy, vertical: false, room: joint - s.r };
      }));
    };
    draw();
    const observer = new ResizeObserver(draw);
    observer.observe(root);
    return () => observer.disconnect();
    // eslint-disable-next-line react-hooks/exhaustive-deps -- edges are derived from the pipeline signature
  }, [signature]);

  const register = (id: string) => (el: HTMLElement | null) => void (el ? cards.current.set(id, el) : cards.current.delete(id));
  // Widen the gap between columns until the longest arrow label fits, in up to two lines, between its cards;
  // +22 leaves room for the joint where several arrows meet before a card.
  const longest = Math.max(0, ...edges.map((e) => (e.label ?? "").length));
  const gap = Math.min(Math.max(56, (longest <= 8 ? longest * 12 + 24 : Math.ceil(longest / 2) * 12 + 28) + 22), 160);
  const grid = { gridTemplateColumns: `repeat(${columns}, minmax(150px, 1fr))`, columnGap: gap, rowGap: 20 };

  return (
    <section aria-label="서비스 구현 흐름">
      {/* Canvas; the padding also keeps the selected card's ring from being clipped by the scroll box. */}
      <div className="overflow-x-auto rounded-xl border border-line bg-[#fafaf7] p-6">
        <div ref={box} className="relative space-y-8" style={{ minWidth: columns * 150 + (columns - 1) * gap }}>
          <svg className="pointer-events-none absolute inset-0 z-0 size-full overflow-visible" aria-hidden>
            <defs>
              {["main", "sft"].map((id) => (
                <marker key={id} id={`arrow-${id}`} viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                  <path d="M0,0 L10,5 L0,10 z" fill={id === "sft" ? "#9b6a96" : "#7d8a80"} />
                </marker>
              ))}
            </defs>
            {lines.map((l) => (
              <path key={l.key} d={l.d} fill="none" stroke={l.sft ? "#9b6a96" : "#7d8a80"} strokeWidth={1.5}
                strokeDasharray={l.dashed ? "6 5" : undefined} markerEnd={`url(#arrow-${l.sft ? "sft" : "main"})`} />
            ))}
          </svg>
          {lines.filter((l) => l.label).map((l) => (
            <span key={l.key} className={`pointer-events-none absolute z-20 rounded bg-[#fafaf7] px-1 text-center text-xs leading-tight break-keep text-muted ${l.vertical ? "-translate-y-1/2" : "-translate-x-1/2 -translate-y-[calc(100%+4px)]"}`}
              style={{ left: l.x, top: l.y, width: "max-content", maxWidth: Math.max(40, l.room - 12) }}>
              {l.label}
            </span>
          ))}

          <div className="grid" style={grid}>
            {main.map((n) => <Card key={n.id} node={n} cardRef={register(n.id)} selectedId={selectedId} onSelect={onSelect} />)}
          </div>

          {track.length > 0 && (
            <div className="grid" style={grid}>
              {track.map((n) => <Card key={n.id} node={n} cardRef={register(n.id)} selectedId={selectedId} onSelect={onSelect} />)}
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

/** Shown whenever there are fine-tuning candidates, with or without a flow diagram. */
export function FineTuneTip({ candidates, fineTuning, onSelect }: { candidates: Candidate[]; fineTuning?: string; onSelect?: (id: string) => void }) {
  // Same set as the detail panel's SFT 출발점 후보: "both" models are SFT starting points too.
  const sft = candidates.filter((c) => c.type === "model" && (c.group === "sft" || c.group === "both"));
  if (sft.length === 0) return null;
  return (
    <p className="flex gap-2 rounded-xl border border-[#f0dfb5] bg-warn-soft px-4 py-3 text-sm leading-relaxed">
      <span aria-hidden>💡</span>
      <span>
        <b>이렇게 파인튜닝해 보세요</b> · {fineTuning || sft[0].role}
        <span className="mt-1 block text-xs text-muted">
          출발점 후보:{" "}
          {sft.map((m, i) => (
            <span key={m.id}>
              {i > 0 && ", "}
              <button className="font-bold text-brand hover:underline" onClick={() => onSelect?.(m.id)}>{m.name}</button>
            </span>
          ))}
        </span>
      </span>
    </p>
  );
}
