---
language:
  - ko
license: apache-2.0
task_categories:
  - text-generation
tags:
  - tool-calling
  - function-calling
  - agent
  - korean
  - desktop-automation
  - openmascotai
pretty_name: OpenMascotAI Jarvis (tool-calling, persona-free)
dataset_info:
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
        num_examples: 6585
      - name: eval
        num_examples: 349
      - name: probe
        num_examples: 175
configs:
  - config_name: tools
    default: true
    data_files:
      - split: train
        path: data/tools-train-*
      - split: eval
        path: data/tools-eval-*
      - split: probe
        path: data/probe-*
---

# OpenMascotAI Jarvis — 페르소나 없는 자비스(도구 호출) 데이터셋

## v2 (2026-10-02)

v2는 모든 행을 OpenMascotAI 서버 S12(HEAD 29a67bba)의 **프롬프트 빌더로 다시 조립**한 판이다. 표본 101행(결정 지점
185곳)에서 학습 렌더가 서버 추론 프롬프트(llama-server `/apply-template`)의 정확한 접두사임을 확인했다.
서버 S13(HEAD 8e81815c)의 빌더로 전 행을 다시 조립해도 그대로 일치한다.

| config | split | v1 | v2 |
|---|---|---:|---:|
| `tools` | `train` / `eval` / `probe` | 5,494 / 322 / — | 6,585 / 349 / 175 |

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
  말 되풀이 요청('한 번 더 말해줘' → 도구 없이 직전 답 되풀이) 24. 마무리 답은 프로그램 변주로 같은 문장 비율 11%·고유 뼈대 82%.
- eval은 템플릿 단위로 다시 나눴다(근접 중복 군집 통째로) — train↔eval 근접 중복 0. `probe`(175행)는 **같은 템플릿·하나만 보류**
  (슬롯·결과·발화·문형 중 하나, 행마다 `probe:<종류>` 태그) 일반화 점검용으로 train에서 뺐다. eval·probe id는 이 판에서 고정했다(다음 판도 유지).
- 길이: 8192 토큰을 넘는 행 94개는 전부 PC 기본 구성(`pc_full`·`pc_full_shell`) — `max_seq_length` 9216 이상이어야 학습된다.
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

[OpenMascotAI](https://github.com/MelissaJSM/OpenMascotAI) 데스크톱 마스코트의 **자비스 모드**(마스코트가 윈도우를
실제로 조작하는 모드)를 순정 LLM에 가르치기 위한 한국어 function-calling 데이터셋입니다. 캐릭터 페르소나 데이터셋
(`MelissaJ/ProjectLucia_Hera`의 `tools` config)에서 **캐릭터 요소를 전부 걷어낸** 공개 참고용 판입니다.

| config | split | 행 수 |
|---|---|---:|
| `tools` | `train` / `eval` | 5,494 / 322 |

*A Korean function-calling dataset for the "Jarvis mode" of OpenMascotAI (a desktop mascot that actually operates
Windows). It is the persona-free edition of the character dataset: user names and character vocatives are removed and
every assistant utterance was regenerated by the stock model in a neutral polite tone. Tool schemas, tool calls, and
tool results are unchanged. Use it to teach any Korean-capable base model the tool-calling behaviour, then stack your own
persona on top via the system prompt (or a separate persona LoRA).*

## 무엇이 들어 있나

- 89개 도구(클라이언트가 실행하는 87개 + 서버가 실행하는 `web_search`·`read_webpage`)에 대한 도구 호출 대화.
  도구 정의는 OpenAI function 스키마이며, 각 행에는 정답 도구와 방해 도구가 무작위 순서로 5~15개(일부는 전체 카탈로그) 실린다.
