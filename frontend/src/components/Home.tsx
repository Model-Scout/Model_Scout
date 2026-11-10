"use client";

import { useEffect, useState } from "react";
import { Logo } from "@/components/ui";
import { listGroups, type GroupSummary } from "@/lib/api";

const EXAMPLES = [
  { title: "따릉이 주차 경로 추천", desc: "로컬에서 구현할 수 있는 대여소·경로 추천", query: "로컬에서 구현할 수 있는 따릉이 대여소·주차 경로 추천 서비스를 만들고 싶어." },
  { title: "영문 긴 문서 검색", desc: "긴 문서 검색에 쓸 모델과 평가 데이터", query: "영문 긴 문서를 검색하는 서비스를 만들고 싶어. 검색 모델과 평가 데이터가 필요해." },
  { title: "차트 이해 멀티모달", desc: "차트를 읽고 답하는 모델과 데이터셋", query: "차트 이미지를 읽고 질문에 답하는 멀티모달 서비스를 만들고 싶어." },
];

const LANGUAGES = ["한국어", "영어"];
const RUNTIMES = ["로컬 GPU 8GB", "로컬 GPU 16GB", "로컬 GPU 24GB", "CPU만"];
const MAX = 2000;

/** No conditions API: selected conditions are appended to the query as a sentence the user can see. */
function withConditions(idea: string, language: string, runtime: string, commercial: boolean) {
  const parts = [language && `언어 ${language}`, runtime && `실행 환경 ${runtime}`, commercial && "상업적 이용 가능"].filter(Boolean);
  return parts.length ? `${idea}\n조건: ${parts.join(", ")}.` : idea;
}

export function Home({ onSend, onOpenGroup }: { onSend: (query: string) => void; onOpenGroup: (id: string) => void }) {
  const [idea, setIdea] = useState("");
  const [language, setLanguage] = useState("한국어");
  const [runtime, setRuntime] = useState("");
  const [commercial, setCommercial] = useState(false);
  const [drawer, setDrawer] = useState(false);

  const query = withConditions(idea.trim(), language, runtime, commercial);
  const tooLong = query.length > MAX;
  const submit = (text: string) => {
    const q = withConditions(text.trim(), language, runtime, commercial);
    if (text.trim() && q.length <= MAX) onSend(q);
  };

  const chip = "rounded-full border border-line bg-white px-3 py-1 text-xs text-ink";

  return (
    <div className="relative flex min-h-dvh overflow-hidden">
      <div aria-hidden className="pointer-events-none absolute -right-40 -top-64 size-[720px] rounded-full bg-brand-soft blur-3xl" />
      <div aria-hidden className="pointer-events-none absolute -bottom-40 -left-72 size-[640px] rounded-full bg-brand-soft/70 blur-3xl" />

      {drawer ? (
        <HistoryDrawer onClose={() => setDrawer(false)} onOpen={onOpenGroup} />
      ) : (
        <button
          aria-label="대화 기록 열기"
          className="absolute left-5 top-5 z-10 rounded-lg p-2 text-ink hover:bg-soft"
          onClick={() => setDrawer(true)}
        >
          <PanelIcon />
        </button>
      )}

      <main className="relative flex flex-1 flex-col items-center px-4 pb-10 pt-[22vh]">
        <div className="flex items-center gap-4">
          <Logo size={64} />
          <h1 className="text-4xl font-bold sm:text-5xl">Model Scout</h1>
        </div>
        <p className="mt-3 text-lg text-muted">데이터 · 모델 추천 서비스</p>

        <form
          className="mt-10 w-full max-w-[760px] rounded-2xl border border-line bg-white p-5 shadow-[0_8px_24px_rgba(111,58,104,0.08)] focus-within:border-brand/50"
          onSubmit={(e) => {
            e.preventDefault();
            submit(idea);
          }}
        >
          <textarea
            aria-label="서비스 아이디어"
            rows={2}
            className="w-full resize-none text-base outline-none placeholder:text-faint"
            placeholder="만들고 싶은 서비스 아이디어를 한 줄로 적어 주세요"
            value={idea}
            onChange={(e) => setIdea(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
                e.preventDefault();
                submit(idea);
              }
            }}
          />
          <div className="mt-3 flex items-center gap-2">
            <div className="flex flex-1 flex-wrap items-center gap-2">
              <span className="text-xs font-semibold text-muted">조건</span>
              <select aria-label="언어" className={chip} value={language} onChange={(e) => setLanguage(e.target.value)}>
                <option value="">언어: 상관없음</option>
                {LANGUAGES.map((l) => (
                  <option key={l} value={l}>
                    언어: {l}
                  </option>
                ))}
              </select>
              <select aria-label="실행 환경" className={chip} value={runtime} onChange={(e) => setRuntime(e.target.value)}>
                <option value="">실행: 상관없음</option>
                {RUNTIMES.map((r) => (
                  <option key={r} value={r}>
                    실행: {r}
                  </option>
                ))}
              </select>
              <button
                type="button"
                aria-pressed={commercial}
                className={`${chip} ${commercial ? "border-brand bg-brand-soft text-brand" : "text-muted"}`}
                onClick={() => setCommercial((c) => !c)}
              >
                상업적 이용 {commercial ? "✓" : ""}
              </button>
            </div>
            <button
              aria-label="추천 받기"
              disabled={!idea.trim() || tooLong}
              className="grid size-10 shrink-0 place-items-center rounded-full bg-brand text-white disabled:opacity-40"
            >
              ↑
            </button>
          </div>
          {idea.trim() && query !== idea.trim() && (
            <p className="mt-3 border-t border-line pt-2 text-xs text-muted">
              {query.slice(idea.trim().length + 1)} <span className="text-faint">· 요청에 이 문장을 붙여 보내요</span>
            </p>
          )}
          {tooLong && <p className="mt-2 text-xs text-danger">조건 포함 {MAX.toLocaleString()}자까지 보낼 수 있어요.</p>}
        </form>

        <section className="mt-10 w-full max-w-[760px]">
          <h2 className="mb-2 text-sm text-muted">이런 아이디어로 시작해 보세요</h2>
          <div className="grid gap-3 sm:grid-cols-3">
            {EXAMPLES.map((ex) => (
              <button
                key={ex.title}
                className="rounded-xl border border-line bg-white p-3 text-left hover:border-brand/50"
                onClick={() => submit(ex.query)}
              >
                <div className="text-sm font-semibold">{ex.title}</div>
                <div className="mt-1 text-xs text-muted">{ex.desc}</div>
              </button>
            ))}
          </div>
        </section>

        <footer className="mt-auto pt-16 text-xs text-faint">
          공공데이터포털 · 서울 열린데이터광장 · Hugging Face · Kaggle에서 찾아요
        </footer>
      </main>
    </div>
  );
}

