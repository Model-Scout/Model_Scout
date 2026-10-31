---
language:
  - ko
task_categories:
  - text-generation
tags:
  - persona
  - character-ai
  - korean
  - tool-calling
  - function-calling
  - agent
configs:
  - config_name: default
    data_files:
      - split: train
        path: data/train-00000-of-00001.parquet
  - config_name: tools
    data_files:
      - split: train
        path: data/tools-train-*
      - split: eval
        path: data/tools-eval-*
      - split: probe
        path: data/probe-*
dataset_info:
  - config_name: default
    features:
      - name: response
        dtype: string
      - name: instruction
        dtype: string
      - name: train_on
        dtype: string
      - name: tags
        dtype: string
    splits:
      - name: train
        num_examples: 4836
  - config_name: tools
    features:
      - name: id
        dtype: string
      - name: kind
        dtype: string
      - name: messages
        dtype: string
      - name: tools
        dtype: string
      - name: tool_names
        dtype: string
      - name: final_answer_needed
        dtype: bool
      - name: final_brief
        dtype: string
      - name: final_source
        dtype: string
      - name: judge_ok
        dtype: bool
      - name: judge_flags
        dtype: string
      - name: train_on
        dtype: string
      - name: tags
        dtype: string
    splits:
      - name: train
        num_examples: 6586
      - name: eval
        num_examples: 349
      - name: probe
        num_examples: 175
---

# SampleToHiyori

## v2 (2026-10-02)

v2는 모든 행을 OpenMascotAI 서버 S12(HEAD 29a67bba)의 **프롬프트 빌더로 다시 조립**한 판이다. 표본 101행(결정 지점
185곳)에서 학습 렌더가 서버 추론 프롬프트(llama-server `/apply-template`)의 정확한 접두사임을 확인했다.
서버 S13(HEAD 8e81815c)의 빌더로 전 행을 다시 조립해도 그대로 일치한다.

| config | split | v1 | v2 |
|---|---|---:|---:|
| `tools` | `train` / `eval` / `probe` | 5,495 / 322 / — | 6,586 / 349 / 175 |
| `default` | `train` | 4,837 | 4,836 |

- 형식: system(페르소나·활동 줄·인적 정보 블록·기억 블록·`[자비스 모드]`·`[웹 검색]`), 마지막 user만 `[참고 정보]` 래퍼, 기록은 S12
  자비스 뷰(목록 밖 도구·기기 미지원 실패 왕복·무호출 완료/약속·배경 발화를 빼고 16쌍 넘으면 12쌍), 도구 결과는 서버 페이로드
  (`pending`·`note`는 이번 턴 예약형에만), 도구 정의는 현행 카탈로그(`build_tools`).
- 도구 목록: 무작위 부분집합 / PC 기본 94개(`pc_full`) / 셸 켠 PC 기본 96개(`pc_full_shell`) / 카테고리 몇 개 끈 PC(`pc_settings`) /
  안경 18개(`glass`, S12 `supported_tools`) / 일반 채팅 2개(`web`).
- 수리·삭제: 텍스트 툴콜 답, 무호출 기억 주장, **턴을 끝내는 미실행 약속**, **결과를 왜곡한 답**, 라벨 없는 취소, '바꿔줘' 정정,
  add_reminder 지어낸 인자, 제거된 도구, 경로 읽기, 정확 중복, '자비스 모드를 켜면' 거절, 정각 알람 오전/오후, 조사 등.
  배포용(자비스·히요리)은 모든 문자열 열을 익명화했다(답·final_brief 포함).
- 보강 1,368 시나리오(세 데이터셋 같은 id, 답만 말투별): 반복 요청 기록 240 · 실패 뒤 재시도 100 · 한국어 시간 표현 204 · 라벨 없는 취소 80 ·
  안경 150 · 만료 알림 80 · 긴 기록 120 · 언어 고정 30 · 새 도구(포모도로·루틴·되돌리기·문서 보기·기억/잊기·출력 장치·탭·주소·별칭) 280 ·
  반복 예약(`repeat` 인자) 30 · 되묻기 다음 턴(기록의 되묻기 쌍 → 사용자 답 → 호출) 30 ·
  말 되풀이 요청('한 번 더 말해줘' → 도구 없이 직전 답 되풀이) 24. 마무리 답은 프로그램 변주로 같은 문장 비율 12%·고유 뼈대 84%.
