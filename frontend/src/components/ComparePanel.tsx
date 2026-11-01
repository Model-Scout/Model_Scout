"use client";

import { useState } from "react";
import { compareModels, type CompareRow } from "@/lib/api";

export function ComparePanel({ ids, onClear }: { ids: string[]; onClear: () => void }) {
  const [gpuGb, setGpuGb] = useState("");
  const [rows, setRows] = useState<CompareRow[] | null>(null);
  const [missing, setMissing] = useState<string[]>([]);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function run() {
    setLoading(true);
    setError("");
    try {
      const result = await compareModels(ids, Number(gpuGb) || undefined);
      setRows(result.models);
      setMissing(result.missing);
    } catch (e) {
      setError(String(e instanceof Error ? e.message : e));
    } finally {
      setLoading(false);
    }
  }

  return (
    <section className="space-y-3 rounded-lg border border-neutral-200 p-4">
      <div className="flex flex-wrap items-center gap-2">
        <h2 className="font-semibold">모델 비교 ({ids.length}/3)</h2>
        <span className="text-sm text-neutral-500">{ids.join(", ")}</span>
      </div>
      <div className="flex flex-wrap items-center gap-2">
        <label className="flex items-center gap-1 text-sm">
          GPU 메모리(GB)
          <input
            type="number"
            min={1}
            max={1024}
            className="w-20 rounded border border-neutral-300 px-2 py-1"
            value={gpuGb}
            onChange={(e) => setGpuGb(e.target.value)}
          />
        </label>
        <button
          className="rounded bg-neutral-900 px-3 py-1.5 text-sm text-white disabled:opacity-50"
          disabled={ids.length < 2 || loading}
          onClick={run}
        >
          {loading ? "비교 중…" : "비교"}
        </button>
        <button className="text-sm text-neutral-500 underline" onClick={onClear}>
          선택 해제
        </button>
      </div>
      {ids.length < 2 && <p className="text-sm text-neutral-500">결과 카드에서 모델을 2~3개 선택하세요.</p>}
      {error && (
        <p role="alert" className="text-sm text-red-700">
          {error}
        </p>
      )}
      {missing.length > 0 && <p className="text-sm text-amber-700">찾지 못한 모델: {missing.join(", ")}</p>}
      {rows && (
        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="text-neutral-500">
              <tr>
                {["모델", "task", "크기", "context", "라이선스", "양자화", "GPU", "벤치마크"].map((h) => (
                  <th key={h} className="border-b border-neutral-200 px-2 py-1 font-medium">
                    {h}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {rows.map((r) => (
                <tr key={r.model_id} className="align-top">
                  <td className="border-b border-neutral-100 px-2 py-1 font-mono break-all">{r.model_id}</td>
                  <td className="border-b border-neutral-100 px-2 py-1">{r.task ?? "-"}</td>
                  <td className="border-b border-neutral-100 px-2 py-1">{r.parameters_b != null ? `${r.parameters_b}B` : "-"}</td>
                  <td className="border-b border-neutral-100 px-2 py-1">{r.context_length?.toLocaleString() ?? "-"}</td>
                  <td className="border-b border-neutral-100 px-2 py-1">{r.license}</td>
                  <td className="border-b border-neutral-100 px-2 py-1">{r.quantization ?? "-"}</td>
                  <td className="border-b border-neutral-100 px-2 py-1">{r.gpu_fit?.label ?? "-"}</td>
                  <td className="border-b border-neutral-100 px-2 py-1 text-xs">
                    {r.benchmarks.map((b, i) => (
                      <div key={i}>
                        {b.benchmark ?? b.dataset}: {b.score}
                      </div>
                    ))}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </section>
  );
}
