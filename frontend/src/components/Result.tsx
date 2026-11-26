"use client";

import { useEffect, useRef, useState, type ReactNode } from "react";
import type { SendOptions, Turn } from "@/components/App";
import { HistoryDrawer } from "@/components/Home";
import { FineTuneTip, PipelineDiagram } from "@/components/PipelineDiagram";
import { Readme, type ReadmeTarget } from "@/components/Readme";
import { Composer, ReadOnlyNotice, TurnView } from "@/components/Thread";
import { Logo, ORIGIN, StatusBadge } from "@/components/ui";
import { looseMentions } from "@/lib/looseNames";
import type { Candidate, ChatResult, ImplementationGuide, Source } from "@/lib/api";
import { combinations, fallbackPipeline } from "@/lib/flow";

type Props = {
  groupId: string;
  title: string;
  request: string;
  result: ChatResult;
  sources: Source[];
  turns: Turn[];
  owner: boolean;
  onSend: (q: string, o: SendOptions) => void;
  onCancel: () => void;
  onReload?: () => void;
  onHome: () => void;
  onOpenGroup: (id: string) => void;
};

type ReadmeOpen = (s: { source_id: string; kind: "model" | "dataset"; title?: string | null; url?: string | null; quote?: string | null }) => void;

/** 추천 결과: 후보 목록, 서비스 기획과 선택한 후보 상세, 후속 대화. */
export function Result({ title, request, result, sources, turns, owner, onSend, onCancel, onReload, onHome, onOpenGroup }: Props) {
  const candidates = result.candidates;
  const models = candidates.filter((c) => c.type === "model" && c.group !== "sft");
  // Model-linked data ("모델 학습·평가") shows only in a model's detail, not in the 데이터 후보 tab.
  const datasets = candidates.filter((c) => c.type === "dataset" && projectRoles(c).length > 0);
  const [selectedId, setSelectedId] = useState(candidates[0]?.id);
  const [readme, setReadme] = useState<ReadmeTarget | null>(null);
  const [mode, setMode] = useState<SendOptions["mode"]>("question");
  const [chatOpen, setChatOpen] = useState(false);
  const [history, setHistory] = useState(false);
  const input = useRef<HTMLTextAreaElement>(null);
  const panel = useRef<HTMLElement>(null);

  // A new recommendation snapshot may not contain the old selection.
  const selected = candidates.find((c) => c.id === selectedId) ?? candidates[0];
  useEffect(() => {
    if (selected && selected.id !== selectedId) setSelectedId(selected.id);
  }, [selected, selectedId]);
  // The sticky detail panel scrolls on its own: start each newly picked candidate at its top.
  useEffect(() => {
    // Braces matter: Chrome's scrollTo returns a Promise, which React rejects as an effect cleanup.
    panel.current?.scrollTo({ top: 0 });
  }, [selected?.id]);

  const last = turns.at(-1);
  const running = last?.running ?? false;
  // A clarify answer must go back as recommend.
  const effectiveMode = last?.type === "clarify" ? "recommend" : mode;

  const openSource: ReadmeOpen = (s) =>
    setReadme({ sourceId: s.source_id, kind: s.kind, title: s.title ?? s.source_id, url: s.url ?? null, quote: s.quote });

  const send = (q: string) =>
    onSend(q, {
      mode: effectiveMode,
      target: effectiveMode === "question" && selected ? { id: selected.id, name: selected.name } : undefined,
    });

  return (
    <div className="flex min-h-dvh bg-page">
      <nav aria-label="메뉴" className="sticky top-0 hidden h-dvh w-[72px] shrink-0 flex-col items-center gap-3 border-r border-line bg-white py-6 sm:flex">
        <button aria-label="홈으로" title="홈으로" className="mb-3 rounded-xl" onClick={onHome}>
          <Logo size={32} />
        </button>
        <button aria-label="홈으로" title="홈으로" className="grid size-11 place-items-center rounded-xl text-brand hover:bg-brand-soft" onClick={onHome}>
          <HomeIcon />
        </button>
        <button aria-label="대화 기록" title="대화 기록" className="grid size-11 place-items-center rounded-xl text-muted hover:bg-brand-soft" onClick={() => setHistory(true)}>
          <ClockIcon />
        </button>
      </nav>

      <div className="flex min-w-0 flex-1 flex-col gap-6 p-4 lg:p-8">
        <header className="flex items-center gap-3">
          <button aria-label="홈으로" className="grid size-9 shrink-0 place-items-center rounded-full border border-line bg-white hover:border-brand/50" onClick={onHome}>
            ←
          </button>
          <p className="min-w-0 flex-1 truncate text-sm text-muted">
            <span className="font-semibold text-brand">추천 결과</span>
            {request && <span> / “{request.replace(/\n조건: [^\n]*\.$/, "")}”</span>}
          </p>
        </header>

        <h1 className="border-b border-line pb-6 text-3xl font-bold tracking-tight lg:text-4xl">{result.title || title}</h1>

        <div className="grid flex-1 items-start gap-8 lg:grid-cols-[minmax(0,2fr)_minmax(0,1fr)]">
          <ScoutSummary result={result} models={models} datasets={datasets} selectedId={selected?.id} onSelect={setSelectedId} />
          <section ref={panel} aria-label="선택한 후보 상세" className="@container min-w-0 rounded-2xl bg-white p-5 lg:sticky lg:top-6 lg:max-h-[calc(100dvh-3rem)] lg:overflow-y-auto lg:p-6">
            {selected ? (
              <Detail
                candidate={selected}
                all={candidates}
                implementationGuide={result.assessment?.implementation_guide}
                sources={sources.filter((s) => s.source_id === selected.source_id && s.kind === selected.type)}
                onSelect={setSelectedId}
                onReadme={openSource}
              />
            ) : (
              <div className="grid h-full place-items-center py-16 text-center text-muted">
                <div>
                  <p className="text-lg font-semibold text-ink">조건에 맞는 후보가 없어요</p>
                  <p className="mt-2 text-sm">‘대화 이어하기’에서 조건을 바꿔 다시 추천을 받아 보세요.</p>
                </div>
              </div>
            )}
          </section>
        </div>
      </div>

      {!chatOpen && (
        <button
          aria-label="대화 이어하기"
          className="fixed bottom-6 right-6 z-20 rounded-2xl rounded-br-sm bg-brand px-4 py-3 text-sm font-semibold text-white opacity-60 shadow-lg transition hover:-translate-y-0.5 hover:opacity-100 hover:shadow-xl focus-visible:opacity-100"
          onClick={() => setChatOpen(true)}
        >
          대화를 이어가 보세요!
          {running && <span className="absolute -right-1 -top-1 size-3 animate-pulse rounded-full bg-white ring-2 ring-brand" aria-label="답변 중" />}
        </button>
      )}
      {chatOpen && <div aria-hidden className="fixed inset-0 z-30" onClick={() => setChatOpen(false)} />}
      {chatOpen && (
        <aside
          aria-label="추천에 대해 묻기"
          className="fixed inset-y-0 right-0 z-30 flex w-full flex-col border-l border-line bg-white shadow-2xl sm:w-[420px]"
          onKeyDown={(e) => e.key === "Escape" && setChatOpen(false)}
        >
          <div className="flex items-center justify-between gap-2 border-b border-line px-4 py-3">
            <h2 className="flex items-center gap-2 font-bold">
              <Logo size={22} /> 추천에 대해 묻기
            </h2>
            <div className="flex min-w-0 items-center gap-2">
              <button aria-label="대화 닫기" className="rounded-lg px-2 py-1 text-lg text-muted hover:bg-soft" onClick={() => setChatOpen(false)}>
                ×
              </button>
            </div>
          </div>
          <div className="flex-1 space-y-3 overflow-y-auto p-4">
            {turns.map((t, i) => (
              <TurnView key={i} turn={t} compact onCancel={onCancel} onReload={onReload} onSource={openSource} />
            ))}
          </div>
          <div className="space-y-2 border-t border-line p-3">
            {owner ? (
              <>
                {last?.type !== "clarify" && (
                  <div className="flex gap-1 text-xs" role="radiogroup" aria-label="요청 종류">
                    {(
                      [
                        ["question", "결과에 질문"],
                        ["recommend", "조건 바꿔 다시 추천"],
                      ] as const
                    ).map(([value, label]) => (
                      <button
                        key={value}
                        role="radio"
                        aria-checked={mode === value}
                        className={`rounded-full px-3 py-1 ${mode === value ? "bg-ink text-white" : "bg-soft text-muted"}`}
                        onClick={() => setMode(value)}
                      >
                        {label}
                      </button>
                    ))}
                  </div>
                )}
                <Composer
                  ref={input}
                  disabled={running}
                  onSubmit={send}
                  placeholder={
                    last?.type === "clarify"
                      ? "질문에 답해 주세요"
                      : mode === "question"
                        ? "이 추천에 대해 질문하기"
                        : "바꿀 조건을 적어 주세요 (예: 상업 이용 가능한 모델만)"
                  }
                />
              </>
            ) : (
              <ReadOnlyNotice onHome={onHome} />
            )}
          </div>
        </aside>
      )}

      {history && (
        <div className="fixed inset-0 z-40 flex bg-ink/20" onClick={() => setHistory(false)}>
          <div onClick={(e) => e.stopPropagation()}>
            <HistoryDrawer
              onClose={() => setHistory(false)}
              onNew={onHome}
              onOpen={(id) => {
                setHistory(false);
                onOpenGroup(id);
              }}
            />
          </div>
        </div>
      )}

      {readme && <Readme target={readme} onClose={() => setReadme(null)} />}
    </div>
  );
}

