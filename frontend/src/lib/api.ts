// Shapes mirror backend/app/main.py (SSE events) and ai/17_recommend_graph.py (node outputs).

export const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

export type GpuFit = {
  verdict: "runs" | "runs_quantized" | "too_large" | "unknown";
  label: string;
  precision: string | null;
  needed_gib: number | null;
} | null;

export type Benchmark = { benchmark: string | null; dataset: string | null; metric: string | null; score: number | null };

export type Model = {
  model_id: string;
  rank_score: number;
  task: string | null;
  license: string;
  commercial_use: string | null;
  context_length: number | null;
  parameters_b: number | null;
  quant_bits: number | null;
  benchmarks: Benchmark[];
  evidence: string | null;
  url: string | null;
  gpu_fit: GpuFit;
};

export type Need = { task: string; purpose_ko: string; model_query: string };

export type Plan = {
  summary_ko: string;
  needs: Need[];
  constraints: {
    commercial_only: boolean;
    gpu_memory_gb: number | null;
    max_parameter_count_billion: number | null;
    min_context_length: number | null;
  };
  dataset_terms: string[];
  dataset_query: string;
  clarifying_questions: string[];
};

export type Dataset = {
  dataset: string;
  title: string | null;
  source: string | null;
  score: number;
  reasons: string[];
  downloads: number | null;
  url: string;
  summary_ko: string | null;
  licenses: string[];
  evidence: { concept: string; source: string; text: string | null }[];
};

export type Datasets = {
  per_model: Record<string, Dataset[]>;
  project_training: Dataset[];
  service_data: Dataset[];
};

export type LicenseItem = { kind: string; id: string; license: string | string[]; class: string };

export type Assessment = {
  license: {
    verdict: "commercial_ok" | "review" | "blocked";
    label: string;
    reason: string;
    blockers: LicenseItem[];
    review: LicenseItem[];
  };
  gpu_memory_gb: number | null;
};

export type StreamEvent =
  | { event: "status"; data: { node: string; elapsed: number } }
  | { event: "plan"; data: Plan }
  | { event: "clarify"; data: { questions: string[]; thread_id: string } }
  | { event: "models"; data: { need: Need; models: Model[] }[] }
  | { event: "datasets"; data: Datasets }
  | { event: "assessment"; data: Assessment }
  | { event: "token"; data: { text: string } }
  | { event: "done"; data: { thread_id: string; elapsed: number } }
  | { event: "error"; data: { message: string } };

export type RecommendBody = { message?: string; answer?: string; thread_id?: string };

// EventSource cannot POST, so the stream is read from fetch and split on blank lines.
export async function streamRecommend(
  body: RecommendBody,
  onEvent: (event: StreamEvent) => void,
  signal?: AbortSignal,
): Promise<void> {
  const res = await fetch(`${API_URL}/api/recommend`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(body),
    signal,
  });
  if (!res.ok || !res.body) throw new Error(await errorMessage(res));

  const reader = res.body.pipeThrough(new TextDecoderStream()).getReader();
  let buffer = "";
  for (;;) {
    const { value, done } = await reader.read();
    if (done) return;
    buffer += value;
    let end;
    while ((end = buffer.indexOf("\n\n")) >= 0) {
      const chunk = buffer.slice(0, end);
      buffer = buffer.slice(end + 2);
      let event = "message";
      let data = "";
      for (const line of chunk.split("\n")) {
        if (line.startsWith("event: ")) event = line.slice(7);
        else if (line.startsWith("data: ")) data += line.slice(6);
      }
      if (data) onEvent({ event, data: JSON.parse(data) } as StreamEvent);
    }
  }
}

export type CompareRow = {
  model_id: string;
  task: string | null;
  parameters_b: number | null;
  context_length: number | null;
  license: string;
  license_class: string;
  downloads: number | null;
  quantization: string | null;
  gpu_fit: GpuFit;
  benchmarks: Benchmark[];
  url: string | null;
};

export async function compareModels(
  ids: string[],
  gpuGb?: number,
): Promise<{ models: CompareRow[]; missing: string[] }> {
  const params = new URLSearchParams({ models: ids.join(",") });
  if (gpuGb) params.set("gpu_gb", String(gpuGb));
  const res = await fetch(`${API_URL}/api/compare?${params}`);
  if (!res.ok) throw new Error(await errorMessage(res));
  return res.json();
}

async function errorMessage(res: Response): Promise<string> {
  try {
    const body = await res.json();
    return typeof body.detail === "string" ? body.detail : JSON.stringify(body.detail ?? body);
  } catch {
    return `HTTP ${res.status}`;
  }
}
