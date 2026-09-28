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

create index if not exists model_scout_models_korean_verified_idx
    on public.model_scout_models ((filter_metadata->>'korean_verified'));
create index if not exists model_scout_models_parameter_count_idx
    on public.model_scout_models ((filter_metadata->>'parameter_count_billion'));
create index if not exists model_scout_models_context_length_idx
    on public.model_scout_models ((filter_metadata->>'context_length'));
create index if not exists model_scout_models_popularity_tier_idx
    on public.model_scout_models ((filter_metadata->>'popularity_tier'));

-- Remove the legacy signature so an unfiltered call cannot be selected
-- accidentally by PostgreSQL overload resolution.
drop function if exists public.match_model_scout_models(vector, integer, text);

create or replace function public.match_model_scout_models(
    query_embedding vector(1536),
    match_count integer default 20,
    pool_filter text default null,
    task_filters text[] default null,
    korean_required boolean default false,
    min_parameter_count_billion numeric default null,
    max_parameter_count_billion numeric default null,
    min_context_length integer default null,
    max_context_length integer default null,
    require_known_parameters boolean default false,
    require_known_context boolean default false,
    popularity_tier_filter text default null,
    query_text text default null,
    dense_weight real default 0.65,
    sparse_weight real default 0.35
)
returns table (
    model_id text,
    source_pool text,
    candidate jsonb,
    task jsonb,
    language jsonb,
    popularity jsonb,
    family jsonb,
    filter_metadata jsonb,
    technical_metadata jsonb,
    semantic_metadata jsonb,
    evidence jsonb,
    benchmark_metadata jsonb,
    source_provenance jsonb,
    task_consistency jsonb,
    evidence_index jsonb,
    dense_similarity real,
    sparse_score real,
    similarity real
)
language sql
stable
as $$
with scored as (
    select
        m.model_id,
        m.source_pool,
        m.candidate,
        m.task,
        m.language,
        m.popularity,
        m.family,
        m.filter_metadata,
        m.technical_metadata,
        m.semantic_metadata,
        m.evidence,
        m.benchmark_metadata,
        m.source_provenance,
        m.task_consistency,
        coalesce(e.parents, '[]'::jsonb) as evidence_index,
        (1 - (m.embedding <=> query_embedding))::real as dense_similarity,
        least(
            1.0,
            ts_rank_cd(
                (
                    setweight(to_tsvector('simple', coalesce(m.model_id, '')), 'A') ||
                    setweight(to_tsvector('simple', coalesce(m.filter_metadata->>'translation_pairs', '')), 'A') ||
                    setweight(to_tsvector('simple', coalesce(m.filter_metadata->>'search_aliases', '')), 'A') ||
                    setweight(to_tsvector('simple', coalesce(m.task::text, '')), 'B') ||
                    setweight(to_tsvector('simple', coalesce(m.language::text, '')), 'B') ||
                    setweight(to_tsvector('simple', coalesce(m.filter_metadata::text, '')), 'C') ||
                    setweight(to_tsvector('simple', coalesce(m.benchmark_metadata::text, '')), 'C') ||
                    setweight(to_tsvector('simple', coalesce(m.technical_metadata::text, '') || coalesce(m.semantic_metadata::text, '')), 'D')
                ),
                plainto_tsquery('simple', coalesce(query_text, ''))
            )::real
        )::real as sparse_score
    from public.model_scout_models as m
    left join public.model_scout_evidence as e
      on e.model_id = m.model_id and e.active = true
    where m.active = true
      and (pool_filter is null or m.source_pool = pool_filter)
      and (
          task_filters is null
          or cardinality(task_filters) = 0
          or m.task->>'primary' = any(task_filters)
          or exists (
              select 1
              from jsonb_array_elements_text(coalesce(m.task->'matched', '[]'::jsonb)) as matched(value)
              where matched.value = any(task_filters)
          )
      )
      and (not korean_required or m.filter_metadata->>'korean_verified' = 'true')
      and (
          not require_known_parameters
          or jsonb_typeof(m.filter_metadata->'parameter_count_billion') = 'number'
      )
      and (
          not require_known_context
          or jsonb_typeof(m.filter_metadata->'context_length') = 'number'
      )
      and (
          min_parameter_count_billion is null
          or (m.filter_metadata->>'parameter_count_billion')::numeric >= min_parameter_count_billion
      )
      and (
          max_parameter_count_billion is null
          or (m.filter_metadata->>'parameter_count_billion')::numeric <= max_parameter_count_billion
      )
      and (
          min_context_length is null
          or (m.filter_metadata->>'context_length')::integer >= min_context_length
      )
      and (
          max_context_length is null
          or (m.filter_metadata->>'context_length')::integer <= max_context_length
      )
      and (
          popularity_tier_filter is null
          or m.filter_metadata->>'popularity_tier' = popularity_tier_filter
      )
)
select
    scored.model_id,
    scored.source_pool,
    scored.candidate,
    scored.task,
    scored.language,
    scored.popularity,
    scored.family,
    scored.filter_metadata,
    scored.technical_metadata,
    scored.semantic_metadata,
    scored.evidence,
    scored.benchmark_metadata,
    scored.source_provenance,
    scored.task_consistency,
    scored.evidence_index,
    scored.dense_similarity,
    scored.sparse_score,
    (
        greatest(dense_weight, 0.0) * scored.dense_similarity +
        greatest(sparse_weight, 0.0) * scored.sparse_score
    )::real as similarity
from scored
order by similarity desc, scored.model_id
limit least(greatest(match_count, 1), 100);
$$;