function tally(c: Candidate) {
  const n = (s: string) => c.checks.filter((k) => k.status === s).length;
  return { ok: n("ok"), check: n("check"), unknown: n("unknown"), total: c.checks.length };
}

/** Category chips (전체 + one per category, with counts) over a list; hidden when there is only one category. */
function useCategories(items: Candidate[], categoryOf: (c: Candidate) => string | undefined, label: string) {
  const [picked, setPicked] = useState<string | null>(null);
  const counts = new Map<string, number>();
  for (const c of items) {
    const k = categoryOf(c);
    if (k) counts.set(k, (counts.get(k) ?? 0) + 1);
  }
  // A new result may not contain the picked category: fall back to 전체.
  const active = picked && counts.has(picked) ? picked : null;
  const shown = active ? items.filter((c) => categoryOf(c) === active) : items;
  const chips = counts.size > 1 && (
    <div className="mt-3 flex flex-wrap gap-1 text-xs" role="radiogroup" aria-label={label}>
      {[[null, "전체", items.length] as const, ...[...counts].map(([k, n]) => [k, k, n] as const)].map(([value, text, n]) => (
        <button
          key={text}
          role="radio"
          aria-checked={active === value}
          className={`rounded-full px-3 py-1 ${active === value ? "bg-ink text-white" : "bg-soft text-muted"}`}
          onClick={() => setPicked(value)}
        >
          {text} {n}
        </button>
      ))}
    </div>
  );
  return { shown, chips };
}

