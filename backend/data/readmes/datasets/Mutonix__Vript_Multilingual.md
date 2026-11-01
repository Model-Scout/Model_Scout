---
task_categories:
- video-classification
- visual-question-answering
- text-to-video
- text-to-image
- image-to-video
language:
- zh
- en
- de
- ja
- ko
- ru
- es
- pt
- jv
- fr
- id
- vi
size_categories:
- 100K<n<1M
configs:
- config_name: bili
  data_files:
  - split: train
    path: vript_CN-V2_captions/vript_CN-V2_captions.jsonl
---
# 🎬 Vript: A Video Is Worth Thousands of Words [[Github Repo](https://github.com/mutonix/Vript)]
---
We construct another **fine-grained** video-text dataset with 19.1K annotated high-resolution UGC videos **(~677k clips)** **<font color=red>in multiple languages</font>** to be the **Vript_Multilingual**. 

**<font color=orange>New in Vript_Multilingual</font>**: 
1. Multilingual: zh (60%), en (17%), de (15%), ja (6%), ko (2%), ru (<1%), es (<1%), pt (<1%), jv (<1%), fr (<1%), id (<1%), vi (<1%)
2. More diverse and fine-grained categories: 113 categories (please check [vript_CN-V2_meta.json](https://huggingface.co/datasets/Mutonix/Vript_Multilingual/blob/main/vript_CN-V2_meta.jsonl))
3. Wider range: from 2011-01 to 2024-06
4. Higher resolution: 1080p
5. Longer duration: > 10 minutes in average
6. More clips: ~677k clips


## Getting Started
**By downloading these datasets, you agree to the terms of the [License](#License).**

The captions of the videos in the Vript_Multilingual dataset are structured as follows:
```
{
    "meta": {
        "video_id": "xxx",
        "video_title": "...",
        "num_clips": ...,
        "integrity": true, 
    },
    "data": {
            "xxx-Scene-001": {
                "video_id": "xxx",
                "clip_id": "xxx-Scene-001",
                "video_title": "...",
                "caption":{
                    "shot_type": "...",
                    "camera_movement": "...",
                    "content": "...",
                    "scene_title": "...",
                },
                "voiceover": ["..."],
            },
            "xxx-Scene-002": {
                ...
            }
        }
}
```
- `video_id`: The ID of the video from YouTube.
- `video_title`: The title of the video.
- `num_clips`: The number of clips in the video. If the `integrity` is `false`, some clips may not be captioned.
- `integrity`: Whether all clips of the video are captioned.
- `clip_id`: The ID of the clip in the video, which is the concatenation of the `video_id` and the scene number.
- `caption`: The caption of the scene, including the shot type, camera movement, content, and scene title.
- `voiceover`: The transcription of the voice-over in the scene.

The data is organized as follows:
```
Vript_Multilingual/
|
├── vript_CN-V2_meta.json
│
├── vript_CN-V2_captions/
│   ├── vript_CN-V2_captions.zip
│   └── vript_CN-V2_captions.jsonl
│
├── vript_CN-V2_videos/
│   ├── CN-V2_video_1_of_224.zip 
│   │   ├── xxx.mp4
│   │   └── ...
│   ├── CN-V2_video_2_of_224.zip
│   └── ...
│
└── vript_CN-V2_clips/
    ├── CN-V2_clips_1_of_224.zip 
    │   ├── xxx/
    │   │   ├── xxx_cut_meta.json
    │   │   ├── xxx_asr.jsonl
    │   │   ├── xxx-Scene-001.mp4
    │   │   └── ...
    │   └── ...
    ├── CN-V2_clips_2_of_224.zip
    └── ...
 

```
- `vript_CN-V2_meta.json`: The meta information of the videos in the Vript_Multilingual dataset, including the video id, title, url, description, category, etc.

- `vript_CN-V2_captions/`: The video captions of the videos in the Vript_Multilingual dataset, which are structured as described above.

- `vript_CN-V2_videos/` (711 GB): The untrimmed videos in the Vript_Multilingual dataset. We divide the whole data into multiple zip files, each containing 200 videos.

- `vript_CN-V2_clips/` (890 GB): The trimmed video clips in the Vript_Multilingual dataset, which correspond to scenes in the `video_CN-V2_captions`. 

- `xxx_cut_meta.json`: The meta information about how the video is trimmed, including the start time, end time, and the duration of the scene.

- `xxx_asr.jsonl`: The transcription of the voice-over in the scene.


## License
By downloading or using the data or model, you understand, acknowledge, and agree to all the terms in the following agreement.

- ACADEMIC USE ONLY

Any content from the Vript-related dataset and Vriptor model is available for academic research purposes only. You agree not to reproduce, duplicate, copy, trade, or exploit for any commercial purposes

- NO DISTRIBUTION

Respect the privacy of personal information of the original source. Without the permission of the copyright owner, you are not allowed to perform any form of broadcasting, modification or any other similar behavior to the data set content.

- RESTRICTION AND LIMITATION OF LIABILITY

In no event shall we be liable for any other damages whatsoever arising out of the use of, or inability to use this dataset and its associated software, even if we have been advised of the possibility of such damages.

- DISCLAIMER

You are solely responsible for legal liability arising from your improper use of the dataset content. We reserve the right to terminate your access to the dataset at any time. You should delete the Vript-related dataset or Vriptor model if required.

This license is modified from the [HD-VG-100M](https://github.com/daooshee/HD-VG-130M) license.


## Citation
```
@misc{yang2024vript,
      title={Vript: A Video Is Worth Thousands of Words}, 
      author={Dongjie Yang and Suyuan Huang and Chengqiang Lu and Xiaodong Han and Haoxin Zhang and Yan Gao and Yao Hu and Hai Zhao},
      year={2024},
      eprint={2406.06040},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

## Contact
**Dongjie Yang**: [djyang.tony@sjtu.edu.cn](djyang.tony@sjtu.edu.cn)

Paper: arxiv.org/abs/2406.06040