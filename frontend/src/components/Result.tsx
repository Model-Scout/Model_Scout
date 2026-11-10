"use client";

import { useEffect, useRef, useState } from "react";
import type { SendOptions, Turn } from "@/components/App";
import { Readme, type ReadmeTarget } from "@/components/Readme";
import { Composer, ReadOnlyNotice, TurnView } from "@/components/Thread";
import { Logo, ORIGIN, StatusBadge } from "@/components/ui";
import type { Candidate, ChatResult, Source } from "@/lib/api";

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
};

type Filter = "all" | "model" | "dataset";

/** B. 추천 결과: requirements + candidates | candidate detail | follow-up questions. */
export function Result({ groupId, title, request, result, sources, turns, owner, onSend, onCancel, onReload, onHome }: Props) {
  const candidates = result.candidates;
  const [selectedId, setSelectedId] = useState(candidates[0]?.id);
  const [filter, setFilter] = useState<Filter>("all");
  const [readme, setReadme] = useState<ReadmeTarget | null>(null);
  const [copied, setCopied] = useState(false);
  const [mode, setMode] = useState<SendOptions["mode"]>("question");
  const [askSelected, setAskSelected] = useState(true);
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

  const openSource = (s: { source_id: string; kind: "model" | "dataset"; title?: string | null; url?: string | null; quote?: string | null }) =>
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
    input.current?.focus();
  }

  const send = (q: string) =>
    onSend(q, {
      mode: effectiveMode,
      target: effectiveMode === "question" && askSelected && selected ? { id: selected.id, name: selected.name } : undefined,
    });

  return (
    <div className="flex h-dvh flex-col bg-[#f6f6f9]">
      <header className="flex items-center gap-4 border-b border-line bg-white px-5 py-3">
        <button className="shrink-0 rounded-full bg-brand-soft px-3 py-1.5 text-sm font-semibold text-brand" onClick={onHome}>
          홈으로
        </button>
        <Logo size={30} />
        <div className="min-w-0 flex-1">
          <h1 className="truncate text-lg font-bold">{result.title || title}</h1>
          {request && <p className="truncate text-xs text-muted">“{request}”</p>}
        </div>
        <button className="shrink-0 rounded-full border border-line px-3 py-1.5 text-sm" onClick={share}>
          {copied ? "복사됨" : "공유"}
        </button>
        {owner && (
          <button className="shrink-0 rounded-full bg-brand px-3 py-1.5 text-sm text-white disabled:opacity-50" disabled={running} onClick={reanalyze}>
            다시 분석
          </button>
        )}
      </header>

      <div className="grid min-h-0 flex-1 gap-4 overflow-y-auto p-4 lg:grid-cols-[300px_minmax(0,1fr)_340px] lg:overflow-hidden">
        <CandidateList
          result={result}
          filter={filter}
          onFilter={setFilter}
          selectedId={selected?.id}
          onSelect={setSelectedId}
        />

        <section className="min-h-0 overflow-y-auto rounded-2xl border border-line bg-white p-6 lg:p-8">
          {selected ? (
            <Detail
              candidate={selected}
              all={candidates}
              sources={sources.filter((s) => s.source_id === selected.source_id && s.kind === selected.type)}
              onSelect={setSelectedId}
              onReadme={openSource}
            />
          ) : (
            <div className="grid h-full place-items-center text-center text-muted">
              <div>
                <p className="text-lg font-semibold text-ink">조건에 맞는 후보가 없어요</p>
                <p className="mt-2 text-sm">오른쪽에서 조건을 바꿔 다시 추천을 받아 보세요.</p>
              </div>
            </div>
          )}
        </section>

        <aside className="flex min-h-[480px] flex-col rounded-2xl border border-line bg-white lg:min-h-0">
          <div className="flex items-center justify-between gap-2 border-b border-line px-4 py-3">
            <h2 className="font-bold">추천에 대해 묻기</h2>
            {owner && effectiveMode === "question" && selected && (
              <button
                className={`truncate rounded-full px-2.5 py-0.5 text-xs ${askSelected ? "bg-brand-soft text-brand" : "bg-soft text-muted"}`}
                onClick={() => setAskSelected((v) => !v)}
                title="질문 대상을 바꾸려면 누르세요"
              >
                질문 대상 · {askSelected ? selected.name : "추천 전체"}
              </button>
            )}
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
      </div>

      {readme && <Readme target={readme} onClose={() => setReadme(null)} />}
    </div>
  );
}

function okCount(c: Candidate) {
  return `충족 ${c.checks.filter((k) => k.status === "ok").length}/${c.checks.length}`;
}