- 종류(`kind`): `tool`(1회 호출→결과→보고) · `multistep`(2~3회 순차 호출) · `chat_with_tools`(도구가 있어도 부르면 안 되는
  잡담·상식·기억 질문) · `ambiguous`(되묻기) · `refusal_or_unsupported`(실패·거부·미지원을 **정직하게** 보고) ·
  `correction`(값 수정·재시도·문맥 되돌리기) · `web_chat` / `web_chat_neg`(자비스 OFF의 일반 채팅 웹 검색 긍정/부정).
- 도구 결과(`tool` 메시지)는 실제 OpenMascotAI 클라이언트가 돌려주는 문자열 포맷을 그대로 재현한 것이다
  (`volume: 55% (muted)`, `launched: notepad.exe`, `{"ok": false, "error": "denied_by_user"}` …).

## 형식

`messages`는 OpenAI 스타일 메시지 배열(JSON 문자열)이다. `system` 메시지는 다음 모양이다.

```
{{PERSONA}}

[자비스 모드]
- 사용자가 컴퓨터에서 무언가를 해 달라고 하면 …(10줄)

[웹 검색]
- 최신 정보·시세·날씨·뉴스·확실하지 않은 사실은 지어내지 말고 web_search로 확인한 뒤 답한다. …(4줄)
```

- **`{{PERSONA}}`** 자리표시자는 학습 스크립트가 자기 시스템 프롬프트로 치환한다. 이 데이터의 답변은 아래 중립 프롬프트로
  생성했으므로, 기본값으로 이 문장을 쓰면 학습/생성이 일치한다.

  ```
  당신은 사용자의 컴퓨터를 대신 다뤄 주는 한국어 비서입니다. 정중하고 간결한 존댓말로 말합니다.
  부탁받은 일은 도구를 호출해 실제로 수행한 뒤 결과를 한두 문장으로 정확하게 보고합니다.
  실패·거부·못 하는 일은 숨기지 않고 그대로 말하고, 하지 않은 일을 했다고 말하지 않습니다.
  사용자에게 이름이나 특정 호칭을 붙이지 않습니다.
  ```
- `[자비스 모드]`·`[웹 검색]` 지시문은 OpenMascotAI 서버(`Core/ai/llm_prompts.py`)가 추론 때 시스템 프롬프트 끝에 붙이는
  원문과 바이트 단위로 같다. 일반 채팅(자비스 OFF) 행은 `{{PERSONA}}` + `[웹 검색]`만 담는다. 일부 행은 `{{PERSONA}}` 뒤에
  서버의 장기 기억 블록(`[기억하고 있는 사실]`)이 들어 있다.
- 웹 도구(`web_search`·`read_webpage`)를 부르는 `assistant` 메시지는 `content`에 **실행 전 한마디**("서울 날씨 찾아보겠습니다.")를
  담고 `tool_calls`를 함께 싣는다. ChatML 계열(Qwen)은 그대로 렌더되고, Gemma 4 템플릿은 content를 tool_call 뒤로 밀기 때문에
  한마디를 별도 assistant 메시지로 앞에 떼어 렌더해야 한다(아래 노트북 참고).
- `final_brief`: 마지막 답변이 담아야 할 사실 요약. `judge_flags`에 `soft:brief_number`가 있으면 brief의 숫자 일부가 답변에
  빠졌다는 뜻이다(행은 유지).
- `final_source`: `stock-neutral`(순정 모델 재생성) 또는 `manual`(재생성 결과가 규칙은 통과했지만 내용이 깨져 수기로 고친 행,
  아래 "만든 방법" 5). 접미 `+name`은 이름 보강 행("만든 방법" 6) — system의 `{{PERSONA}}` 바로 뒤에 OpenMascotAI 서버가
  유저 프로필로 붙이는 블록(`### [대화 하고있는 상대방 X님에 대한 인적 정보]` + `- **성함(혹은 닉네임):** X`)이 들어 있고,
  마지막 답변이 그 이름을 부른다("X님, …" / "…했습니다, X님."). 나머지 행은 이름을 부르지 않는다.

