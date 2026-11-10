"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Home } from "@/components/Home";
import { Result } from "@/components/Result";
import { Thread } from "@/components/Thread";
import { Logo } from "@/components/ui";
import {
  ApiError,
  getGroup,
  listGroups,
  streamChat,
  type ChatDone,
  type ChatResult,
  type ChatStatus,
  type GroupDetail,
  type Source,
} from "@/lib/api";

export type Turn = {
  role: "user" | "assistant";
  content: string;
  type?: ChatDone["type"] | null;
  sources?: Source[];
  /** user question turns: name of the candidate asked about */
  target?: string;
  status?: ChatStatus[];
  running?: boolean;
  error?: string;
  /** done arrived but history_saved=false */
  notSaved?: boolean;
  /** stream cut without done/error: offer to reload saved history instead of resending */
  interrupted?: boolean;
};

export type SendOptions = { mode: "recommend" | "question"; target?: { id: string; name: string } };

type Loaded = { result: ChatResult | null; sources: Source[] };

function restore(group: GroupDetail): Loaded & { turns: Turn[] } {
  const turns: Turn[] = group.messages.map((m) => ({
    role: m.role,
    content: m.content,
    type: m.type,
    sources: m.sources,
  }));
  // Latest snapshot wins even with 0 candidates, matching the live screen; result and sources come from the same message.
  // The contract's top-level result skips empty snapshots, so it is only a fallback (e.g. no message carries a result).
  const origin = group.messages.findLast((m) => m.result !== null);
  return { turns, result: origin?.result ?? group.result, sources: origin?.sources ?? [] };
}

function resultUrl(id: string) {
  return `/result/${encodeURIComponent(id)}`;
}

