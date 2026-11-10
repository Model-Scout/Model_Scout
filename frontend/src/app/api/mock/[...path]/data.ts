// Demo data in the V2 contract shape (backend/app/result.py). Fictional demo content, not verified model facts.
import type { Candidate, ChatResult, Source } from "@/lib/api";

const model = (c: Partial<Candidate> & Pick<Candidate, "source_id" | "name" | "role" | "checks">): Candidate => ({
  id: `model:${c.source_id}`,
  type: "model",
  tags: [],
  source: "Hugging Face",
  url: `https://huggingface.co/${c.source_id}`,
  evidence: [],
  related: [],
  rank_score: null,
  context_length: null,
  parameters_b: null,
  benchmarks: [],
  gpu_fit: null,
  ...c,
});

const dataset = (c: Partial<Candidate> & Pick<Candidate, "source_id" | "name" | "role" | "checks" | "source">): Candidate => ({
  id: `dataset:${c.source_id}`,
  type: "dataset",
  tags: [],
  url: null,
  evidence: [],
  related: [],
  rank_score: null,
  context_length: null,
  parameters_b: null,
  benchmarks: [],
  gpu_fit: null,
  ...c,
});

const local = { key: "execution", label: "로컬 실행", status: "unknown", reason: "원문에서 관련 근거를 찾지 못했어요.", source_id: null, quote: null, origin: "unknown" } as const;

