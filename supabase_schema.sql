-- Model Scout production storage.
-- Stores only the Core and Low Popularity recommendation corpus.
-- Apply with the Supabase SQL editor or 08_sync_supabase.py --apply.

-- pgvector is enabled once in Supabase project settings; the sync script verifies it.

create table if not exists public.model_scout_sync_runs (
    run_id uuid primary key,
    status text not null check (status in ('running', 'completed', 'failed')),
    started_at timestamptz not null default now(),
    completed_at timestamptz,
    stage_versions jsonb not null default '{}'::jsonb,
    row_count integer not null default 0,
    error text
);

create table if not exists public.model_scout_models (
    model_id text primary key,
    source_pool text not null check (source_pool in ('core', 'low_popularity')),
    source_stage1_version integer not null,
    source_stage2_version integer not null,
    source_stage3_version integer not null,
    source_stage4_version integer not null,
    candidate jsonb not null default '{}'::jsonb,
    task jsonb not null default '{}'::jsonb,
    language jsonb not null default '{}'::jsonb,
    popularity jsonb not null default '{}'::jsonb,
    family jsonb not null default '{}'::jsonb,
    filter_metadata jsonb not null default '{}'::jsonb,
    technical_metadata jsonb not null default '{}'::jsonb,
    semantic_metadata jsonb not null default '{}'::jsonb,
    evidence jsonb not null default '{}'::jsonb,
    benchmark_metadata jsonb not null default '{}'::jsonb,
    source_provenance jsonb not null default '{}'::jsonb,
    task_consistency jsonb not null default '{}'::jsonb,
    document_hash text,
    embedding_model text not null,
    embedding_dimensions integer not null,
    embedding vector(1536) not null,
    last_seen_run uuid references public.model_scout_sync_runs(run_id),
    active boolean not null default true,
    refreshed_at timestamptz not null default now(),
    stale_at timestamptz,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

-- One row per model containing the Stage 3 Parent–Child evidence sidecar.
-- The model table remains the retrieval index; this table stores the full
-- parent text and child evidence used when building grounded responses.
create table if not exists public.model_scout_evidence (
    model_id text primary key references public.model_scout_models(model_id) on delete cascade,
    source_pool text not null check (source_pool in ('core', 'low_popularity')),
    source_stage3_version integer not null,
    schema_version integer not null,
    evidence_index_version integer not null,
    source_stage3_hash text not null,
    parent_count integer not null default 0,
    child_count integer not null default 0,
    parents jsonb not null default '[]'::jsonb,
    last_seen_run uuid references public.model_scout_sync_runs(run_id),
    active boolean not null default true,
    refreshed_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);

create index if not exists model_scout_evidence_pool_active_idx
    on public.model_scout_evidence (source_pool, active);

alter table public.model_scout_evidence enable row level security;

do $$
begin
    if not exists (
        select 1 from pg_policies
        where schemaname = 'public'
          and tablename = 'model_scout_evidence'
          and policyname = 'model_scout_evidence_public_read'
    ) then
        create policy model_scout_evidence_public_read
            on public.model_scout_evidence
            for select
            to anon, authenticated
            using (active = true);
    end if;
end
$$;

create index if not exists model_scout_models_pool_active_idx
    on public.model_scout_models (source_pool, active);
create index if not exists model_scout_models_candidate_type_idx
    on public.model_scout_models ((candidate->>'type'));
create index if not exists model_scout_models_primary_task_idx
    on public.model_scout_models ((task->>'primary'));
create index if not exists model_scout_models_embedding_hnsw_idx
    on public.model_scout_models using hnsw (embedding vector_cosine_ops);

alter table public.model_scout_models enable row level security;

do $$
begin
    if not exists (
        select 1 from pg_policies
        where schemaname = 'public'
          and tablename = 'model_scout_models'
          and policyname = 'model_scout_models_public_read'
    ) then
        create policy model_scout_models_public_read
            on public.model_scout_models
            for select
            to anon, authenticated
            using (active = true);
    end if;
end
$$;

create or replace function public.match_model_scout_models(
    query_embedding vector(1536),
    match_count integer default 20,
    pool_filter text default null
)
returns table (
    model_id text,
    source_pool text,
    candidate jsonb,
    task jsonb,
    language jsonb,
    popularity jsonb,
    filter_metadata jsonb,
    technical_metadata jsonb,
    semantic_metadata jsonb,
    evidence jsonb,
    benchmark_metadata jsonb,
    similarity real
)
language sql
stable
as $$
    select
        m.model_id,
        m.source_pool,
        m.candidate,
        m.task,
        m.language,
        m.popularity,
        m.filter_metadata,
        m.technical_metadata,
        m.semantic_metadata,
        m.evidence,
        m.benchmark_metadata,
        (1 - (m.embedding <=> query_embedding))::real as similarity
    from public.model_scout_models as m
    where m.active = true
      and (pool_filter is null or m.source_pool = pool_filter)
    order by m.embedding <=> query_embedding
    limit least(greatest(match_count, 1), 100);
$$;
