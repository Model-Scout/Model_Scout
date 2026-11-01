---
pretty_name: Korean-English Web Agent SFT Mixes
language:
- ko
- en
license: odc-by
size_categories:
- 10K<n<100K
tags:
- web-agents
- gui-agents
- supervised-fine-tuning
- multilingual
- korean
configs:
- config_name: mix_ko_en_2080
  data_files: mix_ko_en_2080/training.jsonl
- config_name: mix_ko_en_5050
  data_files: mix_ko_en_5050/training.jsonl
- config_name: ko_only_20k
  data_files: ko_only_20k/training.jsonl
- config_name: en_only_20k
  data_files: en_only_20k/training.jsonl
---

# Korean-English Web Agent SFT Mixes

브라우저 GUI 에이전트 SFT 용 한국어·영어 혼합 데이터. **언어 비율만 다르고 나머지는
동일하게 통제된 4개 구성**이라, 비율이 성능에 미치는 영향을 직접 비교할 수 있다.

## 구성

| config | ko : en | 스텝 | 궤적 |
| --- | --- | ---: | ---: |
| `ko_only_20k` | 10 : 0 | 20,001 | 3,042 |
| `mix_ko_en_5050` | 5 : 5 | 20,008 | 2,663 |
| `mix_ko_en_2080` | 2 : 8 | 20,003 | 2,436 |
| `en_only_20k` | 0 : 10 | 20,009 | 2,274 |

**비율은 궤적 수가 아니라 스텝 수 기준이다.** 스텝 하나가 학습 샘플 하나인데
한국어 궤적은 평균 6.6스텝, 영어는 8.7스텝이라, 궤적 수로 5:5 를 맞추면 실제
gradient 기여가 5:5 가 되지 않는다. 궤적은 절대 쪼개지 않는다.

**네 구성의 표본은 서로 중첩된다.** 시드(42)가 같아 `mix_ko_en_2080` 의 한국어 궤적
593개는 `mix_ko_en_5050` 의 한국어 1,510개에 완전히 포함되고, 5050 의 영어 1,153개는
2080 의 영어 1,843개에 완전히 포함된다. 따라서 구성 간 차이는 표본 추출이 아니라
언어 비율에서만 온다.

## 스키마

각 줄이 스텝 하나다(flat JSONL).

| 필드 | 설명 |
| --- | --- |
| `task` | 자연어 목표 |
| `traj_id` | 궤적 식별자. 앞에 `ko-` / `en-` 접두사가 붙어 소스를 구분한다 |
| `step` | 궤적 내 스텝 번호 |
| `image` | 스크린샷 **상대경로** (아래 "이미지" 참조) |
| `image_source` | `molmoweb` 또는 `koweb` |
| `image_size` | `{"width": …, "height": …}` |
| `thought` | 그 스텝의 사고 (한국어 데이터는 한국어, 영어 데이터는 영어) |
| `action` | 액션 dict — 아래 액션 스페이스 참조 |
| `action_call` | 액션의 문자열 표기 (`action` 과 항상 일치한다) |
| `mix_tag` | `ko` / `en` |

한국어 행에는 수집 파이프라인의 주석(`quality`, `judge_verdict`, `task_cluster` 등)이
추가로 붙어 있다.

## 액션 스페이스 (17종)

모든 행이 이 17종을 따르도록 정규화되어 있다. 좌표는 스크린샷 픽셀, 원점은 좌상단.

| 그룹 | 액션 |
| --- | --- |
| Pointer | `click(x,y)` `double_click(x,y)` `right_click(x,y)` `hover(x,y)` `drag(x,y,x2,y2)` `focus(x,y)` `clear(x,y)` |
| Keyboard | `type(text)` `hotkey(keys)` |
| Viewport / nav | `scroll(dy,dx)` `goto(url)` `go_back()` `go_forward()` |
| Pacing | `wait(seconds)` |
| Termination | `finished(answer)` `fail()` `unknown()` |