export const BIKE: ChatResult = {
  title: "따릉이 주차 경로 추천",
  summary: ["따릉이 주차 경로 추천", "언어: 한국어", "실행: 로컬 GPU 8GB", "데이터: 대여소 위치·이용량", "기능: 경로 추천"],
  needs_check: ["BGE-M3: GPU 메모리", "Qwen3-8B: GPU 메모리"],
  candidates: [
    model({
      source_id: "BAAI/bge-m3",
      name: "BGE-M3",
      role: "대여소 주변 장소·코스 설명을 의미로 검색",
      tags: ["Embedding", "sentence-transformers", "multilingual"],
      rank_score: 0.91,
      context_length: 8192,
      parameters_b: 0.568,
      benchmarks: [{ benchmark: "MIRACL", dataset: "ko", metric: "nDCG@10", score: 72.1 }],
      gpu_fit: { verdict: "runs", label: "8GB에서 실행 가능(추정)", precision: "FP32", needed_gib: 2.3 },
      related: ["dataset:seoul/bike-stations"],
      checks: [
        { key: "language", label: "한국어 지원", status: "ok", reason: "다국어 지원을 README에 명시", source_id: "BAAI/bge-m3", quote: "It can support more than 100 working languages.", origin: "readme" },
        { key: "license", label: "상업적 이용", status: "ok", reason: "License: apache-2.0", source_id: "BAAI/bge-m3", quote: "License: apache-2.0", origin: "metadata" },
        { key: "context", label: "입력 길이", status: "ok", reason: "최대 8,192 tokens", source_id: "BAAI/bge-m3", quote: "long documents of up to 8192 tokens.", origin: "readme" },
        { key: "gpu", label: "GPU 메모리", status: "check", reason: "파라미터 568M 기준 약 2.3GB 추정(FP32) · 원문에 명시 없음", source_id: "BAAI/bge-m3", quote: null, origin: "estimate" },
        local,
      ],
    }),
    model({
      source_id: "Qwen/Qwen3-8B",
      name: "Qwen3-8B",
      role: "요청 해석 · 추천 이유 설명",
      tags: ["LLM", "text-generation"],
      rank_score: 0.84,
      context_length: 32768,
      parameters_b: 8.2,
      gpu_fit: { verdict: "runs_quantized", label: "4bit 양자화 시 실행 가능(추정)", precision: "INT4", needed_gib: 5.1 },
      related: ["dataset:data-go-kr/bike-roads"],
      checks: [
        { key: "language", label: "한국어 지원", status: "ok", reason: "100개 이상 언어 지원을 README에 명시", source_id: "Qwen/Qwen3-8B", quote: "support of 100+ languages and dialects", origin: "readme" },
        { key: "license", label: "상업적 이용", status: "ok", reason: "License: apache-2.0", source_id: "Qwen/Qwen3-8B", quote: "License: apache-2.0", origin: "metadata" },
        { key: "context", label: "입력 길이", status: "ok", reason: "최대 32,768 tokens", source_id: "Qwen/Qwen3-8B", quote: null, origin: "metadata" },
        { key: "gpu", label: "GPU 메모리", status: "check", reason: "BF16 약 16.4GB 추정으로 8GB 초과 · 4bit 양자화 필요", source_id: "Qwen/Qwen3-8B", quote: null, origin: "estimate" },
        local,
      ],
    }),
    model({
      source_id: "google/timesfm-2.5-200m-pytorch",
      name: "TimesFM-2.5-200M",
      role: "대여소별 대여·반납량 예측",
      tags: ["TSM", "time-series-forecasting"],
      rank_score: 0.77,
      context_length: 16384,
      parameters_b: 0.2,
      gpu_fit: { verdict: "runs", label: "8GB에서 실행 가능(추정)", precision: "FP32", needed_gib: 0.8 },
      related: ["dataset:seoul/bike-usage"],
      checks: [
        { key: "language", label: "한국어 지원", status: "unknown", reason: "시계열 모델이라 언어 지원 근거가 없어요.", source_id: null, quote: null, origin: "unknown" },
        { key: "license", label: "상업적 이용", status: "ok", reason: "License: apache-2.0", source_id: "google/timesfm-2.5-200m-pytorch", quote: "License: apache-2.0", origin: "metadata" },
        { key: "gpu", label: "GPU 메모리", status: "ok", reason: "파라미터 200M 기준 약 0.8GB 추정", source_id: "google/timesfm-2.5-200m-pytorch", quote: null, origin: "estimate" },
        local,
      ],
    }),
    model({
      source_id: "BAAI/bge-reranker-v2-m3",
      name: "bge-reranker-v2-m3",
      role: "검색 결과 재정렬",
      tags: ["Reranker"],
      rank_score: 0.72,
      parameters_b: 0.568,
      gpu_fit: { verdict: "runs", label: "8GB에서 실행 가능(추정)", precision: "FP32", needed_gib: 2.3 },
      checks: [
        { key: "language", label: "한국어 지원", status: "ok", reason: "다국어 리랭커로 README에 명시", source_id: "BAAI/bge-reranker-v2-m3", quote: "multilingual capabilities", origin: "readme" },
        { key: "license", label: "상업적 이용", status: "ok", reason: "License: apache-2.0", source_id: "BAAI/bge-reranker-v2-m3", quote: "License: apache-2.0", origin: "metadata" },
        { key: "gpu", label: "GPU 메모리", status: "ok", reason: "약 2.3GB 추정(FP32)", source_id: "BAAI/bge-reranker-v2-m3", quote: null, origin: "estimate" },
        local,
      ],
    }),
    dataset({
      source_id: "seoul/bike-stations",
      name: "서울시 공공자전거 대여소 정보",
      role: "대여소 위치 · 거치대 수",
      source: "서울 열린데이터광장",
      tags: ["공공"],
      url: "https://data.seoul.go.kr/",
      related: ["model:BAAI/bge-m3"],
      evidence: [{ label: "대여소 위치", text: "대여소 번호, 대여소명, 위도, 경도, 거치대 수를 제공합니다.", origin: "readme" }],
      checks: [{ key: "license", label: "라이선스", status: "check", reason: "공공누리 제1유형 · 라이선스 이름만으로 상업 이용을 확정할 수 없어요.", source_id: "seoul/bike-stations", quote: "공공누리 제1유형", origin: "metadata" }],
    }),
    dataset({
      source_id: "seoul/bike-usage",
      name: "서울시 공공자전거 이용정보",
      role: "시간대별 대여·반납 기록",
      source: "서울 열린데이터광장",
      tags: ["공공"],
      url: "https://data.seoul.go.kr/",
      related: ["model:google/timesfm-2.5-200m-pytorch"],
      evidence: [{ label: "이용량", text: "대여소별 대여 건수와 반납 건수를 시간 단위로 제공합니다.", origin: "readme" }],
      checks: [{ key: "license", label: "라이선스", status: "check", reason: "공공누리 제1유형 · 라이선스 이름만으로 상업 이용을 확정할 수 없어요.", source_id: "seoul/bike-usage", quote: null, origin: "metadata" }],
    }),
    dataset({
      source_id: "data-go-kr/bike-roads",
      name: "전국 자전거도로 표준데이터",
      role: "경로 후보가 될 자전거도로",
      source: "공공데이터포털",
      tags: ["공공"],
      url: "https://www.data.go.kr/",
      related: ["model:Qwen/Qwen3-8B"],
      evidence: [{ label: "자전거도로", text: null, origin: "metadata" }],
      checks: [{ key: "license", label: "라이선스", status: "unknown", reason: "라이선스 정보를 찾지 못했어요.", source_id: "data-go-kr/bike-roads", quote: null, origin: "unknown" }],
    }),
  ],
  assessment: null,
};

