-- Conversation history owned by the backend. Idempotent; run once before deploying the backend.
-- The schema stays out of the Data API: no grants to anon/authenticated, and RLS on as a second lock.
-- group_id doubles as the AI's LangGraph thread_id, but nothing here references the langgraph schema.
create schema if not exists app;
revoke all on schema app from public, anon, authenticated;

create table if not exists app.groups (
    group_id uuid primary key,
    session_id uuid not null,
    title text not null,
    created_at timestamptz not null default now(),
    updated_at timestamptz not null default now()
);
create index if not exists groups_session_idx on app.groups (session_id, updated_at desc);

create table if not exists app.messages (
    id bigint generated always as identity primary key,
    group_id uuid not null references app.groups (group_id) on delete cascade,
    role text not null check (role in ('user', 'assistant')),
    content text not null,
    type text check (type in ('answer', 'clarify', 'reject')),
    result jsonb,
    created_at timestamptz not null default now()
);
create index if not exists messages_group_idx on app.messages (group_id, id);

alter table app.groups enable row level security;
alter table app.messages enable row level security;
