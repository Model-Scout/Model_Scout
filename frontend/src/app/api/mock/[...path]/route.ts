// Mock of the five public V2 APIs for screen work and demos without the AI server.
// The client calls `${NEXT_PUBLIC_API_URL}/api/chat`, so with NEXT_PUBLIC_API_URL=/api/mock requests arrive as /api/mock/api/*.
// Enabled in `next dev`, or anywhere with MOCK_API=1 (server env). Otherwise every path is 404.
import { randomUUID } from "crypto";
import type { ChatDone, ChatResult, GroupDetail, Message, Source } from "@/lib/api";
import { BIKE, BIKE_SOURCES, READMES } from "./data";

export const dynamic = "force-dynamic";

const enabled = process.env.NODE_ENV === "development" || process.env.MOCK_API === "1";
const DELAY = Number(process.env.MOCK_DELAY_MS ?? 700);

type Group = { detail: GroupDetail; session: string; running: boolean };
// ponytail: in-memory store. Survives dev HMR via globalThis, but on Vercel each instance has its own copy,
// so a refresh may land on a fresh instance and 404. Use a KV store if the demo needs durable history.
const store: Map<string, Group> = ((globalThis as { __mockGroups?: Map<string, Group> }).__mockGroups ??= new Map());
let messageId = 0;

const json = (body: unknown, status = 200, headers: Record<string, string> = {}) =>
  Response.json(body, { status, headers });
const now = () => new Date().toISOString();
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));

type Ctx = { params: Promise<{ path: string[] }> };

export async function GET(req: Request, { params }: Ctx) {
  if (!enabled) return json({ detail: "Not Found" }, 404);
  const [api, name, ...rest] = (await params).path;
  if (api !== "api") return json({ detail: "Not Found" }, 404);

  if (name === "health") return json({ ok: true });

  if (name === "groups" && rest.length === 0) {
    const session = req.headers.get("x-session-id");
    if (!session) return json({ detail: "X-Session-Id 필요" }, 422);
    const mine = [...store.values()].filter((g) => g.session === session).map((g) => g.detail);
    mine.sort((a, b) => b.updated_at.localeCompare(a.updated_at));
    return json(mine.slice(0, 100).map(({ group_id, title, created_at, updated_at }) => ({ group_id, title, created_at, updated_at })));
  }

  if (name === "groups" && rest.length === 1) {
    const group = store.get(rest[0]);
    return group ? json(group.detail) : json({ detail: "없는 group_id" }, 404);
  }

  if (name === "files" && rest.length > 0) {
    const kind = new URL(req.url).searchParams.get("kind") ?? "model";
    const sourceId = rest.map(decodeURIComponent).join("/");
    const content = READMES[`${kind}:${sourceId}`];
    return content ? json({ source_id: sourceId, content, truncated: false }) : json({ detail: "원문 없음" }, 404);
  }

  return json({ detail: "Not Found" }, 404);
}