function ModelList({ models, selectedId, onSelect }: { models: Candidate[]; selectedId?: string; onSelect: (id: string) => void }) {
  // tags[0] is the need's task (embedding, generation, ...; retrieval is folded into embedding), set by the backend.
  const { shown, chips } = useCategories(models, (c) => c.tags[0], "태스크별 보기");
  const row = (c: Candidate) => {
    const t = tally(c);
    return (
      <li key={c.id}>
        <button
          aria-current={c.id === selectedId}
          className={`flex w-full items-center gap-3 rounded-xl px-3 py-3 text-left ${c.id === selectedId ? "bg-brand-soft" : "hover:bg-soft"}`}
          onClick={() => onSelect(c.id)}
        >
          <span className="grid size-7 shrink-0 place-items-center rounded-lg bg-white text-brand ring-1 ring-line" aria-hidden>
            ⬡
          </span>
          <span className="min-w-0 flex-1 truncate font-semibold">{c.name}</span>
          {c.tags[0] && <span className="hidden shrink-0 rounded-full bg-soft px-2 py-0.5 text-[11px] text-muted xl:inline">{c.tags[0]}</span>}
          <span className="h-1.5 w-14 shrink-0 overflow-hidden rounded-full bg-soft" aria-hidden>
            <span className="block h-full rounded-full bg-brand" style={{ width: `${t.total ? (t.ok / t.total) * 100 : 0}%` }} />
          </span>
          <span className="w-8 shrink-0 text-right text-xs text-muted">
            {t.ok}/{t.total}
          </span>
        </button>
      </li>
    );
  };
  return (
    <section className="p-6">
      <h2 className="flex items-center gap-2 font-bold">
        추천 모델 <span className="rounded-full bg-soft px-2 text-xs font-normal text-muted">{models.length}</span>
        <span className="text-xs font-normal text-faint">추천 순</span>
      </h2>
      {models.length === 0 && <p className="mt-3 text-sm text-muted">추천 모델이 없어요.</p>}
      {chips}
      <ul className="mt-3 max-h-64 space-y-1 overflow-y-auto">{shown.map(row)}</ul>
    </section>
  );
}

