-- Speed up public.match_model_scout_models and halve its vector storage.
--
-- 1. search_tsv: the full-text vector, stored instead of rebuilt per row on every call.
-- 2. embedding vector(1536) -> halfvec(1536): every stored value is already exactly
--    representable in fp16 (measured: 0 values change, top-5/10/20 identical over 300 queries),
--    so rankings and scores are bit-identical; vectors and the HNSW index take half the space.
--    08_sync_supabase.py keeps inserting %s::vector (implicit vector->halfvec cast), and the
--    function keeps its vector(1536) parameter, so 09 and the CI need no change.
--
-- The function rebuilt to_tsvector over every model's JSON metadata on each call: 16.6 s of a
-- 7-17 s search (measured 2026-11-01, 3,872 active models). Storing the identical expression as
-- a generated column makes ranking a per-row ts_rank_cd on a ready vector. Results are unchanged
-- (same expression, same weights); 08_sync_supabase.py needs no change because Postgres fills
-- the column on insert/update. Cost: ~29 MB (avg 7.4 KB per model).
--
-- Rollback: restore the previous function body from git history of supabase_schema.sql, then
--   alter table public.model_scout_models drop column search_tsv;
--   alter table public.model_scout_models alter column embedding type vector(1536) using embedding::vector(1536);
--   (and recreate the HNSW index with vector_cosine_ops)

alter table public.model_scout_models
    add column if not exists search_tsv tsvector generated always as (
        setweight(to_tsvector('simple', coalesce(model_id, '')), 'A') ||
        setweight(to_tsvector('simple', coalesce(filter_metadata->>'translation_pairs', '')), 'A') ||
        setweight(to_tsvector('simple', coalesce(filter_metadata->>'search_aliases', '')), 'A') ||
        setweight(to_tsvector('simple', coalesce(task::text, '')), 'B') ||
        setweight(to_tsvector('simple', coalesce(language::text, '')), 'B') ||
        setweight(to_tsvector('simple', coalesce(filter_metadata::text, '')), 'C') ||
        setweight(to_tsvector('simple', coalesce(benchmark_metadata::text, '')), 'C') ||
        setweight(to_tsvector('simple', coalesce(technical_metadata::text, '') || coalesce(semantic_metadata::text, '')), 'D')
    ) stored;

drop index if exists public.model_scout_models_embedding_hnsw_idx;
alter table public.model_scout_models
    alter column embedding type halfvec(1536) using embedding::halfvec(1536);
create index if not exists model_scout_models_embedding_hnsw_idx
    on public.model_scout_models using hnsw (embedding halfvec_cosine_ops);

-- Same function: reads the stored tsvector, compares in halfvec. Parameters are unchanged.
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
        (1 - (m.embedding <=> query_embedding::halfvec(1536)))::real as dense_similarity,
        least(
            1.0,
            ts_rank_cd(
                m.search_tsv,
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
