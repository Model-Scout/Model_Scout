---
license: cc-by-3.0
language:
- ar
- de
- en
- ko
- ru
- vi
task_categories:
- automatic-speech-recognition
- translation
tags:
- interpreting
- consecutive-interpretation
- interview
- code-switching
- speech-translation
- cabin-offline
pretty_name: Cabin interpreted interviews (CC BY YouTube, pilot)
configs:
- config_name: de-ru
  data_files:
  - split: train
    path:
    - data/de-ru/train-00000-of-00001.parquet
- config_name: de-ru-pairs
  data_files:
  - split: train
    path:
    - data/de-ru-pairs/train-00000-of-00001.parquet
- config_name: en-ar
  data_files:
  - split: train
    path:
    - data/en-ar/train-00000-of-00001.parquet
- config_name: en-ar-pairs
  data_files:
  - split: train
    path:
    - data/en-ar-pairs/train-00000-of-00001.parquet
- config_name: vi-en
  data_files:
  - split: test
    path:
    - data/vi-en/test-00000-of-00001.parquet
- config_name: vi-en-pairs
  data_files:
  - split: test
    path:
    - data/vi-en-pairs/test-00000-of-00001.parquet
- config_name: vi-ko
  data_files:
  - split: train
    path:
    - data/vi-ko/train-00000-of-00001.parquet
- config_name: vi-ko-pairs
  data_files:
  - split: train
    path:
    - data/vi-ko-pairs/train-00000-of-00001.parquet
---

# Cabin interpreted interviews (pilot)