function bucket(iso: string) {
  const days = (Date.now() - new Date(iso).getTime()) / 86_400_000;
  if (new Date(iso).toDateString() === new Date().toDateString()) return "오늘";
  if (days < 7) return "지난 7일";
  if (days < 30) return "지난 30일";
  return "이전";
}

function HistoryDrawer({ onClose, onOpen }: { onClose: () => void; onOpen: (id: string) => void }) {
  const [groups, setGroups] = useState<GroupSummary[] | null>(null);
  const [error, setError] = useState<string>();

  useEffect(() => {
    listGroups()
      .then(setGroups)
      .catch((e) => setError(e instanceof Error ? e.message : String(e)));
  }, []);

  const sections = new Map<string, GroupSummary[]>();
  for (const g of groups ?? []) {
    const key = bucket(g.updated_at);
    sections.set(key, [...(sections.get(key) ?? []), g]);
  }

  return (
    <aside className="relative z-10 flex h-dvh w-[300px] shrink-0 flex-col border-r border-line bg-white/95 p-4">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2 font-bold">
          <Logo size={26} /> Model Scout
        </div>
        <button aria-label="대화 기록 닫기" className="rounded-lg p-2 hover:bg-soft" onClick={onClose}>
          <PanelIcon />
        </button>
      </div>
      <button
        className="mt-4 rounded-lg bg-brand-soft px-3 py-2.5 text-left text-sm font-semibold text-brand"
        onClick={onClose}
      >
        + 새 추천 시작
      </button>

      <nav className="mt-4 flex-1 space-y-4 overflow-y-auto" aria-label="지난 대화">
        {error && <p className="text-sm text-danger">{error}</p>}
        {!groups && !error && <p className="text-sm text-muted">불러오는 중…</p>}
        {groups?.length === 0 && <p className="text-sm text-muted">아직 대화가 없어요.</p>}
        {[...sections].map(([label, rows]) => (
          <div key={label}>
            <h3 className="mb-1 px-2 text-xs text-muted">{label}</h3>
            {rows.map((g) => (
              <button
                key={g.group_id}
                className="block w-full rounded-lg px-3 py-2 text-left hover:bg-brand-soft"
                onClick={() => onOpen(g.group_id)}
              >
                <div className="truncate text-sm">{g.title}</div>
                <div className="text-xs text-muted">{new Date(g.updated_at).toLocaleString("ko-KR", { dateStyle: "short", timeStyle: "short" })}</div>
              </button>
            ))}
          </div>
        ))}
      </nav>

      <p className="mt-3 rounded-lg bg-soft p-3 text-xs text-muted">
        <b className="block text-ink">로그인 없이 쓰는 서비스예요</b>
        대화 기록은 이 브라우저의 세션 ID로 기억해요. 브라우저 데이터를 지우면 기록도 사라져요.
      </p>
    </aside>
  );
}

function PanelIcon() {
  return (
    <svg width="20" height="20" viewBox="0 0 20 20" fill="none" stroke="currentColor" strokeWidth="1.6" aria-hidden>
      <rect x="2.5" y="3" width="15" height="14" rx="2" />
      <path d="M7.5 3v14" />
    </svg>
  );
}
