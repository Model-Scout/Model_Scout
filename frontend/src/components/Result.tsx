"use client";

import { useEffect, useRef, useState } from "react";
import type { SendOptions, Turn } from "@/components/App";
import { HistoryDrawer } from "@/components/Home";
import { Readme, type ReadmeTarget } from "@/components/Readme";
import { Composer, ReadOnlyNotice, TurnView } from "@/components/Thread";
import { Logo, Markdown, ORIGIN, StatusBadge } from "@/components/ui";
import type { Candidate, ChatResult, ImplementationGuide, Source } from "@/lib/api";

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

/** v5 B. 추천 결과 (대시보드): top picks | selected candidate + Model Scout 요약 | chat in a side panel. */
export function Result({ groupId, title, request, result, sources, turns, owner, onSend, onCancel, onReload, onHome, onOpenGroup }: Props) {
  const candidates = result.candidates;
  const models = candidates.filter((c) => c.type === "model");
  const datasets = candidates.filter((c) => c.type === "dataset");
  const [selectedId, setSelectedId] = useState(candidates[0]?.id);
  const [readme, setReadme] = useState<ReadmeTarget | null>(null);
  const [copied, setCopied] = useState(false);
  const [mode, setMode] = useState<SendOptions["mode"]>("question");
  const [askSelected, setAskSelected] = useState(true);
  const [chatOpen, setChatOpen] = useState(false);
  const [history, setHistory] = useState(false);
  const input = useRef<HTMLTextAreaElement>(null);

  // A new recommendation snapshot may not contain the old selection.
  const selected = candidates.find((c) => c.id === selectedId) ?? candidates[0];
  useEffect(() => {
    if (selected && selected.id !== selectedId) setSelectedId(selected.id);
  }, [selected, selectedId]);

  const last = turns.at(-1);
  const running = last?.running ?? false;
  // A clarify answer must go back as recommend.
  const effectiveMode = last?.type === "clarify" ? "recommend" : mode;

  const openSource: ReadmeOpen = (s) =>
    setReadme({ sourceId: s.source_id, kind: s.kind, title: s.title ?? s.source_id, url: s.url ?? null, quote: s.quote });

  async function share() {
    const ok = confirm("링크를 가진 사람은 누구나 이 대화의 모든 메시지와 추천 결과를 볼 수 있어요. 링크를 복사할까요?");
    if (!ok) return;
    await navigator.clipboard.writeText(`${location.origin}/result/${encodeURIComponent(groupId)}`);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  }

  function reanalyze() {
    setMode("recommend");
    setChatOpen(true);
    requestAnimationFrame(() => input.current?.focus());
  }

  const send = (q: string) =>
    onSend(q, {
      mode: effectiveMode,
      target: effectiveMode === "question" && askSelected && selected ? { id: selected.id, name: selected.name } : undefined,
    });

  return (
    <div className="flex min-h-dvh bg-page">
      <nav aria-label="메뉴" className="sticky top-0 hidden h-dvh w-[72px] shrink-0 flex-col items-center gap-3 border-r border-line bg-white py-6 sm:flex">
        <Logo size={32} />
        <button aria-label="홈으로" title="홈으로" className="mt-3 grid size-11 place-items-center rounded-xl text-brand hover:bg-brand-soft" onClick={onHome}>
          <HomeIcon />
        </button>
        <button aria-label="대화 기록" title="대화 기록" className="grid size-11 place-items-center rounded-xl text-muted hover:bg-brand-soft" onClick={() => setHistory(true)}>
          <ClockIcon />
        </button>
      </nav>

      <div className="flex min-w-0 flex-1 flex-col gap-4 p-4 lg:p-6">
        <header className="flex items-center gap-4">
          <button aria-label="홈으로" className="grid size-10 shrink-0 place-items-center rounded-full border border-line bg-white hover:border-brand/50" onClick={onHome}>
            ←
          </button>
          <div className="min-w-0 flex-1">
            <h1 className="truncate text-xl font-bold">{result.title || title}</h1>
            {request && <p className="truncate text-xs text-muted">“{request}”</p>}
          </div>
          <button className="shrink-0 rounded-full border border-line bg-white px-4 py-2 text-sm font-semibold" onClick={share}>
            {copied ? "복사됨" : "공유"}
          </button>
          {owner && (
            <button className="shrink-0 rounded-full bg-brand px-4 py-2 text-sm font-semibold text-white disabled:opacity-50" disabled={running} onClick={reanalyze}>
              다시 분석
            </button>
          )}
        </header>

        {candidates.length > 0 && <div className={`grid divide-y divide-line rounded-2xl bg-white lg:divide-x lg:divide-y-0 ${result.project && !result.project.search_targets.includes("model") ? "" : "lg:grid-cols-3"}`}>
          {(!result.project || result.project.search_targets.includes("model")) && <>
            <TopModel c={models[0]} onReadme={openSource} />
            <ModelList models={models} selectedId={selected?.id} onSelect={setSelectedId} />
          </>}
          <DataList datasets={datasets} all={candidates} selectedId={selected?.id} onSelect={setSelectedId} />
        </div>}

        <div className={candidates.length ? "grid flex-1 gap-4 lg:grid-cols-[minmax(0,1fr)_360px]" : "mx-auto w-full max-w-4xl"}>
          {candidates.length > 0 && <section className="min-w-0 rounded-2xl bg-white p-6 lg:p-8">
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
          </section>}
          <ScoutSummary result={result} />
        </div>
      </div>

      {!chatOpen && (
        <button
          className="fixed bottom-6 right-6 z-20 flex items-center gap-2 rounded-full bg-brand px-6 py-3.5 font-semibold text-white shadow-lg"
          onClick={() => setChatOpen(true)}
        >
          <Logo size={20} /> 대화 이어하기
          {running && <span className="size-2 animate-pulse rounded-full bg-white" aria-label="답변 중" />}
        </button>
      )}

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
              {owner && effectiveMode === "question" && selected && (
                <button
                  className={`truncate rounded-full px-2.5 py-0.5 text-xs ${askSelected ? "bg-brand-soft text-brand" : "bg-soft text-muted"}`}
                  onClick={() => setAskSelected((v) => !v)}
                  title="질문 대상을 바꾸려면 누르세요"
                >
                  질문 대상 · {askSelected ? selected.name : "추천 전체"}
                </button>
              )}
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

function TopModel({ c, onReadme }: { c?: Candidate; onReadme: ReadmeOpen }) {
  if (!c) return <div className="p-6 text-sm text-muted">추천 모델이 없어요.</div>;
  const t = tally(c);
  const pct = t.total ? (t.ok / t.total) * 100 : 0;
  return (
    <section className="p-6">
      <div className="flex items-center justify-between">
        <h2 className="font-bold">1순위 모델</h2>
        <span className="rounded-full bg-brand px-2 py-0.5 text-xs font-semibold text-white">★ 1순위</span>
      </div>
      <div className="mt-3 flex flex-wrap items-center gap-2">
        <span className="break-all text-3xl font-bold">{c.name}</span>
        {c.tags[0] && <span className="rounded-full bg-soft px-2.5 py-0.5 text-xs text-muted">{c.tags[0]}</span>}
      </div>
      <p className="mt-2 text-sm text-muted">{c.role}</p>
      <div className="mt-4 flex items-center gap-6">
        <div className="relative w-36 shrink-0">
          <svg viewBox="0 0 120 68" className="w-full" aria-hidden>
            <path d="M10 62 A50 50 0 0 1 110 62" fill="none" stroke="var(--color-soft)" strokeWidth="12" strokeLinecap="round" />
            <path
              d="M10 62 A50 50 0 0 1 110 62"
              fill="none"
              stroke="var(--color-brand)"
              strokeWidth="12"
              strokeLinecap="round"
              pathLength={100}
              strokeDasharray={`${pct} 100`}
            />
          </svg>
          <span className="absolute inset-x-0 bottom-0 text-center text-3xl font-bold">
            {t.ok}/{t.total}
          </span>
        </div>
        <dl className="space-y-1 text-sm">
          <dt className="text-xs text-muted">조건 충족</dt>
          {(
            [
              ["충족", t.ok, "bg-ok"],
              ["확인 필요", t.check, "bg-warn"],
              ["미확인", t.unknown, "bg-faint"],
            ] as const
          ).map(([label, n, dot]) => (
            <dd key={label} className="flex items-center gap-2">
              <span className={`size-2 rounded-full ${dot}`} aria-hidden />
              {label} <b>{n}</b>
            </dd>
          ))}
        </dl>
      </div>
      <div className="mt-5 flex flex-wrap gap-2">
        <button
          className="rounded-full bg-brand px-4 py-2 text-sm font-semibold text-white"
          onClick={() => onReadme({ source_id: c.source_id, kind: c.type, title: c.name, url: c.url })}
        >
          README 보기
        </button>
        {c.url && (
          <a className="rounded-full border border-line px-4 py-2 text-sm font-semibold hover:border-brand/50" href={c.url} target="_blank" rel="noopener noreferrer">
            {c.source}에서 열기 ↗
          </a>
        )}
      </div>
    </section>
  );
}

function ModelList({ models, selectedId, onSelect }: { models: Candidate[]; selectedId?: string; onSelect: (id: string) => void }) {
  return (
    <section className="p-6">
      <h2 className="flex items-center gap-2 font-bold">
        추천 모델 <span className="rounded-full bg-soft px-2 text-xs font-normal text-muted">{models.length}</span>
        <span className="text-xs font-normal text-faint">추천 순</span>
      </h2>
      {models.length === 0 && <p className="mt-3 text-sm text-muted">추천 모델이 없어요.</p>}
      <ul className="mt-3 max-h-64 space-y-1 overflow-y-auto">
        {models.map((c) => {
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
        })}
      </ul>
    </section>
  );
}

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
  return (
    <section className="p-6">
      <h2 className="flex items-center gap-2 font-bold">
        추천 데이터 <span className="rounded-full bg-soft px-2 text-xs font-normal text-muted">{datasets.length}</span>
        <span className="text-xs font-normal text-faint">연결 모델 표시</span>
      </h2>
      {datasets.length === 0 && <p className="mt-3 text-sm text-muted">추천 데이터가 없어요.</p>}
      <ul className="mt-3 max-h-64 divide-y divide-line overflow-y-auto">
        {datasets.map((d) => {
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

/** Model Scout 요약: built from the result the pipeline already returned, so it costs no extra LLM call. */
function ScoutSummary({ result }: { result: ChatResult }) {
  const [ask, ...chips] = result.summary;
  const sentences = result.combination ?? [];
  const noModelNeeded = result.project && !result.project.search_targets.includes("model");
  // Older results have no LLM sentences: fall back to the line-per-need template.
  const { lines, training, service } = combinations(result.candidates);
  const names = (ds: Candidate[]) =>
    ds.map((d, i) => (
      <span key={d.id}>
        {i > 0 && ", "}
        <b className="text-ok">{d.name}</b>
      </span>
    ));

  return (
    <aside className="space-y-5 rounded-2xl bg-white p-6 text-sm">
      <h2 className="flex items-center gap-2 text-lg font-bold">
        <PencilIcon /> Model Scout 요약
      </h2>

      <section>
        <h3 className="mb-1.5 text-xs text-muted">요구하신 것</h3>
        <p className="leading-relaxed">{ask}</p>
        {chips.length > 0 && (
          <div className="mt-2 flex flex-wrap gap-1.5">
            {chips.map((c) => (
              <span key={c} className="rounded-full bg-soft px-2.5 py-0.5 text-xs text-muted">
                {c}
              </span>
            ))}
          </div>
        )}
      </section>

      {result.project && (
        <section className="border-t border-line pt-4">
          <h3 className="mb-1.5 text-xs text-muted">이해한 프로젝트</h3>
          <p className="leading-relaxed">{result.project.definition}</p>
          {noModelNeeded && <p className="mt-2 leading-relaxed">현재 확인한 기능은 별도의 LLM·임베딩 모델 없이 구현할 수 있어요.</p>}
          {result.project.search_targets.length === 0 && <p className="mt-2 leading-relaxed">외부 데이터 검색 없이 서비스에서 직접 등록·저장하는 정보를 사용해요.</p>}
        </section>
      )}

      {result.answer ? (
        <section className="border-t border-line pt-4">
          <h3 className="mb-1.5 text-xs text-muted">{result.project ? "구현에 필요한 자원과 활용 방법" : "질문에 대한 답변"}</h3>
          <Markdown text={result.answer} />
        </section>
      ) : sentences.length > 0 ? (
        <section className="border-t border-line pt-4">
          <h3 className="mb-1.5 text-xs text-muted">이렇게 조합해 보세요</h3>
          <div className="space-y-2.5 leading-relaxed">
            {sentences.map((line, i) => (
              <p key={i}>
                <Highlighted text={line} candidates={result.candidates} />
              </p>
            ))}
          </div>
        </section>
      ) : (lines.length > 0 || training.length > 0 || service.length > 0) && (
        <section className="border-t border-line pt-4">
          <h3 className="mb-1.5 text-xs text-muted">이렇게 조합해 보세요</h3>
          <ul className="space-y-2.5 leading-relaxed">
            {lines.map(({ model, datasets }) => (
              <li key={model.id}>
                <b className="text-brand">{model.name}</b> — {model.role}
                {datasets.length > 0 && <> · 함께 쓸 데이터 {names(datasets)}</>}
              </li>
            ))}
            {training.length > 0 && <li>학습·평가 데이터: {names(training)}</li>}
            {service.length > 0 && <li>서비스에 붙일 데이터: {names(service)}</li>}
          </ul>
        </section>
      )}

      {result.needs_check.length > 0 && (
        <section className="border-t border-line pt-4">
          <h3 className="mb-1.5 text-xs text-muted">먼저 확인할 것</h3>
          <ul className="space-y-1 rounded-xl bg-warn-soft p-4 font-semibold text-warn">
            {result.needs_check.map((n) => (
              <li key={n}>{n}</li>
            ))}
          </ul>
        </section>
      )}
    </aside>
  );
}

/** Model names in brand color, dataset names in green; the sentence itself stays plain text. */
function Highlighted({ text, candidates }: { text: string; candidates: Candidate[] }) {
  const kind = new Map<string, Candidate["type"]>();
  for (const c of candidates) for (const n of [c.name, c.source_id]) if (n.length > 1) kind.set(n.toLowerCase(), c.type);
  if (kind.size === 0) return text;
  const names = [...kind.keys()].sort((a, b) => b.length - a.length).map((n) => n.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
  return text.split(new RegExp(`(${names.join("|")})`, "i")).map((part, i) => {
    const type = kind.get(part.toLowerCase());
    return type ? (
      <b key={i} className={type === "model" ? "text-brand" : "text-ok"}>
        {part}
      </b>
    ) : (
      part
    );
  });
}

function PencilIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 20 20" fill="none" stroke="var(--color-brand)" strokeWidth="1.6" strokeLinejoin="round" aria-hidden>
      <path d="M13.5 3.5l3 3L7 16H4v-3z" />
      <path d="M11.5 5.5l3 3" />
    </svg>
  );
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
  const cards: { label: string; value: string | null; unit?: string; note: string }[] = [
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
    <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => (
        <div key={card.label} className="rounded-xl bg-soft p-4">
          <div className="text-xs text-muted">{card.label}</div>
          {card.value ? (
            <div className="mt-1 break-all text-xl font-bold text-brand">{card.value}</div>
          ) : (
            <div className="mt-1 text-xl font-bold text-faint">미확인</div>
          )}
          {card.value && card.unit && <div className="text-xs text-muted">{card.unit}</div>}
          <div className="mt-1 text-[11px] text-faint">{card.note}</div>
        </div>
      ))}
    </div>
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
  const readme = (quote?: string | null) => onReadme({ source_id: c.source_id, kind: c.type, title: c.name, url: c.url, quote });

  return (
    <article className="space-y-8">
      <header className="space-y-4">
        <div className="flex flex-wrap items-center gap-3">
          <h2 className="break-all text-3xl font-bold">{c.name}</h2>
          <span className="rounded-full bg-brand px-2.5 py-0.5 text-xs font-semibold text-white">{c.type === "model" ? "모델" : "데이터셋"}</span>
          {c.tags.map((t) => (
            <span key={t} className="rounded-full bg-soft px-2.5 py-0.5 text-xs text-muted">
              {t}
            </span>
          ))}
        </div>
        <div className="flex flex-wrap items-center gap-2">
          <button className="rounded-full bg-brand px-5 py-2 text-sm font-semibold text-white" onClick={() => readme()}>
            README 보기
          </button>
          {c.url && (
            <>
              <a className="rounded-full border border-line px-5 py-2 text-sm font-semibold hover:border-brand/50" href={c.url} target="_blank" rel="noopener noreferrer">
                {c.source}에서 열기 ↗
              </a>
              <span className="truncate text-xs text-faint">{c.url.replace(/^https?:\/\//, "")}</span>
            </>
          )}
        </div>
        <p className="text-sm">
          <span className="font-semibold text-brand">이 아이디어에서의 역할</span> {c.role}
        </p>
      </header>

      <section>
        <h3 className="mb-2 flex flex-wrap items-baseline gap-2 text-lg font-bold">
          조건 확인 <span className="text-xs font-normal text-faint">밑줄 친 출처를 누르면 README의 해당 문장으로 이동해요</span>
        </h3>
        {c.checks.length === 0 ? (
          <p className="text-sm text-muted">판정할 조건이 없어요.</p>
        ) : (
          <ul className="text-sm">
            {c.checks.map((k) => (
              <li key={k.key} className="grid gap-2 border-b border-line py-4 sm:grid-cols-[140px_100px_minmax(0,1fr)]">
                <span className="font-semibold">{k.label}</span>
                <span>
                  <StatusBadge status={k.status} />
                </span>
                <div>
                  <p>{k.quote ? `“${k.quote}”` : k.reason}</p>
                  <p className="mt-0.5 text-xs text-faint">
                    {k.quote ? (
                      <button className="text-brand underline" onClick={() => readme(k.quote)}>
                        {ORIGIN[k.origin]} · 원문에서 보기 ↗
                      </button>
                    ) : (
                      ORIGIN[k.origin]
                    )}
                    {k.quote && <span className="ml-2">{k.reason}</span>}
                  </p>
                </div>
              </li>
            ))}
          </ul>
        )}
      </section>

      {c.type === "model" && <Metrics c={c} />}

      {c.type === "model" && implementationGuide && (
        <section>
          <h3 className="mb-2 font-bold">프로젝트 구현 가이드</h3>
          <dl className="space-y-3 rounded-xl bg-soft p-3 text-sm">
            {implementationGuide.structured_output && (
              <div>
                <dt className="font-semibold">구조화 출력</dt>
                <dd className="mt-1">{implementationGuide.structured_output}</dd>
              </div>
            )}
            {implementationGuide.fine_tuning && (
              <div>
                <dt className="font-semibold">추가 학습 검토</dt>
                <dd className="mt-1">{implementationGuide.fine_tuning}</dd>
              </div>
            )}
          </dl>
        </section>
      )}

      {c.type === "dataset" && (
        <section>
          <h3 className="mb-2 font-bold">추천 근거</h3>
          {c.evidence.length === 0 ? (
            <p className="text-sm text-muted">저장된 추천 근거가 없어요.</p>
          ) : (
            <ul className="space-y-2">
              {c.evidence.map((e, i) => (
                <li key={i} className="rounded-xl bg-soft p-3 text-sm">
                  <div className="font-semibold">{e.label}</div>
                  {e.text && <p className="mt-1">“{e.text}”</p>}
                  <p className="mt-1 text-xs text-faint">{ORIGIN[e.origin]}</p>
                </li>
              ))}
            </ul>
          )}
        </section>
      )}

      <section>
        <h3 className="mb-2 font-bold">출처 · 인용</h3>
        {sources.length === 0 ? (
          <p className="text-sm text-muted">이 후보에 저장된 인용이 없어요.</p>
        ) : (
          <ul className="space-y-2">
            {sources.map((s, i) => (
              <li key={i} className="rounded-xl border border-line p-3 text-sm">
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
      </section>

      {related.length > 0 && (
        <section>
          <h3 className="mb-2 font-bold">{c.type === "model" ? "연결 데이터셋 · 학습·평가에 쓸 수 있어요" : "연결 모델"}</h3>
          <div className="grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
            {related.map((r) => (
              <button key={r.id} className="rounded-xl bg-soft p-4 text-left hover:bg-brand-soft" onClick={() => onSelect(r.id)}>
                <div className="text-[11px] text-faint"># {r.source}</div>
                <div className="break-all font-semibold text-brand underline">{r.name}</div>
                <div className="mt-1 text-xs text-muted">{r.role}</div>
              </button>
            ))}
          </div>
        </section>
      )}
    </article>
  );
}
