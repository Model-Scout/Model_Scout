---
license: other
language:
  - ko
  - ja
  - en
  - zh
task_categories:
  - text-generation
  - text-to-speech
tags:
  - subculture
  - character-dialogue
  - visual-novel
  - roleplay
  - persona
size_categories:
  - 10K<n<100K
---

# EVAI Assets

Character, story and voice assets for subculture-style AI training and local character-chat
applications. The payload is kept here instead of in the application repository so that the
client stays small and the assets can be fetched on demand.

## Contents

| Path | Files | Size | Description |
| --- | ---: | ---: | --- |
| `data/dataset/` | 285 | 31 MB | Per-character persona profiles, localized dialogue sets and intimacy patterns (JSON / JSONL) |
| `data/eversoul-assets/` | 2,196 | 549 MB | Character portraits and skins, talk backgrounds, story UI frames (PNG) |
| `data/story/` | 94 | 24 MB | Story index, main and bond story scripts with actor placement, stage layout, per-line voice/BGM references and endings (JSON) |
| `data/story-media/voice/` | 63,328 | ~3.2 GB | Korean and Japanese voice lines (OGG Vorbis, mono 24 kHz) |
| `data/story-media/video/` | 547 | ~80 MB | Story cutscenes (MP4) |
| `data/story-media/bgm/` | 338 | 451 MB | Background music (OGG Vorbis, stereo 44.1 kHz) with a localized track index |
| `data/story-media/sfx/` | 1,135 | 26 MB | Ambience and scene sound effects (OGG Vorbis, mono 32 kHz) |

## Layout

```
data/
  dataset/<character>.json
  eversoul-assets/
    backgrounds/talk/<background>.png
    spirits/<folder>/<skin>/<prefix>_1024.png
    ui/story/<element>.png
  story/
    index.json
    main/<chapter>.json
    love/<character>.json
  story-media/
    video/<kind>/<key>/<clip>.mp4
    voice/<kind>/<key>/<ko|ja>/V_[<speaker>_]<lineId>_<KR|JA>.ogg
    bgm/<track>.ogg
    bgm/index.json
    sfx/<effect>.ogg
```

Story scripts carry per-line actor ids, portrait slots, background keys and branch choices. Each
line also names the media it needs, so nothing has to be guessed from a filename pattern:

```json
{
  "id": 250200100,
  "text": { "ko": "...", "en": "...", "zh_tw": "...", "zh_cn": "..." },
  "speaker": 5020,
  "voice": { "ko": "V_Adrianne_250200100_KR", "ja": "V_Adrianne_250200100_JA" },
  "bgm": "BGM_Lazycloud_LOOP",
  "amb": "SFX_AMB_2D_Room01",
  "background": "Talk_BG_Townstreet"
}
```

`voice` values resolve under `data/story-media/voice/<kind>/<key>/<language>/`, `bgm` under
`data/story-media/bgm/`, `amb` under `data/story-media/sfx/`, and `background` under
`data/eversoul-assets/backgrounds/talk/`. `data/story-media/bgm/index.json` lists every track with
its localized title and arrangement credit taken from the game's own string tables.

## Usage

```bash
# everything
hf download garnetrapture/evai-assets --repo-type dataset --local-dir .

# text only
hf download garnetrapture/evai-assets --repo-type dataset --local-dir . \
  --include "data/dataset/*" "data/story/*"

# single voice language
hf download garnetrapture/evai-assets --repo-type dataset --local-dir . \
  --include "data/story-media/voice/*/*/ko/*"

# music only
hf download garnetrapture/evai-assets --repo-type dataset --local-dir . \
  --include "data/story-media/bgm/*"
```

The repository is public, so plain HTTP works without a token:

```bash
curl -sfL -O https://huggingface.co/datasets/garnetrapture/evai-assets/resolve/main/data/story/index.json
```

## Notes

- Text is available in Korean, Japanese, English and Simplified Chinese; voice lines exist in
  Korean and Japanese only. Roughly 55% of script lines are voiced; the rest are narration.
- Audio is transcoded to OGG Vorbis to keep the download small — voice at mono 24 kHz, music at
  stereo 44.1 kHz, effects at mono 32 kHz. It is meant for playback and TTS reference, not for
  mastering.
- Assets are derived from game bundles and are published for research and non-commercial
  personal use. Rights to the original artwork, text and recordings remain with their owners.
