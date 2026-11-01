---
license: cc-by-nc-nd-4.0
language:
- zh
- en
- ja
- ko
viewer: false
---
# gi_cutscn_new

This repository contains cut-scene video files from a certain anime game (a.k.a. GI).

![Release Channel](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fdatasets%2FDeliberatorArchiver%2Fgi_cutscn_new%2Fresolve%2Fmain%2Fversion.json&query=%24.channel&label=Channel) ![Release Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fdatasets%2FDeliberatorArchiver%2Fgi_cutscn_new%2Fresolve%2Fmain%2Fversion.json&query=%24.version&label=Version) ![Official Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fis.gd%2FcDklOb&query=%24.data.game_packages[2].main.major.version&label=Official%20Version)

## Disclaimer

**This resource is released for educational or research purposes only. Copyrights and other rights to this resource belong to their respective copyright holders.**

## About

All cut-scene video files are encoded using HLS streaming technology.

### Details

The original files were extracted directly from the game.

The original file contains one video track and four audio tracks (Chinese, English, Japanese, and Korean). The video track is encoded in VP9 and the audio track is encoded in CRI HCA. All video and audio tracks are packed in CRI USM.

<details>
<summary>Details of encoded video files</summary>

See [Gist](https://gist.github.com/daydreamer-json/8e0f2bf2025db209a9727ad4f2dd983a) for the parameters used during encoding.

|Type|Level|Audio|Resolution|Codec|Color|Max Bitrate|Avg Bitrate|
|---|---|---|---|---|---|---|---|
|Video|L-5|L-2|1920 x 1080|VP9|YUV 4:2:0 8bit BT.601|Copy|Copy|
|Video|L-4|L-1|1920 x 1080|HEVC|YUV 4:2:0 8bit BT.709|12800 kbps|9600 kbps|
|Video|L-3|L-1|1280 x 720|HEVC|YUV 4:2:0 8bit BT.709|6400 kbps|4800 kbps|
|Video|L-2|L-0|854 x 480|HEVC|YUV 4:2:0 8bit BT.709|3600 kbps|2400 kbps|
|Video|L-1|L-0|640 x 360|HEVC|YUV 4:2:0 8bit BT.709|2400 kbps|1600 kbps|
|Video|L-0|L-0|426 x 240|HEVC|YUV 4:2:0 8bit BT.709|1600 kbps|800 kbps|

|Type|Level|Resolution|Codec|Max Bitrate|Avg Bitrate|
|---|---|---|---|---|---|
|Audio|L-2|16bit 48kHz 2ch|FLAC|1536 kbps|Lossless|
|Audio|L-1|16bit 48kHz 2ch|AAC|? kbps|256 kbps|
|Audio|L-0|16bit 48kHz 2ch|AAC|? kbps|128 kbps|
</details>

## Cut-scene Video Links

### See [Links page](lists.md)