export async function POST(req: Request, { params }: Ctx) {
  if (!enabled) return json({ detail: "Not Found" }, 404);
  const path = (await params).path.join("/");
  if (path !== "api/chat") return json({ detail: "Not Found" }, 404);

  const session = req.headers.get("x-session-id");
  if (!session) return json({ detail: [{ loc: ["header", "x-session-id"], msg: "Field required" }] }, 422);
  let body: { query?: unknown; group_id?: unknown; mode?: unknown; target_id?: unknown };
  try {
    body = await req.json();
  } catch {
    return json({ detail: "JSON 본문 필요" }, 422);
  }
  const query = typeof body.query === "string" ? body.query.trim() : "";
  const mode = body.mode ?? "recommend";
  const targetId = (body.target_id as string | null) ?? null;
  if (!query || (body.query as string).length > 2000) return json({ detail: "query는 1~2,000자" }, 422);
  if (mode !== "recommend" && mode !== "question") return json({ detail: "mode 오류" }, 422);
  if (targetId && mode !== "question") return json({ detail: "target_id는 question에서만" }, 422);

  // Fixed inputs that reproduce non-answer paths (see frontend/README.md).
  if (query.includes("[한도]")) return json({ detail: "요청이 너무 많습니다. 잠시 후 다시 시도해 주세요." }, 429, { "Retry-After": "30" });

  let group: Group | undefined;
  if (body.group_id) {
    group = store.get(String(body.group_id));
    if (!group) return json({ detail: "없는 group_id" }, 404);
    if (group.session !== session) return json({ detail: "다른 세션의 대화" }, 403);
    if (group.running) return json({ detail: "같은 대화를 처리 중이에요." }, 409);
    if (mode === "question" && !group.detail.result) return json({ detail: "설명할 추천 결과가 없어요." }, 409);
    if (targetId && !group.detail.result?.candidates.some((c) => c.id === targetId)) return json({ detail: "없는 target_id" }, 422);
  } else {
    if (mode === "question") return json({ detail: "설명할 추천 결과가 없어요." }, 409);
    const id = randomUUID();
    group = {
      session,
      running: false,
      detail: { group_id: id, title: query.split("\n")[0].slice(0, 40), created_at: now(), updated_at: now(), messages: [], result: null },
    };
    store.set(id, group);
  }

  const g = group;
  const lastAssistant = g.detail.messages.findLast((m) => m.role === "assistant");
  g.detail.messages.push(message("user", query, null, null, []));
  g.running = true;

  const done = respond(query, mode, targetId, g.detail, lastAssistant?.type === "clarify");
  const steps = mode === "question" ? [[4, "답변 생성"]] : done.type === "clarify" || done.type === "reject" ? [[1, "요구사항 분석"]] : [[1, "요구사항 분석"], [2, "모델 검색"], [3, "데이터셋 검색"], [4, "답변 생성"]];

  const encoder = new TextEncoder();
  let cancelled = false;
  const stream = new ReadableStream({
    async start(ctl) {
      const send = (event: string, data: unknown) => {
        if (!cancelled) ctl.enqueue(encoder.encode(`event: ${event}\ndata: ${JSON.stringify(data)}\n\n`));
      };
      try {
        const started = Date.now();
        for (const [step, label] of steps) {
          send("status", { step, total: 4, label, elapsed: (Date.now() - started) / 1000 });
          await sleep(DELAY);
          if (cancelled) return;
        }
        if (query.includes("[오류]")) {
          send("token", { text: "부분 답변이 오다가 " });
          send("error", { code: "AI_UNAVAILABLE", message: "잠시 후 다시 시도해 주세요.", group_id: g.detail.group_id });
          return;
        }
        if (query.includes("[끊김]")) {
          send("token", { text: "부분 답변" });
          return;
        }
        for (const piece of done.answer.match(/[\s\S]{1,12}/g) ?? []) {
          send("token", { text: piece });
          await sleep(40);
        }
        if (cancelled) return;
        done.elapsed = (Date.now() - started) / 1000;
        if (done.history_saved) {
          g.detail.messages.push(message("assistant", done.answer, done.type, done.result, done.sources));
          // Any non-null result is the latest snapshot, even with 0 candidates.
          if (done.result) g.detail.result = done.result;
          g.detail.updated_at = now();
        }
        send("done", done);
      } finally {
        g.running = false;
        if (!cancelled) ctl.close();
      }
    },
    cancel() {
      // Client aborted: like the backend, the current step finishes, nothing more is sent or saved.
      cancelled = true;
    },
  });

  return new Response(stream, {
    headers: { "Content-Type": "text/event-stream", "Cache-Control": "no-cache", "X-Group-Id": g.detail.group_id },
  });
}

function message(role: Message["role"], content: string, type: Message["type"], result: ChatResult | null, sources: Source[]): Message {
  return { id: ++messageId, role, content, type, result, sources, created_at: now() };
}

function respond(query: string, mode: string, targetId: string | null, group: GroupDetail, answeringClarify: boolean): ChatDone {
  const base = { schema_version: 2 as const, group_id: group.group_id, elapsed: 0, sources: [] as Source[], result: null as ChatResult | null, history_saved: !query.includes("[저장실패]") };

  if (mode === "question") {
    const result = group.result ?? BIKE;
    const target = result.candidates.find((c) => c.id === targetId);
    if (!target) {
      const models = result.candidates.filter((c) => c.type === "model").map((c) => c.name);
      return { ...base, type: "answer", answer: `저장된 추천 기준으로 설명할게요.\n\n- 모델 ${models.length}개: ${models.join(", ")}\n- 확인 필요: ${result.needs_check.join(", ") || "없음"}\n\n순위나 후보는 바뀌지 않아요.`, sources: BIKE_SOURCES };
    }
    const lines = target.checks.map((k) => `- **${k.label}**: ${{ ok: "충족", check: "확인 필요", unknown: "미확인" }[k.status]} — ${k.reason}`);
    return {
      ...base,
      type: "answer",
      answer: `**${target.name}**의 저장된 조건 판정이에요.\n\n${lines.join("\n")}\n\n추정 값은 실기기에서 검증되지 않았어요.`,
      sources: BIKE_SOURCES.filter((s) => s.source_id === target.source_id),
    };
  }

  if (query.includes("날씨")) return { ...base, type: "reject", answer: "모델과 데이터를 추천할 수 있는 프로젝트 아이디어로 다시 입력해 주세요." };
  if (!group.result && !answeringClarify && query.includes("따릉이") && !query.includes("[바로]")) {
    return { ...base, type: "clarify", answer: "어떤 기능이 가장 중요한가요? 예: 대여소 추천, 대여·반납량 예측, 경로 추천" };
  }
  if (query.includes("[빈결과]")) {
    return { ...base, type: "answer", answer: "조건에 맞는 후보가 없어요.", result: { title: "후보 없음", summary: ["후보 없음"], needs_check: [], candidates: [], assessment: null } };
  }
  const answer = group.result
    ? `바꾼 조건(“${query}”)을 반영해 다시 추천했어요. 시연 데이터라 후보 구성은 같아요.`
    : `모델 ${BIKE.candidates.filter((c) => c.type === "model").length}개와 데이터 ${BIKE.candidates.filter((c) => c.type === "dataset").length}개를 찾았어요. 후보를 고르면 조건 판정과 근거를 원문과 함께 볼 수 있어요.`;
  return { ...base, type: "answer", answer, result: BIKE, sources: BIKE_SOURCES };
}
