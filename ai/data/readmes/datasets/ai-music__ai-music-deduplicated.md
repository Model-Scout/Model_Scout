---
license: mit
task_categories:
  - audio-classification
  - text-to-audio
language:
  - en
  - ko
  - ja
  - zh
tags:
  - music
  - audio
  - ai-music
  - generative-music
  - webdataset
size_categories:
  - 100K-1M
---

# AI Music Deduplicated

A large-scale collection of AI-generated music from five platforms: **Mureka**, **Riffusion**, **Sonauto**, **Suno**, and **Udio**. Each song includes the original audio file and its full platform metadata as a JSON sidecar.

## Overview

| Subset | Songs | Tar Files | Size | Audio Format | Source Platform |
|---|---|---|---|---|---|
| **mureka** | ~312K | 49 | ~981 GB | `.mp3` | [Mureka](https://mureka.ai) |
| **riffusion** | ~105K | 14 | ~266 GB | `.m4a` | [Riffusion](https://riffusion.com) |
| **sonauto** | ~15K | 2 | ~25 GB | `.ogg` | [Sonauto](https://sonauto.ai) |
| **suno** | ~307K | 65 | ~1.3 TB | `.mp3` | [Suno](https://suno.com) |
| **udio** | ~126K | 33 | ~642 GB | `.mp3` | [Udio](https://udio.com) |
| **Total** | **~865K** | **163** | **~3.2 TB** | | |

## Dataset Format

This dataset uses the [WebDataset](https://github.com/webdataset/webdataset) format. Each tar file contains pairs of files sharing the same numeric key:

```
00000000.mp3      # audio file
00000000.json     # metadata JSON
00000001.mp3
00000001.json
...
```

Tar files are capped at ~21 GB each. The directory structure is:

```
mureka/
    mureka_000000.tar
    mureka_000001.tar
    ...
riffusion/
    riffusion_000000.tar
    ...
sonauto/
    sonauto_000000.tar
    sonauto_000001.tar
suno/
    suno_000000.tar
    ...
udio/
    udio_000000.tar
    ...
```

### Loading with WebDataset

```python
import webdataset as wds

dataset = wds.WebDataset("mureka/mureka_000000.tar")
for sample in dataset:
    audio_bytes = sample[".mp3"]          # raw audio bytes
    metadata = json.loads(sample[".json"]) # parsed metadata dict
```

---

## Metadata Columns by Subset

### Mureka (11 fields)

| Column | Type | Description | Example |
|---|---|---|---|
| `uuid` | string | Unique identifier (UUID) | `"144e84c0-c30d-..."` |
| `song_id` | int | Platform song ID | `82035884556290` |
| `title` | string | Song title | `"Tyson's Brilliance"` |
| `version` | string | Generation version | `"2"` |
| `duration in milliseconds` | int | Audio duration in ms | `122117` |
| `generated_at` | int | Unix timestamp (epoch seconds) | `1751796158` |
| `genres` | list[str] | Genre tags | `["pop", "world-music"]` |
| `moods` | list[str] | Mood tags | `["inspired", "calm"]` |
| `model` | string | Model version | `"V6"` |
| `audio_url` | string | Original download URL | `"https://static-cos.mureka.ai/..."` |
| `video_url` | string \| null | Video URL if available | `null` |

### Riffusion (33 fields)

| Column | Type | Description | Example |
|---|---|---|---|
| `id` | string | Unique identifier (UUID) | `"c2df598c-..."` |
| `group_id` | string | Group identifier | `""` |
| `author_id` | string | Author UUID | `"94d1ddac-..."` |
| `created_at` | string | ISO 8601 timestamp | `"2025-07-10T01:59:07Z"` |
| `audio_variation` | null \| object | Audio variation info | `null` |
| `lyrics` | string | Song lyrics | `"[Instrumental]"` |
| `title` | string | Song title | `"Pulse"` |
| `image_override` | null \| string | Custom image override | `null` |
| `sound` | string | Style/genre description | `"trip-hop, male vocals"` |
| `topic` | string | Topic description | `"haunting, atmospheric"` |
| `image_id` | string | Image UUID | `"c2df598c-..."` |
| `simple_waveform` | null \| object | Waveform data | `null` |
| `remix_parent_id` | null \| string | Parent remix ID | `null` |
| `duration_s` | float | Duration in seconds | `173.128` |
| `privacy` | string | Privacy setting | `"public"` |
| `transform` | null \| object | Transform info | `null` |
| `parent_riff_id` | null \| string | Parent riff ID | `null` |
| `audio_upload_id` | null \| string | Audio upload reference | `null` |
| `model_display_name` | string | Model name | `"FUZZ-1.1 Pro"` |
| `is_favorite` | bool | Favorited flag | `false` |
| `favorite_count` | int | Number of favorites | `0` |
| `play_count` | int | Number of plays | `5` |
| `allow_public_use` | bool | Public use allowed | `true` |
| `can_use` | bool | Usable flag | `true` |
| `audio_b64` | null | Always null (audio is in tar) | `null` |
| `image_b64` | null | Always null | `null` |
| `video_id` | null \| string | Video identifier | `null` |
| `seed` | null \| int | Generation seed | `null` |
| `conditions` | list[object] | Prompt conditions | `[{"type":"prompt","value":"..."}]` |
| `lyrics_timestamped` | object | Word-level timestamps | `{"words":[...]}` |
| `audio_url` | string | Original download URL | `"https://storage.googleapis.com/..."` |
| `image_url` | string | Cover image URL | `"https://storage.googleapis.com/..."` |
| `video_url` | null \| string | Video URL | `null` |

### Sonauto (27 fields)

| Column | Type | Description | Example |
|---|---|---|---|
| `id` | string | Unique identifier (UUID) | `"8c6e0e95-..."` |
| `created_at` | string | ISO 8601 timestamp | `"2025-02-07T09:08:15Z"` |
| `title` | string | Song title | `"Mortal Rage"` |
| `song_path` | string | Original audio URL | `"https://cdn.sonauto.ai/..."` |
| `artwork` | string | Artwork identifier | `"clientgen-ad8ace76-..."` |
| `description` | string | User description | `"part 2 of immortal rage"` |
| `artist_id` | string | Artist UUID | `"c4eea79b-..."` |
| `version` | string | Platform version | `"v2"` |
| `likes` | int | Like count | `0` |
| `type` | string | Content type | `"song"` |
| `tags` | list[str] | Genre/style tags | `["electronic", "dark"]` |
| `comments_count` | int | Number of comments | `0` |
| `folllowers` | int | Follower count (note: original typo) | `0` |
| `song_count` | int | Artist's song count | `0` |
| `artwork_bucket_id` | string | Storage bucket | `"images"` |
| `play_count` | int | Play count | `37` |
| `fts` | string | Full-text search tokens | `"'2':4B 'deatslad':8C"` |
| `track_params_id` | string | Track parameters UUID | `"3bfdb080-..."` |
| `lyrics_id` | string | Lyrics UUID | `"88c7217d-..."` |
| `video_path` | string | Video URL | `"https://cdn.sonauto.ai/..."` |
| `track_id` | string | Track UUID | `"1e5515b2-..."` |
| `artist_username` | string | Artist name | `"deatslade"` |
| `user_upload` | bool | User-uploaded flag | `false` |
| `remixed_from` | null \| string | Remix source | `null` |
| `video_artwork_used` | null \| string | Video artwork ref | `null` |
| `artist_artwork` | string \| null | Artist artwork ref | `"clientgen-b67e58df-..."` |
| `keyword` | string | Search keyword | `"mortal"` |

### Suno (27-29 fields, variable)

| Column | Type | Description | Example |
|---|---|---|---|
| `id` | string | Unique identifier (UUID) | `"77ce1eae-..."` |
| `status` | string | Generation status | `"complete"` |
| `title` | string | Song title | `"Cybernetic organism"` |
| `play_count` | int | Play count | `157` |
| `upvote_count` | int | Upvote count | `30` |
| `allow_comments` | bool | Comments enabled | `true` |
| `entity_type` | string | Entity type | `"song_schema"` |
| `audio_url` | string | Audio download URL | `"https://cdn1.suno.ai/...mp3"` |
| `video_url` | string | Video URL | `"https://cdn1.suno.ai/...mp4"` |
| `video_cover_url`* | string | Video cover URL | `"https://cdn1.suno.ai/..."` |
| `preview_url`* | string | Preview URL | `"https://cdn1.suno.ai/..."` |
| `image_url` | string | Cover image URL | `"https://cdn2.suno.ai/...jpeg"` |
| `image_large_url` | string | Large cover image URL | `"https://cdn2.suno.ai/...jpeg"` |
| `major_model_version` | string | Model version | `"v4"` |
| `model_name` | string | Model name | `"chirp-v4"` |
| `metadata` | object | Generation metadata (see below) | `{...}` |
| `is_liked` | bool | Liked flag | `false` |
| `user_id` | string | Creator UUID | `"7b3b6a22-..."` |
| `display_name` | string | Creator display name | `"..."` |
| `handle` | string | Creator handle | `"kommodore404"` |
| `is_handle_updated` | bool | Handle updated flag | `true` |
| `avatar_image_url` | string | Creator avatar URL | `"https://cdn1.suno.ai/...webp"` |
| `is_trashed` | bool | Trashed flag | `false` |
| `created_at` | string | ISO 8601 timestamp | `"2025-02-20T20:55:40Z"` |
| `is_public` | bool | Public flag | `true` |
| `persona`* | object | Persona info | `{...}` |
| `explicit` | bool | Explicit content flag | `false` |
| `comment_count` | int | Comment count | `6` |
| `flag_count` | int | Flag count | `0` |
| `is_contest_clip` | bool | Contest entry flag | `false` |
| `has_hook` | bool | Has hook flag | `false` |

\* = optional, not present in all entries

**`metadata` sub-object:**

| Key | Type | Description | Example |
|---|---|---|---|
| `tags` | string | Comma-separated genre tags | `"Dark Techno, robotic"` |
| `prompt` | string | Lyrics / generation prompt | `"[Chorus]\nWe rise..."` |
| `type` | string | Generation type | `"gen"` |
| `duration` | float | Duration in seconds | `240.0` |
| `refund_credits` | bool | Credits refunded | `false` |
| `stream` | bool | Streaming enabled | `true` |

### Udio (36 fields)

| Column | Type | Description | Example |
|---|---|---|---|
| `id` | string | Unique identifier (UUID) | `"d0e3e1d9-..."` |
| `user_id` | string | Creator UUID | `"5fbac12c-..."` |
| `artist` | string | Artist name | `"Staff"` |
| `artist_image` | string | Artist image URL | `"https://imagedelivery.net/..."` |
| `title` | string | Song title | `"Neon Pulse"` |
| `created_at` | string | ISO 8601 creation time | `"2024-03-31T07:01:36Z"` |
| `error_id` | null \| string | Error identifier | `null` |
| `error_type` | null \| string | Error type | `null` |
| `error_code` | null \| string | Error code | `null` |
| `generation_id` | string | Generation UUID | `"35ddc83f-..."` |
| `image_path` | string | Cover image URL | `"https://imagedelivery.net/..."` |
| `lyrics` | string | Song lyrics | `"..."` |
| `prompt` | string | Generation prompt | `"Electro house, Progressive"` |
| `likes` | int | Like count | `2207` |
| `plays` | int | Play count | `76248` |
| `published_at` | string | ISO 8601 publish time | `"2024-04-08T16:43:31Z"` |
| `replaced_tags` | null \| object | Replaced tags info | `null` |
| `song_path` | string | Original audio URL | `"https://storage.googleapis.com/..."` |
| `tags` | list[str] | Genre/style tags | `["Electro house"]` |
| `duration` | float | Duration in seconds | `95.467` |
| `video_path` | string | Video URL | `"https://storage.googleapis.com/..."` |
| `error_detail` | null \| string | Error detail | `null` |
| `finished` | bool | Generation complete | `true` |
| `liked` | bool | Liked by viewer | `false` |
| `disliked` | bool | Disliked by viewer | `false` |
| `publishable` | bool | Can be published | `true` |
| `audio_conditioning_type` | null \| string | Audio conditioning | `null` |
| `attribution` | string | Attribution text | `""` |
| `description` | string | Song description | `""` |
| `user_tags` | list | User-defined tags | `[]` |
| `original_song_path` | null \| string | Original song ref | `null` |
| `style_source_song_id` | null \| string | Style source song | `null` |
| `style_source_type` | null \| string | Style source type | `null` |
| `style_id` | null \| string | Style identifier | `null` |

---

## Common Fields Across All Subsets

All five subsets share these conceptual fields (under different key names):

| Concept | Mureka | Riffusion | Sonauto | Suno | Udio |
|---|---|---|---|---|---|
| **Unique ID** | `uuid` | `id` | `id` | `id` | `id` |
| **Title** | `title` | `title` | `title` | `title` | `title` |
| **Created** | `generated_at` (unix) | `created_at` (ISO) | `created_at` (ISO) | `created_at` (ISO) | `created_at` (ISO) |
| **Duration** | `duration in milliseconds` (ms) | `duration_s` (sec) | — | `metadata.duration` (sec) | `duration` (sec) |
| **Audio URL** | `audio_url` | `audio_url` | `song_path` | `audio_url` | `song_path` |
| **Tags/Genre** | `genres` (list) | `sound` (string) | `tags` (list) | `metadata.tags` (string) | `tags` (list) |
| **Play Count** | — | `play_count` | `play_count` | `play_count` | `plays` |
| **Lyrics** | — | `lyrics` | — | `metadata.prompt` | `lyrics` |
| **Model** | `model` | `model_display_name` | `version` | `model_name` | — |

## License

This dataset is released under MIT