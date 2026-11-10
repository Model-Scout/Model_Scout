"use client";

import { useEffect, useState } from "react";
import { Markdown } from "@/components/ui";
import { ApiError, getFile, type SourceFile } from "@/lib/api";

export type ReadmeTarget = { sourceId: string; kind: "model" | "dataset"; title: string; url: string | null; quote?: string | null };

/** README viewer. location is always null in V2, so the quote is located by exact text match only. */
export function Readme({ target, onClose }: { target: ReadmeTarget; onClose: () => void }) {
  const [file, setFile] = useState<SourceFile | null>(null);
  const [error, setError] = useState<string>();

  useEffect(() => {
    let live = true;
    getFile(target.sourceId, target.kind)
      .then((f) => live && setFile(f))
      .catch((e) => live && setError(e instanceof ApiError && e.status === 404 ? "서버에 이 원문이 없어요." : String(e instanceof Error ? e.message : e)));
    return () => {
      live = false;
    };
  }, [target.sourceId, target.kind]);

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => e.key === "Escape" && onClose();
    addEventListener("keydown", onKey);
    return () => removeEventListener("keydown", onKey);
  }, [onClose]);

  const quote = target.quote?.trim();
  const at = file && quote ? file.content.indexOf(quote) : -1;

  return (
    <div className="fixed inset-0 z-50 flex justify-end bg-black/30" onClick={onClose}>
      <div
        role="dialog"
        aria-modal
        aria-label={`${target.title} README`}
        className="flex h-full w-full max-w-3xl flex-col bg-white shadow-xl"
        onClick={(e) => e.stopPropagation()}
      >
        <header className="flex items-center gap-3 border-b border-line px-6 py-4">
          <div className="min-w-0 flex-1">
            <div className="text-xs text-muted">README 원문</div>
            <h2 className="truncate text-lg font-bold">{target.title}</h2>
          </div>
          {target.url && (
            <a className="rounded-full border border-line px-3 py-1 text-sm" href={target.url} target="_blank" rel="noopener noreferrer">
              출처 페이지 ↗
            </a>
          )}
          <button aria-label="닫기" className="rounded-lg px-2 py-1 text-xl text-muted hover:bg-soft" onClick={onClose}>
            ×
          </button>
        </header>

        <div className="flex-1 overflow-y-auto px-6 py-5">
          {error && <p className="rounded-lg bg-soft p-4 text-sm text-muted">{error}{target.url && " 위의 출처 페이지에서 확인해 주세요."}</p>}
          {!file && !error && <p className="text-sm text-muted">원문을 불러오는 중…</p>}
          {file && (
            <>
              {quote && (
                <div className={`mb-5 rounded-xl p-4 text-sm ${at >= 0 ? "bg-ok-soft" : "bg-warn-soft"}`}>
                  {at >= 0 ? (
                    <>
                      <div className="mb-1 text-xs font-semibold text-ok">원문에서 찾은 인용 위치</div>
                      <p className="whitespace-pre-wrap">
                        …{file.content.slice(Math.max(0, at - 200), at)}
                        <mark className="bg-yellow-200">{quote}</mark>
                        {file.content.slice(at + quote.length, at + quote.length + 200)}…
                      </p>
                    </>
                  ) : (
                    <>
                      <div className="mb-1 text-xs font-semibold text-warn">저장된 인용문 · 현재 원문에서 같은 문장을 찾지 못했어요</div>
                      <p className="whitespace-pre-wrap">“{quote}”</p>
                    </>
                  )}
                </div>
              )}
              {file.truncated && <p className="mb-4 text-xs text-warn">원문이 길어 앞부분만 보여 줘요.</p>}
              <Markdown text={file.content} />
            </>
          )}
        </div>
      </div>
    </div>
  );
}
