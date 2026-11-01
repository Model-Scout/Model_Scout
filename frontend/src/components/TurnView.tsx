"use client";

import { useState } from "react";
import type { Assessment, Dataset, Datasets, Model, Need, Plan } from "@/lib/api";

export type Turn = {
  request: string;
  steps: string[];
  plan?: Plan;
  clarify?: string[];
  models?: { need: Need; models: Model[] }[];
  datasets?: Datasets;
  assessment?: Assessment;
  answer: string;
  elapsed?: number;
  error?: string;
  running: boolean;
};

const STEP_LABEL: Record<string, string> = {
  decompose: "요청 분석",
  clarify: "추가 질문",
  search_models: "모델 검색",
  search_datasets: "데이터셋 검색",
  assess: "라이선스 판단",
  explain: "답변 작성",
};

const VERDICT_STYLE: Record<string, string> = {
  commercial_ok: "bg-emerald-50 text-emerald-800 border-emerald-200",
  review: "bg-amber-50 text-amber-800 border-amber-200",
  blocked: "bg-red-50 text-red-800 border-red-200",
  runs: "bg-emerald-50 text-emerald-800 border-emerald-200",
  runs_quantized: "bg-amber-50 text-amber-800 border-amber-200",
  too_large: "bg-red-50 text-red-800 border-red-200",
  unknown: "bg-neutral-100 text-neutral-600 border-neutral-200",
};

function Badge({ tone, children }: { tone?: string; children: React.ReactNode }) {
  return (
    <span className={`inline-block rounded border px-1.5 py-0.5 text-xs ${VERDICT_STYLE[tone ?? "unknown"]}`}>
      {children}
    </span>
  );
}

export function TurnView({
  turn,
  selected,
  onToggleModel,
  onAnswer,
}: {
  turn: Turn;
  selected: string[];
  onToggleModel: (id: string) => void;
  onAnswer: (answer: string) => void;
}) {
  return (
    <article className="space-y-5 border-b border-neutral-200 pb-8">
      <p className="rounded-lg bg-neutral-100 px-4 py-3 font-medium">{turn.request}</p>

      <ol className="flex flex-wrap gap-2 text-xs text-neutral-500" aria-label="진행 단계">
        {turn.steps.map((step, i) => (
          <li key={i} className="rounded-full bg-neutral-100 px-2 py-0.5">
            ✓ {STEP_LABEL[step] ?? step}
          </li>
        ))}
        {turn.running && <li className="animate-pulse px-2 py-0.5">진행 중…</li>}
        {turn.elapsed !== undefined && <li className="px-2 py-0.5">{turn.elapsed}s</li>}
      </ol>

      {turn.clarify && <ClarifyForm questions={turn.clarify} onAnswer={onAnswer} />}

      {turn.plan && (
        <section>
          <h3 className="mb-1 text-sm font-semibold text-neutral-500">계획</h3>
          <p>{turn.plan.summary_ko}</p>
        </section>
      )}

      {turn.models?.map((group) => (
        <section key={group.need.task + group.need.model_query}>
          <h3 className="mb-2 text-sm font-semibold text-neutral-500">
            모델 · {group.need.purpose_ko} <span className="font-normal">({group.need.task})</span>
          </h3>
          {group.models.length === 0 && <p className="text-sm text-neutral-500">조건에 맞는 모델이 없습니다.</p>}
          <ul className="grid gap-3 md:grid-cols-2">
            {group.models.map((m) => (
              <ModelCard
                key={m.model_id}
                model={m}
                checked={selected.includes(m.model_id)}
                onToggle={() => onToggleModel(m.model_id)}
              />
            ))}
          </ul>
        </section>
      ))}

      {turn.datasets && <DatasetsView datasets={turn.datasets} />}

      {turn.assessment && (
        <section className={`rounded-lg border p-4 ${VERDICT_STYLE[turn.assessment.license.verdict]}`}>
          <h3 className="font-semibold">{turn.assessment.license.label}</h3>
          <p className="text-sm">{turn.assessment.license.reason}</p>
        </section>
      )}

      {turn.answer && <div className="whitespace-pre-wrap leading-relaxed">{turn.answer}</div>}

      {turn.error && (
        <p role="alert" className="rounded-lg border border-red-200 bg-red-50 p-3 text-sm text-red-800">
          {turn.error}
        </p>
      )}
    </article>
  );
}

