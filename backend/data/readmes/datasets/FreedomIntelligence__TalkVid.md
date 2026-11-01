---
license: cc-by-nc-4.0
task_categories:
- image-to-video
language:
- en
- zh
- ar
- pl
- de
- ru
- fr
- ko
- pt
- ja
- th
- es
- it
- hi
tags:
- audio-driven
- talking-head-synthesis
- video-generation
- multilingual
- diversity
- large-scale
---

# TalkVid Dataset

This repository hosts the [**TalkVid**](https://github.com/FreedomIntelligence/TalkVid) dataset.

- Paper: [TalkVid: A Large-Scale Diversified Dataset for Audio-Driven Talking Head Synthesis](https://huggingface.co/papers/2508.13618)
- Arxiv paper: https://arxiv.org/abs/2508.13618
- Project Page: https://freedomintelligence.github.io/talk-vid
- GitHub: https://github.com/FreedomIntelligence/TalkVid

## Abstract
Audio-driven talking head synthesis has achieved remarkable photorealism, yet state-of-the-art (SOTA) models exhibit a critical failure: they lack generalization to the full spectrum of human diversity in ethnicity, language, and age groups. We argue that this generalization gap is a direct symptom of limitations in existing training data, which lack the necessary scale, quality, and diversity. To address this challenge, we introduce TalkVid, a new large-scale, high-quality, and diverse dataset containing 1244 hours of video from 7729 unique speakers. TalkVid is curated through a principled, multi-stage automated pipeline that rigorously filters for motion stability, aesthetic quality, and facial detail, and is validated against human judgments to ensure its reliability. Furthermore, we construct and release TalkVid-Bench, a stratified evaluation set of 500 clips meticulously balanced across key demographic and linguistic axes. Our experiments demonstrate that a model trained on TalkVid outperforms counterparts trained on previous datasets, exhibiting superior cross-dataset generalization. Crucially, our analysis on TalkVid-Bench reveals performance disparities across subgroups that are obscured by traditional aggregate metrics, underscoring its necessity for future research. Code and data can be found in this https URL

## Dataset Overview

**TalkVid** is a large-scale and diversified open-source dataset for audio-driven talking head synthesis, featuring:

-   **Scale**: 7,729 unique speakers with over 1,244 hours of HD/4K footage
-   **Diversity**: Covers 15 languages and wide age range (0–60+ years)
-   **Quality**: High-resolution videos (1080p & 2160p) with comprehensive quality filtering
-   **Rich Context**: Full upper-body presence unlike head-only datasets
-   **Annotations**: High-quality captions and comprehensive metadata

**More example videos** can be found in our [🌐 Project Page](https://freedomintelligence.github.io/talk-vid).

### Data Format

```json
{
    "id": "videovideoTr6MMsoWAog-scene1-scene1",
    "height": 1080,
    "width": 1920,
    "fps": 24.0,
    "start-time": 0.1,
    "start-frame": 0,
    "end-time": 5.141666666666667,
    "end-frame": 121,
    "durations": "5.042s",
    "info": {
        "Person ID": "597",
        "Ethnicity": "White",
        "Age Group": "60+",
        "Gender": "Male",
        "Video Link": "https://www.youtube.com/watch?v=Tr6MMsoWAog",
        "Language": "English",
        "Video Category": "Personal Experience"
    },
    "description": "The provided image sequence shows an older man in a suit, likely being interviewed or participating in a recorded conversation. He is seated and maintains a consistent, upright posture. Across the frames, his head rotates incrementally towards the camera's right, suggesting he is addressing someone off-screen in that direction. His facial expressions also show subtle shifts, likely related to speaking or reacting. No significant movements of the hands, arms, or torso are observed.  Because these are still images, any dynamic motion analysis is limited to inferring likely movements from the subtle positional changes between frames.",
    "dover_scores": 8.9,
    "cotracker_ratio": 0.9271857142448425,
    "head_detail": {
        "scores": {
            "avg_movement": 97.92236052453518,
            "min_movement": 89.4061028957367,
            "avg_rotation": 93.79223716779671,
            "min_rotation": 70.42514759667668,
            "avg_completeness": 100.0,
            "min_completeness": 100.0,
            "avg_resolution": 383.14267156972596,
            "min_resolution": 349.6849455656829,
            "avg_orientation": 80.29047955896623,
            "min_orientation": 73.27433271185937
        }
    }
}
```

### Data Statistics

The dataset exhibits excellent diversity across multiple dimensions:

-   **Languages**: English, Chinese, Arabic, Polish, German, Russian, French, Korean, Portuguese, Japanese, Thai, Spanish, Italian, Hindi
-   **Age Groups**: 0–19, 19–30, 31–45, 46–60, 60+
-   **Video Quality**: HD (1080p) and 4K (2160p) resolution with Dover score (mean ≈ 8.55), Cotracker ratio (mean ≈ 0.92), and head-detail scores concentrated in the 90–100 range
-   **Duration Distribution**: Balanced segments from 3-30 seconds for optimal training

## Sample Usage

We provide an easy-to-use inference script for generating talking head videos.

### Environment Setup

```bash
# Create conda environment
conda create -n talkvid python=3.10 -y
conda activate talkvid

# Install dependencies
pip install -r requirements.txt

# Install additional dependencies for video processing
conda install -c conda-forge 'ffmpeg<7' -y
conda install torchaudio==2.4.0 pytorch-cuda=12.1 -c pytorch -c nvidia -y
```

### Model Downloads

Before running inference, download the required model checkpoints:

```bash
# Download the model checkpoints
huggingface-cli download tk93/V-Express --local-dir V-Express
mv V-Express/model_ckpts model_ckpts
mv V-Express/*.bin model_ckpts/v-express
rm -rf V-Express/
```

### Quick Inference

We provide an easy-to-use inference script for generating talking head videos.

#### Command Line Usage

```bash
# Single sample inference
bash scripts/inference.sh

# Or run directly with Python
cd src
python src/inference.py \
    --reference_image_path "./test_samples/short_case/tys/ref.jpg" \
    --audio_path "./test_samples/short_case/tys/aud.mp3" \
    --kps_path "./test_samples/short_case/tys/kps.pth" \
    --output_path "./output.mp4" \
    --retarget_strategy "naive_retarget" \
    --num_inference_steps 25 \
    --guidance_scale 3.5 \
    --context_frames 24
```

## Citation

If our work is helpful for your research, please consider giving a star ⭐ and citing our paper 📝

```bibtex
@misc{chen2025talkvidlargescalediversifieddataset,
      title={TalkVid: A Large-Scale Diversified Dataset for Audio-Driven Talking Head Synthesis}, 
      author={Shunian Chen and Hejin Huang and Yexin Liu and Zihan Ye and Pengcheng Chen and Chenghao Zhu and Michael Guan and Rongsheng Wang and Junying Chen and Guanbin Li and Ser-Nam Lim and Harry Yang and Benyou Wang},
      year={2025},
      eprint={2508.13618},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2508.13618}, 
}
```

## License

### Dataset License
The **TalkVid dataset** is released under [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/), allowing only non-commercial research use.

### Code License
The **source code** is released under [Apache License 2.0](LICENSE), allowing both academic and commercial use with proper attribution.