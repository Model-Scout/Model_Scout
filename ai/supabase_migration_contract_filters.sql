-- Model Scout 데이터 계약 필터를 match_model_scout_models 에 추가한다.
-- 선행: supabase_migration_model_search_tsv.sql (search_tsv + halfvec)
--
-- 왜
-- --
-- 타깃 사용자(부트캠프 수료생, 창업 준비자)가 실제로 묻는 질문 중 셋이 지금
-- 필터로 표현되지 않는다.
--
--   Q1 "상업 서비스에 쓸 수 있는 한국어 모델"   → 라이선스 필터가 없다
--   Q2 "RTX 5080(16GB)에 들어가는 모델"        → 파라미터 상한뿐, 실제 용량이 없다
--   Q3 "Ollama로 돌릴 수 있는 모델"             → artifact 필터가 없다
--   Q7 "바로 내려받을 수 있는 모델"             → gated 필터가 없다
--
-- 값은 Stage 4 가 filter_metadata 에 이미 올려 둔다(04_build_embeddings.py 의
-- contract_filter_fields). 이 마이그레이션은 그 값을 WHERE 절에 연결한다.
--
-- 누락 값 처리
-- -----------
-- 조건을 걸면 값이 없는 행은 탈락한다. PostgreSQL 이 JSON 값을 캐스팅하면
-- 없는 값은 NULL 이 되고 WHERE 가 그 행을 제외한다. 05_validate_retrieval
-- .numeric_ok() 가 같은 규칙을 구현하고 있어 오프라인 평가와 운영 검색의
-- 후보 집합이 일치한다.
--
-- commercial_status_filter = ARRAY['permitted'] 를 걸면 unknown 모델이 빠지는
-- 것이 **의도된 동작**이다. 모르는 모델을 상업 이용 가능으로 섞어 보여주면
-- 사용자가 창업에 쓰고 나서 문제를 알게 된다.
--
-- 롤백
-- ----
--   drop function if exists public.match_model_scout_models(
--       vector, integer, text, text[], boolean, numeric, numeric, integer, integer,
--       boolean, boolean, text, text, real, real, text[], text[], numeric, boolean);
--   그리고 supabase_migration_model_search_tsv.sql 의 함수를 다시 적용한다.

-- 파라미터가 늘면 PostgreSQL 은 다른 함수로 보고 과부하를 만든다. 구 시그니처를
-- 명시적으로 지워야 09_model_scout_mcp_readonly.py 가 모호성 오류를 보지 않는다.
drop function if exists public.match_model_scout_models(
    vector, integer, text, text[], boolean, numeric, numeric, integer, integer,
    boolean, boolean, text, text, real, real);

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
          or (m.filter_metadata->>'artifact_runnable_gib')::numeric <= max_artifact_gib
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