/** Sources of the recommendation, built from the quoted checks and dataset evidence. */
export const BIKE_SOURCES: Source[] = BIKE.candidates.flatMap((c) => [
  ...c.checks
    .filter((k) => k.quote && k.origin !== "metadata")
    .map((k) => ({ source_id: c.source_id, kind: c.type, title: c.name, url: c.url, quote: k.quote, origin: k.origin, location: null })),
  ...c.evidence
    .filter((e) => e.text)
    .map((e) => ({ source_id: c.source_id, kind: c.type, title: c.name, url: c.url, quote: e.text, origin: e.origin, location: null })),
]);

/** README bodies for the file viewer. Quotes above appear verbatim. bike-roads is missing on purpose (404 path). */
export const READMES: Record<string, string> = {
  "model:BAAI/bge-m3": `# BGE-M3\n\n시연용 README입니다.\n\n## Introduction\n\nBGE-M3 is a versatile embedding model.\n\n- **Multi-Linguality**: It can support more than 100 working languages.\n- **Multi-Granularity**: It is able to process inputs of different granularities, spanning from short sentences to long documents of up to 8192 tokens.\n\n| 항목 | 값 |\n| --- | --- |\n| Parameters | 568M |\n| License | apache-2.0 |\n`,
  "model:Qwen/Qwen3-8B": `# Qwen3-8B\n\n시연용 README입니다.\n\n## Highlights\n\n- Expertise in agent capabilities.\n- Strong support of 100+ languages and dialects.\n\nContext length: 32,768 natively.\n`,
  "model:google/timesfm-2.5-200m-pytorch": `# TimesFM 2.5\n\n시연용 README입니다. Time series foundation model for forecasting.\n`,
  "model:BAAI/bge-reranker-v2-m3": `# bge-reranker-v2-m3\n\n시연용 README입니다. Lightweight reranker with strong multilingual capabilities.\n`,
  "dataset:seoul/bike-stations": `# 서울시 공공자전거 대여소 정보\n\n시연용 설명입니다.\n\n대여소 번호, 대여소명, 위도, 경도, 거치대 수를 제공합니다.\n\n이용허락: 공공누리 제1유형\n`,
  "dataset:seoul/bike-usage": `# 서울시 공공자전거 이용정보\n\n시연용 설명입니다.\n\n대여소별 대여 건수와 반납 건수를 시간 단위로 제공합니다.\n`,
};
