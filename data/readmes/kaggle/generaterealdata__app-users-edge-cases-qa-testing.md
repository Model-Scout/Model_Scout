# App Users with Edge Cases for QA Testing

Seed data that breaks naive code: Unicode, injection strings, soft deletes

> **Created with [GenerateRealData](https://generaterealdata.com?ref=kaggle)**, a platform that generates realistic synthetic data from a plain-English description or your own SQL schema. To learn more or create your own dataset, visit **https://generaterealdata.com** or email **support@generaterealdata.com**.

Seed data for testing a multi-tenant web application: organizations, users, memberships, API tokens and an audit log. Most rows are ordinary. A deliberate share are the cases real applications trip over: names in Arabic, Hebrew, Chinese, Japanese, Korean, Cyrillic and Greek, emoji, one-character and 100-character names, leading and trailing spaces, SQL and HTML injection strings, plus-addressed emails, soft-deleted and never-logged-in users, expired and revoked tokens, IPv6 addresses.

## Why this dataset

- About one user in seven has a display name chosen to break something: non-Latin scripts, right-to-left text, emoji, quotes, commas, tabs, 'Null', 'undefined', '0', "Robert'); DROP TABLE users;--" and "".
- Emails are always unique and always at example domains, and include plus-addressing, a subdomain and very long local parts.
- States are consistent, so your assertions can be strict: deleted users have a deletion time after creation and nobody else has one; invited users have never logged in; a membership never predates its user or organization.
- Thirty locales, each with a matching IANA time zone; a mix of IPv4 and IPv6 addresses in the audit log.

**Good for:** Seeding test and staging databases; QA of forms, search, sorting, exports and emails with awkward text; Security-testing input handling (the strings are harmless samples); Testing soft-delete, invitation and token-expiry logic.

## Tables

| Table | Rows | What it holds |
|---|---:|---|
| `organizations` | 2,000 | Tenants of the application. |
| `users` | 40,000 | User accounts, with deliberately awkward values among ordinary ones. |
| `memberships` | 46,000 | Which user belongs to which organization. Every organization and every user has at least one. |
| `api_tokens` | 6,000 | API tokens issued to users. |
| `audit_events` | 106,000 | The audit log. |

**How the tables connect:** `memberships.org_id` Ã¢â€ â€™ `organizations`; `memberships.user_id` Ã¢â€ â€™ `users`; `api_tokens.user_id` Ã¢â€ â€™ `users`; `audit_events.org_id` Ã¢â€ â€™ `organizations`; `audit_events.user_id` Ã¢â€ â€™ `users`.

## Rules you can rely on

30 rules were checked on the full dataset and all 30 hold. Each rule is a query that counts the rows breaking it, and every count is 0. The queries are in the [GitHub repository](https://github.com/generaterealdata/synthetic-datasets/tree/main/app-users-edge-cases).

- organizations.org_id is unique
- organizations.slug is unique
- users.user_id is unique
- users.email is unique
- Every memberships.org_id exists in organizations
- Every memberships.user_id exists in users
- Every api_tokens.user_id exists in users
- Every audit_events.org_id exists in organizations
- Every audit_events.user_id exists in users
- Emails use example domains only
- Plus-addressed emails are present
- Non-Latin, right-to-left and injection-style names are present
- Edge-case names are 10-20% of users
- deleted_at is set exactly for deleted users
- deleted_at is after created_at
- Invited users have never logged in
- Last login is after creation
- Every organization has a membership
- joined_at is not before the organization existed
- A token expires 30-365 days after creation
- revoked_at is after created_at
- Both IPv4 and IPv6 addresses are present
- No token is created or revoked after 2026-09-30
- A token is revoked before it expires
- A token is never created before its user
- No audit event is dated after 2026-09-30
- An audit event never happens before its user or organization existed
- No login or deletion is dated after 2026-09-30
- No membership starts after 2026-09-30
- A membership never starts before the user's account existed

## Questions to try

1. The edge-case names and how often each appears
2. Names that contain characters outside basic ASCII
3. Names with leading or trailing whitespace, or a tab inside
4. Email shapes: plus-addressing, subdomains and length
5. Users by status, with login and deletion facts
6. Locales and their time zones
7. Token states: live, expired and revoked (as of 30 September 2026)
8. Organizations with the most members, and their owners
9. Audit actions and IP versions
10. Users who belong to more than one organization

The starter notebook answers all ten with SQL.

## Good to know

- The injection-style names are inert test strings; they are there so you can confirm your application stores and shows them safely.
- Organization slugs are simply team-1, team-2 and so on; they are not derived from the organization name.
- Roles are assigned independently, so an organization can have several owners or none.
- Audit events are not tied to memberships: the user of an event is not necessarily a member of its organization.
- Yes/no columns hold 1 and 0. Empty cells in the CSV files mean no value (NULL in the database files).
- The CSV files are UTF-8. Dates are `YYYY-MM-DD` and timestamps `YYYY-MM-DD HH:MM:SS`.

## How it was made

Fully synthetic: generated with [GenerateRealData](https://generaterealdata.com/industries/software-testing-qa/?ref=kaggle) from a database schema and a set of rules, using a fixed seed. No real person, company or transaction is in the data, and no value was edited after generation. No field was written by AI. The schema, the generation plan, the rule checks and a small sample are on [GitHub](https://github.com/generaterealdata/synthetic-datasets/tree/main/app-users-edge-cases).

## Licence

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Use it for anything, including commercial work; please credit "App Users with Edge Cases for QA Testing, GenerateRealData" with a link to https://generaterealdata.com.

출처: Kaggle (generaterealdata/app-users-edge-cases-qa-testing)
태그: computer science, tabular, text, sql, english
라이선스: Attribution 4.0 International (CC BY 4.0)
수정일: 2026-10-15T09:10:32.703Z
