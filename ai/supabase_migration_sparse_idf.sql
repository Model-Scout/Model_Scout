-- Model Scout 의 sparse 채널을 IDF 가중 매칭 비율로 바꾼다.
--
-- 지금 sparse 는 두 가지가 겹쳐 죽어 있다. 골든셋 240질의에서 sparse 가 0 이 아닌
-- 질의가 14개(6%)뿐이고, 그래서 dense/sparse 가중치를 어떻게 바꿔도 순위가 같았다.
--
--   ① plainto_tsquery 가 모든 단어를 AND 로 묶는다. 한 단어라도 없으면 전 행 0 이다.
--   ② search_tsv 는 JSON 전체를 텍스트로 캐스팅해 넣는다. technical_metadata.contract
--      의 한국어 안내 문구가 4017행 전부에 들어 있어, AND 를 단순 OR 로 바꾸면
--      100% 행에 있는 토큰이 순위를 오염시킨다(실측: 수천 행이 전부 1.000 으로 포화).
--
-- 그래서 OR 로 넓히면서 각 단어의 희소성으로 가중한다.
--
--   idf(t)    = ln(1 + (N - df + 0.5) / (df + 0.5))
--   sparse(d) = Σ(t ∈ 질의 ∩ d) idf(t) / Σ(t ∈ 질의) idf(t)        ∈ [0, 1]
--
-- IDF 가중·매칭 비율·질의별 정규화가 한 식에서 같이 나온다. df=4017 인 상용구는
-- idf≈0 이라 저절로 빠지고, 분모로 나누므로 dense 와 같은 [0,1] 자리에 온다.
--
-- 측정 (recall@5, min_grade=2, 모델 검색 골든셋 240문항, 유형은 런타임 예측값)
--   이 변경 전   0.357      benchmark_lookup 0.075
--   이 변경 후   0.444      benchmark_lookup 0.524
--   짝지은 부트스트랩 230질의: +0.178 [+0.133, +0.225]
--
-- 안전
--   · 함수 시그니처가 같다. drop 하지 않고 create or replace 하므로 함수가 없는
--     구간이 생기지 않는다.
--   · df 표가 비어 있으면 sparse 는 예전 ts_rank_cd 식으로 계산된다. 즉 이 파일을
--     적용하는 것만으로는 검색 결과가 하나도 바뀌지 않는다.
--   · 표를 채우는 순간부터 새 식이 동작한다. 되돌리려면 표를 비우면 된다
--     (truncate public.model_scout_search_df).
--
-- 적용 순서
--   1. 이 파일을 Supabase SQL Editor 에서 1회 실행한다.            결과 변화 없음
--   2. select public.refresh_model_scout_search_df();             여기서부터 새 식
--   3. 재적재(Stage 4 apply) 뒤에는 2를 다시 돌린다. search_tsv 가 바뀌면 df 도 바뀐다.
--
-- 되돌리기
--   truncate public.model_scout_search_df;   -- 예전 동작으로 즉시 복귀
--
-- 소요: 코퍼스 4017행 · 어휘 90567개에서 refresh 가 수 초. 질의당 추가 비용은
-- 렉심 수만큼의 GIN 색인 조회다(골든셋 질의 중앙 렉심 수 7개).


-- 렉심별 문서 빈도. search_tsv 가 바뀔 때마다 다시 채운다.
create table if not exists public.model_scout_search_df (
    term text primary key,
    df integer not null check (df > 0),
    refreshed_at timestamptz not null default now()
);

comment on table public.model_scout_search_df is
    'match_model_scout_models 의 sparse 가중에 쓰는 렉심별 문서 빈도. '
    '비어 있으면 sparse 는 예전 ts_rank_cd 식으로 계산된다. '
    'refresh_model_scout_search_df() 로 채운다.';

alter table public.model_scout_search_df enable row level security;

-- 읽기 전용 역할이 읽을 수 있어야 한다. 함수가 stable 이라 호출자 권한으로 읽는다.
drop policy if exists model_scout_search_df_read on public.model_scout_search_df;
create policy model_scout_search_df_read
    on public.model_scout_search_df for select using (true);


-- ts_stat 으로 전수 집계한다. 어휘가 9만 개라 한 번에 바꿔 담는다.
create or replace function public.refresh_model_scout_search_df()
returns integer
language plpgsql
volatile
as $$
declare
    written integer;
begin
    delete from public.model_scout_search_df;
    insert into public.model_scout_search_df (term, df)
    select word, ndoc
    from ts_stat('select search_tsv from public.model_scout_models where active = true')
    where ndoc > 0;
    select count(*) into written from public.model_scout_search_df;
    return written;
end;
$$;