Real **consecutive interpretation** recorded on YouTube: interviews, press conferences and Q&A where a speaker (MC /
journalist / foreign guest) talks in one language and an **interpreter** repeats it in another. Built for the Cabin
Offline app (two-way on-device interpretation): ASR on interpreter-style speech, spoken language ID at turn changes,
turn segmentation and speech-translation pairs. Companion of [doanhlt/cabin-interpreter-interview-test](https://huggingface.co/datasets/doanhlt/cabin-interpreter-interview-test)
(same video ids / `start_sec` / `end_sec` / `lang` / role names `mc`, `guest`, `interpreter`).

**Licence: CC BY 3.0.** Every video was published on YouTube under *Creative Commons Attribution (reuse allowed)* —
checked on its own watch page with yt-dlp on the date in `licence_evidence.jsonl`; videos from
[YODAS2](https://huggingface.co/datasets/espnet/yodas2) (CC BY 3.0) were re-checked on YouTube and dropped if the
uploader has since switched to another licence (kept if still CC BY or no longer online; see `licence`). Attribution for every video (channel, title, URL) is in the table below and `attribution.jsonl`.
Text labels are machine transcripts by our own model (no Gemini / OpenAI / Soniox output anywhere).

## Configs

`<pair>` configs have one row per speech segment; `<pair>-pairs` have one row per source turn + interpreter turn.
Splits are **video-disjoint** (~20 % of videos in `test`, frozen in the build so later versions keep them).

| config | split | videos | segments | hours | hours by language | pairs | pair hours |
|---|---|---|---|---|---|---|---|
| de-ru | train | 1 | 43 | 0.07 | de 0.05, ru 0.02 | 6 | 0.01 |
| en-ar | train | 1 | 193 | 0.27 | ar 0.18, en 0.08 | 4 | 0.02 |
| vi-en | test | 1 | 36 | 0.06 | en 0.03, vi 0.03 | 6 | 0.03 |
| vi-ko | train | 1 | 36 | 0.06 | ko 0.04, vi 0.02 | 5 | 0.03 |

Raw audio hours of videos where two languages were detected, by pair: ar-de 0.15 h, ar-fr 1.02 h, de-fr 0.10 h, de-it 0.04 h, de-ko 0.05 h, de-ru 0.48 h, en-ar 0.66 h, en-de 1.22 h, en-es 0.14 h, en-fr 0.07 h, en-it 0.13 h, en-ja 3.98 h, en-ko 2.61 h, en-th 0.34 h, en-zh 0.38 h, es-it 0.21 h, es-zh 0.47 h, fr-it 0.09 h, fr-ja 0.33 h, it-ko 0.17 h, ja-ko 0.38 h, ja-th 0.04 h, ja-zh 0.40 h, ko-pt 0.03 h, ko-zh 0.22 h, vi-en 0.94 h, vi-es 0.05 h, vi-ko 0.50 h, vi-zh 1.02 h.
Video outcome counts: {'monolingual': 247, 'bilingual_no_interpretation': 78, 'eval_overlap': 2, 'interpreted': 4}.

### Segment columns
`audio` (16 kHz mono FLAC), `video_id`, `url`, `channel`, `channel_id`, `title`, `upload_date`, `licence`, `source`
(youtube / yodas2), `start`, `end` (= `start_sec`, `end_sec`, seconds in the original video), `duration`, `turn_id`,
`speaker_cluster` (per video), `bilingual_speaker` (cluster speaks both languages: usually the interpreter), `lang`,
`lid_p`, `text` (R13x transcript), `caption_text` (YouTube caption over the same span, manual track first, else the
original-language auto track), `caption_kind`, `agree_wer` (interior WER / CER of `text` vs caption), `label_check`
(`agree` or `teacher_only` = no caption to compare), `pair_id`, `role` (`mc` / `guest` / `interpreter`, only inside a
pair), `pair_role` (`speaker` / `interpreter`), `pair_xsim`, `split`.

### Pair columns
`src_audio`, `tgt_audio`, `pair_id`, `video_id`, `url`, `channel`, `licence`, `src_lang`, `tgt_lang`, `src_text`,
`tgt_text`, `xsim` (multilingual MiniLM cosine of the two transcripts), `src_start/end`, `tgt_start/end`,
`src_speaker_cluster`, `tgt_speaker_cluster`, `split`.

## Method
1. **Search** (`search.py`): about 35 interpreter / press-conference queries in vi, en, zh, ja, ko, fr, de, es,
   each as a plain search and with YouTube's Creative Commons filter, plus the seed videos' channels / events (MSI 2019,
   Park Hang-seo press conferences, ...). Every candidate's licence string is read from its watch page; only
   `Creative Commons Attribution license (reuse allowed)`, public, not age-restricted, not live, 2-90 min is kept.
   Sign-language and children's content are excluded by title / tags.
2. **YODAS2 mining** (`yodas_mine.py`): caption text of YODAS2 vi/ko/ja/zh/en/fr/de/es shards scanned for language
   alternation and interpreter keywords; audio taken from YODAS2.
3. **Segmentation** (`segment.py`, CPU): Silero VAD -> segments <= 15 s; VoxLingua107 ECAPA LID (int8, renormalised over
   13 interview languages); SpeechBrain ECAPA speaker embeddings + agglomerative clustering (cosine 0.6). Video pair =
   two dominant languages (2nd >= 8 % of confident speech, else monolingual and dropped); per-segment language
   re-decided inside the pair. Turns = same speaker + language runs; candidate pairs = adjacent turns in different
   languages by different speakers, gap <= 4 s, both >= 1.5 s, length ratio 1/3-3.
4. **Transcription** (GPU): R13x (our Qwen3-ASR-1.7B fine-tune) with the segment language as a hint.
5. **Filters** (`build.py`): caption agreement (WER / CER <= 0.30 when a caption exists, else `teacher_only`), wrong
   teacher language, repetition loops, eval overlap (video ids of all our eval / dev manifests and Vietnamese eval
   transcripts are excluded); a pair is kept only if all its segments pass and `xsim >= 0.5`
   (the interpreter turn really translates the source turn); a video is kept with >= 2 such pairs.

Segment verdicts: {'unlabelled': 6025, 'teacher_only': 1995, 'teacher_lang': 296, 'agree': 249, 'empty': 17, 'cap_length': 50, 'disagree': 144}. Pairs checked 61, kept 22.

## Example pairs
**de-ru (6 pairs)**

- `wx38yRQYgPo_p005` xsim 0.74 [de] Ja, natürlich selbstverständlich. Genau, und dann bringen Sie mir das Dokument einfach wieder, wenn es ausgefüllt ist.
  -> [ru] И потом вы принесете просто документ, когда вы все заполнили.
- `wx38yRQYgPo_p009` xsim 0.69 [ru] до скорой встречи, я вам желаю еще хорошего дня.
  -> [de] Dann beende ich das Gespräch jetzt. Vielen Dank.
- `wx38yRQYgPo_p000` xsim 0.64 [de] Okay, super. Also Sie können sich verstehen, ja?
  -> [ru] Мы понимаем друг друга, да? Да, все понятно.

**en-ar (4 pairs)**

- `W0w-u0Ua3xw_p022` xsim 0.58 [en] You stated earlier that while you were waiting for the cops, you saw someone that looked suspicious to you hanging around the place and looking at your ride. Is that what happened?
  -> [ar] تماماً، حالما أغلقت الهاتف بعد أن تحدثت إلى عامل المقسم، لاحظت بأن رجلاً يرتدي... خيرقا يتسكعون حول سيارتي وينظروا من خلال الشباك.
- `W0w-u0Ua3xw_p007` xsim 0.50 [en] And you said that a deputy was arriving at this time. Did he immediately approach you?
  -> [ar] نعم هذا صحيح. خرج من سيارته. وسأل من اتصل.
- `W0w-u0Ua3xw_p023` xsim 0.51 [en] And you said that a deputy was arriving at this time. Did he immediately approach you?
  -> [ar] نعم هذا صحيح. خرج من سيارته. و سأل من اتصل.

**vi-en (6 pairs)**

- `vcgBfZ5ZN9Y_p006` xsim 0.60 [en] Well, we are just coming to beat everyone game by game. Every game is important, so every game matters, and. We are taking every game as serious as we can, even though. I think we can show a lot stronger performance.
  -> [vi] tất cả những trận đấu tại giải em bé sai này rất là quan trọng cho nên chúng tôi sẽ đánh bại tất cả các đối thủ trên con đường đi của chúng tôi
- `vcgBfZ5ZN9Y_p001` xsim 0.74 [en] Well, I feel good that we are performing kind of well. I think our games can be better. And today I played pretty poorly, so. I want to play better.
  -> [vi] mặc dù chúng tôi rất là vui vì chúng tôi giành được chiến thắng nhưng mà ngày hôm nay tôi thi đấu không được tốt lắm cho nên tôi sẽ cố gắng hơn trong những chiến đấu về sau
- `vcgBfZ5ZN9Y_p002` xsim 0.51 [en] Like just very stupid mistakes, so. Yeah, I think the game was there was not point in game that I felt like we were gonna lose the game. So yeah.
  -> [vi] thực ra thì chúng tôi không nghĩ là chúng tôi sẽ có nhiều khó khăn như vậy đến flashbook nhưng mà bản thân tôi đã mất khá nhiều sai lầm như là dịch chuyển có học lên hay là tóc biến trước mặt tiêm địch và có những giây p

**vi-ko (5 pairs)**

- `C9yjoixv3-E_p005` xsim 0.58 [ko] 응원해 주셔서 정말 감사하고, 열심히 하겠습니다.
  -> [vi] rất cảm ơn mọi người, tôi sẽ xin cố gắng, khai thinh.
- `C9yjoixv3-E_p002` xsim 0.55 [vi] và trong một vài trận đấu khó khăn vừa rồi mà các bạn đã trải qua thì bạn đã có những vị tướng có lẽ như là bạn rất là ít khi sử dụng như là Sona hay là Miss Fortune thì bạn có nghĩ đó thật sự là vấn đề hay không
  -> [ko] 어 최근에 몇 개의 경기에 진행하셨는데 SKT에 조금 힘들었던 경기들이 있었어요. 혹시나 저희 그 자주 쓰지 않는 그 체험 변 때문에 그렇습니까? 혹시 예를 들면 소나타인지 그리고 저희 그 미스트 포티튠 포티튠 인지 그것 때문에 자주 쓰지 않으신. 그 챔피언 때문에 조금 휘들었던 경기 있었는지 혹시 그렇게 좀 얘기할 수 있을까요?
- `C9yjoixv3-E_p004` xsim 0.90 [vi] và như bạn cũng thấy đó là bạn có rất nhiều người hâm mộ ở Việt Nam vậy cuối cùng bạn có lời nào muốn gửi đến họ không?
  -> [ko] 도시다시비. 보시다시피 여기는 베트남 팬이 많이 있다고 보시죠. 혹시 우리 여기에 베트남 팬들한테 하고 싶은 말씀 있으세요?


## Known issues
- Pilot size; speaker clusters are per video and not a real diarizer (overlap not modelled; MC and journalists may
  share a cluster). `role` is a heuristic from pair order + host language.
- `text` is a machine transcript (R13x); `teacher_only` rows had no caption to cross-check.
- Some videos are about interpreting rather than interpreted (lectures, practice tapes); `xsim` + `min_pairs` remove
  most, not all. Language-pair coverage follows what CC BY material exists, which is thin for vi-zh / vi-ja.
- Adults only by intent (children's titles excluded) — no age estimation was run.
- YouTube Terms of Service restrict automated download even for CC-licensed videos; we fetched audio at a low rate,
  without login or cookies. CC BY applies to the uploader's content; if you are the rights holder of a video and want it
  removed, open a discussion on this repo.
- Non-CC interpreted interviews found during search are listed only (no audio) in `eval_candidates_noncc.jsonl`.

## Attribution (CC BY 3.0)

| video | channel | title | source | config | split | licence checked |
|---|---|---|---|---|---|---|
| [C9yjoixv3-E](https://www.youtube.com/watch?v=C9yjoixv3-E) | Channel LOL | [MSI 2019] Phỏng vấn SKT Teddy: " cảm ơn các bạn Việt Nam" | youtube | vi-ko | train | 2026-10-28 |
| [W0w-u0Ua3xw](https://www.youtube.com/watch?v=W0w-u0Ua3xw) | Texan Translation | English-Arabic Consecutive Practice for the State Court Interpreter Oral Exam | youtube | en-ar | train | 2026-10-28 |
| [vcgBfZ5ZN9Y](https://www.youtube.com/watch?v=vcgBfZ5ZN9Y) | Channel LOL | [MSI 2019]  Phỏng vấn Perkz: "chúng tôi sẽ đánh bại mọi đối thủ" | youtube | vi-en | test | 2026-10-28 |
| [wx38yRQYgPo](https://www.youtube.com/watch?v=wx38yRQYgPo) | ZwischenSprachen | Besonderheiten beim Telefondolmetschen | youtube | de-ru | train | 2026-10-28 |