// role is "모델 학습·평가" / "프로젝트 학습·평가" / "서비스 데이터", joined with " / " when a dataset has several.
const projectRoles = (d: Candidate) => d.role.split(" / ").filter((r) => r !== "모델 학습·평가");

function DataList({
  datasets,
  all,
  selectedId,
  onSelect,
}: {
  datasets: Candidate[];
  all: Candidate[];
  selectedId?: string;
  onSelect: (id: string) => void;
}) {
  const { shown, chips } = useCategories(datasets, (d) => projectRoles(d)[0], "용도별 보기");
  return (
    <section className="p-6">
      <h2 className="flex items-center gap-2 font-bold">
        추천 데이터 <span className="rounded-full bg-soft px-2 text-xs font-normal text-muted">{datasets.length}</span>
        <span className="text-xs font-normal text-faint">연결 모델 표시</span>
      </h2>
      {datasets.length === 0 && <p className="mt-3 text-sm text-muted">추천 데이터가 없어요.</p>}
      {chips}
      <ul className="mt-3 max-h-64 divide-y divide-line overflow-y-auto">
        {shown.map((d) => {
          const model = all.find((m) => m.type === "model" && d.related.includes(m.id));
          return (
            <li key={d.id} className={`flex items-start gap-3 px-1 py-3 ${d.id === selectedId ? "bg-ok-soft/50" : ""}`}>
              <span className="grid size-8 shrink-0 place-items-center rounded-lg bg-ok-soft text-ok" aria-hidden>
                ▤
              </span>
              <div className="min-w-0 flex-1">
                <button aria-current={d.id === selectedId} className="block max-w-full truncate text-left text-sm font-semibold hover:underline" onClick={() => onSelect(d.id)}>
                  {d.name}
                </button>
                {d.url ? (
                  <a className="text-xs text-ok hover:underline" href={d.url} target="_blank" rel="noopener noreferrer">
                    {d.source} ↗
                  </a>
                ) : (
                  <span className="text-xs text-muted">{d.source}</span>
                )}
              </div>
              <div className="shrink-0 space-y-1 text-right text-xs text-muted">
                {model ? <div>→ {model.name}</div> : <div className="text-faint">{d.role}</div>}
                {d.checks.some((k) => k.status === "unknown") && <StatusBadge status="unknown" />}
              </div>
            </li>
          );
        })}
      </ul>
    </section>
  );
}

