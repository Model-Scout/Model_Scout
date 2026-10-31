-- Model Scout dataset index (HF, Kaggle, 서울 열린데이터광장, 공공데이터포털).
-- Loaded by 20_sync_dataset_index.py from data/dataset_index + data/hypergraph.
-- Vectors are halfvec: the local index is float16 already, and it halves storage.
-- No ANN index: ranking needs every dataset's best chunk (max per dataset), which is an
-- exact scan anyway; at tens of thousands of chunks that scan is fast. Add an HNSW index
-- (halfvec_cosine_ops) if the table grows past a few hundred thousand rows.

create extension if not exists vector;

create table if not exists public.model_scout_datasets (
    dataset_id text primary key,
    source text not null,
    title text,
    url text,
    summary_ko text,
    concepts text[] not null default '{}',
    entity jsonb not null,
    active boolean not null default true,
    updated_at timestamptz not null default now()
);

create table if not exists public.model_scout_dataset_chunks (
    chunk_id text primary key,
    dataset_id text not null references public.model_scout_datasets(dataset_id) on delete cascade,
    kind text not null,
    heading_path text[] not null default '{}',
    text text not null,  -- first 600 chars; full text is in data/dataset_index/chunks.jsonl
    text_hash text not null,
    embedding halfvec(1536) not null,
    updated_at timestamptz not null default now()
);

create index if not exists model_scout_dataset_chunks_dataset_idx
    on public.model_scout_dataset_chunks (dataset_id);
create index if not exists model_scout_dataset_chunks_hash_idx
    on public.model_scout_dataset_chunks (text_hash);
create index if not exists model_scout_datasets_concepts_idx
    on public.model_scout_datasets using gin (concepts);

alter table public.model_scout_datasets enable row level security;
alter table public.model_scout_dataset_chunks enable row level security;

do $$
begin
    if not exists (select 1 from pg_policies where schemaname = 'public'
                   and tablename = 'model_scout_datasets' and policyname = 'model_scout_datasets_public_read') then
        create policy model_scout_datasets_public_read on public.model_scout_datasets
            for select to anon, authenticated using (active = true);
    end if;
    if not exists (select 1 from pg_policies where schemaname = 'public'
                   and tablename = 'model_scout_dataset_chunks' and policyname = 'model_scout_dataset_chunks_public_read') then
        create policy model_scout_dataset_chunks_public_read on public.model_scout_dataset_chunks
            for select to anon, authenticated using (true);
    end if;
end
$$;

-- Best cosine similarity per dataset over all of its chunks (card + README sections).
create or replace function public.match_model_scout_datasets(query_embedding halfvec(1536))
returns table (dataset_id text, similarity real)
language sql stable
as $$
    select c.dataset_id, max(1 - (c.embedding <=> query_embedding))::real
    from public.model_scout_dataset_chunks c
    join public.model_scout_datasets d on d.dataset_id = c.dataset_id and d.active
    group by c.dataset_id
$$;