실제로 등장하는 것은 `click` `scroll` `type` `hotkey` `goto` `go_back` `wait`
`finished` 이고, 나머지는 사양에는 있으나 이 데이터에는 나타나지 않는다.

정규화에서 적용한 규약 두 가지를 밝혀 둔다.

- `scroll` 은 한국어 원천이 `scroll_dy`/`scroll_dx` 로 기록하던 것을 `dy`/`dx` 로
  통일했다. 값은 그대로다.
- `wait.seconds` 는 원천에 지속시간 정보가 없어 **3.0 으로 채운 규약값**이다.
  복원된 값이 아니다.

## 이미지

**이 리포지토리는 스크린샷을 포함하지 않는다.** `image` 는 소스 루트 기준 상대경로다.

영어 부분(`image_source: molmoweb`)은 공개 원천에서 그대로 복원된다:

```bash
huggingface-cli download allenai/MolmoWeb-SyntheticTrajs \
    --repo-type dataset --local-dir ./MolmoWeb-SyntheticTrajs

python restore_images.py \
    --in  mix_ko_en_2080/training.jsonl \
    --out mix_ko_en_2080/training.local.jsonl \
    --molmoweb-root ./MolmoWeb-SyntheticTrajs
```

한국어 부분(`image_source: koweb`)의 원천 스크린샷은 공개 배포본이 없다. 따라서
한국어를 포함한 세 구성(`ko_only_20k`, `mix_ko_en_5050`, `mix_ko_en_2080`)은 이
리포지토리만으로는 학습에 바로 쓸 수 없다.

## 출처와 라이선스

영어 부분은 [`allenai/MolmoWeb-SyntheticTrajs`](https://huggingface.co/datasets/allenai/MolmoWeb-SyntheticTrajs)
에서 파생했다. 원천은 **ODC-BY 1.0** 이고 이 파생본도 같은 라이선스를 따른다.
원천의 지시문은 Gemini Flash / GPT 계열 모델로 생성되었으므로 각 제공자의 이용약관도
함께 적용된다.

원천에서 두 서브셋을 **의도적으로 제외**했다.

- `node_traversal` — bbox 가 문서 좌표계라 클릭의 68% 가 화면 밖이다.
- `task_seeded_om2w` — Online-Mind2Web 평가 오염 소지.

한국어 부분은 자체 수집한 한국어 웹 에이전트 궤적이다.

## 재현

각 config 디렉터리의 `mix_report.json` 에 시드, 소스별 스텝 예산, 실제 취한 스텝·궤적
수, 화면 밖 좌표로 제외된 궤적 수가 들어 있다.

## 참고 결과

Qwen3.5-9B LoRA SFT (r16/α32, 3 epoch, lr 1e-4) 후 Online-Mind2Web 300 태스크,
30-step, WebJudge 판정:

| 학습 데이터 | MolmoWeb JSON 포맷 | OpenWebRL tool 포맷 |
| --- | ---: | ---: |
| `en_only_20k` | **52.33%** | 36.00% |
| `mix_ko_en_2080` | 38.33% | 40.67% |
| `mix_ko_en_5050` | 37.33% | 40.67% |
| `ko_only_20k` | 16.00% | — |

비율은 선형으로 작동하지 않는다. 한국어를 50%에서 20%로 줄여도 성공률이 움직이지
않고(두 포맷 모두 표준오차 약 4%p 안), 의미 있는 변화는 완전히 뺐을 때만 나타난다.
그 방향조차 포맷에 따라 반대다 — MolmoWeb 포맷에서는 영어 only 가 앞서지만
OpenWebRL 포맷에서는 오히려 가장 낮다.

이 수치는 **영어 웹 태스크 한 벤치마크만** 측정한 것이다. 한국어 데이터가 한국어
웹에서 갖는 값어치는 여기서 측정되지 않는다.
