-- Model Scout dataset index, corpus v2 (refined public data: official license, delivery, cycle,
-- coverage). Loaded by `20_sync_dataset_index.py --corpus v2` from data/dataset_index_v2 +
-- data/hypergraph_v2. Separate tables from v1 (supabase_dataset_schema.sql): loading v2 never
-- touches what the running service reads. Same layout and search function as v1, plus a record
-- of which frozen build the rows came from.

create extension if not exists vector;

create table if not exists public.model_scout_datasets_v2 (
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

create table if not exists public.model_scout_dataset_chunks_v2 (
    chunk_id text primary key,
    dataset_id text not null references public.model_scout_datasets_v2(dataset_id) on delete cascade,
    kind text not null,
    heading_path text[] not null default '{}',
    text text not null,  -- the whole chunk (v1 keeps a 600-char preview)
    text_hash text not null,
    embedding halfvec(1536) not null,
    updated_at timestamptz not null default now()
);

-- The build the rows mirror: documents_id / corpus_id / data_version / model list, one row per load.
create table if not exists public.model_scout_dataset_index_v2_meta (
    key text primary key,
    value jsonb not null,
    updated_at timestamptz not null default now()
);

create index if not exists model_scout_dataset_chunks_v2_dataset_idx
    on public.model_scout_dataset_chunks_v2 (dataset_id);
create index if not exists model_scout_dataset_chunks_v2_hash_idx
    on public.model_scout_dataset_chunks_v2 (text_hash);
create index if not exists model_scout_datasets_v2_concepts_idx
    on public.model_scout_datasets_v2 using gin (concepts);

alter table public.model_scout_datasets_v2 enable row level security;
alter table public.model_scout_dataset_chunks_v2 enable row level security;
alter table public.model_scout_dataset_index_v2_meta enable row level security;

do $$
begin
    if not exists (select 1 from pg_policies where schemaname = 'public'
                   and tablename = 'model_scout_datasets_v2' and policyname = 'model_scout_datasets_v2_public_read') then
        create policy model_scout_datasets_v2_public_read on public.model_scout_datasets_v2
            for select to anon, authenticated using (active = true);
    end if;
    if not exists (select 1 from pg_policies where schemaname = 'public'
                   and tablename = 'model_scout_dataset_chunks_v2' and policyname = 'model_scout_dataset_chunks_v2_public_read') then
        create policy model_scout_dataset_chunks_v2_public_read on public.model_scout_dataset_chunks_v2
            for select to anon, authenticated using (true);
    end if;
end
$$;

-- Best cosine similarity per dataset over all of its chunks (card + sections), v2 tables only.
create or replace function public.match_model_scout_datasets_v2(query_embedding halfvec(1536))
returns table (dataset_id text, similarity real)
language sql stable
as $$
    select c.dataset_id, max(1 - (c.embedding <=> query_embedding))::real
    from public.model_scout_dataset_chunks_v2 c
    join public.model_scout_datasets_v2 d on d.dataset_id = c.dataset_id and d.active
    group by c.dataset_id
$$;