function ClarifyForm({ questions, onAnswer }: { questions: string[]; onAnswer: (answer: string) => void }) {
  const [answer, setAnswer] = useState("");
  return (
    <form
      className="space-y-2 rounded-lg border border-blue-200 bg-blue-50 p-4"
      onSubmit={(e) => {
        e.preventDefault();
        if (answer.trim()) onAnswer(answer.trim());
      }}
    >
      <p className="text-sm font-semibold text-blue-900">조금 더 알려주세요</p>
      <ul className="list-disc pl-5 text-sm text-blue-900">
        {questions.map((q) => (
          <li key={q}>{q}</li>
        ))}
      </ul>
      <div className="flex gap-2">
        <input
          aria-label="추가 질문에 대한 답변"
          className="flex-1 rounded border border-blue-200 bg-white px-3 py-2"
          value={answer}
          onChange={(e) => setAnswer(e.target.value)}
        />
        <button className="rounded bg-blue-600 px-4 py-2 text-white disabled:opacity-50" disabled={!answer.trim()}>
          답변
        </button>
      </div>
    </form>
  );
}

function ModelCard({ model, checked, onToggle }: { model: Model; checked: boolean; onToggle: () => void }) {
  return (
    <li className="space-y-2 rounded-lg border border-neutral-200 p-3">
      <div className="flex items-start justify-between gap-2">
        <a href={model.url ?? undefined} target="_blank" rel="noreferrer" className="font-mono text-sm break-all underline">
          {model.model_id}
        </a>
        <label className="flex shrink-0 items-center gap-1 text-xs text-neutral-500">
          <input type="checkbox" checked={checked} onChange={onToggle} />
          비교
        </label>
      </div>
      <div className="flex flex-wrap gap-1">
        <Badge tone={model.commercial_use === "commercial" ? "commercial_ok" : "review"}>{model.license}</Badge>
        {model.parameters_b != null && <Badge>{model.parameters_b}B</Badge>}
        {model.context_length != null && <Badge>ctx {model.context_length.toLocaleString()}</Badge>}
        {model.gpu_fit && <Badge tone={model.gpu_fit.verdict}>GPU: {model.gpu_fit.label}</Badge>}
      </div>
      {model.benchmarks.length > 0 && (
        <ul className="text-xs text-neutral-600">
          {model.benchmarks.map((b, i) => (
            <li key={i}>
              {[b.benchmark, b.dataset, b.metric].filter(Boolean).join(" · ")}: <b>{b.score}</b>
            </li>
          ))}
        </ul>
      )}
      {model.evidence ? (
        <blockquote className="border-l-2 border-neutral-300 pl-2 text-xs text-neutral-600">{model.evidence}</blockquote>
      ) : (
        <p className="text-xs text-neutral-400">모델 카드 근거 없음 (메타데이터만)</p>
      )}
    </li>
  );
}

function DatasetsView({ datasets }: { datasets: Datasets }) {
  const groups: [string, Dataset[]][] = [
    ["학습 데이터", datasets.project_training],
    ["서비스 데이터", datasets.service_data],
    ...Object.entries(datasets.per_model).map(([m, rows]): [string, Dataset[]] => [`${m} 학습 데이터`, rows]),
  ];
  return (
    <>
      {groups
        .filter(([, rows]) => rows.length > 0)
        .map(([title, rows]) => (
          <section key={title}>
            <h3 className="mb-2 text-sm font-semibold text-neutral-500">{title}</h3>
            <ul className="space-y-2">
              {rows.map((d) => (
                <li key={d.dataset} className="rounded-lg border border-neutral-200 p-3 text-sm">
                  <div className="flex flex-wrap items-center gap-2">
                    <a href={d.url} target="_blank" rel="noreferrer" className="font-medium underline">
                      {d.title ?? d.dataset}
                    </a>
                    {d.source && <Badge>{d.source}</Badge>}
                    {d.licenses.map((l) => (
                      <Badge key={l}>{l}</Badge>
                    ))}
                  </div>
                  {d.summary_ko && <p className="mt-1 text-neutral-600">{d.summary_ko}</p>}
                  {d.evidence.slice(0, 2).map((e, i) => (
                    <p key={i} className="mt-1 text-xs text-neutral-500">
                      {e.concept} — {e.source}
                      {e.text && `: ${e.text}`}
                    </p>
                  ))}
                </li>
              ))}
            </ul>
          </section>
        ))}
    </>
  );
}