function CandidateList({
  result,
  filter,
  onFilter,
  selectedId,
  onSelect,
}: {
  result: ChatResult;
  filter: Filter;
  onFilter: (f: Filter) => void;
  selectedId?: string;
  onSelect: (id: string) => void;
}) {
  const models = result.candidates.filter((c) => c.type === "model");
  const datasets = result.candidates.filter((c) => c.type === "dataset");
  const summary = result.summary.filter((s) => s !== result.title);
  const groups: [string, Candidate[]][] = [
    ["추천 모델", filter === "dataset" ? [] : models],
    ["추천 데이터", filter === "model" ? [] : datasets],
  ];

  return (
    <section className="min-h-0 space-y-4 overflow-y-auto rounded-2xl border border-line bg-white p-4">
      <div>
        <h2 className="mb-2 text-sm font-semibold text-muted">요구사항 분석</h2>
        <div className="flex flex-wrap gap-1.5">
          {summary.map((s) => (
            <span key={s} className="rounded-full border border-line px-2.5 py-1 text-xs">
              {s}
            </span>
          ))}
          {summary.length === 0 && <span className="text-xs text-muted">정리된 요구사항이 없어요.</span>}
        </div>
      </div>

      {result.needs_check.length > 0 && (
        <div className="rounded-xl bg-warn-soft p-3 text-sm text-warn">
          <div className="font-semibold">확인 필요 {result.needs_check.length}</div>
          <ul className="mt-1 space-y-0.5 text-xs">
            {result.needs_check.map((n) => (
              <li key={n}>{n}</li>
            ))}
          </ul>
        </div>
      )}

      <div className="grid grid-cols-3 rounded-xl bg-soft p-1 text-sm" role="tablist">
        {(
          [
            ["all", `전체 ${result.candidates.length}`],
            ["model", `모델 ${models.length}`],
            ["dataset", `데이터 ${datasets.length}`],
          ] as const
        ).map(([value, label]) => (
          <button
            key={value}
            role="tab"
            aria-selected={filter === value}
            className={`rounded-lg py-1.5 ${filter === value ? "bg-white font-semibold shadow-sm" : "text-muted"}`}
            onClick={() => onFilter(value)}
          >
            {label}
          </button>
        ))}
      </div>

      {result.candidates.length === 0 && <p className="text-sm text-muted">후보가 없어요.</p>}

      {groups.map(
        ([label, items]) =>
          items.length > 0 && (
            <div key={label}>
              <h3 className="mb-2 text-sm font-semibold">
                {label} {items.length}
              </h3>
              <ul className="space-y-2">
                {items.map((c) => (
                  <li key={c.id}>
                    <button
                      className={`w-full rounded-xl border p-3 text-left ${c.id === selectedId ? "border-brand bg-brand-soft/60" : "border-line hover:border-brand/40"}`}
                      aria-current={c.id === selectedId}
                      onClick={() => onSelect(c.id)}
                    >
                      <div className="flex items-start justify-between gap-2">
                        <span className="break-all font-semibold">{c.name}</span>
                        <span className="shrink-0 rounded-full border border-line bg-white px-2 py-0.5 text-[11px] text-muted">
                          {c.tags[0] ?? c.source}
                        </span>
                      </div>
                      <div className="mt-1 flex justify-between gap-2 text-xs text-muted">
                        <span className="truncate">{c.role}</span>
                        {c.checks.length > 0 && <span className="shrink-0">{okCount(c)}</span>}
                      </div>
                    </button>
                  </li>
                ))}
              </ul>
            </div>
          ),
      )}
    </section>
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
  sources,
  onSelect,
  onReadme,
}: {
  candidate: Candidate;
  all: Candidate[];
  sources: Source[];
  onSelect: (id: string) => void;
  onReadme: (s: { source_id: string; kind: "model" | "dataset"; title?: string | null; url?: string | null; quote?: string | null }) => void;
}) {
  const related = c.related.map((id) => all.find((x) => x.id === id)).filter((x): x is Candidate => Boolean(x));
  const readme = (quote?: string | null) => onReadme({ source_id: c.source_id, kind: c.type, title: c.name, url: c.url, quote });

  return (
    <article className="space-y-8">
      <header className="space-y-3">
        <div className="flex flex-wrap items-center gap-3">
          <h2 className="break-all text-3xl font-bold">{c.name}</h2>
          <span className="rounded-full bg-brand px-2.5 py-0.5 text-xs font-semibold text-white">{c.type === "model" ? "모델" : "데이터셋"}</span>
          <div className="ml-auto flex gap-2">
            <button className="rounded-full border border-line px-3 py-1 text-sm hover:border-brand/50" onClick={() => readme()}>
              README 원문
            </button>
            {c.url && (
              <a className="rounded-full border border-line px-3 py-1 text-sm hover:border-brand/50" href={c.url} target="_blank" rel="noopener noreferrer">
                ↗ {c.source}
              </a>
            )}
          </div>
        </div>
        <p className="text-sm">
          <span className="font-semibold text-brand">이 아이디어에서의 역할</span> {c.role}
        </p>
        {c.tags.length > 0 && (
          <div className="flex flex-wrap gap-1.5">
            {c.tags.map((t) => (
              <span key={t} className="rounded-full border border-line px-2.5 py-1 text-xs">
                {t}
              </span>
            ))}
          </div>
        )}
      </header>

      {c.type === "model" && <Metrics c={c} />}

      <section>
        <h3 className="mb-2 font-bold">조건 확인</h3>
        {c.checks.length === 0 ? (
          <p className="text-sm text-muted">판정할 조건이 없어요.</p>
        ) : (
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-line text-left text-xs text-muted">
                  <th className="py-2 pr-4 font-normal">확인 항목</th>
                  <th className="py-2 pr-4 font-normal">판정</th>
                  <th className="py-2 font-normal">근거</th>
                </tr>
              </thead>
              <tbody>
                {c.checks.map((k) => (
                  <tr key={k.key} className="border-b border-line align-top">
                    <td className="whitespace-nowrap py-3 pr-4 font-semibold">{k.label}</td>
                    <td className="py-3 pr-4">
                      <StatusBadge status={k.status} />
                    </td>
                    <td className="py-3">
                      {k.quote && <p>“{k.quote}”</p>}
                      <p className={k.quote ? "text-xs text-muted" : ""}>{k.reason}</p>
                      <p className="mt-0.5 text-xs text-faint">
                        {ORIGIN[k.origin]}
                        {k.quote && k.source_id && (
                          <button className="ml-2 text-brand underline" onClick={() => readme(k.quote)}>
                            원문에서 보기
                          </button>
                        )}
                      </p>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>

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
