"use client";

import { useEffect, useState } from "react";
import { Markdown } from "@/components/ui";
import { ApiError, getFile, getWiki, type SourceFile, type WikiInfo } from "@/lib/api";

export type ReadmeTarget = { sourceId: string; kind: "model" | "dataset"; title: string; url: string | null; quote?: string | null };

/** README viewer. location is always null in V2, so the quote is located by exact text match only. */
export function Readme({ target, onClose }: { target: ReadmeTarget; onClose: () => void }) {
  const [file, setFile] = useState<SourceFile | null>(null);
  const [error, setError] = useState<string>();
  const [wiki, setWiki] = useState<WikiInfo | null>(null);

  useEffect(() => {
    let live = true;
    getFile(target.sourceId, target.kind)
      .then((f) => live && setFile(f))
      .catch((e) => live && setError(e instanceof ApiError && e.status === 404 ? "서버에 이 원문이 없어요." : String(e instanceof Error ? e.message : e)));
    setWiki(null);
    getWiki(target.sourceId, target.kind)
      .then((w) => live && setWiki(w))
      .catch(() => {}); // wiki is optional: no page or offline just hides the card
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
          {wiki && (wiki.summary || wiki.tags.length > 0) && <WikiCard wiki={wiki} />}
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

/** Wiki summary kept outside the README text so generated content is never mistaken for the original. */
function WikiCard({ wiki }: { wiki: WikiInfo }) {
  return (
    <section aria-label="Wiki 요약" className="mb-5 rounded-xl border border-line bg-soft p-4 text-sm">
      <div className="mb-2 flex items-baseline justify-between gap-2">
        <span className="text-sm font-bold">Model Scout Wiki 요약</span>
        <span className="text-xs text-faint">README 원문이 아닌 자동 생성 요약입니다</span>
      </div>
      {wiki.summary && <p className="mb-2">{wiki.summary}</p>}
      {wiki.tags.length > 0 && (
        <ul className="mb-3 grid grid-cols-2 gap-2 sm:grid-cols-3">
          {wiki.tags.map((t) => (
            <li key={t.label + t.value}>
              <a
                className="group flex h-full flex-col rounded-lg border border-line bg-white px-3 py-2 transition hover:border-brand hover:bg-brand-soft hover:shadow-sm"
                href={t.href}
                target="_blank"
                rel="noopener noreferrer"
              >
                <span className="text-xs text-faint">{t.label}</span>
                <span className="flex items-center justify-between gap-1 font-semibold">
                  {t.value}
                  <span aria-hidden className="text-faint group-hover:text-brand">↗</span>
                </span>
              </a>
            </li>
          ))}
        </ul>
      )}
      {wiki.related.length > 0 && (
        <p className="mb-2 text-xs">
          <span className="text-faint">관련 데이터 · 모델: </span>
          {wiki.related.slice(0, 5).map((r, i) => (
            <span key={r.href}>
              {i > 0 && ", "}
              <a className="text-brand underline" href={r.href} target="_blank" rel="noopener noreferrer">{r.text}</a>
            </span>
          ))}
          {wiki.related.length > 5 && ` 외 ${wiki.related.length - 5}개`}
        </p>
      )}
      <a className="text-xs text-brand underline" href={wiki.url} target="_blank" rel="noopener noreferrer">
        wiki에서 자세히 보기 →
      </a>
    </section>
  );
}