/** Left column: the service flow, why it is combined that way, then every other candidate. Built from the result, no extra LLM call. */
function ScoutSummary({ result, models, datasets, selectedId, onSelect }:
  { result: ChatResult; models: Candidate[]; datasets: Candidate[]; selectedId?: string; onSelect: (id: string) => void }) {
  const sentences = result.combination ?? [];
  // Older results have no LLM sentences: fall back to the line-per-need template.
  const { lines, training, service } = combinations(result.candidates);
  const names = (ds: Candidate[]) =>
    ds.map((d, i) => (
      <span key={d.id}>
        {i > 0 && ", "}
        <span className={MARK.dataset}>{d.name}</span>
      </span>
    ));
  const reasons = sentences.length > 0
    ? sentences.map((line, i) => <Highlighted key={i} text={line} candidates={result.candidates} />)
    : [
        ...lines.map(({ model, datasets }) => (
          <span key={model.id}>
            <span className={MARK.model}>{model.name}</span> — {model.role}
            {datasets.length > 0 && <> · 함께 쓸 데이터 {names(datasets)}</>}
          </span>
        )),
        ...(training.length > 0 ? [<span key="training">학습·평가 데이터: {names(training)}</span>] : []),
        ...(service.length > 0 ? [<span key="service">서비스에 붙일 데이터: {names(service)}</span>] : []),
      ];
  const tip = <FineTuneTip candidates={result.candidates} fineTuning={result.assessment?.implementation_guide?.fine_tuning} onSelect={onSelect} />;
  const others = <OtherCandidates models={models} datasets={datasets} all={result.candidates} selectedId={selectedId} onSelect={onSelect} />;

  const pipeline = result.pipeline ?? fallbackPipeline(result.candidates);
  // The backend names what the user's conditions removed (result.py excluded_models); without it a filter is invisible.
  const excluded = result.summary.find((line) => line.startsWith("후보에서 뺀 모델:"));

  return (
    <div className="min-w-0 space-y-12">
      {excluded && <p className="rounded-xl bg-soft px-4 py-3 text-sm text-muted">{excluded}</p>}
      {pipeline ? (
        <section className="space-y-4">
          <Heading title="서비스 구현 흐름"
            sub={result.pipeline ? "카드를 누르면 오른쪽에서 자세히 볼 수 있어요." : "추천 후보로 구성한 기본 흐름이에요. 카드를 누르면 오른쪽에서 자세히 볼 수 있어요."} />
          <PipelineDiagram pipeline={pipeline} candidates={result.candidates} selectedId={selectedId} onSelect={onSelect} />
          {tip}
        </section>
      ) : (
        <>
          {tip}
          {others}
        </>
      )}

      {reasons.length > 0 && (
        <section className="space-y-4">
          <Heading title="이렇게 조합해 보세요" />
          <div className="space-y-3 text-[15px] leading-relaxed">
            {reasons.map((r, i) => (
              <p key={i}>{r}</p>
            ))}
          </div>
        </section>
      )}

      {pipeline && others}
    </div>
  );
}

function Heading({ title, sub }: { title: string; sub?: string }) {
  return (
    <div>
      <h2 className="text-xl font-bold">{title}</h2>
      {sub && <p className="mt-1 text-sm text-muted">{sub}</p>}
    </div>
  );
}

function OtherCandidates({ models, datasets, all, selectedId, onSelect }:
  { models: Candidate[]; datasets: Candidate[]; all: Candidate[]; selectedId?: string; onSelect: (id: string) => void }) {
  return (
    <section className="space-y-4">
      <Heading title="다른 후보 살펴보기" sub="추천 순서대로 모았어요. 누르면 오른쪽에서 자세히 볼 수 있어요." />
      <div className="grid divide-y divide-line rounded-2xl border border-line bg-white md:grid-cols-2 md:divide-x md:divide-y-0">
        <ModelList models={models} selectedId={selectedId} onSelect={onSelect} />
        <DataList datasets={datasets} all={all} selectedId={selectedId} onSelect={onSelect} />
      </div>
    </section>
  );
}

