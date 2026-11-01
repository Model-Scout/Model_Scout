---
license: apache-2.0
language:
- ko
---

# Bucheon Public Notices (KO JSON, Harmony)

부천시 고시/공고 원문을 기반으로 **Harmony 포맷** 학습 데이터로 변환했습니다.  
`assistant`의 `<content>` 구간은 아래 JSON 스키마를 따릅니다.

```json
{ "title": str, "notice_id": str, "date": "YYYY-MM-DD", "department": str, "summary": str }