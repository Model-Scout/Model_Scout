"use client";

import { useRef, useState } from "react";
import { ComparePanel } from "@/components/ComparePanel";
import { TurnView, type Turn } from "@/components/TurnView";
import { streamRecommend, type RecommendBody, type StreamEvent } from "@/lib/api";

const EXAMPLES = ["따릉이 경로 추천 서비스를 만들고 싶어", "한국어 요약 모델, 8B 이하, 상업 이용 가능"];

function applyEvent(turn: Turn, ev: StreamEvent): Turn {
  switch (ev.event) {
    case "status":
      return { ...turn, steps: [...turn.steps, ev.data.node] };
    case "plan":
      return { ...turn, plan: ev.data };
    case "clarify":
      return { ...turn, clarify: ev.data.questions };
    case "models":
      return { ...turn, models: ev.data };
    case "datasets":
      return { ...turn, datasets: ev.data };
    case "assessment":
      return { ...turn, assessment: ev.data };
    case "token":
      return { ...turn, answer: turn.answer + ev.data.text };
    case "done":
      return { ...turn, elapsed: ev.data.elapsed };
    case "error":
      return { ...turn, error: ev.data.message };
  }
}

export default function Home() {
  const [turns, setTurns] = useState<Turn[]>([]);
  const [threadId, setThreadId] = useState<string>();
  const [input, setInput] = useState("");
  const [selected, setSelected] = useState<string[]>([]);
  const abort = useRef<AbortController | null>(null);
  const running = turns.at(-1)?.running ?? false;

  const updateLast = (fn: (t: Turn) => Turn) => setTurns((ts) => [...ts.slice(0, -1), fn(ts[ts.length - 1])]);

  async function send(body: RecommendBody, request?: string) {
    if (request) setTurns((ts) => [...ts, { request, steps: [], answer: "", running: true }]);
    else updateLast((t) => ({ ...t, clarify: undefined, running: true }));
    abort.current = new AbortController();
    try {
      await streamRecommend(
        body,
        (ev) => {
          if (ev.event === "clarify" || ev.event === "done") setThreadId(ev.data.thread_id);
          updateLast((t) => applyEvent(t, ev));
        },
        abort.current.signal,
      );
    } catch (e) {
      if (!abort.current.signal.aborted) updateLast((t) => ({ ...t, error: String(e instanceof Error ? e.message : e) }));
    } finally {
      updateLast((t) => ({ ...t, running: false }));
    }
  }

  function submit(text: string) {
    const message = text.trim();
    if (message.length < 2 || running) return;
    setInput("");
    send({ message, thread_id: threadId }, message);
  }

  function reset() {
    abort.current?.abort();
    setTurns([]);
    setThreadId(undefined);
    setSelected([]);
  }

  const toggleModel = (id: string) =>
    setSelected((s) => (s.includes(id) ? s.filter((x) => x !== id) : s.length < 3 ? [...s, id] : s));

  return (
    <main className="mx-auto max-w-4xl space-y-8 px-4 py-10">
      <header className="flex items-baseline justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold">Model Scout</h1>
          <p className="text-sm text-neutral-500">만들고 싶은 서비스를 말하면 한국어 모델과 데이터셋을 근거와 함께 추천합니다.</p>
        </div>
        {turns.length > 0 && (
          <button className="text-sm text-neutral-500 underline" onClick={reset}>
            새 대화
          </button>
        )}
      </header>

      {turns.map((turn, i) => (
        <TurnView
          key={i}
          turn={turn}
          selected={selected}
          onToggleModel={toggleModel}
          onAnswer={(answer) => send({ answer, thread_id: threadId })}
        />
      ))}

      {selected.length > 0 && <ComparePanel ids={selected} onClear={() => setSelected([])} />}

      <form
        className="sticky bottom-4 space-y-2 rounded-xl border border-neutral-200 bg-white p-3 shadow-sm"
        onSubmit={(e) => {
          e.preventDefault();
          submit(input);
        }}
      >
        <textarea
          aria-label="요청"
          rows={2}
          maxLength={2000}
          className="w-full resize-none rounded px-2 py-1 outline-none"
          placeholder={turns.length ? "이어서 요청하기 (예: 상업용만 다시)" : "어떤 서비스를 만들고 싶나요?"}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
              e.preventDefault();
              submit(input);
            }
          }}
        />
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div className="flex flex-wrap gap-1">
            {turns.length === 0 &&
              EXAMPLES.map((ex) => (
                <button
                  type="button"
                  key={ex}
                  className="rounded-full bg-neutral-100 px-3 py-1 text-xs text-neutral-600"
                  onClick={() => submit(ex)}
                >
                  {ex}
                </button>
              ))}
          </div>
          <button
            className="rounded-lg bg-neutral-900 px-4 py-2 text-sm text-white disabled:opacity-50"
            disabled={running || input.trim().length < 2}
          >
            {running ? "추천 중…" : "보내기"}
          </button>
        </div>
      </form>
    </main>
  );
}