/** Model names in brand color, dataset names in green; the sentence itself stays plain text. */
// Model names purple, dataset names green: color only, no highlight.
const MARK = {
  model: "font-semibold text-brand",
  dataset: "font-semibold text-ok",
};

function Highlighted({ text, candidates }: { text: string; candidates: Candidate[] }) {
  const kind = new Map<string, Candidate["type"]>();
  for (const c of candidates) for (const n of [c.name, c.source_id, c.source_id.split("/").pop() ?? ""]) if (n.length > 1) kind.set(n.toLowerCase(), c.type);
  // The writer sometimes names a model by its organization alone ("junmo-k 모델"): still a model mention.
  for (const c of candidates) {
    const org = c.type === "model" && c.source_id.includes("/") ? c.source_id.split("/")[0].toLowerCase() : "";
    if (org.length > 2 && !kind.has(org)) kind.set(org, "model");
  }
  if (kind.size === 0) return text;
  const names = [...kind.keys()].sort((a, b) => b.length - a.length).map((n) => n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
  const titles = candidates.filter((c) => c.type === "dataset").map((c) => c.name);
  return text.split(new RegExp(`(${names.join("|")})`, "i")).map((part, i) => {
    const type = kind.get(part.toLowerCase());
    if (type) return <span key={i} className={MARK[type]}>{part}</span>;
    // Not an exact name: a paraphrased dataset title still shows green.
    const pieces = [];
    let at = 0;
    for (const [start, end] of looseMentions(part, titles)) {
      pieces.push(part.slice(at, start), <span key={`${i}-${start}`} className={MARK.dataset}>{part.slice(start, end)}</span>);
      at = end;
    }
    pieces.push(part.slice(at));
    return <span key={i}>{pieces}</span>;
  });
}

function HomeIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinejoin="round" aria-hidden>
      <path d="M3 9l7-6 7 6v8H12v-5H8v5H3z" />
    </svg>
  );
}

function ClockIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" aria-hidden>
      <circle cx="10" cy="10" r="7.5" />
      <path d="M10 6v4l2.5 2" />
    </svg>
  );
}

const fmt = (n: number) => n.toLocaleString("ko-KR");

function str(v: unknown): string | null {
  return typeof v === "string" && v ? v : typeof v === "number" ? fmt(v) : null;
}

function Metrics({ c }: { c: Candidate }) {
  // verdict "unknown" carries only a "미확인" label, not a value.
  const gpu = c.gpu_fit && c.gpu_fit.verdict !== "unknown" ? c.gpu_fit : null;
  const bench = c.benchmarks.find((b) => typeof b.score === "number");
  const rows: { label: string; value: string | null; unit?: string; note: string }[] = [
    { label: "최대 입력 길이", value: c.context_length ? fmt(c.context_length) : null, unit: "tokens", note: "메타데이터" },
    { label: "파라미터", value: c.parameters_b ? fmt(c.parameters_b) : null, unit: "B", note: "메타데이터" },
    {
      label: "예상 GPU 메모리",
      value: typeof gpu?.needed_gib === "number" ? `≈${fmt(Math.round(gpu.needed_gib * 10) / 10)}` : str(gpu?.label),
      unit: typeof gpu?.needed_gib === "number" ? `GiB${gpu?.precision ? ` · ${gpu.precision}` : ""}` : undefined,
      note: "추정 · 실기기 검증 아님",
    },
    {
      label: "벤치마크",
      value: bench ? fmt(bench.score as number) : null,
      unit: bench ? [str(bench.benchmark) ?? str(bench.dataset), str(bench.metric)].filter(Boolean).join(" · ") : undefined,
      note: "모델마다 벤치마크가 달라 직접 비교 불가",
    },
  ];
  return (
    <DetailSection title="주요 수치">
      <Rows
        rows={rows.map((r) => [
          r.label,
          <>
            {r.value ? (
              <b className="break-all">
                {r.value}
                {r.unit && <span className="ml-1 font-normal text-muted">{r.unit}</span>}
              </b>
            ) : (
              <span className="text-faint">미확인</span>
            )}
            <span className="mt-0.5 block text-xs text-faint">{r.note}</span>
          </>,
        ])}
      />
    </DetailSection>
  );
}

