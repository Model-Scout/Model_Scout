"use client";

import { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { Check, ChatStatus, Origin } from "@/lib/api";

export function Logo({ size = 28 }: { size?: number }) {
  // eslint-disable-next-line @next/next/no-img-element
  return <img src="/logo.png" alt="" width={size} height={Math.round((size * 75) / 88)} className="shrink-0" />;
}

/** Safe markdown: react-markdown never renders raw HTML. */
export function Markdown({ text, foldTables }: { text: string; /** answers: each table behind a toggle */ foldTables?: boolean }) {
  return (
    <div className="md">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          a: (props) => <a {...props} target="_blank" rel="noopener noreferrer" />,
          ...(foldTables && {
            table: ({ node: _node, ...props }) => (
              <details className="rounded-lg border border-line px-3 py-2">
                <summary className="cursor-pointer text-xs font-semibold text-brand">추천 · 대안 · 관련 데이터 보기</summary>
                <table {...props} className="mt-2" />
              </details>
            ),
          }),
        }}
      >
        {text}
      </ReactMarkdown>
    </div>
  );
}

const STATUS: Record<Check["status"], [string, string]> = {
  ok: ["충족", "bg-ok-soft text-ok"],
  check: ["확인 필요", "bg-warn-soft text-warn"],
  unknown: ["미확인", "bg-soft text-muted"],
};

export function StatusBadge({ status }: { status: Check["status"] }) {
  const [label, cls] = STATUS[status] ?? STATUS.unknown;
  return <span className={`inline-block whitespace-nowrap rounded-full px-2.5 py-0.5 text-xs font-semibold ${cls}`}>{label}</span>;
}

export const ORIGIN: Record<Origin, string> = {
  readme: "README 원문",
  metadata: "메타데이터",
  estimate: "추정",
  unknown: "근거 없음",
};

/** Finished analysis: every step checked, with the total time. */
export function DoneSteps({ status, elapsed }: { status: ChatStatus[]; elapsed?: number }) {
  const labels = [...new Set(status.map((s) => s.label))];
  return (
    <div className="space-y-2">
      <span className="inline-block rounded-full bg-ok-soft px-2 py-0.5 text-xs font-semibold text-ok">
        ✓ 분석 완료{elapsed !== undefined && ` · ${Math.round(elapsed)}초`}
      </span>
      {labels.length > 0 && (
        <ol className="flex flex-wrap gap-x-5 gap-y-1 text-sm">
          {labels.map((label) => (
            <li key={label} className="flex items-center gap-1.5">
              <span className="grid h-4 w-5 place-items-center rounded-full bg-ok text-[10px] text-white" aria-hidden>
                ✓
              </span>
              {label}
            </li>
          ))}
        </ol>
      )}
    </div>
  );
}

/** Progress from SSE status events. step is not a percentage and may repeat or skip, so only labels are shown. */
export function Progress({ status, onCancel }: { status: ChatStatus[]; onCancel?: () => void }) {
  const labels = [...new Set(status.map((s) => s.label))];
  // Status events arrive only between steps, so the shown time ticks locally every second.
  const [started] = useState(() => Date.now() - (status.at(-1)?.elapsed ?? 0) * 1000);
  const [now, setNow] = useState(() => Date.now());
  useEffect(() => {
    const id = setInterval(() => setNow(Date.now()), 1000);
    return () => clearInterval(id);
  }, []);
  const elapsed = Math.max(0, (now - started) / 1000);
  return (
    <div className="space-y-2">
      <ol className="space-y-1 text-sm">
        {labels.length === 0 && <li className="text-muted">요청을 보내는 중…</li>}
        {labels.map((label, i) => {
          const current = i === labels.length - 1;
          return (
            <li key={label} className={`flex items-center gap-2 ${current ? "font-semibold text-ink" : "text-muted"}`}>
              <span
                className={`size-2 rounded-full ${current ? "animate-pulse bg-brand" : "bg-ok"}`}
                aria-hidden
              />
              {label}
              {current && " 중…"}
            </li>
          );
        })}
      </ol>
      <div className="flex items-center gap-3 text-xs text-muted">
        <span>{Math.floor(elapsed)}초 경과</span>
        {onCancel && (
          <button type="button" className="underline hover:text-ink" onClick={onCancel}>
            취소
          </button>
        )}
      </div>
    </div>
  );
}