- default: 내용 삭제 없음(도구 요청처럼 보이는 행도 히요리 일상 잡담), 같은 답이 3번 이상 나온 것 중 1행을 지워 4,837 → 4,836행, `no_jarvis` 48행.
- eval은 템플릿 단위로 다시 나눴다(근접 중복 군집 통째로) — train↔eval 근접 중복 0. `probe`(175행)는 **같은 템플릿·하나만 보류**
  (슬롯·결과·발화·문형 중 하나, 행마다 `probe:<종류>` 태그) 일반화 점검용으로 train에서 뺐다. eval·probe id는 이 판에서 고정했다(다음 판도 유지).
- 길이: 8192 토큰을 넘는 행 198개는 전부 PC 기본 구성(`pc_full`·`pc_full_shell`) — `max_seq_length` 9216 이상이어야 학습된다.
- 배포 전제: 안경 클라이언트(`Frames.java chat()`)가 `supported_tools`를 보내야 학습한 18개 도구 구성이 된다(안 보내면 서버가 38개를 준다).

### 스키마 계약(노트북 v2 로더용)

- 파일·열은 원본과 같다. `tools` config: `data/tools-{train,eval}-00000-of-00001.parquet` + **`data/probe-00000-of-00001.parquet`**(split `probe`)
  — `id, kind, messages, tools, tool_names, final_answer_needed, final_brief, final_source, judge_ok, judge_flags` + **`train_on`**, **`tags`**.
  대화(default) config(히요리·루시아): `data/train-00000-of-00001.parquet` — `response, instruction` + `train_on`, `tags`.
- `messages`·`tools`·`tool_names`·`final_brief`·`judge_flags`·`tags`는 원본과 같은 **JSON 문자열**(`json.dumps(ensure_ascii=False)`).
  툴콜 `arguments`도 JSON 문자열이다(노트북이 dict로 바꾼다).
- `train_on`: `"all"` = 모든 assistant 턴 학습, `"final_only"` = **마지막 `[참고 정보]` user 턴 이후만** 학습(기록 assistant는 loss 제외).
  대화 행은 전부 `"all"`.
- `tags`(JSON 목록): `src:v1`(원본 변환) · `aug:<유형>` · `profile:<pc_subset|pc_full|pc_full_shell|pc_settings|glass|web|notify>` ·
  `shell_on`(셸 카테고리를 켠 설정) · `glass` · `notification`(알림 행) · `no_call`(도구 없이 답하는 행) · `repaired:<유형>` ·
  `review`(사람 검수 권장) · `s12_bypass` · `stale_refusal` · `lang_lock` · `ask_ampm` · `tomorrow_reminder`('내일' 알람인데 오늘 그 시각이 남아
  `add_reminder`에 내일 날짜를 넣은 행) · `clarify_followup`(기록에 되묻기 쌍, 이번 턴은 사용자 답으로 호출) · `tool:<이름>` · `history:<쌍 수>` ·
  **`vision`**(이미지 결과 턴의 답이 화면 내용·상태를 묘사 — 텍스트만 학습하면 지어낸 묘사가 되므로 노트북 기본 제외) ·
  **`probe:policy`**(probe 중 정책 일관성 점검 행 — 따로 집계) · **`probe:slot|result|utterance|phrasing`**(깨끗한 probe 행의 보류
  종류 — 아래) · `pii`(루시아 tools의 실제 생일·거주지 행).
  `pc_full_shell`은 셸을 켠 PC 기본 구성(도구 96개)으로 셸 끈 `pc_full`(94개)과 다른 서버 설정이다. 대화 행: **`no_jarvis`**(자비스형·웹형
  감싸기 금지, 평문으로만), `repaired:default_trim|default_edit|default_r8|default_r9`, `review`, `pii`(루시아 실명·생년·거주지 언급 행).
- 자리표시: `{{PERSONA}}`(도구 행 system에 정확히 1번), **`{user}`**(인적 정보 블록의 이름과 사용자를 이름으로 부르는 답 — 노트북
  `USER_NAME`으로 채움). `{character}`는 쓰지 않았다(사용자 호격은 원래 이름 '히요리야·루시아야' 그대로). 툴콜 인자·도구 결과에는
  자리표시가 없다(노트북이 인자는 채우지 않으므로).