export function App({ initialGroupId }: { initialGroupId?: string }) {
  const [groupId, setGroupId] = useState<string | null>(initialGroupId ?? null);
  const [title, setTitle] = useState("");
  const [turns, setTurns] = useState<Turn[]>([]);
  const [result, setResult] = useState<ChatResult | null>(null);
  const [resultSources, setResultSources] = useState<Source[]>([]);
  // A shared link is readable by anyone; only the creating session may continue it.
  const [owner, setOwner] = useState(true);
  const [loading, setLoading] = useState(Boolean(initialGroupId));
  const [loadError, setLoadError] = useState<string>();
  const abort = useRef<AbortController | null>(null);
  // Bumped whenever the screen switches conversation; late stream/load results from an older one are dropped.
  const conv = useRef(0);
  const running = turns.at(-1)?.running ?? false;

  const load = useCallback(async (id: string) => {
    const mine = ++conv.current;
    setLoading(true);
    setLoadError(undefined);
    try {
      // ponytail: ownership = "in my /api/groups list" (max 100 newest); a 403 on send also flips it. Needs an owner field in GroupDetail to be exact.
      const [group, myGroups] = await Promise.all([getGroup(id), listGroups().catch(() => null)]);
      if (conv.current !== mine) return;
      const restored = restore(group);
      setGroupId(id);
      setTitle(group.title);
      setTurns(restored.turns);
      setResult(restored.result);
      setResultSources(restored.sources);
      setOwner(myGroups ? myGroups.some((g) => g.group_id === id) : false);
      setLoading(false);
    } catch (e) {
      if (conv.current !== mine) return;
      setLoadError(e instanceof ApiError && e.status === 404 ? "대화를 찾을 수 없어요." : e instanceof Error ? e.message : String(e));
      setLoading(false);
    }
  }, []);

  const clear = useCallback(() => {
    conv.current++;
    abort.current?.abort();
    setGroupId(null);
    setTitle("");
    setTurns([]);
    setResult(null);
    setResultSources([]);
    setOwner(true);
    setLoadError(undefined);
    setLoading(false);
  }, []);

  useEffect(() => {
    if (initialGroupId) load(initialGroupId);
  }, [initialGroupId, load]);

  // pushState keeps this component mounted, so back/forward must be applied by hand.
  useEffect(() => {
    const onPop = () => {
      const id = location.pathname.match(/^\/result\/([^/]+)/)?.[1];
      abort.current?.abort();
      if (id) load(decodeURIComponent(id));
      else clear();
    };
    addEventListener("popstate", onPop);
    return () => removeEventListener("popstate", onPop);
  }, [load, clear]);

  function goHome() {
    clear();
    history.pushState(null, "", "/");
  }

  function openGroup(id: string) {
    abort.current?.abort();
    history.pushState(null, "", resultUrl(id));
    load(id);
  }

  async function send(query: string, { mode, target }: SendOptions) {
    const q = query.trim();
    if (!q || running || !owner) return;
    const mine = conv.current;
    const live = () => conv.current === mine;
    const update = (fn: (t: Turn) => Turn) => {
      if (live()) setTurns((ts) => [...ts.slice(0, -1), fn(ts[ts.length - 1])]);
    };
    setTurns((ts) => [
      ...ts,
      { role: "user", content: q, target: target?.name },
      { role: "assistant", content: "", running: true, status: [] },
    ]);
    if (!title) setTitle(q);

    const ctl = new AbortController();
    abort.current = ctl;
    try {
      const end = await streamChat(
        { query: q, group_id: groupId, mode, target_id: target?.id ?? null },
        (ev) => {
          if (ev.event === "status") update((t) => ({ ...t, status: [...(t.status ?? []), ev.data] }));
          else if (ev.event === "token") update((t) => ({ ...t, content: t.content + ev.data.text }));
        },
        {
          signal: ctl.signal,
          onGroupId: (id) => {
            if (groupId || !live()) return;
            setGroupId(id);
            history.replaceState(null, "", resultUrl(id));
          },
        },
      );
      if (!live()) return;
      if (end.event === "done") {
        const d = end.data;
        update(() => ({ role: "assistant", content: d.answer, type: d.type, sources: d.sources, notSaved: !d.history_saved }));
        // result=null (question, clarify, reject) keeps the current recommendation on screen.
        if (d.result) {
          setResult(d.result);
          setResultSources(d.sources);
          setTitle(d.result.title);
        }
      } else {
        // Partial tokens are not an answer.
        update((t) => ({ ...t, running: false, content: "", error: end.data.message }));
      }
    } catch (e) {
      if (!live()) return;
      if (ctl.signal.aborted) {
        update((t) => ({
          ...t,
          running: false,
          content: "",
          error: "분석을 취소했어요. 진행 중이던 단계가 끝날 때까지 다시 요청하면 잠시 기다리거나 거절될 수 있어요.",
        }));
        return;
      }
      const err = e instanceof ApiError ? e : new ApiError(0, String(e));
      if (err.status === 403) setOwner(false);
      const wait = err.retryAfter ? ` (${err.retryAfter}초 후 다시 시도할 수 있어요)` : "";
      update((t) => ({ ...t, running: false, content: "", error: err.message + wait, interrupted: err.status === 0 }));
    }
  }

  const cancel = () => abort.current?.abort();
  const reload = groupId ? () => load(groupId) : undefined;

  if (loading || loadError) {
    return (
      <main className="flex min-h-dvh flex-col items-center justify-center gap-4 text-muted">
        <Logo size={44} />
        <p>{loadError ?? "대화를 불러오는 중…"}</p>
        {loadError && (
          <button className="rounded-full bg-brand px-4 py-2 text-sm text-white" onClick={goHome}>
            홈으로
          </button>
        )}
      </main>
    );
  }

  if (result && groupId) {
    return (
      <Result
        groupId={groupId}
        title={title}
        request={turns.find((t) => t.role === "user")?.content ?? ""}
        result={result}
        sources={resultSources}
        turns={turns}
        owner={owner}
        onSend={send}
        onCancel={cancel}
        onReload={reload}
        onHome={goHome}
      />
    );
  }

  if (turns.length > 0) {
    return <Thread turns={turns} owner={owner} onSend={send} onCancel={cancel} onReload={reload} onHome={goHome} />;
  }

  return <Home onSend={(q) => send(q, { mode: "recommend" })} onOpenGroup={openGroup} />;
}
