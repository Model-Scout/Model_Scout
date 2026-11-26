import type { Candidate, ChatDone, ChatResult, Display, Pipeline } from "./api";

const STATUS = { ok: "충족", check: "확인 필요", unknown: "미확인" } as const;

type RequirementTurn = {
  role: "user" | "assistant";
  content: string;
  type?: ChatDone["type"] | null;
  display?: Display;
};

/** Older snapshots only have message history. Take inputs paired with completed recommendations. */
function savedRequirements(turns: RequirementTurn[]): string[] {
  const requests: string[] = [];
  let userInput = "";
  let pending: string[] = [];
  let question = "";
  for (const turn of turns) {
    if (turn.role === "user") {
      userInput = turn.content;
      continue;
    }
    if (turn.type === "clarify" || turn.display === "recommendation") {
      if (userInput) pending.push(question ? `(질문) ${question}\n(답변) ${userInput}` : userInput);
      if (turn.display === "recommendation") {
        requests.push(...pending);
        pending = [];
        question = "";
      } else {
        question = turn.content;
      }
    }
    userInput = "";
  }
  const first = turns.find((turn) => turn.role === "user")?.content;
  return requests.length ? requests : first ? [first] : [];
}

/** SPEC.md text built from the recommendation itself, so a re-recommendation rewrites it with no extra LLM call. */
export function buildSpec(result: ChatResult, turns: RequirementTurn[], pipeline: Pipeline | null): string {
  const requirements = result.requirements?.length ? result.requirements : savedRequirements(turns);
  const byId = new Map(result.candidates.map((c) => [c.id, c]));
  const usedIds = new Set(pipeline?.nodes.flatMap((node) => node.candidate_id ? [node.candidate_id] : []));
  const used = [...usedIds].map((id) => byId.get(id)).filter((c): c is Candidate => c !== undefined);
  const parts = used.length > 0 ? used : result.candidates.filter((c) => c.type === "model" && c.group !== "sft").slice(0, 3);
  const dataCandidates = result.candidates.filter((c) => c.type === "dataset" && !usedIds.has(c.id));
  const label = new Map((pipeline?.nodes ?? []).map((n) => [n.id, n.label]));
  const guide = result.assessment?.implementation_guide;

  const part = (c: Candidate) => [
    `### ${c.name} (${c.type === "model" ? "모델" : "데이터"})`,
    `- ID: \`${c.source_id}\`${c.url ? ` · ${c.url}` : ""}`,
    `- 역할: ${c.role}`,
    ...(c.context_length ? [`- 최대 입력 길이: ${c.context_length.toLocaleString("ko-KR")} tokens`] : []),
    ...(c.parameters_b ? [`- 파라미터: ${c.parameters_b}B`] : []),
    ...c.checks.map((k) => `- ${k.label}: ${STATUS[k.status]} — ${k.reason}${k.quote && k.quote !== k.reason ? ` · “${k.quote}”` : ""}`),
  ].join("\n");

  return [
    `# ${result.title || "서비스"} 구현 명세`,
    requirements.length > 0 && `## 요구사항\n${requirements.map((text, index) =>
      `${index + 1}. ${text.replace(/\r?\n/g, "\n   ")}`,
    ).join("\n")}`,
    result.summary.length > 0 && `## 요약\n${result.summary.map((s) => `- ${s}`).join("\n")}`,
    pipeline && `## 처리 흐름\n${pipeline.nodes.map((n, i) => `${i + 1}. ${n.label}${n.note ? ` — ${n.note}` : ""}`).join("\n")}\n\n연결:\n${pipeline.edges
      .map((e) => `- ${label.get(e.source) ?? e.source} → ${label.get(e.target) ?? e.target}${e.label ? ` (${e.label})` : ""}`)
      .join("\n")}`,
    (result.combination ?? []).length > 0 && `## 조합 방법\n${result.combination!.map((s) => `- ${s}`).join("\n")}`,
    parts.length > 0 && `## 사용 모델·데이터\n${parts.map(part).join("\n\n")}`,
    dataCandidates.length > 0 && `## ${used.length ? "추가 데이터 후보" : "추천 데이터 후보"}\n${dataCandidates.map(part).join("\n\n")}`,
    (guide?.structured_output || guide?.fine_tuning) &&
      `## 구현 가이드\n${[guide.structured_output && `- 구조화 출력: ${guide.structured_output}`, guide.fine_tuning && `- 추가 학습: ${guide.fine_tuning}`].filter(Boolean).join("\n")}`,
    result.needs_check.length > 0 && `## 직접 확인할 것\n${result.needs_check.map((s) => `- ${s}`).join("\n")}`,
  ].filter(Boolean).join("\n\n");
}

/** Self-contained: the spec rides inside the prompt, so the agent needs no file the user may not have saved. */
export const buildPrompt = (spec: string) => `아래 명세대로 이 서비스의 동작하는 첫 버전(MVP)을 지금 바로 만들어 줘. 중간에 확인 질문 없이 끝까지 진행해.
- 요구사항은 입력 순서대로 읽고, 조건이 충돌하면 최근에 명시한 조건을 우선해.
- 처리 흐름의 단계를 코드 구조(함수·모듈)로 옮기고, 채택한 모델·데이터는 명세의 ID와 출처를 그대로 써. 다른 모델로 바꾸지 마. 데이터 후보는 역할과 제공 범위를 보고 필요한 것만 골라.
- 언어·프레임워크는 요구사항의 실행 환경에 맞게 네가 정해. 모델이 그 환경에서 무거우면 같은 ID를 Hugging Face Inference API 등으로 호출하는 방식을 택해.
- '확인 필요'·'미확인' 조건(라이선스, GPU 메모리 등)은 README의 "출시 전 확인할 것"에 정리하고 구현은 계속해.
- 완료 기준: 명령 하나로 실행되고, 샘플 입력 하나로 처리 흐름 전체가 돌아가는 것을 직접 확인해. 명세는 SPEC.md, 실행 방법·필요한 키·샘플 실행 결과는 README에 적어.

---

${spec}`;