- 인적 정보 블록: 서버 `Core/llm/prompts.py`의 **`_user_info_block()`**(`server_config.LLM.LLM_USER_NAME="{user}"`, 성별·생년월일
  빈 값)을 `build_jarvis_chat_messages`/`build_web_chat_messages`(→ `_build_chat_messages`)와 `_build_notification_messages`가 그대로
  붙인 것. 대화 행을 같은 모양으로 조립할 때의 system은
  `PERSONA + "\n\n" + ACTIVITY_SYSTEM_LINE + _user_info_block()` (+ 기억 블록이면 `"\n\n" + memory_block`),
  블록 문자열은 정확히 `"\n    ### [대화 하고있는 상대방 {user}님에 대한 인적 정보]\n    - **성함(혹은 닉네임):** {user}\n    \n\n"` 이다(이름이 비면 블록 전체 생략).
- 알림 행(`kind=notification`, `tools="[]"`): system = 인적 정보 블록 + `{{PERSONA}}`(지시문 없음), user = 서버
  `notification_prompt("타이머", 내용)` 원문, assistant = 답. train·eval·probe 각각 **맨 뒤**에 둬서 노트북의 '앞 300행 system 꼬리' 검사를 지킨다.
- 안경 행(`profile:glass`, 494행·전부 보강)은 마지막 user에 감정 줄(`… 감정 상태는 Neutral …`)이 항상 있다 — 안경 클라이언트가
  `emotion:true`를 늘 보낸다.
- `judge_ok`: 답을 바꾸지 않은 원본 행은 원래 값(true), 바꾸거나 새로 만든 행은 null. `final_source`: 원본 값 / `v2-manual`(수기 표) /
  `v2-rule`(규칙) / `v2-template`(보강), 이름 보강 행은 `+name` 유지.
- `probe` split: **같은 템플릿, 하나만 보류** — train에 남은 근접 중복 군집과 같은 문형이고, 무엇을 보류했는지가 행마다 태그로 있다.
  깨끗한 141행 = `probe:slot` 86(슬롯값 — 단위 붙은 숫자·라벨·시각·툴콜 인자 — 조합이 군집의 train 행과 다름) ·
  `probe:result` 22(슬롯은 같고 도구 결과가 군집에서 유일) · `probe:utterance` 14(슬롯 없는 도구,
  발화가 군집에서 유일) · `probe:phrasing` 19(슬롯·결과가 같은 다른 문형). 모두 '정규화한 마지막 발화(부탁 어미 포함) +
  첫 정답'이 어떤 train 행과도 같지 않다. train에서 뺐고(학습 안 됨) eval과 섞이지 않는다. 일반화 점검용(eval은 새 템플릿 점검용).
  `probe:policy` 34행은 같은 문형에서 기록·목록이 달라 답이 갈려야 하는 정책 일관성 점검이라 첫 정답이 train과 같을 수 있다 —
  깨끗한 probe 점수에서는 빼고 따로 본다.
- eval·probe id는 이 판에서 **고정**했다(빌드 쪽 `splits_v2.json`, CHANGELOG 16절) — 다음 판도 같은 id를 eval·probe로 두고, 고정 행의 답이
  바뀌면 CHANGELOG에 버전별 id 목록을 적는다(바뀌지 않은 부분집합끼리 비교).

아래는 v1 설명이다. v2와 다른 곳(도구 수, 인적 정보 블록·이름 보강 방식, '자비스 모드를 켜면' 문구, 결과 형식)은 위 절이 우선한다.

'모모세 히요리(桃瀬 ひより)' 페르소나 학습용 한국어 데이터셋. config 두 개로 이루어진다.

| config | split | 행 수 | 내용 |
|---|---|---:|---|
| `default` | `train` | 4,837 | 단일 턴 한국어 페르소나 대화 (`instruction` / `response`) |
| `tools` | `train` / `eval` | 5,495 / 322 | 도구 호출(function calling) 대화 |

히요리는 상대를 항상 **"오빠"** 라고 부르고, 일인칭은 **"히요리"**, 말투는 **"~인걸" / "~인거야"** 다.

## `tools`

OpenMascotAI 마스코트의 **자비스 모드**(윈도우를 실제로 조작하는 모드)에서 쓰기 위한 도구 호출
학습 데이터. 페르소나 LoRA를 얹으면 베이스 모델이 도구를 전혀 호출하지 않게 되는 현상을 고치려고
만들었다. 시나리오(도구·인자·결과·브리프)는 자매 데이터셋 `MelissaJ/ProjectLucia_Hera` 의 `tools`
config 와 **동일한 구조**이며, 호칭·이름만 히요리 세계로 옮기고 최종 대사를 히요리 LoRA로 새로 생성했다.

### 컬럼

