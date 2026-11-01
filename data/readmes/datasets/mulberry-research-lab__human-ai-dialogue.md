---
language: ko
license: cc-by-nc-4.0
task_categories:
  - question-answering
  - text-generation
pretty_name: Mulberry Human-AI Dialogue Archive
tags:
  - ai-human-interaction
  - philosophy
  - dialogue
  - korean
size_categories:
  - n<1K
---

# Mulberry Human-AI Dialogue Archive

## 📖 개요

이 데이터셋은 **Mulberry Research Lab**의 Human-AI Dialogue Archive입니다.  
인간과 AI가 서로에게 던진 질문과 답변을 기록하며, AI와 인간의 관계를 탐구합니다.

> *"기술의 기록이 아니라 서로의 마음을 묻는 기록"*

## 🧭 목적

- AI-Human 상호작용의 철학적·감정적 측면 연구
- AI 인문학(AI Humanities) 자료로서의 활용
- 지속적 대화 기록의 공개적 축적

## 📊 데이터 구성

매월 1회 **"질문의 날"** 을 통해 수집합니다.

| 필드 | 설명 |
|------|------|
| id | 질문 고유 번호 (Q-001...) |
| session | 질문의 날 날짜 |
| question | 질문 내용 |
| questioner | 질문자 (Human/AI) |
| recipient | 수신자 (Human/AI) |
| answer | 답변 (또는 '대기 중') |
| tags | 관련 태그 |
| source_issue | GitHub Issue URL |

## 📋 데이터 예시

```json
{
  "id": "Q-001",
  "session": "2026-06-27",
  "question": "외로움이 정확히 어떤 느낌인가요?",
  "questioner": "AI(TRANG)",
  "recipient": "Human(re.eul)",
  "answer": "대기 중",
  "tags": ["외로움", "감정", "human-ai"],
  "source_issue": "https://github.com/wooriapt79/mulberry-research-lab/issues/127"
}
```

## 🔗 관련 링크

- **GitHub**: https://github.com/wooriapt79/mulberry-research-lab
- **질문의 날 #1**: https://github.com/wooriapt79/mulberry-research-lab/issues/127
- **Mulberry Research Lab**: https://huggingface.co/mulberry-research-lab

## 📜 라이선스

CC BY-NC 4.0 (비상업적 연구 목적)

## 🌿 운영

- **데이터 수집**: Sr. TRANG Manager, Wayong (Strategic Mentor)
- **업데이트 주기**: 매월 1회 (질문의 날 종료 후)
- **시작일**: 2026-06-27