"use client";

import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import type { Check, ChatStatus, Origin } from "@/lib/api";

export function Logo({ size = 28 }: { size?: number }) {
  // eslint-disable-next-line @next/next/no-img-element
  return <img src="/logo.png" alt="" width={size} height={Math.round((size * 75) / 88)} className="shrink-0" />;
}

/** Safe markdown: react-markdown never renders raw HTML. */
export function Markdown({ text }: { text: string }) {
  return (
    <div className="md">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{ a: (props) => <a {...props} target="_blank" rel="noopener noreferrer" /> }}
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

/** Progress from SSE status events. step is not a percentage and may repeat or skip, so only labels are shown. */
export function Progress({ status, onCancel }: { status: ChatStatus[]; onCancel?: () => void }) {
  const labels = [...new Set(status.map((s) => s.label))];
  const elapsed = status.at(-1)?.elapsed;
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
        {elapsed !== undefined && <span>{Math.round(elapsed)}초 경과</span>}
        {onCancel && (
          <button type="button" className="underline hover:text-ink" onClick={onCancel}>
            취소
          </button>
        )}
      </div>
    </div>
  );
}