function DetailSection({ title, hint, children }: { title: string; hint?: string; children: ReactNode }) {
  return (
    <section>
      <h3 className="mb-1 text-base font-bold">{title}</h3>
      {hint && <p className="mb-1 text-xs text-faint">{hint}</p>}
      {children}
    </section>
  );
}

/** Label on the left, value on the right, a rule between rows. */
function Rows({ rows }: { rows: [ReactNode, ReactNode][] }) {
  return (
    <dl className="divide-y divide-line border-b border-line text-sm">
      {rows.map(([label, value], i) => (
        <div key={i} className="grid grid-cols-[6.5rem_minmax(0,1fr)] gap-3 py-3">
          <dt className="text-muted">{label}</dt>
          <dd className="min-w-0 [overflow-wrap:anywhere]">{value}</dd>
        </div>
      ))}
    </dl>
  );
}

function Detail({
  candidate: c,
  all,
  implementationGuide,
  sources,
  onSelect,
  onReadme,
}: {
  candidate: Candidate;
  all: Candidate[];
  implementationGuide?: ImplementationGuide;
  sources: Source[];
  onSelect: (id: string) => void;
  onReadme: ReadmeOpen;
}) {
  const related = c.related.map((id) => all.find((x) => x.id === id)).filter((x): x is Candidate => Boolean(x));
  const sft = all.filter((x) => x.type === "model" && (x.group === "sft" || x.group === "both"));
  const readme = (quote?: string | null) => onReadme({ source_id: c.source_id, kind: c.type, title: c.name, url: c.url, quote });
  const isData = c.type === "dataset";
  const accent = isData ? "text-ok" : "text-brand";
  const guide: [ReactNode, ReactNode][] = [];
  if (implementationGuide?.structured_output) guide.push(["구조화 출력", implementationGuide.structured_output]);
  if (implementationGuide?.fine_tuning || sft.length > 0)
    guide.push([
      "추가 학습 검토",
      <>
        {implementationGuide?.fine_tuning}
        {sft.length > 0 && (
          <span className="mt-2 flex flex-wrap gap-1.5">
            {sft.map((m) => (
              <button
                key={m.id}
                aria-current={m.id === c.id}
                className={`rounded-md border px-2.5 py-1 text-xs font-semibold ${m.id === c.id ? "border-brand bg-brand-soft text-brand" : "border-line bg-white hover:border-brand/50"}`}
                onClick={() => onSelect(m.id)}
              >
                {m.name}
              </button>
            ))}
          </span>
        )}
      </>,
    ]);

  return (
    <article className="space-y-8">
      <header className="space-y-3">
        <p className={`text-sm font-semibold ${accent}`}>{isData ? "데이터" : c.group === "sft" ? "파인튜닝 모델" : "모델"}</p>
        <h2 className="[overflow-wrap:anywhere] text-2xl font-bold leading-snug">{c.name}</h2>
        <p className="text-sm text-muted">{[c.source, ...c.tags].filter(Boolean).join(" · ")}</p>
        <div className="flex flex-wrap gap-2 pt-1">
          <button className="rounded-lg bg-ink px-4 py-2 text-sm font-semibold text-white" onClick={() => readme()}>
            README 보기
          </button>
          {c.url && (
            <a className="rounded-lg border border-line bg-white px-4 py-2 text-sm font-semibold hover:border-ink/40" href={c.url} target="_blank" rel="noopener noreferrer">
              {c.source}에서 열기 ↗
            </a>
          )}
        </div>
      </header>

      <div className={`rounded-xl px-5 py-4 text-sm leading-relaxed ${isData ? "bg-ok-soft" : "bg-brand-soft"}`}>
        <p className={`mb-1 font-semibold ${accent}`}>{c.group === "sft" ? "SFT 검토 이유" : "이 아이디어에서의 역할"}</p>
        <p>{c.role}</p>
      </div>

      {isData && c.evidence.length > 0 && (
        <DetailSection title="추천 근거">
          <Rows
            rows={c.evidence.map((e) => [
              e.label,
              <>
                {e.text ? `“${e.text}”` : <span className="text-faint">내용 없음</span>}
                <span className="mt-0.5 block text-xs text-faint">{ORIGIN[e.origin]}</span>
              </>,
            ])}
          />
        </DetailSection>
      )}

      <DetailSection title="조건 확인" hint="출처를 누르면 README의 해당 문장으로 이동해요">
        {c.checks.length === 0 ? (
          <p className="py-3 text-sm text-muted">판정할 조건이 없어요.</p>
        ) : (
          <ul className="divide-y divide-line border-b border-line text-sm">
            {c.checks.map((k) => (
              <li key={k.key} className="space-y-1 py-3">
                <div className="flex items-center justify-between gap-2">
                  <span className="font-semibold">{k.label}</span>
                  <StatusBadge status={k.status} />
                </div>
                <p className="[overflow-wrap:anywhere] text-muted">{k.quote ? `“${k.quote}”` : k.reason}</p>
                <p className="text-xs text-faint">
                  {k.quote ? (
                    <button className="text-brand underline" onClick={() => readme(k.quote)}>
                      {ORIGIN[k.origin]} · 원문에서 보기 ↗
                    </button>
                  ) : (
                    ORIGIN[k.origin]
                  )}
                  {k.quote && <span className="ml-2">{k.reason}</span>}
                </p>
              </li>
            ))}
          </ul>
        )}
      </DetailSection>

      {c.type === "model" && <Metrics c={c} />}

      {c.type === "model" && guide.length > 0 && (
        <DetailSection title="프로젝트 구현 가이드">
          <Rows rows={guide} />
        </DetailSection>
      )}

      {related.length > 0 && (
        <DetailSection title={c.type === "model" ? "연결 데이터셋" : "연결 모델"} hint={c.type === "model" ? "학습·평가에 쓸 수 있어요" : undefined}>
          <ul className="divide-y divide-line border-b border-line text-sm">
            {related.map((r) => (
              <li key={r.id}>
                <button className="w-full py-3 text-left hover:bg-soft" onClick={() => onSelect(r.id)}>
                  <span className={`block break-all font-semibold ${r.type === "dataset" ? "text-ok" : "text-brand"}`}>{r.name}</span>
                  <span className="block text-xs text-muted">
                    {r.source} · {r.role}
                  </span>
                </button>
              </li>
            ))}
          </ul>
        </DetailSection>
      )}

      <DetailSection title="원문 출처">
        {sources.length === 0 ? (
          <p className="py-3 text-sm text-muted">이 후보에 저장된 인용이 없어요.</p>
        ) : (
          <ul className="divide-y divide-line border-b border-line text-sm">
            {sources.map((s, i) => (
              <li key={i} className="py-3">
                {s.quote ? <p>“{s.quote}”</p> : <p className="text-muted">인용문 없음</p>}
                <p className="mt-1 text-xs text-faint">
                  {s.title ?? s.source_id} · {ORIGIN[s.origin]}
                  <button className="ml-2 text-brand underline" onClick={() => onReadme(s)}>
                    원문에서 보기
                  </button>
                </p>
              </li>
            ))}
          </ul>
        )}
      </DetailSection>
    </article>
  );
}
