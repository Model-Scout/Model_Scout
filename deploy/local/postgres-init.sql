-- Local validation postgres (deploy/compose.local.yml). Supabase has these roles; app_schema.sql and the
-- AI's checkpoint setup revoke access from them, so the local database needs them to exist.
create role anon nologin;
create role authenticated nologin;