```python
import json
from datasets import load_dataset

ds = load_dataset("MelissaJ/OpenMascotAI_Jarvis", "tools", split="train")
row = ds[0]
messages = json.loads(row["messages"])
tools = json.loads(row["tools"])
messages[0]["content"] = messages[0]["content"].replace("{{PERSONA}}", MY_SYSTEM_PROMPT)
for m in messages:                       # 챗 템플릿은 arguments가 dict여야 한다
    for tc in m.get("tool_calls") or []:
        tc["function"]["arguments"] = json.loads(tc["function"]["arguments"])
text = tokenizer.apply_chat_template(messages, tools=tools, tokenize=False)
```

## 검증 결과(2026-09-09, Qwen3.8-27B LoRA)

이 리비전(이름 보강 포함)으로 `Qwen38_Jarvis_unsloth_gguf.ipynb`를 돌려 만든 LoRA를 순정 `Qwen3.8-27B-UD-Q8_K_L` GGUF에
스케일 8.0으로 얹고, OpenMascotAI 서버의 실측 배터리(`devtools/eval/web_autosearch_battery.py`, 발화는 학습 데이터에 없는
홀드아웃)로 쟀다. 시스템 프롬프트는 캐릭터 컨셉 텍스트 + 서버 유저 프로필 블록(페르소나 LoRA 없음) — 이 데이터셋이 겨냥한
"컨셉만 있는 사용자" 조합이다.

| 모드 | 도구/검색 재현율 | 오호출 | 비고 |
|---|---|---|---|
| 자비스 모드(클라이언트 도구 87 + 웹 2), 2회 | 20/20 · 20/20 | 0/20 · 0/20 | 실행 전 한마디 정상 |
| 일반 채팅(웹 도구만) | 20/20 | 0/20 | 클라이언트 도구 요청엔 "자비스 모드를 켜 주시면" 안내 |
| 프롬프트 속 사용자 이름 보존(40샘플) | 40/40 | — | 이름 보강 전 학습본은 2/40 |

잔여: 한자 단어가 한국어 자리에 섞이는 현상 1~3/40(베이스·스케일 8 조합의 성격, LoRA 종류와 무관), 말투는 중립 존댓말로
고정(캐릭터 말투는 별도 페르소나 LoRA의 몫).

## 학습 노트북

OpenMascotAI 저장소의 `colab_finetune` 노트북 2종이 이 데이터셋만으로 LoRA를 만든다(Unsloth, Colab G4).

- `Qwen38_Jarvis_unsloth_gguf.ipynb` — `unsloth/Qwen3.8-27B`, 일반 LoRA(r=64, rslora), 응답 토큰만 학습.
- `Gemma4_Jarvis_unsloth_gguf.ipynb` — `unsloth/gemma-4-31B-it-qat-q4_0-unquantized`, QAT LoRA. 빈 thought 블록 스캐폴드와
  한마디/tool_call 분리 렌더를 포함한다.

둘 다 병합하지 않고 `*.lora.gguf`로 변환해 순정 GGUF 베이스에 런타임으로 얹는다: `llama-server --lora-scaled <파일>:8.0`.
(스케일 8.0은 rslora r=64·alpha=64의 alpha/√r 보정값이다.)

## 만든 방법

1. 원본: `MelissaJ/ProjectLucia_Hera` `tools` config(2026-09-03 리비전). 발화 템플릿 × 슬롯 풀로 규칙 합성했고, 도구 인자는
   서버 `validate_args`로, 도구 결과 문자열은 클라이언트 C# 구현으로 검증한 데이터다.
2. 사용자 발화의 캐릭터 호격("루시아야, ")을 지우고, 마스코트 자신을 가리키는 이름은 "마스코트"로, 사용자 이름은 "내"로 바꿨다
   (도구 인자·결과의 파일명도 같은 규칙).