| 컬럼 | 타입 | 설명 |
|---|---|---|
| `id` | string | 행 식별자 |
| `kind` | string | `tool` / `multistep` / `chat_with_tools` / `ambiguous` / `refusal_or_unsupported` / `correction` |
| `messages` | string(JSON) | OpenAI 스타일 메시지 배열 (`system` / `user` / `assistant`(+`tool_calls`) / `tool`) |
| `tools` | string(JSON) | 제시된 OpenAI tool 스키마 배열 (정답 도구 + 방해 도구, 순서 무작위) |
| `tool_names` | string(JSON) | 실제로 호출한 도구 이름 |
| `final_answer_needed` | bool | 최종 답변이 필요한 행인지 |
| `final_brief` | string(JSON) | 각 최종 답변이 담아야 할 사실 |
| `final_source` | string | `lora`(모델 생성) / `template`(규칙 기반 폴백) / `manual`(재검수 수기 수정) |
| `judge_ok` / `judge_flags` | bool / string(JSON) | 순정 모델 심사 결과 |

`system` 메시지 맨 앞의 **`{{PERSONA}}`** 자리표시자는 학습 스크립트가 자기 캐릭터 프롬프트로
치환한다. 그 뒤에는 OpenMascotAI 서버의 자비스 지시문이 붙어 있다.

```python
import json
from datasets import load_dataset

ds = load_dataset("MelissaJ/SampleToHiyori", "tools", split="train")
row = ds[0]
messages, tools = json.loads(row["messages"]), json.loads(row["tools"])
messages[0]["content"] = messages[0]["content"].replace("{{PERSONA}}", MY_PERSONA_PROMPT)
for m in messages:                       # 챗 템플릿은 arguments 가 dict 여야 한다
    for tc in (m.get("tool_calls") or []):
        tc["function"]["arguments"] = json.loads(tc["function"]["arguments"])
text = tokenizer.apply_chat_template(messages, tools=tools, tokenize=False)
```

### 종류별 구성

| kind | 행 수 |
|---|---:|
| `ambiguous` | 326 |
| `chat_with_tools` | 455 |
| `correction` | 401 |
| `multistep` | 605 |
| `refusal_or_unsupported` | 349 |
| `tool` | 3,166 |

### 도구 카탈로그

OpenMascotAI 자비스 도구 89개 — 클라이언트 실행 87개 + 서버 실행 웹 도구 2개
(`web_search`, `read_webpage`). 호출되는 도구는 모두 최소 24회 등장한다(`register_alias` 는
나중에 카탈로그에 추가돼 방해 도구로만 나온다). 도구 결과는 실제 클라이언트 구현이 돌려주는
문자열 포맷을 그대로 재현했다.

### 생성 방법

규칙 기반 합성(seed 고정)으로 시나리오를 만들고, 모든 인자를 서버의 `validate_args` 로 검증했다.
선택 인자는 발화가 근거를 줄 때만 넣는다. 최종 대사는 히요리 LoRA(Gemma 4 31B QAT, scale 8.0,
think OFF)가 도구 결과를 문맥에 넣은 상태로 생성했고, **LoRA 없는 순정 모델**이 각 답변을
"실행하지 않은 동작을 했다고 하는가 / 결과에 없는 사실을 지어내는가 / 실패를 성공이라 하는가 /
호칭이 '오빠'가 아닌가"로 심사해 통과할 때까지 재생성했다. `final_source` 중 98.2%가 모델 생성(`lora`)이고, 규칙 기반 폴백 `template` 85행, 2026-09-02 재검수 수기 수정 `manual` 12행이다.

### 개정 이력

**2026-09-03 E 보강 (5,495 / 322행, `default` 4,837행)** — 루시아와 같은 id·구조로 적용했다(답변만 히요리 말투).
스펙 `docs/superpowers/specs/2026-09-03-dataset-boost-design.md`, 스크립트 `devtools/dataset/step_e_boost.py`.

- **홀드아웃 복구.** 실측 배터리 발화(`devtools/eval/prompts_web.py`)와 글자까지 같던 13행(`wc-pos-0001/0002/0004/0035`,
  `wc-neg-0001/0009/0054/0069/0082`, `chatweb-0003/0039`, `web-search-0030`, `corr-0015` 첫 턴)의 **발화만** 재표현.
  `validate`가 배터리 발화와 정규화 일치하는 첫 발화를 거부한다(검사 8). 히요리 `default`에는 누출이 없었다.
- **안정 상식 검색 13행 → 무호출 전환** — `web-search-0055/0077/0085/0096/0107/0115/0126/0137/0145/0156/0158/0167/0227`.
  검색 요청어 없는 안정 상식 질문("로마제국 언제 망했어?" 등)에 검색하던 행이 자비스 모드 오검색의 원인이었다.
