"use client";

import { forwardRef, useState } from "react";
import type { SendOptions, Turn } from "@/components/App";
import { Logo, Markdown, ORIGIN, Progress } from "@/components/ui";
import type { Source } from "@/lib/api";

type Actions = { onCancel: () => void; onReload?: () => void; onSource?: (s: Source) => void };

export function TurnView({ turn, onCancel, onReload, onSource, compact }: { turn: Turn; compact?: boolean } & Actions) {
  if (turn.role === "user") {
    return (
      <div className="ml-auto max-w-[85%] rounded-2xl bg-brand-soft px-4 py-3 text-sm">
        <div className="mb-1 text-xs font-semibold text-brand">사용자{turn.target && ` · ${turn.target}에 대해`}</div>
        <p className="whitespace-pre-wrap">{turn.content}</p>
      </div>
    );
  }

  const label = turn.type === "clarify" ? "AI · 추가 질문" : turn.type === "reject" ? "AI · 안내" : "AI";
  return (
    <div className={`max-w-[95%] rounded-2xl bg-soft px-4 py-3 text-sm ${compact ? "" : "sm:max-w-[85%]"}`}>
      <div className="mb-1 text-xs font-semibold text-muted">{label}</div>
      {turn.running && <Progress status={turn.status ?? []} onCancel={onCancel} />}
      {/* Streaming tokens are provisional; done replaces them with the final answer. */}
      {turn.content && (
        <div className={turn.running ? "mt-3 opacity-70" : ""}>
          <Markdown text={turn.content} />
        </div>
      )}
      {turn.error && (
        <div className="mt-2 rounded-lg bg-danger-soft px-3 py-2 text-danger">
          {turn.error}
          {turn.interrupted && onReload && (
            <button className="ml-2 underline" onClick={onReload}>
              저장된 기록 확인
            </button>
          )}
        </div>
      )}
      {turn.notSaved && <p className="mt-2 text-xs text-warn">답변을 기록에 저장하지 못했어요. 새로고침하면 이 답변이 보이지 않을 수 있어요.</p>}
      {turn.sources && turn.sources.length > 0 && turn.type === "answer" && (
        <div className="mt-3 border-t border-line pt-2">
          <div className="mb-1 text-xs font-semibold text-muted">답변에 쓸 수 있었던 자료</div>
          <div className="flex flex-wrap gap-1">
            {dedupe(turn.sources).map((s) => (
              <button
                key={s.source_id + s.kind}
                className="rounded-md border border-line bg-white px-2 py-0.5 text-xs hover:border-brand/50"
                onClick={() => onSource?.(s)}
                title={ORIGIN[s.origin]}
              >
                {s.title ?? s.source_id}
              </button>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

function dedupe(sources: Source[]) {
  return [...new Map(sources.map((s) => [s.kind + s.source_id, s])).values()];
}

type ComposerProps = { placeholder: string; disabled: boolean; onSubmit: (text: string) => void };

export const Composer = forwardRef<HTMLTextAreaElement, ComposerProps>(function Composer({ placeholder, disabled, onSubmit }, ref) {
  const [text, setText] = useState("");
  const submit = () => {
    if (!text.trim() || disabled) return;
    onSubmit(text);
    setText("");
  };
  return (
    <form
      className="flex items-end gap-2 rounded-2xl border border-line bg-white p-2 pl-4 focus-within:border-brand/50"
      onSubmit={(e) => {
        e.preventDefault();
        submit();
      }}
    >
      <textarea
        ref={ref}
        rows={1}
        maxLength={2000}
        aria-label={placeholder}
        className="max-h-40 flex-1 resize-none py-2 text-sm outline-none [field-sizing:content] placeholder:text-faint"
        placeholder={placeholder}
        value={text}
        onChange={(e) => setText(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) {
            e.preventDefault();
            submit();
          }
        }}
      />
      <button aria-label="보내기" disabled={disabled || !text.trim()} className="grid size-9 shrink-0 place-items-center rounded-full bg-brand text-white disabled:opacity-40">
        ↑
      </button>
    </form>
  );
});

export function ReadOnlyNotice({ onHome }: { onHome: () => void }) {
  return (
    <div className="rounded-xl bg-soft p-3 text-xs text-muted">
      공유 링크로 연 대화예요. 읽기만 할 수 있고, 이어서 질문은 이 대화를 만든 브라우저에서만 가능해요.
      <button className="ml-1 font-semibold text-brand underline" onClick={onHome}>
        새 추천 시작
      </button>
    </div>
  );
}

/** Before the first recommendation: progress, clarify questions, reject notices. */
export function Thread({
  turns,
  owner,
  onSend,
  onCancel,
  onReload,
  onHome,
}: { turns: Turn[]; owner: boolean; onSend: (q: string, o: SendOptions) => void; onHome: () => void } & Actions) {
  const last = turns.at(-1);
  const running = last?.running ?? false;
  const placeholder =
    last?.type === "clarify" ? "질문에 답해 주세요" : last?.type === "reject" ? "다른 아이디어로 다시 적어 주세요" : "이어서 요청하기";

  return (
    <div className="flex min-h-dvh flex-col">
      <header className="flex items-center gap-3 border-b border-line px-5 py-3">
        <button className="rounded-full bg-brand-soft px-3 py-1.5 text-sm font-semibold text-brand" onClick={onHome}>
          홈으로
        </button>
        <Logo size={28} />
        <span className="font-bold">Model Scout</span>
      </header>
      <main className="mx-auto flex w-full max-w-3xl flex-1 flex-col gap-4 px-4 py-8">
        {turns.map((t, i) => (
          <TurnView key={i} turn={t} onCancel={onCancel} onReload={onReload} />
        ))}
        {running && (
          <div className="space-y-2" aria-hidden>
            <div className="h-20 animate-pulse rounded-xl bg-soft" />
            <div className="h-32 animate-pulse rounded-xl bg-soft" />
          </div>
        )}
      </main>
      <div className="sticky bottom-0 mx-auto w-full max-w-3xl bg-white px-4 pb-6">
        {owner ? (
          <Composer placeholder={placeholder} disabled={running} onSubmit={(q) => onSend(q, { mode: "recommend" })} />
        ) : (
          <ReadOnlyNotice onHome={onHome} />
        )}
      </div>
    </div>
  );
}