3. 어시스턴트 발화(최종 보고·중간 답변·검색 전 한마디)는 **순정 Qwen3.8-27B(LoRA 없음)** 가 위 중립 프롬프트 + `[자비스 모드]`
   `[웹 검색]` 지시문 + 대화 문맥(도구 결과 포함) + `final_brief`를 보고 다시 생성했다. 검증(호칭·한자·줄바꿈·길이·마크다운·
   웃음 표기·규칙 문구 되읽기·"보고 대신 되묻기")을 통과하지 못하면 최대 3회 재생성했고, 끝내 실패한 행은 뺐다.
4. 실측 배터리 발화(OpenMascotAI `devtools/eval/prompts_web.py`)는 정규화 기준으로 학습 데이터에 없다(홀드아웃).
5. **2026-09-07 손질.** 이 데이터로 학습한 LoRA(Qwen3.8-27B)를 실측했더니 규칙 검증은 통과했지만 내용이 깨진 재생성 답변을
   모델이 그대로 외우고 있었다(예: "물도, 물도. 물은 1기압에서…"). 전 행을 다시 훑어 40행을 수기로 고쳤고(`final_source=manual`),
   같은 유형이 다시 들어오지 않도록 검증에 다섯 가지를 추가했다 — 첫 어절 반복(말더듬), "저희" 자칭, "저는 인공지능이라" 같은
   자기 규정(페르소나를 끼워 쓰는 데이터라 어울리지 않는다), "컴퓨터를 직접 다루지 못한다"는 역할 부정, 그리고 **도구를 하나도
   부르지 않은 행에서 "실행하겠습니다/했습니다"라고 말하는 거짓 실행 주장**(일반 채팅 모드에서 클라이언트 도구 요청을 받은
   행은 "지금 모드에서는 할 수 없고 자비스 모드를 켜면 가능"으로 통일). 고친 행의 유형: 채팅 모드 도구 요청 10, 농담·잡담을
   작업 요청으로 오독 17, 자기 규정·역할 부정 7, 창작 거부 1, 말더듬 1, 기타 4.
6. **2026-09-08 이름 보강.** 5의 데이터로 다시 학습한 LoRA는 도구 호출 배터리를 전부 통과했지만, 답변 6,477개 전부가 "사용자를
   이름으로 부르지 않는" 예시라서 페르소나 프롬프트가 이름을 부르라고 하면 그 이름의 다음 토큰이 억눌려 다른 문자 체계로 새는
   결함이 났다(스케일 8.0에서 "멜리사님" 온전 2/40, 스케일 5.0 이하에서 정상). 그래서 행의 12%(train 647·eval 38, 행 id 해시로
   결정)에 위 인적 정보 블록을 넣고 마지막 답변에서 그 이름을 부르게 했다(`final_source` 접미 `+name`). 이름 풀 30개(한국 이름
   20·외래 이름 10)이며 원본 캐릭터의 사용자 이름은 일반화를 재기 위해 일부러 뺐다. 자기 페르소나로 쓰는 사용자는 서버처럼
   페르소나 뒤에 같은 블록을 붙이면 된다.

## 한계

- 합성 데이터라 발화 다양성은 템플릿 조합 범위 안에 있다. 도구 결과는 포맷을 재현한 것이지 실제 실행 결과가 아니다.
- `capture_screen` 행에는 이미지가 없어 비전 왕복은 학습되지 않는다.
- 답변은 중립 존댓말 한 가지 문체다. 캐릭터 말투는 이 데이터의 범위 밖이며 페르소나 LoRA나 시스템 프롬프트로 얹는다.
- 도구 카탈로그는 OpenMascotAI 클라이언트에 맞춘 것이라 다른 앱에서는 도구 이름·인자 스키마를 바꿔 써야 한다.

## 라이선스

Apache-2.0. 데이터 파이프라인은 OpenMascotAI 저장소 `OpenMascotAI_Server/devtools/dataset/step_j_jarvis_only.py`.
