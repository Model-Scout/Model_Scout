// V2 contract: backend/docs/02-api-v2.md, backend/app/result.py. Only the five public APIs are used.

export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export type Origin = "readme" | "metadata" | "estimate" | "unknown";

export type Source = {
  source_id: string;
  kind: "model" | "dataset";
  title: string | null;
  url: string | null;
  quote: string | null;
  origin: Origin;
  location: string | null;
};

export type Check = {
  key: string;
  label: string;
  status: "ok" | "check" | "unknown";
  reason: string;
  source_id: string | null;
  quote: string | null;
  origin: Origin;
};

export type Evidence = { label: string; text: string | null; origin: "readme" | "metadata" };

export type Candidate = {
  id: string;
  type: "model" | "dataset";
  source_id: string;
  name: string;
  role: string;
  tags: string[];
  source: string;
  url: string | null;
  checks: Check[];
  evidence: Evidence[];
  related: string[];
  rank_score: number | null;
  context_length: number | null;
  parameters_b: number | null;
  // AI metadata extension area: fields may be absent, treat as 미확인.
  benchmarks: Record<string, unknown>[];
  gpu_fit: Record<string, unknown> | null;
};

export type ChatResult = {
  title: string;
  summary: string[];
  needs_check: string[];
  candidates: Candidate[];
  assessment: Record<string, unknown> | null;
};

export type ChatDone = {
  schema_version: 2;
  type: "answer" | "clarify" | "reject";
  group_id: string;
  elapsed: number;
  answer: string;
  sources: Source[];
  result: ChatResult | null;
  history_saved: boolean;
};

export type ChatStatus = { step: number; total: number; label: string; elapsed: number };
export type ChatError = { code: string; message: string; group_id: string };

export type StreamEvent =
  | { event: "status"; data: ChatStatus }
  | { event: "token"; data: { text: string } }
  | { event: "done"; data: ChatDone }
  | { event: "error"; data: ChatError };

export type ChatRequest = {
  query: string;
  group_id: string | null;
  mode: "recommend" | "question";
  target_id: string | null;
};

export type GroupSummary = { group_id: string; title: string; created_at: string; updated_at: string };

export type Message = {
  id: number;
  role: "user" | "assistant";
  content: string;
  type: ChatDone["type"] | null;
  result: ChatResult | null;
  sources: Source[];
  created_at: string;
};

export type GroupDetail = GroupSummary & { messages: Message[]; result: ChatResult | null };

export type SourceFile = { source_id: string; content: string; truncated: boolean };

/** HTTP error before the stream starts. status 0 = network failure. */
export class ApiError extends Error {
  constructor(
    public status: number,
    message: string,
    public retryAfter: number | null = null,
  ) {
    super(message);
  }
}

const SESSION_KEY = "model-scout-session";

// No login API: a browser-generated UUID is the owner identity. Never put it in URLs or logs.
export function sessionId(): string {
  let id = localStorage.getItem(SESSION_KEY);
  if (!id) {
    id = crypto.randomUUID();
    localStorage.setItem(SESSION_KEY, id);
  }
  return id;
}

/** Splits buffered SSE text into complete events; returns the unparsed tail. Handles CRLF and split chunks. */
export function parseSse(buffer: string): { events: StreamEvent[]; rest: string } {
  // A trailing "\r" may be the first half of "\r\n" split across chunks; keep it for the next call.
  const hold = buffer.endsWith("\r") ? "\r" : "";
  const text = (hold ? buffer.slice(0, -1) : buffer).replace(/\r\n?/g, "\n");
  const blocks = text.split("\n\n");
  const rest = (blocks.pop() ?? "") + hold;
  const events: StreamEvent[] = [];
  for (const block of blocks) {
    let event = "message";
    const data: string[] = [];
    for (const line of block.split("\n")) {
      if (line.startsWith("event:")) event = line.slice(6).trim();
      else if (line.startsWith("data:")) data.push(line.slice(5).replace(/^ /, ""));
    }
    if (data.length) events.push({ event, data: JSON.parse(data.join("\n")) } as StreamEvent);
  }
  return { events, rest };
}

/**
 * POST /api/chat. Calls onGroupId as soon as X-Group-Id arrives, then each SSE event.
 * Resolves with the terminal done/error event; throws ApiError for HTTP errors or a stream that ends without one.
 * Never retried automatically: a resend can create a new group or a duplicate AI run.
 */
export async function streamChat(
  body: ChatRequest,
  onEvent: (event: StreamEvent) => void,
  options: { signal?: AbortSignal; onGroupId?: (id: string) => void } = {},
): Promise<Extract<StreamEvent, { event: "done" | "error" }>> {
  const res = await request("/api/chat", {
    method: "POST",
    headers: { "content-type": "application/json", "x-session-id": sessionId() },
    body: JSON.stringify(body),
    signal: options.signal,
  });
  const groupId = res.headers.get("x-group-id");
  if (groupId) options.onGroupId?.(groupId);
  if (!res.body) throw new ApiError(0, "응답 스트림이 없어요.");

  const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();
  let buffer = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) throw new ApiError(0, "연결이 중단됐어요. 대화 기록을 확인한 뒤 다시 요청해 주세요.");
    const parsed = parseSse(buffer + value);
    buffer = parsed.rest;
    for (const ev of parsed.events) {
      onEvent(ev);
      if (ev.event === "done" || ev.event === "error") {
        reader.cancel().catch(() => {});
        return ev;
      }
    }
  }
}

export async function listGroups(): Promise<GroupSummary[]> {
  return (await request("/api/groups", { headers: { "x-session-id": sessionId() } })).json();
}

export async function getGroup(groupId: string): Promise<GroupDetail> {
  return (await request(`/api/groups/${encodeURIComponent(groupId)}`)).json();
}

/** README of a candidate or source. sourceId has no model:/dataset: prefix and may contain "/". */
export async function getFile(sourceId: string, kind: "model" | "dataset"): Promise<SourceFile> {
  const path = sourceId.split("/").map(encodeURIComponent).join("/");
  return (await request(`/api/files/${path}?kind=${kind}`)).json();
}

async function request(path: string, init: RequestInit = {}): Promise<Response> {
  let res: Response;
  try {
    res = await fetch(`${API_URL}${path}`, init);
  } catch (e) {
    if (init.signal?.aborted) throw e;
    throw new ApiError(0, "서버에 연결하지 못했어요.");
  }
  if (res.ok) return res;
  const retry = Number(res.headers.get("retry-after"));
  throw new ApiError(res.status, await errorMessage(res), Number.isFinite(retry) && retry > 0 ? retry : null);
}

const STATUS_MESSAGES: Record<number, string> = {
  403: "다른 브라우저에서 만든 대화라 이어서 질문할 수 없어요.",
  404: "찾을 수 없어요.",
  409: "이전 요청을 아직 처리하고 있어요. 잠시 후 다시 시도해 주세요.",
  429: "요청이 너무 많아요. 잠시 후 다시 시도해 주세요.",
  503: "서버 설정이 준비되지 않았어요.",
};

async function errorMessage(res: Response): Promise<string> {
  try {
    const body = await res.json();
    if (typeof body.detail === "string" && res.status !== 422) return body.detail;
  } catch {
    // 500 bodies may not be JSON.
  }
  return STATUS_MESSAGES[res.status] ?? (res.status === 422 ? "요청 형식이 올바르지 않아요." : `서버 오류 (HTTP ${res.status})`);
}