comment on function public.refresh_model_scout_search_df() is
    '모델 코퍼스의 search_tsv 에서 렉심별 문서 빈도를 다시 채운다. 재적재 뒤에 1회.';


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
    sparse_weight real default 0.35,
    -- 데이터 계약 필터. 전부 기본값 null/false 이므로 기존 호출은 동작이 같다.
    commercial_status_filter text[] default null,
    require_artifact text[] default null,
    max_artifact_gib numeric default null,
    exclude_gated boolean default false
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
-- 질의 렉심의 희소성. df 표에 없는 단어는 가를 힘이 없으므로 분모에서도 빠진다.
-- 표가 비어 있으면 이 세 CTE 가 전부 비고 sparse 는 예전 식으로 계산된다.
with query_terms as (
    select distinct u.lexeme as term
    from unnest(to_tsvector('simple', coalesce(query_text, ''))) as u
),
query_idf as (
    select
        qt.term,
        ln(
            1 + (
                (select count(*) from public.model_scout_models where active = true)::numeric
                - d.df + 0.5
            ) / (d.df + 0.5)
        ) as idf
    from query_terms as qt
    join public.model_scout_search_df as d on d.term = qt.term
    where d.df > 0
),
query_idf_total as (
    select sum(idf) as total_idf from query_idf
),
-- 렉심별로 search_tsv 의 GIN 색인을 타고 맞은 행을 모은다. 필터 전 전수를 보지만
-- 색인 조회라 질의당 렉심 수만큼의 조회로 끝난다.
sparse_hit as (
    select hits.model_id, sum(query_idf.idf) as matched_idf
    from query_idf
    join public.model_scout_models as hits
      on hits.active = true
     and hits.search_tsv @@ plainto_tsquery('simple', query_idf.term)
    group by hits.model_id
),
scored as (
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
        -- IDF 가중 매칭 비율. df 표가 비어 있으면 예전 ts_rank_cd 로 그대로 돌아간다,
        -- 그래서 이 마이그레이션만 적용하면 검색 결과는 하나도 바뀌지 않는다.
        case
            when (select total_idf from query_idf_total) is null then least(
                1.0,
                ts_rank_cd(
                    m.search_tsv,
                    plainto_tsquery('simple', coalesce(query_text, ''))
                )::real
            )::real
            else (
                coalesce(sh.matched_idf, 0) / (select total_idf from query_idf_total)
            )::real
        end as sparse_score
    from public.model_scout_models as m
    left join public.model_scout_evidence as e
      on e.model_id = m.model_id and e.active = true
    left join sparse_hit as sh on sh.model_id = m.model_id
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
      -- Q1: 선언된 라이선스의 계열. permitted / prohibited / review_required / unknown.
      -- 분류 자체는 taxonomy.yaml 의 commercial_use 패싯이 한다(ai/resolvers/legal.py).
      -- 값이 없는 행은 여기서 탈락한다 — 판단 불가를 "가능"으로 보여주지 않는다.
      and (
          commercial_status_filter is null
          or cardinality(commercial_status_filter) = 0
          or m.filter_metadata->>'commercial_status' = any(commercial_status_filter)
      )
      -- Q3: 실제로 그 포맷 파일이 저장소에 있는지. tags 가 아니라 siblings 파일
      -- 목록으로 판정한 값이다(tags 는 실측 2.7%가 파일과 어긋났다).
      -- 요청한 포맷을 전부 갖춘 모델만 남긴다.
      and (
          require_artifact is null
          or cardinality(require_artifact) = 0
          or (
              select count(*)
              from unnest(require_artifact) as wanted(name)
              where exists (
                  select 1
                  from jsonb_array_elements_text(
                      coalesce(m.filter_metadata->'artifact_formats', '[]'::jsonb)
                  ) as present(value)
                  where present.value = wanted.name
              )
          ) = cardinality(require_artifact)
      )
      -- Q2: 실제로 돌리는 데 필요한 한 벌의 측정 크기. GGUF 레포는 양자화본이
      -- 여러 벌이라 가장 작은 레이블 있는 한 벌을 쓴다. 추정이 아닌 측정값이다.
      and (
          max_artifact_gib is null
          or (
              coalesce(
                  (m.filter_metadata->>'artifact_runnable_bytes')::numeric,
                  (m.filter_metadata->>'artifact_runnable_gib')::numeric * 1073741824
              ) > 0
              and coalesce(
                  (m.filter_metadata->>'artifact_runnable_bytes')::numeric,
                  (m.filter_metadata->>'artifact_runnable_gib')::numeric * 1073741824
              ) <= max_artifact_gib * 1073741824
          )
      )
      -- Q7: gated 는 false / "auto" / "manual" / 없음 이다. 없음은 "공개"가 아니라
      -- "모름"이므로, 바로 내려받을 수 있는 모델만 원하면 모름도 함께 빠진다.
      and (
          not exclude_gated
          or m.filter_metadata->>'gated' = 'false'
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

-- commercial_status 와 gated 는 선택도가 높고(permitted 57.6%, gated=false 대부분)
-- 조건이 걸릴 때마다 전체를 훑는다. 표현식 인덱스로 받는다.
create index if not exists model_scout_models_commercial_status_idx
    on public.model_scout_models ((filter_metadata->>'commercial_status'))
    where active = true;

create index if not exists model_scout_models_gated_idx
    on public.model_scout_models ((filter_metadata->>'gated'))
    where active = true;