- **기억 창작 재작성** — `chat-0015/0060/0105/0195/0240/0285`(MSN 메신저를 써 본 것처럼 답함 — 히요리는 그 시절 이후에
  태어난 학생이라 "못 써 봤다"로), `wc-neg-0142`(처음 만난 날 장면 창작). 히요리 `default`에는 같은 모양이 없어 그대로다.
- **신규 tools 215행**(train 194 / eval 21, 호출 120 / 무호출 95): `jrt-` 자비스 ON 실시간 검색 쌍둥이 120, `jkn-` 자비스 ON
  안정 상식 무호출 40, `ckn-` 자비스 OFF 무호출 15, `mem-h-` 기록에 없는 과거 20, `mem-r-` 앞 턴 회상 10, `mem-b-`
  `[기억하고 있는 사실]` 블록 기반 10. 상세는 루시아 카드와 같다.
- **신규 `default` 20행** — "저번에 말한 X 기억나?"에 지금 기록에 없다고 정직하게 답하고 되묻는다.
- 전 행을 `unsloth/Qwen3.8-27B` 챗 템플릿으로 렌더해 예외 0·8,192토큰 이하·호출/무호출 렌더 일치를 확인했다.

**2026-09-02 재검수 (현재 리비전, 5,302행)**

- 자매 데이터셋과 동일한 재검수를 적용했다. `judge_ok=false` 로 남아 있던 9행을 상위 모델이
  재판정해 **결함 6행의 답변만 다시 썼고**(`tool_calls`·인자·도구 결과는 그대로), 오탐 3행은
  `judge_ok` 만 정정했다. 결함 모양: `list_dir` 결과와 다른 파일명·용량 날조 3행,
  서술체 잔재("…할 것 같아") 1행, 능력 부정("난 잘 몰라서 대충 따라할 뿐이야") 1행,
  시각 근거 없는 시각 답변(`amb-0109`, `[참고 정보]` 시간 헤더를 붙여 해소) 1행.
- 심판을 통과했지만 같은 결함(브라우저만 여는 도구의 **안 보이는 결과 내용 서술**, 서술체)인
  5행도 함께 수정했다. 다시 쓴 답변은 `final_source="manual"` 12행. 이제 전 행이 `judge_ok=true` 다.
- `default` config: 일본어 문자 혼입 3행 교정("하이ソックス"→"하이삭스", "자는姿"→"자는 모습" 등)과
  서술체 잔재 2행 재작성. 행 수는 4,817로 그대로다.

**2026-08-30 ~ 09-01 (자매 데이터셋 동기화, 4,947 → 5,302행)**

- `MelissaJ/ProjectLucia_Hera` tools config 의 리비전(재현율 복원 110행 · 문맥 되돌리기 140행 ·
  5차 되돌리기 재설계 + 신규 55행 · 5.1차 자기 행동 서술/없는 기능 요청 50행 · 도구 매핑·능력 주장
  최종 감사)을 같은 시나리오로 반영하고, 최종 대사는 히요리 LoRA로 새로 생성했다.
  상세 배경은 자매 데이터셋 카드의 개정 이력 참고.

**2026-08-29 (4,947행)**

- 시스템 프롬프트를 서버 `JARVIS_SYSTEM_ADDENDUM` 현재 문구(10줄)로 갱신했다 — 지시문을 담은
  4,727행 전부. 웹 전용 220행은 지시문 없이 그대로 둔다. 대화 내용은 재생성하지 않았다.
- 신규 88행: "취소/되돌려" 문맥 42(취소는 **직전에 실제로 한 동작**을 되돌린다) ·
  방법/능력 질문 네거티브 30 · 비교/의견 질문 네거티브 10 · "설정 창" 구분 6.

### 한계

- 합성 데이터이며 도구 결과는 실제 실행 결과가 아니라 포맷을 재현한 것이다.
- `capture_screen` 행에는 이미지가 없어 비전 왕복까지는 학습되지 않는다.
- `web_search` / `read_webpage` 는 이제 서버가 직접 실행한다(`Core/ai/web_tools.py`).
- 도구 정의가 길어 전체 카탈로그를 실은 행은 길다. `max_seq_length` 를 확인할 것.

---

<details>
<summary>기존 카드 원문 (내용이 이 데이터셋과 맞지 않아 보존만 해둠)</summary>

# GRPO Dataset
This is a pairwise GRPO dataset for preference optimization.

</details>
